# Siren's Song in the AI Ocean: A Survey on Hallucination in Large Language Models

## 基本信息

| 属性 | 内容 |
|------|------|
| **论文标题** | Siren's Song in the AI Ocean: A Survey on Hallucination in Large Language Models |
| **作者** | Yue Zhang, Yafu Li, Leyang Cui, Deng Cai, Lemao Liu, Tingchen Fu, Xinting Huang, Enbo Zhao, Yu Zhang, Chen Xu, Yulong Chen, Longyue Wang, Anh Tuan Luu, Wei Bi, Freda Shi, Shuming Shi |
| **机构** | Tencent AI Lab, Soochow University, Zhejiang University, Renmin University, NTU, Toyota Technological Institute |
| **arXiv** | [2309.01219](https://arxiv.org/abs/2309.01219) |
| **GitHub** | [HillZhang1999/llm-hallucination-survey](https://github.com/HillZhang1999/llm-hallucination-survey) |
| **发表时间** | 2023年9月 (v3更新于2025年9月) |
| **方向** | Hallucination（幻觉） |
| **子方向** | Survey, 幻觉检测, 解释, 缓解 |

## 研究背景

### 什么是LLM幻觉

大语言模型（LLMs）虽然在各种下游任务中表现出色，但经常产生"幻觉"——即生成看似合理但实际偏离用户输入、与先前生成的上下文矛盾或与世界知识不符的内容。这种现象严重威胁了LLM在真实场景中的可靠性。

### LLM时代幻觉的新挑战

与传统的NLG设置相比，LLM幻觉面临独特的挑战：

1. **海量训练数据**：LLM预训练使用从网页获取的数万亿token，包含大量伪造、过时或有偏见的信息
2. **LLM的多功能性**：通用LLM需要跨任务、跨语言、跨领域工作，给幻觉的全面评估和缓解带来挑战
3. **错误的不可感知性**：LLM生成的错误信息看起来高度可信，甚至人类难以检测

## 核心贡献

### 1. 提出LLM幻觉的三分类体系

本文将LLM幻觉分为三类：

| 类型 | 定义 | 示例 |
|------|------|------|
| **输入冲突幻觉 (Input-conflicting)** | 生成内容偏离用户输入 | 摘要中将人名"Hill"替换为"Lucas" |
| **上下文冲突幻觉 (Context-conflicting)** | 生成内容与自身先前生成的内容矛盾 | 先说"Silver是现任NBA总裁"，后又说"Stern是总裁" |
| **事实冲突幻觉 (Fact-conflicting)** | 生成内容与已知世界知识矛盾或无法被验证 | 说"Afonso II的母亲是Queen Urraca of Castile"（正确答案是Dulce Berenguer of Barcelona） |

### 2. 全面的评估基准和指标综述

系统梳理了TruthfulQA、FActScore、HaluEval、FACTOR等评估基准及其评估格式（生成式vs判别式）。

### 3. 幻觉来源分析

识别出LLM生命周期四个阶段的幻觉来源：预训练→SFT→RLHF→推理。

### 4. 缓解策略分类

按LLM生命周期阶段组织，对现有幻觉缓解方法进行全面综述。

## 研究方法

### 幻觉分类体系详解

#### 输入冲突幻觉

- **定义**：LLM生成的内容偏离用户的输入（任务指令或任务输入）
- **挑战**：在长上下文场景中特别容易发生
- **示例**：用户上传关于Steve Jobs的段落，问"Jobs的导师返回了日本的哪座寺庙？"，模型回答"Eihei-ji"，但原文中从未提及此信息

#### 上下文冲突幻觉

- **定义**：LLM在生成长文本或多轮响应时自相矛盾
- **原因**：长期记忆能力有限、上下文识别失败
- **示例**：介绍NBA总裁时前后不一致

#### 事实冲突幻觉

- **定义**：生成与 established world knowledge 矛盾的内容
- **重点**：是当前研究的主要焦点（占本文主要讨论篇幅）
- **争议**：未经验证的内容是否都算幻觉——作者主张所有未验证内容都应视为事实冲突幻觉

### 与其他LLM问题的区分

| 问题类型 | 特点 | 与幻觉的区别 |
|----------|------|-------------|
| **歧义性 (Ambiguity)** | 回答模糊，有多种解释 | 不是错误，只是不精确 |
| **不完整性 (Incompleteness)** | 生成内容不完整或碎片化 | 缺少信息但不一定错误 |
| **偏见 (Bias)** | 生成不公平或偏见内容 | 可能是真实的但不公平 |
| **信息不足 (Under-informativeness)** | 回避问题或拒绝回答 | 该说而不说 |

## 实验设置

### 评估基准

#### 按评估格式分类

**生成式评估 (Generation)**
- TruthfulQA：评估LLM响应对问题的真实性
- FActScore：检查LLM生成的传记的事实准确性
- SAFE：使用LLM代理迭代发出Google搜索查询
- SimpleQA：设计有单一明确答案的问题

**判别式评估 (Discrimination)**
- HaluEval：判断陈述是否包含幻觉信息
- FACTOR：评估LLM是否对事实陈述赋予更高可能性

#### 按任务格式分类

1. **问答 (QA)**：TruthfulQA, HaluEval, SimpleQA, SAFE
2. **任务指令 (TI)**：FActScore使用传记介绍指令
3. **文本补全 (TC)**：FACTOR使用维基百科上下文前缀

### 评估指标

| 类型 | 方法 | 优缺点 |
|------|------|--------|
| **人工评估** | 遵循特定原则的手动注释 | 可靠但昂贵且主观 |
| **模型自动评估** | GPT-judge, AlignScore, FactScore | 高效但可能偏差 |
| **规则自动评估** | BLEU, ROUGE, 准确率等 | 适用于特定任务 |

## 实验结果

### 主要发现

1. **事实冲突幻觉是研究重点**：当前benchmark主要评估事实冲突幻觉，因为它对用户最危险
2. **TruthfulQA基准**：GPT-3-6.7B训练出的GPT-judge模型达到90-96%的验证准确率
3. **FActScore**：使用检索+LLaMA-65B评估，在传记生成上评估事实性
4. **HaluEval**：包含52K条指令，用于检测幻觉分布

### 模型能力差异

- **GPT-4** 在识别不可回答或不可知问题上与人类仍有显著差距
- LLMs倾向于过度自信——对正确答案和错误答案的置信度分布相似
- 在Head-to-Tail基准上，LLM对头部（popular）实体表现较好，对躯干和尾部实体表现不佳

## 策略示例

### 缓解方法分类（按LLM生命周期）

#### 预训练阶段

- 数据过滤和清洗
- 知识增强训练

#### SFT阶段

- 指令微调时避免幻觉示范

#### RLHF阶段

- 避免过度优化导致sycophancy
- 调整奖励模型减少幻觉

#### 推理阶段

- 解码策略优化（如greedy vs sampling）
- Self-Correction：LLM自我纠正
- External Knowledge Retrieval：外部知识检索增强

### 关键技术示例

**AlignScore** (Zha et al., 2023)
- 训练统一函数评估两个文本的事实一致性
- 在7个任务（NLI, QA, 复述等）的大规模数据集上训练

**FActScore** (Min et al., 2023)
1. 使用passage retriever收集相关知识
2. 使用LLaMA-65B判断陈述的真实性
3. 采用micro F1和error rate评估

**FactualityPrompt** (Lee et al., 2022)
- 结合命名实体度量 + 文本蕴含度量

## 攻击流程（不适用）

本文是综述论文，不涉及攻击流程。

## 消融实验

本文是综述论文，主要贡献在于分类和综述，不包含原创的消融实验。

## 局限性

1. **研究焦点偏差**：主要关注事实冲突幻觉，对输入冲突和上下文冲突幻觉的缓解策略讨论相对较少
2. **评估挑战**：自由形式生成的评估本质上是困难的，缺乏确定性参考
3. **快速演进**：LLM领域发展迅速，部分内容可能需要更新
4. **幻觉定义争议**：未验证内容是否都应算作幻觉存在争议
5. **人类参与 vs 自动方法**：人类标注确保质量但成本高，完全自动构建方法可以及时更新但质量可能不稳定

## 伦理声明

本文为学术综述论文，无直接伦理问题。但需要注意：

1. 论文提到了LLM可能产生有害内容（如虚假医疗诊断）
2. 强调了幻觉在实际应用中的潜在风险（医疗、法律等领域）
3. 呼吁研究社区关注幻觉问题的解决

## 参考文献（代表性）

1. Brown et al. (2020) - In-context learning
2. Ouyang et al. (2022) - RLHF / InstructGPT
3. Lin et al. (2021) - TruthfulQA
4. Min et al. (2023) - FActScore
5. Li et al. (2023) - HaluEval
6. Muhlgay et al. (2023) - FACTOR
7. Ji et al. (2023) - Survey of Hallucination in NLG
8. Wei et al. (2022) - Chain-of-Thought
9. Kadavath et al. (2022) - LLM self-evaluation
10. Ren et al. (2023) - Knowledge boundary

---

## 总结

**Siren's Song** 是一篇关于LLM幻觉的综合综述，首次系统性地将LLM幻觉分为三类（输入冲突、上下文冲突、事实冲突），并从预训练到推理的完整生命周期角度综述了幻觉的来源和缓解策略。该论文对于理解LLM安全问题、特别是可靠性问题具有重要参考价值。

**GitHub**: https://github.com/HillZhang1999/llm-hallucination-survey

**推荐指数**: ⭐⭐⭐⭐⭐
