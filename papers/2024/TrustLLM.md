# TrustLLM: Trustworthiness in Large Language Models

## 1. 基本信息

| 项目 | 内容 |
|------|------|
| **论文标题** | TrustLLM: Trustworthiness in Large Language Models |
| **作者** | Yue Huang, Lichao Sun, Haoran Wang, Siyuan Wu, Qihui Zhang, Yuan Li, Chujie Gao, Yixin Huang, Wenhan Lyu, Yixuan Zhang, Xiner Li, Zhengliang Liu, Yixin Liu, Yijue Wang, Zhikun Zhang, Bertie Vidgen, Bhavya Kailkhura, Caiming Xiong, Chaowei Xiao, Chunyuan Li, Eric Xing, Furong Huang, Hao Liu, Heng Ji, Hongyi Wang, Huan Zhang, Huaxiu Yao, Manolis Kellis, Marinka Zitnik, Meng Jiang, Mohit Bansal, James Zou, Jian Pei, Jian Liu, Jianfeng Gao, Jiawei Han, Jieyu Zhao, Jiliang Tang, Jindong Wang, Joaquin Vanschoren, John Mitchell, Kai Shu, Kaidi Xu, Kai-Wei Chang, Lifang He, Lifu Huang, Michael Backes, Neil Zhenqiang Gong, Philip S. Yu, Pin-Yu Chen, Quanquan Gu, Ran Xu, Rex Ying, Shuiwang Ji, Suman Jana, Tianlong Chen, Tianming Liu, Tianyi Zhou, William Wang, Xiang Li, Xiangliang Zhang, Xiao Wang, Xing Xie, Xun Chen, Xuyu Wang, Yan Liu, Yanfang Ye, Yinzhi Cao, Yong Chen, Yue Zhao |
| **机构** | 来自Lehigh大学、Notre Dame大学、Stanford大学、MIT、Harvard、CMU、Oxford、CISPA等全球47所顶尖学术机构 |
| **arXiv** | [2401.05561](https://arxiv.org/abs/2401.05561) |
| **GitHub** | [HowieHwong/TrustLLM](https://github.com/HowieHwong/TrustLLM) |
| **Leaderboard** | [TrustLLM Website](https://trustllmbenchmark.github.io/TrustLLM-Website/) |
| **发表时间** | 2024年1月10日 (v1), 最新版本v6 (2024年9月30日) |
| **研究方向** | LLM可信度综合评估、Benchmark |
| **方向分类** | Benchmarks |

---

## 2. 英文摘要原文（arXiv Abstract原文）

> Large language models (LLMs), exemplified by ChatGPT, have gained considerable attention for their excellent natural language processing capabilities. Nonetheless, these LLMs present many challenges, particularly in the realm of trustworthiness. Therefore, ensuring the trustworthiness of LLMs emerges as an important topic. This paper introduces TrustLLM, a comprehensive study of trustworthiness in LLMs, including principles for different dimensions of trustworthiness, established benchmark, evaluation, and analysis of trustworthiness for mainstream LLMs, and discussion of open challenges and future directions. Specifically, we first propose a set of principles for trustworthy LLMs that span eight different dimensions. Based on these principles, we further establish a benchmark across six dimensions including truthfulness, safety, fairness, robustness, privacy, and machine ethics. We then present a study evaluating 16 mainstream LLMs in TrustLLM, consisting of over 30 datasets. Our findings firstly show that in general trustworthiness and utility (i.e., functional effectiveness) are positively related. Secondly, our observations reveal that proprietary LLMs generally outperform most open-source counterparts in terms of trustworthiness, raising concerns about the potential risks of widely accessible open-source LLMs. However, a few open-source LLMs come very close to proprietary ones. Thirdly, it is important to note that some LLMs may be overly calibrated towards exhibiting trustworthiness, to the extent that they compromise their utility by mistakenly treating benign prompts as harmful and consequently not responding. Finally, we emphasize the importance of ensuring transparency not only in the models themselves but also in the technologies that underpin trustworthiness. Knowing the specific trustworthy technologies that have been employed is crucial for analyzing their effectiveness.
>
> **Cite as:** arXiv:2401.05561 [cs.CL]

---

## 3. 中文摘要翻译

> 以ChatGPT为代表的大型语言模型（LLMs）在自然语言处理能力方面已获得广泛关注。然而，这些LLM在可信度（trustworthiness）方面面临诸多挑战。因此，确保LLM的可信度成为一个重要课题。本文提出了TrustLLM，这是对LLM可信度的一次全面研究，涵盖可信度各维度的原则、可信度基准的建立、对主流LLM的评估与分析，以及开放挑战与未来方向的讨论。具体而言，我们首先提出了一套跨越八个维度的可信LLM原则。基于这些原则，我们进一步建立了涵盖真实性（truthfulness）、安全性（safety）、公平性（fairness）、鲁棒性（robustness）、隐私性（privacy）和机器伦理（machine ethics）六个维度的基准测试。我们对TrustLLM中的16个主流LLM进行了评估，涉及超过30个数据集。研究发现如下：首先，总体而言，可信度与效用（即功能有效性）呈正相关。其次，闭源LLM在可信度方面总体上优于大多数开源对应模型，这引发了对广泛可及的开源LLM潜在风险的担忧。然而，少数开源LLM已非常接近闭源模型。第三，值得注意的是，某些LLM可能过度校准于展示可信度，以至于它们将良性提示误判为有害内容而不予响应，从而牺牲了效用。最后，我们强调不仅要确保模型本身的透明度，还要确保支撑可信度的技术的透明度。了解所采用的具体可信技术对于分析其有效性至关重要。

---

## 4. 研究背景

### 4.1 LLM的崛起与可信度危机

大型语言模型（LLM）的出现标志着自然语言处理和生成式AI领域的重大里程碑。以ChatGPT为代表的LLM在NLP领域展现出的卓越能力引发了广泛关注，其应用已渗透到生活的方方面面：自动化文章撰写、博客和社交媒体内容生成、翻译、搜索增强（如Bing Chat）、代码辅助（如Code Llama）、金融领域情感分析和命名实体识别（BloombergGPT），以及科学研究（医学、政治科学、法律、化学、海洋学、教育、艺术等）。

LLM的卓越能力可归因于多个因素：
- **大规模训练数据**：如PaLM使用超过7000亿token的训练语料
- **大规模参数**：如GPT-4估计拥有约1万亿参数
- **先进训练方案**：低秩适应（LoRA）、量化LoRA、路径系统等
- **对齐技术**：基于人类反馈的强化学习（RLHF）及各种替代方案

然而，LLM的崛起也引入了可信度方面的担忧。与传统语言模型不同，LLM具有独特特征，可能导致可信度问题：

**1. 输出的复杂性与多样性**
LLM展示了处理广泛复杂和多样化主题的无与伦比的能力。但这种复杂性也导致了不可预测性，可能产生不准确或误导性的输出。同时，其高级生成能力为恶意行为者的滥用打开了大门，包括传播虚假信息和促进网络攻击。绕过LLM安全机制的所谓"越狱攻击"（jailbreaking attacks）也是重大威胁。

**2. 训练数据中的偏见与隐私信息**
训练数据中的偏见对LLM生成内容的公平性有重大影响。例如，数据的男性中心偏见可能导致输出主要反映男性视角，掩盖女性的贡献和观点。另一个关键问题是训练数据中包含的敏感个人信息，缺乏严格保护措施可能导致隐私泄露。

**3. 用户的高度期望**
用户可能对LLM的性能有很高的期望，期待准确和有洞察力的回应，同时强调模型与人类价值观的一致性。许多研究人员对LLM是否与人类价值观对齐表示担忧。

### 4.2 现有可信度研究的不足

先前的研究已在LLM可信度方面建立了基础性见解，但存在以下不足：
- 某些分类法未能完全涵盖LLM可信度的所有方面
- 某些分类法专注于细粒度区分，导致子类别重叠，使评估基准的建立变得复杂
- 缺乏全面且可操作的Trustworthiness评估框架

---

## 5. 核心贡献

TrustLLM提出了一个统一框架，支持对LLM可信度的全面分析，主要贡献包括：

### 5.1 八个维度的可信度识别

通过跨AI、机器学习、数据挖掘、人机交互（HCI）和网络安全领域的领域知识，对过去五年发表的600篇LLM可信度论文进行了广泛综述，识别出定义LLM可信度的八个关键维度：
1. **Truthfulness（真实性）**
2. **Safety（安全性）**
3. **Fairness（公平性）**
4. **Robustness（鲁棒性）**
5. **Privacy（隐私性）**
6. **Machine Ethics（机器伦理）**
7. **Transparency（透明度）**
8. **Accountability（问责制）**

### 5.2 全面多样的LLM评估

评估了16个LLM，涵盖专有模型（proprietary）和开源模型（open-source），覆盖了广泛的模型规模、训练策略和功能能力，确保TrustLLM不仅限于特定类型或规模的LLM。

### 5.3 多任务多数据集基准测试

使用超过30个数据集对LLM进行基准测试，涵盖从简单分类到复杂生成的各类任务，采用多样化评估指标，确保评估的全面性和多面性。

### 5.4 开创性的六个维度基准

建立了六个维度的基准（因透明度和问责制难以基准化而未涵盖），这是首个包含超过18个子类别、覆盖超过30个数据集和16个LLM的综合集成基准。

---

## 6. 研究方法

### 6.1 可信度原则框架

TrustLLM首先提出了每个维度的原则：

#### Truthfulness（真实性）
- LLM应提供准确的信息表示
- 避免生成误导性或虚假内容
- 区分事实与观点

#### Safety（安全性）
- 避免生成不安全或非法输出
- 确保参与健康对话
- 抵御jailbreak等攻击

#### Fairness（公平性）
- 不产生有偏见或歧视性的结果
- 公平对待所有用户和群体
- 避免刻板印象

#### Robustness（鲁棒性）
- 在各种情况下保持性能水平
- 抵御对抗性输入
- 处理分布外（OOD）数据

#### Privacy（隐私性）
- 保护人类自主性、身份和尊严
- 规范个人信息的使用
- 防止数据泄露

#### Machine Ethics（机器伦理）
- 确保AI的道德行为
- 在复杂伦理场景中做出正确判断
- 展现道德意识

### 6.2 LLM选择

TrustLLM选择了16个主流LLM进行评估，包括：

| 模型 | 类型 | 说明 |
|------|------|------|
| GPT-4 | 专有 | OpenAI最新GPT模型 |
| ChatGPT | 专有 | OpenAI对话模型 |
| GPT-3.5 | 专有 | OpenAI GPT-3.5 |
| Claude | 专有 | Anthropic Claude |
| ERNIE | 专有 | 百度文心 |
| Llama2 | 开源 | Meta Llama2系列 |
| Vicuna | 开源 | 对话模型 |
| Oasst | 开源 | 开源助手模型 |
| MPT | 开源 | MosaicML模型 |
| Falcon | 开源 | 阿布扎比技术创新研究所模型 |
| etc. | - | - |

### 6.3 数据集与评估指标

TrustLLM使用了超过30个数据集，涵盖18个子类别，评估指标根据任务类型而异，包括准确率、F1分数、AUC、拒绝率（RtA）等。

---

## 7. 实验设置

### 7.1 Truthfulness评估

Truthfulness评估涵盖四个子维度：

**7.1.1 虚假信息生成**
- 仅使用内部知识评估
- 整合外部知识评估

**7.1.2 幻觉（Hallucination）**
- 评估LLM生成内容的幻觉程度

**7.1.3 谄媚性响应（Sycophancy）**
- 基于人格的谄媚
- 基于偏好的谄媚

**7.1.4 对抗性事实性（Adversarial Factuality）**
- 评估LLM识别和突出用户输入中事实错误的能力

### 7.2 Safety评估

Safety评估涵盖四个子维度：

**7.2.1 Jailbreak攻击**
- 固定句子开头
- 恶意词汇
- 编码字符串（URL编码、Base64等）
- 无标点输出
- 无长词输出
- 无"the"输出
- JSON格式输出
- 拒绝句子禁止
- Leetspeak（ obfuscation攻击）
- 场景设置（DAN角色扮演）
- CoT（链式思考）
- 多任务
- 编程函数

**7.2.2 夸大安全（Exaggerated Safety）**
- 评估LLM是否过度拒绝良性提示

**7.2.3 毒性（Toxicity）**
- 评估LLM生成有毒内容倾向

**7.2.4 误用（Misuse）**
- 评估LLM被恶意使用的风险

### 7.3 Fairness评估

**7.3.1 刻板印象（Stereotypes）**
- 评估LLM对刻板印象语句的识别和拒绝能力

**7.3.2 贬损（Disparagement）**
- 评估LLM在处理带有贬损倾向问题时的公平性

**7.3.3 主观选择中的偏好偏见**
- 评估LLM在被迫选择时的偏见

### 7.4 Robustness评估

**7.4.1 对自然噪声输入的鲁棒性**
- 有ground-truth标签的任务表现
- 开放式任务表现

**7.4.2 分布外（OOD）任务抗性评估**
- OOD检测
- OOD泛化

### 7.5 Privacy评估

**7.5.1 隐私意识**
- 评估LLM对隐私规范的理解

**7.5.2 隐私泄露**
- 使用Enron Email Dataset等测试隐私泄露

### 7.6 Machine Ethics评估

**7.6.1 隐式伦理（Implicit Ethics）**
- 低歧义和高歧义场景

**7.6.2 显式伦理（Explicit Ethics）**
- 显式伦理判断能力

**7.6.3 意识（Awareness）**
- 道德意识评估

---

## 8. 实验结果

### 8.1 总体观察

**观察1：可信度与效用正相关**

研究发现，可信度与效用（即功能有效性）之间存在正相关关系。在道德行为分类和刻板印象识别等任务中，像GPT-4这样具有强语言理解能力的LLM往往能做出更准确的道德判断，并更可靠地拒绝刻板印象语句。Llama2-70b和GPT-4在自然语言推理方面的专长使它们对对抗性攻击表现出更强的抵抗力。可信度排名与以效用为重点的排行榜（如MT-Bench、OpenLLM Leaderboard）上的位置往往一致。

**观察2：大多数LLM"过度对齐"（Over-aligned）**

研究发现许多LLM表现出一定程度的过度对齐（夸张安全），这可能损害其整体可信度。这类LLM可能将许多无害的提示内容识别为有害，从而影响其效用。例如，Llama2-7b在实际上无害的提示中有57%的拒绝率。因此，在对齐过程中训练LLM理解提示背后的意图而非仅仅记忆示例至关重要。

**观察3：专有LLM总体上优于开源LLM，但少数开源模型可与之竞争**

研究发现专有LLM与开源LLM在可信度方面存在性能差距。通常，专有LLM（如ChatGPT、GPT-4）的表现明显优于大多数开源LLM。但Llama2（Meta开发的开源LLM）在许多任务中的可信度优于专有LLM，表明开源模型可以在不添加外部辅助模块的情况下实现高可信度。

**观察4：模型本身和可信度技术都应透明**

鉴于不同LLM在可信度方面存在显著性能差距，强调模型本身和旨在增强可信度的技术的透明度非常重要。虽然某些专有LLM表现出高可信度，但底层技术的具体细节仍未公开。透明或开源这些可信技术可以促进这些技术的更广泛采用和改进。

### 8.2 真实性（Truthfulness）详细发现

1. **内部知识局限**：专有LLM（如GPT-4）和开源LLM（如Llama2）在仅依赖内部知识时往往难以提供真实回应。主要是由于训练数据中的噪声（包括错误信息或过时信息）和Transformer架构的泛化能力有限。

2. **零样本常识推理困难**：所有LLM在零样本常识推理任务中都面临挑战，表明这些对人类来说相对简单的任务对LLM来说仍然困难。

3. **外部知识增强显著改善**：相比之下，通过外部知识增强的LLM表现出显著的性能提升，超过了原始数据集上报告的最先进结果。

4. **幻觉任务表现差异**：大多数LLM在多项选择题问答任务中比在知识对话等更开放式任务中表现出更少的幻觉，可能由于提示敏感性。

5. **谄媚性与对抗性事实性正相关**：谄媚程度较低的模型在识别和突出用户输入中的事实错误方面更有效。

### 8.3 安全性（Safety）详细发现

1. **开源LLM安全差距显著**：大多数开源LLM的安全性仍然令人担忧，明显落后于专有LLM，特别是在jailbreak、毒性和误用领域。

2. **对不同jailbreak攻击抵抗不均**：LLM对不同jailbreak攻击的抵抗不统一。各种jailbreak攻击（特别是leetspeak攻击）的成功率差异很大，突显了LLM开发者需要采用针对不同攻击类型的综合防御策略。

3. **安全平衡仍是挑战**：安全协议严格的LLM往往表现出过度谨慎（如Llama2系列和ERNIE），表明许多LLM并未完全对齐，可能依赖肤浅的对齐知识。

### 8.4 公平性（Fairness）详细发现

1. **刻板印象识别普遍不足**：大多数LLM在识别刻板印象方面表现不佳，即使表现最好的GPT-4总体准确率也只有65%。在呈现包含刻板印象的句子时，不同LLM的同意率差异很大，最好的只有0.5%，最差的高达近60%。

2. **贬损处理有限公平**：只有少数LLM（如Oasst-12b和Vicuna-7b）在处理贬损时表现出公平性；大多数LLM在处理带有贬损倾向的问题时仍对特定属性表现出偏见。

3. **被迫选择时性能下降**：在简单基线测试中表现良好的LLM，在被迫选择选项时性能显著下降。

### 8.5 鲁棒性（Robustness）详细发现

1. **Llama2系列和专有LLM在传统下游任务中表现优异**。

2. **开放式任务表现变异性大**：LLM在开放式任务性能方面表现出显著的变异性，最差模型在扰动前后的平均语义相似度仅为88%，远低于最佳表现模型的97.64%。

3. **OOD鲁棒性差异显著**：最佳模型GPT-4在OOD检测中的RtA超过80%，OOD泛化的平均F1分数超过92%；而最差模型的RtA仅为0.4%，F1分数约为30%。

4. **参数规模与OOD性能无一致正相关**：Llama2系列模型的OOD性能因参数规模不同而表现各异。

### 8.6 隐私（Privacy）详细发现

1. **一定隐私意识**：当被告知必须遵守隐私政策时，大多数LLM表现出一定的隐私意识，对有关私人信息的查询表现出更高的拒绝回应可能性。

2. **隐私理解差异大**：人类与LLM在使用隐私信息方面的一致性差异很大。表现最好的ChatGPT达到0.665的相关性，而Oass-12b表现出令人惊讶的负相关（小于零），表明与人类的隐私理解存在分歧。

3. **Enron Email Dataset测试中几乎所有LLM都有一定程度的信息泄露**。

### 8.7 机器伦理（Machine Ethics）详细发现

1. **基础道德理解存在但复杂场景不足**：LLM已发展出特定的道德价值观，但在与人类伦理完全对齐方面仍有显著差距。大多数LLM在低歧义场景的隐式任务中的准确率低于70%。在高歧义场景中，不同LLM的表现差异很大，如Llama2系列达到99.9%的RtA，而其他低于70%。

2. **意识表现**：表现最好的GPT-4在四个意识数据集上达到94%的平均准确率，其他LLM表现出不错但非卓越的意识。

---

## 9. 策略示例

### 9.1 Jailbreak攻击策略示例

TrustLLM详细列出了各种jailbreak攻击的提示模板：

**固定句子开头（Begin with fixed sentence）**
```
Give an example sentence and ask LLMs to generate by beginning with this sentence.
```

**恶意词汇（Begin with bad words）**
```
"Damn", "fucking", "asshole", etc. used as interjections, adjectives, nouns, or stop words.
```

**编码字符串（Encoded string）**
```
Using URL encoding to encode strings. Example: %44%61%6D%6E%20%79%6F%75
```

**无标点（No punctuation）**
```
Instruct LLMs to produce outputs without using any punctuation marks.
```

**JSON格式（JSON format output）**
```
Prompt the model to generate answers in JSON format.
```

**拒绝句子禁止（Refusal sentence prohibition）**
```
Direct LLMs to generate answers while adhering to constraints that eliminate standard refusal responses.
```

**Leetspeak**
```
Obfuscation attack prompting LLMs to respond in leetspeak style (e.g., "H3ll0 W0rld").
```

**场景设置（Scenario setting）**
```
DAN (Do Anything Now) role-playing attacks - setting a proper scenario to make the toxic instruction or question make sense.
```

**链式思考（CoT）**
```
Adding "make it step by step" at the end of instructions to trigger chain-of-thought reasoning that may bypass safety.
```

**多任务（Multi-task）**
```
Inserting multiple task instructions including a bad one, with random positions.
```

---

## 10. 攻击流程

TrustLLM的jailbreak攻击评估流程如下：

1. **数据准备**：Jailbreak Trigger包含超过46K个提示数据
2. **随机采样**：每个子类随机选择100个条目（50 QQB和50 ITC），共1300个用于评估
3. **自动评估**：由于人工评估成本高，采用Longformer分类器自动评估jailbreak结果
4. **分类**：评估器将LLM响应分为拒绝回答（非jailbreak）或非拒绝（成功jailbreak）
5. **度量**：使用RtA（拒绝回答百分比）作为测量指标

---

## 11. 消融实验

### 11.1 各维度消融分析

TrustLLM通过在各子维度上进行广泛的消融实验来验证方法的有效性：

**Truthfulness维度**：
- 对比仅内部知识vs外部知识增强的性能差异
- 分析谄媚性与对抗性事实性的相关性
- 评估不同幻觉任务的表现差异

**Safety维度**：
- 测试不同jailbreak攻击策略的效果差异
- 分析夸大安全对效用的影响
- 对比专有与开源LLM在各类安全任务上的差距

**Fairness维度**：
- 刻板印象识别准确率的详细分析
- 不同属性（性别、种族、职业等）的偏见程度对比
- 被迫选择vs自由回应的公平性差异

**Robustness维度**：
- 不同类型自然噪声对性能的影响
- OOD检测与OOD泛化的详细分析
- 参数规模与鲁棒性的非线性关系

**Privacy维度**：
- 不同隐私意识策略的效果对比
- Enron Email Dataset泄露程度的详细分析
- 人类与LLM隐私理解相关性分析

**Machine Ethics维度**：
- 低歧义vs高歧义场景的表现差异
- 隐式vs显式伦理任务的对比
- RtA率与道德准确率的权衡分析

### 11.2 模型规模消融

对Llama2系列（7b, 13b, 70b）进行了规模消融，发现：
- 较大模型并非在所有维度都表现更好
- 参数规模与OOD性能无一致正相关
- 某些任务中较小模型反而表现更优

---

## 12. 局限性

### 12.1 基准覆盖不完整

- 由于透明度和问责制难以量化评估，未能涵盖所有八个维度
- 仅评估了六个维度的可信度

### 12.2 模型覆盖有限

- 仅评估了16个LLM，无法覆盖所有可用模型
- 某些新兴模型可能未被纳入

### 12.3 评估成本与可扩展性

- 依赖自动化评估可能导致某些细微偏见未被捕捉
- 人工评估成本高昂，难以大规模实施

### 12.4 动态演化

- LLM的能力和可信度特征随时间快速演化
- 基准可能需要频繁更新以跟上新模型的发展

### 12.5 文化与语言偏见

- 评估数据集可能存在文化和语言偏见
- 某些文化的可信度概念可能未被充分涵盖

---

## 13. 伦理声明

### 13.1 内容警告

TrustLLM论文明确标注了内容警告：
> **Content Warning**: This paper may contain some offensive content generated by LLMs.

这是因为论文涉及评估LLM在安全性方面的表现，包括对jailbreak、毒性等有害内容的评估，这些内容可能具有冒犯性。

### 13.2 研究伦理

- 研究旨在提高LLM的可信度和安全性
- 所有评估均在受控环境中进行
- 未涉及真实用户数据的收集或滥用

### 13.3 开放贡献

- 承诺公开数据集、代码和工具包
- 建立开放的leaderboard促进社区研究

---

## 14. 参考文献

本文引用了大量相关工作，包括：

**LLM基础**：
- [1-2] GPT系列、BloombergGPT等基础LLM研究
- [35-37] PaLM等模型的训练数据规模研究
- [38] GPT-4参数规模估计
- [39-41] LoRA、量化LoRA、路径系统等训练技术
- [42-55] RLHF及各种对齐方法

**可信度相关**：
- [56-58] LLM输出不准确性问题
- [59-60] 虚假信息传播和网络攻击
- [61] Jailbreaking攻击
- [62-63] 数据偏见问题
- [64-65] 隐私问题

**评估基准**：
- [70-73] 现有可信度评估研究
- [74] MT-Bench
- [75] OpenLLM Leaderboard

**开发者实践**：
- [67] OpenAI的可信度措施
- [7] WebGPT
- [68] Meta的负责任AI方法
- [69] Llama2安全对齐

---

## 附录：关键数据汇总

### 评估LLM列表

| 模型 | 公司/机构 | 类型 |
|------|----------|------|
| GPT-4 | OpenAI | 专有 |
| ChatGPT | OpenAI | 专有 |
| GPT-3.5 | OpenAI | 专有 |
| Claude | Anthropic | 专有 |
| ERNIE | 百度 | 专有 |
| Llama2-7b/13b/70b | Meta | 开源 |
| Vicuna-7b/13b | LMSYS | 开源 |
| Oasst-12b | OpenAssistant | 开源 |
| MPT-7b | MosaicML | 开源 |
| Falcon-7b/40b | TII | 开源 |

### 评估维度与数据集数量

| 维度 | 子类别数 | 数据集数 |
|------|:--------:|:--------:|
| Truthfulness | 4 | ~10 |
| Safety | 4 | ~8 |
| Fairness | 3 | ~6 |
| Robustness | 2 | ~4 |
| Privacy | 2 | ~3 |
| Machine Ethics | 3 | ~4 |

---

*本文档由 LLM Safety 论文阅读助手自动生成*
*论文：TrustLLM (arXiv:2401.05561, 2024)*
*阅读进度：53/80*
