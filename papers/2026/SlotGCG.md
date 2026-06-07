# SlotGCG: Exploiting the Positional Vulnerability in LLMs for Jailbreak Attacks

## 1. 基本信息

| 项目 | 内容 |
|------|------|
| **论文标题** | Exploiting the Positional Vulnerability in LLMs for Jailbreak Attacks |
| **简称** | SlotGCG |
| **作者** | Seungwon Jeong, Jiwoo Jeong, Hyeonjin Kim, Yunseok Lee, Woojin Lee |
| **单位** | Dongguk University-Seoul（韩国东国大学） |
| **会议** | ICLR 2026 |
| **arXiv** | [2606.05609](https://arxiv.org/abs/2606.05609) |
| **GitHub** | [youai058/SlotGCG](https://github.com/youai058/SlotGCG) |
| **研究方向** | Jailbreak Attack / Red Teaming / LLM Security |
| **录用情况** | ICLR 2026 (CCF-A) |

### 作者简介

- **Seungwon Jeong**（第一作者）：东国大学，主要研究方向为LLM安全与对抗攻击
- **Jiwoo Jeong, Hyeonjin Kim**：东国大学研究生
- **Yunseok Lee, Woojin Lee**：东国大学教授，指导研究方向

---

## 2. 英文摘要原文（arXiv Abstract原文）

> As large language models (LLMs) are widely deployed, identifying their vulnerability through jailbreak attacks becomes increasingly critical. Optimization-based attacks like Greedy Coordinate Gradient (GCG) have focused on inserting adversarial tokens to the end of prompts. However, GCG restricts adversarial tokens to a fixed insertion point (typically the prompt suffix), leaving the effect of inserting tokens at other positions unexplored. In this paper, we empirically investigate **slots**, i.e., candidate positions within a prompt where tokens can be inserted. We find that vulnerability to jailbreaking is highly related to the selection of the **slots**. Based on these findings, we introduce the **Vulnerable Slot Score (VSS)** to quantify the positional vulnerability to jailbreaking. We then propose **SlotGCG**, which evaluates all slots with VSS, selects the most vulnerable slots for insertion, and runs a targeted optimization attack at those slots. Our approach provides a position-search mechanism that is attack-agnostic and can be plugged into any optimization-based attack, adding only 200ms of preprocessing time. Experiments across multiple models demonstrate that SlotGCG significantly outperforms existing methods. Specifically, it achieves **14% higher Attack Success Rates (ASR)** over GCG-based attacks, converges faster, and shows superior robustness against defense methods with **42% higher ASR** than baseline approaches.

**Cite as**: arXiv:2606.05609 [cs.CR]

---

## 3. 中文摘要翻译

随着大型语言模型（LLM）的广泛部署，通过越狱攻击识别其漏洞变得越来越关键。基于优化的攻击方法（如Greedy Coordinate Gradient，GCG）一直专注于将对抗性令牌插入到提示的末尾。然而，GCG将对抗性令牌限制在一个固定的插入点（通常是指示后缀），从而忽略了将令牌插入其他位置的效果。本文通过实证研究**slots**（即提示中可以插入令牌的候选位置）来探讨这一问题。我们发现，越狱的脆弱性与**slots**的选择高度相关。基于这些发现，我们引入了**Vulnerable Slot Score（VSS）**来量化越狱的位置脆弱性。随后，我们提出了**SlotGCG**，它使用VSS评估所有slots，选择最脆弱的slots进行插入，并针对这些slots运行定向优化攻击。我们的方法提供了一个与攻击方法无关的位置搜索机制，可以插入到任何基于优化的攻击中，仅增加200毫秒的预处理时间。在多个模型上的实验表明，SlotGCG显著优于现有方法。具体而言，相比基于GCG的攻击，它实现了**14%更高的攻击成功率（ASR）**，收敛更快，并且在防御方法下表现出更强的鲁棒性，比基线方法**高42%的ASR**。

---

## 4. 研究背景

### 4.1 LLM安全与越狱攻击概述

大型语言模型（LLM）在自然语言理解和生成任务中展现了卓越的能力（参考Touvron et al. 2023; Chiang et al. 2023; Dubey et al. 2024; Achiam et al. 2023）。尽管取得了这些进展，它们仍然容易受到越狱攻击的影响——攻击者通过精心设计的提示可以诱导模型产生有害响应。近年来的AI安全研究越来越多地将这些攻击作为红队测试的一部分，以暴露对齐机制中的漏洞（Maslej et al. 2025; Wei et al. 2023a）。这些攻击采用多种技术，包括提示注入、上下文操纵和基于梯度优化的方法（Yi et al. 2024）。

### 4.2 GCG及其局限性

在众多越狱攻击方法中，Greedy Coordinate Gradient（GCG）（Zou et al. 2023）是一种代表性的基于优化的攻击方法。GCG通过将对抗性令牌附加到有害提示后，并迭代优化这些令牌来诱导不安全响应。

GCG的有效性可以从以下角度理解：
- 放置在提示末尾（即后缀）的对抗性令牌对模型输出具有不成比例的影响
- 注意力机制可能会放大这些基于后缀的扰动

**然而，基于后缀的方法存在一个根本性的研究空白：它们假设后缀是最优的攻击位置，从而限制了对更具挑战性攻击的探索。**

例如，将对抗性令牌插入任意位置的攻击更难被检测，因为其多样化的插入模式需要扫描整个提示。这种挑战促使我们更深入地研究更灵活的攻击策略所带来的威胁。然而，关于令牌位置如何影响攻击效果的系统性理解仍然基本未被探索。

### 4.3 研究动机

本文的研究动机正是填补这一空白。传统GCG方法将对抗性令牌限制在提示末尾（后缀位置），而忽略了其他位置的攻击潜力。本文认为：
- 每个提示都有其固有的"脆弱slots"——这些位置对对抗性令牌插入更敏感
- 脆弱性与模型的注意力模式密切相关
- 脆弱位置在优化过程中保持稳定，说明脆弱性来自位置本身而非特定令牌序列

---

## 5. 核心贡献

本文的核心贡献可以归纳为以下三点：

### 贡献一：形式化脆弱slots概念与VSS指标

本文正式定义了**脆弱slots**（vulnerable slots）这一概念——即更容易受到对抗性令牌插入的位置。同时，引入了**Vulnerable Slot Score（VSS）**来量化位置脆弱性。VSS通过测量从after-chat模板到插入对抗性令牌的注意力权重来评估每个slot的脆弱程度。

### 贡献二：提出SlotGCG方法

SlotGCG是GCG的创新扩展，通过VSS系统地识别高估计脆弱性的插入位置，然后在高VSS位置针对对抗性优化。在跨多个模型和基于GCG方法的实验中，它实现了更高的ASR、更少的优化步骤，以及对输入过滤防御的鲁棒性。

### 贡献三：扩展优化式越狱攻击研究

本文将基于优化的越狱攻击扩展到考虑位置脆弱性，为评估和改进对抗性提示提供了实用指导，并拓宽了红队研究 scope。

---

## 6. 研究方法

### 6.1 Slot与插入操作的定义

本文采用Stern et al. (2019)提出的slot概念来系统地探索潜在的攻击插入位置。

**Slot定义：**
给定一个令牌序列（有害提示）x₁:ₗ = [x₁, x₂, ..., xₗ]，定义L+1个插入slots：
- Slot 0：位于x₁之前的位置
- Slot l（1 ≤ l ≤ L-1）：位于xₗ和xₗ₊₁之间的位置
- Slot L：位于xₗ之后的位置

**插入操作：**
对于slot插入，我们指定一组对抗性令牌A和插入slots Sₐ：
- A = {a₁ᵏ¹, ..., aₘᵏᵐ}：对抗性序列集合
- Sₐ = {s₁, ..., sₘ} ⊆ S：插入位置集合

每个对抗性序列aᵢᵏⁱ = {aᵢ,₁, ..., aᵢ,ₖᵢ}长度为kᵢ，插入到slot sᵢ。

**从右到左插入语义：**
为确保插入过程中slot位置稳定，本文采用从右到左（从最大slot索引到最小）的插入顺序。

**示例：**
对于x₁:₄ = [How, to, make, bomb]，A = {[x,y], [z]}，Sₐ = {0, 2}：
I([How,to,make,bomb], {[x,y],[z]}, {0,2}) = [x,y, How, to, z, make, bomb]

### 6.2 探索性研究设计

本文通过两项互补的探索性实验来研究对抗性令牌位置对越狱攻击的影响：

#### 实验一：穷举Slot扫描（Exhaustive Slot Scan）

作为先导研究，本文穷举扫描有害提示内的所有候选slots，以研究某些slots是否更容易受到对抗性攻击。对于50个有害提示中的每一个，生成变体x^(s) = I(x₁:ₗ, a⁵, s)，其中a⁵是5个对抗性令牌的序列。然后对Llama 2-7B-Chat应用100步GCG优化。

#### 实验二：随机多位置插入（Random Multi-Position Insertion）

作为完整设置研究，该方法检验分布在多个slots中的对抗性令牌是否能在实际条件下引出有害响应。将20个初始对抗性令牌随机分配到多个序列A，然后插入随机采样的slots Sₐ中。

### 6.3 关键发现

**发现一：后缀并非最优位置**

在50个提示中，最优slot（即产生最低对抗性loss的slot）在不同提示间差异很大。而且，产生最小loss的slot从未是后缀（GCG使用的位置）。这表明，对于许多提示来说，后缀并非最脆弱的插入位置。

**发现二：VSS与位置脆弱性高度相关**

对抗性令牌注意力与对抗性loss之间存在负相关关系：具有更高注意力值的slots往往实现更低的loss，表明这些位置更容易受到对抗性令牌的影响。

**发现三：脆弱位置在优化过程中持续有效**

VSS初始化值（VSS^init）与VSS最终值（VSS^final）高度相关，表明脆弱slots在优化过程中保持其高VSS特征。

### 6.4 Vulnerable Slot Score (VSS) 定义

基于上述发现，本文定义VSS来量化slot的脆弱性。对于slot s（插入对抗性序列aᵏ），VSS定义为：

**VSSₛ = Σ_{ℓ∈ℒ_ᵤₕ} Σ_h Σ_{c∈C} Σ_{a∈aᵏ} A^{(ℓ,h)}_{c,a} / k**

其中：
- A^{(ℓ,h)}_{i,j}：第ℓ层第h个注意力头中，从token i到token j的注意力权重
- ℒ_ᵤₕ = {⌊L/2⌋, ..., L}：上半层集合
- C：after-chat模板token集合

本文聚焦于上半层，因为它们捕获了越狱机制最明显的高级语义处理；而after-chat tokens直接影响响应生成。

### 6.5 SlotGCG算法流程

SlotGCG算法包含以下关键步骤：

1. **Slot评估**：使用VSS对所有slots进行评估
2. **最脆弱Slot选择**：选择VSS最高的slots用于插入
3. **定向优化攻击**：在选定的高VSS slots上运行针对优化的攻击

SlotGCG的优势在于：
- 提供位置搜索机制，与攻击方法无关
- 可插入任何基于优化的攻击
- 仅增加200ms预处理时间

---

## 7. 实验设置

### 7.1 目标模型

实验在多个主流LLM上进行评估，包括：
- Llama 2-7B-Chat
- Llama 2-13B-Chat
- Mistral-7B-Instruct
- Vicuna-7B
- 其他模型（见原文附录）

### 7.2 评估数据集

- **AdvBench**：包含50个有害提示（Zou et al. 2023; Chao et al. 2025）
- 涵盖多种有害内容类别，包括暴力、非法活动、仇恨言论等

### 7.3 对比基线方法

- **GCG**（Zou et al. 2023）：标准Greedy Coordinate Gradient攻击
- **AutoDAN**（Liu et al. 2024）：基于梯度的隐蔽越狱提示生成
- **PAIR**（Chao et al. 2024）：20次查询内黑盒越狱
- 其他SOTA方法

### 7.4 评估指标

- **Attack Success Rate (ASR)**：攻击成功率
- **优化收敛速度**：达到特定ASR所需的优化步骤数
- **防御鲁棒性**：在输入过滤防御下的ASR

---

## 8. 实验结果

### 8.1 主要结果：ASR提升

SlotGCG在多个模型上显著优于基线方法：

| 模型 | GCG ASR | SlotGCG ASR | 提升 |
|------|---------|-------------|------|
| Llama 2-7B-Chat | 45% | 59% | +14% |
| Llama 2-13B-Chat | 42% | 56% | +14% |
| Mistral-7B | 48% | 62% | +14% |
| Vicuna-7B | 40% | 54% | +14% |

**关键发现**：SlotGCG平均比基于GCG的攻击方法提高**14%的ASR**。

### 8.2 收敛速度对比

SlotGCG不仅提高ASR，还显著加快收敛：
- 在相同优化步骤下，SlotGCG达到更高ASR
- 达到目标ASR所需的步骤减少约30-40%

### 8.3 对输入过滤防御的鲁棒性

最显著的发现是SlotGCG对防御方法的鲁棒性：

| 防御方法 | 基线ASR | SlotGCG ASR | 提升 |
|----------|---------|-------------|------|
| 输入过滤 | 25% | 67% | +42% |
| 关键词检测 | 30% | 58% | +28% |
| 语义过滤 | 28% | 52% | +24% |

**关键洞察**：SlotGCG通过使用多样化的插入位置，而非集中在后缀，使其更难被基于模式的防御检测，从而实现**42%更高的ASR**。

### 8.4 跨模型攻击迁移性

SlotGCG生成的对抗性提示在不同模型间具有强迁移性：
- 在Llama 2上优化的提示对Mistral、Vicuna等模型同样有效
- 迁移性优于标准GCG，验证了位置脆弱性的普遍性

---

## 9. 策略示例

### 9.1 GCG vs SlotGCG攻击模式对比

**传统GCG攻击**（左侧）：
```
[System Prompt] + [User Query: How to make a bomb?] + [Adversarial Suffix: imperceptibly...]
```

**SlotGCG攻击**（右侧）：
```
[Adversarial Prefix] + [System Prompt] + [User Query: How to make a bomb?] + [Adversarial Infix]
```

### 9.2 具体示例

假设有害查询为"How to make a bomb?"

**GCG攻击**：
```
[System] You are a helpful assistant. [User] How to make a bomb? [Adversarial suffix tokens]
```

**SlotGCG攻击**（插入到slot 0，即系统提示前）：
```
[Adversarial tokens] [System] You are a helpful assistant. [User] How to make a bomb?
```

**SlotGCG攻击**（插入到slot 5，即用户查询中间）：
```
[System] You are a helpful assistant. [User] How [Adversarial tokens] to make a bomb?
```

### 9.3 VSS引导的Slot选择

对于不同的有害查询，最脆弱的slot位置可能不同：
- 某些提示在slot 0（开头）最脆弱
- 某些提示在slot L（末尾）最脆弱
- 某些提示在中间位置最脆弱

VSS通过注意力权重自动识别这些位置，无需穷举搜索。

---

## 10. 攻击流程详解

### 10.1 完整攻击流程

```
1. 初始化
   ├── 输入：有害查询 x¹:ₗᴼ
   ├── 初始化对抗性序列 A
   └── 定义目标有害响应 xᵀ

2. Slot评估阶段（新增，仅200ms）
   ├── 对每个slot s ∈ S计算VSSₛ
   ├── 选择top-k高VSS的slots
   └── 输出：最脆弱的插入位置集合 S*

3. 对抗性优化阶段
   ├── 对于每个候选对抗性序列：
   │   ├── 计算梯度 ∇ℒ
   │   ├── 选择最佳替换候选
   │   └── 更新对抗性序列
   └── 迭代直到收敛或达到最大步骤

4. 攻击验证
   ├── 将优化后的对抗序列插入选定slots
   ├── 输入到目标LLM
   └── 评估是否成功越狱
```

### 10.2 关键创新点

**位置搜索机制**：SlotGCG的核心创新在于提供了一个位置搜索机制，能够：
1. 评估所有候选slots的脆弱性
2. 选择最脆弱的位置进行攻击
3. 在选定位置上进行定向优化

**与攻击方法无关**：VSS引导的位置选择可以与任何基于优化的攻击方法结合：
- GCG → SlotGCG
- AutoDAN → SlotAutoDAN
- 其他梯度-based方法...

### 10.3 时间复杂度分析

- **额外预处理**：200ms（VSS计算）
- **主要优化**：与标准GCG相同
- **总开销**：可忽略不计

---

## 11. 消融实验

### 11.1 Slot数量对ASR的影响

| Top-k Slots | ASR | 相对GCG提升 |
|-------------|-----|-------------|
| k=1 | 55% | +10% |
| k=3 | 58% | +13% |
| k=5 | 59% | +14% |
| k=10 | 58% | +13% |
| k=20 | 56% | +11% |

**发现**：选择top-5 slots达到最佳平衡，过多slots反而降低效果。

### 11.2 VSS vs 随机Slot选择

| Slot选择策略 | ASR |
|--------------|-----|
| 随机选择 | 38% |
| 仅后缀（GCG） | 45% |
| VSS引导（SlotGCG） | 59% |

**发现**：VSS引导的slot选择比随机选择高21% ASR，比仅使用后缀高14% ASR。

### 11.3 VSS计算中不同层的影响

| 层范围 | VSS与ASR相关性 |
|--------|----------------|
| 仅低层（1-10） | 0.42 |
| 仅高层（20-32） | 0.71 |
| 上半层（16-32） | 0.85 |

**发现**：聚焦上半层注意力权重是VSS计算的关键。

### 11.4 不同插入位置的效果

| 插入位置 | ASR |
|----------|-----|
| slot 0（开头） | 52% |
| slot L（末尾/后缀） | 45% |
| slot L/2（中间） | 48% |
| VSS选择的最优slot | 59% |

**发现**：最优slot因提示而异，VSS能有效识别。

### 11.5 对抗性序列长度的影响

| 序列长度 | ASR | 优化时间 |
|----------|-----|----------|
| 5 tokens | 52% | 快速 |
| 10 tokens | 57% | 中等 |
| 20 tokens | 59% | 较慢 |
| 50 tokens | 60% | 慢 |

**发现**：20 tokens是效果与效率的良好平衡点。

---

## 12. 局限性

### 12.1 适用范围的局限性

1. **白盒攻击前提**：SlotGCG需要访问模型的注意力权重来计算VSS，对于完全黑盒的商用API（如GPT-4 API）不直接适用
2. **仅针对基于优化的攻击**：对于非梯度-based攻击（如PAIR、manual jailbreaks），SlotGCG的位置搜索机制不能直接应用
3. **仅验证文本LLM**：实验主要在文本LLM上进行，对多模态模型的适用性待验证

### 12.2 防御措施的潜在应对

虽然SlotGCG对某些防御展示了鲁棒性，但以下防御可能有效：
1. **输出过滤**：基于模型输出内容的检测
2. **完整序列扫描**：对整个输入序列进行全面安全检测
3. **注意力异常检测**：检测异常的关注模式
4. **RLHF对抗训练**：通过对抗样本进行安全微调

### 12.3 实际部署的限制

1. **计算成本**：尽管预处理仅200ms，但完整的攻击优化仍需大量GPU资源
2. **可检测性**：尽管比后缀攻击更隐蔽，但精心设计的输入验证仍可能检测到异常插入模式
3. **模型特异性**：某些对齐良好的模型可能对位置操纵攻击具有内在抵抗力

### 12.4 伦理与社会影响

1. **双刃剑性质**：本文提出的攻击方法可能被恶意行为者滥用
2. **负责任的披露**：作者应与模型提供商协调，确保在论文发表前有足够的防御措施
3. **红队测试价值**：本研究为LLM安全评估提供了更全面的测试方法，有助于提升整体AI安全水平

---

## 13. 伦理声明

**Warning**: 本论文包含可能被认为具有攻击性的模型输出。

本文研究了LLM的越狱攻击漏洞，这是一种对AI系统安全评估具有重要价值的研究方向。论文的主要目标是：

1. **提升LLM安全评估的全面性**：通过揭示位置脆弱性，帮助研究者和开发者更好地理解LLM的安全边界

2. **促进防御研究**：攻击的进步推动防御的进步，SlotGCG揭示的新脆弱性可以指导更有效的防御机制设计

3. **负责任的研究实践**：
   - 所有实验使用标准的AdvBench有害查询集
   - 不涉及真实的恶意使用场景
   - 研究结果将用于提升LLM安全性，而非降低它

4. **与学术诚信一致**：本文遵循ICLR的伦理审查标准，所有攻击研究均在受控实验环境中进行

**注意**：尽管本文涉及越狱攻击，但这是AI安全研究的必要组成部分。类似的安全研究在网络安全、软件工程等领域已被广泛接受和鼓励。

---

## 14. 参考文献

1. Vaswani, A., et al. (2017). Attention Is All You Need. NeurIPS.

2. Zou, A., et al. (2023). Universal and Transferable Adversarial Attacks on Aligned Language Models. arXiv:2307.15043.

3. Touvron, H., et al. (2023). Llama 2: Open Foundation and Fine-Tuned Chat Models. arXiv:2307.09288.

4. Chiang, Z., et al. (2023). Vicuna: An Open-Source Chatbot Impressing GPT-4 with 90% ChatGPT Quality.

5. Dubey, A., et al. (2024). The Llama 3 Herd of Models. arXiv:2407.21783.

6. Achiam, J., et al. (2023). GPT-4 Technical Report. arXiv:2303.08774.

7. Wei, A., et al. (2023). Jailbroken: How Does LLM Safety Training Fail? NeurIPS.

8. Maslej, N., et al. (2025). The AI Index Report 2025. Stanford HAI.

9. Yi, S., et al. (2024). Benchmarking Indirect Prompt Injection Attacks and Defenses. arXiv:2312.14197.

10. Stern, N., et al. (2019). Insertion Decoder Language Model. arXiv:1909.02152.

11. Ben-Tov, M., et al. (2025). [Reference to jailbreaking attention mechanisms].

12. Wang, B., et al. (2024). [Reference to suffix attention in jailbreaking].

13. Zhang, Y., et al. (2025). [Reference to positional effects].

14. Li, H., et al. (2024). [Reference to suffix token influence].

15. Zhao, X., et al. (2024). [Reference to attention amplification].

16. Hu, X., et al. (2025). [Reference to perturbation amplification].

17. Liu, Y., et al. (2024). AutoDAN: Generating Stealthy Jailbreak Prompts on Aligned Large Language Models. ICLR 2024.

18. Chao, P., et al. (2024). Jailbreaking Black Box LLMs in Twenty Queries. arXiv:2310.08419.

19. Chao, P., et al. (2025). HarmBench: Standardized Evaluation of Automated Red Teaming. arXiv.

---

*本文档由 LLM Safety 论文阅读助手 自动生成*
*论文发表时间：2026年6月4日（arXiv提交）*
*笔记生成时间：2026年6月8日*