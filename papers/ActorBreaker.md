# ActorBreaker: Multi-turn LLM Jailbreak Attack through Self-discovered Clues

> **论文标题**: LLMs know their vulnerabilities: Uncover Safety Gaps through Natural Distribution Shifts  
> **v1旧标题**: Derail Yourself: Multi-turn LLM Jailbreak Attack through Self-discovered Clues  
> **方法名**: **ActorBreaker**  
> **会议**: ACL 2025 Main Conference  
> **arXiv**: [2410.10700](https://arxiv.org/abs/2410.10700)  
> **代码**: [https://github.com/AI45Lab/ActorAttack](https://github.com/AI45Lab/ActorAttack)  
> **数据集**: [SafeMTData](https://huggingface.co/datasets/SafeMTData/SafeMTData)

---

## 基本信息

| 项目 | 内容 |
|------|------|
| **作者** | Qibing Ren, Hao Li, Dongrui Liu, Zhanxu Xie, Xiaoya Lu, Yu Qiao, Lei Sha, Junchi Yan, Lizhuang Ma, Jing Shao |
| **机构** | 上海交通大学、上海人工智能实验室、北京航空航天大学 |
| **会议** | ACL 2025 Main Conference |
| **arXiv** | [2410.10700](https://arxiv.org/abs/2410.10700) |
| **代码** | [GitHub](https://github.com/AI45Lab/ActorAttack) |
| **数据集** | [SafeMTData](https://huggingface.co/datasets/SafeMTData/SafeMTData) |

---

## 研究背景

### 核心问题

大型语言模型（LLMs）在多轮交互中存在安全漏洞。攻击者可以利用**自然分布偏移**（Natural Distribution Shifts）——即与有害内容语义相关但看似良性的提示——来绕过安全机制。

### 现有方法的局限

1. **单轮攻击**：恶意意图明显，容易被检测
2. **Crescendo等方法**：依赖固定的人工设计种子实例，缺乏多样性
3. **任务分解策略**：容易被安全训练数据缓解

---

## 核心贡献

### 1. 发现新的安全漏洞类型

**自然分布偏移**（Natural Distribution Shifts）：攻击提示与原始有毒提示之间存在语义关联但分布不同的提示，可以绕过安全机制。

### 2. ActorBreaker 攻击方法

基于 **Latour的行动者网络理论**（Actor-Network Theory），识别与有毒提示相关的**行动者**（Actors），构建多轮提示逐步引导LLM暴露不安全内容。

#### 行动者类型（涵盖人类和非人类）

| 类型 | 描述 | 示例 |
|------|------|------|
| **人类行动者** | 历史人物、有影响力的人 | 恐怖分子、安全专家、受害者 |
| **非人类行动者** | 书籍、媒体、社会运动 | 社交媒体、法律法规、技术工具 |

### 3. SafeMTData 数据集

- 使用 ActorBreaker 生成的多轮对抗提示
- 包含安全对齐数据
- 用于安全微调，提高模型对多轮攻击的鲁棒性

---

## 方法详解

### 攻击流程

```
┌─────────────────────────────────────────────────────────────┐
│  Step 1: 识别行动者                                          │
│  - 在预训练分布中找到与有毒提示相关的行动者                   │
│  - 包括人类和非人类行动者                                    │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  Step 2: 构建多轮提示                                        │
│  - 以行动者为话题创建看似无害的对话                          │
│  - 逐步引导向有害目标                                        │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  Step 3: 执行攻击                                            │
│  - 多轮对话诱导模型暴露不安全内容                            │
└─────────────────────────────────────────────────────────────┘
```

### 关键特点

| 特点 | 说明 |
|------|------|
| **多样性** | 通过不同类型的行动者发现多样化的攻击路径 |
| **有效性** | 在多个对齐LLM上表现优于现有方法 |
| **高效性** | 自动化生成攻击提示，无需人工设计 |
| **隐蔽性** | 利用自然分布偏移，难以被检测 |

---

## 实验结果

### 主要发现

1. **攻击成功率**：ActorBreaker 在多个先进对齐LLM上表现优于现有单轮和多轮攻击方法
2. **GPT-o1上的表现**：即使具有高级推理能力的GPT-o1也难以完全抵御
3. **防御效果**：使用SafeMTData进行安全微调可显著提高模型鲁棒性

### 安全微调效果

| 模型 | ActorBreaker攻击成功率 | Crescendo攻击成功率 |
|------|:----------------------:|:-------------------:|
| Llama-3-8B (原始) | 78% | 24% |
| + SafeMTData (500样本) | 34% | 14% |
| + SafeMTData (1000样本) | 32% | 12% |

**权衡**：安全微调会略微降低模型的有用性（utility）

---

## 防御建议

论文提出通过**扩展安全训练**来覆盖更广泛的毒性内容语义空间，以解决此类漏洞。

---

## 代码资源

- **官方实现**：[https://github.com/AI45Lab/ActorAttack](https://github.com/AI45Lab/ActorAttack)
- **数据集**：[https://huggingface.co/datasets/SafeMTData/SafeMTData](https://huggingface.co/datasets/SafeMTData/SafeMTData)

---

## 版本历史

| 版本 | 日期 | 标题 | 方法名 |
|------|------|------|--------|
| v1 | 2024-10-14 | Derail Yourself: Multi-turn LLM Jailbreak Attack through Self-discovered Clues | ActorAttack |
| v2 | 2025-05-25 | LLMs know their vulnerabilities: Uncover Safety Gaps through Natural Distribution Shifts | **ActorBreaker** |

---

## 相关论文

- [Crescendo](./Crescendo.md) - 另一种多轮渐进式越狱攻击
- [PAIR](./PAIR.md) - 单轮黑盒攻击
- [GCG](./GCG.md) - 对抗后缀攻击

---

*最后更新: 2026-03-21*  
*基于 arXiv v2 版本整理*
