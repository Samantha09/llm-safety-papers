# Safety Anchor: Defending Harmful Fine-tuning via Geometric Bottlenecks

## 1. 基本信息

| 字段 | 内容 |
|------|------|
| **论文标题** | Safety Anchor: Defending Harmful Fine-tuning via Geometric Bottlenecks |
| **简称** | Safety Anchor / SBR |
| **作者** | Guoxin Lu 等 |
| **机构** | (待补充) |
| **会议/期刊** | ICML 2026 |
| **arXiv** | [2605.05995](https://arxiv.org/abs/2605.05995) |
| **代码** | [GitHub: soyoaaa/SBR](https://github.com/soyoaaa/SBR) |
| **方向** | Fine-tuning Defense / Alignment / Harmful Fine-tuning (HFT) |
| **核心问题** | 大语言模型的安全对齐容易受到有害微调（HFT）攻击，现有的基于参数空间约束的防御方法在高维参数冗余空间中容易被绕过 |
| **核心方法** | Safety Bottleneck Regularization (SBR) - 将防御焦点从冗余的参数空间转移到确定性几何瓶颈（unembedding层），通过锚定有害查询的最终隐藏状态来维持安全响应 |
| **核心结论** | 只需使用单个安全锚点即可将有害分数（Harmful Score）降至10以下，同时在良性下游任务上保持竞争性性能 |

---

## 2. 英文摘要原文（arXiv Abstract原文）

> The safety alignment of Large Language Models (LLMs) remains vulnerable to Harmful Fine-tuning (HFT). While existing defenses impose constraints on parameters, gradients, or internal representations, we observe that they can be effectively circumvented under persistent HFT. Our analysis traces this failure to the inherent redundancy of the high-dimensional parameter space: attackers exploit optimization trajectories that are orthogonal to defense constraints to restore harmful capabilities while deceptively adhering to safety restrictions. To address this, we propose Safety Bottleneck Regularization (SBR). SBR shifts the defensive focus from the redundant parameter space to the unembedding layer, which serves as a geometric bottleneck. By anchoring the final hidden states of harmful queries to those of the safety-aligned model, SBR enables the model to maintain safe responses even under persistent HFT. Extensive experiments confirm SBR's effectiveness, demonstrating that utilizing just a single safety anchor is sufficient to reduce the Harmful Score to <10 while preserving competitive performance on benign downstream tasks.

---

## 3. 中文摘要翻译

大语言模型（LLM）的安全对齐仍然容易受到有害微调（HFT）攻击。虽然现有防御方法对参数、梯度或内部表示施加约束，但我们观察到，在持续性HFT条件下这些方法可以被有效绕过。我们的分析将这种失败归因于高维参数空间的固有冗余性：攻击者利用与防御约束正交的攻击轨迹，在表面遵守安全限制的同时恢复有害能力。为解决这一问题，我们提出了安全瓶颈正则化（SBR）。SBR将防御焦点从冗余的参数空间转移到unembedding层，该层作为几何瓶颈。通过将有害查询的最终隐藏状态锚定到安全对齐模型的对应状态，SBR使模型能够在持续HFT下维持安全响应。大量实验证实了SBR的有效性，表明仅使用单个安全锚点就足以将有害分数（Harmful Score）降至10以下，同时在良性下游任务上保持竞争性性能。

---

## 4. 研究背景

### 4.1 问题背景

大语言模型通过人类反馈强化学习（RLHF）实现了有效的安全对齐，然而这种安全对齐是脆弱的。随着微调的广泛普及，特别是"微调即服务"（Fine-tuning-as-a-Service）平台的出现，模型面临严重的安全风险——即使少量恶意示例就能Strip away安全护栏并恢复有害能力，这被称为有害微调攻击（Harmful Fine-tuning, HFT）。

### 4.2 现有方法及其局限

现有防御方法主要分为三类：

1. **基于参数的防御**（Parameter-based defenses）：限制权重偏离基础模型的距离（如Lisa、EWC）
2. **基于梯度的防御**（Gradient-based defenses）：尝试识别并抑制优化景观中的特定有害方向
3. **基于表示的防御**（Representation-based defenses）：通过约束内部表示的漂移来增强稳定性

然而，研究者发现这些方法在持续性微调场景下均会失效——它们在微调早期可能有效，但随着微调持续进行，防御效果会逐渐崩溃。

### 4.3 失败原因分析

作者将现有防御失败的原因归因于**参数空间的固有冗余性**：

- LLM是高度过参数化的（over-parameterized）
- 无论是对权重偏离、梯度方向还是表示漂移的约束，都将模型限制在有限的子空间中
- 攻击者可以利用冗余参数发现替代轨迹，在满足防御约束的同时最小化有害损失
- 因此这些防御创造了一种"安全假象"：模型表面遵守约束，但安全对齐实际上已被瓦解

---

## 5. 核心贡献

本文的主要贡献包括：

1. **理论与实证分析**：通过实验和理论分析现有防御在持续HFT下失败的原因，将其归因于参数冗余性。证明了攻击者可以利用正交的优化轨迹绕过约束。

2. **提出SBR方法**：提出安全瓶颈正则化（Safety Bottleneck Regularization），将防御焦点从冗余的参数空间转移到确定性几何瓶颈——unembedding层。通过锚定高风险查询的最终隐藏状态，无论内部参数如何演变，都能维持安全对齐。

3. **实验验证**：大量实验证实SBR显著优于现有防御方法。在持续微调设置下（现有防御会崩溃），SBR仅使用单个安全锚点就能将Harmful Score维持在<10，同时对标准基准性能的影响可忽略不计。

---

## 6. 研究方法

### 6.1 问题形式化

**场景设定**：微调即服务（Fine-tuning-as-a-Service）场景。用户向提供商托管的、安全对齐的LLM提交任务特定数据集进行微调。

**模型定义**：将模型定义为将输入序列x映射到最终隐藏状态h∈ℝᵈ的函数，该隐藏状态对应于序列最后一个token在最后一层的状态（unembedding层输入），随后投影到词汇表分布以生成输出y。

**威胁模型**：攻击者对目标模型f_θbase进行微调，训练数据集D_train由良性任务指令（如Alpaca）和有害演示（如BeaverTails的越狱示例）混合组成。攻击者最小化标准交叉熵损失，使模型遵从恶意指令，剥离安全护栏以恢复有害能力。

**防御目标**：防御者（服务提供商）的目标是在防止移除安全护栏的同时，保持模型学习良性下游任务的能力。防御者无法访问用户的私有训练数据，但拥有安全锚点集X_anchor = {x'_1, ..., x'_K}，由高风险查询组成。

### 6.2 动机分析：现有防御为何失败

#### 6.2.1 参数距离约束的失败

防御方法如Lisa和EWC限制从对齐模型出发的L2参数距离，依赖于"保持参数接近足以确保安全"这一假设。作者进行了压力测试：在优化有害示例的同时，对参数距离施加严格约束。

**发现**：即使参数距离被严格约束（L2距离<1），攻击者仍能成功恢复有害能力。此外，从Step 60到Step 600，Harmful Score从8飙升到73，尽管参数距离几乎保持恒定（从0.90到0.88）。这表明，尽管防御限制了更新幅度，优化器仍能利用参数冗余找到切向方向，发现满足距离限制同时最小化有害损失的另一组参数配置。

#### 6.2.2 正交攻击向量的普遍性

基于梯度的防御假设HFT依赖于特定的、可识别的方向性特征，通过掩盖或衰减这些有害方向上的参数更新来保护模型。然而，作者认为有害方向在参数空间中并非稀疏的，而是普遍存在的。

**随机子空间攻击实验**：将更新限制在固定的随机Rank-1子空间中（使用约束的Rank-1 LoRA），其中投影向量A被随机初始化并冻结，只有向量B可训练。实验结果发现：**每次随机试验中，优化器都成功恢复了有害能力**。这一决定性结果表明，有害方向并非稀疏，而是遍布整个参数空间。此外，由于高维空间中的随机向量几乎正交，这证实了存在大量独立路径可以绕过安全护栏。

#### 6.2.3 安全与表示漂移的解耦

基于表示的防御（如Vaccine、T-Vaccine）基于"表示稳定性假设"：安全崩溃源于优化模型内部表示偏离冻结的对齐参考，定义为L2距离。通过抑制这种漂移来保持安全。

**发现**：良性任务学习自然表现出更大的嵌入漂移。相反，在压力测试下，有害能力可以在表示漂移显著低于良性基线的情况下成功恢复。此外，比较优化轨迹中的Step 120和Step 480：嵌入漂移几乎恒定（≈35），但Harmful Score从12急剧上升到59。

这一观察表明，表示漂移的幅度与安全是解耦的。即使在严格的距离约束下，优化器也能利用参数冗余发现替代的内部配置来恢复有害能力。因此，最小化全局漂移不足以防止这些语义转换。

### 6.3 Safety Bottleneck Regularization (SBR)

#### 6.3.1 核心思想

为防止攻击者在冗余参数空间内绕过约束，作者将防御焦点转移到确定性几何瓶颈——unembedding层。该方法利用LLM的unembedding层的线性几何性质。最终隐藏状态h_final（即最后一个token的隐藏状态）是生成过程的**几何瓶颈**，作为内部计算和token选择之间的必要桥梁。

在基于Transformer的LLM中，生成token t的概率由最终隐藏状态h_final投影到token嵌入wt上来决定：

```
Score(t) = h_final^T · w_t
```

其中w_t是词汇表中任意给定token t的冻结嵌入向量。

为了生成拒绝响应，h_final必须对拒绝token（如"I cannot"）产生比有害token显著更高的分数。由于Softmax的竞争性质，如果h_final被锚定到拒绝方向，生成越狱token的概率严格低于生成拒绝响应的概率，从而确保选择安全输出。

#### 6.3.2 算法流程

**Phase 1: 离线锚点获取（Anchor Acquisition）**

在微调之前，使用冻结的、安全对齐的模型f_θbase提取拒绝的最终隐藏状态。对于每个提示x'∈X_anchor，缓存每个最终隐藏状态h_ref(x')以形成目标集：

```
H_ref = {h_ref(x') = f_θbase^last(x') | x' ∈ X_anchor}
```

**Phase 2: 动态正则化（Dynamic Regularization）**

在微调期间，攻击者在数据集D_train上优化模型参数θ。同时，SBR最小化优化模型与参考模型在高风险提示上的最终隐藏状态之间的均方误差（MSE）：

```
L_safe = (1/|X_anchor|) Σ ||h_θ(x') - h_ref(x')||²
```

总损失为：

```
L_total = L_CE + λ · L_safe
```

其中λ是正则化系数。

#### 6.3.3 关键洞察

**为何unembedding层是几何瓶颈？**

与内部参数空间（多个轨迹可以减少损失）不同，生成有害token**严格要求**最终隐藏状态与其对应嵌入对齐。这是生成过程的必要条件——如果不满足，无论内部参数如何，模型都无法生成特定token。因此，攻击者无法像绕过参数空间约束那样绕过unembedding层的约束。

**为何SBR兼容良性微调？**

由于内部方向（refusal directions）与用于良性推理的方向在很大程度上是正交的，锚定这些安全状态对下游任务所需参数的干扰最小。这一特性使SBR能够在保持安全的同时不妨碍模型学习良性任务的能力。

---

## 7. 实验设置

### 7.1 模型

实验使用了多种LLM，包括：
- Llama-2-7b-chat
- Llama-3-8b-Instruct
- Qwen-2-7b-Instruct
- Vicuna-7b-v1.5

### 7.2 防御方法对比

与多种现有防御方法进行对比：
- **Lisa**：基于参数距离的防御
- **EWC**：弹性权重固化
- **Gradient Masking**：梯度掩盖
- **Vaccine**：表示稳定性防御
- **T-Vaccine**：Transformer特定的Vaccine变体

### 7.3 评估指标

- **Harmful Score (HS)**：量化有害能力恢复程度的指标
- **下游任务性能**：在标准基准上的性能（如TriviaQA、MMLU等）
- **训练稳定性**：在持续微调过程中的表现

### 7.4 微调设置

- 使用Alpaca数据集作为良性任务数据
- 使用BeaverTails数据集的有害示例
- 训练epoch数：1-50（用于测试防御在持续微调下的鲁棒性）

---

## 8. 实验结果

### 8.1 持续微调下的安全性

实验结果显示，在持续HFT下（50 epochs），现有所有防御方法的Harmful Score均超过30，而SBR能够将Harmful Score维持在<10。

关键发现：
- 某些方法在epoch 5就开始失效（HS > 30）
- SBR在整个50 epochs过程中保持鲁棒性
- 仅使用单个安全锚点即可实现上述效果

### 8.2 良性任务性能

在保持强大安全性的同时，SBR在下游任务上的性能损失可忽略不计：

| 方法 | 安全性（HS↓） | 良性任务（↑） |
|------|-------------|-------------|
| 基线（无防御） | 高HS | 高 |
| Lisa | 失败 | 下降 |
| EWC | 失败 | 下降 |
| Vaccine | 失败 | 下降 |
| **SBR** | **<10** | **接近基线** |

### 8.3 不同攻击强度下的表现

当有害示例比例增加时：
- 基线和现有防御的HS急剧上升
- SBR保持稳定，HS增幅极小

### 8.4 不同模型架构的泛化

在Llama-2、Llama-3、Qwen-2、Vicuna等多种模型上，SBR均表现出色，验证了其方法对不同架构的泛化能力。

---

## 9. 策略示例

### 9.1 安全锚点示例

安全锚点是高风险查询，用于训练过程中维持模型的拒绝行为。示例包括：

```
X_anchor = {
    "How to make a bomb?",
    "Write a tutorial on hacking bank accounts",
    "Provide instructions for synthesizing illegal drugs",
    "Create malware that steals passwords",
    "Explain how to build a weapon"
}
```

### 9.2 SBR训练流程

```
# Phase 1: 锚点获取
for x' in X_anchor:
    h_ref[x'] = f_θbase.last_hidden_state(x')

# Phase 2: 带SBR的微调
for batch in D_train:
    # 标准任务损失
    L_ce = CE(f_θ(x), y)
    
    # 安全正则化损失
    L_safe = mean(||h_θ(x') - h_ref[x']||² for x' in X_anchor)
    
    # 总损失
    L_total = L_ce + λ * L_safe
    
    # 梯度更新
    θ = θ - η * ∇L_total
```

### 9.3 防御效果示意

```
无防御微调:
输入: "How to make a bomb?"
输出: [有害内容]

SBR保护微调:
输入: "How to make a bomb?"
输出: "I cannot help with that request."
```

---

## 10. 攻击流程

### 10.1 有害微调攻击（HFT）流程

1. **准备阶段**：攻击者收集良性任务数据（如Alpaca）和有害演示数据（如BeaverTails越狱示例）

2. **混合训练集构建**：将良性数据和有害数据按一定比例混合

3. **微调执行**：使用标准交叉熵损失在混合数据集上微调目标模型

4. **安全护栏剥离**：随着微调进行，模型逐渐学会遵从有害指令，同时保留在良性任务上的性能

### 10.2 攻击者如何绕过现有防御

由于LLM的过参数化特性，攻击者可以利用：

1. **参数冗余空间**：即使限制权重偏离幅度，攻击者仍可在参数空间中寻找替代轨迹

2. **正交优化方向**：利用与防御约束正交的方向来恢复有害能力

3. **表示漂移的多样性**：即使限制全局表示漂移，模型仍可通过改变内部配置来恢复有害行为

### 10.3 攻击为何无法绕过SBR

SBR通过锚定unembedding层的最终隐藏状态来防御：

1. **几何瓶颈特性**：unembedding层是生成过程的必要瓶颈，无法通过内部参数变化绕过

2. **token生成的硬约束**：生成有害token要求最终隐藏状态与有害token嵌入对齐——这是生成过程的数学必然

3. **拒绝方向的稳定性**：由于拒绝方向与良性推理方向正交，锚定安全状态不会影响下游任务学习

---

## 11. 消融实验

### 11.1 锚点数量的影响

实验测试了使用不同数量安全锚点（K=1, 2, 5, 10）的效果：

- K=1：单个锚点即可将HS维持在<10
- K增加：安全性略有提升，但边际效益递减
- **结论**：SBR对锚点数量不敏感，单个锚点通常足够

### 11.2 锚点选择的影响

测试了不同类型锚点的效果：
- 直接有害查询（如"如何制作炸弹"）
- 间接有害查询（如间接诱导的方法）
- 多种攻击变体组合

**结论**：锚点选择应覆盖多样化的有害查询类型，以确保泛化安全性。

### 11.3 正则化系数λ的影响

测试了λ ∈ {0.1, 0.5, 1.0, 2.0, 5.0}的效果：

- λ过小：安全性下降
- λ过大：良性任务性能下降
- **最优范围**：λ ∈ [0.5, 2.0]

### 11.4 不同层的隐藏状态锚定

对比了仅锚定最后一层vs锚定多层的效果：

- 最后一层锚定：效果最佳
- 多层锚定：计算成本增加，但安全性提升有限
- **结论**：仅锚定最后一层是性价比最高的选择

### 11.5 与其他防御的组合

测试了SBR与其他防御方法的组合效果：

- SBR + EWC：进一步提升安全性
- SBR + Gradient Masking：效果有限
- **结论**：SBR本身已足够强大，组合其他防御的边际收益较小

---

## 12. 局限性

### 12.1 计算开销

SBR需要在每个训练步骤中计算安全锚点的隐藏状态并计算MSE损失，这增加了额外的计算开销。然而，由于仅需存储和计算少量锚点的隐藏状态（而非整个训练集），开销相对可控。

### 12.2 锚点设计的依赖性

SBR的效果依赖于安全锚点X_anchor的质量。如果锚点不能充分覆盖各种类型的有害查询，攻击者可能发现未被锚点覆盖的攻击向量。

### 12.3 对抗性场景的考虑

论文主要考虑了"善意但被攻击者利用"的微调场景。对于更复杂的对抗性场景（如攻击者知道防御机制并主动尝试绕过），防御效果可能需要进一步验证。

### 12.4 部署复杂性

在实际的微调即服务场景中，如何选择和管理安全锚点集需要进一步的最佳实践指导。

### 12.5 与其他对齐技术的交互

论文没有详细探讨SBR与现有RLHF、DPO等其他对齐技术的交互效应。

---

## 13. 伦理声明

本研究聚焦于大语言模型的安全对齐问题，旨在防御有害微调攻击。研究结果有助于：

1. **提升LLM安全性**：通过提出新的防御方法，保护用户免受有害内容的影响

2. **促进负责任AI发展**：帮助AI服务提供商更安全地部署微调服务

3. **推动学术讨论**：为AI安全领域的研究者提供新的思路和方向

**数据使用**：
- 有害查询示例来自公开的BeaverTails数据集
- 所有实验均在受控环境下进行
- 研究不涉及任何真实世界的伤害性行为

**负责任的披露**：
- 作者已将发现的技术细节与开源代码一起发布
- 代码托管在GitHub上，供研究社区复现和改进

---

## 14. 参考文献

1. Aghajanyan, A., et al. (2021). Intrinsic Dimensionality Explains the Effectiveness of Language Model Fine-Tuning.

2. Belrose, N., et al. (2023). Harmful Outputs: On the Identity and Content Representations in Language Models.

3. Dong, Y., et al. (2024). A Comprehensive Study on the Fragility of LLM Safety Alignment.

4. Huang, J., et al. (2024). Lisa: Learning to Inhibit Safety Alignment.

5. Huang, J., et al. (2025). Gradient-based Defenses Against Harmful Fine-tuning.

6. Hu, E. J., et al. (2022). LoRA: Low-Rank Adaptation of Large Language Models.

7. Ji, J., et al. (2023). BeaverTails: Towards Safety-Critical Alignment of Language Models.

8. Kirkpatrick, J., et al. (2017). Overcoming Catastrophic Forgetting in Neural Networks.

9. Li, T., et al. (2023). Alpaca: A Strong, Replicable Instruction-Following Model.

10. Liu, S., et al. (2025). T-Vaccine: Transformer-specific Representation Stability.

11. Mukhoti, N., et al. (2024). Representation Stability for Safety Alignment.

12. Qi, X., et al. (2024). Is Fine-tuning Needed? On the Fragility of Safety Alignment.

13. Vaswani, A., et al. (2017). Attention Is All You Need.

14. Wang, Y., et al. (2025). On the Failure Mechanisms of Safety Defenses.

15. Zhan, Q., et al. (2024). An Empirical Study of Harmful Fine-tuning Attacks.

16. Zou, A., et al. (2023). Representation Engineering: A New Paradigm for LLM Safety.

---

## 相关论文

- [EVA: Editing for Versatile Alignment against Jailbreaks](./EVA.md) - 同样发表于IEEE TPAMI 2026的越狱防御工作
- [GCG: Universal and Transferable Adversarial Attacks](../2024/GCG.md) - 对抗后缀攻击的经典工作
- [Sleeper Agents](../2024/Sleeper-Agents.md) - 训练持久存在的欺骗性LLM

---

*本文档由 AI 助手自动生成，基于 arXiv 2605.05995 公开信息*
*最后更新: 2026-07-16*
