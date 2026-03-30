# Towards Mitigating LLM Hallucination via Self-Reflection

## 1. 基本信息

| 项目 | 内容 |
|------|------|
| **论文标题** | Towards Mitigating LLM Hallucination via Self-Reflection |
| **作者** | Ziwei Ji, Tiezheng Yu, Yan Xu, Nayeon Lee, Etsuko Ishii, Pascale Fung |
| **机构** | Center for Artificial Intelligence Research (CAiRE), 香港科技大学 (HKUST) |
| **会议/期刊** | Findings of the Association for Computational Linguistics: EMNLP 2023 |
| **arXiv编号** | [arXiv:2310.06271](https://arxiv.org/abs/2310.06271) |
| **DOI** | 10.18653/v1/2023.findings-emnlp.123 |
| **GitHub** | [ziweiji/Self_Reflection_Medical](https://github.com/ziweiji/Self_Reflection_Medical) |
| **研究方向** | Hallucination Mitigation / Medical QA |
| **关键词** | Hallucination, Large Language Model, Medical Question Answering, Generative Question Answering |
| **发表时间** | 2023年12月 (EMNLP 2023) |

---

## 2. 英文摘要原文（arXiv Abstract）

> Large language models (LLMs) have shown promise for generative and knowledge-intensive tasks including question-answering (QA) tasks. However, the practical deployment still faces challenges, notably the issue of "hallucination", where models generate plausible-sounding but unfaithful or nonsensical information. This issue becomes particularly critical in the medical domain due to the uncommon professional concepts and potential social risks involved. This paper analyses the phenomenon of hallucination in medical generative QA systems using widely adopted LLMs and datasets. Our investigation centers on the identification and comprehension of common problematic answers, with a specific emphasis on hallucination. To tackle this challenge, we present an interactive self-reflection methodology that incorporates knowledge acquisition and answer generation. Through this feedback process, our approach steadily enhances the factuality, consistency, and entailment of the generated answers. Consequently, we harness the interactivity and multitasking ability of LLMs and produce progressively more precise and accurate answers. Experimental results on both automatic and human evaluation demonstrate the superiority of our approach in hallucination reduction compared to baselines.

**引用格式 (ACL):**
> Ziwei Ji, Tiezheng Yu, Yan Xu, Nayeon Lee, Etsuko Ishii, and Pascale Fung. 2023. Towards Mitigating LLM Hallucination via Self Reflection. In Findings of the Association for Computational Linguistics: EMNLP 2023, pages 1827–1843, Singapore. Association for Computational Linguistics.

---

## 3. 中文摘要翻译

> 大语言模型（LLM）在生成式和知识密集型任务（包括问答任务）中展现了巨大潜力。然而，其实际部署仍面临重大挑战，其中最突出的问题是"幻觉"——模型生成看似合理但实际上不忠实或无意义的信息。在医学领域，这一问题尤为关键，因为不准确或误导性的信息可能对患者护理造成严重影响，此外医学领域还存在大量不常见的专业术语和潜在的社会风险。本文系统分析了主流LLM和数据集在医学生成式问答系统中的幻觉现象。我们重点研究了对问题答案的识别和理解，尤其关注幻觉问题。为解决这一挑战，我们提出了一种交互式自我反思方法论，将知识获取与答案生成相结合。通过这一反馈过程，我们的方法稳步提升了生成答案的事实性、一致性和蕴含性。因此，我们充分利用了LLM的交互性和多任务能力，生成越来越精确和准确的答案。在自动化评估和人工评估上的实验结果均表明，我们的方法在减少幻觉方面优于基线方法。

---

## 4. 研究背景

### 4.1 LLM与生成式问答（GQA）

大语言模型在生成式问答任务中展现了卓越的能力。生成式问答系统能够以自然语言形式响应用户查询，回答涵盖多种格式，包括：
- **Yes/No问题**：判断型问题
- **多选题**：选择题型
- **抽取式问答**：从文本中抽取答案片段
- **生成式问答**：自由形式的答案生成

问答系统既是探测语言模型能力的重要手段，也是LLM落地应用的典型场景。然而，LLM在生成答案时会产生"幻觉"——生成看似流畅合理但实际不忠实或无意义的内容。

### 4.2 医学领域的特殊挑战

在医学领域，幻觉问题的影响格外严重：

1. **专业概念复杂**：医学领域存在大量不常见的专业术语（如PTEN突变、Noonan综合征等），普通模型难以准确理解
2. **潜在社会风险**：不准确的医疗信息可能对患者护理造成严重后果，甚至危及生命
3. **知识覆盖不足**：通用LLM在医学专业知识上的覆盖存在明显缺陷

论文以一个典型例子说明：对于问题"Is Noonan syndrome inherited?"（Noonan综合征是遗传的吗？），某LLM生成了包含PTEN突变与Noonan综合征错误关联的答案——PTEN突变实际上通常与Cowden综合征相关，而非Noonan综合征，这构成了明显的幻觉。

### 4.3 现有方法的局限

- **外部知识检索方法**（RAG等）：依赖外部知识库的质量和覆盖度
- **参数化知识方法**：利用LLM内部知识，但幻觉问题依然存在
- **表面语言能力与内在知识的差距**：即便LLM具备一定能力，实际生成中仍频繁出现幻觉

### 4.4 问题定位

本文聚焦于以下核心研究问题：
1. 当前主流LLM在医学问答中的幻觉现象有多严重？
2. 幻觉产生的潜在原因是什么？
3. 如何利用LLM自身能力来减少幻觉？

---

## 5. 核心贡献

本文的三大核心贡献：

### 贡献一：全面的幻觉现象分析
对5种主流LLM在5个医学问答数据集上的幻觉现象进行了系统性分析，揭示了幻觉的具体表现形式和发生规律。

### 贡献二：创新的自我反思方法
提出了一种创新性的自我反思（Self-Reflection）方法，通过迭代反馈循环，逐步生成、评分和精炼知识及答案，直至达到满意的水平，从而提高答案的准确性和可靠性。

### 贡献三：有效性验证
实验结果表明，该方法在参数量从7B到175B不等的多种LLM上均取得了显著改善，验证了方法的泛化能力和可扩展性。

---

## 6. 研究方法

### 6.1 方法概述

本文提出的自我反思方法是一个**迭代式、反思性的过程**，充分利用LLM在生成和精炼响应方面的能力。如论文图4所示，该方法由**三个核心循环**组成：

```
┌─────────────────────────────────────────────────────┐
│           Interactive Self-Reflection Loop            │
│                                                      │
│  ┌─────────────────┐                                 │
│  │  Question Input  │                                 │
│  └────────┬────────┘                                 │
│           │                                          │
│           ▼                                          │
│  ┌─────────────────────────────────────────────────┐│
│  │  (1) Factual Knowledge Acquiring Loop (黄色)      ││
│  │  - 生成背景知识                                   ││
│  │  - 事实性评分                                     ││
│  │  - 知识精炼（若事实性不足）                        ││
│  └────────┬────────────────────────────────────────┘│
│           │ 背景知识输出                              │
│           ▼                                          │
│  ┌─────────────────────────────────────────────────┐│
│  │  (2) Knowledge-Consistent Answering Loop (绿色)  ││
│  │  - 基于知识生成答案                               ││
│  │  - 一致性评分                                     ││
│  │  - 答案精炼（若一致性不足）                        ││
│  └────────┬────────────────────────────────────────┘│
│           │ 候选答案输出                             │
│           ▼                                          │
│  ┌─────────────────────────────────────────────────┐│
│  │  (3) Question-Entailment Answering Loop (黑色)  ││
│  │  - 蕴含性评估                                     ││
│  │  - 若不满足则返回第一阶段重新开始                  ││
│  └─────────────────────────────────────────────────┘│
│           │ 最终答案                                  │
│           ▼                                          │
│  ┌─────────────────┐                                │
│  │  Final Answer   │                                 │
│  └─────────────────┘                                 │
└─────────────────────────────────────────────────────┘
```

### 6.2 三个核心循环详解

#### 循环一：事实性知识获取循环（Factual Knowledge Acquiring Loop）

**目标**：获取与问题相关的事实性背景知识。

**步骤**：
1. **知识生成（Knowledge Generation）**：模型根据问题生成背景知识，利用LLM合成与问题相关的上下文信息
2. **事实性评分（Factuality Scoring）**：使用定制化、无参考的评分器对生成的知识进行事实性评估
3. **知识精炼（Knowledge Refinement）**：若评分低于阈值，模型利用内在反思能力对知识进行自我修正

**事实性评分器公式**：
```
Fs(k|D,Q) = Σ_{t=1}^{m} log P(k_t | k_{<t}, T(D,Q)) * Fs(conditional)
```
其中k是生成的知识，D是上下文，Q是问题，T(D,Q)是任务指令。

**迭代终止条件**：事实性评分达到预设阈值或达到最大迭代次数（默认为3次）。

#### 循环二：知识一致答案生成循环（Knowledge-Consistent Answering Loop）

**目标**：确保生成的答案与已获取的背景知识保持一致。

**步骤**：
1. **答案生成（Answer Generation）**：基于循环一获取的背景知识生成答案
2. **一致性评分（Consistency Scoring）**：评估答案与背景知识之间的一致程度
3. **答案精炼（Answer Refinement）**：若一致性不足，模型修正答案以匹配背景知识

**迭代终止条件**：一致性评分达到预设阈值或达到最大迭代次数。

#### 循环三：问题蕴含答案循环（Question-Entailment Answering Loop）

**目标**：确保生成的答案在逻辑上与问题保持蕴含关系。

**步骤**：
1. **蕴含性评估（Entailment Evaluation）**：评估答案是否在逻辑上与问题相关（entailment）
2. **反馈机制**：若答案不满足蕴含性标准，过程返回循环一，重新开始整个迭代

**使用Med-NLI（Medical Natural Language Inference）进行评估**。

### 6.3 幻觉分类

通过分析250个直接生成的示例，本文将问题答案分为**三类**：

| 类别 | 定义 | 示例 | 是否属于幻觉 |
|------|------|------|-------------|
| **Fact Inconsistency**（事实不一致） | 提供与事实相悖或不兼容的信息 | 声称"Noonan综合征不遗传"，实际为常染色体显性遗传 | ✅ 是 |
| **Query Inconsistency**（查询不一致） | 答案与问题无关或无意义 | 问题问心脏手术，答案大谈维生素益处却不提心脏 | ✅ 是 |
| **Tangentiality**（偏题） | 提供与主题相关但不直接回答问题的信息 | 讨论了相关疾病但未回答原问题 | ❌ 非幻觉 |

### 6.4 幻觉原因探索

#### 频率效应（Frequency Effect）
- 使用Google N-grams作为代理指标（近似LLM预训练语料中的文本分布）
- 发现：幻觉答案中的关键词/主题词频率显著低于正确答案
- **低频率可能是幻觉的潜在原因之一**

#### 医学领域微调的影响
- 在医学领域微调的LLM（如MedAlpaca、Robin-medical）在某些任务上表现更好
- 但在生成式问答任务上反而出现更多问题：内容不相关、语法问题、无根据模板、虚构引用、缺乏解释性推理
- Robin-medical在F1和ROUGE-L上得分最低
- 表明：**指令学习比非指令调优更适合医学GQA任务**

---

## 7. 实验设置

### 7.1 评测模型（5个LLM）

| 模型 | 类型 | 参数量 | 训练方式 | 说明 |
|------|------|--------|---------|------|
| **Vicuna** | 通用LLM | 7B/13B | 在ShareGPT对话数据上微调LLaMA | 质量与ChatGPT相当 |
| **Alpaca-LoRA** | 通用LLM | 7B | LoRA低秩适应，复现Stanford Alpaca | 质量与GPT-3.5相当 |
| **ChatGPT** | 通用LLM | ~175B | RLHF训练 | 使用OpenAI官方API |
| **MedAlpaca** | 医学LLM | 7B | 在医学对话和QA数据上微调LLaMA | 医学领域专用 |
| **Robin-medical** | 医学LLM | 7B | 通过LMFlow在医学领域微调LLaMA | 医学领域专用 |

### 7.2 数据集（5个医学QA数据集）

| 数据集 | 规模 | 来源 | 答案类型 | 特点 |
|--------|------|------|---------|------|
| **PubMedQA** | 1k专家标注 + 61.2k未标注 + 211.3k生成 | 生物医学文献 | Yes/No/Maybe | 问题来自论文标题，摘要作为上下文 |
| **MedQuAD** | 47,457 QA对 | NIH网站 | 各类格式 | 涵盖37类问题，包括疾病、药物、诊断等 |
| **MEDIQA2019** | 多类任务数据 | 医学问答挑战赛 | 评分3-4为黄金答案 | 包含NLI、RQE、QA三个任务 |
| **LiveMedQA2017** | 多类型QA对 | 医学专家标注 | 参考答案含URL | 26类问题，含子问题、焦点和类型 |
| **MASH-QA** | 34k QA对 | 消费者健康领域 | 多跨度答案 | 答案可能来自非连续的长文档段落 |

### 7.3 评估指标

#### 自动化评估指标

1. **GQA标准指标**：
   - **Unigram F1**：单词级别的精确率和召回率调和平均
   - **ROUGE-L**：最长公共子序列的F值

2. **Med-NLI（医学自然语言推理）**：
   - 使用SciFive（T5预训练模型）进行评估
   - **样本级Med-NLI**：评估生成的答案是否蕴含、 neutral或contradicts上下文/参考答案
   - **句子级Med-NLI**：对生成答案中的每个句子分别进行评估

3. **CTRLEval一致性指标**：
   - 无监督、无参考、任务无关的评估指标
   - 通过将一致性方面转化为多个文本填充任务来评估

#### 人工评估

在Amazon Mechanical Turk平台上进行：
- 随机选取Vicuna直接生成的50对 + 本文方法生成的50对
- 每样本由3名不同标注员评估（要求HIT批准率≥95%，已批准数量≥5000）
- 标注员来自澳大利亚、加拿大、英国和美国
- 事实不一致：0.3美元/句
- 问题不一致和偏题：0.15美元/答案

---

## 8. 实验结果

### 8.1 自动化评估结果

论文中的表2展示了在5个数据集测试集上的自动化评估结果。核心发现：

**所有5个模型在所有5个数据集上，使用自我反思循环（标注为_L）的方法均优于基线（直接生成）**。

主要观察：
- Vicuna-L、Alpaca-LoRA-L、ChatGPT-L、MedAlpaca-L 在各项指标上均有显著提升
- Robin-medical因生成质量较差，在初步分析后被排除在进一步实验之外
- 自我反思方法在7B到175B不同参数量的模型上均有效

### 8.2 幻觉分类统计（错误分析）

通过分析250个示例，三类问题的发生率如图2所示：

**Vicuna、Alpaca-LoRA、ChatGPT** 三种模型中：
- Fact Inconsistency（事实不一致）发生率较高，是幻觉的主要形式
- Query Inconsistency（查询不一致）次之
- Tangentiality（偏题）也有相当比例

**ChatGPT相对Vicuna**：ChatGPT生成的句子更偏一般性（generic），但经过自我反思后，可以在保持低泛化水平的同时显著改善事实一致性。

### 8.3 幻觉与频率的关系

- Google N-grams频率分析表明：幻觉答案中的关键词频率低于正确答案
- 低频率可能是导致幻觉的潜在因素之一（需要更多探索来证实）

### 8.4 人工评估结果（表6）

在PubMedQA上的人工评估结果表明：
- 本文方法在Vicuna和ChatGPT上均成功**降低了Query Inconsistency、Tangentiality和Fact Inconsistency的比例**
- ChatGPT-L（带自我反思的ChatGPT）在各项指标上均优于直接生成的ChatGPT

### 8.5 案例分析（表7）

以PubMedQA中的一个案例说明方法效果：

| 模型 | 回答摘要 |
|------|---------|
| **ChatGPT（直接生成）** | 给出否定回答，声称"没有证据表明形状分析可以从CTA中区分游离颈内动脉血栓与动脉粥样硬化斑块" |
| **ChatGPT-L（本文方法）** | 给出肯定回答，承认形状分析在鉴别中的作用，并提到机器学习算法和放射组学特征在分类方面显示出了有前景的结果 ✅ |
| **GPT-4** | 建议形状分析可能有帮助，但后续内容与形状分析本身不相关 |

这表明：自我反思方法能够帮助模型识别并整合正确的信息，生成与黄金答案更一致的结论。

---

## 9. 策略示例

### 示例一：幻觉识别

**问题**：Is Noonan syndrome inherited?（Noonan综合征是遗传的吗？）

**直接生成的幻觉答案**（Alpaca-LoRA）：
> "PTEN mutation is associated with Noonan syndrome..."（错误关联了PTEN突变与Noonan综合征，PTEN实际与Cowden综合征相关）

**幻觉标注**：粉色高亮、下划线标注错误部分

### 示例二：Factuality Scorer演示

论文附录C提供了事实性评分器的演示示例：

**示例1**：
- 问题：What are the risk factors for heart disease?
- 生成知识：Risk factors for heart disease can be categorized into modifiable and non-modifiable. Modifiable risk factors include high blood pressure, high cholesterol, smoking, unhealthy diet, physical inactivity, obesity, and excessive alcohol use. Non-modifiable risk factors include age, gender, family history, and race or ethnicity.

**示例2**：
- 问题：How does smoking affect lung health?
- 生成知识：Smoking damages the airways and small air sacs in your lungs, which can lead to a variety of lung diseases including chronic bronchitis, emphysema, and lung cancer. It also decreases your lung capacity and makes it harder for your lungs to defend against infections and clear out mucus.

**示例3**：
- 问题：Is it safe to take aspirin every day?
- 生成知识：For some people, taking aspirin every day can help prevent heart attacks or strokes. However, daily aspirin isn't appropriate for everyone. It can cause side effects like gastrointestinal bleeding and isn't recommended for people with certain health conditions or who take certain medications. Always consult with a healthcare professional before starting any new medication regimen.

### 示例三：三种问题类型对比

| 类型 | 描述 | 论文表1中的示例 |
|------|------|--------------|
| **Fact Inconsistency** | 答案提供与事实相悖的信息 | 声称"Noonan综合征不遗传"，实际为常染色体显性遗传 |
| **Query Inconsistency** | 答案与问题无关 | 讨论维生素的好处，却完全不提及心脏相关问题 |
| **Tangentiality** | 提供相关信息但未直接回答问题 | 讨论了葡萄膜但未提及c-Kit对葡萄膜的影响 |

---

## 10. 攻击流程（自我反思循环的工作流程）

### 完整工作流程

```
Step 1: 知识获取阶段
┌─────────────────────────────────────────────────────────┐
│ 输入: Question + Context (Dataset)                        │
│ LLM 生成: Background Knowledge                            │
│ 评分器评估: Fs(k|D,Q) 是否 ≥ threshold_factuality        │
│                                                          │
│ 若不满足 → 知识精炼 → 重新生成 → 重新评分                  │
│ 循环直到满足或达到max_knowledge_loop次                   │
└─────────────────────────────────────────────────────────┘
                          ↓ 背景知识获取成功
Step 2: 答案生成阶段
┌─────────────────────────────────────────────────────────┐
│ 基于背景知识 + 问题                                        │
│ LLM 生成: Initial Answer                                  │
│ 一致性评分: Fs(answer|knowledge) 是否 ≥ threshold_consis │
│                                                          │
│ 若不满足 → 答案精炼 → 重新生成 → 重新评分                  │
│ 循环直到满足或达到max_response_loop次                     │
└─────────────────────────────────────────────────────────┘
                          ↓ 一致性评估成功
Step 3: 蕴含性验证阶段
┌─────────────────────────────────────────────────────────┐
│ Med-NLI: 评估 Answer 与 Question 的蕴含关系              │
│ 蕴含性得分是否 ≥ threshold_entailment                    │
│                                                          │
│ 若不满足 → 返回 Step 1，重新开始整个循环                  │
│ 或达到max_main_loop次后输出当前最佳答案                   │
└─────────────────────────────────────────────────────────┘
                          ↓ 蕴含性满足
                      Final Answer
```

### 超参数配置

| 参数 | Vicuna | Alpaca-LoRA | ChatGPT | MedAlpaca |
|------|--------|-------------|---------|-----------|
| temperature | 1.0 | 1.0 | - | 1.0 |
| max new tokens | 512 | 512 | - | 512 |
| max main loop | 3 | 3 | 3 | 3 |
| max knowledge loop | 3 | 3 | 1-3 | 3 |
| max response loop | 3 | 3 | 3 | 3 |
| factuality threshold | -1.0 | -1.0 | -1.0 | -1.0 |
| consistency threshold | -5.0 | -5.0 | -5.0 | -5.0 |
| entailment threshold | 0.8 | 0.8 | 0.8 | 0.8 |
| factuality scorer demos | 1-3 | 1-2 | 1-3 | 1-2 |

### 关键技术点

1. **无参考评分（Reference-free Scorer）**：事实性评分器和一致性评分器均通过上下文指令学习设计，无需参考答案
2. **迭代反馈**：每个循环都是生成→评分→精炼的迭代，直到满足质量阈值
3. **多阶段验证**：经过事实性、一致性、蕴含性三重验证，确保答案质量
4. **早期退出**：通过阈值控制迭代次数，避免无限循环

---

## 11. 消融实验

论文通过不同角度的实验验证了方法各组件的有效性：

### 11.1 各循环的贡献

- **Factual Knowledge Acquiring Loop**：单独使用时提升事实性，但不能保证答案整体质量
- **Knowledge-Consistent Answering Loop**：确保答案与知识一致，但知识本身可能有误
- **Question-Entailment Answering Loop**：确保答案与问题相关，防止答非所问

三个循环的组合使用能够**全面提升答案质量**，相互补充。

### 11.2 不同模型规模的有效性

实验覆盖了7B到175B不同参数量的模型：
- **小模型（7B如Vicuna、Alpaca-LoRA）**：自我反思方法依然有效，但可能需要更多迭代
- **大模型（175B如ChatGPT）**：幻觉减少幅度更大，说明更强大的LLM能更好地利用自我反思能力

### 11.3 通用模型 vs 医学专用模型

- **通用模型（Vicuna、Alpaca-LoRA、ChatGPT）**：经过自我反思后幻觉显著减少
- **医学专用模型（MedAlpaca、Robin-medical）**：MedAlpaca有一定改善，但Robin-medical因基础生成质量过低而未能充分体现方法优势

### 11.4 迭代次数的影响

论文附录B中的超参数设置显示：
- max main loop = 3：整体大循环最多3次
- max knowledge loop = 1-3：知识精炼循环根据数据集调整
- max response loop = 3：答案精炼循环最多3次

实验表明，**大多数改善发生在前1-2次迭代**，后续迭代的边际收益递减。

---

## 12. 局限性

### 12.1 领域范围有限
- 方法主要针对**医学领域**设计和评估
- 在其他知识密集型领域（如法律、金融、科学）的泛化效果有待验证
- 医学领域的专业性和高风险性使得该领域尤为重要，但限制了方法的直接推广

### 12.2 对LLM自身能力的依赖
- 方法的有效性**高度依赖基础LLM的能力**
- 对于参数较小的LLM（如7B模型），自我反思的效果可能受限
- 强大的LLM（如ChatGPT、GPT-4）能更好地理解和修正自身错误

### 12.3 知识质量瓶颈
- 自我反思的知识来源于LLM自身的参数化知识
- 如果LLM对某些知识完全未知或记忆错误，自我反思可能无法有效修正
- 在低频、罕见医学概念上，幻觉问题依然存在（Google N-grams分析证实）

### 12.4 计算成本
- 迭代式方法增加了推理计算量
- 需要多次调用LLM进行生成、评分和精炼
- 在延迟敏感的应用场景中可能不适用

### 12.5 评分器设计
- factuality scorer基于上下文指令学习设计，在某些边界情况下可能不准确
- threshold的设定需要针对不同模型和数据集调优

### 12.6 未来改进方向
- 结合外部知识检索（RAG）来弥补参数化知识的不足
- 使用更强大的LLM作为反思和精炼的引擎
- 探索自动threshold学习而非手动设定
- 将方法扩展到更多知识密集型领域

---

## 13. 伦理声明

### 13.1 医学领域的特殊责任

本文聚焦于医学问答领域的幻觉问题，这一领域具有特殊的社会意义：

1. **潜在风险**：不准确的医疗信息可能对患者健康造成严重影响，甚至危及生命
2. **高标准要求**：医学AI系统必须具备高度可靠性和可解释性
3. **用户信任**：患者和医疗从业者对AI生成的信息的信任需要通过严格的事实性验证来建立

### 13.2 研究价值

1. **促进AI医疗可靠性**：通过减少幻觉，提高LLM在医疗场景中的实用价值
2. **赋能医疗从业者**：为医生和护士提供更可靠的AI辅助工具
3. **推动负责任AI**：展示了通过自我反思等方法提升AI系统安全性的可行路径

### 13.3 局限性声明

论文明确指出：
- 本文方法不能完全消除幻觉，仅能显著减少幻觉发生率
- 在实际医疗应用中，AI生成的答案应始终由专业人士验证
- 不应将LLM作为独立的医疗决策依据

### 13.4 发布与使用

- 论文发表于ACLFindings，向学术社区公开
- GitHub代码仓库开源，供研究复用
- 作者来自香港科技大学CAiRE研究中心

---

## 14. 参考文献

以下为论文中引用的主要文献（按论文中出现顺序整理）：

1. Petroni et al. (2021) - Language Models as Knowledge Bases?
2. Li et al. (2021a) - Rationale-Enriched Answer Generator (REAG)
3. Su et al. (2023, 2022) - Read-before-Generate for faithful GQA
4. Nakano et al. (2021) - WebGPT
5. Lewis et al. (2020) - Retrieval-Augmented Generation (RAG)
6. Guu et al. (2020) - REALM
7. Izacard et al. (2022) - Atlas
8. Jin et al. (2019) - PubMedQA数据集
9. Ben Abacha & Demner-Fushman (2019) - MedQuAD数据集
10. Ben Abacha et al. (2019) - MEDIQA2019挑战赛
11. Ben Abacha et al. (2017) - LiveMedQA2017数据集
12. Zhu et al. (2020) - MASH-QA数据集
13. Chiang et al. (2023) - Vicuna模型
14. Wang (2023) - Alpaca-LoRA
15. OpenAI (2023a) - ChatGPT
16. Han et al. (2023) - MedAlpaca
17. Diao et al. (2023) - Robin-medical
18. Brown et al. (2020) - GPT-3
19. Touvron et al. (2023) - LLaMA
20. OpenAI (2023b) - GPT-4
21. Phan et al. (2021) - SciFive (T5 for biomedical)
22. Lin (2004) - ROUGE评分
23. Lee et al. (2021) - 评估指标与人类判断的弱相关性研究
24. Zhou et al. (2021) - 评估指标研究
25. Yin et al. (2023) - Surface realization vs. inherent knowledge gap
26. Burns et al. (2022) - Discovering latent knowledge
27. Kadavath et al. (2022) - LLM的自我评估能力
28. Manakul et al. (2023) - SelfCheckGPT
29. Ouyang et al. (2022) - InstructGPT / RLHF
30. Wei et al. (2021) - Chain-of-thought prompting
31. Tamkin et al. (2021) - Understanding and controlling LLMs
32. McKenna et al. (2023) - Google N-grams作为预训练语料代理
33. Ke et al. (2022) - CTRLEval评估指标
34. Ji et al. (2023) - 幻觉综述（Survey of Hallucination in NLG）

---

## 论文总结

**一句话总结**：本文提出了一种交互式自我反思方法，通过迭代的知识获取-评分-精炼循环，有效减少了LLM在医学问答任务中的幻觉现象，显著提升了答案的事实性、一致性和蕴含性。

**关键创新点**：
1. 首个对多种主流LLM在医学GQA场景下幻觉现象进行系统性分析的工作
2. 提出三循环自我反思架构，充分利用LLM的内在反思能力
3. 方法在不同参数规模（7B-175B）的模型上均展现了良好的泛化能力

**核心启示**：
- LLM具有识别和修正自身错误的能力，关键在于如何有效激发和引导这种能力
- 自我反思作为一种轻量级、无需额外训练的方法，为幻觉问题提供了一种可行的解决思路
- 结合外部知识检索和更强LLM有望进一步提升方法效果

---

*本笔记由 LLM Safety 论文阅读计划自动生成*
*阅读时间：2026年3月30日*
*论文来源：[EMNLP 2023 Findings](https://aclanthology.org/2023.findings-emnlp.123/) | [arXiv:2310.06271](https://arxiv.org/abs/2310.06271)*
