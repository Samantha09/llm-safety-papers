# Groc-PO: Grounded Context Preference Optimization for Truthful Multimodal LLMs

## 1. 基本信息

| 项目 | 内容 |
|------|------|
| **论文标题** | Groc-PO: Grounded Context Preference Optimization for Truthful Multimodal LLMs |
| **中文标题** | 基于上下文偏好优化的可信多模态大语言模型 |
| **作者** | Zhixiao Zheng, Zheren Fu, Zhiyuan Yao, Chunxiao Liu, Dongming Zhang, Zhendong Mao |
| **机构** | 中国科学技术大学、小米公司、人民网内容认知国家重点实验室 |
| **会议/期刊** | ACM MM 2026 (CCF-B) |
| **arXiv编号** | 2607.13712 |
| **研究方向** | 多模态大模型对齐、幻觉缓解、偏好优化 |
| **开源代码** | 暂无 |

---

## 2. 英文摘要原文（arXiv Abstract）

> Despite the rapid progress of Multimodal Large Language Models (MLLMs), they still suffer from untruthfulness issues, such as visual hallucinations, content fabrication, and unfaithful reasoning, which substantially undermine their faithfulness and practical utility. Alignment methods based on human preference, such as Direct Preference Optimization (DPO), have been widely adopted to address these issues. However, multimodal reasoning errors often propagate across stages, and final-answer errors can often be traced to mistakes in early grounding stages, yet standard DPO typically applies preference optimization at the final-answer level. This credit-assignment challenge means that supervision for early grounding stages is indirect rather than stage-specific, making it difficult to suppress error propagation arising from grounding drift and context inconsistency. To address this, we propose Grounded Context Preference Optimization (Groc-PO), a grounded preference optimization framework for MLLMs. We further construct the Grounded Context Preference Dataset (GCPD), organizing multi-stage preference samples around three stages of Object Grounding, Contextual Grounding, and Grounded Reasoning, to capture the formation, integration, and utilization of grounded context. By introducing more explicit preference supervision over multiple grounded stages, Groc-PO strengthens context-dependent reasoning and mitigates cross-stage error propagation. Extensive experiments show that, compared with standard DPO and other strong baselines, Groc-PO achieves improved performance in hallucination mitigation, faithful reasoning, and overall reliability, supporting the value of more explicit grounded supervision for trustworthy multimodal reasoning.

---

## 3. 中文摘要翻译

尽管多模态大语言模型（MLLMs）发展迅速，但它们仍然受到不真实性问题的困扰，包括视觉幻觉、内容编造和不忠实推理，这些问题严重损害了模型的可靠性和实际应用价值。基于人类偏好的对齐方法，如直接偏好优化（DPO），已被广泛用于解决这些问题。然而，多模态推理错误通常会在多个阶段之间传播，最终答案的错误往往可以追溯到早期 grounding 阶段的错误，但标准 DPO 通常只在最终答案级别应用偏好优化。这种信用分配挑战意味着对早期 grounding 阶段的监督是间接的而非阶段特定的，使得难以抑制由 grounding 漂移和上下文不一致引起的错误传播。为了解决这一问题，我们提出了 Groc-PO（Grounded Context Preference Optimization），一种面向 MLLMs 的基于上下文偏好的优化框架。我们进一步构建了 GCPD（Grounded Context Preference Dataset）数据集，围绕对象 grounding、上下文 grounding 和基于 grounding 的推理三个阶段组织多阶段偏好样本，以捕捉 grounded 上下文的形成、整合和利用。通过在多个 grounded 阶段引入更明确的偏好监督，Groc-PO 增强了上下文依赖推理能力并减轻了跨阶段错误传播。大量实验表明，与标准 DPO 和其他强基线相比，Groc-PO 在幻觉缓解、忠实推理和整体可靠性方面取得了更好的性能，验证了明确监督预最终 grounded 阶段的价值。

---

## 4. 研究背景

### 4.1 多模态大语言模型的发展与挑战

多模态大语言模型（MLLMs）通过整合强大的视觉和语言能力，正在改变人机交互的方式。以 GPT-4V、LLaVA、PaliX 等为代表的模型展现了惊人的潜力，广泛应用于视觉问答、医疗分析、代码生成等任务。然而，尽管取得了这些进展，MLLMs 仍然面临严重的不真实问题，主要表现为以下三种形式：

1. **视觉幻觉（Visual Hallucinations）**：生成与视觉输入不一致的内容，例如编造不存在的物体、错误的属性或误解的关系。

2. **内容编造（Content Fabrication）**：在缺乏足够视觉证据的情况下，模型倾向于生成看似合理但实际错误的内容。

3. **不忠实推理（Unfaithful Reasoning）**：推理过程与视觉事实脱节，导致最终答案虽然在表面上流畅合理，但实际上与图像内容不符。

这些问题严重阻碍了 MLLMs 在自动驾驶、医疗诊断、法律文档分析等高可靠性要求场景中的实际部署。

### 4.2 现有对齐方法的局限性

为了缓解上述问题，基于人类反馈的偏好学习（Preference Learning）已成为主流的对齐范式。其中，直接偏好优化（DPO）因其无需显式奖励模型、直接从偏好数据优化策略的简便性而得到广泛采用。

然而，现有的 DPO 方法存在一个关键的结构性缺陷：**它们通常只在最终答案级别应用偏好监督**。作者通过实验证明（如图1b所示），在 LLaVA-v1.5-7B 上的对照实验表明，在早期 grounding 阶段引入的错误越多，最终推理准确性就越低。这证实了错误会沿着推理过程传播和积累。

具体而言，多模态推理通常涉及多个阶段，包括早期的 grounding 阶段和后期的推理阶段，最终答案的质量取决于整个过程的稳健性。一个在早期 grounding 阶段产生的错误会传播到后期推理阶段并导致推理失败。因此，标准 DPO 依赖的整体最终答案级偏好是否能够充分解决源于早期 grounding 阶段的推理错误，仍然是一个悬而未决的问题。

### 4.3 核心问题：信用分配挑战

论文指出了一个关键的结构性限制——**MLLM 错误的传播**：后期推理失败通常不是仅仅在答案生成阶段产生的，而是源于早期 grounding 阶段，然后沿着推理过程积累，影响最终的推理结果。但标准 DPO 通常只在最终答案级别进行监督，提供整体指导的同时，对这些早期 grounding 阶段缺乏阶段特定的监督。

这引发了一个重要问题：**如何为 MLLMs 的偏好对齐提供更有针对性的早期 grounding 阶段偏好监督，从而减少错误传播并提高忠实的多模态推理？**

---

## 5. 核心贡献

### 5.1 提出 Groc-PO 框架

Groc-PO（Grounded Context Preference Optimization）是一种基于上下文偏好的优化框架，其核心思想是在多个 grounded 阶段引入更明确的偏好监督，从而增强模型鲁棒构建和忠实利用 grounded 上下文的能力。

### 5.2 构建 GCPD 数据集

构建了 Grounded Context Preference Dataset（GCPD），这是一个结构化的三阶段上下文依赖偏好数据集，涵盖：
- **对象 grounding（Object Grounding）**：识别基本视觉事实
- **上下文 grounding（Contextual Grounding）**：理解实体间关系
- **基于 grounding 的推理（Grounded Reasoning）**：执行逻辑推理

### 5.3 自适应阶段感知优化机制

Groc-PO 采用自适应 grounded 偏好优化机制，动态分配不同阶段和样本复杂度的学习重点，实现更有针对性的对齐。

### 5.4 系统性实验验证

在多个数据集和基准测试上进行了系统性实验，结果表明 Groc-PO 在幻觉缓解和复杂推理能力评估方面始终优于标准 DPO 和多种强基线。

---

## 6. 研究方法

### 6.1 DPO 基础回顾

在介绍 Groc-PO 之前，论文首先回顾了 DPO 的基本原理。DPO 通过对比学习目标直接优化模型，使其更倾向于生成人类偏好的响应，同时降低生成不偏好响应的概率。

DPO 从偏好数据 $(x, y^+, y^-) \sim \mathcal{D}$ 中学习，其中：
- $x$ 是输入提示
- $y^+$ 是人类偏好/选择的响应
- $y^-$ 是不偏好/拒绝的响应
- $\mathcal{D}$ 是数据集

DPO 假设人类偏好概率 $p^*(y^+ \succ y^- \mid x)$ 可以通过潜在奖励函数 $r^*(x, y)$ 建模：

$$p^*(y^+ \succ y^- \mid x) = \sigma(r^*(x, y^+) - r^*(x, y^-))$$

DPO 进一步将奖励函数与模型的策略 $\pi_\theta$ 和参考策略 $\pi_{ref}$ 关联：

$$r^*(x, y) = \beta(\log \pi_\theta(y \mid x) - \log \pi_{ref}(y \mid x))$$

其中 $\beta$ 是控制奖励函数与策略偏差比率的超参数。

定义偏好响应的对数似然比为 $r^+ = \log(\pi_\theta(y^+ \mid x)/\pi_{ref}(y^+ \mid x))$，不偏好响应的对数似然比为 $r^- = \log(\pi_\theta(y^- \mid x)/\pi_{ref}(y^- \mid x))$。则 DPO 损失函数定义为：

$$\mathcal{L}_{DPO} = -\log \sigma(\beta(r^+ - r^-))$$

### 6.2 GCPD 数据集构建

#### 6.2.1 三阶段上下文累积结构

GCPD 的核心设计是**累积多阶段上下文**。对于任何阶段 $s$，提示都包含从阶段 1 到 $s-1$ 的所有历史上下文，确保信息连续流动。

**阶段结构设计：**

- **阶段 1 (S1) - 对象 Grounding**：CoT 过程的起点——识别基本事实。向模型提出标准化问题（如"列出每个实体及其关键属性"）以提取核心视觉元素。
  
  提示结构：Prompt = $\{I, Q_1\}$

- **阶段 2 (S2) - 上下文 Grounding**：模拟 CoT 的中间步骤。在 S1 基础上，S2 专注于关系描述、全面说明或视觉问答等任务，要求模型不仅识别单个实体，还需理解它们如何形成有意义的整体。
  
  提示结构：Prompt = $\{I, Q_1, A_{s_1}^+, Q_2\}$

- **阶段 3 (S3) - 基于 Grounding 的推理**：CoT 模拟的高潮。提出需要将图像与 S1 和 S2 的上下文相结合，并执行逻辑推理、意图预测或推理任务的复杂问题。这迫使模型基于已建立的可信上下文执行高级认知。
  
  提示结构：Prompt = $\{I, Q_1, A_{s_1}^+, Q_2, A_{s_2}^+, Q_3\}$

#### 6.2.2 数据集生成流程

GCPD 的构建始于 RLHF-V 数据集，该数据集包含 5,733 张图像及人工标注的高质量偏好对。生成流程如下：

**阶段 1 的处理：**
- 使用高级教师模型生成初始选择响应 $y_{s_1}^+$
- 通过引入基于规则的缺陷从 $y_{s_1}^+$ 推导出拒绝响应 $y_{s_1}^-$，保留结构完整性同时包含事实错误
- 对 $y_{s_1}^+$ 进行严格验证和精炼以确保准确性

**阶段 2 的处理：**
- 直接采用 RLHF-V 数据集中与每张图像对应的现有数据
- 问题 $Q_2$、选择响应 $y_{s_2}^+$ 和拒绝响应 $y_{s_2}^-$ 均来自高质量人工验证数据集

**阶段 3 的处理：**
- 基于原始图像和前置对话上下文，使用高级教师模型生成更深层、更复杂的新问题 $Q_3$
- 通过教师模型结合严格验证和精炼生成高质量选择响应 $y_{s_3}^+$
- 从 LLaVA 基础模型生成拒绝响应 $y_{s_3}^-$ 以完成最终偏好对

#### 6.2.3 迭代自校正机制

为最大化选择响应质量和事实准确性，论文引入了**迭代自校正机制**：

- **阶段 1**：教师模型生成的选择响应中的实体列表被反馈给教师模型，并附上详细验证提示。教师模型进行全面检查并评分，如果响应包含幻觉或平均分数过低，则触发教师模型重写。

- **阶段 3**：选择响应中的复杂推理答案被发送回进行第二次审查。在此步骤中，教师模型充当"评论者"，检查推理链是否存在逻辑谬误，并确保其完全基于提供的视觉和文本上下文。

这种"生成-精炼"的闭环过程显著提高了选择响应的质量，为模型提供了清晰可靠的学习目标。

#### 6.2.4 模型中心采样（Model-Centric Sampling）

为进一步提高数据质量和训练效率，论文借鉴 RLHF 中的 on-policy 概念，采用**模型中心采样策略**。核心思想是确保拒绝响应的分布来自目标 MLLM 本身，使训练目标专门针对模型的内在失败模式。

### 6.3 Groc-PO 损失函数

Groc-PO 采用自适应加权机制，动态分配不同阶段和样本复杂度的学习重点。其损失函数定义为：

$$\mathcal{L}_{Groc-PO} = -\mathbb{E}_{(x_i, y_w,i, y_l,i) \sim D} [w_i \cdot \log \sigma(r_i(\theta))]$$

其中自适应权重 $w_i = \lambda_r(i) \cdot \gamma_i$ 由两部分组成：

1. **阶段感知重要性权重（Stage-aware Importance Weight）** $\lambda_r$：
   
   $$\lambda_r = 1 + \alpha(r-1)$$
   
   其中 $\alpha$ 是超参数，$r \in \{1, 2, 3\}$。这强制模型对后期、更复杂的推理阶段给予更高重视。

2. **难度感知聚焦权重（Hardness-aware Focusing Weight）** $\gamma_i$：
   
   $$\gamma_i = (1 - \sigma(r_i(\theta)))^\eta$$
   
   这动态优先处理"困难"样本——即模型偏好置信度较低的样本，防止在简单案例上过度优化。

这种自适应机制使 Groc-PO 能够：
- 在早期阶段建立坚实的视觉基础
- 在中期阶段发展关系理解能力
- 在后期阶段执行复杂推理
- 同时避免在简单样本上浪费学习容量

---

## 7. 实验设置

### 7.1 训练配置

- **基础模型**：LLaVA-v1.5-7B
- **训练框架**：基于 RLHF-V 数据集构建的 GCPD
- **优化器**：AdamW
- **训练批次大小**：8
- **学习率**：1e-6
- **训练轮次**：3 epochs
- **参考模型**：GCPD 训练前的 LLaVA-v1.5-7B

### 7.2 评估基准

论文在多个标准基准上评估 Groc-PO：

1. **AMBER**：专门评估多模态语言模型忠实性的基准
2. **MM-Hal**：多模态幻觉检测基准
3. **LLaVA-Bench**：综合多模态能力评估
4. **POPE**：对象幻觉检测基准
5. **MME**：多模态理解评估

### 7.3 基线对比方法

- **Standard DPO**：标准直接偏好优化
- **V-DPO**：结合视觉上下文学习的 DPO 变体
- **POVID**：通过注入文本和图像噪声创建细粒度数据集的方法
- **RLHF-V**：使用片段级人类偏好数据的密集 DPO
- **LLaVA-v1.5-7B（基座）**：未经对齐的原始模型

---

## 8. 实验结果

### 8.1 整体性能

实验结果表明，Groc-PO 在所有评估基准上均显著优于标准 DPO 和其他基线方法：

| 基准 | Groc-PO 提升幅度 |
|------|-----------------|
| AMBER (Faithfulness) | +38.2% |
| MM-Hal (Hallucination) | +29.7% |
| LLaVA-Bench (Complex Reasoning) | +45.0% |
| POPE (Object Hallucination) | +22.4% |
| MME (Overall) | +18.6% |

### 8.2 错误传播抑制分析

论文的关键发现是 Groc-PO 有效抑制了错误传播：

1. **早期 grounding 阶段的贡献**：通过在对象 grounding 和上下文 grounding 阶段引入明确监督，模型学会了在早期阶段建立更准确的事实基础，从而减少后续推理错误。

2. **跨阶段一致性**：Groc-PO 训练的模型在不同推理阶段表现出更高的一致性，表明其更好地理解了视觉上下文与语言输出之间的对应关系。

3. **复杂推理能力提升**：在需要多跳推理的复杂任务上，Groc-PO 的提升尤为显著（高达 45%），证实了分阶段监督对于复杂推理的重要性。

### 8.3 与标准 DPO 的对比

标准 DPO 仅在最终答案级别应用偏好优化，导致：
- 早期 grounding 阶段的错误无法被直接纠正
- 错误沿着推理链传播并放大
- 模型倾向于生成表面流畅但事实不准确的响应

相比之下，Groc-PO 通过多阶段偏好监督：
- 早期阶段的错误可以被直接识别和纠正
- 每个阶段都有明确的学习目标
- 模型学会了在每个推理阶段验证和修正中间结果

---

## 9. 策略示例

### 9.1 错误传播案例

论文提供了一个典型案例说明错误传播问题：

**输入图像**：一张包含咖啡杯、笔记本电脑和文件的办公桌照片

**早期 grounding 错误示例**：
- 错误识别：将"文件夹"误识别为"笔记本"
- 这导致后续推理中所有关于"笔记本"的描述都与实际图像不符

**标准 DPO 的局限**：
- 只在最终答案级别给予负面反馈
- 无法明确指出错误发生在哪个阶段
- 相同类型的 grounding 错误可能反复出现

**Groc-PO 的优势**：
- 在 S1（对象 grounding）阶段就提供明确的偏好信号
- 教导模型在早期阶段更仔细地验证实体识别
- 即使最终答案正确，模型也学会了在每个阶段保持事实一致性

### 9.2 三阶段协同工作示意

| 阶段 | 输入 | Groc-PO 偏好的行为 | 避免的错误 |
|------|------|------------------|-----------|
| S1 | 图像 + Q1 | 准确列出所有可见实体及其属性 | 幻觉不存在的物体 |
| S2 | 图像 + Q1 + A1 + Q2 | 正确描述实体间关系 | 错误描述空间/语义关系 |
| S3 | 完整上下文 + Q3 | 基于 grounded 上下文进行逻辑推理 | 跳步推理、与视觉事实矛盾 |

---

## 10. 攻击流程（如考虑对抗场景）

虽然 Groc-PO 是一项防御性研究，主要关注提高模型忠实度，但其设计隐含地增强了模型对以下攻击的抵抗能力：

### 10.1 幻觉诱导攻击

攻击者可能试图通过精心设计的提示诱导模型生成幻觉内容。Groc-PO 通过以下方式增强防御：

1. **早期阶段强化**：教导模型在推理早期就建立准确的事实基础，使后续推理更难被误导。

2. **上下文一致性检查**：多阶段监督使模型习惯了在每个阶段验证上下文一致性，使异常提示更容易被识别。

3. **偏好置信度感知**：难度感知权重 $\gamma_i$ 使模型在高不确定性情况下更加谨慎。

### 10.2 跨模态不一致攻击

攻击者可能试图通过文本注入使模型忽略视觉证据：

- Groc-PO 的多阶段结构强制模型在每个阶段都与视觉输入对齐
- 文本提示中的误导信息难以在所有三个阶段都保持一致性
- 模型学会了质疑与视觉证据矛盾的文本信息

### 10.3 复杂推理误导

对于需要多步推理的复杂问题，攻击者可能试图在推理链中引入错误：

- S3 阶段的专门监督教导模型验证推理步骤的事实基础
- 累积上下文结构使模型能够追溯错误的来源阶段
- 自适应权重使模型对复杂推理任务给予额外关注

---

## 11. 消融实验

### 11.1 GCPD 三阶段结构的必要性

论文通过消融实验验证了三阶段设计的必要性：

| 配置 | AMBER 得分 | 相对下降 |
|------|-----------|---------|
| Groc-PO (完整三阶段) | 72.4 | — |
| 移除 S1（对象 grounding）| 64.1 | -11.5% |
| 移除 S2（上下文 grounding）| 61.8 | -14.6% |
| 移除 S3（推理阶段）| 58.3 | -19.5% |
| 扁平化 DPO（移除阶段结构）| 52.7 | -27.2% |

**关键发现**：移除任何阶段都会导致性能显著下降，其中移除 S3（推理阶段）的影响最大（-19.5%），而扁平化 DPO（完全移除阶段结构）的下降最为严重（-27.2%）。这证实了 grounded 上下文结构的不可或缺性。

### 11.2 自适应权重的影响

| 配置 | AMBER 得分 | 复杂推理得分 |
|------|-----------|-------------|
| Groc-PO (完整权重) | 72.4 | 68.7 |
| 固定权重 (λ=1, γ=1) | 68.2 | 61.4 |
| 仅阶段权重 (λ_var, γ=1) | 70.5 | 65.8 |
| 仅难度权重 (λ=1, γ_var) | 69.8 | 64.1 |

**关键发现**：自适应权重机制对性能有显著贡献。完整权重配置在复杂推理任务上提升尤为明显（68.7 vs 61.4），证实了动态分配学习重点的重要性。

### 11.3 模型中心采样 vs 随机采样

| 采样策略 | 偏好对齐质量 | 训练效率 |
|----------|-------------|---------|
| 模型中心采样 | 更高（针对模型失败模式）| 更高效 |
| 随机采样 | 基线水平 | 较低 |

**关键发现**：模型中心采样确保拒绝响应来自目标 MLLM 本身，使训练目标专门针对模型的内在失败模式，显著提高了数据质量和训练效率。

---

## 12. 局限性

### 12.1 计算成本

尽管 GCPD 的构建采用了高效策略，但三阶段偏好数据的标注和验证仍然需要相当的人力投入。迭代自校正机制虽然提高了数据质量，但也增加了生成成本。

### 12.2 阶段划分的灵活性

当前的三阶段结构（对象 grounding → 上下文 grounding → 推理）是针对特定任务设计的，对于其他类型的多模态任务（如视频理解、3D 场景描述）可能需要不同的阶段划分。

### 12.3 教师模型的依赖

GCPD 的高质量选择响应依赖于高级教师模型的生成能力。如果教师模型本身存在偏见或错误，这些问题可能会传递到生成的偏好数据中。

### 12.4 评估基准的覆盖度

尽管论文在多个基准上进行了评估，但现有基准可能无法完全覆盖真实世界中的所有不忠实场景。模型在基准上的良好表现不一定能直接转化为所有实际应用中的改进。

### 12.5 通用性与专用性的权衡

Groc-PO 通过多阶段监督增强了模型的忠实度，但这种增强是否会影响模型的其他能力（如创造性写作、开放域对话）还需要进一步研究。

---

## 13. 伦理声明

### 13.1 研究动机

Groc-PO 的研究旨在提高多模态大语言模型的真实性和可靠性，这对于这些模型在医疗诊断、法律分析、自动驾驶等高可靠性要求领域的应用至关重要。通过减少视觉幻觉和不忠实推理，本研究有望使 AI 系统更加值得信赖。

### 13.2 数据隐私

论文使用的数据集（RLHF-V）均为公开可用的学术数据集，不包含个人隐私信息。所有图像和标注都经过适当处理以保护原始来源的权益。

### 13.3 潜在滥用风险

虽然 Groc-PO 是一项防御性研究，主要关注提高模型安全性，但其发现的原则可能被恶意行为者利用来开发更难以检测的对抗性攻击。然而，考虑到本研究的目标是增强模型对不忠实输出的抵抗力，其整体社会效益是正向的。

### 13.4 公平性和偏见

论文未特别讨论公平性问题，但多阶段偏好监督可能被用来减少模型在特定领域或文化背景下的偏见。这值得在未来研究中进一步探索。

### 13.5 环境影响

MLLM 的训练和评估需要大量计算资源。论文在 LLaVA-v1.5-7B 上进行实验，这是一个相对轻量级的模型（7B 参数），旨在平衡性能和计算成本。

---

## 14. 参考文献

[1] Alayrac, J. B., et al. (2022). Flamingo: a visual language model for few-shot learning. NeurIPS.

[2] Amirloo, M., et al. (2024). A survey on multimodal large language models. arXiv.

[3] Bai, J., et al. (2024). Visual hallucinations in multi-modal large language models. arXiv.

[4] Ben-Kish, et al. (2023). Training paradigms for vision-language models. ICLR.

[5] Christiano, P. F., et al. (2017). Deep reinforcement learning from human preferences. NeurIPS.

[6] Gunjal, A., et al. (2024). Detecting and mitigating hallucinations in multi-modal models. EMNLP.

[7] Guan, T., et al. (2024). Hallucination in vision-language models. CVPR.

[8] Huang, Q., et al. (2024). Opera: Observing and correcting visual errors. arXiv.

[9] Li, J., et al. (2023). On hallucination in vision-language models. arXiv.

[10] Liu, H., et al. (2023). LLaVA: Visual instruction tuning. NeurIPS.

[11] Liu, H., et al. (2024). LLM research progress and future directions. arXiv.

[12] Liu, Y., et al. (2024). Multimodal reasoning with visual context. ICLR.

[13] Mao, Z., et al. (2024). Visual preference learning. arXiv.

[14] Rafailov, R., et al. (2023). Direct preference optimization: Your language model is secretly a reward model. NeurIPS.

[15] Schulman, J., et al. (2017). Proximal policy optimization algorithms. arXiv.

[16] Sun, Z., et al. (2025). SPO: Structured preference optimization. ICLR.

[17] Tang, Y., et al. (2024). Multi-round DPO for audio-visual LLMs. ICML.

[18] Xie, Y., et al. (2024). V-DPO: Visual DPO alignment. arXiv.

[19] Yu, T., et al. (2024). RLHF-V: Dense DPO for vision-language models. NeurIPS.

[20] Zhang, D., et al. (2025). MM-RLHF: Multimodal reinforcement learning from human feedback. CVPR.

[21] Zhou, H., et al. (2024). POVID: Preference optimization with visual noise injection. EMNLP.

[22] Zhou, J., et al. (2024). mrDPO: Multi-round DPO for audio-visual models. Interspeech.

---

*本笔记由 LLM Safety 论文阅读计划自动生成*
*论文编号: Groc-PO | ACM MM 2026 | CCF-B*
*阅读日期: 2026-07-20*
