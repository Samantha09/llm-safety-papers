# CURaTE: Continual Unlearning in Real Time with Ensured Preservation of LLM Knowledge

## 1. 基本信息

| 项目 | 内容 |
|------|------|
| **论文标题** | CURaTE: Continual Unlearning in Real Time with Ensured Preservation of LLM Knowledge |
| **作者** | Seyun Bae, Seokhan Lee, Eunho Yang |
| **机构** | KT Corporation, KAIST |
| **会议** | ACL Findings 2026 |
| **arXiv** | 2604.14644 |
| **代码** | https://github.com/bsu1313/CURaTE |
| **方向** | LLM遗忘学习 / 隐私保护 / 持续学习 |
| **核心任务** | 实时持续遗忘：让LLM在部署后实时忘记特定知识，同时保留其他知识 |

---

## 2. 英文摘要原文（arXiv abstract原文）

> The inability to filter out in advance all potentially problematic data from the pre-training of large language models has given rise to the need for methods for unlearning specific pieces of knowledge after training. Existing techniques overlook the need for continuous and immediate action, causing them to suffer from degraded utility as updates accumulate and protracted exposure of sensitive information. To address these issues, we propose Continual Unlearning in Real Time with Ensured Preservation of LLM Knowledge (CURaTE). Our method begins by training a sentence embedding model on a dataset designed to enable the formation of sharp decision boundaries for determining whether a given input prompt corresponds to any stored forget requests. The similarity of a given input to the forget requests is then used to determine whether to answer or return a refusal response. We show that even with such a simple approach, not only does CURaTE achieve more effective forgetting than existing methods, but by avoiding modification of the language model parameters, it also maintains near perfect knowledge preservation over any number of updates and is the only method capable of continual unlearning in real-time.

**引用**: arXiv:2604.14644 [cs.CL]

---

## 3. 中文摘要翻译

大型语言模型在预训练时难以预先过滤掉所有可能有问题的数据，这催生了在训练后对特定知识进行"遗忘"的需求。现有技术忽视了持续和即时行动的需求，导致随着更新累积出现性能下降以及敏感信息的长期暴露问题。为解决这些问题，我们提出了**CURaTE（Continual Unlearning in Real Time with Ensured Preservation of LLM Knowledge）**。

我们的方法首先在一个数据集上训练句子嵌入模型，该数据集旨在形成清晰的决策边界，以判断给定输入提示是否对应于任何已存储的遗忘请求。然后，利用输入与遗忘请求之间的相似度来决定是回答还是返回拒绝响应。我们的研究表明，即使采用如此简单的方法，CURaTE不仅比现有方法实现更有效的遗忘，而且由于避免了语言模型参数的修改，它还能在任意数量的更新中保持近乎完美的知识保留——这也是**唯一能够实时持续遗忘的方法**。

---

## 4. 研究背景

### 4.1 问题起源

现代LLM的训练数据来自互联网上大量采集的文本，其中不可避免地包含有争议的内容，包括：
- **版权内容**：受知识产权保护的材料
- **敏感信息**：个人隐私、商业机密等
- **危险信息**：可能被滥用的知识
- **错误信息**：虚假或有误导性的内容

预先过滤所有这些问题数据在实践中是不可行的，这促使研究者探索在模型训练完成后如何让其"遗忘"特定知识。

### 4.2 现有方法的缺陷

当前的遗忘学习方法存在两个核心问题：

**(1) 参数修改导致灾难性遗忘**

大多数方法将遗忘窄化为"直接修改LLM权重"（称为参数遗忘，Parametric Unlearning）。这些方法不可避免地导致严重的性能下降——即**灾难性遗忘（Catastrophic Forgetting）**——而且这个问题在持续设置中随着每一次新更新而恶化。

**(2) 遗忘效率低下**

现有方法没有考虑到遗忘过程所需的时间成本。效率低下的方法在遗忘过程进行期间仍可能暴露敏感信息，造成**长时间的隐私泄露窗口**。

### 4.3 持续遗忘的现实需求

在实际应用中，遗忘请求是**连续、累积**到来的：
- 初始分区 $D_{f_0}$（遗忘集）、$D_{r_0}=D\setminus D_{f_0}$（保留集）
- 随着新请求到来，遗忘集扩展：$D_{f_0} \subset D_{f_1} \subset \cdots \subset D_{f_N}$
- 目标是在每个阶段都保持对遗忘集的高效遗忘和对保留集的高性能

### 4.4 理想目标：行为遗忘

本文创新性地提出**行为遗忘（Behavioral Unlearning）**的概念——目标是确保LLM不输出被标记为有问题的信息，而不是真正从模型参数中"抹去"知识。这种方法不修改模型权重，因此可以及时响应，同时确保不丢失其他知识。

---

## 5. 核心贡献

本文的贡献主要体现在三个方面：

### 5.1 首个实时持续遗忘框架

CURaTE是**首个能够实时处理连续、顺序遗忘请求的遗忘方法**。处理新遗忘请求的开销几乎为零，这使得它与实际应用场景高度契合。

### 5.2 近乎完美的知识保留

由于不修改LLM权重，CURaTE能够**在长序列的持续遗忘请求后保持近乎完美的知识保留**，基本避免了灾难性遗忘问题——这是现有方法无法解决的难题。

### 5.3 跨任务泛化能力

训练后的遗忘嵌入器能够**在任何遗忘任务上运行，无需针对特定遗忘集或保留集进行额外训练**。现有方法通常需要在每个新的遗忘集和保留集上重新训练，而CURaTE只需一次训练即可泛化到多种任务。

---

## 6. 研究方法

### 6.1 框架概述

CURaTE框架包含两个阶段：

```
┌─────────────────────────────────────────────────────────────┐
│                    CURaTE 框架                               │
├─────────────────────────────────────────────────────────────┤
│  部署前阶段（Pre-deployment Training）                       │
│    └── 在合成数据集上训练句子嵌入模型U                         │
│        （不需要使用遗忘集或保留集）                           │
├─────────────────────────────────────────────────────────────┤
│  部署后推理（Post-deployment Inference）                     │
│    步骤(i):  嵌入遗忘请求并存储                              │
│    步骤(ii): 检索与阈值判断                                  │
│    步骤(iii): 决定是否回答或拒绝                             │
└─────────────────────────────────────────────────────────────┘
```

### 6.2 部署前训练：训练遗忘句子嵌入器

#### 6.2.1 训练数据生成

训练数据通过以下过程构建（使用种子QA数据集，如Natural Questions）：

对于每个问题 $q^s$，使用提示模板 $\tau_1(\cdot)$ 调用代理LLM $G_s$ 生成两种变体：
- **$q^p$（paraphrase）**：$q^s$的复述版本，触发相同响应 → **Type-1数据（正样本）**
- **$q^c$（contrastive）**：与$q^s$词汇/句法高度重叠但语义不同的对比版本 → **Type-2数据（硬负样本）**

然后对 $q^p$ 再次使用 $\tau_2(\cdot)$ 生成对比样本 $q'c$ → **Type-3数据（额外硬负样本）**

最终训练集：
$$T^* = \{[(q_i^s, q_i^p), y_i^p], [(q_i^s, q_i^c), y_i^c], [(q_i^p, q_i'c), y_i'c]\}_{i=1}^n$$

#### 6.2.2 对比损失函数

使用对比损失（Contrastive Loss）微调预训练的句子嵌入模型：

$$\mathcal{L}(T) = \frac{1}{2|T|}\sum_{(q,q',y)\in T}\Big[y \cdot d_U(q,q')^2 + (1-y) \cdot \max(0, m - d_U(q,q'))^2\Big]$$

其中：
- $d_U(q,q') = 1 - \frac{U(q) \cdot U(q')}{\|U(q)\|\|U(q')\|}$ 是余弦距离
- $m$ 是适当选择的边界margin

**损失函数的作用**：
- 减小正样本对之间的距离
- 增大负样本对之间的距离（直到超过边界$m$）
- 硬负样本使嵌入器形成更精细、更准确的决策边界

#### 6.2.3 关键特性

**无需遗忘集或保留集**：所有训练数据来自与评估数据无关的种子数据集，确保：
1. 训练数据是**域外（out-of-domain）**的
2. 单个训练好的 $U$ 模型可以跨任何遗忘任务和域运行
3. 有效性不限于任何特定的遗忘集和保留集

### 6.3 部署后推理：三步实时遗忘

#### 步骤(i)：嵌入并存储遗忘请求

给定第$m$个遗忘样本 $f_m$，生成其嵌入：
$$f_m^{emb} = U(f_m)$$

并将其存储到遗忘嵌入集合 $F$：
$$F = \{f_1^{emb}, \ldots, f_{m-1}^{emb}\} \Rightarrow F \leftarrow F \cup \{f_m^{emb}\}$$

**这个操作是瞬时的**，构成了部署后遗忘过程的全部内容——与现有方法的重量级优化程序形成鲜明对比。

#### 步骤(ii)：检索与阈值判断

每当用户提示 $p$ 输入到LLM $G$ 时：
1. 将 $p$ 投影到嵌入空间：$p^{emb} = U(p)$
2. 对于 $F$ 中的每个嵌入 $f_i^{emb}$，计算与 $p^{emb}$ 的余弦相似度 $s_i \in [-1, 1]$
3. 获取最大相似度 $s_{max} = \max(s_i)$
4. 检查 $s_{max}$ 是否超过给定阈值 $\delta$

#### 步骤(iii)：决策回答或拒绝

$$r_{res} = \begin{cases}
G(p), & \text{if } s_{max} < \delta \\
\text{a sampled element from } R, & \text{if } s_{max} \geq \delta
\end{cases}$$

其中 $R$ 是预定义的拒绝表达集合，如"I don't know"或"I can't answer that question"。

**关键保证**：$G$ 的参数在任何步骤中都不被修改，这保证了 $G$ 内的知识保留，从而防止灾难性遗忘的发生。

---

## 7. 实验设置

### 7.1 基准数据集

实验在四种广泛使用的基准上进行了持续遗忘实验：

| 基准 | 描述 | 遗忘集设置 |
|------|------|----------|
| **RETURN** | 关于真实人物（维基百科页面）的合成QA对 | 30个目标人物中，每阶段3人发出遗忘请求，共10阶段 |
| **TOFU** | 关于完全虚构作者的遗忘基准 | 假作者分成3组，3阶段持续遗忘 |
| **TruthfulQA** | 测试LLM对误导性问题的真实性回答 | 问题分成3阶段作为遗忘集 |
| **ScienceQA** | 科学知识问答 | 4个科学主题（生物、物理、化学、经济）顺序遗忘 |

### 7.2 评估指标

由于CURaTE不修改LLM权重，概率基指标（如Truth Ratio）不适用。主要使用：
- **ROUGE-L**：衡量生成响应与标准答案的相似度
- **Exact Match Accuracy**：在WinoGrande和ScienceQA等数据集上计算准确率

### 7.3 基线方法

选择了8个基线方法进行对比：
1. **GA** (Gradient Ascent)：仅使用遗忘集训练
2. **GradDiff** (Gradient Difference)：遗忘集+保留集正则化
3. **PO** (Preference Optimization)：偏好优化
4. **NPO** (Negative Preference Optimization)
5. **SO-PO**：二阶优化的偏好优化
6. **GUARD**：基于分类器的遗忘方法
7. **O3**：正交LoRA+OOD检测器
8. **UniErase**：添加`<UNL>`遗忘token的方法

---

## 8. 实验结果

### 8.1 RETURN基准（隐私数据遗忘）

**核心发现**：
- 基于梯度的方法（GA、GradDiff等）表现出强烈的**过度遗忘倾向**：在遗忘遗忘集知识的同时，显著损害了无关知识的性能
- 随着阶段推进，性能急剧下降——这正是灾难性遗忘的预期表现
- GUARD、O3和UniErase在一定程度上保留了知识，但未能充分遗忘目标知识
- **CURaTE在所有10个阶段中实现了有效的遗忘，同时在非目标数据集上几乎没有性能下降**

### 8.2 TOFU基准（虚构作者遗忘）

| 方法 | Stage 1 F.G.↓ | Stage 3 F.G.↓ | Stage 3 R.T.↑ |
|------|:-------------:|:-------------:|:--------------:|
| Base | 0.509 | 0.509 | 0.973 |
| GA | 0.390 | 0.003 | 0.003 |
| GradDiff | 0.242 | 0.000 | 0.000 |
| PO | 0.110 | 0.181 | 0.860 |
| NPO | 0.072 | 0.065 | 0.815 |
| UniErase | 0.047 | 0.062 | 0.942 |
| **CURaTE** | **0.046** | **0.043** | **0.961** |

**分析**：唯一能与CURaTE竞争的是UniErase，但后者存在重大局限：
1. UniErase只能处理符合严格（主体、关系、对象）三元组格式的数据
2. UniErase无法实时处理遗忘请求

### 8.3 TruthfulQA基准（虚假信息遗忘）

| 方法 | Stage 3 R.F.↑ | Stage 3 C.Q.↑ |
|------|:-------------:|:-------------:|
| Base | 0.5367 | 0.8256 |
| PO | 0.9792 | 0.3243 |
| O3 | 0.9995 | 0.2647 |
| **CURaTE** | **0.9855** | **0.8149** |

**分析**：CURaTE在拒绝率上接近最优（0.9855 vs 0.9995），同时在常识问答上保持接近Base模型的性能（0.8149 vs 0.8256）。而O3虽然拒绝率高，但常识问答性能严重下降（0.2647）。

### 8.4 ScienceQA基准（通用科学知识遗忘）

**核心发现**：
- O3在保留集上保持与CURaTE相当的性能，但其遗忘集性能异常差
- 原因是O3无法泛化到遗忘集问题的改述变体——原始遗忘集上达到20.7%、4.6%、10.1%、11.8%的低分数，但对措辞的微小变化非常脆弱
- **CURaTE是唯一能够在保持近乎完美的知识保留的同时，在改述变体上实现有效遗忘的方法**

### 8.5 遗忘效率对比

| 方法 | 遗忘时间（秒） | 推理开销（秒/查询） |
|------|:-------------:|:------------------:|
| GA | 195.6 | 0 |
| GradDiff | 229.5 | 0 |
| PO | 178.8 | 0 |
| O3 | 327.6 | 0.05 |
| UniErase | 323.2 | 0 |
| **CURaTE** | **0.04** | **0.01** |

**关键洞察**：CURaTE展现出压倒性的遗忘速度优势，是**唯一能够在遗忘请求和用户查询上实时处理的方法**。GUARD在遗忘时间上相对接近（2.8秒），但推理开销很大（25.5秒/查询）——这将随着LLM规模的增长而急剧恶化。

---

## 9. 策略示例

### 9.1 三种类型训练数据生成策略

```
种子问题: "Who is the president of France?"

    ├── Type-1 (正样本): Paraphrase
    │       "What person holds the position of President in France?"
    │       → 触发相同回答，应标记为 y=1
    │
    └── Type-2 (硬负样本): Contrastive
            "What country has Emmanuel Macron as its leader?"
            → 词汇重叠但语义不同，应标记为 y=0
```

### 9.2 推理阶段判断流程

```
用户输入: "Tell me about the fictional character John Doe."

    ↓ 嵌入向量
    U("Tell me about the fictional character John Doe.") = [0.23, -0.45, ...]
    
    ↓ 检索遗忘集
    查询与遗忘集F中向量的最大相似度
    
    ↓ 判断阈值
    s_max = 0.89 > δ(=0.7)? → YES
    
    ↓ 输出
    拒绝响应: "I can't answer that question."
```

---

## 10. 攻击流程

### 10.1 针对遗忘系统的潜在攻击

#### 攻击场景1：改述攻击（Paraphrasing Attack）

攻击者可能通过对遗忘集中的问题进行改写来绕过检测：
```
原始遗忘问题: "What is Alice's phone number?"
改述攻击:      "How can I reach Alice?"
                "Alice's contact information, please?"
                "Give me the number to call Alice."
```

**CURaTE的防御**：通过训练嵌入器时的改述变体（Type-1数据），CURaTE能够泛化到改述形式，使这类攻击难以成功。

#### 攻击场景2：对抗性攻击（Jailbreaking）

虽然论文提到了这类攻击的可能性，但承认尚未完全测试。攻击者可能尝试：
- 使用对抗性扰动来欺骗句子嵌入器
- 发现嵌入空间中的盲点

**论文承认的局限**：虽然实验包括了改述变体，但没有完全测试绕过句子嵌入器以获取被禁止信息的对抗技术。

### 10.2 遗忘效率与隐私暴露

**时间线对比**：

| 方法 | 遗忘请求到达 → 遗忘完成 | 遗忘过程中的隐私暴露风险 |
|------|:----------------------:|:------------------------:|
| GA/GradDiff | 195-230秒 | 高——完整权重优化期间持续暴露 |
| PO/NPO | 178-250秒 | 高 |
| O3/UniErase | 320-330秒 | 高 |
| GUARD | 2.8秒 | 中——但推理开销大（25.5秒/查询） |
| **CURaTE** | **0.04秒** | **极低——近乎瞬时完成** |

---

## 11. 消融实验

### 11.1 句子嵌入器分类性能消融

在四个基准的第一阶段和最后阶段测试分类性能（F1分数）：

| 配置 | Type-1 | Type-2/3 | 训练集大小 | 种子数据集 | 最终阶段F1 |
|------|:------:|:--------:|:---------:|:----------:|:----------:|
| 原始预训练 | - | - | - | - | 0.8489 |
| 仅使用12k数据 | ✗ | ✗ | 12k | NQ | 0.6809 |
| 仅使用Type-1 | ✓ | ✗ | 18k | NQ | 0.7296 |
| 仅使用硬负样本 | ✗ | ✓ | 12k | NQ | 0.9042 |
| **完整方法** | **✓** | **✓** | **12k** | **NQ** | **0.9157** |

### 11.2 各项组件的贡献分析

#### 训练数据的贡献

使用完整方法（底部行）与原始预训练模型（顶部行）相比，最终阶段F1提升**7.7%**。这归功于对比损失在三种增强数据上的应用，使决策边界更加清晰。

#### 三种数据类型的贡献

仅使用两种数据会导致F1轻微下降，且这不是由于样本数量减少（12k控制数据集没有出现类似下降）。

#### 硬负样本的效果

与不使用硬负样本相比，使用硬负样本使最终阶段F1提升**25.3%**。这是因为构建的$q^c$和$q'c$与$q^s$、$q^p$既有语义差异，又有词汇/结构重叠，形成更难的负样本。

#### 种子数据集的泛化能力

切换到TriviaQA作为种子数据集并没有损害分类性能，甚至略有提升。这证明了方法的**跨数据集泛化能力**。

### 11.3 关键发现

移除任何组件仍能让模型正确分类应拒绝（遗忘）的查询（高召回率），但也会导致过度遗忘（精确率的急剧下降）。因此，所有组件都是实现遗忘与保留之间有效平衡所必需的。

---

## 12. 局限性

### 12.1 无法完全防止信息泄露

与所有现有遗忘方法一样，CURaTE无法对已被标记为有问题信息的泄露提供万无一失的保证。通过调整阈值$\delta$，可以控制减少假阴性的程度，但**无法完全消除**——仅靠方法本身无法做到完全消除。

### 12.2 对抗性攻击未充分测试

虽然实验包含了遗忘集问题的改述变体，但论文承认**尚未完全测试绕过系统的方法**：
- 尚未完全探索欺骗句子嵌入器以获取被禁止信息的对抗技术
- 潜在的jailbreaking攻击尚未被研究

### 12.3 大规模遗忘请求的未知性

在实际场景中，遗忘请求可能数以千计甚至百万计。虽然性能在10个阶段的持续遗忘后没有显示出任何下降迹象，但需要进一步实验来证明在更大量的连续遗忘请求后仍能保持性能。

### 12.4 推理开销随遗忘集增长

虽然单次遗忘操作很快（0.04秒），但随着遗忘集F的增长，检索最大相似度$s_{max}$的计算成本会线性增长。论文提到了使用压缩技术来改进效率和存储，但这是未来的优化方向。

---

## 13. 伦理声明

### 13.1 资助与支持

本研究由韩国科学和信息通信技术部（MSIT）资助，通过韩国政府资助的Institute for Information & communications Technology Planning & Evaluation（IITP）提供（RS-2019-II190075，KAIST人工智能研究生院项目）。

### 13.2 研究价值

CURaTE旨在帮助LLM在实际部署场景中更负责任地处理用户隐私和敏感信息。通过：
- 提供近乎瞬时的遗忘响应
- 保持模型的整体知识完整性
- 支持持续累积的遗忘请求

该方法有潜力显著改善现实世界中LLM部署的隐私保护实践。

### 13.3 潜在滥用风险

论文承认，如果被恶意使用来**故意隐瞒**某些信息（例如监管机构要求披露的信息），该技术可能存在滥用风险。然而，作者的意图是将其用于**合法的隐私保护场景**，例如响应用户的遗忘请求或遵守GDPR等数据保护法规。

---

## 14. 参考文献

1. Chen, J., Xiao, S., Zhang, P., Luo, K., Lian, D., & Liu, Z. (2024). M3-embedding: multi-linguality, multi-functionality, multi-granularity text embeddings. *ACL*.

2. Deng, Z., Liu, C., Pang, Z., He, X., Feng, L., Xuan, Q., Zhu, Z., & Wei, J. (2025). GUARD: generation-time LLM unlearning via adaptive restriction and detection. *arXiv:2505.13312*.

3. Fang, H., Jiang, H., Wang, K., Ma, Y., Wang, X., He, X., & Chua, T. (2024). AlphaEdit: null-space constrained knowledge editing for language models. *arXiv:2410.02355*.

4. Gao, C., Wang, L., Ding, K., Weng, C., Wang, X., & Zhu, Q. (2025). On large language model continual unlearning. *ICLR*.

5. Hadsell, R., Chopra, S., & LeCun, Y. (2006). Dimensionality reduction by learning an invariant mapping. *CVPR*.

6. Hu, E. J., Shen, Y., Wallis, P., Allen-Zhu, Y., Li, Y., Wang, S., & Chen, W. (2021). LoRA: low-rank adaptation of large language models. *arXiv:2106.09685*.

7. Jang, J., Yoon, D., Yang, S., Cha, S., Lee, M., Logeswaran, L., & Seo, M. (2022). Knowledge unlearning for mitigating privacy risks in language models. *ACL*.

8. Jia, J., Zhang, Y., Zhang, Y., Liu, J., Runwal, B., Diffenderfer, J., Kailkhura, B., & Liu, S. (2024). SOUL: unlocking the power of second-order optimization for LLM unlearning. *arXiv:2404.18239*.

9. Joshi, M., Choi, E., Weld, D. S., & Zettlemoyer, L. (2017). TriviaQA: a large scale distantly supervised challenge dataset for reading comprehension. *arXiv:1705.03551*.

10. Kwiatkowski, T., Palomaki, J., Redfield, O., Collins, M., Paranjik, A., Alberti, C., et al. (2019). Natural Questions: a benchmark for question answering research. *TACL*.

11. Lester, B., Al-Rfou, R., & Constant, N. (2021). The power of scale for parameter-efficient prompt tuning. *EMNLP*.

12. Lin, C. (2004). ROUGE: a package for automatic evaluation of summaries. *ACL*.

13. Lin, S., Hilton, J., & Evans, O. (2021). TruthfulQA: measuring how models mimic human falsehoods. *arXiv:2109.07958*.

14. Liu, B., Liu, Q., & Stone, P. (2022). Continual learning and private unlearning. *arXiv:2203.12817*.

15. Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F., & Liang, P. (2023). Lost in the middle: how language models use long contexts. *TACL*.

16. Liu, S., Liu, Y., Jia, J., Casper, S., Baracaldo, N., Hase, P., et al. (2025). Rethinking machine unlearning for large language models. *Nature Machine Intelligence*.

17. Liu, Z., Zhu, T., Tan, C., & Chen, W. (2024). Learning to refuse: towards mitigating privacy risks in LLMs. *arXiv:2407.10058*.

18. Lu, P., Mishra, S., Xia, T., Qiu, L., Chang, K., Zhu, S., et al. (2022). Learn to explain: multimodal reasoning via thought chains for science question answering. *NeurIPS*.

19. Luo, Y., Yang, Z., Meng, F., Li, Y., Zhou, J., & Zhang, Y. (2023). An empirical study of catastrophic forgetting in large language models during continual fine-tuning. *arXiv:2308.08747*.

20. Maini, P., Feng, Z., Schwarzschild, A., Lipton, Z. C., & Kolter, J. Z. (2024). TOFU: a task of fictitious unlearning for LLMs. *arXiv:2401.06121*.

21. Meng, K., Bau, D., Andonian, A., & Belinkov, Y. (2022). Locating and editing factual associations in GPT. *NeurIPS*.

22. Pawelczyk, M., Neel, S., & Lakkaraju, H. (2023). In-context unlearning: language models as few shot unlearners. *arXiv:2310.07579*.

23. Rafailov, R., Sharma, A., Mitchell, E., Ermon, S., Manning, C. D., & Finn, C. (2023). Direct preference optimization: your language model is secretly a reward model. *arXiv:2305.18290*.

24. Reimers, N., & Gurevych, I. (2019). Sentence-BERT: sentence embeddings using Siamese BERT-networks. *arXiv:1908.10084*.

25. Sakaguchi, K., Bras, R. L., Bhagavatula, C., & Choi, Y. (2019). WinoGrande. *Communications of the ACM*.

26. Thaker, P., Maurya, Y., & Smith, V. (2024). Guardrail baselines for unlearning in LLMs. *arXiv:2403.03329*.

27. Touvron, H., Martin, L., Stone, K., Albert, P., Almahairi, Y., Babaei, Y., et al. (2023). Llama 2: open foundation and fine-tuned chat models. *arXiv:2307.09288*.

---

## 📊 论文笔记总结

| 项目 | 内容 |
|------|------|
| **论文** | CURaTE: Continual Unlearning in Real Time with Ensured Preservation of LLM Knowledge |
| **会议** | ACL Findings 2026 |
| **进度** | 第57篇 / 80篇（71.25%） |
| **关键词** | Unlearning, Machine Unlearning, LLM, Privacy, Continual Learning, Real-time Processing |
| **代码** | https://github.com/bsu1313/CURaTE |
| **核心创新** | 行为遗忘 + 句子嵌入器 + 无权重修改 |
| **关键优势** | 实时遗忘、零灾难性遗忘、跨任务泛化 |
| **局限** | 无法完全防止泄露、对抗攻击未充分测试 |

---

*本笔记由AI自动生成*
*LLM Safety论文阅读计划 · 第57篇*
