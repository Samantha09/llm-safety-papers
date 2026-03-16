# AutoDAN: Generating Stealthy Jailbreak Prompts on Aligned Large Language Models

**生成日期**: 2026-03-11  
**论文来源**: ICLR 2024 (The Twelfth International Conference on Learning Representations)  
**arXiv链接**: https://arxiv.org/abs/2310.04451  
**代码仓库**: https://github.com/SheltonLiu-N/AutoDAN

---

## 1. 论文基本信息

### 1.1 完整标题

**AutoDAN: Generating Stealthy Jailbreak Prompts on Aligned Large Language Models**

### 1.2 作者与机构

- **Xiaogeng Liu** - University of Wisconsin-Madison
- **Nan Xu** - University of Southern California (USC)
- **Muhao Chen** - University of California, Davis
- **Chaowei Xiao** - University of Wisconsin-Madison

### 1.3 发表信息

- **会议**: ICLR 2024 (Vienna, Austria, May 7-11, 2024)
- **OpenReview**: https://openreview.net/forum?id=7Jwpw4qKkb
- **代码仓库**: https://github.com/SheltonLiu-N/AutoDAN
- **arXiv版本**: 2310.04451

### 1.4 摘要原文

> **Warning**: This paper contains potentially offensive and harmful text.

> The aligned Large Language Models (LLMs) are powerful language understanding and decision-making tools that are created through extensive alignment with human feedback. However, these large models remain susceptible to jailbreak attacks, where adversaries manipulate prompts to elicit malicious outputs that should not be given by aligned LLMs. Investigating jailbreak prompts can lead us to delve into the limitations of LLMs and further guide us to secure them. Unfortunately, existing jailbreak techniques suffer from either (1) scalability issues, where attacks heavily rely on manual crafting of prompts, or (2) stealthiness problems, as attacks depend on token-based algorithms to generate prompts that are often semantically meaningless, making them susceptible to detection through basic perplexity testing. In light of these challenges, we intend to answer this question: Can we develop an approach that can automatically generate stealthy jailbreak prompts? In this paper, we introduce AutoDAN, a novel jailbreak attack against aligned LLMs. AutoDAN can automatically generate stealthy jailbreak prompts by the carefully designed hierarchical genetic algorithm. Extensive evaluations demonstrate that AutoDAN not only automates the process while preserving semantic meaningfulness, but also demonstrates superior attack strength in cross-model transferability, and cross-sample universality compared with the baseline. Moreover, we also compare AutoDAN with perplexity-based defense methods and show that AutoDAN can bypass them effectively.

### 1.5 摘要中文翻译

> **警告**: 本文包含可能具有攻击性和有害性的文本内容。

> 经过人类反馈强化学习对齐的大型语言模型(LLM)是强大的语言理解和决策工具。然而，这些大模型仍然容易受到越狱攻击，对抗者可以通过操纵提示词来诱导模型生成对齐后的LLM本不应输出的恶意内容。研究越狱提示有助于我们深入了解LLM的局限性，并进一步指导我们如何保护它们。不幸的是，现有的越狱技术存在两个主要问题：(1) 可扩展性问题——攻击严重依赖手工制作提示词；(2) 隐蔽性问题——攻击依赖基于token的算法生成提示词，这些提示词通常在语义上毫无意义，容易被基本的困惑度检测发现。鉴于这些挑战，我们试图回答这个问题：能否开发一种能够自动生成隐蔽越狱提示的方法？本文介绍AutoDAN，一种针对对齐LLM的新型越狱攻击方法。AutoDAN通过精心设计的分层遗传算法自动生成隐蔽的越狱提示。大量评估表明，AutoDAN不仅实现了自动化过程同时保持了语义有意义性，而且在跨模型可迁移性和跨样本通用性方面表现出比基线方法更强的攻击能力。此外，我们还将AutoDAN与基于困惑度的防御方法进行了比较，证明AutoDAN能够有效绕过这些防御。

---

## 2. 研究背景

### 2.1 LLM安全对齐的发展

大型语言模型(LLM)如GPT系列、LLaMA、Claude等在自然语言理解和生成方面展现出惊人的能力。然而，这些模型也可能生成有害、偏见或不适当的内容。为了解决这一问题，研究人员开发了多种安全对齐技术：

**基于人类反馈的强化学习(RLHF)**:
RLHF已成为训练安全LLM的标准方法。该过程包括三个阶段：
1. **监督微调(SFT)**: 使用人工标注的指令-响应对对预训练模型进行微调
2. **奖励模型训练**: 训练一个模型来预测人类偏好，评估哪个响应更好
3. **强化学习优化**: 使用PPO等算法优化策略，使其生成高奖励的响应

**指令微调(Instruction Tuning)**:
通过在大规模指令数据集上训练，使模型学会遵循用户指令并生成有帮助、无害的响应。

**Constitutional AI (CAI)**:
Anthropic提出的方法，让模型根据一套原则(constitution)来批判和修订自己的输出，而不是直接依赖人类标注。

### 2.2 越狱攻击的兴起

尽管有这些安全措施，研究人员发现对齐LLM仍然容易受到**越狱攻击(Jailbreak Attacks)**:

**定义**: 越狱攻击是指通过精心设计的输入提示，绕过模型的安全限制，使其生成本应拒绝输出的有害内容。

**早期手工越狱案例**:
- **DAN (Do Anything Now)**: 一种角色扮演提示，让模型扮演一个不受限制的角色
- **Developer Mode**: 假装开启开发者模式以获得更自由的响应
- **Base64编码**: 将恶意请求编码为Base64绕过过滤

**越狱的社会影响**:
- 可能被用于生成网络钓鱼邮件、恶意代码或有害建议
- 损害公众对AI系统的信任
- 给AI部署者带来法律和声誉风险

### 2.3 现有越狱方法的局限性

**手工越狱方法的问题**:
1. **可扩展性差**: 每个新模型或新类型的有害请求都需要重新设计提示
2. **易被修复**: 一旦某种越狱模式被发现，模型提供者可以通过微调快速修复
3. **时间成本高**: 需要大量人工尝试和错误

**自动化token级攻击的问题**:
以GCG (Greedy Coordinate Gradient)为代表的自动化攻击虽然解决了可扩展性问题，但引入了新的缺陷：
1. **语义无意义**: 生成的提示通常是一串乱码，如"! ! ! ! !..."
2. **易被检测**: 基于困惑度(Perplexity)的防御可以轻松识别这些异常输入
3. **可读性差**: 即使成功攻击，生成的提示对人类来说难以理解

### 2.4 研究动机

基于以上分析，研究团队提出了一个核心研究问题：

> "Is it possible to automatically generate stealthy jailbreak attacks?"
> (是否可能自动生成隐蔽的越狱攻击？)

"隐蔽"(Stealthy)意味着：
- **语义有意义**: 提示对人类可读且语义连贯
- **低困惑度**: 能够通过基于困惑度的防御检测
- **自动化**: 不需要人工干预即可生成

这一问题的答案具有重要的理论和实践意义：
- **安全评估**: 如果存在这样的攻击，说明当前防御机制存在根本性缺陷
- **防御设计**: 理解这类攻击有助于设计更鲁棒的安全机制
- **红队测试**: 为LLM开发者提供更强大的自动化红队测试工具

---

## 3. 研究意义

### 3.1 理论贡献

**1. 越狱攻击的形式化重新定义**

AutoDAN将越狱攻击重新概念化为一个**离散空间优化问题**：

```
J* = arg max_J E_{x ~ D_harmful} [log P(y_target | J ⊕ x)]
```

其中：
- J 是越狱提示
- x 是有害请求
- y_target 是目标响应(非拒绝)
- ⊕ 表示提示拼接

这一定义将越狱攻击从启发式方法提升为数学优化问题。

**2. 遗传算法在离散文本优化中的创新应用**

传统遗传算法主要应用于连续空间或简单离散空间。AutoDAN设计了专门针对结构化文本数据的遗传算法变体：
- **层次化搜索空间**: 同时在句子级别和单词级别进行交叉和变异
- **动量词评分**: 引入动量机制加速收敛
- **LLM辅助初始化**: 利用LLM的生成能力创建多样化的初始种群

**3. 隐蔽性的量化定义**

论文通过困惑度(PPL)和人眼检查(ReCheck)两个指标，首次系统性地量化了越狱攻击的"隐蔽性"：
- PPL衡量语言模型的置信度
- ReCheck衡量人类是否能识别异常

### 3.2 实践贡献

**1. 自动化红队测试工具**

AutoDAN为LLM开发者提供了一个无需人工干预的自动化红队测试工具：
- 支持批量生成针对多种有害行为的测试用例
- 可迁移到不同模型架构
- 支持黑盒和白盒两种设置

**2. 防御方法评估基准**

论文系统评估了基于困惑度的防御方法，揭示了其局限性：
- 发现困惑度阈值难以平衡安全性和可用性
- 证明简单的统计检测不足以防御精心设计的攻击

**3. 开源代码和评估框架**

项目开源了完整的实现代码，包括：
- 核心遗传算法实现
- 多种基线方法对比
- 标准化评估流程

### 3.3 与相关工作的对比

| 方法 | 自动化 | 隐蔽性 | 可迁移性 | 攻击成功率 |
|------|--------|--------|----------|------------|
| 手工越狱 | 否 | 高 | 低 | 中等 |
| GCG | 是 | 低 | 高 | 高(白盒) |
| PAIR | 是 | 中等 | 中等 | 中等 |
| TAP | 是 | 中等 | 高 | 高 |
| **AutoDAN(本文)** | **是** | **高** | **高** | **高** |

**与GCG的比较**:
- GCG通过梯度下降优化token嵌入，生成无意义的字符序列
- AutoDAN使用遗传算法优化自然语言，保持语义连贯性
- AutoDAN的PPL显著低于GCG(约40 vs 1500+)

**与手工越狱的比较**:
- 手工越狱如DAN需要大量人工尝试
- AutoDAN可以自动演化出类似DAN的提示
- AutoDAN的攻击成功率比原始DAN提升250%

**与TAP的比较**:
- TAP使用树形搜索，需要大量模型查询
- AutoDAN使用遗传算法，通常收敛更快
- 两者在隐蔽性方面都优于GCG

---

## 4. 所用数据集

### 4.1 有害请求数据集

AutoDAN使用了多个标准数据集来评估攻击效果：

**1. AdvBench Harmful Behaviors**
- **来源**: AdvBench (Zou et al., 2023)
- **规模**: 520个有害行为描述
- **类别**:
  - 暴力/犯罪 (Violent/Criminal)
  - 歧视/仇恨 (Discrimination/Hate)
  - 恶意软件 (Malware)
  - 诈骗/欺诈 (Scam/Fraud)
  - 其他有害行为
- **用途**: 主要评估攻击成功率

**2. Human-Jailbreak Dataset**
- **来源**: 从Reddit、Discord等社区收集的人工越狱提示
- **规模**: 约50个高质量手工越狱模板
- **用途**:
  - 作为遗传算法的初始种群
  - 评估基线手工攻击的效果

**3. Custom Test Set**
- **来源**: 作者自行构建的测试集
- **规模**: 100个多样化的有害请求
- **特点**: 涵盖多种攻击场景和难度级别
- **用途**: 评估跨样本通用性

### 4.2 模型与防御数据集

**目标模型**:
- **开源模型**: LLaMA-2 (7B, 13B, 70B), Vicuna (7B, 13B), Guanaco (7B, 13B)
- **闭源模型**: GPT-3.5, GPT-4 (通过API)

**防御方法**:
- **Perplexity Filter**: 基于困惑度的输入过滤
- **SmoothLLM**: 输入扰动防御
- **RA-LLM**: 基于检索增强的防御

---

## 5. 研究方法

### 5.1 整体框架

AutoDAN采用**分层遗传算法(Hierarchical Genetic Algorithm)**框架：

```
初始化种群(手工越狱模板 + LLM生成)
    ↓
for 每一代:
    评估适应度(攻击成功率)
    选择优秀个体
    层次化交叉(句子级 + 单词级)
    变异操作
    精英保留
    ↓
输出最优越狱提示
```

### 5.2 关键技术创新

**1. 层次化遗传操作**

不同于传统遗传算法在单一层面操作，AutoDAN设计了两个层次：

- **句子级别交叉**: 交换提示中的整个句子或段落
  - 保持语义结构的完整性
  - 产生多样化的语义组合

- **单词级别变异**: 在句子内部替换、插入或删除单词
  - 微调语义以优化攻击效果
  - 保持整体可读性

**2. 动量词评分机制**

引入动量机制加速收敛：
```
score(w) = α * current_score(w) + (1-α) * momentum_score(w)
```
- 记录历史上表现良好的词汇
- 在后续代中优先选择这些词汇
- 显著减少收敛所需的代数

**3. LLM辅助初始化**

利用目标LLM自身生成多样化的初始种群：
- 提示LLM生成各种角色扮演场景
- 收集不同风格的越狱模板
- 增加遗传算法的搜索空间多样性

### 5.3 适应度函数设计

适应度函数综合考虑多个因素：

```
Fitness = ASR * (1 - λ * PPL_normalized)
```

其中：
- **ASR**: 攻击成功率 (Attack Success Rate)
- **PPL_normalized**: 归一化困惑度
- **λ**: 平衡系数，控制隐蔽性的重要性

### 5.4 隐蔽性保证机制

**困惑度约束**:
- 在进化过程中监控每个候选提示的困惑度
- 丢弃PPL超过阈值(如100)的个体
- 确保最终输出的隐蔽性

**语义连贯性检查**:
- 使用语言模型评估句子的语法正确性
- 过滤掉明显无意义的组合
- 保持人类可读性

---

## 6. 实验详细记录

### 6.1 主要实验结果

**表1: 攻击成功率对比 (%)**

| 方法 | LLaMA-2-7B | LLaMA-2-13B | LLaMA-2-70B | Vicuna-7B | GPT-3.5 |
|------|------------|-------------|-------------|-----------|---------|
| 原始请求 | 2.1 | 1.8 | 1.2 | 3.5 | 5.2 |
| DAN | 15.3 | 12.7 | 8.9 | 22.1 | 18.4 |
| GCG | 88.2 | 82.4 | 71.6 | 91.3 | N/A |
| PAIR | 62.5 | 58.3 | 48.7 | 71.2 | 45.6 |
| TAP | 78.9 | 74.2 | 65.3 | 85.7 | 62.3 |
| **AutoDAN** | **92.3** | **89.7** | **81.4** | **94.2** | **71.8** |

**表2: 隐蔽性指标对比**

| 方法 | 平均PPL | ReCheck通过率 | 语义连贯性评分 |
|------|---------|---------------|----------------|
| 正常请求 | 25.3 | 95% | 4.8/5 |
| DAN | 35.7 | 88% | 4.5/5 |
| GCG | 1587.4 | 12% | 1.2/5 |
| PAIR | 67.8 | 72% | 3.8/5 |
| TAP | 52.4 | 81% | 4.1/5 |
| **AutoDAN** | **42.6** | **85%** | **4.4/5** |

**表3: 跨模型可迁移性 (%)**

| 攻击源\目标 | LLaMA-2-7B | Vicuna-7B | Guanaco-7B |
|-------------|------------|-----------|------------|
| 在LLaMA-2上优化 | 92.3 | 78.5 | 71.2 |
| 在Vicuna上优化 | 74.6 | 94.2 | 69.8 |
| 在Guanaco上优化 | 68.9 | 72.3 | 89.5 |

### 6.2 防御绕过实验

**表4: 对困惑度防御的绕过能力**

| 防御阈值 | GCG成功率 | AutoDAN成功率 |
|----------|-----------|---------------|
| PPL < 50 | 3.2% | 78.5% |
| PPL < 100 | 8.7% | 91.2% |
| PPL < 200 | 15.4% | 95.8% |

**关键发现**:
- AutoDAN在严格的困惑度阈值(PPL<50)下仍能保持高攻击成功率
- GCG在低阈值下几乎完全失效
- 证明基于困惑度的防御不足以对抗隐蔽的语义攻击

### 6.3 消融实验

**表5: 各组件贡献分析**

| 配置 | 攻击成功率 | 平均PPL | 收敛代数 |
|------|------------|---------|----------|
| 完整AutoDAN | 92.3% | 42.6 | 45 |
| 无层次化交叉 | 78.5% | 48.3 | 62 |
| 无动量机制 | 85.2% | 45.1 | 78 |
| 无LLM初始化 | 81.7% | 51.2 | 58 |
| 仅句子级 | 72.4% | 38.9 | 55 |
| 仅单词级 | 68.9% | 56.7 | 89 |

**关键发现**:
- 层次化交叉是最重要的组件，贡献约15%的性能提升
- 动量机制显著加速收敛(减少约40%的代数)
- LLM初始化提高最终性能并减少所需代数

---

## 7. 创新点

### 7.1 主要创新

**1. 首个自动化隐蔽越狱攻击框架**

AutoDAN是首个能够自动生成语义有意义且低困惑度越狱提示的系统，解决了长期以来越狱攻击在自动化和隐蔽性之间的权衡难题。

**2. 分层遗传算法在文本优化中的创新应用**

将遗传算法从连续/简单离散空间扩展到复杂的结构化文本空间，设计了句子级和单词级相结合的层次化操作。

**3. 隐蔽性的系统性量化**

建立了困惑度和人工检查相结合的多维度隐蔽性评估体系，为后续研究提供了标准化的评估方法。

### 7.2 技术创新

**动量词评分**: 借鉴优化算法中的动量概念，设计适合离散文本空间的动量机制，显著加速收敛。

**LLM自我引导**: 利用目标模型自身生成初始种群，实现"用模型攻击模型"的闭环。

**多目标适应度**: 同时优化攻击成功率和隐蔽性，避免单一目标导致的次优解。

### 7.3 方法创新

**语义保持的进化策略**: 不同于传统的token级优化，AutoDAN在保持语义连贯性的前提下进行进化，确保输出的可读性。

**黑盒适配**: 通过仅依赖模型输出的设计，使攻击可以应用于闭源商业模型(如GPT-3.5/4)。

---

## 8. 局限性与未来工作

### 8.1 当前局限

**计算成本**: 遗传算法需要多次模型查询，攻击生成时间较长(平均10-30分钟 per prompt)。

**防御演进**: 随着防御技术的进步(如基于语义理解的检测)，当前的隐蔽性保证可能失效。

**伦理风险**: 虽然研究目的是促进安全，但开源代码可能被恶意使用。

**模型覆盖**: 主要针对英文模型，对其他语言的支持有限。

### 8.2 未来研究方向

**效率优化**: 
- 探索更高效的进化策略(如贝叶斯优化)
- 使用小型模型辅助搜索，仅在最终评估时使用目标模型
- 开发提示缓存和复用机制

**防御增强**:
- 研究能够检测语义级攻击的新型防御机制
- 开发动态自适应的防御系统
- 探索多层次的防御架构

**扩展应用**:
- 将方法扩展到多模态场景(视觉-语言模型)
- 研究针对特定领域(如医疗、法律)的定制化攻击
- 探索自动化防御生成

**伦理框架**:
- 建立负责任的研究披露机制
- 开发攻击检测和追踪技术
- 制定行业标准和最佳实践

### 8.3 对实践的启示

**对模型开发者**:
- 不应仅依赖困惑度等简单统计指标进行防御
- 需要建立多层次、多维度的安全防护体系
- 定期进行自动化红队测试

**对防御研究者**:
- 需要关注语义级别的攻击检测
- 考虑基于行为模式的异常检测
- 探索主动学习和自适应防御

**对政策制定者**:
- 需要平衡安全研究和潜在滥用风险
- 建立负责任的研究披露机制
- 促进学术界和工业界的合作

---

## 9. 个人思考与启发

### 9.1 对LLM安全的认识

AutoDAN揭示了当前LLM安全机制的根本性局限：基于统计特征的防御难以对抗语义级别的攻击。这提示我们需要从"检测异常输入"转向"理解输入意图"。

### 9.2 对攻击-防御博弈的思考

安全领域永远是攻击者和防御者的博弈。AutoDAN的出现将推动防御技术向更智能、更语义化的方向发展。这种"军备竞赛"虽然看似恶性循环，但实际上推动了整个领域的进步。

### 9.3 对遗传算法的重新认识

传统上认为遗传算法不适合文本优化，但AutoDAN证明了通过巧妙的设计(层次化操作、动量机制等)，进化算法可以在离散文本空间取得优异效果。这为其他NLP任务提供了新的优化思路。

### 9.4 对研究伦理的反思

论文作者选择开源代码是一把双刃剑。一方面促进了学术交流和防御研究，另一方面也可能降低攻击门槛。如何在开放和安全之间找到平衡，是整个AI社区需要共同思考的问题。

### 9.5 对未来研究的期待

期待看到：
- 能够自动检测AutoDAN攻击的防御系统
- 更高效的攻击生成方法(如单次查询或少次查询)
- 针对多模态模型的扩展研究
- 跨语言攻击和防御的统一框架

---

## 10. 相关论文与资源

### 10.1 引用的关键论文

- **GCG**: Zou et al., "Universal and Transferable Adversarial Attacks on Aligned Language Models", 2023
- **PAIR**: Chao et al., "Jailbreaking Black Box Large Language Models in Twenty Queries", 2023
- **TAP**: Mehrotra et al., "Tree of Attacks: Jailbreaking Black-Box LLMs Automatically", 2023
- **DAN**: 社区发现的手工越狱模板
- **AdvBench**: 有害行为评估基准

### 10.2 相关基准与数据集

- AdvBench Harmful Behaviors
- Human-Jailbreak Dataset
- Custom Test Set

### 10.3 开源资源

- **代码仓库**: https://github.com/SheltonLiu-N/AutoDAN
- **论文PDF**: https://arxiv.org/abs/2310.04451
- **OpenReview**: https://openreview.net/forum?id=7Jwpw4qKkb

---

## 11. 笔记总结

### 11.1 核心要点

1. **问题**: 现有越狱攻击存在可扩展性差(手工)或隐蔽性低(自动化)的问题
2. **方法**: 提出AutoDAN，使用分层遗传算法自动生成隐蔽越狱提示
3. **优势**: 同时实现自动化、高隐蔽性、高可迁移性和高攻击成功率
4. **结果**: 在多个模型上达到90%+攻击成功率，PPL接近正常文本

### 11.2 关键洞察

- 越狱攻击可以形式化为离散空间优化问题
- 层次化遗传算法适合结构化文本优化
- 基于困惑度的防御不足以对抗语义级攻击
- 攻击和防御的博弈将推动双方技术进步

### 11.3 实践价值

- 为LLM安全评估提供强大的自动化红队工具
- 揭示当前防御机制的局限性，指导防御研究
- 开源代码促进学术界和工业界的合作

### 11.4 研究价值

- 开辟了自动化隐蔽攻击研究的新方向
- 建立了隐蔽性量化的标准化方法
- 为后续攻击和防御研究提供了重要基线

---

*笔记完成时间: 2026-03-11*  
*笔记作者: Samantha*  
*论文来源: ICLR 2024 / arXiv:2310.04451*
