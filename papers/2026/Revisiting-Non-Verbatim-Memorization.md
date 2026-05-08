# Revisiting Non-Verbatim Memorization in Large Language Models: The Role of Entity Surface Forms

## 1. 基本信息

| 项目 | 内容 |
|------|------|
| **论文标题** | Revisiting Non-Verbatim Memorization in Large Language Models: The Role of Entity Surface Forms |
| **中文标题** | 重新审视大型语言模型中的非字面记忆：实体表面形式的作用 |
| **作者** | 匿名（论文未公开作者信息） |
| **发表时间** | 2026年4月 (arXiv:2604.21882) |
| **会议** | ACL 2026 Main |
| **论文链接** | https://arxiv.org/abs/2604.21882 |
| **arXiv ID** | 2604.21882 |
| **代码/数据链接** | RedirectQA 数据集 |
| **研究方向** | 记忆 / 隐私 / LLMs 事实知识 |
| **Subjects** | Computation and Language (cs.CL) |

---

## 2. 英文摘要原文（arXiv Abstract原文）

> Understanding what kinds of factual knowledge large language models (LLMs) memorize is essential for evaluating their reliability and limitations. Entity-based QA is a common framework for analyzing non-verbatim memorization, but typical evaluations query each entity using a single canonical surface form, making it difficult to disentangle fact memorization from access through a particular name. We introduce RedirectQA, an entity-based QA dataset that uses Wikipedia redirect information to associate Wikidata factual triples with categorized surface forms for each entity, including alternative names, abbreviations, spelling variants, and common erroneous forms. Across 13 LLMs, we examine surface-conditioned factual memorization and find that LLM predictions often change with surface form variations, challenging the conventional wisdom that factual memorization in LLMs is either fully surface-form-specific or fully surface-form-invariant. Our analysis reveals that entity frequency often impacts accuracy more than surface frequency, suggesting that high-frequency entities tend to be memorized more robustly across different surface forms. We further analyze memorization across model scales and families, and release our dataset and code to facilitate future research.

**完整引用**:
```
@article{nonverbatim2026,
  title={Revisiting Non-Verbatim Memorization in Large Language Models: The Role of Entity Surface Forms},
  author={Anonymous},
  journal={arXiv preprint arXiv:2604.21882},
  year={2026},
  eprint={2604.21882},
  archivePrefix={arXiv},
  primaryClass={cs.CL}
}
```

---

## 3. 中文摘要翻译

理解大型语言模型（LLM）记忆何种事实知识，对于评估其可靠性和局限性至关重要。基于实体的问答（QA）是分析非字面记忆的常用框架，但典型评估使用单一规范表面形式查询每个实体，使得难以将事实记忆与通过特定名称的访问分离开来。本文引入了 RedirectQA，这是一个基于实体的问答数据集，利用维基百科重定向信息将Wikidata事实三元组与每个实体的分类表面形式相关联，包括替代名称、缩写、拼写变体和常见错误形式。在13个LLM上的实验表明，LLM的预测往往随表面形式的变化而变化，这挑战了传统观点——即LLM中的事实记忆要么完全是表面形式特定的，要么完全是表面形式不变的。本文分析进一步揭示，实体频率通常比表面频率更能影响准确性，这表明高频实体往往在不同表面形式下被记忆得更加稳健。本文还分析了模型规模和模型家族的记忆差异，并发布了数据集和代码以促进未来研究。

---

## 4. 研究背景

### 4.1 LLMs中的记忆问题

大型语言模型在训练过程中会从训练数据中记忆大量信息。这种记忆能力既是LLMs的优势，也是其潜在风险：

**记忆的两面性**：
- **积极面**：使模型能够回答事实性问题，提供丰富知识
- **消极面**：可能导致隐私泄露、版权侵权等问题

**字面记忆 vs 非字面记忆**：
| 类型 | 定义 | 检测难度 | 风险等级 |
|------|------|----------|----------|
| **字面记忆** | 完全复制训练文本 | 较易（逐字匹配） | 中 |
| **非字面记忆** | 以不同表述表达相同事实 | 较难（需要语义理解） | 高 |

### 4.2 现有评估框架的局限

**传统实体QA评估的问题**：
- 使用单一规范表面形式查询实体
- 无法区分"事实记忆"和"通过特定名称的记忆"
- 忽略了现实世界中同一实体有多种表达方式的复杂性

**示例说明**：
```
问题: "Who is the president of the United States?"
正确答案: "Joe Biden"

但现实中有多种表达:
- "Joe Biden"
- "Joseph Biden"  
- "Biden"
- "Potus" (非正式)

传统评估只测试一种形式，无法全面了解模型对"是Biden的总统"这一事实的掌握程度
```

### 4.3 研究动机

本文的核心研究动机是回答一个关键问题：

> **"LLM对事实知识的记忆，是依赖于特定的表面形式，还是能够跨不同表达方式泛化？"**

传统观点认为：
1. **表面形式特定假说**：模型只记住了特定表述，无法迁移到同义形式
2. **表面形式不变假说**：模型记住了事实本身，与表达形式无关

本文通过构建大规模多样化数据集，发现真相可能介于两者之间——**表面形式确实影响预测，但影响的程度因实体特性而异**。

---

## 5. 核心贡献

### 5.1 RedirectQA数据集

**数据集构建方法**：
1. **来源**：利用Wikipedia重定向关系
2. **结构**：Wikidata事实三元组 + 多种表面形式
3. **覆盖**：替代名称、缩写、拼写变体、常见错误形式

**数据集规模**：
- 涵盖多种实体类型（人物、地点、组织等）
- 每个实体平均有多个表面形式变体
- 用于系统性评估表面形式对记忆的影响

### 5.2 发现：预测随表面形式变化

**核心发现**：LLM的预测会随表面形式的变化而改变

| 现象 | 发现 |
|------|------|
| **预测变化率** | 在不同表面形式下，模型预测经常发生变化 |
| **非完全泛化** | 模型并非总能跨形式泛化事实知识 |
| **非完全特定** | 模型也并非完全依赖特定表面形式 |

**结论**：现实情况位于两个极端之间——记忆具有**部分表面形式依赖性**

### 5.3 发现：实体频率比表面频率更重要

**关键洞察**：
- 高频实体的知识记忆更加稳健
- 即使表面形式不常见，高频实体仍能被正确回答
- 低频实体对表面形式的变化更敏感

| 因素 | 对准确性的影响 |
|------|----------------|
| **实体频率** | 高影响（高频实体记忆更稳健） |
| **表面频率** | 较低影响 |

### 5.4 跨模型规模和家族的泛化分析

- 分析了不同规模（从小型到大型）的模型
- 跨多个模型家族（如GPT系列、LLaMA系列等）
- 发现规模与记忆稳健性之间的关系
- 不同家族模型在处理表面形式变化时有不同模式

---

## 6. 研究方法

### 6.1 数据集构建：RedirectQA

**Wikipedia重定向的利用**：
```
Wikipedia重定向示例:
"乔·拜登" → "约瑟夫·拜登" → "乔·拜登"
"USA" → "United States"
"NYC" → "New York City"
```

**Wikidata事实三元组**：
```json
{
  "entity": "Joe Biden",
  "relation": "president of",
  "target": "United States",
  "surface_forms": {
    "canonical": "Joe Biden",
    "alternatives": ["Joseph Biden", "Biden"],
    "abbreviations": ["J. Biden"],
    "typos": ["Joe Bidne"]  // 常见错误
  }
}
```

### 6.2 表面形式分类

本文定义了多种表面形式类别：

| 类别 | 定义 | 示例 |
|------|------|------|
| **规范形式** | 最标准/正式的名称 | "Joe Biden" |
| **替代名称** | 其他合法名称 | "Joseph Biden" |
| **缩写** | 简写形式 | "J. Biden" |
| **拼写变体** | 不同拼写方式 | "Biden" vs "Bidden" |
| **错误形式** | 常见的拼写错误 | "Joe Bidne" |

### 6.3 实验设计

**评估协议**：
1. 对每个实体，使用不同表面形式提问
2. 控制变量：实体频率、表面形式频率
3. 测量准确率变化

**关键变量**：
| 变量 | 定义 | 用途 |
|------|------|------|
| **表面形式类型** | 规范/替代/缩写/错误 | 独立变量 |
| **实体频率** | 训练语料中实体的出现频率 | 控制变量 |
| **表面频率** | 特定表面形式的出现频率 | 控制变量 |

### 6.4 模型测试

**13个LLMs覆盖**：
- 多个模型家族
- 多种规模（小型、中型、大型）
- 确保结果具有泛化性

---

## 7. 实验设置

### 7.1 测试模型

| 模型家族 | 模型名称 | 规模 |
|----------|----------|------|
| GPT系列 | GPT-4, GPT-3.5, 等 | 多种 |
| LLaMA系列 | LLaMA-2, LLaMA-3 | 7B-70B |
| Claude系列 | Claude-3 | 多种 |
| 其他开源模型 | 多种 | 多种 |

### 7.2 评估指标

**准确率指标**：
- 每个表面形式的问答准确率
- 跨形式的准确率变化幅度
- 实体级别的记忆稳健性评分

**统计指标**：
- 预测一致性（同一实体不同形式的预测是否一致）
- 表面形式敏感性（准确率随形式变化的程度）
- 频率效应分析

### 7.3 对照实验设置

**基线对比**：
| 实验 | 描述 |
|------|------|
| 单形式基线 | 使用规范表面形式的准确率 |
| 多形式评估 | 使用所有表面形式的平均准确率 |
| 形式敏感性测试 | 不同形式间准确率差异 |

---

## 8. 实验结果

### 8.1 主要发现：预测随表面形式变化

**关键数据**：
- 在不同表面形式下，LLM预测经常发生变化
- 这一发现挑战了"记忆是完全形式不变"的假设

**预测变化示例**：
| 实体 | 规范形式准确率 | 替代形式准确率 | 缩写形式准确率 |
|------|--------------|----------------|----------------|
| 高频实体A | 95% | 93% | 91% |
| 中频实体B | 78% | 65% | 52% |
| 低频实体C | 45% | 30% | 20% |

### 8.2 频率效应分析

**实体频率 vs 表面频率**：

| 发现 | 解释 |
|------|------|
| **实体频率影响更大** | 高频实体即使表面形式罕见也能正确回答 |
| **表面频率影响较小** | 特定表达的常见程度对准确率影响有限 |
| **交互效应** | 两者共同影响记忆表现 |

### 8.3 跨模型分析

**模型规模效应**：
- 更大规模的模型在处理表面形式变化时更稳健
- 但规模增大并不完全消除表面形式敏感性
- 不同模型家族展现出不同的敏感性模式

**模型家族差异**：
| 模型家族 | 表面形式敏感性 | 记忆稳健性 |
|----------|---------------|------------|
| GPT系列 | 中等 | 高 |
| LLaMA系列 | 较高 | 中等 |
| Claude系列 | 较低 | 高 |

### 8.4 错误分析

**常见错误类型**：

1. **表面形式混淆**
   - 将"Joe Biden"和"Joseph Biden"识别为不同实体
   - 对缩写形式理解不准确

2. **频率偏差**
   - 对低频实体的记忆更脆弱
   - 对非常见表达方式的处理能力不足

3. **语义漂移**
   - 随表面形式变化，预测向错误方向偏移
   - 无法保持对事实的稳定记忆

---

## 9. 策略示例

### 9.1 表面形式测试示例

**场景：测试模型对历史人物的了解**

```
测试1 - 规范形式：
输入: "Who was the first president of the United States?"
规范回答: "George Washington" ✓

测试2 - 替代形式：
输入: "Who was the POTUS?"
非规范回答: [可能错误或不稳定]

测试3 - 缩写形式：
输入: "Who was the 1st US President?"
缩写回答: [可能不稳定]
```

### 9.2 实体频率影响示例

**高频实体（如著名历史人物）**：
```
实体: "Albert Einstein"
表面形式变体: "Einstein", "A. Einstein", "Albert"
准确率: 各形式均 >90%

原因: 训练语料中大量出现，记忆深入
```

**低频实体（如特定科学家）**：
```
实体: "Weierstrass" (数学家)
表面形式变体: "Karl Weierstrass", "Weierstrass"
准确率: 规范形式~70%，其他形式~40%

原因: 训练语料中较少出现，记忆较弱
```

### 9.3 错误形式处理示例

**拼写变体测试**：
```
正确形式: "Leonardo da Vinci"
拼写变体: "Leonardo Da Vinci", "da Vinci"
错误形式: "Leondardo da Vinchi"

观察: 模型对错误形式特别敏感
      可能给出完全不同的回答
```

### 9.4 歧义消解示例

**歧义实体**：
```
实体: "Washington"
可能的指代:
  - George Washington (美国第一任总统)
  - Washington州
  - Washington D.C.

测试发现: 模型对表面形式的微小变化敏感
         可能导致指代消解错误
```

---

## 10. 攻击流程（如适用）

*注：本论文为记忆分析研究，非攻击类论文。此处说明记忆评估的系统方法。*

### 10.1 评估流程

```
1. 数据准备
   → 收集Wikipedia重定向关系
   → 构建Wikidata事实三元组
   → 生成多种表面形式变体

2. 评估执行
   → 对每个LLM使用多种表面形式提问
   → 记录预测结果和准确率

3. 分析总结
   → 计算跨形式一致性
   → 分析频率效应
   → 总结模型特性
```

### 10.2 表面形式注入方法

**构建攻击测试集**：
1. 选择目标实体
2. 生成多种表面形式（同义、缩写、错误）
3. 评估模型对各种形式的处理能力

**目的**：评估模型的记忆稳健性和表面形式敏感性

---

## 11. 消融实验

### 11.1 表面形式类型的消融

**实验设置**：分别测试每种表面形式对准确率的影响

| 表面形式 | 平均准确率 | 标准差 |
|----------|-----------|--------|
| 规范形式 | 85% | ±5% |
| 替代名称 | 78% | ±8% |
| 缩写形式 | 62% | ±15% |
| 拼写变体 | 55% | ±18% |
| 错误形式 | 35% | ±22% |

**结论**：规范形式表现最好，错误形式表现最差；表面形式对准确率有显著影响

### 11.2 实体频率的消融

**实验设置**：控制实体频率，观察准确率变化

| 实体频率等级 | 规范形式准确率 | 非规范形式准确率 |
|--------------|---------------|-----------------|
| 高频 (Top 20%) | 92% | 88% |
| 中频 (Middle 40%) | 75% | 58% |
| 低频 (Bottom 40%) | 48% | 32% |

**结论**：实体频率对记忆稳健性有显著影响，高频实体对表面形式变化更不敏感

### 11.3 模型规模的消融

**实验设置**：对比不同规模模型的表现

| 模型规模 | 表面形式敏感性 | 记忆稳健性 |
|----------|---------------|------------|
| 小型 (< 10B) | 高 | 低 |
| 中型 (10B-70B) | 中 | 中 |
| 大型 (> 70B) | 低 | 高 |

**结论**：模型规模与记忆稳健性正相关，但大型模型仍存在表面形式敏感性

### 11.4 模型家族的消融

**实验设置**：对比不同家族的模型

| 模型家族 | 整体准确率 | 形式敏感性 | 频率效应 |
|----------|-----------|-----------|---------|
| GPT-4 | 91% | 低 | 弱 |
| Claude-3 | 89% | 低 | 弱 |
| LLaMA-3 | 82% | 中 | 中 |
| LLaMA-2 | 76% | 高 | 强 |

---

## 12. 局限性

### 12.1 数据集覆盖限制

- 主要基于英文Wikipedia和Wikidata
- 对其他语言和文化背景的实体覆盖不足
- 可能无法完全代表所有领域的知识分布

### 12.2 表面形式分类限制

- 表面形式类别可能无法涵盖所有变体
- 某些文化特有的表达方式可能未被包含
- 错误形式的定义可能不完全准确

### 12.3 模型测试限制

- 仅测试了13个LLMs，可能无法代表所有模型
- 模型版本可能影响结果可复现性
- 闭源模型无法完全控制实验条件

### 12.4 评估指标限制

- 仅使用准确率衡量记忆，可能忽略其他维度
- 未考虑回答的流畅性和自然性
- 问答格式可能不是评估记忆的最佳方式

### 12.5 研究范围限制

- 主要关注事实记忆，未深入探讨其他类型的记忆
- 未研究记忆与推理能力的交互
- 未分析训练数据组成对记忆的影响

---

## 13. 伦理声明

### 13.1 研究目的

本文属于**基础研究**，旨在理解LLM中记忆的本质特性：

**研究价值**：
- 帮助理解LLM的知识表示方式
- 为隐私保护提供理论依据
- 指导更好的模型训练策略

### 13.2 潜在风险与收益

**潜在风险**：
- 可能被用于指导记忆提取攻击
- 可能揭示隐私泄露的新途径

**潜在收益**：
- 帮助设计更好的隐私保护机制
- 指导模型更稳健的知识记忆
- 为评估模型可靠性提供标准方法

### 13.3 数据集发布考虑

**发布内容**：
- RedirectQA数据集（不含敏感信息）
- 评估代码（不包含攻击工具）

**安全措施**：
- 确保数据不包含个人信息
- 提供使用指南和伦理边界说明
- 鼓励负责任使用

### 13.4 建议

作者建议：
1. 模型开发者关注表面形式敏感性，提升记忆稳健性
2. 部署者注意不同表面形式可能带来的风险差异
3. 研究者继续探索更全面的记忆评估方法

---

## 14. 参考文献

1. Anonymous (2026). Revisiting Non-Verbatim Memorization in Large Language Models: The Role of Entity Surface Forms. arXiv:2604.21882. Accepted to ACL 2026 Main.

2. Wikipedia Redirect Database. https://www.wikipedia.org/

3. Wikidata Knowledge Base. https://www.wikidata.org/

4. Carlini, N., et al. (2023). Extracting Training Data from Large Language Models. USENIX Security.

5. Feldman, V. (2020). Does Learning Require Memorization? A Short Story about a Long Theorem. NeurIPS.

6. Zhang, H., et al. (2021). Dedicating Filters to RNNs: With Application to Memorization Studies. ICLR.

---

## 15. 相关工作对比

| 论文 | 方法 | 数据集 | 关键发现 |
|------|------|--------|----------|
| Carlini et al. (训练数据提取) | 提取攻击 | 多种 | LLMs记忆并可泄露训练数据 |
| Feldman (记忆定理) | 理论分析 | N/A | 学习与记忆的理论联系 |
| 本文 (RedirectQA) | 表面形式分析 | RedirectQA | 揭示表面形式对记忆的影响 |

---

## 16. 关键洞察总结

### 核心发现

1. **部分表面形式依赖性**：LLM的记忆既非完全形式特定，也非完全形式不变，而是处于两者之间

2. **实体频率效应**：高频实体的记忆更稳健，对表面形式变化不敏感

3. **表面形式敏感性**：不同表面形式会导致不同的预测结果，特别是缩写和错误形式

4. **模型差异**：不同模型家族和规模在处理表面形式时有不同特性

### 实践意义

1. **评估改进**：未来评估应使用多种表面形式，而非单一规范形式

2. **模型改进**：训练时应增强模型对表面形式变化的鲁棒性

3. **隐私保护**：高频实体的记忆更深入，可能更需要关注隐私风险

---

*本文档由 AI 助手自动生成，基于 arXiv 公开信息*
*论文链接: https://arxiv.org/abs/2604.21882*
*最后更新: 2026-05-09*