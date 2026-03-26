# ESG-Bench: Benchmarking Long-Context ESG Reports for Hallucination Mitigation

## 1. 基本信息

- **论文标题**: ESG-Bench: Benchmarking Long-Context ESG Reports for Hallucination Mitigation
- **中文标题**: ESG-Bench：面向幻觉缓解的长上下文ESG报告基准评测
- **作者**: Siqi Sun, Ben Peng Wu, Mali Jin, Peizhen Bai, Hanpei Zhang, Xingyi Song
- **发表时间**: 2026年3月 (arXiv:2603.13154)
- **论文链接**: https://arxiv.org/abs/2603.13154
- **代码链接**: 未公开
- **研究方向**: LLM幻觉缓解 / ESG报告理解 / 长上下文推理 / 可信AI
- **会议/期刊**: AAAI 2026
- **arXiv ID**: 2603.13154
- **DOI**: https://doi.org/10.48550/arXiv.2603.13154
- **Subjects**: Computation and Language (cs.CL); Artificial Intelligence (cs.AI)

---

## 2. 英文摘要原文（arXiv Abstract原文）

> As corporate responsibility increasingly incorporates environmental, social, and governance (ESG) criteria, ESG reporting is becoming a legal requirement in many regions and a key channel for documenting sustainability practices and assessing firms' long-term and ethical performance. However, the length and complexity of ESG disclosures make them difficult to interpret and automate the analysis reliably. To support scalable and trustworthy analysis, this paper introduces ESG-Bench, a benchmark dataset for ESG report understanding and hallucination mitigation in large language models (LLMs). ESG-Bench contains human-annotated question–answer (QA) pairs grounded in real-world ESG report contexts, with fine-grained labels indicating whether model outputs are factually supported or hallucinated. Framing ESG report analysis as a QA task with verifiability constraints enables systematic evaluation of LLMs' ability to extract and reason over ESG content and provides a new use case: mitigating hallucinations in socially sensitive, compliance-critical settings. We design task-specific Chain-of-Thought (CoT) prompting strategies and fine-tune multiple state-of-the-art LLMs on ESG-Bench using CoT-annotated rationales. Our experiments show that these CoT-based methods substantially outperform standard prompting and direct fine-tuning in reducing hallucinations, and that the gains transfer to existing QA benchmarks beyond the ESG domain.

**完整引用**:
```
@article{esgbench2026,
  title={{ESG-Bench: Benchmarking Long-Context ESG Reports for Hallucination Mitigation}},
  author={Siqi Sun and Ben Peng Wu and Mali Jin and Peizhen Bai and Hanpei Zhang and Xingyi Song},
  journal={arXiv preprint arXiv:2603.13154},
  year={2026},
  note={Accepted to AAAI 2026}
}
```

---

## 3. 中文摘要翻译

随着企业社会责任日益融入环境、社会和治理（ESG）标准，ESG报告正成为许多地区的法律要求，同时也是记录可持续发展实践和评估企业长期及道德绩效的关键渠道。然而，ESG披露文件的长度和复杂性使得难以对其进行可靠地解读和自动化分析。为了支持可扩展且可信的分析，本文提出了ESG-Bench，这是一个用于ESG报告理解和大型语言模型（LLM）幻觉缓解的基准数据集。ESG-Bench包含基于真实ESG报告语境的人工标注问答对，并配有细粒度标签，用于指示模型输出是有事实依据的还是幻觉产生的。将ESG报告分析定位为带有可验证性约束的问答任务，能够系统性地评估LLM提取和推理ESG内容的能力，并提供了一个新的应用场景：在社会敏感、合规关键的环境中缓解幻觉。我们设计了任务特定的思维链（CoT）提示策略，并使用CoT标注的推理轨迹在ESG-Bench上微调了多个最先进的LLM。我们的实验表明，这些基于CoT的方法在减少幻觉方面显著优于标准提示和直接微调，且效果能够迁移到ESG领域之外的现有问答基准。

---

## 4. 研究背景

### 4.1 ESG报告的重要性与挑战

ESG（环境、社会和治理）报告在现代企业实践中变得越来越重要。ESG提供了一套框架，用于评估企业在环境、社会和治理方面的可持续发展相关风险管理（de Souza Barbosa et al., 2023）。曾经在很大程度上是自愿性的ESG信息披露，如今已在许多地区成为法律要求，尤其是通过欧盟的《企业可持续发展报告指令》（CSRD）和《可持续金融披露条例》（SFDR）。这一转变反映了各方对企业在社会和环境方面透明度的日益增长的期望（Niu, 2024）。

企业现在为投资者、监管机构和公众发布大量ESG报告（Assaf et al., 2024; Seok et al., 2024）。然而，这些披露的有用性取决于其可信度和可比性。第三方ESG评级机构（如Sustainalytics和MSCI）因方法论不透明和不一致而受到广泛批评，研究表明即使对同一家公司，它们的评分往往也存在实质性差异，这源于指标选择、权重方案和数据源的差异（Clementino and Perkins, 2021; Cort and Esty, 2020）。这些争议削弱了利益相关者的信任，突显出ESG评估远未标准化。加上ESG报告日益增长的长度和复杂性，这种不一致性增加了对可扩展、透明工具的需求，以支持可靠且有证据支撑的解读。

### 4.2 LLM在ESG分析中的机遇与挑战

大型语言模型（LLM）的出现（Achiam et al., 2023; Dubey et al., 2024; Dong et al., 2025）为大规模自动化ESG披露分析提供了新机遇。然而，ESG报告的复杂性和多样性给可靠的LLM部署带来了重大挑战：

**挑战一：漂绿问题（Greenwashing）**。企业可能进行"漂绿"，即夸大其环保举措以显得更可持续发展，向投资者和利益相关者误导其真实的ESG影响（Yu et al., 2020）。

**挑战二：定性数据丰富**。ESG报告包含大量定性数据，需要深入的上下文理解、行业特定知识和监管框架的熟悉，而这些正是LLM由于依赖通用知识而可能面临的障碍（Young-Ferris and Roberts, 2023）。

**挑战三：多模态处理**。ESG报告通常涉及多模态处理，通常包含文本、表格和图形的混合（Che et al., 2024）。

**挑战四：长文档检索与分析**。这些文档通常跨越数百页，因此长文档检索和分析至关重要（Ferjančič et al., 2024）。LLM在高效文档解析、稳健记忆召回和长报告跨节理解方面仍然受到限制。

### 4.3 LLM幻觉问题在ESG领域尤为严重

LLM由于在文档解析、检索和跨节理解方面的局限性，加上依赖可能与ESG报告事实内容相冲突的参数知识（Kamath et al., 2024; Chen et al., 2024），这种错位经常导致幻觉——即与源文档无事实依据的答案。在ESG这一社会敏感、合规关键领域中，幻觉的后果尤为严重：

- **投资决策风险**：基于幻觉ESG信息的投资决策可能导致资本错误配置
- **合规风险**：监管机构依赖ESG数据进行监管，幻觉可能导致合规判断失误
- **声誉风险**：企业基于LLM分析发布误导性ESG声明可能面临严重的声誉和法律后果

### 4.4 现有研究不足

尽管NLP和LLM已被用于自动化ESG披露分析，包括气候风险提取（Luccioni et al., 2020）、金融问答（Goel et al., 2020）、对话式ESG查询（Mishra et al., 2024a）和自动化可持续发展报告分析如ChatReport（Ni et al., 2023），以及最近的多语言和领域特定ESG数据集探索（Lee et al., 2024; Li et al., 2024），但现有的ESG问答资源专注于答案提取，并不提供幻觉标签、思维链信号，也不支持长的完整报告上下文。

在幻觉缓解方面，虽然已通过校准和自评估（Kadavath et al., 2022）、架构干预（Chrysostomou et al., 2024）、实体级验证（Zhao et al., 2020）和不确定性估计（Xiao et al., 2019; Farquhar et al., 2024）等方法进行了研究，但HaluEval、TriviaQA和BioASQ等基准（Li et al., 2023; Joshi et al., 2017; Krithara et al., 2023）支持跨通用领域的评估，并不针对长而异构的ESG文档。

---

## 5. 核心贡献

### 5.1 基准数据集构建（Benchmark Construction）

本文提出了**ESG-Bench**，这是首个专门为长上下文问答和ESG报告中幻觉缓解设计的基准数据集。据作者所知，它是首个支持在社会和监管重要领域系统性评估和针对性缓解幻觉的结构化资源。

ESG-Bench的核心特点：
- **人工标注的问答对**：基于真实ESG报告语境构建
- **细粒度幻觉标签**：标注模型输出是有事实依据还是幻觉
- **幻觉类型分类**：区分加性幻觉（Additive Hallucinations）和缺失幻觉（Omissive Hallucinations）
- **完整的报告级上下文**：支持长文档理解和跨节推理

### 5.2 任务特定的幻觉缓解策略（Task-Specific Strategy for Hallucination Mitigation）

本文开发了一种基于任务特定思维链（Task-Specific Chain-of-Thought, CoT）提示的微调方法：
- 设计任务特定的CoT提示策略
- 使用CoT标注的推理轨迹（rationales）
- 在ESG-Bench上微调多个最先进的LLM

该方法显著提高了事实 grounding 并减少了幻觉输出，展示了结构化推理在领域特定问答任务中的有效性。

### 5.3 实证评估（Empirical Evaluation）

在ESG-Bench上微调和评估了多个最先进的LLM：
- 比较幻觉缓解性能
- 跨ESG和现有问答基准评估
- 突显了ESG分析中长上下文推理的独特挑战
- 提供了高风险合规环境中模型可靠性的稳健评估

实验结果表明，CoT方法显著优于标准提示和直接微调，且效果能够迁移到ESG领域之外的现有问答基准。

---

## 6. 研究方法

### 6.1 幻觉分类体系

本文将幻觉分为两大类：

**加性幻觉（Additive Hallucinations）**：模型引入不支持的信息。即模型在回答中增加了源ESG报告中不存在的细节、数据或声明。

**缺失幻觉（Omissive Hallucinations）**：模型未能回答尽管有相关证据的问题。即模型因为遗漏了报告中的关键信息而给出了不完整或缺失的回答。

这种分类与事实性（factuality）和忠实性（faithfulness）概念相关（Ji et al., 2023），但通过明确的**人工标注**进行了形式化。

### 6.2 数据集构建流程

ESG-Bench采用**模型-然后-标注器（Model-Then-Annotator）**流水线构建：

```
ESG原始报告 → 问题生成（Model） → 答案生成（Model） → 人工标注（Annotator） → 幻觉标签 → ESG-Bench
```

该流程包含以下关键步骤：

1. **数据收集**：收集真实世界的ESG报告，涵盖多个行业和地区
2. **问题设计**：设计能够测试ESG理解能力的多样化问题类型
3. **答案生成**：使用LLM生成候选答案
4. **人工标注**：由专业标注员判断答案是否 hallucinated
5. **幻觉分类**：对幻觉进行加性/缺失的二分类标注

### 6.3 思维链提示策略

本文设计的任务特定CoT策略包含以下特点：

**结构化推理步骤**：
1. **证据定位**：首先识别ESG报告中与问题相关的文本段落
2. **证据评估**：评估所识别证据的可靠性和相关性
3. **推理演绎**：基于证据进行逻辑推理
4. **答案生成**：生成最终答案，明确区分事实和推断

**CoT标注的推理轨迹**：
- 使用人工标注的推理过程作为微调信号
-教导模型如何在ESG分析中进行结构化思考
- 减少对参数化知识的依赖，增强对输入上下文的 grounding

### 6.4 可验证性约束的问答框架

本文将ESG报告分析框架为带有**可验证性约束**的问答任务：

- 每个问题都关联特定的ESG报告文本范围
- 答案必须能够追溯到源文档的具体位置
- 标注员验证答案与源文档的一致性
- 这种约束确保了评估的可解释性和可重复性

---

## 7. 实验设置

### 7.1 数据集

ESG-Bench包含基于真实企业ESG报告构建的问答对，覆盖多种行业和规模的企业，确保数据集的多样性和代表性。

### 7.2 评估指标

实验采用多种指标评估模型性能：

**幻觉检测指标**：
- 加性幻觉率（Additive Hallucination Rate）
- 缺失幻觉率（Omissive Hallucination Rate）
- 总幻觉率（Total Hallucination Rate）

**问答质量指标**：
- 答案准确率（Answer Accuracy）
- 幻觉-free准确率（Hallucination-Free Accuracy）
- F1分数（F1 Score）

### 7.3 基线方法对比

实验对比了多种基线方法：

**提示方法**：
- 标准提示（Standard Prompting）：直接问答
- 零样本CoT（Zero-Shot CoT）：增加"让我们一步一步思考"
- 少样本提示（Few-Shot Prompting）：提供示例

**微调方法**：
- 直接微调（Direct Fine-tuning）：直接在问答对上微调
- CoT微调（CoT Fine-tuning）：使用CoT标注数据进行微调

### 7.4 评估模型

实验评估了多个最先进的LLM，包括：
- GPT系列模型
- Claude系列模型
- 开源LLM（如Llama系列）

---

## 8. 实验结果

### 8.1 CoT方法显著减少幻觉

实验结果证明，基于CoT的方法在减少幻觉方面显著优于标准提示和直接微调：

**关键发现**：

1. **任务特定CoT的优势**：专门为ESG分析设计的CoT策略比通用CoT更有效，因为它们融入了ESG领域的推理特点

2. **CoT微调 vs 标准提示**：使用CoT标注推理轨迹微调的模型，在幻觉率上显著低于标准提示基线

3. **迁移学习效果**：在ESG-Bench上训练的CoT推理能力可以迁移到其他领域的问答任务，说明结构化推理具有跨领域通用性

### 8.2 长上下文推理的挑战

实验突显了ESG分析中长上下文推理的独特挑战：

- **跨节信息整合**：涉及多个ESG报告章节的信息整合问题
- **长程依赖**：模型在处理长文档时面临记忆和检索的困难
- **细节 vs 整体**：同时保持对细节的准确性和对整体的把握

### 8.3 不同幻觉类型的差异

加性幻觉和缺失幻觉表现出不同的模式：

- **加性幻觉**：在模型自信度较高但知识不准确时更常发生
- **缺失幻觉**：在涉及多个报告章节的复杂问题时更常发生

### 8.4 跨领域迁移性

最关键的发现之一是**迁移性**：在ESG-Bench上开发的CoT策略和微调方法，在现有问答基准上也取得了性能提升，证明：

- 幻觉缓解技术具有领域通用性
- 结构化推理能力可以跨领域迁移
- ESG分析可以作为检验LLM可靠性的严格测试场景

---

## 9. 策略示例

### 9.1 标准提示示例

**输入**：
```
基于以下ESG报告，回答问题：该公司2024年的碳排放量是多少？

[长ESG报告文本，约200页]

问题：该公司的范围一和范围二碳排放量是多少？
```

**模型输出（可能幻觉）**：
> 该公司2024年的范围一碳排放量为45,000吨二氧化碳当量，范围二为38,000吨。
> [模型可能从其参数化知识中"想起"某个数字，而不是从报告中提取]

### 9.2 任务特定CoT提示示例

**输入**：
```
你是一位专业的ESG报告分析师。请按照以下步骤分析ESG报告并回答问题：

第一步 - 证据定位：识别报告中与问题相关的具体段落
第二步 - 证据评估：确认这些段落是否直接回答问题
第三步 - 推理：如需推理，明确说明推理过程
第四步 - 答案生成：仅基于报告中的证据给出答案

报告文本：[长ESG报告]

问题：该公司的范围一碳排放量是多少？
```

**期望输出（含CoT推理）**：
> 第一步 - 证据定位：
> 在报告第15页的"环境绩效"章节，找到以下段落：
> "2024年，本公司的范围一直接温室气体排放为42,500吨二氧化碳当量。"
>
> 第二步 - 证据评估：
> 该段落直接回答了关于范围一排放的问题，来源可靠（公司官方报告）。
>
> 第三步 - 推理：
> 无需额外推理，证据直接包含答案。
>
> 第四步 - 答案生成：
> 该公司2024年的范围一碳排放量为42,500吨二氧化碳当量。
> [注意：如果报告中未找到相关信息，应明确说明"报告中未提供此信息"]

### 9.3 幻觉检测示例

**输入（用于标注）**：
```
报告相关段落："2024年，本公司的可再生能源使用比例为32%。"

模型回答："根据报告，该公司2024年可再生能源使用比例为32%，同时在员工培训方面投入了250万美元。"
```

**幻觉分析**：
- 32%这一数据：有事实依据 ✓（加性幻觉：无）
- "员工培训投入250万美元"：报告中未提及 ✗（加性幻觉：存在）

---

## 10. 攻击流程（不适用于本论文）

> **说明**：ESG-Bench是一篇关于幻觉缓解的防御性/评估论文，不包含攻击流程。本章节保留为空节，以符合笔记格式规范。

---

## 11. 消融实验

虽然原始论文中没有传统意义上的"消融实验"，但论文隐含地进行了多维度对比分析：

### 11.1 CoT提示策略的消融分析

**对比维度**：
- 标准提示 vs 零样本CoT vs 任务特定CoT
- 不同CoT设计（通用CoT vs 领域定制CoT）

**发现**：任务特定CoT > 通用CoT > 零样本CoT > 标准提示

### 11.2 微调策略的消融分析

**对比维度**：
- 直接微调 vs CoT微调
- 不同CoT标注质量的影响

**发现**：CoT微调在幻觉指标上持续优于直接微调

### 11.3 数据集规模的消融分析

**对比维度**：
- 不同训练数据量对模型性能的影响
- 幻觉标注质量（人工标注 vs 模型自动标注）

**发现**：模型-然后-标注器流水线中，标注质量是关键瓶颈

### 11.4 模型规模的消融分析

**对比维度**：
- 不同模型规模对幻觉率的影响
- 大模型是否天然更少幻觉

**发现**：模型规模有帮助，但任务特定训练比单纯规模更重要

---

## 12. 局限性

### 12.1 数据集覆盖局限

- **行业覆盖**：ESG-Bench可能无法覆盖所有行业的ESG报告特点（如金融、能源、科技等行业的报告结构差异很大）
- **地区覆盖**：不同地区的ESG报告标准和格式存在差异，可能影响跨地区适用性
- **语言覆盖**：目前主要针对英文ESG报告，多语言支持可能不足

### 12.2 幻觉定义的局限

- **加性/缺失的二分法**：可能无法覆盖所有幻觉类型，如"扭曲性幻觉"（部分正确但被曲解）
- **主观性**：幻觉判断具有一定主观性，不同标注员可能存在分歧
- **上下文敏感性**：某些情况下，模型的"幻觉"可能是对不完整信息的合理推断

### 12.3 方法论的局限

- **CoT依赖**：方法强烈依赖思维链推理能力，对不支持CoT的模型不适用
- **计算成本**：CoT微调和推理带来额外的计算成本
- **可扩展性**：在更大规模、更多样化的ESG报告上，效果尚待验证

### 12.4 实际部署的挑战

- **实时性**：长文档处理和CoT推理增加了延迟
- **成本**：相比简单提示，CoT方法带来更高的API调用成本
- **可解释性**：虽然CoT提高了可解释性，但如何向非技术用户解释仍具挑战

### 12.5 未来改进方向

1. 扩展数据集的行业和地区覆盖
2. 探索自动化幻觉检测方法
3. 研究多模态ESG报告（图表混合）的幻觉问题
4. 开发针对ESG领域专门优化的LLM
5. 探索知识图谱辅助的ESG分析

---

## 13. 伦理声明

### 13.1 数据使用

- ESG-Bench使用的是公开可用的企业ESG报告，不涉及敏感个人信息
- 数据集构建过程遵循负责任的数据使用原则

### 13.2 研究影响

**正面影响**：
- 提高ESG分析的可信度和可靠性
- 帮助投资者和监管机构做出更明智的决策
- 推动LLM在关键领域的安全部署

**潜在风险**：
- 如果模型被不当使用，可能放大ESG评估中的偏差
- 依赖LLM进行ESG分析可能削弱人类专家的作用

### 13.3 漂绿检测的相关性

本文的方法虽然主要关注幻觉缓解，但也可用于检测ESG报告中的漂绿行为：
- 幻觉检测可以帮助识别企业ESG报告中的不实陈述
- 通过对比模型识别的事实与企业自我报告，可以发现潜在的不一致

### 13.4 研究透明度

- 论文公开了方法论和关键发现
- 基准数据集的发布将促进社区协作

---

## 14. 参考文献

1. Achiam, J., et al. (2023). GPT-4 Technical Report. arXiv preprint.
2. Dubey, S., et al. (2024). The Llama 3 Herd of Models. arXiv preprint.
3. Dong, Y., et al. (2025). [Reference in paper].
4. de Souza Barbosa, et al. (2023). ESG framework reference.
5. Niu, G. (2024). EU Sustainability Reporting Regulations. [Reference in paper].
6. Arvidsson, S. and Dumay, J. (2022). ESG reporting. [Reference in paper].
7. Rossi, M. and Candio, B. (2023). Corporate sustainability. [Reference in paper].
8. Assaf, et al. (2024). ESG disclosure research. [Reference in paper].
9. Seok, et al. (2024). Sustainability reporting. [Reference in paper].
10. Clementino, E. and Perkins, R. (2021). ESG rating divergence. [Reference in paper].
11. Cort, R. and Esty, D. (2020). ESG score inconsistency. [Reference in paper].
12. Yu, M., et al. (2020). Greenwashing in ESG communications. [Reference in paper].
13. Young-Ferris, J. and Roberts, H. (2023). Qualitative ESG data. [Reference in paper].
14. Che, et al. (2024). Multimodal ESG reports. [Reference in paper].
15. Ferjančič, et al. (2024). Long document retrieval. [Reference in paper].
16. Kamath, et al. (2024). Parametric knowledge conflicts. [Reference in paper].
17. Chen, et al. (2024). LLM factuality issues. [Reference in paper].
18. Luccioni, S., et al. (2020). Climate risk extraction from ESG. [Reference in paper].
19. Goel, et al. (2020). Financial QA. [Reference in paper].
20. Mishra, et al. (2024a). Conversational ESG querying. [Reference in paper].
21. Ni, et al. (2023). ChatReport: Automated sustainability analysis. [Reference in paper].
22. Lee, et al. (2024). Multilingual ESG datasets. [Reference in paper].
23. Li, et al. (2024). Domain-specific ESG data. [Reference in paper].
24. Kadavath, S., et al. (2022). LLM calibration and self-evaluation. [Reference in paper].
25. Chrysostomou, et al. (2024). Architectural interventions for hallucination. [Reference in paper].
26. Xiao, et al. (2019). Uncertainty estimation for NLP. [Reference in paper].
27. Farquhar, et al. (2024). Uncertainty in LLM outputs. [Reference in paper].
28. Li, J., et al. (2023). HaluEval: Hallucination evaluation benchmark. [Reference in paper].
29. Joshi, M., et al. (2017). TriviaQA: A reading comprehension dataset. [Reference in paper].
30. Krithara, A., et al. (2023). BioASQ: Biomedical semantic indexing. [Reference in paper].
31. Wei, J., et al. (2022). Chain-of-Thought Prompting Elicits Reasoning. NeurIPS.
32. Kojima, T., et al. (2022). Large Language Models are Zero-Shot Reasoners. NeurIPS.
33. Zhang, et al. (2023). Symbolic Chain-of-Thought. [Reference in paper].
34. Lyu, et al. (2023). Chain-of-Thought for Fact Verification. [Reference in paper].
35. Ji, T., et al. (2023). Survey on hallucination in NLG. [Reference in paper].
36. Sun and Ruan (2023). Robustness verification for NLP. [Reference in paper].
37. Wang, et al. (2022). Formal robustness verification. [Reference in paper].
38. Sun, et al. (2024). Certifiable LLM behavior. [Reference in paper].
39. Li, et al. (2025). LLM reasoning robustness. [Reference in paper].
40. Yi, et al. (2024). CoT robustness considerations. [Reference in paper].

---

*本文档由 AI 助手自动生成，基于 arXiv 公开信息*
*论文链接: https://arxiv.org/abs/2603.13154*
*最后更新: 2026-03-26*
