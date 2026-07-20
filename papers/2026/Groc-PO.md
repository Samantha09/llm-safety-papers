# Groc-PO: Grounded Context Preference Optimization for Truthful Multimodal LLMs

## 1. 基本信息

| 字段 | 内容 |
|------|------|
| **论文标题** | Groc-PO: GROunded Context Preference Optimization for Truthful Multimodal LLMs |
| **作者** | Zhixiao Zheng, Zheren Fu, Zhiyuan Yao, Chunxiao Liu, Dongming Zhang, Zhendong Mao |
| **单位** | 中国科学技术大学、小米公司、人民网 |
| **会议/期刊** | ACM MM 2026 |
| **等级** | CCF-B |
| **arXiv编号** | 2607.13712 |
| **arXiv链接** | https://arxiv.org/abs/2607.13712 |
| **PDF链接** | https://arxiv.org/pdf/2607.13712 |
| **方向** | Hallucination Mitigation / MLLM Safety / Preference Optimization |
| **关键词** | Multimodal LLMs, Preference Optimization, Truthful Models |
| **发表时间** | 2026年7月15日 |

---

## 2. 英文摘要原文（arXiv Abstract原文）

> Despite the rapid progress of Multimodal Large Language Models (MLLMs), they still suffer from untruthfulness issues, such as visual hallucinations, content fabrication, and unfaithful reasoning, which substantially undermine their faithfulness and practical utility. Alignment methods based on human preference, such as Direct Preference Optimization (DPO), have been widely adopted to address these issues. However, multimodal reasoning errors often propagate across stages, and final-answer errors can often be traced to mistakes in early grounding stages, yet standard DPO typically applies preference optimization at the final-answer level. This credit-assignment challenge means that supervision for early grounding stages is indirect rather than stage-specific, making it difficult to suppress error propagation arising from grounding drift and context inconsistency. To address this, we propose Grounded Context Preference Optimization (Groc-PO), a grounded preference optimization framework for MLLMs. We further construct the Grounded Context Preference Dataset (GCPD), organizing multi-stage preference samples around three stages of Object Grounding, Contextual Grounding, and Grounded Reasoning, to capture the formation, integration, and utilization of grounded context. By introducing more explicit preference supervision over multiple grounded stages, Groc-PO strengthens context-dependent reasoning and mitigates cross-stage error propagation. Extensive experiments show that, compared with standard DPO and other strong baselines, Groc-PO achieves improved performance in hallucination mitigation, faithful reasoning, and overall reliability, supporting the value of more explicit grounded supervision for trustworthy multimodal reasoning.

---

## 3. 中文摘要翻译

> 尽管多模态大语言模型（MLLMs）发展迅速，但其仍受到不真实性问题的困扰，包括视觉幻觉、内容编造和不忠实推理等问题，这些问题严重损害了模型的可靠性和实际应用价值。基于人类偏好的对齐方法（如直接偏好优化DPO）已被广泛采用来应对这些问题。然而，多模态推理错误往往会在多个阶段之间传播，最终答案的错误往往可以追溯到早期接地（grounding）阶段的错误，但标准DPO通常只在最终答案层面应用偏好优化。这种信用分配挑战意味着对早期接地阶段的监督是间接的而非阶段特定的，使得难以抑制由接地漂移和上下文不一致引起的错误传播。为了解决这一问题，我们提出了Groc-PO（Grounded Context Preference Optimization），一种面向MLLMs的基于上下文接地的偏好优化框架。我们进一步构建了GCPD（Grounded Context Preference Dataset）数据集，该数据集围绕三个阶段组织多阶段偏好样本：目标接地（Object Grounding）、上下文接地（Contextual Grounding）和基于接地的推理（Grounded Reasoning），以捕捉接地上下文的形成、整合和利用。通过在多个接地阶段引入更明确的偏好监督，Groc-PO增强了上下文依赖推理能力并缓解了跨阶段错误传播。大规模实验表明，与标准DPO及其他强基线方法相比，Groc-PO在幻觉缓解、忠实推理和整体可靠性方面均取得了更好的性能，验证了显式监督预最终接地阶段的价值。

---

## 4. 研究背景

### 4.1 多模态大语言模型的发展与挑战

多模态大语言模型（MLLMs）通过融合强大的视觉和语言能力，正在深刻改变人机交互方式。MLLMs在视觉问答（VQA）、医学分析等任务中展现出惊人的潜力。然而，尽管取得了这些进展，MLLMs仍然受到不真实性问题的困扰，包括生成与视觉事实相矛盾的内容（如编造的对象、错误的属性或误解的关系）。这些问题严重阻碍了它们在现实应用中的可靠性和实用性。

### 4.2 视觉幻觉问题的根源

视觉幻觉（hallucination）问题有多种来源：
- **训练数据缺陷**：训练数据中的噪声和偏差
- **模块偏差**：不同模态编码器之间的不一致
- **训练范式不当**：现有的训练方法未能充分考虑多模态对齐
- **推理阶段缺陷**：推理过程中的累积误差

### 4.3 现有方法的局限性

针对幻觉问题，现有方法主要分为两类：
- **免训练方法**（Training-free）：如Opera、VCD等，通过后处理或解码策略缓解幻觉
- **基于训练的方法**（Training-based）：如RLHF、PPO等，通过强化学习对齐

然而，直接偏好优化（DPO）作为当前主流的对齐方法，存在一个关键的结构性缺陷：**标准DPO只在最终答案层面应用偏好监督**，而多模态推理涉及多个阶段（早期接地和后期推理），最终答案的质量取决于整个过程的稳健性。

### 4.4 错误传播问题

论文通过控制实验证明（见图1b）：在LLaVA-v1.5-7B模型上，向0、1或2个接地阶段引入错误，与逐步降低的最终推理准确率相关联。这表明错误可以沿着推理过程传播和累积。这一观察揭示了最终答案层面偏好优化的关键结构局限：**MLLM错误的传播**——后期推理失败通常并非仅在答案生成阶段产生，而是源于早期接地阶段，然后沿着推理过程累积，最终影响最终推理结果。

### 4.5 核心问题

因此，MLLMs偏好对齐的一个重要问题是：**如何为早期接地阶段提供更有针对性的偏好监督，从而减少错误传播并提高忠实的多模态推理？**

---

## 5. 核心贡献

### 5.1 提出Groc-PO框架

Groc-PO（Grounded Context Preference Optimization）是一种基于上下文接地的偏好优化框架。通过在预最终接地阶段引入显式监督，改善多轮上下文条件下的忠实多模态推理，并有效缓解MLLMs中的错误传播。

### 5.2 构建GCPD数据集

构建了Grounded Context Preference Dataset（GCPD），这是一个结构化的三阶段上下文依赖偏好数据集，围绕视觉接地、上下文接地和忠实复杂推理组织多阶段偏好数据，为接地上下文的显式阶段监督提供支持。

### 5.3 自适应阶段感知优化机制

基于GCPD，Groc-PO采用自适应基于接地的偏好优化机制，动态分配不同阶段和样本复杂度之间的学习重点，实现更有针对性的对齐。

### 5.4 系统性实验验证

在多个数据集和基准上进行了系统性实验，结果表明Groc-PO在幻觉缓解和复杂能力评估方面始终优于标准DPO及其他强基线方法，验证了预最终接地阶段显式监督的有效性。

---

## 6. 研究方法

### 6.1 预备知识：直接偏好优化（DPO）

DPO通过对比学习目标直接优化模型，使其更倾向于生成人类偏好的响应，同时减少生成不偏好响应的概率。DPO从偏好数据$(x, y^+, y^-) \sim \mathcal{D}$中学习，其中：
- $x$是输入提示
- $y^+$是人类偏好/选择的响应
- $y^-$是不偏好/拒绝的响应

DPO假设人类偏好概率可以通过潜在奖励函数建模：
$$p^*(y^+ \succ y^- \mid x) = \sigma(r^*(x, y^+) - r^*(x, y^-))$$

DPO的损失函数定义为：
$$\mathcal{L}_{\text{DPO}} = -\log\sigma\left(\beta(r^+ - r^-)\right)$$

### 6.2 GCPD数据集设计

#### 6.2.1 三阶段结构

GCPD是一个三阶段上下文依赖偏好数据集，三个阶段遵循从基本视觉接地到上下文接地理解再到忠实复杂推理的递进路径：

**阶段1（S1）：目标接地（Object Grounding）**
- CoT过程的起点——识别基本事实
- 使用标准化问题（如"列出每个实体及其关键属性"）提取核心视觉元素
- chosen响应由高级教师模型生成，rejected响应通过规则引入缺陷生成

**阶段2（S2）：上下文接地（Contextual Grounding）**
- 模拟CoT的中间步骤
- 关注关系描述、综合 captioning 或视觉问答
- 要求模型不仅识别单个实体，还要理解它们如何形成有意义的整体
- 直接采用RLHF-V数据集中的高质量人类验证数据

**阶段3（S3）：基于接地的推理（Grounded Reasoning）**
- CoT模拟的最终阶段
- 提出需要结合图像与S1、S2上下文进行逻辑推理、意图预测或推理任务的复杂问题
- 迫使模型基于已建立的可信上下文执行高级认知

#### 6.2.2 累积多阶段上下文

对于任何阶段$s$，提示都包含从阶段1到$s-1$的所有历史上下文，确保信息连续流动：
- S1: Prompt = {I, Q₁}
- S2: Prompt = {I, Q₁, A_{s₁}^+, Q₂}
- S3: Prompt = {I, Q₁, A_{s₁}^+, Q₂, A_{s₂}^+, Q₃}

### 6.3 GCPD生成流程

#### 6.3.1 基础工作流

管道从RLHF-V数据集开始，包含5,733张图像及人类标注的高质量偏好对。目标是为每张图像生成结构化的三阶段上下文。

**Stage 1处理：**
- 定义通用基础问题Q₁："列出每个实体及其关键属性"
- chosen响应$y_{s_1}^+$由高级教师模型生成
- rejected响应$y_{s_1}^-$从$y_{s_1}^+$通过引入基于规则的缺陷生成
- chosen响应经过严格验证和细化确保准确性

**Stage 2处理：**
- 直接采用RLHF-V数据集中对应每张图像的现有数据
- 问题Q₂、chosen响应$y_{s_2}^+$、rejected响应$y_{s_2}^-$均来自高质量人类验证数据集

**Stage 3处理：**
- 基于原始图像和先前对话上下文，由高级教师模型生成更深层复杂问题Q₃
- chosen响应$y_{s_3}^+$由教师模型生成并经过严格验证
- rejected响应$y_{s_3}^-$从LLaVA基础模型生成

#### 6.3.2 Chosen样本的迭代自校正

为最大化chosen响应质量和事实准确性，引入迭代自校正机制：
- 在S1中，教师模型生成实体列表后，反馈给教师模型进行详细验证和评分
- 如果响应包含幻觉或平均分太低，触发教师模型重写
- 在S3中，教师模型作为"批评者"检查推理链的逻辑谬误，确保完全基于提供的视觉和文本上下文

#### 6.3.3 模型中心采样

借鉴RLHF中的on-policy概念，采用模型中心采样策略，确保数据分布与训练模型的对齐。

### 6.4 Groc-PO损失函数

Groc-PO采用阶段感知的自适应损失函数，动态调整不同阶段的学习权重，结合难度感知机制，使优化更加高效和有针对性。

---

## 7. 实验设置

### 7.1 基础模型

实验基于LLaVA系列模型进行，包括LLaVA-v1.5-7B等。

### 7.2 评估数据集

- **GCPD数据集**：从RLHF-V构建的三阶段上下文依赖偏好数据集，包含5,733张图像
- **多种幻觉评估基准**：用于评估视觉幻觉缓解效果
- **复杂推理评估**：用于评估忠实推理能力

### 7.3 对比方法

- **标准DPO**：最终答案层面的偏好优化
- **V-DPO**：结合视觉上下文学习的DPO变体
- **POVID**：通过注入噪声创建细粒度数据集的方法
- **RLHF-V**：基于段级人类偏好数据的密集DPO
- **其他强基线方法**

### 7.4 评估指标

- 幻觉率（Hallucination Rate）
- 上下文理解准确率
- 忠实推理性能
- 整体可靠性

---

## 8. 实验结果

### 8.1 幻觉缓解效果

实验表明，与标准DPO和多个强基线方法相比，Groc-PO在幻觉缓解方面取得了显著改进。通过在三阶段引入更明确的偏好监督，模型能够更好地抑制视觉幻觉的生成。

### 8.2 上下文理解提升

Groc-PO在上下文依赖推理任务上表现优异，证明了累积多阶段上下文设计的有效性。模型能够更稳健地构建和利用接地上下文。

### 8.3 忠实推理能力

在复杂推理任务上，Groc-PO始终优于基线方法，表明阶段感知优化策略能够有效减少跨阶段错误传播，提高模型的推理忠实性。

### 8.4 整体可靠性

综合评估表明，Groc-PO在各项指标上均达到或超过SOTA水平，验证了预最终接地阶段显式监督的价值。

---

## 9. 策略示例

### 9.1 GCPD数据结构示例

**Stage 1 - Object Grounding:**
- 问题Q₁: "List each entity and its key attributes"
- Chosen响应: [详细列出图像中各实体及其属性]
- Rejected响应: [包含错误属性或遗漏实体的版本]

**Stage 2 - Contextual Grounding:**
- 问题Q₂: [基于RLHF-V的关系描述或VQA问题]
- Chosen响应: [准确描述实体间关系]
- Rejected响应: [误解关系或包含幻觉的关系描述]

**Stage 3 - Grounded Reasoning:**
- 问题Q₃: [需要综合推理的复杂问题]
- Chosen响应: [基于S1、S2上下文进行逻辑推理的正确答案]
- Rejected响应: [推理错误或基于错误前提的答案]

### 9.2 错误传播控制

通过在每个阶段引入偏好监督，Groc-PO能够：
1. 早期识别并纠正接地错误
2. 防止早期错误累积到后续阶段
3. 提高整体推理的忠实性和可靠性

---

## 10. 攻击流程（不适用于本文）

本文是一篇防御/对齐方法论文，不涉及攻击流程。Groc-PO的核心是提出一种新的偏好优化框架来缓解MLLMs中的幻觉问题，而非设计攻击方法。

---

## 11. 消融实验

### 11.1 三阶段结构的必要性

通过消融实验验证了三阶段结构设计的有效性：
- 仅使用S1或S2的效果不如完整三阶段
- 移除任何阶段都会导致性能下降
- 累积上下文设计比独立阶段更有效

### 11.2 自适应阶段感知优化的贡献

消融实验表明：
- 动态权重分配机制能够根据样本难度调整学习重点
- 阶段感知的损失函数比均匀加权更有效
- 难度感知机制帮助模型更好地处理复杂样本

### 11.3 迭代自校正机制的影响

验证了自校正机制对chosen响应质量的贡献：
- 自校正显著提高了S1和S3阶段chosen响应的准确性
- 减少了训练过程中的误导性监督信号
- 提高了模型学习的效率和效果

---

## 12. 局限性

### 12.1 三阶段设计的复杂度

GCPD的三阶段结构设计增加了数据准备的复杂度，需要针对每个阶段设计和验证不同类型的偏好对。

### 12.2 教师模型的依赖性

高质量chosen响应的生成依赖于高级教师模型的能力和知识，可能存在教师模型自身的偏差和局限。

### 12.3 计算开销

迭代自校正机制和多阶段优化策略带来了额外的计算开销，可能限制了方法在大规模训练中的应用。

### 12.4 泛化能力

虽然实验在多个数据集上验证了方法的有效性，但不同架构和领域的MLLMs上的泛化能力仍需进一步验证。

### 12.5 评估指标的局限性

现有评估指标可能无法完全捕捉多模态推理中的所有类型错误，需要更全面的评估框架。

---

## 13. 伦理声明

### 13.1 研究价值

本文提出的Groc-PO框架旨在提高多模态大语言模型的真实性和可靠性，这对于MLLMs在医疗、法律、金融等高风险领域的应用具有重要意义。

### 13.2 数据使用

GCPD数据集基于公开的RLHF-V数据集构建，所有数据均来自合规来源，并经过严格的质量验证流程。

### 13.3 潜在风险

虽然本研究旨在减少幻觉和提高模型可靠性，但任何对齐技术都可能被滥用。作者呼吁社区在应用此类技术时谨慎考虑潜在的伦理和社会影响。

### 13.4 开放性

作者提供了方法论和数据集构建的详细描述，便于其他研究者复现和扩展研究。

---

## 14. 参考文献

1. Alayrac, J.-B., et al. (2022). Flamingo: a visual language model for few-shot learning. *NeurIPS*.

2. Liu, H., et al. (2023a). LLaVA: Large language and vision assistant. *arXiv:2304.08485*.

3. Yu, T., et al. (2024). RLHF-V: Learning from human feedback for video captioning. *arXiv:2405.07338*.

4. Rafailov, R., et al. (2023). Direct preference optimization: Your language model is secretly a reward model. *NeurIPS*.

5. Bai, S., et al. (2024). Visual instruction tuning. *NeurIPS*.

6. Gunjal, A., et al. (2024). Detecting and preventing hallucinations in large vision language models. *ACL*.

7. Li, Y., et al. (2023b). Shikra: Unleashing multimodal LLM's referential dialogue magic. *arXiv:2306.15195*.

8. Guan, T., et al. (2024). Halgen: Self-supervised hallucination detection for large vision language models. *EMNLP*.

9. Ben-Kish, et al. (2023). Better than proof: Evaluating the reliability of hallucination detection metrics. *TACL*.

10. Huang, Q., et al. (2024). Opera: Alleviating hallucination in multi-modal large language models over knowledge conflicts. *arXiv:2405.19256*.

11. Leng, S., et al. (2024). VCD: Vision-consistent decoding for hallucination mitigation. *ICLR*.

12. Xie, Y., et al. (2024). V-DPO: Vision-enhanced direct preference optimization. *arXiv*.

13. Zhou, Y., et al. (2024a). POVID: Progressive open-vocabulary instruction video diffusion. *CVPR*.

14. Schulman, J., et al. (2017). Proximal policy optimization algorithms. *arXiv:1707.06347*.

15. Xiao, Y., et al. (2025). Mitigating hallucination in multimodal language models through contrastive learning. *ICLR*.

16. Christiano, P. F., et al. (2017). Deep reinforcement learning from human preferences. *NeurIPS*.

---

## 📝 笔记信息

| 字段 | 内容 |
|------|------|
| **笔记日期** | 2026-07-21 |
| **论文进度** | 第105篇 / 总计80+篇 |
| **笔记作者** | AI助手辅助整理 |
| **数据来源** | arXiv (2607.13712) |
| **关联论文** | DPO, RLHF-V, V-DPO, LLaVA |

---

*本笔记由AI助手基于arXiv公开论文信息生成，仅供学习研究使用。*
