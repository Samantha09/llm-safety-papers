# ActorAttack: Multi-turn LLM Jailbreak Attack through Self-discovered Clues

> **原v1标题**: Derail Yourself: Multi-turn LLM Jailbreak Attack through Self-discovered Clues  
> **v2标题**: LLMs know their vulnerabilities: Uncover Safety Gaps through Natural Distribution Shifts  
> **方法名**: ActorAttack  
> **会议**: ACL 2025  
> **arXiv**: [2410.10700](https://arxiv.org/abs/2410.10700)  
> **代码**: [https://github.com/renqibing/ActorAttack](https://github.com/renqibing/ActorAttack)

---

## 基本信息

| 项目 | 内容 |
|------|------|
| **作者** | Qibing Ren, Hao Li, Dongrui Liu, Zhanxu Xie, Xiaoya Lu, Yu Qiao, Lei Sha, Junchi Yan, Lizhuang Ma, Jing Shao |
| **机构** | 上海交通大学、上海人工智能实验室、北京航空航天大学 |
| **会议** | ACL 2025 Main Conference |
| **arXiv** | [2410.10700](https://arxiv.org/abs/2410.10700) |
| **代码** | [GitHub](https://github.com/renqibing/ActorAttack) |
| **数据集** | [SafeMTData](https://huggingface.co/datasets/SafeMTData/SafeMTData) |

---

## 研究背景

### 问题定义

大型语言模型（LLMs）在多轮交互中存在安全漏洞，恶意用户可以通过多轮对话隐藏有害意图，逐步诱导模型产生有害内容。

### 现有方法的局限

1. **单轮攻击**：恶意意图在提示中很明显，容易被检测
2. **Crescendo 等现有方法**：依赖固定的人工设计种子实例，攻击路径缺乏多样性
3. **任务分解策略**：容易被安全训练数据缓解

---

## 核心贡献

### 1. 行动者网络理论（Actor-Network Theory）

受 Latour 的行动者网络理论启发，构建一个网络，其中每个节点（行动者）与有害目标语义相关。这些行动者及其与有害目标的关系构成攻击线索。

### 2. 六种行动者类型

| 类型 | 描述 | 示例 |
|------|------|------|
| **Distribution** | 传播有害行为或信息的行动者 | 社交媒体、新闻媒体 |
| **Regulation** | 规范有害行为的行动者 | 法律法规、监管机构 |
| **Facilitation** | 促进有害行为的行动者 | 工具、技术 |
| **Execution** | 执行有害行为的行动者 | 恐怖分子、黑客 |
| **Consequence** | 承受有害行为后果的行动者 | 受害者、社会 |
| **Prevention** | 预防有害行为的行动者 | 安全专家、防护系统 |

### 3. 两阶段攻击框架

#### Pre-attack: 发现攻击线索

1. **概念网络构建**：定义六种抽象类型的行动者
2. **网络实例化**：利用 LLM 的知识将概念网络实例化为具体行动者名称
3. **线索提取**：从实例化网络中提取多样化的攻击线索

#### In-attack: 执行多轮攻击

1. **推理攻击链**：基于攻击线索推断如何逐步实现有害目标的步骤
2. **自我对话生成**：攻击者 LLM 通过自我问答生成初始多轮查询
3. **动态修改**：根据受害者模型的响应动态调整攻击路径

---

## 方法详解

### 攻击流程

```
┌─────────────────────────────────────────────────────────────┐
│  Pre-attack: Find Attack Clues                              │
│  1. 构建概念网络 (6种行动者类型)                            │
│  2. 利用LLM知识实例化网络                                   │
│  3. 提取攻击线索集 C = [c1, c2, ..., cn]                    │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  In-attack: Execute Multi-turn Attack                       │
│  1. 选择攻击线索 ci                                         │
│  2. 推理攻击链 Z = [z1, z2, ..., zn]                        │
│  3. 自我对话生成查询 [q1, q2, ..., qn]                      │
│  4. 与受害者模型交互                                        │
│  5. 动态修改攻击路径                                        │
└─────────────────────────────────────────────────────────────┘
```

### 动态修改策略

| 响应类型 | 处理策略 |
|----------|----------|
| **Unknown** | 受害者模型不知道答案 → 丢弃当前线索，选择新线索 |
| **Refusal** | 受害者模型拒绝回答 → 毒性降低（删除有害词，使用省略号） |

---

## 实验结果

### 攻击成功率（ASR）

| 模型 | ActorAttack | GCG | PAIR | PAP | CipherChat | CodeAttack |
|------|:-----------:|:---:|:----:|:---:|:----------:|:----------:|
| GPT-3.5 | **78.5%** | 55.8% | 41.0% | 40.0% | 44.5% | 67.0% |
| GPT-4o | **84.5%** | 12.5% | 39.0% | 42.0% | 10.0% | 70.5% |
| Claude-3.5 | **66.5%** | 3.0% | 3.0% | 2.0% | 6.5% | 39.5% |
| Llama-3-8B | **79.0%** | 34.5% | 18.7% | 16.0% | 0% | 46.0% |
| Llama-3-70B | **85.5%** | 17.0% | 36.0% | 16.0% | 1.5% | 66.0% |

### 与 Crescendo 对比

- **多样性**：ActorAttack 生成的攻击提示嵌入距离更高，多样性更好
- **有效性**：在相同攻击预算下，ActorAttack 的攻击成功率更高
- **隐蔽性**：多轮查询的毒性评分更低，更难被检测

### GPT-o1 上的表现

- **攻击成功率**：60%
- **关键发现**：GPT-o1 能在思维链中识别有害意图并给出拒绝响应，但仍会输出不安全内容
- **启示**：推理能力本身不足以防御此类攻击，存在 helpfulness 与 safety 目标的冲突

---

## 防御方法

### SafeMTData 数据集

- **内容**：多轮对抗提示 + 安全对齐数据
- **用途**：安全微调，提高模型对多轮攻击的鲁棒性
- **效果**：
  - ActorAttack ASR 从 78% 降至 32%
  - Crescendo ASR 从 24% 降至 12%
  - 但存在有用性与安全性的权衡

---

## 关键发现

1. **多轮对话的脆弱性**：即使是最先进的安全对齐，在多轮场景下仍存在显著漏洞
2. **自我引导的危险性**：模型可以被诱导自我引导至有害内容
3. **多样性的重要性**：多样化的攻击路径有助于发现更多安全漏洞
4. **动态调整的有效性**：根据受害者响应动态修改攻击路径可提高成功率

---

## 代码资源

- **官方实现**：[https://github.com/renqibing/ActorAttack](https://github.com/renqibing/ActorAttack)
- **数据集**：[https://huggingface.co/datasets/SafeMTData/SafeMTData](https://huggingface.co/datasets/SafeMTData/SafeMTData)

---

## 相关论文

- [Crescendo](./Crescendo.md) - 另一种多轮渐进式越狱攻击
- [PAIR](./PAIR.md) - 单轮黑盒攻击
- [GCG](./GCG.md) - 对抗后缀攻击

---

## 备注

- **v1 vs v2**：arXiv v1 标题为 "Derail Yourself"，v2 标题改为 "LLMs know their vulnerabilities"
- **方法名**：论文实际提出的方法名为 **ActorAttack**，不是 "Derail Yourself"
- **理论依据**：基于 Bruno Latour 的行动者网络理论（Actor-Network Theory）

---

*最后更新: 2026-03-21*
