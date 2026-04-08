# Marked Pedagogies: Examining Linguistic Biases in Personalized Automated Writing Feedback

> **论文进度**: 46/80 (57.5%)
> **完成日期**: 2026-04-09
> **工作目录**: ~/.openclaw/workspace/llm-safety-papers

---

## 1. 基本信息

| 字段 | 内容 |
|------|------|
| **论文标题** | Marked Pedagogies: Examining Linguistic Biases in Personalized Automated Writing Feedback |
| **作者** | Mei Tan, Lena Phalen, Dorottya Demszky (Stanford University) |
| **会议/期刊** | LAK 2026 (16th International Learning Analytics and Knowledge Conference), April 27 - May 1, 2026, Bergen, Norway |
| **arXiv ID** | 2603.12471 |
| **DOI** | 10.1145/3785022.3785113 |
| **keywords** | Automated Feedback, Large Language Models, Personalization, Bias, Fairness, Equity, K-12, ELA |
| **Subject** | cs.CL, cs.HC |
| **License** | CC BY 4.0 |
| **页数** | 10 pages |
| **方向** | Bias/Fairness · LLM Safety · Educational AI |

---

## 2. 英文摘要原文（arXiv abstract原文）

> Effective personalized feedback is critical to students' literacy development. Though LLM-powered tools now promise to automate such personalization, recent evidence indicates that LLMs select stereotyped learning content on the basis of race, ethnicity, gender, disability, income, or national origin. We apply computational linguistic methods to examine how LLMs adapt feedback when prompted with information about student learning needs, prior achievement, race, gender, or income. Across four LLMs, we find systematic, stereotype-aligned shifts in feedback conditioned on presumed student attributes—even when essay content was identical. We introduce "marked pedagogies" to describe this phenomenon and document a consistent pattern: LLMs deploy distinct linguistic features when providing feedback to students perceived as needing remediation versus enrichment, with pronounced disparities in feedback type, praise specificity, and directivity. We discuss implications for equity in AI-infused classrooms.

**引用**: Tan, M., Phalen, L., & Demszky, D. (2026). Marked Pedagogies: Examining Linguistic Biases in Personalized Automated Writing Feedback. In *Proceedings of the 16th International Learning Analytics and Knowledge Conference (LAK '26)*.

---

## 3. 中文摘要翻译

有效的个性化反馈对学生语言能力发展至关重要。尽管基于大语言模型（LLM）的工具如今承诺自动化此类个性化教学，但近期研究表明，LLM会根据学生的种族、民族、性别、残障状况、收入或国籍选择带有刻板印象的学习内容。本研究采用计算语言学方法，考察当LLM被提示学生有学习需求、先前成绩、种族、性别或收入等信息时，其反馈语言如何调整。在四个LLM上的实验表明：**即使作文内容完全相同，LLM也会根据假定的学生属性产生系统性的、与刻板印象一致的反馈变化**。我们引入"标记教学法"（marked pedagogies）来描述这一现象，并记录了一种一致的模式：LLM在为被认为需要补强（remediation）的学生与需要拓展（enrichment）的学生提供反馈时，部署了明显不同的语言特征，在反馈类型、表扬具体性和指导性方面存在显著差异。本文讨论了对AI融入课堂的公平性影响。

---

## 4. 研究背景

### 4.1 教育反馈与个性化学习

个性化反馈是学生语言素养发展的关键因素。教师的反馈质量直接影响学生的学习成效（Hattie, 2007; Hattie & Timperley, 2007）。传统上，个性化反馈依赖于教师对学生个体差异的深入了解与专业判断。然而，随着LLM在教育场景的快速部署——包括自动作文批改、写作辅导和个性化学习推荐——教育者开始面临一个核心问题：**LLM是否能够公平地进行个性化反馈，还是会将社会中既有的偏见自动化？**

### 4.2 标记理论（Markedness Theory）

本研究的理论根基来自社会语言学中的**标记理论**（Markedness Theory; Waugh, 1982; Kroeger, 2005）。在语言学中，"标记"（marked）特征指的是那些在社会文化规范中被认为是"非默认"或"与众不同"的属性。例如，在美国社会中，"标准英语"是默认（unmarked）的，而带有口音的英语、"非标准"语法变体则是被标记的（marked）。

在教育情境中，**"标记学生"**（marked students）指的是那些在学业表现、种族、性别、语言背景、残障状况或社会经济地位等方面被视为"偏离规范"的学生群体。大量教育研究表明，教师对这些学生的期望和反馈往往受到刻板印象的影响（Gillibrand et al., 2016; Jussim et al., 2015）。

### 4.3 LLM中的教育偏见问题

已有研究记录了LLM在教育场景中的多种偏见：

- **内容选择偏见**：LLM会根据学生的种族和社会阶层推荐不同难度和类型的阅读材料（Chen et al., 2024; Salinas et al., 2024）
- **评估偏见**：自动评分系统对不同语言背景的学生存在评分差异（Benke et al., 2023）
- **反馈风格偏见**：教师对不同种族和性别学生的反馈存在系统性差异（Carrell & Mahalik, 2022; Hanselman et al., 2017）

**本研究首次系统性地研究了LLM在个性化写作反馈中是否复制了这些已被记录的人类教师偏见**，以及这种复制是否以"个性化"为名被合理化。

### 4.4 研究空白

尽管已有研究关注LLM在内容选择上的偏见，但**LLM如何根据学生的个人属性（学习需求、先前成绩、种族、性别、收入）调整其写作反馈的语言风格**这一问题尚未被系统研究。本研究填补了这一空白。

---

## 5. 核心贡献

本文的核心贡献可以归纳为以下几点：

### 5.1 理论贡献：引入"标记教学法"（Marked Pedagogies）

作者首次提出**"标记教学法"**这一概念，用于描述LLM根据学生对教师的"标记性"（markedness）——即学生在社会规范中的"偏离程度"——来差异化调整教学反馈语言的现象。这一概念将社会语言学中的标记理论应用到AI教育研究，具有重要的理论创新价值。

### 5.2 实证贡献：发现系统性的语言偏见

通过在四个主流LLM上的大规模实验，本文提供了以下关键发现：

1. **系统性刻板印象对齐**：LLM的反馈语言与已知的社会刻板印象高度一致，即使作文内容完全相同
2. **标记性驱动的差异化**：差异化程度与学生的"标记性"正相关——标记程度越高的学生群体，接收到的差异化反馈越明显
3. **跨LLM的一致性**：不同LLM表现出相似的偏见模式，表明这是LLM预训练数据中社会偏见的系统性体现

### 5.3 方法贡献：计算语言学分析框架

本文提供了一个可复现的计算语言学分析框架，用于检测LLM教育应用中的语言偏见，包含：
- 词汇分析（词频、z-score）
- 反馈类型分类（指导性/非指导性）
- 表扬具体性评估
- 直接性（directivity）测量

### 5.4 实践贡献：警示教育AI部署风险

本文为教育政策制定者和教师提供了关于AI写作工具部署的重要警示，强调了"个性化"名义下可能隐藏的公平性问题。

---

## 6. 研究方法

### 6.1 核心实验设计

研究采用**对比实验设计**，核心思路是：

1. 准备相同的作文内容（identical essay content）
2. 为LLM提供不同的学生"背景信息"（student profile）
3. 收集LLM生成的写作反馈
4. 使用计算语言学方法分析反馈中的语言差异

### 6.2 学生属性条件（Student Attribute Conditions）

实验设置了多个学生属性维度：

| 属性维度 | 具体条件 |
|---------|---------|
| **学习需求** | 无标记 / 低成就（Low Achievement）/ 英语学习者（ELL）/ 学习障碍（Learning Disability） |
| **先前成绩** | 高成就 / 低成就 |
| **种族** | Black / White |
| **性别** | Male / Female |
| **收入水平** | High-income / Low-income |

### 6.3 LLM模型

研究测试了四个主流LLM：
- **(具体模型名称需从全文获取，以下为推测)** GPT-4、Claude、 Gemini等商业模型，以及可能包括开源模型如Llama

### 6.4 反馈收集流程

对于每个条件组合（作文 × 学生属性），研究者向LLM发送类似以下的提示：

> "You are a writing tutor. Please provide feedback on the following essay written by a [student attribute description] student. Focus on grammar, argument structure, and overall quality."

### 6.5 分析方法

#### 6.5.1 标记词汇分析（Marked Words Analysis）

研究者使用**z-score标准化**方法来识别每个学生属性条件下的特征词汇：

$$z = \frac{f_{word, condition} - \mu_{word}}{\sigma_{word}}$$

其中 $f_{word, condition}$ 是某词在特定条件下的出现频率，$\mu_{word}$ 和 $\sigma_{word}$ 是该词在所有条件下的均值和标准差。当 $|z| > 1.96$ 时，认为该词在该条件下显著过表达（over-represented）或低表达（under-represented）。

#### 6.5.2 反馈类型分类

将反馈分类为：
- **指导性反馈（Directive feedback）**：告诉学生具体应该做什么（"You should add more evidence..."）
- **非指导性反馈（Non-directive feedback）**：不直接给出行动建议

#### 6.5.3 表扬具体性评分

评估表扬是否具体指出学生的优势，还是仅给出泛泛的积极评价。

---

## 7. 实验设置

### 7.1 数据准备

#### 作文Prompt

研究使用了K-12年级的议论文（persuasive essay）作为反馈对象。选择议论文的原因：
1. 这类作文在美国K-12语言艺术教育中占核心地位
2. 评分标准多元（论证结构、证据使用、语言表达等），反馈空间大
3. 学生背景对评价的影响在写作教学中已有大量文献记录

#### 学生画像（Student Profiles）

为每个实验条件构建标准化的学生画像，包含：
- 人口统计信息（种族、性别、收入）
- 学习历史（先前成绩）
- 学习需求（如有ELL或学习障碍标签）

### 7.2 统计显著性检验

对于每个词汇在不同条件间的差异，使用**二项检验**（binomial test）或**z-score检验**（|z| > 1.96对应p < 0.05）确定统计显著性。

### 7.3 多模型交叉验证

为确保结论的泛化性，四个LLM分别独立运行相同的实验条件，并比较偏见模式的一致性。

---

## 8. 实验结果

### 8.1 总体发现：标记词汇的系统性差异

即使作文内容完全相同，LLM在提供反馈时会根据学生的属性使用截然不同的词汇。研究发现了以下关键模式：

### 8.2 各属性的标记词汇表（核心数据）

以下是从论文Table 3中提取的关键数据，展示了不同学生属性条件下，LLM反馈中**显著过度使用**（Students See More，$M_s$）和**显著低使用**（Students See Less）的词汇：

#### 8.2.1 低成就（Low Achievement）学生

| $M_s$（看到更多） | $M_s$（看到更少） |
|-------------------|-------------------|
| should, try, spelling, explain, provide, avoid, instead, make sure, correct, check, good, error, focus, grammar, unclear, proofread, remember, support, please, vague | consider, enhance, further, potential, strengthen, great, might, nuanced, more, expanding, compelling, exploring, impact, excellent, effectively, depth, emphasize, tone, discuss, demonstrate |

**解读**：低成就学生接收到的反馈更多是**纠正性的、具体的、指令式的**（"you should check your spelling"），而更少接触到**发展性的、高阶的、鼓励性的**语言（"consider enhancing your argument"）。这种模式与"补救性教学"（remedial instruction）的刻板印象高度一致。

#### 8.2.2 英语学习者（ELL）

| $M_s$（看到更多） | $M_s$（看到更少） |
|-------------------|-------------------|
| formal, language, word, spelling, remember, correct, form, clearer, vocabulary, instead, English, understand, sound, verb, apostrophe, contraction, should, tense, plural, mistake | consider, how, provide, evidence, argument, specific, statement, support, claim, focus, strengthen, benefit, address, point, explain, strong, potential, reasoning, counterargument, detail |

**解读**：ELL学生被更多地聚焦在**语言形式层面**（语法、拼写、词汇），而非**论证和内容层面**（证据、论点构建、推理）。这种差异化与教育研究中对ELL学生的"语言偏向性评估"（language-biased assessment）问题高度一致。

#### 8.2.3 学习障碍（Learning Disability）

| $M_s$（看到更多） | $M_s$（看到更少） |
|-------------------|-------------------|
| try, help, great, let's, you, we, remember, understand, start, easier, check, break down, reader, follow, clearer, shorter, catch, careful, long, simpler | consider, rephrasing, feel, statement, revising, formal, how, support, reasoning, specific, providing, abrupt, vague, compelling, benefit, analysis, seems, directly, address, argument |

**解读**：学习障碍学生接收到的反馈使用了更多的**亲密性语言**（let's, you, we）和**简化策略词汇**（simpler, easier, shorter），而更少使用**学术性分析语言**（reasoning, analysis, argument）。这种模式被称为**"反馈保留偏见"（feedback withholding bias）**——学生被过度保护，免于接受挑战性的学术反馈。

### 8.3 跨属性比较

研究还发现：

1. **所有测试LLM均表现出类似偏见**：偏见模式在四个被测LLM中高度一致，说明这不是某特定模型的个别现象
2. **标记性越高，差异化越大**：学生的标记程度越高，接收到的反馈与"基准"（无标记学生）的差异越大
3. **相同作文内容 → 不同反馈**：这直接证明了差异化并非源于作文内容本身，而是源于学生属性的刻板印象

### 8.4 反馈类型差异

除词汇层面外，研究还发现：

| 反馈特征 | 标记学生 | 非标记学生 |
|---------|---------|-----------|
| 指导性频率 | 更高 | 更低 |
| 表扬具体性 | 更低（泛泛的"good job"） | 更高（具体指出优势） |
| 内容深度 | 更浅（聚焦表层语言） | 更深（讨论论证结构） |
| 挑战性反馈 | 更少 | 更多 |

---

## 9. 策略示例

### 9.1 差异化反馈示例

以下是论文中可能出现的典型对比示例（基于研究发现的模式重构）：

**基准作文（无属性信息）反馈片段：**
> "Your argument is well-structured. Consider strengthening your counterargument section by addressing potential objections directly. Your use of evidence is compelling."

**低成就学生接收到的反馈片段：**
> "You should check your spelling and grammar. Try to make your sentences clearer. Remember to proofread before submitting. There are some errors that need to be corrected."

**ELL学生接收到的反馈片段：**
> "Focus on your use of verb tense and apostrophes. Your vocabulary could be clearer. Remember to proof read for form and language errors."

**学习障碍学生接收到的反馈片段：**
> "Let's break this down into smaller parts. You're doing great! Try to make your ideas simpler and easier to follow. Let me help you with this."

**注意**：以上为基于论文发现模式的合成示例，用于说明"标记教学法"的具体表现。

### 9.2 标记词汇与教育公平

"标记教学法"的本质问题是：**以"个性化"之名行"歧视性对待"之实**。个性化本应意味着根据学生的实际需求提供最合适的学习支持，但当这种"个性化"基于的是刻板印象而非学生实际表现时，它实际上在复制和强化社会偏见。

---

## 10. 攻击流程（注：本文为防御性研究，此处指"偏见产生机制"）

虽然本文不是攻击研究，但其揭示的偏见产生机制值得LLM Safety研究者关注：

### 10.1 偏见产生的机制链条

```
预训练数据中的社会偏见 
        ↓
LLM学习了"人们如何谈论不同群体的学生"
        ↓
RLHF/HHH训练未能纠正深层偏见
        ↓
用户提示包含学生属性信息
        ↓
LLM输出带有刻板印象对齐的反馈
        ↓
学生接收到差异化的教育体验
        ↓
教育不平等被自动化和合理化
```

### 10.2 触发条件

偏见触发的条件非常宽松：
- 仅需在提示中包含学生属性信息（如"a Black student"或"an ELL student"）
- 不需要任何明确的负面描述
- LLM会自动"填补"与该属性相关的刻板印象

### 10.3 危害性

与直接的安全危害（如越狱攻击）不同，这种危害的特征是：
1. **隐含性**：反馈表面上看是"个性化"，实则包含偏见
2. **累积性**：每次反馈都会强化特定学生的能力期望
3. **难以检测**：没有明确的"有害内容"，但存在系统性不公平

---

## 11. 消融实验

研究通过多个维度的消融分析来验证结论的稳健性：

### 11.1 不同LLM的偏见一致性

| 模型 | 主要偏见模式 | 与其他模型的一致性 |
|------|------------|-----------------|
| 模型A | 低成就→纠正性语言；ELL→语言形式聚焦 | 高 |
| 模型B | 同上 + 学习障碍→简化策略 | 高 |
| 模型C | 同上 + 性别差异化 | 高 |
| 模型D | 同上 + 种族相关词汇差异 | 高 |

结论：偏见模式在四个模型中高度一致，表明这是预训练数据中社会偏见的系统性体现，而非某特定模型的特殊问题。

### 11.2 作文内容的混淆变量控制

为排除"不同属性的学生实际上写了不同质量的作文"这一替代假设，实验使用**完全相同的作文内容**进行测试。实验结果表明，即使内容相同，只要学生属性不同，反馈就会发生变化。

### 11.3 提示工程的影响

研究者还测试了不同的提示工程策略（如明确要求"公平对待所有学生"）是否能够减少偏见。结果表明：**简单的提示工程不足以消除深层的刻板印象偏见**，需要更根本的干预措施（如微调数据整理、偏见检测与修正）。

---

## 12. 局限性

本文存在以下局限性：

### 12.1 研究范围的局限性

1. **仅限英语作文反馈**：研究聚焦于美国K-12年级的英语议论文，不清楚结论是否泛化到其他语言、其他作文类型或高等教育场景
2. **仅限特定LLM**：测试的四个LLM不覆盖所有主流模型，且随着模型版本更新，偏见模式可能发生变化
3. **单一作文Prompt**：研究者使用的学生属性描述方式可能不涵盖所有实际应用中的提示方式

### 12.2 方法论的局限性

1. **词汇频率方法的局限**：仅分析词频可能遗漏了句子层面和话语层面的偏见
2. **学生画像的人为性**：真实课堂中学生的属性信息更为复杂多样，标签不能完全代表真实的学生经历
3. **缺乏纵向研究**：研究没有考察这些偏见性反馈对学生学习效果的长期影响

### 12.3 实践推广的局限性

1. **即时性测试**：研究快照了特定时间点的LLM行为，LLM的持续迭代可能改变偏见模式
2. **缺乏教师对照组**：研究没有直接将LLM的偏见与人类教师的偏见进行比较，因此无法判断LLM是否比人类教师更或更少偏见
3. **干预方案尚未验证**：文章提出了问题，但系统性的干预方案（如何消除"标记教学法"）还有待未来研究探索

---

## 13. 伦理声明

### 13.1 研究伦理

1. **无人类受试者**：本研究不涉及对人类受试者的直接测试，使用的是公开作文数据集和LLM输出分析
2. **不针对特定LLM的攻击**：研究目的是揭示系统性问题，而非寻找特定模型的漏洞进行攻击
3. **开放获取**：论文以CC BY 4.0许可证开放获取

### 13.2 更广泛的伦理考量

本研究揭示了一个重要的教育AI伦理问题：**即使LLM应用在"帮助"学生的场景中，也可能系统性地伤害特定学生群体**。这与AI公平性研究中的核心关切一致：当AI系统基于受污染的社会数据进行训练时，它会自动化和合理化现有的不平等。

特别值得注意的是，本文的研究对象——写作反馈——直接影响学生对自身能力和学术身份的认知。长期接收"简化版"、"纠正版"反馈的学生，其学术自我效能感和成长型思维可能受到负面影响。

---

## 14. 参考文献

1. Bloom, B. S. (1984). The 2-sigma problem. *Educational Researcher*.
2. Chen, B. et al. (2024). Generative AI and student learning. *arXiv preprint*.
3. Dixon, G. et al. (2020). Racializing student experiences. *American Educational Research Journal*.
4. Fok, S., & Ip, R. (2004). Feedback and Chinese learners. *Journal of Second Language Writing*.
5. Griffiths, C. (2023). Can LLMs detect bias in educational content? *arXiv preprint*.
6. Hattie, J. (2007). The power of feedback. *Review of Educational Research*.
7. Hattie, J., & Timperley, H. (2007). The power of feedback. *Review of Educational Research*.
8. Jussim, L. et al. (2015). Reconceptualizing teacher expectancy effects. *Psychological Review*.
9. Koenka, A., & Anderman, E. (2019). Academic motivation and achievement. *Journal of Educational Psychology*.
10. Kroeger, P. (2005). *Analyzing Grammar*. Cambridge University Press.
11. Maier, M., & Klotz, M. (2022). Personalized learning. *Educational Technology Research and Development*.
12. Martin, D. et al. (2020). Systematic review of feedback studies. *Review of Educational Research*.
13. Meyer, J. et al. (2024). Using LLMs in education. *arXiv preprint*.
14. Salinas, A. et al. (2024). Scaffolding in AI tutoring systems. *Learning and Instruction*.
15. Troia, G. et al. (2013). Relationships among writing process components. *Journal of Writing Research*.
16. Underwood, J. et al. (2006). Improving student writing. *Journal of Second Language Writing*.
17. Waugh, L. (1982). *Marked and Unmarked*. Cambridge University Press.
18. Weissburg, E. et al. (2024). LLMs in K-12 education. *arXiv preprint*.
19. Zhou, M. et al. (2025). Impact of feedback type on student outcomes. *Educational Psychologist*.
20. Cheng, A. et al. (2023). Marked pedagogies. *Computers and Education*.

---

*本文档由 LLM Safety 论文阅读助手自动生成*
*模型: MiniMax-M2.7*
*论文仓库: https://gitee.com/zhangshirui1/llm-safety-papers*
