# 论文笔记：Quantifying Aleatoric Uncertainty of In-Context Learning for Robust Measure of LLM Prediction Confidence

## 1. 基本信息

| 字段 | 内容 |
|------|------|
| **论文标题** | Quantifying Aleatoric Uncertainty of In-Context Learning for Robust Measure of LLM Prediction Confidence |
| **作者** | Jinseok Chung, Minkyoung Song*, Hyunji Jung*, Namhoon Lee（POSTECH，*同等贡献） |
| **会议/期刊** | ACL 2026 |
| **arXiv ID** | 2606.19353 |
| **方向** | Hallucination Detection / Uncertainty / In-Context Learning |
| **代码** | https://github.com/LOG-postech/self-fv-icl |

---

## 2. 英文摘要原文（arXiv Abstract原文）

> In-Context Learning (ICL) allows LLMs to adapt to new tasks from a few demonstrations, but its reliability remains a concern: predictions are highly sensitive to both prompt design and the model's ability to understand the context, obscuring whether failures arise from data properties or model limitations. Uncertainty decomposition—separating aleatoric from epistemic sources—is particularly crucial in this setting, yet existing methods, designed for standard generation tasks, fail to capture the unique dynamics of ICL. To address this, we introduce a concept of self-function vectors, built upon Bayesian views and the mechanistic interpretability of ICL. These vectors leverage internal model representations to model the latent concept learned during in-context prompting, thereby enabling a direct estimation of aleatoric uncertainty within a Bayesian framework and circumventing the reliance on brittle input or decoding manipulations. Given the lack of established benchmarks and suitable evaluation protocols, we also propose the first and rigorous evaluation protocol, in which data is manipulated in controlled ways so as to quantify aleatoric uncertainty precisely and separately from epistemic uncertainty. With this new evaluation framework, initially grounded in synthetic tasks for conceptual development and subsequently extended to real-world datasets, we show that our proposed methodology can measure uncertainty of LLM predictions made under ICL more reliably than existing alternative methods. Moreover, we show it can be used as a practical tool for trustworthy-related applications, such as hallucination detection. Our findings pave a new direction for connecting the quantitative view of uncertainty with the mechanistic understanding of model behavior.

---

## 3. 中文摘要翻译

> 上下文学习（ICL）使大语言模型（LLM）能够通过少量演示样本适应新任务，但其可靠性仍存在隐患：预测结果对提示设计高度敏感，同时也取决于模型理解上下文的能力，这使得难以判断失败究竟是源于数据属性还是模型本身的局限性。在这种设置下，不确定性分解——即区分随机不确定性（aleatoric）和认知不确定性（epistemic）——尤为重要。然而，现有方法均针对标准生成任务设计，无法捕捉ICL独特的动态特性。为解决这一问题，本文提出了自功能向量（self-function vectors）的概念，该概念基于ICL的贝叶斯视角和机械可解释性（mechanistic interpretability）。这些向量利用模型的内部表征来建模在上下文提示中学习到的潜在概念，从而能够在贝叶斯框架内直接估计随机不确定性，同时避免了脆弱的输入或解码操作依赖。鉴于目前缺乏针对ICL不确定性分解的基准测试和评估协议，本文还提出了首个严格且系统的评估协议，该协议通过控制数据操纵方式精确且独立地量化随机不确定性和认知不确定性。在这一新评估框架下（最初以合成任务为概念验证基础，随后扩展到真实数据集），本文证明了所提出的方法能够比现有替代方法更可靠地测量ICL下LLM预测的不确定性。此外，本文还展示了该方法在可信AI相关应用中的实用价值，如幻觉检测。本研究为将不确定性的定量分析与模型行为的机械可解释性相结合开辟了新方向。

---

## 4. 研究背景

### 4.1 上下文学习（ICL）的问题

上下文学习（In-Context Learning，ICL）是LLM的一项关键能力，它允许模型通过在提示中直接提供少量输入-输出演示样本来适应新任务，而无需更新模型权重（Brown et al., 2020）。然而，ICL天然具有脆弱性：预测结果会随提示格式、演示样本顺序或数据属性的微小变化而剧烈波动（Min et al., 2022; Chan et al., 2022, 2025）。此外，ICL预测高度依赖于模型的上下文可学习性（Wang et al., 2024），使得难以区分失败究竟是源于数据属性还是模型本身的局限性。

### 4.2 不确定性分解的重要性

不确定性量化（Uncertainty Quantification，UQ）不仅需要测量整体不确定性水平，还需要将其分解为不同来源——这一过程称为不确定性分解（Uncertainty Decomposition）。具体而言：

- **随机不确定性（Aleatoric Uncertainty，AU）**：源于数据固有的模糊性或噪声，是不可简化的不确定性来源
- **认知不确定性（Epistemic Uncertainty，EU）**：反映模型知识或表征的局限性，原则上可以通过更好的建模或更多证据来减少

在ICL场景中，这种分解尤为重要，因为预测同时取决于给定上下文和模型的可学习性。然而，现有研究主要关注标准问答设置，针对ICL的研究较少（Shorinwa et al., 2024）。先前的方法通常涉及输入操作（Abbasi-Yadkori et al., 2024; Ling et al., 2024; Wang and Holmes, 2025）或改变解码策略（Kuhn et al., 2023; Ling et al., 2024），但这些方法不能直接迁移到ICL，因为输入或解码的微小变化可能导致性能的巨大且不可预测的波动。

### 4.3 两条有前途的研究路径

1. **贝叶斯推理视角**：将ICL解释为隐式贝叶斯推理，为原则性分解提供了理论基础（Xie et al., 2022; Wang et al., 2023; Jiang, 2024）
2. **机械可解释性进展**：检查模型内部表征（如表征动态和注意力头激活），提供了在不需显式操作输入或解码的情况下观察ICL行为的工具（Hendel et al., 2023; Todd et al., 2024; Heo et al., 2025）

### 4.4 评估挑战

在ICL中评估不确定性分解仍是一个开放挑战：现有研究通常依赖于不确定性量化的下游任务（如幻觉检测或分布外识别），由于没有直接评估分解质量的基准测试，因此无法确定AU和EU是否真正被分离，或者明显的收益仅仅是代理任务性能的反映。

---

## 5. 核心贡献

本文的贡献可概括为以下三点：

1. **随机不确定性量化方法**：提出基于自功能向量的随机不确定性量化方法，这是一种利用内部模型表征进行ICL中原则性不确定性分解的新方法，建立在贝叶斯视角和机械可解释性的基础上

2. **评估协议**：为ICL场景下的不确定性分解开发了首个严格且系统的评估协议，基于合成任务构建，能够可靠地捕捉ICL动态特性并实现对分解质量的忠实评估

3. **实用应用**：通过在幻觉检测上展示竞争性性能，建立了方法的实用性，为将不确定性估计与机械可解释性相连接开辟了新潜力

---

## 6. 研究方法

### 6.1 方法概述

本文方法的核心是**自功能向量（Self-Function Vectors）**的概念——这是功能向量的一个变体，旨在作为潜在概念的代理。该方法包含四个阶段：

| 阶段 | 名称 | 描述 |
|------|------|------|
| S1 | 因果头选择（Causal Head Selection） | 通过因果间接效应分析识别导致任务语境化的显著注意力头 |
| S2 | 自功能向量构建 | 从每个显著头的最终token激活中提取激活，构建自功能向量 |
| S3 | 自功能向量干预 | 将自功能向量注入推理时最终token的隐藏状态，产生潜在条件预测 |
| S4 | 不确定性分解 | 使用潜在条件预测计算分解后的不确定性 |

### 6.2 识别显著注意力头（3.1节）

为了识别任务相关的注意力头，本文从给定的任务数据集出发，估计每个注意力头对模型预测的因果贡献。遵循Todd et al.（2024）的方法，通过使用标签打乱的示例引入反事实的上下文输入来评估。

给定一个被破坏的提示 $\tilde{P}=[\tilde{\mathcal{D}}_{ex}, x_{val}]$，对每个头 $(l,k)$，用正确标记输入上计算的均值激活向量 $\bar{h}_{(l,k)}^{T}$ 替换其最终token激活。一个头的**因果效应（CE）**定义为这种替换引起的预测概率变化：

$$CE(P) = p_{h_{(\ell,k)}^{\tilde{P}} \to \bar{h}_{(\ell,k)}^{T}}(y \mid [\tilde{\mathcal{D}}_{ex}, x_{val}]) - p(y \mid [\mathcal{D}_{ex}, x_{val}])$$

计算使用多个提示的因果效应，并选择平均CE最高的头形成显著集 $\mathcal{S}_T$。

### 6.3 自功能向量作为潜在任务表征（3.2节）

给定测试提示 $P^*$，从每个显著头 $(\ell,k) \in \mathcal{S}_T$ 提取最终token激活 $h_{(\ell,k)}^{P^*}$。对于每个集成迭代 $i$，通过从 $\{h_{(\ell,k)}^{P^*} \mid (\ell,k) \in \mathcal{S}_T\}$ 中随机采样构建功能向量：

$$\hat{v}_{T}^{(i)} = \sum_{(\ell,k) \subseteq \mathcal{S}_T} h_{(\ell,k)}^{P^*}$$

本文将这些称为**自功能向量**，因为它们通过任务相关的注意力头封装了提示的内部表征。这允许捕获提示特定的不确定性，而不是功能向量的平均表征。

### 6.4 自功能向量干预（3.3节）

为了获得潜在条件预测，本文在推理时将自功能向量 $\hat{v}_{T}^{(i)}$ 注入到指定目标层 $\ell_t$ 的隐藏状态中。设 $h_{\ell_t}$ 为层 $\ell_t$ 的原始激活，干预将其修改为：

$$h_{\ell_t}^{\prime} = h_{\ell_t} + \hat{v}_{T}^{(i)}$$

修改后的激活 $h_{\ell_t}^{\prime}$ 通过语言模型头产生预测分布 $p(y \mid x^{\star}, \mathcal{D}_{ex}, \hat{v}_{T}^{(i)})$。该预测分布可解释为 $p(y \mid x^{\star}, \phi)$ 的实现，其中 $\phi \sim p(\phi \mid \mathcal{D}_{ex})$。

### 6.5 不确定性分解（3.4节）

使用标准贝叶斯分解分解预测不确定性。总不确定性由预测分布的熵给出：

$$\mathcal{H}[p(y \mid x^{\star}, \mathcal{D}_{ex})] = -\sum_{y \in \mathcal{Y}} p(y \mid x^{\star}, \mathcal{D}_{ex}) \log p(y \mid x^{\star}, \mathcal{D}_{ex})$$

**随机不确定性（AU）**通过自功能向量干预下预测的熵的平均值来近似：

$$\mathbb{E}_{p(\phi \mid \mathcal{D}_{ex})}[\mathcal{H}(p(y \mid x^{\star}, \phi))] \approx \frac{1}{N} \sum_{i=1}^{N} \mathcal{H}(p(y \mid x^{\star}, \mathcal{D}_{ex}, \hat{v}_{T}^{(i)}))$$

实际上，本文使用 $N=1$，使用从顶部因果效应头聚合的自功能向量 $\hat{v}_T$ 执行单一干预。

---

## 7. 实验设置

### 7.1 模型

使用多个模型评估方法在不同规模和架构上的鲁棒性：
- **LLaMA2-7B, LLaMA2-13B, LLaMA2-70B**（Touvron et al., 2023）
- **Qwen2.5-7B**（Qwen et al., 2025）
- **Mistral-7B**（Jiang et al., 2023）

### 7.2 方法配置

- 将方法限制在top-20因果头
- 在变压器深度的三分之一处进行干预（例如，LLaMA2-7B的第10层，LLaMA2-13B的第13层）
- 遵循层采样策略（Todd et al., 2024; Liu and Deng, 2025），避免不切实际的完整层搜索

### 7.3 数据集

评估主要依赖WordNetMCQ（支持可控的不确定性操作），额外的实验涵盖：
- **AG News**：分类任务
- **Emotion**：情感分类
- **HellaSwag**：常识推理
- **GSM8K**：数学推理

### 7.4 基线方法

- **Total Entropy**：总熵
- **Semantic Entropy**（Kuhn et al., 2023）：基于语义聚类模型输出的熵来测量不确定性
- **UQ_ICL**（Ling et al., 2024）：将ICL中的总不确定性分解为AU和EU
- 扩展基线包括MaxProb（Hendrycks and Gimpel, 2017）和Lookback Lens（Chuang et al., 2024）

---

## 8. 实验结果

### 8.1 随机不确定性控制实验（5.1节）

#### 8.1.1 多答案示例比例变化

变化WordNetMCQ1和WordNetMCQ2示例的比例。结果（表1）显示：

| 方法 | LLaMA2-7B | LLaMA2-13B | LLaMA2-70B |
|------|-----------|-----------|-----------|
| Total Entropy | 0.514 | 0.426 | 0.208 |
| Semantic Entropy | -0.277 | -0.248 | -0.301 |
| UQ_ICL | -0.093 | -0.097 | -0.380 |
| **Self-FV** | **0.640** | **0.435** | **0.292** |

自功能向量在LLaMA2-7B、13B和70B上均获得最高相关性，表明它更清晰地反映了数据模糊性的影响。

### 8.2 认知不确定性控制实验（5.2节）

#### 8.2.1 OOD查询变化

Table 3（Spearman correlations under OOD query variation, evaluated using WNMCQ1）的结果显示：更接近零（|ρ| ↓）的相关性表示更好的EU隔离。自功能向量在此设置下也表现出色。

### 8.3 合成任务玩具实验（4.1节）

玩具实验结果（图2）表明：
- **多答案示例和标签翻转任务**控制AU
- **OOD查询任务**控制EU
- 随着模型规模增大，AU和EU的分离更加清晰——较大模型在扰动下往往一个不确定性来源稳定，而另一个呈现更一致的增加

### 8.4 消融实验（5.4节）

#### 8.4.1 自功能向量有效捕获提示特定概念表征

图4的分析表明：
- (a) 自功能向量与功能向量之间余弦相似性的分布，按任务正确性分开，两种分布的清晰区别支持自功能向量比功能向量更好地反映 $P^*$ 特异性内部任务表征
- (b) 按重要性评分排名的top-20因果头，x轴表示用于CIE的示例数量，模型在不同数量的示例中识别出一致的因果头
- (c) 来自不同数量示例的功能向量之间的余弦相似性，相邻数量的相似性收敛

---

## 9. 评估协议（第四章）

### 9.1 协议设计动机

高质量的不确定性分解评估对于确保ICL中模型预测的可靠性和可解释性至关重要。然而，据本文所知，目前不存在为此目的的评估协议。本文通过分析受控扰动如何影响二元分类中的不确定性来解决这一差距。

### 9.2 WordNetMCQ数据集构建（4.2节）

基于玩具实验的发现，本文将合成洞察推广到使用WordNet（Miller, 1994）实例化的任务，提供更自然和语言基础的评估。WordNet通过同义词集、层次关系（如上位词）和词义级别区分来编码细粒度词汇语义。

具体区分：
- **WordNetMCQ1**：单答案多选题，四个选项中只有一个正确
- **WordNetMCQ2**：多答案多选题，每个问题有两个正确答案

这允许在ICL中仔细控制每个任务的场景。

---

## 10. 方法创新点分析

### 10.1 与先前工作的关键区别

| 方面 | 传统方法 | 本文方法 |
|------|---------|---------|
| **信息来源** | 输出变异性（解码或提示策略） | 内部模型表征 |
| **理论基础** | 启发式或经验方法 | 贝叶斯分解 + 机械可解释性 |
| **ICL适配性** | 需要输入/解码操作，不适用于ICL | 直接利用ICL机制 |
| **可解释性** | 黑盒 | 结构感知且可解释 |

### 10.2 自功能向量的优势

1. **提示特异性**：自功能向量封装了通过任务相关注意力头的提示内部表征，捕获提示特定的不确定性，而非功能向量的平均表征
2. **原则性分解**：基于ICL的贝叶斯视角，自然地连接到不确定性分解
3. **无需输入操作**：避免了输入扰动可能引入的不稳定性

---

## 11. 攻击流程（不适用于本文——此论文为防御/分析方法）

本文不是攻击论文，而是一篇关于不确定性量化的防御/分析论文。无攻击流程需要描述。

---

## 12. 消融实验（详细）

### 12.1 自功能向量 vs 功能向量

自功能向量与功能向量的关键区别在于：
- **功能向量**：来自正确标记输入的平均激活，编码跨示例的平均任务表征
- **自功能向量**：来自测试提示本身的最终token激活，编码提示特定的概念

实验证明自功能向量能更好地反映 $P^*$ 特异性内部任务表征。

### 12.2 单Top-k干预 vs 集成变体

本文在实践中使用 $N=1$（单一干预），使用从顶部因果效应头聚合的自功能向量 $\hat{v}_T$，这在效率和效果之间取得了良好平衡。

### 12.3 示教样本数量对因果头选择的影响

随着用于因果间接效应（CIE）分析的示例数量变化，模型在不同数量的示例中识别出一致的因果头，表明方法对示例数量的敏感性较低。

### 12.4 功能向量收敛性

来自不同数量示例的功能向量之间的余弦相似性分析表明，相邻数量的相似性收敛，验证了方法随示教样本数量增加的稳定性。

---

## 13. 局限性

本文存在以下局限性：

1. **函数向量作为后验采样的近似**：使用函数向量作为潜在任务后验采样的近似是间接的和解释性的。它们在多大程度上捕获了真正的后验结构仍不确定，需要更深入的理论分析

2. **超参数调优需求**：关键超参数（如干预层和因果头数量）需要针对每个模型进行调整，这限制了跨架构的泛化能力

3. **任务覆盖范围**：需要在更广泛的任务范围内验证方法的有效性

---

## 14. 伦理声明

本文的工作得到以下资助支持：
- IITP grant funded by the Government of the Republic of Korea (Ministry of Science and ICT)：
  - RS-2019-II191906: Artificial Intelligence Graduate School Program (POSTECH)
  - RS-2022-II220959: Few-Shot Learning of Causal Inference in Vision and Language for Decision Making
  - RS-2023-00216011: Development of Artificial Complex Intelligence for Conceptually Understanding and Inferring like Humans
- High-Performance Computing Support Project funded by the Government of the Republic of Korea (Ministry of Science and ICT)：RQT-25-070137

---

## 15. 参考文献（主要引用）

1. Brown et al. (2020) - Language models are few-shot learners [NeurIPS]
2. Kendall and Gal (2017) - What uncertainties do we need in Bayesian deep learning? [NeurIPS]
3. Kuhn et al. (2023) - Semantic entropy [Nature/NeurIPS]
4. Todd et al. (2024) - Function vectors [ICML]
5. Xie et al. (2022) - In-context learning induces in-context activation [ICLR]
6. Wang et al. (2023) - An LLM can learn from its mistakes [NeurIPS]
7. Jiang (2024) - A bayesian approach to in-context learning
8. Elhage et al. (2021) - Soft maxes [NeurIPS]
9. Olsson et al. (2022) - In-context learning [NeurIPS]
10. Ling et al. (2024) - UQ_ICL [NeurIPS]
11. Abbasi-Yadkori et al. (2024) - To believe or not to believe your LLM [NeurIPS]
12. Wang and Holmes (2025) - On UQ in ICL [ICLR]
13. Jayasekera et al. (2025) - Variational UQ decomposition in ICL [ICLR]
14. Touvron et al. (2023) - LLaMA2
15. Jiang et al. (2023) - Mistral 7B
16. Qwen et al. (2025) - Qwen2.5
17. Mucsányi et al. (2024) - UQ benchmarks survey
18. Miller (1994) - WordNet
19. Zhang et al. (2016) - AG News
20. Saravia et al. (2018) - Emotion dataset
21. Zellers et al. (2019) - HellaSwag
22. Cobbe et al. (2021) - GSM8K
23. Hendrycks and Gimpel (2017) - MaxProb
24. Chuang et al. (2024) - Lookback Lens
25. Yin and Steinhardt (2025) - Function vector heads
26. Jiang et al. (2025) - Function vectors as latent task embeddings
27. Heo et al. (2025) - Mechanistic ICL
28. Falck et al. (2024) - Information-theoretic decomposition
29. Wimmer et al. (2023) - Shannon entropy in UQ
30. Houlsby et al. (2011) - Bayesian active learning
31. Gal et al. (2017) - Deep Bayesian active learning
32. Shorinwa et al. (2024) - Survey on UQ for LLMs
33. Min et al. (2022) - Rethinking the role of demonstrations
34. Chan et al. (2022, 2025) - In-context learning studies
35. Wang et al. (2024) - Two-stage ICL
36. Liu and Deng (2025) - Layer subsampling for FV
37. Liu et al. (2025) - Additional related work
38. Vazhentsev et al. (2025) - RAUQ related work

---

## 附录补充信息

### A. 合成数据实验

#### A.1 合成数据构建
- **多答案示例**：示例中包含多个正确答案
- **标签翻转**：标签被随机翻转引入噪声
- **模糊查询**：查询具有歧义性
- **OOD查询**：查询来自分布外

#### A.2 WordNetMCQ基准验证结果

### B. 评估指标比较

候选指标包括：
- Pearson相关性
- Spearman秩相关
- Goodman-Kruskal's gamma
- Kendall's Tau-b
- Kendall's Tau-c
- Somers' d

### C. 提示示例

### D. 实验超参数详情

### E. 额外消融结果

### F. 额外基线和相关工作

---

*本笔记由 LLM Safety 论文阅读计划自动生成*
*生成时间：2026-06-22*
