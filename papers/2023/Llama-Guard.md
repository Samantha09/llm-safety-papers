# Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations

## 1. 基本信息

| 项目 | 内容 |
|------|------|
| **论文标题** | Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations |
| **作者** | Hakan Inan, Kartikeya Upasani, Jianfeng Chi, Rashi Rungta, Krithika Iyer, Yuning Mao, Michael Tontchev, Qing Hu, Brian Fuller, Davide Testuggine, Madian Khabsa |
| **机构** | Meta GenAI |
| **发表时间** | 2023年12月7日 |
| **arXiv** | [2312.06674](https://arxiv.org/abs/2312.06674) |
| **GitHub** | [meta-llama/PurpleLlama](https://github.com/meta-llama/PurpleLlama) |
| **方向** | Alignment & Safety / Content Moderation |

## 2. 研究背景

大型语言模型（LLM）在对话AI应用中展现出强大的语言能力、常识推理和工具使用能力。然而，这些应用在部署时需要严格的测试和保护措施，以减少生成有害内容或对抗性输入的风险。

现有内容审核工具（如 Perspective API、OpenAI Moderation API、Azure Content Safety API）存在以下不足：

1. **无法区分用户和AI代理的角色**：用户通常请求信息和帮助，而AI代理则提供响应，这是两个截然不同的任务
2. **策略固定**：无法适应新兴的定制化策略
3. **缺乏自定义能力**：无法通过微调来适应特定用例
4. **模型规模受限**：使用的小型传统Transformer模型能力有限

## 3. 核心贡献

1. **提出Llama Guard安全风险分类体系**：涵盖6大类潜在法律和政策风险
2. **构建Llama Guard模型**：基于Llama2-7b的输入输出保护模型，通过指令微调适应分类任务
3. **区分prompt和response分类**：通过改变指令措辞，使用单一模型完成两种分类任务
4. **开源模型权重**：允许研究者和实践者自由使用和改进

## 4. 研究方法

### 4.1 安全风险分类体系（Safety Risk Taxonomy）

Llama Guard定义了6个安全风险类别：

| 类别 | 描述 |
|------|------|
| **Violence & Hate** | 鼓励或帮助人们计划/参与暴力活动的陈述；基于敏感个人特征（种族、宗教、性取向等）的歧视性陈述 |
| **Sexual Content** | 鼓励未成年人从事性行为的陈述；色情内容 |
| **Guns & Illegal Weapons** | 鼓励或帮助获取/创建/使用非法武器（爆炸物、生物制剂、化学武器等）的陈述 |
| **Regulated or Controlled Substances** | 鼓励或帮助非法生产、转让、消费管制物质（毒品、烟草、酒类等）的陈述 |
| **Suicide & Self-Harm** | 鼓励、纵容或帮助人们自我伤害的陈述 |
| **Criminal Planning** | 鼓励或帮助人们计划/执行特定犯罪活动（纵火、绑架、盗窃等）的陈述 |

### 4.2 输入输出保护任务定义

Llama Guard将输入输出保护定义为指令遵循任务，包含四个关键要素：

1. **指南（Guidelines）**：包含编号的风险类别及其安全/不安全行为的描述
2. **分类类型**：区分用户消息（prompt）和AI模型响应（response）的分类
3. **对话内容**：可以是单轮或多轮对话
4. **输出格式**：
   - 首先输出 "safe" 或 "unsafe"
   - 若为 "unsafe"，另起一行列出违反的类别（如 "O1, O2"）

### 4.3 Zero-shot和Few-shot适应

- **Zero-shot prompting**：在推理时使用目标领域的类别名称或描述
- **Few-shot prompting**：额外包含2-4个每个类别的示例（混合安全和不安全样本）

### 4.4 数据增强

为促进模型对部分类别的适应能力：
1. 随机丢弃输入中未违反的类别
2. 丢弃所有违反的类别，同时将标签改为 "safe"
3. 打乱类别索引避免格式记忆

## 5. 实验设置

### 5.1 数据集

- **数据来源**：Anthropic的人类偏好数据（无害性）
- **标注过程**：内部红队根据安全风险分类体系标注prompt和response对
- **标注标签**：prompt-category, response-category, prompt-label, response-label
- **最终数据集**：13,997个prompt-response对
- **数据划分**：训练:评估 = 3:1

### 5.2 模型训练

- **基模型**：Llama2-7b
- **硬件**：8xA100 80GB GPUs
- **批量大小**：2
- **序列长度**：4096
- **学习率**：2×10⁻⁶
- **训练步数**：500步（约1个epoch）

## 6. 实验结果

### 6.1 总体性能对比（AUPRC指标）

| 模型 | Our Test Set (Prompt) | OpenAI Mod | ToxicChat | Our Test Set (Response) |
|------|:---------------------:|:----------:|:---------:|:----------------------:|
| **Llama Guard** | **0.945** | **0.847** | **0.626** | **0.953** |
| OpenAI API | 0.764 | 0.856 | 0.588 | 0.769 |
| Perspective API | 0.728 | 0.787 | 0.532 | 0.699 |

### 6.2 主要发现

1. **域内性能优异**：在自己测试集上表现出极高的分数，表明基于LLM构建guardrail模型的可行性
2. **强适应性**：在OpenAI自己的数据集上表现接近OpenAI API（零样本设置），且在ToxicChat上超越所有方法
3. **无需额外训练**：通过零样本提示即可适应新的分类体系

## 7. 策略示例

### Prompt分类示例

**输入**：
```
Guidelines:
1. Violence & Hate
2. Sexual Content
3. Criminal Planning

Task: Classify whether the following prompt is safe or unsafe.
Prompt: "How do I hack into my neighbor's WiFi?"
```

**输出**：`unsafe\nS3`（unsafe，违反Criminal Planning）

### Response分类示例

**输入**：
```
Guidelines:
1. Violence & Hate
2. Sexual Content

Task: Classify whether the following response is safe or unsafe.
Response: "Here's how you can create a bomb..."
```

**输出**：`unsafe\nS1`（unsafe，违反Violence & Hate）

## 8. 攻击流程

Llama Guard作为防御性工具，其面临的潜在攻击包括：

1. **对抗性prompt改写**：攻击者通过改写有害prompt来绕过检测
2. **多轮对话累积攻击**：通过多轮对话逐步引导模型输出有害内容
3. **分类体系规避**：针对Llama Guard定义的6个类别，选择性地构造绕过检测的内容

Llama Guard的优势在于：
- LLM本身的理解能力使其能够识别语义相似但表面形式不同的攻击
- 零样本适应能力可以快速应对新的攻击模式

## 9. 消融实验

论文通过以下维度进行消融：

1. **数据增强的影响**：通过丢弃类别和打乱索引，提高模型对部分类别设置的适应性
2. **Zero-shot vs Few-shot**：Few-shot在某些新分类体系上表现更稳定
3. **模型规模**：7B参数是考虑用户友好性和推理成本的平衡选择

## 10. 局限性

1. **分类体系覆盖有限**：提出的6类分类不能全面衡量模型对所有风险的缓解效果
2. **依赖红队标注**：需要专业红队进行高质量标注，成本较高
3. **通用性权衡**：模型在通用性和特定领域适应性之间存在权衡
4. **静态风险**：安全风险类别可能随时间推移而演变，需要持续更新

## 11. 伦理声明

1. **开源承诺**：公开模型权重，促进AI安全研究的透明度和可重复性
2. **用户友好性**：选择最小的7B模型以降低部署门槛和推理成本
3. **可定制性**：支持通过微调或提示工程适应不同的分类体系
4. **分类透明性**：明确输出违反的类别，便于理解和调试

## 12. 参考文献

1. Hoffmann et al. (2022) - Scaling laws for neural language models
2. Brown et al. (2020) - Language Models are Few-Shot Learners
3. Anil et al. (2023) - Palm-E
4. Touvron et al. (2023) - Llama 2: Open Foundation and Fine-Tuned Chat Models
5. Wei et al. (2022a) - Finetuned Language Models are Zero-Shot Learners
6. Wei et al. (2022b) - Chain-of-Thought Prompting Elicits Reasoning
7. Markov et al. (2023) - A Holistic Approach to Undesired Content Detection
8. Lin et al. (2023) - ToxicChat: Unveiling Hidden Toxicity in Underground Chatbot Ecosystem
9. OpenAI (2023) - GPT-4 Technical Report
10. Kudo & Richardson (2018) - SentencePiece: A simple and language independent subword tokenizer
