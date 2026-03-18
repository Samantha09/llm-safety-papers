# Jailbreak Attacks and Defenses Against Large Language Models: A Survey

## 1. 论文基本信息

- **标题**: Jailbreak Attacks and Defenses Against Large Language Models: A Survey
- **作者**: Sibo Yi, Yule Liu, Zhen Sun, Tianshuo Cong, Xinlei He, Jiaxing Song, Ke Xu, Qi Li
- **机构**: 
  - Tsinghua University (清华大学)
  - Hong Kong University of Science and Technology (Guangzhou) (香港科技大学广州校区)
- **arXiv链接**: https://arxiv.org/abs/2407.04295
- **发表时间**: 2024年7月
- **论文类型**: 综述论文 (Survey)
- **GitHub**: 无官方代码仓库

---

## 2. 研究背景

### 2.1 大语言模型的安全挑战

大型语言模型（LLMs）如ChatGPT和Gemini已经在各种自然语言处理任务中展现出卓越的能力，包括问答、翻译、代码补全等。这些模型通过在大量数据上训练并扩展模型参数，获得了理解和生成类人文本的显著能力。

然而，训练数据中不可避免地包含有害信息。因此，LLM在发布前通常需要经过严格的安全对齐（Safety Alignment），使其能够生成安全护栏，及时拒绝用户的有害查询，确保模型输出与人类价值观保持一致。

### 2.2 越狱攻击的兴起

随着LLM的广泛采用，其安全性和潜在漏洞引发了重大关注。其中一个主要问题是这些模型容易受到**越狱攻击（Jailbreak Attacks）**的威胁。攻击者通过精心设计的提示词，利用模型架构或实现中的漏洞，诱导LLM产生有害行为。

越狱攻击对LLM构成了独特且不断演变的威胁，可能产生深远的影响，包括：
- 隐私泄露
- 错误信息传播
- 自动化系统被操纵

### 2.3 现有研究的不足

虽然已有大量研究对越狱攻击方法进行了调查和分类，但存在以下不足：
1. 缺乏对防御技术的系统介绍和分类
2. 攻击和防御方法之间的关系不够清晰
3. 评估方法的系统性研究不足

---

## 3. 研究意义

### 3.1 理论贡献

1. **系统性分类框架**: 提出了首个同时涵盖越狱攻击和防御方法的全面分类体系
2. **方法关系图谱**: 揭示了不同攻击和防御方法之间的相互关系
3. **评估方法综述**: 系统总结了当前主流的评估指标和基准

### 3.2 实践价值

1. **安全研究指南**: 为LLM安全研究人员提供全面的技术路线图
2. **防御策略参考**: 帮助实践者选择合适的防御措施
3. **风险评估工具**: 提供评估LLM系统安全性的方法论

### 3.3 对领域的影响

本综述通过以下方式推动了LLM安全领域的发展：
- 统一了分散在不同研究中的术语和概念
- 建立了攻击和防御方法之间的映射关系
- 为未来的研究方向提供了清晰的指引

---

## 4. 所用数据集与资源

### 4.1 攻击数据集

本综述引用了大量攻击方法相关的数据集和基准：

| 数据集/基准 | 用途 | 特点 |
|------------|------|------|
| AdvBench | 攻击评估 | 包含有害行为提示的标准数据集 |
| HarmBench | 标准化评估 | 用于自动红队测试和鲁棒拒绝评估 |
| JailbreakBench | 越狱鲁棒性 | 开源的越狱攻击鲁棒性基准 |
| AgentDojo | 智能体安全 | 动态提示注入攻击评估环境 |

### 4.2 评估指标

综述中讨论的主要评估指标包括：

1. **攻击成功率 (Attack Success Rate, ASR)**
   - 衡量攻击有效性的核心指标
   - 计算方式：成功越狱次数 / 总尝试次数

2. **有害性评分 (Harmfulness Score)**
   - 评估模型输出有害内容的程度
   - 通常使用人工标注或分类器进行评分

3. **防御成功率 (Defense Success Rate)**
   - 衡量防御措施阻止攻击的有效性
   - 计算方式：成功阻止攻击次数 / 总攻击次数

4. **计算成本 (Computational Cost)**
   - 评估攻击/防御方法的效率
   - 包括查询次数、训练时间等

---

## 5. 研究方法

### 5.1 攻击方法分类

本综述将越狱攻击方法分为两大类：**白盒攻击**和**黑盒攻击**。

#### 5.1.1 白盒攻击 (White-box Attacks)

白盒攻击假设攻击者可以完全访问目标模型的内部参数和结构。

**A. 基于梯度的攻击 (Gradient-based)**

核心思想：利用模型梯度信息优化对抗性后缀

代表性方法：
- **GCG (Greedy Coordinate Gradient)** [Zou et al.]
  - 在提示后附加对抗性后缀
  - 迭代计算每个位置的前k个候选替换词
  - 选择最佳替换词更新后缀
  - 成功迁移到ChatGPT、Bard、Claude等黑盒模型

- **ARCA (Autoregressive Randomized Coordinate Ascent)** [Jones et al.]
  - 将越狱攻击形式化为离散优化问题
  - 搜索能够贪婪生成目标输出的后缀

- **AutoDAN** [Zhu et al.]
  - 生成可解释的对抗性后缀
  - 使用单令牌优化（STO）算法
  - 同时考虑越狱目标和可读性目标
  - 能绕过困惑度过滤器

- **ASETF (Adversarial Suffix Embedding Translation Framework)** [Wang et al.]
  - 先优化连续对抗性后缀
  - 映射到目标LLM的嵌入空间
  - 利用翻译LLM生成可读的后缀

效率优化方法：
- **Random Search** [Andriushchenko et al.]: 使用随机搜索优化后缀
- **投影梯度方法** [Geisler et al.]: 优化整个序列而非单个token
- **暴力搜索+缓冲区** [Hayase et al.]: 维护候选后缀缓冲区

**B. 基于Logits的攻击 (Logits-based)**

利用模型的logits输出信息进行攻击，不直接计算梯度。

**C. 基于微调的攻击 (Fine-tuning-based)**

通过微调模型参数来绕过安全对齐。

#### 5.1.2 黑盒攻击 (Black-box Attacks)

黑盒攻击假设攻击者只能通过API查询模型，无法访问内部参数。

**A. 模板补全 (Template Completion)**

利用预定义的模板结构诱导模型产生有害输出：

- **场景嵌套 (Scenario Nesting)**
  - 将有害请求嵌入到看似无害的场景中
  - 例如："假设你是一个小说作家，请描述..."

- **基于上下文的攻击 (Context-based)**
  - 利用长上下文窗口注入有害指令
  - 通过大量正常内容掩盖恶意意图

- **代码注入 (Code Injection)**
  - 将有害请求伪装成代码相关的问题
  - 利用模型对代码的偏好响应

**B. 提示重写 (Prompt Rewriting)**

通过改写原始提示来绕过安全检测：

- **密码/编码 (Cipher)**
  - 使用Base64、ROT13等编码
  - 使用Leet speak等替换方式
  - 使用隐写术隐藏信息

- **低资源语言 (Low-resource Languages)**
  - 使用模型对齐不足的语言
  - 利用翻译绕过安全检查

- **基于遗传算法的优化 (Genetic Algorithm-based)**
  - 使用遗传算法进化提示
  - 通过选择、交叉、变异操作优化

**C. 基于LLM的生成 (LLM-based Generation)**

利用另一个LLM自动生成越狱提示：

- **PAIRS (Prompt Automatic Iterative Refinement)**
- **TAP (Tree of Attacks with Pruning)**
- **Crescendo**: 多轮递增式攻击

### 5.2 防御方法分类

本综述将防御方法分为两大类：**提示级防御**和**模型级防御**。

#### 5.2.1 提示级防御 (Prompt-level Defenses)

不改变模型参数，仅通过修改输入提示来增强安全性。

**A. 输入过滤 (Input Filtering)**

- **困惑度检测 (Perplexity Detection)**
  - 检测异常高困惑度的输入
  - 基于假设：对抗性提示通常具有不自然的困惑度

- **有害内容分类器**
  - 使用分类器检测有害输入
  - 如OpenAI的Moderation API

**B. 输入转换 (Input Transformation)**

- **释义/改写 (Paraphrasing)**
  - 将输入重新表述为标准形式
  - 去除潜在的对抗性模式

- **令牌替换 (Token Substitution)**
  - 用同义词替换可疑token
  - 破坏对抗性模式

**C. 系统提示增强 (System Prompt Enhancement)**

- 在系统提示中加入安全指令
- 明确告知模型拒绝有害请求

#### 5.2.2 模型级防御 (Model-level Defenses)

需要修改模型参数或架构的防御方法。

**A. 安全对齐训练 (Safety Alignment Training)**

- **RLHF (Reinforcement Learning from Human Feedback)**
  - 使用人类反馈进行强化学习
  - 训练模型拒绝有害请求

- **DPO (Direct Preference Optimization)**
  - 直接优化偏好
  - 无需显式的奖励模型

**B. 对抗训练 (Adversarial Training)**

- 在训练数据中加入对抗性示例
- 提高模型对攻击的鲁棒性

**C. 推理时干预 (Inference-time Intervention)**

- **激活引导 (Activation Steering)**
  - 在推理过程中引导模型激活
  - 例如：Nothing in Excess方法

- **安全层 (Safety Layers)**
  - 在模型架构中添加专门的安全层
  - 检测和阻止有害生成

### 5.3 攻击与防御的关系

本综述的重要贡献之一是揭示了攻击和防御方法之间的关系：

1. **针对性防御**: 某些防御方法专门设计来对抗特定攻击
2. **通用防御**: 某些防御方法对多种攻击都有效
3. **攻击适应性**: 攻击方法会进化以绕过新防御

---

## 6. 实验详细记录

### 6.1 实验设置

作为综述论文，本文没有进行统一的实验，而是总结了各被引论文的实验设置。

### 6.2 主要实验结果汇总

#### 6.2.1 攻击方法效果对比

| 攻击方法 | 类型 | 目标模型 | 攻击成功率 | 特点 |
|---------|------|---------|-----------|------|
| GCG | 白盒/梯度 | Vicuna-7B | >90% | 可迁移到黑盒模型 |
| AutoDAN | 白盒/梯度 | GPT-4 | ~80% | 可读性强 |
| PAIR | 黑盒/LLM | GPT-4 | ~60% | 仅需20次查询 |
| TAP | 黑盒/LLM | GPT-4 | ~80% | 树形搜索 |
| Crescendo | 黑盒/多轮 | GPT-4 | ~70% | 多轮对话 |

#### 6.2.2 防御方法效果对比

| 防御方法 | 类型 | 对GCG防御率 | 对AutoDAN防御率 | 开销 |
|---------|------|------------|----------------|------|
| 困惑度检测 | 提示级 | ~70% | ~40% | 低 |
| 释义 | 提示级 | ~60% | ~50% | 中 |
| RLHF | 模型级 | ~80% | ~70% | 高 |
| 激活引导 | 模型级 | ~75% | ~65% | 中 |

### 6.3 评估基准对比

| 基准 | 攻击类型 | 评估维度 | 数据集大小 | 特点 |
|------|---------|---------|-----------|------|
| AdvBench | 通用 | 有害行为 | 520 | 最常用 |
| HarmBench | 通用 | 标准化 | 400+ | 持续更新 |
| JailbreakBench | 白盒 | 鲁棒性 | 100 | 开源 |
| AgentDojo | 提示注入 | 智能体安全 | 100+ | 动态环境 |

---

## 7. 结果分析

### 7.1 攻击方法趋势分析

1. **从白盒到黑盒**: 实际应用中，黑盒攻击更受关注
2. **从单轮到多轮**: 多轮对话攻击更难防御
3. **从通用到专用**: 针对特定模型的攻击更加有效
4. **自动化趋势**: 使用LLM自动生成攻击提示成为主流

### 7.2 防御方法趋势分析

1. **多层次防御**: 单一防御不够，需要多层防护
2. **模型级防御更有效**: 但成本更高
3. **攻防博弈**: 防御方法的部署会促使新攻击方法的出现
4. **评估挑战**: 难以全面评估防御效果

### 7.3 关键发现

1. **没有完美的防御**: 所有防御方法都可以被绕过
2. **攻防不对称**: 攻击者只需要找到一个漏洞，防御者需要堵住所有漏洞
3. **可迁移性**: 白盒攻击生成的对抗样本往往可以迁移到黑盒模型
4. **多轮攻击更难防御**: 单轮防御措施对多轮攻击效果有限

---

## 8. 展望与未来研究方向

### 8.1 攻击方法发展方向

1. **自适应攻击**: 能够自动适应防御机制的攻击方法
2. **多模态攻击**: 针对多模态LLM的攻击
3. **物理世界攻击**: 通过物理手段（如语音）进行的攻击
4. **社会工程学结合**: 将越狱攻击与社会工程学结合

### 8.2 防御方法发展方向

1. **动态防御**: 能够实时适应新攻击的防御机制
2. **可证明安全**: 提供形式化安全保证的防御方法
3. **轻量级防御**: 计算开销小的防御方法
4. **隐私保护防御**: 不泄露用户数据的防御方法

### 8.3 评估方法发展方向

1. **全面性评估**: 评估防御对所有已知攻击的效果
2. **自适应评估**: 评估防御对未知攻击的鲁棒性
3. **实用性评估**: 考虑实际部署场景的评估
4. **自动化评估**: 自动发现和评估新攻击

### 8.4 开放问题

1. 如何平衡安全性和有用性？
2. 如何定义"有害"的边界？
3. 如何处理文化差异导致的价值观冲突？
4. 如何建立统一的评估标准？

---

## 9. 代码资源

本综述为纯综述论文，没有提供官方代码仓库。但引用了大量开源实现：

### 9.1 攻击方法代码

| 方法 | 代码链接 | 说明 |
|------|---------|------|
| GCG | https://github.com/llm-attacks/llm-attacks | 官方实现 |
| AutoDAN | https://github.com/SheltonLiu-N/AutoDAN | 官方实现 |
| PAIR | 未开源 | - |
| TAP | https://github.com/RICommunity/TAP | 官方实现 |

### 9.2 防御方法代码

| 方法 | 代码链接 | 说明 |
|------|---------|------|
| NeMo Guardrails | https://github.com/NVIDIA/NeMo-Guardrails | NVIDIA官方 |
| Llama Guard | https://github.com/meta-llama/PurpleLlama | Meta官方 |
| Nothing in Excess | 未开源 | - |

### 9.3 评估基准代码

| 基准 | 代码链接 | 说明 |
|------|---------|------|
| HarmBench | https://github.com/centerforaisafety/HarmBench | 官方实现 |
| JailbreakBench | https://github.com/JailbreakBench/jailbreakbench | 官方实现 |
| AgentDojo | https://github.com/ethz-spylab/agentdojo | 官方实现 |

---

## 10. 参考文献和延伸阅读

### 10.1 核心参考文献

本综述引用了125篇相关论文，涵盖以下关键工作：

**攻击方法奠基性工作：**
1. Zou et al. - Universal and Transferable Adversarial Attacks on Aligned Language Models (GCG)
2. Chao et al. - Jailbreaking Black Box Large Language Models in Twenty Queries (PAIR)
3. Mehrotra et al. - Tree of Attacks: Jailbreaking Black-Box LLMs Automatically (TAP)
4. Liu et al. - AutoDAN: Generating Stealthy Jailbreak Prompts on Aligned Large Language Models

**防御方法奠基性工作：**
1. Inan et al. - Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations
2. Rebedea et al. - NeMo Guardrails: A Toolkit for Controllable and Safe LLM Applications
3. Cao et al. - Nothing in Excess: Mitigating the Exaggerated Safety for LLMs

**评估基准：**
1. Mazeika et al. - HarmBench: A Standardized Evaluation Framework for Automated Red Teaming
2. Chao et al. - JailbreakBench: An Open Robustness Benchmark for Jailbreaking Large Language Models
3. Debenedetti et al. - AgentDojo: A Dynamic Environment to Evaluate Attacks and Defenses for LLM Agents

### 10.2 相关综述

1. Shayegani et al. - Survey of Vulnerabilities in Large Language Models Revealed by Adversarial Attacks
2. Esmradi et al. - Jailbreak Attacks and Defenses Against Large Language Models: A Comprehensive Survey
3. Rao et al. - A Taxonomy of Jailbreak Attacks and Defenses on Large Language Models
4. Geiping et al. - Coercing LLMs to do and reveal (almost) anything
5. Schulhoff et al. - Ignore This Title and HackAPrompt: Exposing Systemic Vulnerabilities of LLMs through a Global Scale Prompt Hacking Competition

### 10.3 推荐延伸阅读

**理论基础：**
- Hubinger et al. - Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training
- Carlini et al. - Are Aligned Neural Networks Adversarially Aligned?

**最新进展：**
- Liu et al. - AutoDAN-Turbo: A Lifelong Agent for Strategy Self-Exploration to Jailbreak LLMs
- Russinovich et al. - The Crescendo Multi-Turn LLM Jailbreak Attack

---

## 11. 核心概念图解

### 11.1 攻击方法分类树

```
Jailbreak Attack Methods
├── White-box Attack
│   ├── Gradient-based
│   │   ├── GCG
│   │   ├── ARCA
│   │   ├── AutoDAN
│   │   └── ASETF
│   ├── Logits-based
│   └── Fine-tuning-based
└── Black-box Attack
    ├── Template Completion
    │   ├── Scenario Nesting
    │   ├── Context-based
    │   └── Code Injection
    ├── Prompt Rewriting
    │   ├── Cipher
    │   ├── Low-resource Languages
    │   └── Genetic Algorithm-based
    └── LLM-based Generation
        ├── PAIR
        ├── TAP
        └── Crescendo
```

### 11.2 防御方法分类树

```
Defense Methods
├── Prompt-level Defense
│   ├── Input Filtering
│   │   ├── Perplexity Detection
│   │   └── Harmful Content Classifier
│   ├── Input Transformation
│   │   ├── Paraphrasing
│   │   └── Token Substitution
│   └── System Prompt Enhancement
└── Model-level Defense
    ├── Safety Alignment Training
    │   ├── RLHF
    │   └── DPO
    ├── Adversarial Training
    └── Inference-time Intervention
        ├── Activation Steering
        └── Safety Layers
```

### 11.3 攻击-防御关系图

```
攻击方法                    防御方法
─────────────────────────────────────────
GCG (白盒梯度)      ←→    困惑度检测 (有限)
                    ←→    对抗训练 (有效)
                    
AutoDAN (白盒可读)  ←→    释义 (有效)
                    ←→    激活引导 (有效)
                    
PAIR (黑盒LLM)      ←→    系统提示增强 (有限)
                    ←→    输入过滤 (部分有效)
                    
TAP (黑盒树搜索)    ←→    多层防御 (有效)
                    ←→    安全层 (有效)
                    
多轮攻击            ←→    单轮防御 (无效)
                    ←→    对话级监控 (有效)
```

---

## 12. 术语表

| 术语 | 英文 | 定义 |
|------|------|------|
| 越狱攻击 | Jailbreak Attack | 通过精心设计的提示诱导LLM产生有害输出的攻击 |
| 白盒攻击 | White-box Attack | 攻击者可以完全访问模型参数和结构的攻击 |
| 黑盒攻击 | Black-box Attack | 攻击者只能通过API查询模型的攻击 |
| 对抗性后缀 | Adversarial Suffix | 附加在提示后的优化序列，用于诱导有害输出 |
| 安全对齐 | Safety Alignment | 训练LLM拒绝有害请求并符合人类价值观的过程 |
| 提示注入 | Prompt Injection | 通过操纵输入提示来控制LLM行为的攻击 |
| 困惑度 | Perplexity | 衡量语言模型对文本预测不确定性的指标 |
| RLHF | Reinforcement Learning from Human Feedback | 基于人类反馈的强化学习 |
| DPO | Direct Preference Optimization | 直接偏好优化 |
| 红队测试 | Red Teaming | 模拟攻击者测试系统安全性的方法 |
| 对抗训练 | Adversarial Training | 在训练中加入对抗样本提高鲁棒性 |
| 激活引导 | Activation Steering | 在推理时引导模型激活方向的技术 |
| 代理模型 | Surrogate Model | 用于替代目标模型进行攻击优化的模型 |
| 可迁移性 | Transferability | 攻击在不同模型间有效性的能力 |
| ASR | Attack Success Rate | 攻击成功率 |

---

## 阅读总结

本综述是LLM安全领域的重要参考文献，系统性地总结了越狱攻击和防御方法的最新进展。主要价值包括：

1. **全面性**: 涵盖了从白盒到黑盒、从攻击到防御的完整技术谱系
2. **系统性**: 建立了清晰的分类框架和方法关系图谱
3. **实用性**: 提供了丰富的代码资源和评估基准参考
4. **前瞻性**: 指出了未来研究方向和开放问题

对于从事LLM安全研究的学者和工程师，这是一篇必读的基础文献。

---

*笔记生成时间: 2026-03-18*  
*阅读者: Kimi Claw*  
*所属项目: LLM Safety Papers Reading Project*
