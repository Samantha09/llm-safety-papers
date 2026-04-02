# Qwen2.5 LoRA 微调 + Ollama 部署完整指南

本文档记录如何将 Qwen2.5 模型通过 LoRA 微调训练角色（以甄嬛为例），并导出到本地 Ollama 运行的完整流程。

> 源文件：飞书文档（2026-03-23）

---

## 目录

- [1. 数据准备](#1-数据准备)
- [2. LoRA 微调训练](#2-lora-微调训练)
- [3. 断点续训](#3-断点续训)
- [4. 导出到 GGUF 格式](#4-导出到-gguf-格式)
- [5. 导入 Ollama](#5-导入-ollama)
- [6. 本地运行](#6-本地运行)

---

## 1. 数据准备

### 数据格式（Alpaca 格式）

```json
{
    "instruction": "小姐，别的秀女都在求中选，唯有咱们小姐想被撂牌子，菩萨一定记得真真儿的——",
    "input": "",
    "output": "嘘——都说许愿说破是不灵的。"
}
```

| 字段 | 说明 |
|------|------|
| instruction | 用户输入/场景描述（对方的台词） |
| input | 额外输入（可选，可为空） |
| output | 期望模型的回答（甄嬛的回应） |

### 加载数据

```python
from datasets import Dataset
import pandas as pd

df = pd.read_json('dataset/huanhuan.json')
ds = Dataset.from_pandas(df)
```

---

## 2. LoRA 微调训练

### 2.1 导入依赖

```python
from transformers import (
    AutoTokenizer, AutoModelForCausalLM,
    DataCollatorForSeq2Seq, TrainingArguments, Trainer
)
from peft import LoraConfig, TaskType, get_peft_model
import torch
```

### 2.2 加载 Tokenizer

```python
model_path = '/root/autodl-tmp/qwen/Qwen2.5-7B-Instruct'
# 或使用小模型：Qwen2.5-0.5B-Instruct, Qwen2.5-1.5B-Instruct, Qwen2.5-3B-Instruct

tokenizer = AutoTokenizer.from_pretrained(
    model_path,
    use_fast=False,
    trust_remote_code=True
)
```

### 2.3 数据预处理

```python
def process_func(example):
    MAX_LENGTH = 384

    # 构建 ChatML 格式对话
    instruction = tokenizer(
        f"<|im_start|>system\n现在你要扮演皇帝身边的女人--甄嬛<|im_end|>\n"
        f"<|im_start|>user\n{example['instruction'] + example['input']}<|im_end|>\n"
        f"<|im_start|>assistant\n",
        add_special_tokens=False
    )

    response = tokenizer(f"{example['output']}", add_special_tokens=False)

    # 拼接输入和输出
    input_ids = instruction["input_ids"] + response["input_ids"] + [tokenizer.pad_token_id]
    attention_mask = instruction["attention_mask"] + response["attention_mask"] + [1]

    # labels：instruction 部分设为 -100（不计算损失），只学习 response
    labels = [-100] * len(instruction["input_ids"]) + response["input_ids"] + [tokenizer.pad_token_id]

    # 截断
    if len(input_ids) > MAX_LENGTH:
        input_ids = input_ids[:MAX_LENGTH]
        attention_mask = attention_mask[:MAX_LENGTH]
        labels = labels[:MAX_LENGTH]

    return {
        "input_ids": input_ids,
        "attention_mask": attention_mask,
        "labels": labels
    }

tokenized_id = ds.map(process_func, remove_columns=ds.column_names)
```

### 2.4 加载基础模型

```python
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    device_map="auto",           # 自动分配 GPU/CPU
    torch_dtype=torch.bfloat16   # 节省显存
)
model.enable_input_require_grads()  # 使用梯度检查点时需要
```

### 2.5 配置 LoRA

```python
from peft import LoraConfig, TaskType, get_peft_model

config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
                    "gate_proj", "up_proj", "down_proj"],
    inference_mode=False,
    r=8,                # LoRA 秩
    lora_alpha=32,      # 缩放因子，缩放比例 = alpha/r = 4
    lora_dropout=0.1
)

model = get_peft_model(model, config)
model.print_trainable_parameters()  # 查看可训练参数比例
```

### 2.6 训练参数配置

```python
args = TrainingArguments(
    output_dir="./output/Qwen2.5_instruct_lora",
    per_device_train_batch_size=4,
    gradient_accumulation_steps=4,      # 有效 batch = 4*4 = 16
    logging_steps=10,
    num_train_epochs=3,
    save_steps=100,                     # 每 100 步保存 checkpoint
    learning_rate=1e-4,
    save_on_each_node=True,
    gradient_checkpointing=True          # 节省显存
)

trainer = Trainer(
    model=model,
    args=args,
    train_dataset=tokenized_id,
    data_collator=DataCollatorForSeq2Seq(tokenizer=tokenizer, padding=True),
)

# 开始训练
trainer.train()
```

---

## 3. 断点续训

### 自动寻找最新 checkpoint

```python
import os

output_dir = "./output/Qwen2.5_instruct_lora"
last_checkpoint = None

if os.path.isdir(output_dir):
    checkpoints = [f for f in os.listdir(output_dir) if f.startswith("checkpoint")]
    if checkpoints:
        last_checkpoint = os.path.join(output_dir, sorted(checkpoints)[-1])
        print(f"找到断点: {last_checkpoint}")

# 传入 resume_from_checkpoint 参数
trainer.train(resume_from_checkpoint=last_checkpoint)
```

### 指定特定 checkpoint

```python
# 从第 200 步继续
trainer.train(resume_from_checkpoint="./output/Qwen2.5_instruct_lora/checkpoint-200")
```

---

## 4. 导出到 GGUF 格式

### 4.1 合并 LoRA 权重

创建 `merge_lora.py`：

```python
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

base_model_path = '/root/autodl-tmp/qwen/Qwen2.5-7B-Instruct'
lora_path = './output/Qwen2.5_instruct_lora/checkpoint-699'  # 修改为你的 checkpoint
output_path = './huanhuan-merged'

print("加载基础模型...")
model = AutoModelForCausalLM.from_pretrained(
    base_model_path,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained(base_model_path, trust_remote_code=True)

print("加载 LoRA 权重...")
model = PeftModel.from_pretrained(model, lora_path)

print("合并权重...")
model = model.merge_and_unload()

print(f"保存到 {output_path}...")
model.save_pretrained(output_path)
tokenizer.save_pretrained(output_path)

print("完成！")
```

运行：

```bash
python merge_lora.py
```

### 4.2 安装 llama.cpp

```bash
git clone https://github.com/ggerganov/llama.cpp.git
cd llama.cpp
pip install -r requirements.txt
```

### 4.3 转换为 GGUF

```bash
# Q4 量化（推荐，约 4GB）
python convert_hf_to_gguf.py ../huanhuan-merged \
    --outfile ../huanhuan-q4.gguf \
    --outtype q4_0

# Q5 量化（约 4.7GB，质量稍好）
python convert_hf_to_gguf.py ../huanhuan-merged \
    --outfile ../huanhuan-q5.gguf \
    --outtype q5_0

# Q8 量化（约 7GB，接近无损）
python convert_hf_to_gguf.py ../huanhuan-merged \
    --outfile ../huanhuan-q8.gguf \
    --outtype q8_0
```

### 量化类型对比

| 类型 | 文件大小 | 质量损失 | 适用场景 |
|------|----------|----------|----------|
| Q4_K_M | ~4GB | 较小 | 推荐，平衡选择 |
| Q5_K_M | ~4.7GB | 轻微 | 质量优先 |
| Q8_0 | ~7GB | 几乎无损 | 追求质量 |

---

## 5. 导入 Ollama

### 创建 Modelfile

```dockerfile
FROM ./huanhuan-q4.gguf

# 推理参数
PARAMETER temperature 0.7
PARAMETER top_p 0.9
PARAMETER top_k 40
PARAMETER num_ctx 4096      # 上下文长度

# 系统提示词（保持角色设定）
SYSTEM """
你是甄嬛，皇帝身边的女人。你说话应当温婉含蓄，带着古典韵味，展现出后宫嫔妃的教养与智慧。
"""

# 使用 ChatML 模板（与训练时一致）
TEMPLATE """{{ if .System }}<|im_start|>system
{{ .System }}<|im_end|>
{{ end }}{{ if .Prompt }}<|im_start|>user
{{ .Prompt }}<|im_end|>
{{ end }}<|im_start|>assistant
"""
```

### 导入并运行

```bash
# 创建模型
ollama create huanhuan -f Modelfile

# 运行
ollama run huanhuan
```

---

## 6. 本地运行

### MacBook M4 16GB 配置

M4 16GB 运行 Q4/Q5 量化模型非常流畅：

| 量化类型 | 内存占用 | 生成速度 | 推荐度 |
|----------|----------|----------|--------|
| Q4_K_M | ~4GB | 20-25 tokens/s | ⭐⭐⭐⭐⭐ |
| Q5_K_M | ~5GB | 15-20 tokens/s | ⭐⭐⭐⭐ |
| Q8_0 | ~7GB | 10-15 tokens/s | ⭐⭐⭐⭐ |

### 针对 M4 优化的 Modelfile

```dockerfile
FROM ./huanhuan-q4.gguf

PARAMETER temperature 0.7
PARAMETER top_p 0.9
PARAMETER num_ctx 4096      # M4 16GB 可以开 4K 上下文
PARAMETER num_thread 4      # 性能核心数

SYSTEM """
你是甄嬛，皇帝身边的女人。说话温婉含蓄，带着古典韵味。
"""

TEMPLATE """{{ if .System }}<|im_start|>system
{{ .System }}<|im_end|>
{{ end }}{{ if .Prompt }}<|im_start|>user
{{ .Prompt }}<|im_end|>
{{ end }}<|im_start|>assistant
"""
```

### 其他设备参考

| 设备配置 | 推荐量化 | 预期表现 |
|----------|----------|----------|
| 显存 8GB+ (RTX 3060/4060) | Q4 | 流畅 |
| 显存 4-6GB | Q4 + 减小 num_ctx | 可用 |
| 无显卡，内存 16GB+ | Q4 CPU 运行 | 较慢但可用 |
| 内存 < 8GB | 换 3B/1.5B 模型 | - |

---

## 常见问题

### 1. 模型太大本机跑不动？

换用小模型重新训练：

```python
# 0.5B、1.5B、3B 都可以选
model_path = '/root/autodl-tmp/qwen/Qwen2.5-3B-Instruct'
```

### 2. 角色扮演效果不像？

- 检查 TEMPLATE 是否与训练时一致（ChatML 格式）
- 尝试更大的模型（7B > 3B）
- 增加 LoRA rank（r=8 → r=32）

### 3. 想修改系统提示词？

Modelfile 中的 SYSTEM 可以随时修改，不需要重新训练：

```dockerfile
SYSTEM """
你是甄嬛，现在已经是太后。说话更有威严，但仍带温婉。
"""
```

---

## 一键脚本

完整导出脚本 `export.sh`：

```bash
#!/bin/bash

set -e

echo "=== Step 1: 合并 LoRA 权重 ==="
python merge_lora.py

echo "=== Step 2: 转换为 GGUF ==="
cd llama.cpp

python convert_hf_to_gguf.py ../huanhuan-merged \
    --outfile ../huanhuan-q4.gguf \
    --outtype q4_0

cd ..

echo "=== Step 3: 创建 Modelfile ==="
cat > Modelfile << 'EOF'
FROM ./huanhuan-q4.gguf

PARAMETER temperature 0.7
PARAMETER top_p 0.9
PARAMETER num_ctx 4096

SYSTEM """
你是甄嬛，皇帝身边的女人。说话温婉含蓄，带着古典韵味。
"""

TEMPLATE """{{ if .System }}<|im_start|>system
{{ .System }}<|im_end|>
{{ end }}{{ if .Prompt }}<|im_start|>user
{{ .Prompt }}<|im_end|>
{{ end }}<|im_start|>assistant
"""
EOF

echo "=== Step 4: 导入 Ollama ==="
ollama create huanhuan -f Modelfile

echo "=== 完成！运行命令：ollama run huanhuan ==="
```

---

## 附录：核心概念

### LoRA 原理

- 冻结原始模型权重，只训练低秩矩阵（A 和 B）
- 可训练参数占比：~0.26%（7B 模型约 2000 万参数）
- 大幅降低显存需求和训练时间

### GGUF 格式

- 包含：模型权重 + 分词器 + 配置 + 元数据
- 支持量化（Q4/Q5/Q8）
- 单文件分发，Ollama/llama.cpp 通用

### ChatML 格式

```
<|im_start|>system
系统提示<|im_end|>
<|im_start|>user
用户输入<|im_end|>
<|im_start|>assistant
模型回复<|im_end|>
```

---

*文档生成时间：2026-03-23*
