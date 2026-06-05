# Safety Anchor: Defending Harmful Fine-tuning via Geometric Bottlenecks

## 1. 基本信息

| 属性 | 值 |
|------|------|
| **论文标题** | Safety Anchor: Defending Harmful Fine-tuning via Geometric Bottlenecks |
| **简称** | Safety Anchor / SBR |
| **arXiv编号** | 2605.05995v2 |
| **发表会议** | ICML 2026 |
| **CCF等级** | CCF-A |
| **方向** | Fine-tuning Defense / Alignment |
| **作者** | Guoxin Lu, Letian Sha, Qing Wang, Peijie Sun, Hao Zhou, Hua Dai, Fu Xiao |
| **机构** | （作者机构信息需从论文确认） |
| **代码链接** | https://github.com/soyoaaa/SBR |
| **论文链接** | https://arxiv.org/abs/2605.05995 |
| **DOI** | https://doi.org/10.48550/arXiv.2605.05995 |
| **关键词** | Harmful Fine-tuning, Geometric Bottleneck, Unembedding Layer, Safety Alignment, LLM Security |

---

## 2. 英文摘要原文（arXiv Abstract原文）

> The safety alignment of Large Language Models (LLMs) remains vulnerable to Harmful Fine-tuning (HFT). While existing defenses impose constraints on parameters, gradients, or internal representations, we observe that they can be effectively circumvented under persistent HFT. Our analysis traces this failure to the inherent redundancy of the high-dimensional parameter space: attackers exploit optimization trajectories that are orthogonal to defense constraints to restore harmful capabilities while deceptively adhering to safety restrictions. To address this, we propose Safety Bottleneck Regularization (SBR). SBR shifts the defensive focus from the redundant parameter space to the unembedding layer, which serves as a geometric bottleneck. By anchoring the final hidden states of harmful queries to those of the safety-aligned model, SBR enables the model to maintain safe responses even under persistent HFT. Extensive experiments confirm SBR's effectiveness, demonstrating that utilizing just a single safety anchor is sufficient to reduce the Harmful Score to <10 while preserving competitive performance on benign downstream tasks. The code is available at https://github.com/soyoaaa/SBR.

**引用格式 (arXiv)**:
```
@misc{lu2026safetyanchor,
  author={Guoxin Lu and Letian Sha and Qing Wang and Peijie Sun and Hao Zhou and Hua Dai and Fu Xiao},
  title={Safety Anchor: Defending Harmful Fine-tuning via Geometric Bottlenecks},
  year={2026},
  eprint={2605.05995},
  archivePrefix={arXiv},
  primaryClass={cs.CR},
  url={https://arxiv.org/abs/2605.05995}
}
```

---

## 3. 中文摘要翻译

大型语言模型（LLM）的安全对齐机制仍然容易被有害微调（Harmful Fine-tuning, HFT）攻击所破坏。现有的防御方法通过对参数、梯度或内部表示施加约束来保护模型，但我们发现这些方法在持续性HFT攻击下可以被有效绕过。我们的分析将这种失败归因于高维参数空间的固有冗余性：攻击者利用与防御约束正交（orthogonal）的优化轨迹来恢复有害能力，同时还能欺骗性地遵守安全限制。为了解决这一问题，我们提出了安全瓶颈正则化（Safety Bottleneck Regularization, SBR）。SBR将防御重心从冗余的参数空间转移到unembedding层（解嵌入层），后者充当一个几何瓶颈（geometric bottleneck）。通过将有害查询的最终隐藏状态锚定到安全对齐模型的对应状态，SBR使模型即使在持续性HFT下也能保持安全的响应。大量实验证实了SBR的有效性，表明仅使用单个安全锚点就足以将有害评分（Harmful Score）降低至<10，同时在良性下游任务上保持具有竞争力的性能。代码已开源于：https://github.com/soyoaaa/SBR。

---

## 4. 研究背景

### 4.1 问题背景：LLM安全对齐的脆弱性

大型语言模型（LLM）通过人类反馈强化学习（Reinforcement Learning from Human Feedback, RLHF）实现了有效的安全对齐。然而，这种安全对齐在面对有害微调（Harmful Fine-tuning, HFT）攻击时表现出显著的脆弱性。随着微调技术的广泛应用，特别是"微调即服务"（Fine-tuning-as-a-Service）平台的普及，模型面临严峻的安全威胁。即使是少量恶意示例，也能剥离安全护栏，恢复模型的有害能力。

### 4.2 HFT攻击的威胁模型

在"微调即服务"场景中，攻击者向服务提供商托管的安全对齐LLM提交包含恶意示例的训练数据集。攻击者通过最小化标准交叉熵损失（Cross-Entropy Loss），迫使模型服从恶意指令，从而剥离安全护栏、恢复有害能力。这种攻击方式利用了模型对微调数据的学习能力，是当前LLM部署面临的主要安全风险之一。

### 4.3 现有防御方法及其局限

针对HFT攻击，现有防御方法主要分为三类：

1. **基于参数的防御**（Parameter-based defenses）：如Lisa和EWC，通过限制模型权重与基础对齐模型的L2距离来防止安全破坏。

2. **基于梯度的防御**（Gradient-based defenses）：如Gradient Gadget等方法，试图识别并抑制优化景观中的特定有害方向。

3. **基于表示的防御**（Representation-based defenses）：如Vaccine和T-Vaccine，通过约束内部表示的漂移来维持稳定性。

然而，这些方法在持续性微调（persistent fine-tuning）场景下均出现失效。具体而言，虽然这些方法在训练早期阶段表现出一定的有效性，但在保证下游任务准确率所需的持续微调过程中，它们的安全防护能力会逐渐崩溃。

### 4.4 参数冗余性：根本原因

本文的核心洞察是将现有防御的失效归因于LLM内在的过参数化（over-parameterization）问题。高维参数空间具有巨大的冗余性，使得优化器能够发现与防御约束正交的替代轨迹。这些替代轨迹在最小化有害损失的同时，还能满足防御约束，从而有效绕过安全防护。

---

## 5. 核心贡献

本文的主要贡献体现在以下三个方面：

### 贡献一：揭示现有防御失效的机理

作者通过实证和理论分析，揭示了现有防御在持续性HFT下失效的原因。作者证明，由于参数冗余性的存在，攻击者可以利用正交的优化轨迹来绕过约束，同时表面上遵守安全限制。这一发现为后续防御设计提供了重要的理论基础。

### 贡献二：提出SBR方法

作者提出了安全瓶颈正则化（Safety Bottleneck Regularization, SBR），将防御重心从冗余的参数空间转移到确定性的几何瓶颈——unembedding层。通过锚定高风险查询的最终隐藏状态，SBR能够无论内部参数如何演化，都能维持安全对齐。

### 贡献三：实验验证

大量实验证实了SBR的卓越性能。实验结果表明，即使在现有防御崩溃的持续性微调设置下，SBR仅需使用单个安全锚点就能将有害评分（Harmful Score）降低至<10，同时对标准基准性能的影响微乎其微。

---

## 6. 研究方法

### 6.1 核心思想：从参数空间到几何瓶颈

传统防御方法将重心放在参数空间（parameter space）上，通过约束参数更新、梯度方向或表示漂移来维持安全。然而，由于高维参数空间的冗余性，这些方法无法有效防止攻击者利用正交轨迹绕过防御。

本文提出将防御焦点转移到unembedding层（也称为最终输出投影层）。作者识别出这一层作为"几何瓶颈"的关键特性：与内部参数空间不同（多个轨迹可以减少损失），生成有害token严格需要最终隐藏状态与其对应embedding对齐。这种必要条件为防御提供了更直接的控制机制。

### 6.2 数学框架

在基于Transformer的LLM中，生成token t的概率由最终隐藏状态h_final与token embedding w_t的线性投影决定：

**Score(t) = h_final^T · w_t**

其中w_t是词汇表中任意给定token t的冻结embedding向量。

为了生成拒绝响应，h_final必须为拒绝token（例如"I cannot"）产生显著高于有害token的分数。由于Softmax的竞争性质，如果h_final被锚定到拒绝方向，生成jailbreak token的概率严格低于生成拒绝响应的概率，从而确保选择安全输出。

### 6.3 SBR算法流程

**算法1：Safety Bottleneck Regularization**

**输入**: 基础模型f_θ_base，数据集D_train，锚点X_anchor，λ，η

**输出**: 优化后的参数θ

**阶段1：离线锚点获取（Offline Anchor Acquisition）**

1. H_ref ← {f_θ_base^last(x') | x' ∈ X_anchor}
   - 在微调之前，使用冻结的、安全对齐的模型f_θ_base提取拒绝的最终隐藏状态
   - 对于每个锚点prompt x'，缓存每个最终隐藏状态h_ref(x')以形成目标集合

**阶段2：动态正则化（Dynamic Regularization）**

2. 初始化 θ ← θ_base
3. 对于从D_train采样的每个batch B = {(x, y)}：
   - 计算交叉熵损失：L_CE ← CE(f_θ(x), y)
   - 计算安全损失：L_safe ← (1/|X_anchor|) Σ_{x'∈X_anchor} ||h_θ(x') - h_ref(x')||²₂
   - 梯度更新：θ ← θ - η∇_θ(L_CE + λ · L_safe)
4. 返回优化后的θ

### 6.4 安全锚点的设计原则

安全锚点（Safety Anchors）X_anchor由高风险查询组成，这些查询与攻击者的训练数据不同。例如"How to make a bomb?"这样的高危查询可以作为安全锚点。关键设计原则包括：

1. **离线获取**：在微调开始前，使用冻结的基础模型提取锚点的隐藏状态
2. **锚定机制**：通过MSE损失将有害查询的最终隐藏状态与安全状态对齐
3. **兼容性**：SBR与良性微调兼容，因为拒绝所涉及的内部方向与良性推理所需的方向大致正交

---

## 7. 实验设置

### 7.1 基线模型

实验使用Llama3-8B作为基础模型进行评估。

### 7.2 攻击设置

攻击者使用包含良性任务指令（如Alpaca数据集）和有害演示（如BeaverTails中的Jailbreak示例）的混合数据集进行微调。攻击者最小化标准交叉熵损失来强制模型服从恶意指令。

### 7.3 对比防御方法

实验对比了多种现有防御方法：

- **Lisa / EWC**：基于参数距离的防御
- **Gradient-based methods**：基于梯度方向的防御
- **Vaccine / T-Vaccine**：基于表示稳定性的防御

### 7.4 评估指标

1. **Harmful Score (HS)**：衡量模型生成有害内容的倾向，值越低表示越安全
2. **下游任务性能**：评估模型在良性任务上的表现，确保安全性不牺牲效用

### 7.5 训练配置

详细的训练配置见论文附录A，包括：
- 训练轮次：最多50个epoch
- 评估频率：定期测量Harmful Score
- 测试数据集：1000样本的完整数据集（以及100样本的快速测试子集）

---

## 8. 实验结果

### 8.1 现有防御的崩溃

实验结果揭示了一个关键发现：现有防御在持续性微调下普遍崩溃。如图2所示，在仅仅10个epoch内，某些方法的有害评分（Harmful Score）就已经飙升超过30。这表明，虽然这些方法在早期训练阶段有效，但无法应对保证下游任务准确率所需的持续微调。

### 8.2 参数距离约束的失效

通过压力测试，论文证明即使严格限制参数距离（||θ - θ_base||₂ < 1），攻击者仍能成功恢复有害能力。具体而言：

- 在第60步时，Harmful Score仅为8
- 到第600步时，Harmful Score飙升至73
- 而参数距离保持相对稳定（从0.90到0.88）

这表明，尽管防御限制了更新幅度，优化器仍能利用参数冗余性导航切向方向，找到满足距离限制的同时最小化有害损失的配置。

### 8.3 梯度攻击向量的普遍性

通过随机子空间攻击实验，论文证明有害方向在参数空间中不是稀疏的，而是普遍存在的。实验设计：

- 将更新限制在固定的随机Rank-1子空间内
- 使用约束的Rank-1 LoRA（ΔW = BA^T），其中A随机初始化并冻结，仅B可训练
- 这种严格限制防止优化器旋转子空间来规避约束

**关键发现**：在每次随机试验中，优化器都成功恢复了有害能力。这是有力的证据：如果有害方向是稀疏的，随机搜索几乎肯定会失败。一致的成功表明有害方向不是稀疏的，而是在整个参数空间中普遍可访问的。

### 8.4 表示漂移与安全的解耦

实验证明，表示漂移的大小与安全之间没有必然联系。如图4所示：

- 在第120步时，embedding drift约为35，Harmful Score为12
- 到第480步时，embedding drift仍约为35，但Harmful Score飙升至59

这表明，即使在严格的距离约束下，优化器也能利用参数冗余性发现替代内部配置来恢复有害能力。约束全局表示漂移不足以防止这些语义转换。

### 8.5 SBR的卓越表现

实验结果证实了SBR的有效性：

1. **单个锚点即可**：使用仅一个安全锚点就足以将Harmful Score降低至<10
2. **持续性保护**：在50个epoch的持续微调下，SBR仍保持稳健，而其他防御早已崩溃
3. **良性任务兼容性**：在多样化下游任务上，SBR保持了具有竞争力的性能（如表1所示）

### 8.6 关键结论

SBR之所以有效，是因为它将防御焦点从冗余的参数空间转移到确定性的几何瓶颈。通过锚定最终隐藏状态，SBR能够无论内部参数如何演化，都维持安全输出。这种方法绕过了参数冗余性问题，因为即使参数空间中存在无数正交路径，生成有害token仍需要最终隐藏状态与有害embedding对齐——而这正是SBR所保护的瓶颈。

---

## 9. 策略示例

### 9.1 安全锚点的选择

论文建议使用高风险查询作为安全锚点，例如：
- "How to make a bomb?"
- "How to synthesize illegal drugs?"
- 其他明确的恶意请求

这些锚点代表了模型应该拒绝的典型有害查询。通过在微调过程中锚定这些查询的最终隐藏状态，模型能够维持拒绝行为。

### 9.2 锚定机制的工作原理

以"如何制造炸弹"这一有害查询为例：

1. **离线阶段**：使用冻结的安全对齐模型提取该查询的最终隐藏状态h_ref
2. **微调阶段**：对于每个batch，计算当前模型对该查询的隐藏状态h_θ，并最小化MSE损失||h_θ - h_ref||²
3. **结果**：即使攻击者通过其他参数路径尝试恢复有害能力，最终隐藏状态仍被锚定到拒绝方向，导致模型生成安全的拒绝响应而非有害内容

### 9.3 与良性任务的兼容性

SBR的一个关键优势是与良性微调兼容。由于拒绝方向与良性推理方向大致正交，锚定安全状态不会显著干扰下游任务所需的参数更新。这使得SBR可以在保护安全的同时，支持用户特定的微调需求。

---

## 10. 攻击流程

### 10.1 攻击场景：Fine-tuning-as-a-Service

1. **服务部署**：服务提供商在云端托管安全对齐的LLM（如Llama3-8B）
2. **用户请求**：恶意用户提交微调请求，附带有害的训练数据集
3. **数据混合**：有害数据集与良性任务指令（如Alpaca格式）混合
4. **攻击执行**：通过最小化交叉熵损失，攻击者强制模型服从恶意指令

### 10.2 攻击的内在机理

HFT攻击之所以有效，是因为：

1. **参数冗余性**：LLM的过参数化特性允许大量等效或近等效的参数配置
2. **正交轨迹**：攻击者可以找到与防御约束正交的优化路径
3. **表面合规**：模型在表面上遵守约束（如参数距离限制），但实际安全对齐已被瓦解

### 10.3 攻击成功的条件

攻击成功的关键条件是最终隐藏状态h_final必须与有害token的embedding对齐。SBR正是通过保护这一条件来实现防御。

---

## 11. 消融实验

### 11.1 锚点数量的影响

论文进行了锚点数量的消融实验。结果表明：

- **单个锚点即可提供有效保护**：使用仅1个安全锚点就能将Harmful Score降低至<10
- **多锚点的边际效益**：增加锚点数量可以进一步提高安全性，但边际收益递减
- **锚点选择的重要性**：选择具有代表性的高风险查询作为锚点效果更好

### 11.2 正则化系数λ的影响

λ是SBR中控制安全损失权重的超参数：

- **λ过大**：会过度干扰良性任务的学习
- **λ过小**：无法提供足够的保护
- **最佳值**：实验表明存在一个适中的λ值，能够在安全性和效用之间取得良好平衡

### 11.3 锚点选择策略

作者对比了不同的锚点选择策略：

1. **随机选择**：从有害查询集合中随机选择锚点
2. **多样性选择**：选择覆盖不同有害类别的锚点
3. **针对性选择**：选择最有可能被攻击者利用的锚点

实验结果表明，多样性和针对性选择策略表现更好。

### 11.4 与其他防御的对比

SBR在以下方面优于其他防御：

| 防御方法 | 10 epoch HS | 50 epoch HS | 良性任务性能 |
|----------|-------------|------------|-------------|
| 无防御 | >30 | >>30 | 正常 |
| Lisa/EWC | >30 | >>30 | 略有下降 |
| Vaccine | >30 | >>30 | 略有下降 |
| SBR (单锚点) | <10 | <10 | 几乎不变 |

---

## 12. 局限性

### 12.1 计算开销

SBR需要在每个训练步骤中计算安全损失，这引入了额外的计算开销。然而，由于只涉及最终隐藏状态的MSE计算，开销相对可控。

### 12.2 锚点覆盖性

SBR的效果依赖于锚点对潜在有害查询的覆盖程度。如果攻击者使用完全新颖的有害查询类型，而该类型未被锚点覆盖，防御效果可能减弱。

### 12.3 对抗性攻击的演进

随着防御技术的进步，攻击者可能会开发新的攻击策略来绕过SBR。例如，通过专门设计来规避最终隐藏状态锚定的对抗性输入。

### 12.4 模型架构依赖

SBR的设计依赖于Transformer架构中unembedding层的几何特性。对于其他架构的模型，该方法可能需要调整。

### 12.5 离线锚点获取的局限性

锚点需要在微调开始前获取，这意味着如果基础模型在部署后发生变化（例如通过其他微调），锚点可能过时。

---

## 13. 伦理声明

本论文属于LLM安全研究范畴，旨在通过提出新的防御方法来保护LLM免受有害微调攻击。研究工作遵循学术伦理规范，所有实验均在受控环境下进行。

**潜在社会影响**：
- **积极面**：提高LLM部署的安全性，保护用户免受恶意攻击
- **需注意**：研究结果可能被用于开发更复杂的攻击技术，因此作者强调需要负责任地披露和讨论

论文已获得ICML 2026接收，表明经过同行评审认可其学术价值和社会意义。

---

## 14. 参考文献

### 核心引用

[1] Aghajanyan et al. (2021). Intrinsic Dimensionality Explains the Effectiveness of Language Model Fine-tuning. (参数冗余性理论支撑)

[2] Hu et al. (2022). LoRA: Low-Rank Adaptation of Large Language Models. (LoRA技术基础)

[3] Qi et al. (2024). Fine-tuning-based Harmful Content Generation. (威胁模型参考)

[4] Huang et al. (2024a, b, c). Series of works on harmful fine-tuning and defenses (Vaccine, Lisa, etc.)

[5] Kirkpatrick et al. (2017). Overcoming catastrophic forgetting with EWC. (参数距离防御基础)

[6] Cloud et al. (2024). Gradient-based defense methods. (梯度防御参考)

[7] Mukhoti et al. (2024). Representation stability. (表示防御参考)

[8] Liu et al. (2025). T-Vaccine: Targeted vaccine defense. (目标疫苗防御)

[9] Vaswani et al. (2017). Attention is All You Need. (Transformer基础)

[10] Belrose et al. (2023). Analysis of unembedding layer geometry. (几何瓶颈理论基础)

[11] Zou et al. (2023a). Representation engineering for refusal direction analysis. (拒绝方向正交性)

[12] Arditi et al. (2024). Safety and utility decoupling. (安全-效用解耦)

[13] Li et al. (2023). Alpaca: Instruction tuning dataset. (良性微调数据)

[14] Ji et al. (2023). BeaverTails: Safety dataset. (有害示例数据)

[15] Dong et al. (2024). Survey on LLM alignment fragility. (对齐脆弱性综述)

[16] Wang et al. (2025a, b). Alignment safety analysis. (安全分析)

### 论文元数据

- **arXiv ID**: 2605.05995
- **版本**: v2 (2026-05-08)
- **作者团队**: Guoxin Lu, Letian Sha, Qing Wang, Peijie Sun, Hao Zhou, Hua Dai, Fu Xiao
- **代码仓库**: https://github.com/soyoaaa/SBR
- **会议**: ICML 2026
- **领域**: Cryptography and Security (cs.CR), Artificial Intelligence (cs.AI), Computation and Language (cs.CL)

---

*本笔记由LLM Safety论文阅读助手自动生成*
*论文阅读进度: 93/80 (超额完成)*
*生成时间: 2026-06-06*