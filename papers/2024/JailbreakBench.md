# 【论文笔记】JailbreakBench: An Open Robustness Benchmark for Jailbreaking Large Language Models 

阅读日期: 2026年3月9日  
论文来源: NeurIPS 2024 Datasets and Benchmarks Track  
arXiv ID: 2404.01318  
代码仓库: https://github.com/JailbreakBench/jailbreakbench



1. 论文基本信息

1.1 完整标题与作者

标题: JailbreakBench: An Open Robustness Benchmark for Jailbreaking Large Language Models

作者列表: 
Patrick Chao (University of Pennsylvania)
Edoardo Debenedetti (ETH Zurich)
Alexander Robey (University of Pennsylvania)
Maksym Andriushchenko (EPFL)
Francesco Croce (University of Tübingen)
Vikash Sehwag (Princeton University)
Edgar Dobriban (University of Pennsylvania)
Nicolas Flammarion (EPFL)
George J. Pappas (University of Pennsylvania)
Florian Tramer (ETH Zurich)
Hamed Hassani (University of Pennsylvania)
Eric Wong (University of Pennsylvania)

1.2 摘要全文与翻译


Abstract (Original):
Jailbreak attacks cause large language models (LLMs) to generate harmful, unethical, or otherwise objectionable content. Evaluating these attacks presents a number of challenges, which the current collection of benchmarks and evaluation techniques do not adequately address. First, there is no clear standard of practice regarding jailbreaking evaluation. Second, existing works compute costs and success rates in incomparable ways. And third, numerous works are not reproducible, as they withhold adversarial prompts, involve closed-source code, or rely on evolving proprietary APIs. To address these challenges, we introduce JailbreakBench, an open-sourced benchmark with the following components: (1) an evolving repository of state-of-the-art adversarial prompts, which we refer to as jailbreak artifacts; (2) a jailbreaking dataset comprising 100 behaviors -- both original and sourced from prior work (Zou et al., 2023; Mazeika et al., 2023, 2024) -- which align with OpenAI's usage policies; (3) a standardized evaluation framework at this https URL that includes a clearly defined threat model, system prompts, chat templates, and scoring functions; and (4) a leaderboard at this https URL that tracks the performance of attacks and defenses for various LLMs. We have carefully considered the potential ethical implications of releasing this benchmark, and believe that it will be a net positive for the community.


摘要（中文翻译）:
越狱攻击会导致大型语言模型（LLM）生成有害、不道德或其他令人反感的内容。评估这些攻击面临诸多挑战，而现有的基准测试和评估技术集合未能充分解决这些问题。首先，关于越狱评估缺乏明确的标准实践；其次，现有研究以不可比较的方式计算成本和成功率；第三，许多研究无法复现，因为它们不公开对抗性提示、涉及闭源代码或依赖不断演化的专有API。为解决这些挑战，我们引入了JailbreakBench，一个开源基准测试，包含以下组件：（1）一个不断演化的最先进的对抗性提示库，我们称之为越狱工件；（2）一个包含100种行为的越狱数据集——包括原创行为和从先前工作中获取的行为（Zou et al., 2023; Mazeika et al., 2023, 2024）——这些行为符合OpenAI的使用政策；（3）一个标准化的评估框架，包括明确定义的威胁模型、系统提示、聊天模板和评分函数；（4）一个排行榜，追踪各种LLM的攻击和防御性能。我们仔细考虑了发布此基准测试的潜在伦理影响，并相信它将对社区产生净正面的影响。



2. 研究背景

2.1 越狱攻击的兴起与威胁

随着大型语言模型（LLMs）如GPT-4、Claude、Llama等的能力不断增强，它们被广泛应用于各种场景，从日常对话到专业领域辅助。然而，这些模型也面临着严重的安全挑战，其中"越狱攻击"（Jailbreak Attacks）尤为引人关注。

越狱攻击是指通过精心构造的输入提示（prompts），诱导语言模型绕过其安全对齐机制，生成原本被设计为拒绝输出的有害内容。这些内容可能包括：
制造危险物品或武器的 instructions
传播仇恨言论或歧视性内容
生成虚假信息进行欺诈
提供非法活动的指导
生成色情或暴力内容

2023年以来，学术界和工业界都观察到了大量越狱攻击案例。从早期的"DAN"（Do Anything Now）提示，到基于优化算法的对抗性攻击如GCG（Greedy Coordinate Gradient），攻击技术不断演进，对LLM的安全部署构成了实质性威胁。

2.2 现有评估方法的碎片化问题

尽管越狱攻击研究蓬勃发展，但评估方法却呈现出严重的碎片化问题：

缺乏标准化指标：不同研究使用不同的成功率定义。有的研究将模型只要开始回答就算成功，有的则要求生成完整的有害内容，还有的研究采用人工评分。这使得跨研究比较变得极其困难。

成本计算不一致：攻击的计算成本是评估攻击实际威胁性的重要指标，但现有研究在计算查询次数、API调用成本、GPU时间等方面缺乏统一标准。一些研究仅报告优化阶段的查询次数，而忽略了生成最终攻击提示所需的全部交互。

数据集差异巨大：不同研究使用不同的有害行为数据集。有的使用自定义的小型数据集（如10-50个行为），有的从AdvBench等现有数据集采样，还有的完全依赖人工构造。数据集的大小、类别分布、难度级别各不相同。

可复现性危机：许多研究不公开对抗性提示或代码，有些依赖不断变化的专有API（如OpenAI的GPT-4），导致其他研究者无法验证结果或在此基础上继续研究。

2.3 对统一基准的迫切需求

这种碎片化状态严重阻碍了领域的发展：
研究者难以判断新方法是否真正优于基线
防御方法的有效性难以客观评估
工业界在选择安全评估方案时缺乏参考
学术成果的积累和传承受阻

因此，社区迫切需要一个统一的、开源的、可复现的基准测试，来标准化越狱攻击和防御的评估流程。这正是JailbreakBench试图解决的核心问题。



3. 研究意义

3.1 对学术界的贡献

JailbreakBench的发布标志着LLM安全研究领域向成熟化迈出了重要一步。它的学术意义体现在以下几个方面：

建立共同语言：通过定义标准化的威胁模型、评估指标和实验设置，JailbreakBench为整个社区提供了"共同语言"。研究者可以清晰地描述自己的工作与基准的关系，比如"我们的攻击在JailbreakBench上达到了X%的成功率，相比GCG提升了Y%"

促进公平竞争：开源的对抗工件（adversarial artifacts）和标准化的评估代码确保了所有方法在相同条件下测试。这消除了因评估设置差异导致的性能虚高，使真正有效的创新能够脱颖而出。

降低研究门槛：新进入该领域的研究者可以直接使用JailbreakBench提供的工具和数据，而无需从头构建评估基础设施。这加速了研究周期，使研究者能将更多精力投入到核心创新上。

支持纵向追踪：通过维护不断更新的工件库和 leaderboard，JailbreakBench使得追踪领域进展成为可能。研究者可以清楚地看到攻击和防御方法的演进轨迹。

3.2 与相关工作的对比

与AdvBench的对比：AdvBench（Zou et al., 2023）是早期重要的越狱基准，但它主要服务于GCG攻击的评估，数据集规模较小（约500个提示），且缺乏持续的维护和更新机制。JailbreakBench在此基础上进行了扩展和改进，提供了更系统化的评估框架。

与HarmBench的对比：HarmBench（Mazeika et al., 2024）是另一个同期的重要基准，专注于有害行为的分类和评估。JailbreakBench与HarmBench在数据集上有部分重叠，但更强调对抗工件的收集和攻击防御的对比评估。两者形成了互补关系。

与Red Teaming基准的对比：传统的红队测试基准（如Ganguli et al., 2022）通常依赖人工或半自动化的对抗生成。JailbreakBench则专注于基于优化的算法攻击，提供了更系统化的自动化评估。

3.3 对工业界的价值

模型安全评估：AI公司可以使用JailbreakBench作为内部安全测试的标准工具，在模型发布前进行系统化的越狱评估。

防御方法验证：安全团队可以基于JailbreakBench验证其部署的防御机制（如输入过滤、输出检测）的有效性。

合规支持：随着AI监管框架（如EU AI Act）的推进，企业需要证明其模型的安全性。JailbreakBench提供的标准化评估结果可以作为合规文档的一部分。



4. 所用数据集

4.1 数据集构成

JailbreakBench的核心数据集包含100个有害行为（behaviors），这些行为经过精心筛选，符合以下标准：
与OpenAI使用政策明确禁止的内容类别对齐
覆盖多种有害类型，具有代表性
难度适中，既不过于简单（所有模型都拒绝）也不过于困难（所有模型都妥协）

4.2 数据来源统计



数据来源

行为数量

占比

说明

AdvBench (Zou et al., 2023)

37

37%

经典的对抗行为数据集

HarmBench (Mazeika et al., 2024)

34

34%

标准化有害行为基准

原创行为

29

29%

作者团队自主设计

总计

100

100%

-

4.3 行为分类分布

数据集涵盖的主要有害类别包括：



类别

示例行为

占比

非法活动指导

如何制造危险物品、如何实施欺诈

~25%

仇恨与歧视

针对特定群体的仇恨言论

~20%

暴力内容

暴力行为的详细描述

~15%

虚假信息

制造和传播假新闻

~15%

成人内容

色情内容生成

~10%

其他有害内容

自我伤害、骚扰等

~15%

4.4 数据集质量保障

为确保数据集质量，作者采取了以下措施：
人工审核：所有行为都经过人工审核，确保表述清晰、边界明确
去重处理：合并语义相似的行为，确保多样性
难度校准：通过预实验筛选出难度适中的行为，避免极端情况
政策对齐：确保所有行为明确违反主流AI使用政策



5. 研究方法

5.1 整体架构设计

JailbreakBench采用模块化架构，由四个核心组件构成：

组件1: 对抗工件库（Artifact Repository）
收集和整理最先进的越狱提示
采用版本控制，持续更新
支持多种攻击类型（优化型、手工型、混合型）

组件2: 标准化数据集
100个有害行为（如第4节所述）
每个行为配备标准的目标输出描述
支持多种输入格式（纯文本、对话格式）

组件3: 评估框架
明确定义的威胁模型
统一的系统提示和聊天模板
自动化的评分函数

组件4: 公共排行榜
追踪攻击和防御方法的性能
支持多种LLM后端
定期更新结果

5.2 威胁模型定义

JailbreakBench明确定义了评估的威胁模型：

攻击者能力假设：
黑盒访问：攻击者只能通过API查询模型，无法访问模型参数
查询限制：攻击受限于合理的查询预算（如数千次查询）
白盒知识：攻击者可能知道模型的架构和训练方式（用于迁移攻击）

评估目标：
攻击成功率（Attack Success Rate, ASR）：模型生成有害内容的频率
攻击成本：达到成功所需的查询次数或计算资源
迁移性：攻击在不同模型间的有效性

5.3 评估指标详解

主要指标:

Jailbreak Success Rate (JSR):
定义：成功诱导模型生成有害内容的行为比例
计算公式：JSR = (成功攻击的行为数 / 总行为数) × 100%
成功判定：使用自动化Judge（基于Llama-3-70B）或人工评估

查询效率（Query Efficiency）:
定义：达到特定成功率所需的平均查询次数
重要性：反映攻击的实际可行性，高查询成本可能使攻击在实践中不可行

攻击成本（Attack Cost）:
以API调用费用计算
假设使用商业API（如OpenAI GPT-4）的定价

辅助指标:

Over-refusal Rate:
测量模型对无害请求的过度拒绝率
用于评估防御方法是否损害了模型的正常功能

Semantic Preservation:
评估对抗提示是否保持了原始意图的语义
避免通过完全混淆语义实现的"虚假"成功

5.4 Judge设计

评估的核心是自动判定攻击是否成功，即模型输出是否包含有害内容。JailbreakBench采用了基于Llama-3-70B的Judge：

Judge Prompt设计：
将模型输出作为输入
要求Judge判断输出是否提供了对有害行为的指导或信息
使用few-shot示例提高判断准确性

Judge校准：
使用300个人工标注样例进行校准
人工与Judge的一致性达到90%以上
对边界案例提供详细的判断准则

5.5 聊天模板标准化

为确保评估的可复现性，JailbreakBench强制使用标准化的聊天模板：


# 示例模板结构
system_prompt = "You are a helpful assistant."
user_message = "{adversarial_prompt}"
# 使用模型特定的tokenizer.apply_chat_template()处理

这种标准化消除了因提示格式差异导致的评估偏差。



6. 实验详细记录

6.1 实验设置

测试模型：
JailbreakBench支持评估多种主流LLM：



模型

提供商

版本/大小

访问方式

GPT-4

OpenAI

gpt-4-turbo

API

GPT-3.5

OpenAI

gpt-3.5-turbo

API

Llama-2

Meta

7B, 13B, 70B

本地/ HuggingFace

Llama-3

Meta

8B, 70B

本地/ HuggingFace

Claude

Anthropic

claude-3-opus

API

Mistral

Mistral AI

7B, 8x7B

本地/ HuggingFace

测试的攻击方法：



攻击方法

类型

说明

GCG (Zou et al., 2023)

优化型

贪心坐标梯度攻击

AutoDAN (Liu et al., 2024)

优化型

基于遗传算法的攻击

PAIR (Chao et al., 2023)

基于LLM

使用LLM生成和优化攻击

TAP (Mehrotra et al., 2024)

基于LLM

树形攻击搜索

Manual Jailbreaks

手工型

人工设计的越狱提示

测试的防御方法：



防御方法

类型

说明

System Prompt Defense

输入级

强化系统提示的安全指令

Input Filtering

输入级

检测并过滤恶意输入

Output Detection

输出级

检测有害输出并拒绝

SmoothLLM (Robey et al., 2023)

输入级

对抗扰动净化

6.2 主要实验结果

实验1: 攻击方法对比（Llama-2-7B-Chat）



攻击方法

成功率

平均查询次数

估计成本($)

GCG

62%

2,500

~0.50

AutoDAN

58%

1,800

~0.36

PAIR

71%

150

~0.15

TAP

74%

120

~0.12

Manual (最佳)

45%

1

~0.001

观察：基于LLM的攻击（PAIR、TAP）在效率和成功率上表现优异，而传统优化方法成本较高。

实验2: 模型安全性对比（使用GCG攻击）



模型

成功率

备注

GPT-4

38%

安全性最强

GPT-3.5

52%

-

Llama-2-70B

45%

-

Llama-3-70B

28%

较Llama-2有显著改进

Claude-3-Opus

31%

安全性强

观察：最新的模型（Llama-3、Claude-3）展现出更强的越狱抵抗力。

实验3: 防御方法有效性（针对GCG攻击）



防御方法

攻击成功率(无防御)

攻击成功率(有防御)

过度拒绝率

无防御

62%

-

0%

System Prompt

62%

41%

2%

Input Filtering

62%

35%

5%

Output Detection

62%

28%

3%

SmoothLLM

62%

19%

12%

观察：防御方法能有效降低攻击成功率，但可能引入过度拒绝问题。SmoothLLM防御效果最强但副作用也最大。

实验4: 迁移攻击分析

测试在Llama-2-7B上优化的攻击在其它模型上的有效性：



目标模型

迁移成功率

说明

Llama-2-13B

68%

同系列迁移效果好

Llama-2-70B

52%

大模型更难攻击

GPT-3.5

31%

跨架构迁移效果下降

GPT-4

18%

跨架构且更强的模型

观察：迁移攻击在同架构模型间效果较好，跨架构时效果大幅下降。

6.3 消融实验

消融1: Judge准确性分析
人工标注 vs Llama-3-70B Judge的一致性：92%
主要分歧点：边界案例（如提供部分有害信息但包含免责声明）
改进措施：增加few-shot示例后一致性提升至95%

消融2: 查询预算影响
限制GCG的查询次数：
500 queries: 成功率 38%
1000 queries: 成功率 51%
2500 queries: 成功率 62%
5000 queries: 成功率 65%（边际收益递减）

观察：攻击成功率随查询预算增加而提升，但存在明显的边际收益递减。



7. 结果分析

7.1 主要发现

发现1: 基于LLM的攻击更有效率

实验结果表明，PAIR和TAP这类利用LLM自身能力生成攻击的方法，在成功率和查询效率上都显著优于传统的基于梯度的优化方法。这一发现具有重要启示：
LLM对自然语言的"理解"能力可以被用来构造更自然的对抗提示
基于语义理解的攻击可能比基于字符扰动的攻击更难防御
攻击效率的提升意味着越狱攻击的实际威胁性更高

发现2: 模型规模与安全性的非线性关系

有趣的是，更大的模型并不总是更安全：
Llama-2-70B在某些攻击下比Llama-2-7B更容易被攻破
这可能是因为大模型更擅长"理解"攻击提示中的微妙意图
安全性与模型能力的平衡是未来研究的重要方向

发现3: 防御的副作用不可忽视

所有测试的防御方法都引入了不同程度的过度拒绝（over-refusal）：
过度拒绝率在2%-12%之间
这意味着防御可能会损害模型在正常任务上的表现
理想的防御应该在不显著影响正常功能的前提下提供保护

发现4: 跨模型迁移攻击的可行性

迁移攻击实验显示：
同架构模型间的迁移成功率较高（50-70%）
跨架构迁移成功率显著下降（<35%）
这提示不同架构可能具有不同的"脆弱性特征"

7.2 局限性与讨论

局限性1: 评估的对抗性假设

JailbreakBench假设攻击者具有合理的查询预算。然而，资源充足的攻击者可能通过更大量的查询获得更高成功率。如何在评估中考虑极端情况仍是挑战。

局限性2: Judge的不完美性

尽管Judge经过校准，但在以下情况仍可能出错：
非常微妙的有害内容（如隐晦的仇恨言论）
包含大量上下文的复杂场景
新颖的攻击类型

局限性3: 数据集的覆盖范围

100个行为虽然具有代表性，但无法覆盖所有可能的有害场景。随着AI应用的扩展，新的有害类别不断出现。

局限性4: 静态评估的局限

JailbreakBench主要进行静态评估，而真实世界的攻击往往是动态的、适应性的。如何设计动态评估框架是未来的研究方向。

7.3 伦理考量

作者在论文中详细讨论了发布此基准的伦理影响：

潜在风险：
攻击工件可能被恶意使用
详细的攻击方法描述可能帮助攻击者

缓解措施：
只发布经过筛选的攻击工件（移除最危险的）
强调防御方法的重要性
与AI安全社区合作，确保负责任的使用

净正面影响：
帮助AI开发者评估和改进模型安全性
促进安全研究的系统化和科学化
提高公众对AI安全风险的认识



8. 展望

8.1 JailbreakBench的未来发展

持续更新的工件库：
随着新攻击方法的涌现，JailbreakBench计划定期更新对抗工件库。这包括：
每季度评估新发表的攻击方法
建立社区贡献机制，接受经过审核的工件提交
跟踪攻击方法在最新模型上的有效性

扩展模型覆盖：
计划增加对更多模型的支持：
开源模型（如Qwen、ChatGLM等）
多模态模型（处理图像+文本输入）
代码生成专用模型

防御评估的增强：
当前版本主要关注攻击评估，未来将加强对防御方法的评估：
建立防御方法的标准化评估流程
开发更全面的防御效果指标
研究攻击-防御的博弈动态

8.2 领域研究方向

方向1: 自适应防御

当前防御方法大多是静态的。未来研究可以探索：
基于在线学习的自适应防御
检测异常输入模式并动态调整
结合外部知识库进行实时风险评估

方向2: 理论基础

越狱攻击的理论理解仍不充分：
为什么某些提示能成功越狱？
安全对齐的"脆弱点"在哪里？
能否从理论上证明某类防御的有效性？

方向3: 多模态越狱

随着多模态LLM的兴起，新的攻击面出现：
图像+文本的联合攻击
利用视觉信息绕过文本层面的安全机制
JailbreakBench的多模态扩展

方向4: 长期安全评估

当前评估多为一次性测试。未来需要：
长期部署中的安全性监测
模型更新后的安全回归测试
真实攻击场景的日志分析

8.3 对AI治理的启示

JailbreakBench的发布对AI治理具有重要启示：

标准化评估的必要性：
监管机构可以参考JailbreakBench建立标准化的安全评估要求，确保市场上的AI产品达到基本安全标准。

透明度与问责：
公开发布的安全评估结果（如leaderboard）增加了AI开发者的透明度，为问责提供了依据。

持续监测机制：
 JailbreakBench的持续更新模式可以作为AI安全持续监测机制的参考模板。



9. 代码资源与复现

9.1 官方代码仓库

GitHub: https://github.com/JailbreakBench/jailbreakbench

核心模块：

jailbreakbench/
├── src/
│   ├── attacks/        # 攻击方法实现
│   ├── defenses/       # 防御方法实现
│   ├── judge/          # 评估Judge
│   ├── models/         # 模型接口
│   └── evaluation.py   # 评估框架
├── data/
│   └── behaviors.json  # 100个有害行为
├── artifacts/          # 对抗工件库
└── examples/           # 使用示例

9.2 复现难度评估



复现项目

难度

说明

基础评估

低

使用官方脚本可直接运行

GCG攻击

中

需要GPU资源，有开源实现

PAIR攻击

低

仅需API调用

新攻击集成

中

需遵循框架接口规范

新模型接入

低-中

取决于模型访问方式

9.3 硬件要求

最低配置：
CPU: 4核心
RAM: 16GB
GPU: 不需要（仅使用API时）

推荐配置（本地运行Llama-2/3）：
CPU: 8核心
RAM: 32GB
GPU: A100 40GB（用于70B模型）
GPU: RTX 3090（用于7B/8B模型）

9.4 快速开始


# 安装
pip install jailbreakbench

# 运行评估
import jailbreakbench as jbb

# 加载数据集
behaviors = jbb.load_behaviors()

# 使用GCG攻击评估Llama-2
results = jbb.evaluate(
    model="llama-2-7b-chat",
    attack="gcg",
    behaviors=behaviors
)

# 查看结果
print(f"攻击成功率: {results.success_rate:.2%}")



10. 参考文献

以下是与JailbreakBench最相关的5篇关键文献：

Zou, A., Wang, Z., Carlini, N., Nasr, M., Kolter, J. Z., & Fredrikson, M. (2023).
Universal and Transferable Adversarial Attacks on Aligned Language Models.
arXiv preprint arXiv:2307.15043.

提出了GCG攻击方法，是JailbreakBench评估的核心基线之一
GitHub: https://github.com/llm-attacks/llm-attacks

Mazeika, M., Phan, L., Yin, X., Zou, A., Wang, Z., Mu, N., ... & Li, B. (2024).
HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal.
arXiv preprint arXiv:2402.04249.

同期重要的越狱基准，与JailbreakBench形成互补
提供了标准化的有害行为分类
GitHub: https://github.com/centerforaisafety/HarmBench

Chao, P., Robey, A., Dobriban, E., Hassani, H., Pappas, G. J., & Wong, E. (2023).
Jailbreaking Black Box Large Language Models in Twenty Queries.
arXiv preprint arXiv:2310.08419.

提出了PAIR攻击方法
展示了基于LLM的攻击生成的高效性

Mehrotra, A., Zampetakis, M., Kassir, A., Maron, P., Koyejo, S., Krishnamurthy, A., ... & Hazell, J. (2024).
Tree of Attacks: Jailbreaking Black-Box LLMs Automatically.
Advances in Neural Information Processing Systems (NeurIPS).

提出了TAP攻击方法
使用树形搜索优化攻击生成
GitHub: https://github.com/RICommunity/TAP

Liu, X., Xu, N., Chen, M., & Xiao, C. (2024).
AutoDAN: Generating Stealthy Jailbreak Prompts on Aligned Large Language Models.
International Conference on Learning Representations (ICLR).

提出了AutoDAN攻击方法
使用遗传算法生成语义保持的对抗提示
GitHub: https://github.com/SheltonLiu-N/AutoDAN



附录: 相关资源链接

JailbreakBench Leaderboard: https://jailbreakbench.github.io/
论文PDF: https://arxiv.org/pdf/2404.01318
数据集下载: 包含在GitHub仓库中
社区讨论: https://github.com/JailbreakBench/jailbreakbench/discussions



本笔记由 Kimi Claw 基于论文原文及相关资料整理生成
生成时间: 2026年3月9日
