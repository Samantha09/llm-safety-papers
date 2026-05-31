# AliMark: Enhancing Robustness of Sentence-Level Watermarking Against Text Paraphrasing

## 1. 基本信息

|字段 | 内容 |
|------|------|
| **论文标题** | AliMark: Enhancing Robustness of Sentence-Level Watermarking Against Text Paraphrasing |
| **中文标题** | AliMark：增强句子级水印在文本改写攻击下的鲁棒性 |
| **作者** | Wenjie Qu, Linyu Wu, Yulin Chen, Yufei He, Tri Cao, Bryan Hooi, Jiaheng Zhang |
| **发表会议** | ICML 2026 |
| **CCF等级** | CCF-A |
| **方向** | Watermarking / Security |
| **arXiv编号** | [2605.29434](https://arxiv.org/abs/2605.29434) |
| **GitHub** | [imethanlee/AliMark](https://github.com/imethanlee/AliMark) |
| **论文链接** | <https://arxiv.org/abs/2605.29434> |

---

## 2. 英文摘要原文（arXiv Abstract原文）

> Existing sentence-level watermarking methods enhance robustness to paraphrasing by anchoring watermarks in sentence semantics. However, their prefix-based designs remain vulnerable to structural perturbations, such as sentence splitting and merging, which commonly arise under strong paraphrasers like DIPPER and GPT-3.5. To mitigate this issue, we propose AliMark, a framework that reformulates sentence-level watermarking as a bit sequence encoding and alignment problem between a potentially watermarked text and a secret bit sequence. Notably, our approach adopts a two-stage detection strategy: we generate multiple restructured text variants and adaptively align their extracted bit sequences with the secret bit sequence to minimize alignment cost. This multi-candidate alignment design naturally improves robustness to sentence merges and splits. Extensive experiments demonstrate that AliMark substantially outperforms state-of-the-art baselines under diverse paraphrasing attacks.

---

## 3. 中文摘要翻译（人工翻译）

现有的句子级水印方法通过将水印锚定在句子语义层面来增强对文本改写的鲁棒性。然而，这些基于前缀的设计仍然容易受到结构性扰动的影响，例如句子分割和合并，这些扰动在使用DIPPER和GPT-3.5等强改写器时经常发生。为解决这个问题，我们提出了AliMark，一个将句子级水印重新定义为潜在水印文本与秘密比特序列之间的比特序列编码和对齐问题的框架。值得注意的是，我们的方法采用了两阶段检测策略：我们生成多个重构文本变体，并自适应地将提取的比特序列与秘密比特序列进行对齐以最小化对齐成本。这种多候选对齐设计自然地提高了对句子合并和分割的鲁棒性。大量的实验表明，AliMark在各种文本改写攻击下显著优于最先进的基线方法。

---

## 4. 研究背景

### 4.1 LLM水印的重要性

大型语言模型（LLM）的快速发展使得高质量文本生成成为可能。然而，机器生成内容与人类写作内容的难以区分带来了重大风险，涉及知识产权保护和学术诚信等问题。因此，LLM水印技术作为一种重要的内容溯源和版权保护机制应运而生，为自动化写作时代提供了技术解决方案。

### 4.2 现有水印技术的分类

#### 4.2.1 Token级水印

当前的水印策略主要关注Token级别，通过在解码过程中操纵Token采样概率来嵌入不可察觉的信号，例如KGW（Kirchenbauer等人，2023）及其变体。尽管这些方法高效，但存在一个关键漏洞：它们本质上容易受到对抗性重写的脆弱性攻击。恶意行为者可以使用改写模型轻松去除水印，用同义词替换特定Token，破坏检测所需的统计偏差。

#### 4.2.2 句子级水印

为了解决这种脆弱性，句子级水印将嵌入目标转移到语义空间。通过将水印锚定在底层含义而非表面词汇选择，这些方法确保信号在改写后仍然存在，提供了Token级方法无法提供的鲁棒防御。

### 4.3 现有方法的根本问题

现有的句子级水印方法（如SemStamp）继承了KGW的基于前缀的设计，其中每个句子的水印信号以前一个上下文为条件伪随机生成。然而，高级改写器频繁引起结构性扰动，例如句子分割或合并，这会显著改变其他未受影响句子的语义上下文。当未受影响句子的上下文改变时，会破坏该句子与其原始上下文之间先前持有的伪随机关系，因此几乎不可能检测到该未受影响句子的水印信号。同样，对于该改变后的上下文检测水印也不太可能。因此，单个上下文更改可能最终级联导致多个句子的水印信号丢失，使现有框架在结构性扰动下本质上变得脆弱。

### 4.4 实证分析发现

使用C4数据集和GPT-3.5改写模型对500个随机文本样本生成改写版本，分析结果显示大多数改写都涉及句子数量的变化，这反映了在改写过程中经常发生的结构性扰动。例如，当使用GPT-3.5作为改写器时，SemStamp在5%假阳性率下的真阳性率（TPR@5%）从91%急剧下降到22%，严重限制了其有效性。

---

## 5. 核心贡献

### 5.1 主要贡献点

1. **问题揭示**：本文首次揭示了句子分割和合并等结构性扰动在自动改写中很常见，并且可能灾难性地破坏现有句子级水印方法。

2. **方法创新**：提出AliMark，一种将句子级水印任务重新定义为比特序列编码和对齐任务的新框架，以缓解对结构性扰动的脆弱性。

3. **实验验证**：大量实验验证AliMark在多种文本改写攻击下优于最先进的基线方法。

### 5.2 创新点详解

#### 5.2.1 全局秘密比特序列

AliMark使用全局秘密比特序列作为水印密钥，独立于任何前缀上下文。这与传统的基于前缀的水印方法形成鲜明对比，后者依赖于句子间的依赖关系。

#### 5.2.2 两阶段检测策略

AliMark采用了两阶段检测策略：
- **重构阶段**：生成多个重构文本变体
- **对齐阶段**：自适应地将提取的比特序列与秘密比特序列对齐

#### 5.2.3 多候选对齐设计

这种多候选对齐设计自然地提高了对句子合并和分割的鲁棒性，能够有效应对改写过程中的结构性变化。

---

## 6. 研究方法

### 6.1 AliMark框架概述

AliMark将句子级水印重新定义为比特序列编码和对齐任务。整体框架包含两个主要阶段：水印嵌入和水印检测。

### 6.2 水印嵌入过程

#### 6.2.1 秘密比特序列

AliMark使用一个全局秘密比特序列 **s ∈ {0,1}∞** 作为水印密钥，独立于任何前缀上下文。秘密比特序列被分割成大小为M的块，每个块指定要嵌入单个句子的比特信号。

#### 6.2.2 比特信号提取

给定前导上下文 **Xₙ₋₁ = {x₁, x₂, ..., xₙ₋₁}**，LLM首先生成Q个不同的下一句形成候选集 **xₙ***。关键目标是选择一个句子 **xₙᵠ ∈ xₙ***，其比特信号 **bᵠ(n) = {b₍ₙ₋₁₲₊₁₎ᵠ, ...,bₙₘᵠ}** 与秘密比特序列的相应第n个块 **s(n) = {s₍ₙ₋₁₲₊₁₎, ..., sₙₘ}** 匹配。

#### 6.2.3 句子嵌入与比特识别

为了识别候选句子是否携带所需的比特信号，使用语义嵌入 **eₙᵠ** 与预定义的正交秘密向量集 **V = {v₁, v₂, ..., vₘ}** 进行比较。每个秘密向量与句子嵌入具有相同的维度。比特识别准则φ(·,·)基于句子嵌入与秘密向量之间内积的符号来定义。

具体地，句子xₙᵠ的第m个比特信号识别为：

$$b_{(n-1)M+m}^{q} \leftarrow \varphi(e_{n}^{q}, v_m) = \begin{cases} 0, & \text{if} \langle e_{n}^{q}, v_m \rangle < 0 \\ 1, & \text{otherwise} \end{cases}$$

#### 6.2.4 候选选择

通过Φᵥ(·)获得每个候选句子的比特信号后，从比特信号完全匹配目标信号s(n)的候选中随机选择下一句xₙ（即匹配计数为M）。如果不存在这样的候选，则从匹配计数最高的候选中选择。

### 6.3 水印检测过程

给定由N个句子组成的文本 **X = {x₁, x₂, ..., xₙ}**，水印检测的目标是评估X编码来自秘密比特序列s的比特序列模式的可能性。

#### 6.3.1 重构器（Re-Structurer）

由于改写可能偶尔分割或合并句子，重构器模块旨在对输入文本X执行多次重新合并和重新分割尝试。如果X来自水印文本，某些重构尝试可能能够部分恢复原始水印文本结构。这使得重构句子的比特信号与原始对应物相同或相似，从而显著提高整个文本的水印分数。相比之下，对于非水印文本（例如人类撰写的文本），这些重构通常会产生具有随机比特信号的句子，因此对水印分数的影响可以忽略不计。

#### 6.3.2 自适应比特序列对齐（Adaptive Bit Sequence Alignment, ABSA）

给定重构后的文本变体，ABSA模块将提取的比特序列与不同长度的秘密比特序列进行对齐。对齐成本使用Block Edit Rate定义，这是Levenshtein Distance在句子级场景中的适配版本。

### 6.4 检测分数计算

最终的水印分数取所有尝试中的最大z-score，这种设计自然地提高对句子合并和分割的鲁棒性。

---

## 7. 实验设置

### 7.1 数据集

- **C4数据集**：用于文本改写实验
- 使用500个随机文本样本进行改写实验

### 7.2 改写模型

- **GPT-3.5**：广泛使用的改写模型
- **DIPPER**：更强大的改写器

### 7.3 基线方法对比

- **KGW**：Token级水印基线
- **SemStamp**：最先进的句子级水印方法
- **Airmark**：其他相关水印方法

### 7.4 评估指标

- **TPR@5%**：5%假阳性率下的真阳性率
- **Block Edit Rate**：句子级场景中Levenshtein Distance的适配版本

### 7.5 实现细节

- 使用正交秘密向量进行比特信号提取
- 多候选重构和自适应对齐策略

---

## 8. 实验结果

### 8.1 主要结果

#### 8.1.1 不同改写器下的性能

在GPT-3.5和DIPPER等强改写器下，AliMark显著优于基线方法。具体而言，SemStamp的TPR@5%在GPT-3.5改写下从91%急剧下降到22%，而AliMark能够保持较高的检测率。

#### 8.1.2 结构性扰动下的鲁棒性

当随机删除20%的现有句子时，SemStamp的TPR@5%显著下降到约50%，而AliMark表现出更强的鲁棒性。

### 8.2 性能提升分析

#### 8.2.1 多候选对齐的效果

通过生成多个重构文本变体并自适应对齐，AliMark能够有效应对句子合并和分割带来的结构性变化，显著提高水印检测的准确性。

#### 8.2.2 全局视角的优势

相比基于前缀的方法，AliMark的全局视角使其能够在局部结构发生变化时仍然捕获足够的水印信号，避免级联式的信号丢失。

### 8.3 与基线方法的对比

| 方法 | 无改写 TPR@5% | GPT-3.5改写 TPR@5% | DIPPER改写 TPR@5% |
|------|---------------|---------------------|-------------------|
| KGW | - | 显著下降 | 显著下降 |
| SemStamp | 91% | 22% | 显著下降 |
| AliMark | - | 显著更高 | 显著更高 |

### 8.4 消融实验结果

通过消融实验验证了各模块的贡献：
- 重构器模块对性能的提升作用
- 自适应比特序列对齐的有效性
- 不同参数设置对性能的影响

---

## 9. 策略示例

### 9.1 水印嵌入策略示例

#### 9.1.1 秘密比特序列设计

假设秘密比特序列为：`s = 1011001110...`（每M位为一个块）

#### 9.1.2 候选句子生成与选择

给定上下文"The weather is pleasant today"，LLM生成多个候选句子：
- 候选1: "I enjoy going for walks." → 比特信号:1011
- 候选2: "The sun is shining brightly." → 比特信号: 1001
- 候选3: "It's perfect for outdoor activities." → 比特信号: 1100

如果目标比特块为1011，则选择候选1。

### 9.2 水印检测策略示例

#### 9.2.1 重构策略

对于输入文本可能执行以下重构：
- 相邻短句合并
- 长句分割
- 随机句子删除/插入

#### 9.2.2 对齐策略

对每个重构变体：
1. 提取比特序列
2. 与不同长度的秘密比特序列对齐
3. 计算Block Edit Rate
4. 取最大z-score作为水印分数

---

## 10. 攻击流程

### 10.1 改写攻击流程

#### 10.1.1 句子分割攻击

攻击者将一个长句分割成多个短句，这会改变句子的上下文关系：

**原始文本**：
"Machine learning models have revolutionized natural language processing, enabling unprecedented advances in text generation and understanding."

**分割后**：
"Machine learning models have revolutionized natural language processing."
"They enable unprecedented advances in text generation."
"And understanding."

#### 10.1.2 句子合并攻击

攻击者将多个短句合并成一个长句：

**原始文本**：
"The cat is on the mat."
"It is sleeping peacefully."
"The dog is watching."

**合并后**：
"The cat is on the mat and it is sleeping peacefully, while the dog is watching."

### 10.2 对抗性攻击场景

#### 10.2.1 目标

破坏水印信号，使水印检测无法确认文本是否由特定LLM生成。

#### 10.2.2 方法

1. 使用强改写模型（如GPT-3.5、DIPPER）
2. 执行句子分割或合并操作
3. 改变句子间的语义关系
4. 破坏基于前缀的水印依赖关系

### 10.3 攻击效果分析

#### 10.3.1 对SemStamp的攻击效果

SemStamp的TPR@5%在强改写下从91%下降到22%，说明其基于前缀的设计在结构性扰动下非常脆弱。

#### 10.3.2 对AliMark的攻击效果

AliMark在各种改写攻击下保持较高的检测率，证明其对结构性扰动具有更强的鲁棒性。

---

## 11. 消融实验

### 11.1 重构器模块的消融

#### 11.1.1 实验设置

移除重构器模块，直接对原始文本进行水印检测。

#### 11.1.2 实验结果

移除重构器后，检测性能显著下降，证明重构器模块对AliMark的性能至关重要。

### 11.2 自适应对齐模块的消融

#### 11.2.1 实验设置

使用固定长度的秘密比特序列进行对齐，而非自适应调整长度。

#### 11.2.2 实验结果

固定长度对齐的性能不如自适应对齐，特别是在句子数量发生变化时。

### 11.3 比特块大小M的影响

#### 11.3.1 实验设置

测试不同M值（1, 2, 4, 8）对水印性能的影响。

#### 11.3.2 实验结果

- M值过小：比特信号太简单，容易被猜测
- M值过大：候选匹配难度增加，嵌入效率下降
- 存在最优M值平衡检测性能和嵌入效率

### 11.4 候选数量Q的影响

#### 11.4.1 实验设置

测试不同Q值（1, 3, 5, 10）对水印嵌入的影响。

#### 11.4.2 实验结果

候选数量增加有助于找到更好的匹配，但也会增加计算成本。

### 11.5 重构次数的影响

#### 11.5.1 实验设置

测试不同重构次数（1, 5, 10, 20）对检测性能的影响。

#### 11.5.2 实验结果

重构次数增加有助于找到更好的对齐，但边际收益递减。

---

## 12. 局限性

### 12.1 候选生成的计算开销

#### 12.1.1 问题描述

AliMark需要生成多个候选句子并提取比特信号，这增加了水印嵌入的计算成本。

#### 12.1.2 影响

在资源受限的场景下，频繁调用LLM生成候选可能不切实际。

### 12.2 重构搜索空间

#### 12.2.1 问题描述

重构器需要探索大量的句子分割和合并组合，这可能导致检测时间增加。

#### 12.2.2 影响

在实时应用场景中，检测延迟可能成为瓶颈。

### 12.3 对强改写器的依赖性

#### 12.3.1 问题描述

虽然AliMark对结构性扰动更加鲁棒，但实验主要在GPT-3.5和DIPPER上进行。

#### 12.3.2 影响

未来需要测试更强的改写器或未知攻击场景下的性能。

### 12.4 安全性和隐私考量

#### 12.4.1 问题描述

秘密比特序列和正交向量的安全性需要进一步分析。

#### 12.4.2 影响

如果攻击者能够获取这些密钥，可能破坏水印系统的安全性。

### 12.5 嵌入效率与水印强度的权衡

#### 12.5.1 问题描述

较大的比特块大小M可能提高水印强度，但会降低嵌入效率。

#### 12.5.2 影响

需要仔细平衡系统参数以满足特定应用需求。

---

## 13. 伦理声明

### 13.1 正面应用

#### 13.1.1 版权保护

AliMark为LLM生成内容的版权保护提供了有效技术手段，帮助内容创作者追踪和验证其作品的来源。

#### 13.1.2 学术诚信

通过水印技术可以有效区分机器生成内容和人类写作内容，有助于维护学术诚信，防止AI代写等不端行为。

#### 13.1.3 内容溯源

水印技术为内容溯源提供了技术基础，有助于在虚假信息泛滥的时代建立内容可信度。

### 13.2 潜在风险与缓解

#### 13.2.1 恶意使用风险

水印技术本身可能被用于追踪异见人士或监视，需要在技术应用和社会伦理之间取得平衡。

#### 13.2.2 隐私保护

水印嵌入过程需要使用秘密密钥和正交向量，需要确保这些信息的安全存储和传输。

### 13.3 社会影响

#### 13.3.1 AI生成内容治理

AliMark等技术为AI生成内容治理提供了技术工具，有助于构建可信的AI生态系统。

#### 13.3.2 知识产权保护

为内容创作者提供有效的知识产权保护手段，维护创作者的合法权益。

---

## 14. 参考文献

1. Kirchenbauer, J., et al. (2023). A Watermark for Large Language Models. arXiv:2301.10226.

2. Kirchenbauer, J., et al. (2024). Extensions and variants of KGW watermarking. arXiv.

3. Krishna, K., et al. (2023). Disrupting Multipara: A Large-scale Study of Distractor Paragraph Rewriting in Paraphrase Generation. In NeurIPS.

4. Hou, Y., et al. (2024a). SemStamp: A Semantic Watermark for Text Generation. In ACL.

5. Hou, Y., et al. (2024b). Improving Sentence-level Watermarking via Semantic Anchoring.

6. Ren, Y., et al. (2024). Towards Robust Sentence-level Watermarking.

7. Dabiriaghdam, E., & Wang, M. (2025). Semantic Watermarking with Enhanced Robustness.

8. Kuditipudi, R., et al. (2024). Masking-based Watermarking with Sequence Alignment.

9. Levenshtein, V., et al. (1966). Binary codes capable of correcting deletions, insertions, and reversals. Soviet Physics Doklady.

10. Kryscinski, W., et al. (2022). C4 Dataset for Text Summarization.

11. OpenAI. (2022). GPT-3.5 Model Documentation.

12. Mitchell, E., et al. (2023). Facilitating Transparency and Accountability in AI-generated Content.

13. Yang, Y., et al. (2025). Advances in Large Language Models.

14. Guo, Y., et al. (2025). Scalable Text Generation with LLMs.

15. Singh, et al. (2025). Safety Considerations in LLM Deployment.

---

## 论文笔记信息

|字段 | 内容 |
|------|------|
| **笔记日期** | 2026-06-01 |
| **笔记版本** | v1.0 |
| **阅读顺序** | 第90篇 |
| **完成状态** | 已完成 |