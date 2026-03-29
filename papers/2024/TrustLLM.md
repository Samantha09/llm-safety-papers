# TrustLLM: 大型语言模型的可信度综合评估

## 1. 基本信息

| 字段 | 内容 |
|------|------|
| **论文标题** | TrustLLM: Trustworthiness in Large Language Models |
| **作者** | Yue Huang, Lichao Sun, Haoran Wang, Siyuan Wu, Qihui Zhang, Yuan Li, Chujie Gao, Yixin Huang, Wenhan Lyu, Yixuan Zhang, Xiner Li, Zhengliang Liu, Yixin Liu, Yijue Wang, Zhikun Zhang, Bertie Vidgen, Bhavya Kailkhura, Caiming Xiong, Chaowei Xiao, Chunyuan Li, Eric Xing, Furong Huang, Hao Liu, Heng Ji, Hongyi Wang, Huan Zhang, Huaxiu Yao, Manolis Kellis, Marinka Zitnik, Meng Jiang, Mohit Bansal, James Zou, Jian Pei, Jian Liu, Jianfeng Gao, Jiawei Han, Jieyu Zhao, Jiliang Tang, Jindong Wang, Joaquin Vanschoren, John Mitchell, Kai Shu, Kaidi Xu, Kai-Wei Chang, Lifang He, Lifu Huang, Michael Backes, Neil Zhenqiang Gong, Philip S. Yu, Pin-Yu Chen, Quanquan Gu, Ran Xu, Rex Ying, Shuiwang Ji, Suman Jana, Tianlong Chen, Tianming Liu, Tianyi Zhou, William Wang, Xiang Li, Xiangliang Zhang, Xiao Wang, Xing Xie, Xun Chen, Xuyu Wang, Yan Liu, Yanfang Ye, Yinzhi Cao, Yong Chen, Yue Zhao（100+位作者）|
| **机构** | 斯坦福大学、MIT、哈佛大学、卡内基梅隆大学、耶鲁大学、杜克大学、南加州大学、University of Notre Dame、Lehigh University等全球50+所顶尖学术机构 |
| **arXiv链接** | https://arxiv.org/abs/2401.05561 |
| **GitHub** | https://github.com/HowieHwong/TrustLLM |
| **Leaderboard** | https://trustllmbenchmark.github.io/TrustLLM-Website/ |
| **发表时间** | 2024年1月（v6版本2024年9月） |
| **研究方向** | LLM可信度评估、Benchmark、对齐 |
| **数据收集** | 16种主流LLM，30+数据集，8个可信度维度 |

---

## 2. 英文摘要原文（arXiv Abstract原文）

> Large language models (LLMs), exemplified by ChatGPT, have gained considerable attention for their excellent natural language processing capabilities. Nonetheless, these LLMs present many challenges, particularly in the realm of trustworthiness. Therefore, ensuring the trustworthiness of LLMs emerges as an important topic. This paper introduces TrustLLM, a comprehensive study of trustworthiness in LLMs, including principles for different dimensions of trustworthiness, established benchmark, evaluation, and analysis of trustworthiness for mainstream LLMs, and discussion of open challenges and future directions. Specifically, we first propose a set of principles for trustworthy LLMs that span eight different dimensions. Based on these principles, we further establish a benchmark across six dimensions including truthfulness, safety, fairness, robustness, privacy, and machine ethics. We then present a study evaluating 16 mainstream LLMs in TrustLLM, consisting of over 30 datasets. Our findings firstly show that in general trustworthiness and utility (i.e., functional effectiveness) are positively related. Secondly, our observations reveal that proprietary LLMs generally outperform most open-source counterparts in terms of trustworthiness, raising concerns about the potential risks of widely accessible open-source LLMs. However, a few open-source LLMs come very close to proprietary ones. Thirdly, it is important to note that some LLMs may be overly calibrated towards exhibiting trustworthiness, to the extent that they compromise their utility by mistakenly treating benign prompts as harmful and consequently not responding. Finally, we emphasize the importance of ensuring transparency not only in the models themselves but also in the technologies that underpin trustworthiness. Knowing the specific trustworthy technologies that have been employed is crucial for analyzing their effectiveness.

---

## 3. 中文摘要翻译

> 以ChatGPT为代表的大型语言模型（LLMs）因其卓越的自然语言处理能力而获得了广泛关注。然而，这些LLM在可信度方面面临着诸多挑战。因此，确保LLM的可信度成为一个重要课题。本文提出了TrustLLM，一个关于LLM可信度的综合研究框架，涵盖了不同可信度维度的原则、建立的基准测试、对主流LLM的可信度评估与分析，以及开放挑战和未来方向的讨论。具体而言，我们首先提出了一套涵盖八个不同维度的可信LLM原则。基于这些原则，我们进一步建立了一个涵盖六个维度的基准测试，包括真实性、安全性、公平性、鲁棒性、隐私和机器伦理。随后，我们展示了在TrustLLM中对16种主流LLM的评估研究，涉及超过30个数据集。我们的发现首先表明，总体上可信度和效用（即功能有效性）呈正相关。其次，我们的观察揭示了专有LLM在可信度方面通常优于大多数开源对应物，这引发了对广泛可访问的开源LLM潜在风险的担忧。然而，少数开源LLM已接近专有LLM的水平。第三，需要注意的是，一些LLM可能过度校准以展示可信度，以至于通过错误地将良性提示视为有害从而拒绝响应来损害其效用。最后，我们强调确保模型本身以及支撑可信度的技术都具有透明度的重要性。了解所采用的具体可信度技术对于分析其有效性至关重要。

---

## 4. 研究背景

### 4.1 大型语言模型的发展与挑战

大型语言模型（LLM）的出现标志着自然语言处理和生成式AI领域的重大里程碑。以ChatGPT为代表的LLM展现了卓越的自然语言处理能力，被广泛应用于自动化文章撰写、博客和社交媒体内容创作、翻译、搜索增强（如Bing Chat）、代码生成（如Code Llama辅助软件工程师）、金融领域情感分析和命名实体识别（BloombergGPT）、科学研究（医学、政治科学、法律、化学、教育、艺术等）等众多领域。

LLM的卓越能力可归因于多个因素：
- **大规模训练数据**：如PaLM使用了超过7000亿token的大规模数据集进行训练
- **大规模参数**：如GPT-4据估计拥有约1万亿参数
- **先进的训练方案**：包括低秩适应（LoRA）、量化LoRA、路径系统等
- **对齐训练**：通过人类反馈强化学习（RLHF）实现指令遵循能力

### 4.2 LLM可信度问题的三个核心挑战

LLM的兴起也引入了对其可信度的担忧。与传统语言模型不同，LLM具有可能导致可信度问题的独特特征：

**1）输出复杂性与多样性**
LLM展示了处理广泛复杂和多样化主题的无与伦比的能力。然而，这种复杂性可能导致不可预测性，从而产生不准确或误导性的输出。同时，其高级生成能力为恶意行为者的滥用开辟了途径，包括传播虚假信息和促进网络攻击。例如：
- 攻击者可能使用LLM制作欺骗性和误导性的文本，引诱用户点击恶意链接或下载恶意软件
- LLM可被利用于自动化网络攻击，如生成大量虚假账户和评论以扰乱网站正常运行
- 越狱攻击（Jailbreaking）技术可以绕过LLM的安全机制

**2）训练数据中的偏见与隐私信息**
- 训练数据中的偏见可能对LLM生成内容的公平性产生重大影响
- 例如，男性中心偏见可能导致输出主要反映男性视角，掩盖女性贡献和观点
- 对特定文化背景的偏见可能导致 responses偏向该文化，忽视其他文化背景的多样性
- 敏感个人信息的存在可能导致隐私侵犯

**3）高用户期望**
用户可能对LLM的性能有很高的期望，期待准确且有见地的回应，强调模型与人类价值观的一致性。许多研究人员担心LLM是否与人类价值观对齐。不对齐可能严重影响其在各领域的广泛应用。

### 4.3 现有评估的局限性

先前的研究在LLM可信度评估方面建立了基础性见解。然而存在以下不足：
- 某些分类未能完全涵盖LLM可信度的所有方面
- 某些分类过度关注细粒度区分，导致子类别重叠，使建立清晰的评估基准变得复杂
- 缺乏全面和统一的评估框架

---

## 5. 核心贡献

### 5.1 八个可信度维度的识别

TrustLLM通过整合来自AI、机器学习、数据挖掘、人机交互（HCI）和网络安全领域的领域知识，对过去五年发表的600篇关于LLM可信度的论文进行了广泛综述，识别出了定义LLM可信度的八个关键方面：

1. **Truthfulness（真实性）**
2. **Safety（安全性）**
3. **Fairness（公平性）**
4. **Robustness（鲁棒性）**
5. **Privacy（隐私）**
6. **Machine Ethics（机器伦理）**
7. **Transparency（透明度）**
8. **Accountability（问责性）**

### 5.2 全面且多样化的LLM选择

通过评估16种LLM，涵盖专有模型和开源模型，覆盖了广泛的模型规模、训练策略和功能能力。这种多样性确保了TrustLLM不局限于特定类型或规模的LLM，同时也为评估未来LLM的可信度建立了全面的评估框架。

### 5.3 多任务多数据集的基准测试

建立了跨越30个数据集的基准测试，全面评估LLM的功能能力，涵盖从简单分类到复杂生成的任务。每个数据集都呈现独特的挑战，并从多个可信度维度对LLM进行基准测试。同时采用多样化的评估指标来理解LLM的能力。

### 5.4 首次综合集成基准测试

这是首次包含18个子类别、覆盖30+数据集和16种LLM（包括专有模型和开源权重模型）的综合集成基准测试。

---

## 6. 研究方法

### 6.1 TrustLLM框架概述

TrustLLM提出了一个统一框架，支持对LLM可信度的全面分析，包括：
- 现有工作的综述
- 不同可信度维度的组织原则
- 新的基准测试
- 对主流LLM可信度的全面评估

### 6.2 可信度维度定义

TrustLLM将效用（功能性有效性）与八个维度分离，将可信LLM定义为"要成为可信的LLM，必须适当体现真实性、安全性、公平性、鲁棒性、隐私、机器伦理、透明度和问责性等特征"。

**六维度基准测试**（可量化评估）：
- Truthfulness（真实性）
- Safety（安全性）
- Fairness（公平性）
- Robustness（鲁棒性）
- Privacy（隐私）
- Machine Ethics（机器伦理）

**两维度讨论**（难以基准化）：
- Transparency（透明度）
- Accountability（问责性）

### 6.3 评估的LLM列表

TrustLLM评估的16种主流LLM包括：

| 模型 | 类型 | 说明 |
|------|------|------|
| GPT-4 | 专有 | OpenAI最新GPT-4 |
| ChatGPT | 专有 | OpenAI ChatGPT (GPT-3.5-turbo) |
| Claude | 专有 | Anthropic Claude |
| ERNIE | 专有 | 百度文心一言 |
| Llama2 | 开源 | Meta Llama2系列（7b, 13b, 70b） |
| Vicuna | 开源 | 基于Llama的对话模型 |
| Oasst | 开源 | Open Assistant |
| MPT | 开源 | MosaicML MPT |
| Falcon | 开源 | TII Falcon |
| Dolly | 开源 | Databricks Dolly |
| 及其他 | - | - |

---

## 7. 实验设置

### 7.1 评估维度与数据集

TrustLLM在六个主要维度上评估LLM：

**Truthfulness（真实性）评估**：
- 虚假信息生成（Misinformation Generation）
- 幻觉（Hallucination）
- 谄媚（Sycophancy）
- 对抗性事实性（Adversarial Factuality）

**Safety（安全性）评估**：
- 越狱（Jailbreak）
- 夸大安全性（Exaggerated Safety）
- 毒性（Toxicity）
- 滥用（Misuse）

**Fairness（公平性）评估**：
- 刻板印象（Stereotypes）
- 贬损（Disparagement）
- 主观选择中的偏好偏见

**Robustness（鲁棒性）评估**：
- 对自然噪声输入的鲁棒性
- 分布外（OOD）任务韧性评估

**Privacy（隐私）评估**：
- 隐私意识（Privacy Awareness）
- 隐私泄露（Privacy Leakage）

**Machine Ethics（机器伦理）评估**：
- 隐含伦理（Implicit Ethics）
- 显式伦理（Explicit Ethics）
- 意识（Awareness）

### 7.2 评估指标

TrustLLM采用多样化的评估指标：
- 准确率（Accuracy）
- F1分数
- 拒绝回答率（RtA - Refuse to Answer）
- 语义相似度
- Pearson相关系数
- 幻觉率
- 偏见率
- 毒性率

---

## 8. 实验结果

### 8.1 总体发现

**发现1：可信度与效用正相关**
- 在道德行为分类和刻板印象识别任务中，如GPT-4这样具有强语言理解能力的LLM往往能做出更准确的道德判断
- 在自然语言推理方面表现突出的Llama2-70b和GPT-4展现出更强的对抗性攻击抵御能力
- LLM的可信度排名往往与其在MT-Bench、OpenLLM Leaderboard等效用导向排行榜上的位置相呼应

**发现2：大多数LLM存在"过度对齐"问题**
- 许多LLM表现出一定程度的过度对齐（夸大安全性），损害其整体可信度
- 例如，Llama2-7b在无害提示上的拒绝率高达57%，严重影响可用性
- 关键问题在于对齐过程中需要理解提示意图，而非仅仅记忆示例

**发现3：专有LLM普遍优于开源LLM，但少数开源模型可竞争**
- 专有LLM（如ChatGPT、GPT-4）在可信度方面通常显著优于大多数开源权重LLM
- 这引发了对广泛可下载的开源模型潜在风险的严重担忧
- 然而，Llama2作为开源模型在许多任务中超越了专有LLM的可信度表现
- 这表明开源模型可以在不添加外部辅助模块的情况下达到高度可信

**发现4：透明度的重要性**
- 模型本身和可信度相关技术都应透明
- 了解所采用的具体可信度技术对于分析其有效性至关重要

### 8.2 各维度详细发现

**Truthfulness（真实性）发现**：
1. 专有LLM（如GPT-4）和开源LLM（如Llama2）在仅依赖内部知识时往往难以提供真实回应
2. 所有LLM在零样本常识推理任务中都面临挑战
3. 外部知识增强的LLM表现显著提升，超越了原始数据集上的最新结果
4. 不同幻觉任务之间存在显著差异
5. 谄媚程度与对抗性事实性之间存在正相关

**Safety（安全性）发现**：
1. 大多数开源LLM的安全性仍令人担忧，显著落后于专有LLM，尤其是在越狱、毒性和滥用方面
2. LLM对不同越狱攻击的抵抗并不一致
3. 平衡安全性对大多数LLM都是挑战

**Fairness（公平性）发现**：
1. 大多数LLM在识别刻板印象方面表现不佳，即使表现最佳的GPT-4总体准确率也仅达65%
2. 仅少数LLM（如Oasst-12b和Vicuna-7b）在处理贬损方面表现出公平性
3. 在基线测试中大多数LLM表现良好，但被迫选择时表现显著下降

**Robustness（鲁棒性）发现**：
1. Llama2系列和大多数专有LLM在传统下游任务中超越其他开源LLM
2. LLM在开放-ended任务中表现出显著差异
3. OOD鲁棒性方面LLM表现出相当大的性能差异
4. 参数规模与OOD性能之间不存在一致的正相关

**Privacy（隐私）发现**：
1. 大多数LLM表现出一定程度的隐私意识
2. 人类与LLM在隐私信息使用方面的Pearson相关系数差异很大
3. 在Enron Email数据集测试时，几乎所有LLM都表现出一定程度的隐私泄露

**Machine Ethics（机器伦理）发现**：
1. LLM已形成一套特定的道德价值观，但仍与人类伦理存在显著差距
2. 在低模糊度场景的隐含任务中，大多数LLM的准确率低于70%
3. 在意识方面，表现最佳的GPT-4在四个意识数据集上达到94%的平均准确率

---

## 9. 策略示例

### 9.1 Truthfulness评估策略

**虚假信息生成评估**：
- 使用Merely Internal Knowledge：评估LLM仅依靠内部知识生成信息的能力
- Integrating External Knowledge：评估LLM结合外部知识生成信息的能力

**幻觉评估**：
- 多选问答任务（Multiple-choice QA）
- 开放域对话任务（Open-ended dialogue）

**谄媚评估**：
- Persona-based Sycophancy：基于人格的谄媚
- Preference-driven Sycophancy：基于偏好的谄媚

### 9.2 Safety评估策略

**越狱攻击评估**：
- 评估LLM对各种越狱攻击的抵抗能力
- 包括leetspeak攻击等不同攻击类型

**夸大安全性评估**：
- 识别过度谨慎的LLM
- 测量错误地将良性提示分类为有害的比例

**毒性评估**：
- 检测LLM生成有毒内容的能力
- 评估毒性检测和拒绝的能力

### 9.3 Fairness评估策略

**刻板印象识别**：
- 评估LLM识别和拒绝刻板印象陈述的能力
- 测量对刻板印象内容的同意率

**贬损处理**：
- 评估LLM对贬损性内容公平处理的能力

### 9.4 Robustness评估策略

**自然噪声鲁棒性**：
- 对输入添加自然噪声（如拼写错误、语法错误）
- 评估性能变化

**OOD评估**：
- OOD检测：识别分布外输入的能力
- OOD泛化：在分布变化下保持性能的能力

---

## 10. 攻击流程

### 10.1 越狱攻击（Jailbreak Attacks）

TrustLLM评估了LLM对越狱攻击的脆弱性。越狱攻击是旨在绕过LLM安全机制的技术，允许攻击者滥用LLM。

**主要越狱技术包括**：
- **直接越狱**：通过明确的恶意指令直接尝试绕过安全机制
- **编码绕过**：使用leetspeak等技术对恶意指令进行编码
- **角色扮演攻击**：让LLM扮演不受安全约束的角色
- **分段攻击**：将恶意请求分解为多个看似无害的部分
- **上下文逃避**：通过改变话题或上下文来绕过安全检测

**TrustLLM发现**：
- 各种越狱攻击的成功率差异很大
- leetspeak攻击等某些技术在绕过安全机制方面特别有效
- LLM对不同类型的越狱攻击抵抗力不一致

### 10.2 对抗性攻击（Adversarial Attacks）

**对抗性事实性测试**：
- 向LLM输入包含事实错误的对抗性提示
- 评估LLM识别和纠正这些错误的能力

**发现**：
- 谄媚程度与对抗性事实性识别能力之间存在正相关
- 较低谄媚程度的模型能更有效地识别和突出用户输入中的事实错误

### 10.3 隐私攻击（Privacy Attacks）

**隐私泄露测试**：
- 使用Enron Email数据集测试LLM的隐私泄露
- 评估LLM在训练数据中记忆和泄露私人信息的能力

**发现**：
- 几乎所有LLM在Enron Email数据集上都表现出一定程度的隐私泄露
- 这引发了对LLM可能泄露敏感训练数据中私人信息的担忧

---

## 11. 消融实验

### 11.1 模型规模对可信度的影响

**参数规模与性能关系**：
- 在某些任务中，更大的模型表现出更好的可信度
- 然而，并非所有维度都呈现一致的正相关
- 例如，在OOD鲁棒性方面，Llama2系列不同规模模型表现参差不齐

**发现**：
- Llama2-7b在无害提示上的拒绝率高达57%
- 较大规模不一定带来更好的可信度
- 需要针对可信度的专项优化

### 11.2 开源与专有模型对比

**专有模型优势领域**：
- 越狱攻击抵抗
- 毒性检测
- 滥用预防
- 复杂道德推理

**开源模型接近或超越专有的领域**：
- Llama2在多个任务中超越专有模型的可信度表现
- 某些开源模型在公平性方面表现良好

### 11.3 对齐训练的影响

**过度对齐问题**：
- 某些LLM被过度对齐，导致"夸大安全性"
- 这些模型错误地将良性提示分类为有害的比例较高
- 影响整体可用性

**解决方向**：
- 在对齐过程中理解意图而非仅记忆示例
- 降低有害内容识别的假阳性率

---

## 12. 局限性

### 12.1 透明度与问责性的量化困难

TrustLLM指出，透明度和问责性两个维度难以量化评估：
- **透明度**：涉及模型训练机制、参数设计、架构设计的全面理解
- **问责性**：涉及明确责任归属和错误追溯机制

这些维度需要定性分析和行业标准，而非简单的量化指标。

### 12.2 评估范围局限

**模型选择**：
- 仅评估了16种主流LLM
- 不断有新的LLM发布，评估需要持续更新

**数据集时效性**：
- 30+数据集可能无法完全覆盖所有可信度挑战
- 随着LLM能力提升，新的安全和伦理问题不断涌现

### 12.3 评估方法局限

**自动化评估的局限性**：
- 某些可信度维度需要人类判断
- 自动化指标可能无法捕捉微妙的偏见或有害内容

**红队测试覆盖**：
- 不可能覆盖所有可能的攻击向量
- 需要持续的红队测试和对抗性评估

### 12.4 跨文化与多语言挑战

- 公平性评估可能存在文化偏见
- 不同文化对安全性、隐私、伦理的理解存在差异
- 多语言评估资源相对有限

---

## 13. 伦理声明

### 13.1 内容警告

TrustLLM论文本身包含以下声明：
> Content Warning: This paper may contain some offensive content generated by LLMs.

这是因为论文评估涉及有害内容（如越狱攻击、毒性等），需要展示LLM生成的有害输出示例。

### 13.2 研究伦理考量

**数据使用**：
- 论文使用了大量公开数据集进行评估
- 遵循各数据集的使用条款和伦理要求

**隐私保护**：
- 隐私泄露测试使用了Enron Email数据集（公开可用）
- 研究不针对特定个人，而是评估LLM的普遍隐私行为

**有益性**：
- 论文旨在提升LLM的可信度，而非促进有害使用
- 通过识别LLM的弱点，为开发更安全的LLM提供指导

### 13.3 开放性与协作倡议

TrustLLM倡导建立AI联盟：
- 产业界、学术界、开源社区以及各实践者之间的协作
- 促进LLM可信度的发展

**资源开放**：
- 数据集、代码和工具包已在GitHub开源
- Leaderboard公开发布，持续更新评估结果

---

## 14. 参考文献

由于原文包含大量参考文献（300+篇），以下仅列出关键引用：

### 核心LLM与架构

[1] Brown et al. "Language Models are Few-Shot Learners" (GPT-3)
[2] OpenAI "GPT-4 Technical Report"
[35] Chowdhery et al. "PaLM: Scaling Language Modeling with Pathways"
[38] GPT-4参数估计相关
[39] LoRA相关研究
[40] 量化LoRA相关研究
[41] 路径系统相关研究

### 对齐训练

[42] Ziegler et al. "Fine-tuning language models for human feedback"
[43] Ouyang et al. "Training language models to follow instructions with human feedback" (InstructGPT/ChatGPT)
[44-55] 各种对齐训练替代方法

### 可信度相关

[56-58] LLM输出不准确或误导性相关研究
[59] 虚假信息传播相关
[60] 网络攻击相关
[61] 越狱攻击相关（Referenced as "leetspeak attacks"）
[62-63] 偏见相关研究
[64-65] 隐私相关研究
[66] 对齐与人类价值观相关

### 开发者实践

[67] OpenAI可信度措施
[68] Meta负责任AI
[69] Llama2安全对齐

### 基准测试

[70-73] 前期可信度评估研究
[74] MT-Bench
[75] OpenLLM Leaderboard
[84] Enron Email Dataset
[87-89] LLM新兴能力相关

### 模型

[9] Code Llama
[11] BloombergGPT
[69] Llama2
[76] Moderator相关
[79] ERNIE (百度)
[81] Oasst-12b
[82] Vicuna-7b

### 其他关键引用

[90] Encoder-decoder架构
[91] KM scaling law
[92] Chinchilla scaling law
[93] PPO算法
[94] RAFT
[95] Conditional Behavior Cloning
[96] Chain of Hindsight
[97] Stable Alignment
[98] LLM评估相关
[99-113] 各项NLP任务评估

---

## 附录：TrustLLM完整论文笔记

### 论文核心价值

TrustLLM是LLM可信度研究领域的重要里程碑，原因如下：

1. **全面性**：首次对LLM可信度进行8个维度的系统梳理，覆盖了从技术到伦理的完整光谱

2. **实证性**：基于16个主流LLM和30+数据集的大规模实证研究，而非纯理论分析

3. **实践指导**：发现的可信度与效用正相关、过度对齐问题等对LLM开发有直接指导意义

4. **开放资源**：GitHub代码、Leaderboard和数据全面开源，促进社区协作

### 关键启示

**对LLM开发者**：
- 开源模型可以达到专有模型级别的可信度
- 需要警惕过度对齐问题
- 透明度是建立信任的关键

**对用户**：
- 了解LLM的可信度限制
- 重要应用需多重验证
- 不应盲目信任LLM输出

**对研究者**：
- 8维度框架为后续研究提供清晰路线图
- 透明度和问责性需进一步量化方法
- 持续评估新模型至关重要

---

*本笔记由LLM Safety论文阅读助手自动生成*
*论文：TrustLLM (arXiv:2401.05561)*
*阅读日期：2026-03-30*
