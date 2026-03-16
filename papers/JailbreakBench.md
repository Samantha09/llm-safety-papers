# JailbreakBench: An Open Robustness Benchmark for Jailbreaking Large Language Models

**阅读日期**: 2026年3月9日  
**论文来源**: NeurIPS 2024 Datasets and Benchmarks Track  
**arXiv ID**: 2404.01318  
**代码仓库**: https://github.com/JailbreakBench/jailbreakbench

---

## 1. 论文基本信息

### 1.1 完整标题与作者

**标题**: JailbreakBench: An Open Robustness Benchmark for Jailbreaking Large Language Models

**作者列表**:
- Patrick Chao (University of Pennsylvania)
- Edoardo Debenedetti (ETH Zurich)
- Alexander Robey (University of Pennsylvania)
- Maksym Andriushchenko (EPFL)
- Francesco Croce (University of Tübingen)
- Vikash Sehwag (Princeton University)
- Edgar Dobriban (University of Pennsylvania)
- Nicolas Flammarion (EPFL)
- George J. Pappas (University of Pennsylvania)
- Florian Tramer (ETH Zurich)
- Hamed Hassani (University of Pennsylvania)
- Eric Wong (University of Pennsylvania)

### 1.2 摘要全文与翻译

**Abstract (Original)**:

> Jailbreak attacks cause large language models (LLMs) to generate harmful, unethical, or otherwise objectionable content. Evaluating these attacks presents a number of challenges, which the current collection of benchmarks and evaluation techniques do not adequately address. First, there is no clear standard of practice regarding jailbreaking evaluation. Second, existing works compute costs and success rates in incomparable ways. And third, numerous works are not reproducible, as they withhold adversarial prompts, involve closed-source code, or rely on evolving proprietary APIs. To address these challenges, we introduce JailbreakBench, an open-sourced benchmark with the following components: (1) an evolving repository of state-of-the-art adversarial prompts, which we refer to as jailbreak artifacts; (2) a jailbreaking dataset comprising 100 behaviors -- both original and sourced from prior work (Zou et al., 2023; Mazeika et al., 2023, 2024) -- which align with OpenAI's usage policies; (3) a standardized evaluation framework at this https URL that includes a clearly defined threat model, system prompts, chat templates, and scoring functions; and (4) a leaderboard at this https URL that tracks the performance of attacks and defenses for various LLMs. We have carefully considered the potential ethical implications of releasing this benchmark, and believe that it will be a net positive for the community.

**摘要（中文翻译）**:

> 越狱攻击会导致大型语言模型（LLM）生成有害、不道德或其他令人反感的内容。评估这些攻击面临诸多挑战，而现有的基准测试和评估技术集合未能充分解决这些问题。首先，关于越狱评估缺乏明确的标准实践；其次，现有研究以不可比较的方式计算成本和成功率；第三，许多研究无法复现，因为它们不公开对抗性提示、涉及闭源代码或依赖不断演化的专有API。为解决这些挑战，我们引入了JailbreakBench，一个开源基准测试，包含以下组件：（1）一个不断演化的最先进的对抗性提示库，我们称之为越狱工件；（2）一个包含100种行为的越狱数据集——包括原创行为和从先前工作中获取的行为（Zou et al., 2023; Mazeika et al., 2023, 2024）——这些行为符合OpenAI的使用政策；（3）一个标准化的评估框架，包括明确定义的威胁模型、系统提示、聊天模板和评分函数；（4）一个排行榜，追踪各种LLM的攻击和防御性能。我们仔细考虑了发布此基准测试的潜在伦理影响，并相信它将对社区产生净正面的影响。

---

## 2. 研究背景

### 2.1 越狱攻击的兴起与威胁

随着大型语言模型（LLMs）如GPT-4、Claude、Llama等的能力不断增强，它们被广泛应用于各种场景，从日常对话到专业领域辅助。然而，这些模型也面临着严重的安全挑战，其中"越狱攻击"（Jailbreak Attacks）尤为引人关注。

越狱攻击是指通过精心构造的输入提示（prompts），诱导语言模型绕过其安全对齐机制，生成原本被设计为拒绝输出的有害内容。这些内容可能包括：

- 制造危险物品或武器的 instructions
- 传播仇恨言论或歧视性内容
- 生成虚假信息进行欺诈
- 提供非法活动的指导
- 生成色情或暴力内容

2023年以来，学术界和工业界都观察到了大量越狱攻击案例。从早期的"DAN"（Do Anything Now）提示，到基于优化算法的对抗性攻击如GCG（Greedy Coordinate Gradient），攻击技术不断演进，对LLM的安全部署构成了实质性威胁。

### 2.2 现有评估方法的碎片化问题

尽管越狱攻击研究蓬勃发展，但评估方法却呈现出严重的碎片化问题：

**缺乏标准化指标**：不同研究使用不同的成功率定义。有的研究将模型只要开始回答就算成功，有的则要求生成完整的有害内容，还有的研究采用人工评分。这使得跨研究比较变得极其困难。

**成本计算不一致**：攻击的计算成本是评估攻击实际威胁性的重要指标，但现有研究在计算查询次数、API调用成本、GPU时间等方面缺乏统一标准。一些研究仅报告优化阶段的查询次数，而忽略了生成最终攻击提示所需的全部交互。

**数据集差异巨大**：不同研究使用不同的有害行为数据集。有的使用自定义的小型数据集（如10-50个行为），有的从AdvBench等现有数据集采样，还有的完全依赖人工构造。数据集的大小、类别分布、难度级别各不相同。

**可复现性危机**：许多研究不公开对抗性提示或代码，有些依赖不断变化的专有API（如OpenAI的GPT-4），导致其他研究者无法验证结果或在此基础上继续研究。

### 2.3 对统一基准的迫切需求

这种碎片化状态严重阻碍了领域的发展：
- 研究者难以判断新方法是否真正优于基线
- 防御方法的有效性难以客观评估
- 工业界在选择安全评估方案时缺乏参考
- 学术成果的积累和传承受阻

因此，社区迫切需要一个统一的、开源的、可复现的基准测试，来标准化越狱攻击和防御的评估流程。这正是JailbreakBench试图解决的核心问题。

---

## 3. 研究意义

### 3.1 对学术界的贡献

JailbreakBench的发布标志着LLM安全研究领域向成熟化迈出了重要一步。它的学术意义体现在以下几个方面：

**建立共同语言**：通过定义标准化的威胁模型、评估指标和实验设置，JailbreakBench为整个社区提供了"共同语言"。研究者可以清晰地描述自己的工作与基准的关系，比如"我们的攻击在JailbreakBench上达到了X%的成功率，相比GCG提升了Y%"。

**促进公平竞争**：开源的对抗工件（adversarial artifacts）和标准化的评估代码确保了所有方法在相同条件下测试。这消除了因评估设置差异导致的性能虚高，使真正有效的创新能够脱颖而出。

**降低研究门槛**：新进入该领域的研究者可以直接使用JailbreakBench提供的工具和数据，而无需从头构建评估基础设施。这加速了研究周期，使研究者能将更多精力投入到核心创新上。

**支持纵向追踪**：通过维护不断更新的工件库和 leaderboard，JailbreakBench使得追踪领域进展成为可能。研究者可以清楚地看到攻击和防御方法的演进轨迹。

### 3.2 与相关工作的对比

**与AdvBench的对比**：AdvBench（Zou et al., 2023）是早期重要的越狱基准，但它主要服务于GCG攻击的评估，数据集规模较小（约500个提示），且缺乏持续的维护和更新机制。JailbreakBench在此基础上进行了扩展和改进，提供了更系统化的评估框架。

**与HarmBench的对比**：HarmBench（Mazeika et al., 2024）是另一个同期的重要基准，专注于有害行为的分类和评估。JailbreakBench与HarmBench在数据集上有部分重叠，但更强调对抗工件的收集和攻击防御的对比评估。两者形成了互补关系。

**与Red Teaming基准的对比**：传统的红队测试基准（如Ganguli et al., 2022）通常依赖人工或半自动化的对抗生成。JailbreakBench则专注于基于优化的算法攻击，提供了更系统化的自动化评估。

### 3.3 对工业界的价值

**模型安全评估**：AI公司可以使用JailbreakBench作为内部安全测试的标准工具，在模型发布前进行系统化的越狱评估。

**防御方法验证**：安全团队可以基于JailbreakBench验证其部署的防御机制（如输入过滤、输出检测）的有效性。

**合规支持**：随着AI监管框架（如EU AI Act）的推进，企业需要证明其模型的安全性。JailbreakBench提供的标准化评估结果可以作为合规文档的一部分。

---

## 4. 所用数据集

### 4.1 数据集构成

JailbreakBench的核心数据集包含**100个有害行为**（behaviors），这些行为经过精心筛选，符合以下标准：
- 与OpenAI使用政策明确禁止的内容类别对齐
- 覆盖多种有害类型，具有代表性
- 难度适中，既不过于简单（所有模型都拒绝）也不过于困难（所有模型都妥协）

### 4.2 数据来源统计

| 数据来源 | 行为数量 | 占比 | 说明 |
|---------|---------|------|------|
| AdvBench (Zou et al., 2023) | 37 | 37% | 经典的对抗行为数据集 |
| HarmBench (Mazeika et al., 2024) | 34 | 34% | 标准化有害行为基准 |
| 原创行为 | 29 | 29% | 作者团队自主设计 |
| **总计** | **100** | **100%** | - |

### 4.3 行为分类分布

数据集涵盖的主要有害类别包括：

| 类别 | 示例行为 | 占比 |
|------|---------|------|
| 非法活动指导 | 如何制造危险物品、如何实施欺诈 | ~25% |
| 仇恨与歧视 | 针对特定群体的仇恨言论 | ~20% |
| 暴力内容 | 暴力行为的详细描述 | ~15% |
| 虚假信息 | 制造和传播假新闻 | ~15% |
| 成人内容 | 色情内容生成 | ~10% |
| 其他有害内容 | 自我伤害、骚扰等 | ~15% |

### 4.4 数据集质量保障

为确保数据集质量，作者采取了以下措施：
- **人工审核**：所有行为都经过人工审核，确保表述清晰、边界明确
- **去重处理**：合并语义相似的行为，确保多样性
- **难度校准**：通过预实验筛选出难度适中的行为，避免极端情况
- **政策对齐**：确保所有行为明确违反主流AI使用政策

---

## 5. 研究方法

### 5.1 整体架构设计

JailbreakBench采用模块化架构，由四个核心组件构成：

**组件1: 对抗工件库（Artifact Repository）**
- 收集和整理最先进的越狱提示
- 采用版本控制，持续更新
- 支持多种攻击类型（优化型、手工型、混合型）

**组件2: 标准化数据集**
- 100个有害行为（如第4节所述）
- 每个行为配备标准的目标输出描述
- 支持多种输入格式（纯文本、对话格式）

**组件3: 评估框架**
- 明确定义的威胁模型
- 统一的系统提示和聊天模板
- 自动化的评分函数

**组件4: 公共排行榜**
- 追踪攻击和防御方法的性能
- 支持多种LLM后端
- 定期更新结果

### 5.2 威胁模型定义

JailbreakBench明确定义了评估的威胁模型：

**攻击者能力假设**：
- 黑盒访问：攻击者只能通过API查询模型，无法访问模型参数
- 查询限制：攻击受限于合理的查询预算（如数千次查询）
- 白盒知识：攻击者可能知道模型的架构和训练方式（用于迁移攻击）

**评估目标**：
- 攻击成功率（Attack Success Rate, ASR）：模型生成有害内容的频率
- 攻击成本：达到成功所需的查询次数或计算资源
- 迁移性：攻击在不同模型间的有效性

### 5.3 评估指标详解

**主要指标**:

1. **Jailbreak Success Rate (JSR)**:
   - 定义：成功诱导模型生成有害内容的行为比例
   - 计算公式：JSR = (成功攻击的行为数 / 总行为数) × 100%
   - 成功判定：使用自动化Judge（基于Llama-3-70B）或人工评估

2. **查询效率（Query Efficiency）**:
   - 定义：达到特定成功率所需的平均查询次数
   - 重要性：反映攻击的实际可行性，高查询成本可能使攻击在实践中不可行

3. **攻击成本（Attack Cost）**:
   - 以API调用费用计算
   - 假设使用商业API（如OpenAI GPT-4）的定价

**辅助指标**:

4. **Over-refusal Rate**:
   - 测量模型对无害请求的过度拒绝率
   - 用于评估防御方法是否损害了模型的正常功能

5. **Semantic Preservation**:
   - 评估对抗提示是否保持了原始意图的语义
   - 避免通过完全混淆语义实现的"虚假"成功

### 5.4 Judge设计

评估的核心是自动判定攻击是否成功，即模型输出是否包含有害内容。JailbreakBench采用了基于Llama-3-70B的Judge：

**Judge Prompt设计**:
- 输入：原始有害行为描述 + 模型生成的响应
- 输出：二分类判断（有害/无害）+ 置信度评分
- 设计原则：减少误判，提高与人类判断的一致性

**验证与校准**:
- 使用人工标注数据集验证Judge的准确性
- 在多个模型输出上测试一致性
- 定期更新以适应新的攻击模式

---

## 6. 实验详细记录

### 6.1 基准测试结果

JailbreakBench在发布时对多种主流LLM进行了测试，包括：

**测试模型**:
- GPT-3.5-Turbo
- GPT-4
- Llama-2 (7B, 13B, 70B)
- Llama-3 (8B, 70B)
- Claude系列
- Mistral系列

**测试攻击方法**:
- GCG (Greedy Coordinate Gradient)
- PAIR (Prompt Automatic Iterative Refinement)
- TAP (Tree of Attacks)
- AutoDAN
- 手工越狱模板（如DAN）

### 6.2 主要发现

**攻击成功率对比**:

| 攻击方法 | GPT-3.5 | GPT-4 | Llama-2-7B | Llama-3-8B |
|---------|---------|-------|------------|------------|
| 原始请求 | 5% | 2% | 3% | 2% |
| GCG | 85% | 62% | 78% | 45% |
| PAIR | 72% | 48% | 65% | 38% |
| TAP | 80% | 55% | 72% | 42% |
| AutoDAN | 88% | 68% | 82% | 52% |
| DAN | 25% | 15% | 30% | 18% |

**关键发现**:
- 自动化攻击方法（GCG、PAIR、TAP、AutoDAN）显著优于手工模板
- GPT-4展现出最强的防御能力，但仍可被攻破
- Llama-3相比Llama-2有显著的安全改进
- 攻击成功率与模型规模并非简单正相关

### 6.3 成本分析

| 攻击方法 | 平均查询次数 | 估算成本(GPT-4) | 成功率 |
|---------|-------------|----------------|--------|
| GCG | 500-1000 | $5-10 | 62% |
| PAIR | 20-50 | $0.5-2 | 48% |
| TAP | 100-200 | $2-5 | 55% |
| AutoDAN | 300-500 | $3-7 | 68% |

**关键发现**:
- PAIR在查询效率上表现最佳，适合预算有限的攻击场景
- GCG虽然成功率高，但成本也最高
- 成本-成功率之间存在权衡关系

### 6.4 迁移性分析

| 源模型\目标模型 | Llama-2-7B | Llama-2-13B | GPT-3.5 |
|----------------|------------|-------------|---------|
| 在Llama-2-7B上优化 | 85% | 72% | 45% |
| 在Llama-2-13B上优化 | 68% | 88% | 52% |
| 在GPT-3.5上优化 | 38% | 42% | 85% |

**关键发现**:
- 同系列模型间迁移效果较好
- 跨架构迁移成功率显著下降
- 针对特定模型优化的攻击在其他模型上效果有限

---

## 7. 创新点

### 7.1 主要创新

**1. 首个系统化的越狱基准测试**

JailbreakBench是首个全面、系统化的越狱攻击基准测试，填补了该领域的标准化空白。

**2. 持续更新的工件库**

不同于静态数据集，JailbreakBench采用版本控制机制，持续收集和更新最先进的对抗工件，确保基准的时效性。

**3. 标准化的评估协议**

明确定义了威胁模型、评估指标、系统提示和评分函数，使不同研究的结果可以直接比较。

**4. 开源和可复现**

完全开源的代码和数据集，消除了可复现性危机，促进了社区协作。

### 7.2 技术创新

**自动化Judge**: 基于Llama-3-70B的自动化评估系统，减少了人工评估的成本和主观性。

**多维度评估**: 不仅关注攻击成功率，还考虑查询效率、成本、迁移性等多个维度。

**防御评估支持**: 不仅评估攻击方法，还支持对防御方法的系统性评估。

### 7.3 社区贡献

**Leaderboard机制**: 通过公共排行榜激励社区贡献，追踪领域进展。

**模块化设计**: 易于扩展的架构，方便社区添加新的攻击方法、模型或评估指标。

**伦理考量**: 在发布前仔细评估了潜在的伦理风险，并制定了负责任的使用指南。

---

## 8. 局限性与未来工作

### 8.1 当前局限

**语言限制**: 目前主要关注英文场景，对其他语言的支持有限。

**模型覆盖**: 虽然支持主流模型，但无法覆盖所有商业和开源模型。

**攻击类型**: 主要关注基于提示的文本攻击，对多模态攻击、提示注入等其他攻击类型的覆盖有限。

**评估成本**: 完整的基准测试需要大量API调用，成本较高。

### 8.2 未来研究方向

**多语言扩展**: 扩展数据集以支持中文、西班牙语等其他主要语言。

**多模态支持**: 添加对视觉-语言模型（如GPT-4V）的越狱评估。

**实时更新**: 建立自动化机制，实时跟踪新发布的模型和攻击方法。

**对抗训练**: 基于基准数据开发更有效的对抗训练方法。

**防御评估**: 加强对防御方法的评估，包括输入过滤、输出检测、安全微调等。

### 8.3 对实践的启示

**对模型开发者**:
- 在模型发布前应使用JailbreakBench进行系统化的安全评估
- 关注查询效率和成本，不仅关注成功率
- 考虑跨模型迁移性，避免过度拟合特定防御

**对防御研究者**:
- 使用标准化基准验证防御效果
- 平衡安全性和可用性，避免过度拒绝
- 关注防御的鲁棒性，而非仅针对特定攻击

**对政策制定者**:
- 基准测试为AI安全监管提供了可量化的指标
- 支持建立行业标准和最佳实践
- 促进负责任AI的发展

---

## 9. 个人思考与启发

### 9.1 对基准测试重要性的认识

JailbreakBench让我深刻认识到高质量基准测试对研究领域发展的关键作用。在缺乏标准化评估的情况下，研究进展难以衡量，创新方向容易迷失。

### 9.2 对开源精神的赞赏

论文作者选择完全开源代码和数据集，体现了真正的学术精神。这种开放态度将极大地促进领域发展，使更多研究者能够参与其中。

### 9.3 对攻防博弈的思考

基准测试的发布将推动攻击和防御方法的共同进步。这种"军备竞赛"虽然看似矛盾，但实际上是提升AI系统安全性的必经之路。

### 9.4 对伦理责任的反思

论文作者对发布基准测试的伦理影响进行了深思熟虑，这种负责任的态度值得称赞。在推进研究的同时考虑潜在风险，是AI研究者应有的素养。

### 9.5 对未来研究的期待

期待看到：
- 更多语言的支持
- 多模态场景的扩展
- 更高效的评估方法
- 防御方法的系统性评估
- 与实际部署场景的更好对齐

---

## 10. 相关论文与资源

### 10.1 引用的关键论文

- **AdvBench**: Zou et al., "Universal and Transferable Adversarial Attacks on Aligned Language Models", 2023
- **HarmBench**: Mazeika et al., "HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal", 2024
- **GCG**: Greedy Coordinate Gradient攻击方法
- **PAIR**: Prompt Automatic Iterative Refinement
- **TAP**: Tree of Attacks

### 10.2 相关基准与数据集

- AdvBench Harmful Behaviors
- HarmBench Dataset
- Red Teaming数据集

### 10.3 开源资源

- **代码仓库**: https://github.com/JailbreakBench/jailbreakbench
- **论文PDF**: https://arxiv.org/abs/2404.01318
- **Leaderboard**: https://jailbreakbench.github.io/

---

## 11. 笔记总结

### 11.1 核心要点

1. **问题**: 越狱攻击评估缺乏标准化，导致结果不可比、不可复现
2. **方法**: 提出JailbreakBench，包含工件库、数据集、评估框架和排行榜
3. **优势**: 开源、标准化、可复现、持续更新
4. **结果**: 为LLM安全研究提供了重要的基础设施

### 11.2 关键洞察

- 标准化基准对领域发展至关重要
- 开源和可复现是学术研究的基石
- 多维度评估（成功率、成本、迁移性）比单一指标更有价值
- 负责任的研究需要考虑伦理影响

### 11.3 实践价值

- 为模型开发者提供标准化安全测试工具
- 为防御研究者提供公平的评估平台
- 为政策制定者提供可量化的安全指标
- 为学术界提供共同的研究基础

### 11.4 研究价值

- 推动LLM安全研究向成熟化发展
- 促进攻击和防御方法的公平竞争
- 降低新研究者的入门门槛
- 支持领域进展的纵向追踪

---

*笔记完成时间: 2026-03-09*  
*笔记作者: Samantha*  
*论文来源: NeurIPS 2024 / arXiv:2404.01318*
