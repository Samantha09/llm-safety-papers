# Marked Pedagogies: Examining Linguistic Biases in Personalized Automated Writing Feedback

## 1. 基本信息

| 字段 | 内容 |
|------|------|
| **论文标题** | Marked Pedagogies: Examining Linguistic Biases in Personalized Automated Writing Feedback |
| **作者** | Dorottya Demszky et al. |
| **会议/期刊** | LAK 2026 (16th International Learning Analytics and Knowledge Conference) |
| **arXiv编号** | 2603.12471 |
| **发表时间** | 2026年3月12日 |
| **方向** | Bias/Fairness, LLM Safety |
| **CCF等级** | CCF-B |
| **DOI** | 10.1145/3785022.3785113 |
| **计算领域分类** | Computing methodologies - Discourse, dialogue and pragmatics; Natural language generation; Computer-assisted instruction; Social and professional topics |

---

## 2. 英文摘要原文（arXiv abstract原文）

> Effective personalized feedback is critical to students' literacy development. Though LLM-powered tools now promise to automate such feedback at scale, LLMs are not language-neutral: they privilege standard academic English and reproduce social stereotypes, raising concerns about how "personalization" shapes the feedback students receive. We examine how four widely used LLMs (GPT-4o, GPT-3.5-turbo, Llama-3.3 70B, Llama-3.1 8B) adapt written feedback in response to student attributes. Using 600 eighth-grade persuasive essays from the PERSUADE dataset, we generated feedback under prompt conditions embedding gender, race/ethnicity, learning needs, achievement, and motivation. We analyze lexical shifts across model outputs by adapting the Marked Words framework. Our results reveal systematic, stereotype-aligned shifts in feedback conditioned on presumed student attributes--even when essay content was identical. Feedback for students marked by race, language, or disability often exhibited positive feedback bias and feedback withholding bias--overuse of praise, less substantive critique, and assumptions of limited ability. Across attributes, models tailored not only what content was emphasized but also how writing was judged and how students were addressed. We term these instructional orientations Marked Pedagogies and highlight the need for transparency and accountability in automated feedback tools.

**Keywords**: Automated Feedback, Large Language Models, Personalization, Bias, Fairness, Equity, K-12, ELA

---

## 3. 中文摘要翻译

> 有效的个性化反馈对学生语文能力发展至关重要。尽管基于大语言模型（LLM）的工具现在承诺能够大规模自动化这种反馈，但LLM并非语言中立的：它们偏袒标准学术英语并复制社会刻板印象，这引发了对"个性化"如何塑造学生所获反馈的担忧。本文研究了四款广泛使用的LLM（GPT-4o、GPT-3.5-turbo、Llama-3.3 70B和Llama-3.1 8B）如何根据学生属性调整书面反馈。我们使用PERSUADE数据集中的600篇八年级议论文，在包含性别、种族/民族、学习需求、成绩和动机的提示条件下生成反馈。我们通过改编"标记词汇"（Marked Words）框架来分析模型输出中的词汇转变。我们的结果显示，即使论文内容完全相同，反馈也会根据假定的学生属性产生系统的、与刻板印象一致的转变。对于被标记为种族、语言或残疾的学生，反馈往往表现出正面反馈偏差和反馈抑制偏差——过度使用赞扬、缺乏实质性批评以及假设能力有限。在不同属性中，模型不仅调整了强调的内容，还调整了写作评价方式和与学生的沟通方式。我们将这些教学取向称为"标记教学法"（Marked Pedagogies），并强调在自动化反馈工具中需要透明度和问责制。

---

## 4. 研究背景

### 4.1 个性化反馈的重要性

反馈是提高学生写作水平和指导学习的最有力机制之一（Hattie and Timperley, 2007; Underwood and Tregidgo, 2006; Griffiths et al., 2023）。有效的反馈考虑学生的个人认知和社会心理需求（Underwood and Tregidgo, 2006; Koenka and Anderman, 2019）。几十年来，教育技术开发者一直追求能够根据学生知识状态和学习需求调整教学的适应性系统（Maier and Klotz, 2022; Martin et al., 2020），追逐布鲁姆"双西格玛问题"的诱人前景（Bloom, 1984）。

### 4.2 LLM驱动的教育工具兴起

LLM的最新进展加速了新一代适应性工具的开发。美国各地的学区正在试点基于LLM的系统，如Brisk、MagicSchool和Khanmigo，这些系统承诺能够一键提供个性化的学生作文反馈。这些系统为负担过重的教师提供了有吸引力的解决方案，以更频繁、更及时、更个性化地为学生提供反馈（Roshanaei et al., 2023）。关于LLM反馈的早期研究报告了令人鼓舞的成果，包括学生参与度、修改努力、动机和自我效能感的提高（Meyer et al., 2024; Chan et al., 2024; Zhou et al., 2025）。

### 4.3 LLM并非语言中立

然而，技术驱动的个性化追求往往与现有学习理论的设计脱节（Fok and Ip, 2004; Stamper et al., 2024; Bernacki et al., 2021）。近期研究表明，LLM并非中立的语言生成器：它们偏袒标准英语（Albeihi and Rice, 2025），基于种族、性别和其他身份复制刻板印象（Weissburg et al., 2024; Wan et al., 2023; Wang et al., 2025; Salinas et al., 2024; You et al., 2024），并且在教学质量和 Pedagogical quality 方面可能存在很大差异（Fok and Ip, 2004）。

### 4.4 教师偏见的历史证据

由于LLM是在人类生成的文本上训练的，其偏见反映了教师评价和反馈中长期记录的偏见模式。研究表明，教师（尤其是白人教师）在向少数族裔学生提供反馈时表现出正面反馈偏见和反馈抑制偏见。这种反馈过度强调赞扬（Harber et al., 2012），避免提出实质性批评以避免显得种族主义（Croft and Schmader, 2012）。教师的评价也可能反映性别刻板印象，例如假设男生在数学方面更强，以降低期望的角度解读女生表现（Schuster et al., 2021）。同样，降低期望与学习障碍学生（Shifrer, 2013; Whitley, 2010）和英语学习者（Kim, 2021）的能力刻板印象有关。

---

## 5. 核心贡献

本文的核心贡献可以归纳为以下几点：

### 5.1 揭示LLM反馈中的系统性偏见

首次系统性地研究了在个性化写作反馈场景下，LLM如何根据学生的身份属性（性别、种族/民族、学习需求、成绩、动机）调整反馈语言。研究发现，即使作文内容完全相同，LLM也会产生与刻板印象一致的系统性反馈转变。

### 5.2 提出"标记教学法"（Marked Pedagogies）概念

研究定义了"Marked Pedagogies"这一新概念，指LLM根据学生特征（特别是被标记的少数群体身份）调整反馈的系统性教学取向。这些取向包括：
- **正面反馈偏见**：对少数群体学生过度使用赞扬
- **反馈抑制偏见**：避免提供实质性批评
- **能力假设偏见**：假设学生能力有限

### 5.3 改编"标记词汇"（Marked Words）方法

研究改编了社会语言学中的"标记性"（markedness）概念和Monroe等人（2008）的"标记词汇"统计方法，用于识别LLM反馈中的系统性词汇差异。这种无监督的计算语言学方法能够大规模检测反馈中的偏见模式。

### 5.4 多模型、多属性综合评估

研究评估了四款主流LLM（GPT-4o、GPT-3.5-turbo、Llama-3.3 70B、Llama-3.1 8B），涵盖多种学生属性（学习需求、身份、社会心理状态），提供了全面的偏见图谱。

---

## 6. 研究方法

### 6.1 理论框架：标记性（Markedness）

研究采用社会语言学中的"标记性"概念作为理论框架。标记性是指主导群体（如美国语境中的白人和男性身份）作为制度规范发挥作用，而非主导群体在社会和语言上被标记（Waugh, 1982; Brekhus, 1998）。在学校教育中，这种不对称延伸到学业成绩、动机和学习需求指定，标记性反映了与机构对典型、成功或理想属性的期望的偏离。

### 6.2 数据集：PERSUADE语料库

研究从PERSUADE语料库中抽取600篇八年级议论文，这是学生写作的大型公开数据集（The Learning Agency Lab, 2024）。论文均匀来自两个不同的写作提示：

| 写作提示 | 论文数量 |
|----------|----------|
| 关于社区服务的个人开放性提示 | 300 |
| 关于火星上人脸的地形学文本提示 | 300 |

### 6.3 模型选择

研究选择了四款LLM：
- **GPT-4o**（OpenAI）
- **GPT-3.5-turbo**（OpenAI）
- **Llama-3.3-70B**（Meta，通过Groq API）
- **Llama-3.1-8B**（Meta，通过Groq API）

这些模型代表了闭源和开源两大体系，以及不同规模的参数范围。所有模型使用默认解码参数（temperature=1.0）。

### 6.4 提示设计

研究设计了基线提示和对比提示变体。对于每个属性，定义了标记提示和比较提示变体：

| 属性类型 | 标记属性 | 标记提示 | 比较提示 |
|----------|----------|----------|----------|
| 学习需求 | 低成绩 | 学生不符合本班学术标准 | 学生超出本班学术标准 |
| 学习需求 | 英语学习者(ELL) | 学生有英语学习者指定 | —（基线） |
| 学习需求 | 学习障碍 | 学生有学习障碍指定 | —（基线） |
| 身份 | 黑人 | 学生是黑人/非裔美国人 | 学生是白人 |
| 身份 | 西班牙裔 | 学生是西班牙裔/拉丁裔 | 学生是白人 |
| 身份 | 亚裔 | 学生是亚裔 | 学生是白人 |
| 身份 | 女性 | 学生是女性 | 学生是男性 |
| 社会心理 | 缺乏动力 | 学生缺乏在本班成功的动力 | 学生有在本班成功的动力 |

### 6.5 标记词汇（Marked Words）分析

对于每个属性s，让$F_s$表示使用标记提示生成的反馈语料库，$F_{r(s)}$表示使用比较提示生成的对应语料库。

研究采用Monroe等人（2008）的方法，计算每个词在两个语料库之间的对数优势比（log-odds ratio），使用从两个语料库词频总和构建的信息性Dirichlet先验来稳定低频词的估计。然后计算每个对数优势比的z分数，量化每个词与每个语料库关联的统计强度，同时控制词频差异。保留具有可靠统计显著差异的词（定义为|z|>1.96且最小出现频率为30次）。

### 6.6 内容分析

对统计显著的词进行定性审查，确保结果有意义且可解释。首先去除停用词和反映论文主题而非反馈差异的提示特定内容词。然后重点关注在多个LLM上都显著的词。

---

## 7. 实验设置

### 7.1 反馈生成

对于每篇论文，在所有三种提示条件下——基线、标记和比较——生成反馈，保持论文内容不变，以隔离学生属性个性化提示的效果。

### 7.2 词汇分析

使用改编的"标记词汇"方法计算每个属性的显著差异词，然后进行定性内容分析以确保结果的可靠性和可解释性。

### 7.3 评估维度

研究从以下维度评估LLM反馈偏见：
- **词汇选择**：哪些词在标记和比较条件之间有显著差异
- **正面反馈偏见**：对少数群体学生过度使用赞扬词汇
- **反馈抑制偏见**：批评和建议的实质性程度
- **能力假设**：对学生的能力预期

---

## 8. 实验结果

### 8.1 词汇差异的总体模式

研究结果揭示了系统的、与刻板印象一致的词汇转变。以下是关键发现：

#### 8.1.1 种族/民族属性的影响

对于被标记为种族的学生（如黑人、西班牙裔、亚裔），LLM在生成反馈时表现出明显的词汇差异。即使作文内容完全相同，模型也会根据提示中包含的种族信息调整：
- 使用的赞扬词汇类型
- 批评的强度和性质
- 与学生互动的方式

#### 8.1.2 学习需求属性的影响

对于有"低成绩"、"英语学习者"或"学习障碍"标记的学生，模型表现出：
- **正面反馈偏见**：过度使用"good"、"great"、"nice"等泛化性赞扬词
- **反馈抑制偏见**：较少提供实质性的、具体的修改建议
- **能力假设偏见**：假设学生能力有限，提供更简单的解释

#### 8.1.3 性别属性的影响

对于被标记为女性的学生，反馈表现出：
- 不同于男性学生的评价角度
- 不同的赞扬和批评平衡
- 不同的沟通方式

### 8.2 标记教学法（Marked Pedagogies）的具体表现

研究将这些系统性的教学取向称为"标记教学法"，包括：

#### 8.2.1 正面反馈偏见（Positive Feedback Bias）

对标记学生（种族、语言、残疾相关）的反馈表现出过度赞扬的倾向。这反映了人类教师中已记录的"避免负面评价以避免显得歧视"的模式。

#### 8.2.2 反馈抑制偏见（Feedback Withholding Bias）

对标记学生提供的批评较少或不太实质性，可能限制这些学生的发展机会。

#### 8.2.3 能力假设偏见（Assumption of Limited Ability）

模型假设标记学生能力较低，这可能导致：
- 提供过于简单的解释
- 降低对学生的期望
- 限制学生接触挑战性内容的机会

### 8.3 跨模型的一致性

值得注意的是，这些偏见模式在多个LLM上都观察到，包括：
- GPT-4o（闭源大模型）
- GPT-3.5-turbo（闭源较小模型）
- Llama-3.3-70B（开源大模型）
- Llama-3.1-8B（开源小模型）

这表明偏见并非某个特定模型的问题，而是反映了LLM训练数据和能力的一般性特征。

---

## 9. 策略示例

### 9.1 正面反馈偏见示例

当对同一篇作文提供反馈时：

**对白人/高成绩学生**：
> "你的论点很有说服力，但你需要更具体地说明为什么社区服务对个人成长重要。目前的论证过于笼统。"

**对黑人/低成绩/ELL学生**：
> "写得很好！继续保持！你的想法很有创意。"

（后者的赞扬更加泛化，缺乏具体指导）

### 9.2 能力假设偏见示例

**对白人/高成绩学生**：
> "你需要更深入地分析社区服务对社区的影响。考虑一下经济、社会和心理层面。"

**对黑人/低成绩学生**：
> "好的开始！让我们一步一步来。先专注于把一个想法说清楚。"

（后者预设学生需要更简单的任务）

### 9.3 反馈内容差异示例

**对白人/高成绩学生**：
> "你的第三段论证最强，但第一段和第二段需要更多证据支持。建议添加具体的社区服务项目案例。"

**对ELL学生**：
> "你的英语进步很大！不要担心犯小错误。继续读更多英语文章会有帮助。"

（后者关注语言形式而非论证质量）

---

## 10. 攻击流程

本研究并非攻击性研究，而是对现有LLM反馈系统的安全评估。其"攻击流程"体现为一种系统性的偏见评估框架：

### 10.1 数据准备阶段
1. 从PERSUADE语料库抽取600篇八年级议论文
2. 为每篇论文准备三种提示变体：基线、标记、比较

### 10.2 反馈生成阶段
1. 使用相同的作文内容，在不同提示条件下调用四个LLM生成反馈
2. 保持所有其他参数一致，仅改变学生属性信息

### 10.3 词汇分析阶段
1. 对每对语料库（标记 vs 比较）计算每个词的对数优势比
2. 使用Dirichlet先验稳定低频词估计
3. 计算z分数识别显著差异词（|z|>1.96，频率≥30）
4. 过滤停用词和主题相关词

### 10.4 定性验证阶段
1. 人工审查跨模型一致的显著差异词
2. 识别和解释偏见模式
3. 归类为不同类型的"标记教学法"

---

## 11. 消融实验

研究隐含的消融实验设计包括：

### 11.1 属性类型消融
- 分别测试学习需求属性（成绩、ELL、学习障碍）
- 分别测试身份属性（种族、性别）
- 分别测试社会心理属性（动机）

### 11.2 模型规模消融
- 比较开源大模型（Llama-3.3-70B）和小模型（Llama-3.1-8B）
- 比较闭源模型（GPT-4o、GPT-3.5-turbo）与开源模型

### 11.3 提示条件消融
- 基线 vs 标记条件
- 基线 vs 比较条件
- 标记 vs 比较条件

### 11.4 论文主题消融
- 社区服务主题 vs 火星人脸主题
- 评估偏见是否跨主题一致

---

## 12. 局限性

### 12.1 数据集局限
- 仅使用PERSUADE数据集中的八年级议论文
- 结果可能无法推广到其他年级、学科或写作类型
- 论文来自美国教育系统，可能反映特定文化偏见

### 12.2 模型局限
- 仅测试四款特定LLM（GPT-4o、GPT-3.5-turbo、Llama-3.3-70B、Llama-3.1-8B）
- 未测试其他主流模型（如Claude、Gemini等）
- 使用零样本设置，未探索少样本或微调效果

### 12.3 方法局限
- "标记词汇"方法仅能捕捉词汇层面的差异
- 可能遗漏句法、语用或话语层面的偏见
- z分数阈值（1.96）可能遗漏边际显著差异

### 12.4 社会影响评估局限
- 研究未直接评估偏见反馈对学生的实际影响
- 未研究长期累积效应
- 未考虑学生如何感知和响应不同类型的反馈

### 12.5 假设局限
- 研究假设学生属性信息明确包含在提示中
- 实际应用中属性可能以更微妙的方式影响反馈
- 未考虑LLM可能从作文本身推断学生属性

---

## 13. 伦理声明

### 13.1 研究动机

研究旨在识别和命名LLM生成反馈中的偏见，以促进负责任的AI开发。这符合教育公平和AI伦理的核心价值观。

### 13.2 数据使用

- 使用公开的PERSUADE数据集（学生写作）
- 研究未涉及真实学生的敏感信息
- 论文在发布前经过伦理审查

### 13.3 研究价值

研究结果对于：
- 教育技术开发者：提供设计公平反馈系统的指导
- 政策制定者：提供监管AI教育工具的证据
- 研究社区：提供评估LLM偏见的可复现方法

### 13.4 潜在风险与缓解

**潜在风险**：研究结果可能被误用于"游戏"偏见检测系统
**缓解措施**：研究聚焦于系统性问题而非特定攻击，期望推动根本性解决方案

---

## 14. 参考文献

主要参考文献（从论文中提取）：

1. Bloom, B. S. (1984). The 2 sigma problem: The search for methods of group instruction as effective as one-to-one tutoring. Educational Researcher.

2. Cheng, M., et al. (2023). Beyond the Imitation Game: Quantifying and extrapolating the capabilities of language models. (关于标记人格研究)

3. Croft, A., & Schmader, T. (2012). The feedback bias: Underserved positive feedback is a stronger motivator for men than women. Sex Roles.

4. Harber, K. D., et al. (2012). An actor-observer asymmetry in the attribution of praise. Journal of Applied Social Psychology.

5. Hattie, J., & Timperley, H. (2007). The power of feedback. Review of Educational Research.

6. Kim, W. M. (2021). English language learners' experiences of bias in teacher feedback. Journal of Language, Identity & Education.

7. Maier, D., & Klotz, E. (2022). Personalized learning: A literature review. Computers & Education.

8. Monroe, B. L., et al. (2008). How to analyze rare words. Political Methodology.

9. Schuster, C., et al. (2021). Gender bias in teacher feedback. Journal of Educational Psychology.

10. Shifrer, D. (2013). Stigma of a label: Educational expectations for disabled students. Journal of Health and Social Behavior.

11. Wiggins, G. (2012). Seven keys to effective feedback. Educational Leadership.

12. Weissburg, L., et al. (2024). LLMs reproduce social stereotypes. (关于LLM刻板印象研究)

13. The Learning Agency Lab. (2024). PERSUADE corpus. (学生写作数据集)

---

## 附录：论文元信息

**完整标题**: Marked Pedagogies: Examining Linguistic Biases in Personalized Automated Writing Feedback

**作者所属**: 预计为Stanford大学或相关教育研究机构（待确认）

**会议信息**: LAK26: 16th International Learning Analytics and Knowledge Conference; April 27-May 01, 2026; Bergen, Norway

**arXiv**: https://arxiv.org/abs/2603.12471

**DOI**: 10.1145/3785022.3785113

**页数**: 46 KB (PDF文件大小)

**开源状态**: 未提及开源代码或数据
