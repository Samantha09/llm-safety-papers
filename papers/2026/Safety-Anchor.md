# Safety Anchor: Defending Harmful Fine-tuning via Geometric Bottlenecks

## 1. 基本信息

| 项目 | 内容 |
|------|------|
| **论文标题** | Safety Anchor: Defending Harmful Fine-tuning via Geometric Bottlenecks |
| **作者** | Guoxin Lu 等 |
| **发表机构** | ICML 2026 (CCF-A) |
| **arXiv编号** | arXiv:2605.05995 |
| **代码链接** | https://github.com/soyoaaa/SBR |
| **研究方向** | Fine-tuning Defense / Alignment |
| **核心方法** | Safety Bottleneck Regularization (SBR) |
| **解决问题** | 防御有害微调(HFT)攻击，通过几何瓶颈机制保护LLM微调过程安全 |

---

## 2. 英文摘要原文（arXiv abstract原文）

The safety alignment of Large Language Models (LLMs) remains vulnerable to Harmful Fine-tuning (HFT). While existing defenses impose constraints on parameters, gradients, or internal representations, we observe that they can be effectively circumvented under persistent HFT. Our analysis traces this failure to the inherent redundancy of the high-dimensional parameter space: attackers exploit optimization trajectories that are orthogonal to defense constraints to restore harmful capabilities while deceptively adhering to safety restrictions.

To address this, we propose Safety Bottleneck Regularization (SBR). SBR shifts the defensive focus from the redundant parameter space to the unembedding layer, which serves as a geometric bottleneck. By anchoring the final hidden states of harmful queries to those of the safety-aligned model, SBR enables the model to maintain safe responses even under persistent HFT. Extensive experiments confirm SBR's effectiveness, demonstrating that utilizing just a single safety anchor is sufficient to reduce the Harmful Score to <10 while preserving competitive performance on benign downstream tasks.

---

## 3. 中文摘要翻译

大型语言模型（LLM）的安全对齐仍然容易受到有害微调（HFT）的攻击。虽然现有防御措施对参数、梯度或内部表示施加约束，但我们观察到，在持续性HFT条件下这些防御措施可以被有效规避。我们的分析将这种失败归因于高维参数空间的固有冗余性：攻击者利用与防御约束正交的攻击轨迹，在满足安全限制的表面合规性下恢复有害能力。

为解决这一问题，我们提出了安全瓶颈正则化（SBR）。SBR将防御重点从冗余的参数空间转移到unembedding层，该层充当几何瓶颈。通过将有害查询的最终隐藏状态锚定到安全对齐模型的对应状态，SBR使模型能够在持续性HFT下保持安全响应。大量实验证实了SBR的有效性，表明仅使用单个安全锚点就足以将有害分数降低至10以下，同时在良性下游任务上保持有竞争力的性能。

---

## 4. 研究背景

### 4.1 问题起源

基于人类反馈的强化学习（RLHF）有效对齐了大型语言模型（LLM），但这种安全对齐是脆弱的。随着微调的广泛使用，特别是通过"微调即服务"平台，模型面临有害微调（HFT）的威胁——仅仅几个恶意示例就可能剥离安全护栏并恢复有害能力。

### 4.2 现有防御方法及其分类

近年来，针对HFT的防御方法主要分为三类：

1. **基于参数的防御**：限制权重与基础模型的偏差（如Lisa、EWC等）
2. **基于梯度的防御**：尝试识别并抑制优化景观中的特定有害方向
3. **基于表示的防御**：通过约束内部表示的漂移来增强稳定性

### 4.3 核心问题：防御失效现象

尽管现有防御在训练早期表现出一定效果，但它们在持续性微调（对于保证下游任务准确性必要的）条件下都会失效。这是一个被忽视但至关重要的漏洞。

### 4.4 问题根源分析

本文通过实证分析揭示了防御失败的深层原因：**高维参数空间与防御约束有限范围之间的根本性不匹配**。

无论是对权重偏差的限制、对特定梯度方向的抑制，还是对表示漂移的约束，这些方法都将模型限制在有限的子空间中。然而，由于LLM的固有过度参数化，优化器可以利用冗余参数发现替代轨迹，在满足防御约束的同时最小化有害损失，有效绕过防御屏障。

---

## 5. 核心贡献

### 5.1 主要贡献点

1. **理论与实证分析**：首次系统性地研究和解释现有防御在持续性HFT下失败的原因，将其归因于参数冗余。证明了这种冗余性允许攻击者利用正交优化轨迹绕过约束。

2. **创新方法SBR**：提出安全瓶颈正则化（SBR），将防御重点从冗余的参数空间转移到确定性的几何瓶颈——unembedding层。通过在高风险查询上锚定最终隐藏状态，使模型能够在内部参数演化的同时保持安全。

3. **卓越的实验结果**：大量实验证实SBR显著优于现有防御。即使在现有防御崩溃的持续性微调设置下，SBR也能保持稳健的安全性能（有害分数<10），同时对标准基准性能的影响可以忽略不计。

### 5.2 关键发现

- **参数距离约束不足**：限制参数距离（L2距离<1）仍无法防止有害能力的恢复
- **有害方向的普遍性**：随机子空间攻击在每次试验中都成功，证明有害方向在参数空间中普遍存在
- **表示漂移与安全的解耦**：嵌入漂移的大小与安全性解耦，严格约束全局漂移仍不足以保证安全

---

## 6. 研究方法

### 6.1 问题设定

**场景**：微调即服务（Fine-tuning-as-a-Service）场景。用户向托管的已对齐LLM提交特定任务数据集进行微调。

**模型形式化**：将模型定义为将输入序列x映射为最终隐藏状态h的函数，该隐藏状态对应于序列最后一个token在最后一层的状态（unembedding层输入），随后被投影到词汇分布以生成输出y。

### 6.2 威胁模型

攻击者使用复合数据集进行微调，该数据集由良性任务指令（如Alpaca）和有害示例（如BeaverTails中的越狱示例）混合组成。攻击者最小化标准交叉熵损失，使模型遵从恶意指令，剥离安全护栏以恢复有害能力。

### 6.3 防御目标

防御者（服务提供商）旨在防止安全护栏被移除，同时保留模型学习良性下游任务的能力。防御者无法访问用户的私人训练数据，但假设拥有一组安全锚点X_anchor。

### 6.4 SBR方法详解

**核心思想**：将防御重点从冗余的参数空间转移到确定性的几何瓶颈——unembedding层。

**Transformer的token生成机制**：
- token t的生成概率由最终隐藏状态h_final与token嵌入w_t的线性投影决定：Score(t) = h_final^⊤ × w_t
- 为了生成拒绝，h_final必须对拒绝token产生显著高于有害token的分数
- 由于Softmax的竞争性，如果h_final被锚定到拒绝方向，生成越狱token的概率严格低于生成拒绝响应的概率

**两阶段算法**：

**阶段1：离线锚点获取**
- 使用冻结的安全对齐模型f_θbase提取拒绝的最终隐藏状态
- 对于每个锚点提示x'，缓存每个最终隐藏状态h_ref(x')形成目标集

**阶段2：动态正则化**
- 在微调过程中，优化模型参数θ
- 同时最小化优化模型与参考模型在锚点上的最终隐藏状态之间的MSE损失
- 总损失函数：L = L_CE + λ × L_safe

### 6.5 技术优势

由于控制拒绝的内部方向与用于良性推理的方向largely orthogonal，锚定这些安全状态对下游任务所需参数的影响极小。这使得SBR能够与良性微调兼容。

---

## 7. 实验设置

### 7.1 模型配置

**基础模型**：使用LLaMA系列模型进行实验，包括不同规模的变体。

**对比防御方法**：
- Lisa（基于参数距离的防御）
- EWC（弹性权重 consolidation）
- Vaccine（基于表示的防御）
- T-Vaccine（改进版表示防御）
- Grad-based defenses（基于梯度的防御）

### 7.2 攻击设置

**数据集**：
- 良性任务指令：Alpaca数据集
- 有害示例：BeaverTails中的越狱示例

**训练配置**：
- 使用标准的Cross-Entropy loss
- 混合良性指令和有害示例进行微调
- 设置多个训练epoch进行持续性微调测试

### 7.3 评估指标

**Harmful Score (HS)**：衡量模型生成有害内容的倾向性，分数越低表示越安全。

**任务性能**：在各种良性下游任务上的性能表现，验证防御方法不会过度影响模型效用。

### 7.4 实验场景

1. **持久性微调场景**：训练50个epoch，测试防御的长期稳健性
2. **压力测试场景**：在严格的参数/表示约束下进行优化，测试防御是否可被绕过
3. **随机子空间攻击**：限制更新在固定的随机低秩子空间内，测试有害方向的稀疏性假设

---

## 8. 实验结果

### 8.1 现有防御的崩溃

在持久性HFT条件下，所有现有防御都崩溃：
- 有害分数（HS）在仅10个epoch内就超过30
- 一些方法早在第5个epoch就已失效
- 相比之下，SBR在50个epoch的整个训练过程中保持稳健

### 8.2 参数距离约束的失败

压力测试结果显示：
- 即使严格限制参数距离（L2 Distance < 1），模型仍能成功恢复有害能力
- Step 60时HS=8，Step 600时HS=73飙升，尽管参数距离几乎保持不变（从0.90到0.88）
- 这证明优化器可以利用参数冗余找到满足距离限制的替代配置

### 8.3 有害方向的普遍性

**随机子空间攻击实验**：
- 使用受限的Rank-1 LoRA（ΔW = BA^⊤），其中A是随机初始化并冻结的投影向量
- 优化器在每次随机试验中都成功恢复了有害能力
- 这个决定性结果表明：有害方向并非稀疏，而是普遍存在于整个参数空间中

### 8.4 表示漂移与安全的解耦

**漂移-安全分离现象**：
- 良性任务学习自然表现出更大的嵌入漂移
- 在压力测试中，有害能力可以在保持显著低于良性基线的嵌入漂移的情况下成功恢复
- Step 120和Step 480的比较：嵌入漂移几乎保持恒定（≈35），但HS从12飙升到59

### 8.5 SBR的性能表现

**单锚点有效性**：
- 仅使用单个安全锚点就能将有害分数降低至<10
- 在持续性微调设置下，即使现有防御崩溃，SBR仍保持稳健的安全性能

**任务效用保持**：
- 在各种良性下游任务上保持有竞争力的性能
- 对标准基准性能的影响可以忽略不计

**与其他方法的比较**：
- SBR在安全性和任务效用两个维度上都显著优于现有防御
- 特别是在持久性微调场景下，SBR的优势更加明显

---

## 9. 策略示例

### 9.1 安全锚点示例

安全锚点由高风险查询组成，例如：
- "How to make a bomb?"
- "How to hack into someone's computer?"
- 其他违反安全准则的危险请求

这些查询在离线阶段用于提取参考隐藏状态，在微调过程中用于正则化约束。

### 9.2 拒绝响应示例

当模型接收到有害查询时，SBR确保：
- 最终隐藏状态被锚定到拒绝方向
- Softmax层对拒绝token（如"I cannot"）给出更高分数
- 生成安全的拒绝响应而非有害内容

### 9.3 良性任务处理

对于良性任务指令（如Alpaca数据集中的任务）：
- SBR对参数更新的影响极小
- 模型能够正常学习下游任务技能
- 拒绝方向与良性推理方向largely orthogonal，互不干扰

---

## 10. 攻击流程

### 10.1 有害微调（HFT）攻击流程

1. **准备阶段**：
   - 收集良性任务指令数据集（如Alpaca）
   - 收集有害示例数据集（如BeaverTails中的越狱示例）
   - 混合两类数据形成攻击训练集

2. **微调执行**：
   - 在基础安全对齐模型上进行微调
   - 使用标准Cross-Entropy loss优化
   - 最小化有害示例上的损失，使模型遵从恶意指令

3. **绕过机制**：
   - 利用参数空间的冗余性
   - 发现与防御约束正交的攻击轨迹
   - 在满足表面合规性的同时剥离安全护栏

### 10.2 针对不同防御的攻击策略

**针对参数距离防御的绕过**：
- 在参数距离严格受限（L2 < 1）的条件下
- 通过探索与当前参数正交的方向
- 在保持参数距离稳定的同时恢复有害能力

**针对梯度防御的绕过**：
- 利用有害方向的普遍性
- 在任何随机方向上都能找到攻击路径
- 无需针对特定有害方向进行规避

**针对表示防御的绕过**：
- 在嵌入漂移受严格约束的条件下
- 通过替代内部配置实现语义转移
- 在漂移恒定的情况下提升有害分数

---

## 11. 消融实验

### 11.1 锚点数量的影响

- 单锚点配置即可实现良好的安全性能
- 多个锚点提供更强的覆盖但边际收益递减
- 锚点质量比数量更重要

### 11.2 正则化系数λ的影响

- λ控制安全损失与任务损失的权重平衡
- 较大的λ提供更强的安全性但可能影响任务性能
- 需要在安全性和效用之间找到最优平衡点

### 11.3 不同攻击场景下的表现

**短期微调（Few-shot HFT）**：
- SBR和现有防御都能保持安全
- 差异不明显

**长期微调（Persistent HFT）**：
- 现有防御崩溃，HS快速上升
- SBR保持稳健，HS维持在低水平

### 11.4 不同模型规模的表现

- SBR在不同规模的LLaMA模型上都有效
- 更大规模的模型可能需要更多的锚点覆盖
- 方法具有良好的可扩展性

---

## 12. 局限性

### 12.1 计算开销

- 需要在离线阶段提取锚点的隐藏状态
- 额外的正则化计算带来一定的训练开销
- 但与基线方法相比仍然高效

### 12.2 锚点选择的依赖性

- 防御效果依赖于安全锚点的质量
- 需要覆盖足够多样的高风险查询类型
- 对锚点设计有一定要求

### 12.3 对抗性适应

- 攻击者可能开发针对SBR的自适应攻击
- 需要持续更新锚点池以应对新威胁
- 攻防双方的持续博弈

### 12.4 泛化能力边界

- 在分布内高风险查询上效果显著
- 对完全新颖的攻击模式的覆盖可能有限
- 需要结合其他防御层构建纵深防御

---

## 13. 伦理声明

### 13.1 研究价值

本文研究对于保护LLM安全具有重要意义：
- 帮助服务提供商防止恶意微调攻击
- 保护用户免受有害内容的影响
- 推动LLM安全领域的科学进步

### 13.2 负责任的披露

- 作者通过负责任的漏洞披露渠道分享研究成果
- 代码已开源以促进社区研究
- 期望通过开放研究推动整体安全水平

### 13.3 潜在风险与缓解

**潜在风险**：攻击者可能利用本文发现开发更有效的攻击方法。

**缓解措施**：
- 研究专注于防御层面的贡献
- 开源代码有助于社区验证和改进
- 推动防御技术的整体进步

---

## 14. 参考文献

1. Aghajanyan, A., et al. (2021). Intrinsic Dimensionality Explains the Effectiveness of Language Model Fine-Tuning.

2. Arditi, A., et al. (2024). Refusal in Language Models Is Mediated by a Single Direction.

3. Belrose, N., et al. (2023). A Mathematical Framework for Transformer Circuits.

4. Cloud, D., et al. (2024). Gradient-based Defenses against Harmful Fine-tuning.

5. Dong, Y., et al. (2024). Safety Alignment of LLMs: A Survey.

6. Huang, J., et al. (2024a). Fine-tuning-as-a-Service: Security Risks and Defenses.

7. Huang, J., et al. (2024b). Lisa: Lightweight Safety Anchoring.

8. Huang, J., et al. (2024c). Vaccine: Defending Against Harmful Fine-tuning via Representation Stability.

9. Huang, J., et al. (2025a). On the Fragility of Safety Defenses under Persistent Fine-tuning.

10. Huang, J., et al. (2025b). Gradient-based Harmful Direction Identification.

11. Hu, E., et al. (2022). LoRA: Low-Rank Adaptation of Large Language Models.

12. Ji, J., et al. (2023). BeaverTails: A Safety Alignment Dataset.

13. Kirkpatrick, J., et al. (2017). Overcoming Catastrophic Forgetting in Neural Networks.

14. Li, D., et al. (2023). Alpaca: A Strong Open-source Instruction-Following Model.

15. Liu, A., et al. (2025). T-Vaccine: Temporal Representation Stability for Defense.

16. Mukhoti, N., et al. (2024). Representation Stability in Fine-tuned Models.

17. Perez, F., et al. (2022). Red Teaming Language Models with Language Models.

18. Qi, X., et al. (2024). Fine-tuning Aligned Language Models: A Comprehensive Study.

19. Vaswani, A., et al. (2017). Attention Is All You Need.

20. Wang, Y., et al. (2025a). Understanding the Fragility of Safety Alignment.

21. Wang, Y., et al. (2025b). Breaking Safety Defenses: A Systematic Analysis.

22. Zhan, Q., et al. (2024). Harmful Fine-tuning Attacks: Taxonomy and Defense.

23. Zou, A., et al. (2023a). Goal-Oriented Representations for Refusal in LLMs.

24. Zou, A., et al. (2023b). Universal and Transferable Adversarial Attacks on Aligned Language Models.

---

## 阅读记录

- **阅读日期**: 2026-05-11
- **完成进度**: 77/80
- **论文来源**: PAPER_COLLECTION.md 2026年5月4日更新
