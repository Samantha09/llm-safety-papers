# ESG-Bench: Benchmarking Long-Context ESG Reports for Hallucination Mitigation

## 基本信息

- **论文标题**: ESG-Bench: Benchmarking Long-Context ESG Reports for Hallucination Mitigation
- **作者**: Siqi Sun, Ben Peng Wu, Mali Jin, Peizhen Bai, Hanpei Zhang, Xingyi Song
- **机构**: University of Sheffield, UK
- **发表会议**: AAAI 2026 (CCF-A类)
- **arXiv链接**: https://arxiv.org/abs/2603.13154
- **代码仓库**: https://github.com/GateNLP/ESG_Bench
- **发表时间**: 2026年3月

---

## 研究背景

### ESG报告的重要性
- ESG（环境、社会、治理）报告已成为企业可持续发展的关键框架
- 许多地区已将ESG披露作为法律要求（如欧盟的企业可持续发展报告指令）
- ESG报告在合规性和利益相关者评估长期绩效方面发挥关键作用

### 现有挑战
1. **第三方评级机构问题**: Sustainalytics和MSCI等机构的评分方法不透明、不一致
2. **报告复杂性**: ESG报告长度长、内容复杂，难以可靠地自动化分析
3. **LLM部署挑战**:
   - 企业可能存在"漂绿"行为（夸大环保举措）
   - ESG报告富含定性数据，需要深度语境理解
   - 涉及多模态处理（文本、表格、图形）
   - 长文档检索和分析困难

### LLM幻觉问题
- LLM在文档解析、检索和跨章节理解方面存在局限
- 依赖可能与ESG报告事实内容冲突的参数化知识
- 导致两类幻觉：
  - **Additive Hallucinations**: 引入不支持的信息
  - **Omissive Hallucinations**: 尽管有证据但仍未能回答

---

## 核心贡献

### 1. Benchmark Construction
- 提出ESG-Bench基准数据集，专门用于ESG报告的长上下文QA和幻觉缓解
- 首个支持ESG领域幻觉系统性评估和针对性缓解的结构化资源

### 2. Task-Specific Strategy for Hallucination Mitigation
- 开发基于任务特定CoT提示和CoT注释推理轨迹的微调方法
- 显著提高事实基础，减少幻觉输出

### 3. Empirical Evaluation
- 在ESG-Bench上微调和评估多个SOTA LLM
- 比较幻觉缓解性能在ESG和现有QA基准上的表现
- 揭示ESG分析中长上下文推理的独特挑战

---

## 研究方法

### ESG-Bench构建流程

#### 1. ESG报告和问题收集
**报告收集**:
- 来源: ResponsibilityReports.com（公开的企业可持续发展披露数据库）
- 涵盖行业: 金融、能源、技术、医疗保健、消费品、制造业等

**问题收集**:
- 来源:
  - 学术研究（Mishra et al. 2024a; Parikh and Penfield 2024等）
  - 国际非营利组织（Carbon Disclosure Project, Caverion, Invest Europe）
  - ChatGPT生成的问题
- 分类: 按ESG三大支柱分类（环境、社会、治理）
- 总计: 270个问题

#### 2. 模型指令设计
响应格式包含三个关键元素:
1. **Answer**: 生成的回答
2. **Page Number**: 来源页面引用
3. **Format**: 输出类型（文本、图形、表格）

设计考虑四个方面:
1. **Question Diversity**: 多样化问题模板评估幻觉行为
2. **Domain-specific Selection**: 区分通用问题和行业特定问题
3. **Expert Consultation**: ESG领域专家手动审核问题池
4. **Iterative Refinement**: 多轮修订和专家反馈

#### 3. 人工标注
**标注员招募**:
- PhD级别学生，专业为经济学、可持续发展或相关领域
- 熟悉GRI（全球报告倡议）标准

**标注流程**:
- 每个回答由两名标注员独立审核
- 标签类别:
  - **Correct**: 完全由上下文支持
  - **Hallucination**: 包含虚构或不受来源支持的信息
  - **Incomplete**: 部分准确但缺少关键信息
  - **Answer Not Found**: 模型返回"未提供"尽管有有效来源答案

**冲突解决**:
- 标注员一致时直接定稿
- 不一致时由第三名标注员通过多数投票解决

**标注员一致性**:
- 使用Cohen's Kappa统计量
- Group 3: 86.67%（近乎完美一致）
- Group 1: 68.89%（实质性一致）
- Group 2: 73.33%（实质性一致）

### 数据集统计

#### Report-based Dataset
- 270个QA实例，来自94份独特ESG报告（2020-2024年）
- 标签分布:
  - 正确: 46.7%
  - 不完整: 34.8%
  - 未找到答案: 3.0%（遗漏性幻觉）
  - 事实性幻觉: 15.6%

#### Hallucination Mitigation Task Dataset
- 背景段落长度: 最大46,562 tokens，平均2,604 tokens
- 回答长度: 3-3,362 tokens，平均614 tokens
- 总计: 1,358个正确回答，25,516个幻觉回答
  - 上下文不支持: 21,724个
  - 事实错误: 3,706个

---

## 幻觉缓解策略

### 三阶段方法

#### Phase 1: Supervised Fine-tuning with Contextual Grounding
- 在ESG QA数据集上微调LLM
- 每个实例包含报告上下文、问题和人工标注答案
- 鼓励模型关注显式文本证据
- 局限性: 证据模糊或不完整时仍可能产生过度自信的输出

#### Phase 2: CoT Prompting and Fine-tuning

**Two-step CoT**:
1. 确定报告是否提供问题答案: {answerable}
2. 基于推理，正确答案应为: {answer}

**Four-step CoT**:
1. 识别问题中提到的关键主题或实体: {topic}
2. 在报告中搜索与该主题相关的句子或段落: {report summary}
3. 确定报告是否提供问题答案: {answerable}
4. 基于推理，正确答案应为: {answer}

**CoT-based Fine-tuning**:
- 在带有显式CoT推理路径的QA对子集上微调模型
- 每个示例包含中间推理步骤
- 鼓励模型内化结构化决策

---

## 实验设置

### 评估模型
- Llama-3.2-3B Instruct
- Gemma-2-2B-it
- Mistral-7B-Instruct-v0.3

### 数据集
1. **ESG-Bench** (本文提出)
2. **BioASQ**: 生物医学QA数据集
3. **HaluEval**: 专门评估LLM幻觉的基准

### 实现细节
- GPU: NVIDIA GH200 480GB
- 框架: HuggingFace transformers和trl
- 优化器: AdamW
- 学习率: 2e-5
- 训练轮数: 20 epochs
- 批次大小: 32

### 评估指标
1. **WA Accuracy**: 上下文中存在答案时的正确预测比例
2. **WoA Accuracy**: 文档中无答案时的正确预测比例（"未提供"）
3. **Balanced Accuracy**: WA和WoA准确率的平均值
4. **F1 Score**: 精确率和召回率的权衡

---

## 实验结果

### 主要发现

| 模型 | 方法 | WA Acc | WoA Acc | Balanced Acc | F1 |
|------|------|--------|---------|--------------|-----|
| Llama-3.2-3B | 无微调 | 0.72 | 0.45 | 0.59 | 0.58 |
| Llama-3.2-3B | SFT | 0.78 | 0.62 | 0.70 | 0.69 |
| Llama-3.2-3B | CoT (2-step) | 0.81 | 0.71 | 0.76 | 0.75 |
| Llama-3.2-3B | CoT (4-step) | 0.83 | 0.74 | 0.79 | 0.78 |
| Gemma-2-2B | 无微调 | 0.68 | 0.42 | 0.55 | 0.54 |
| Gemma-2-2B | SFT | 0.75 | 0.58 | 0.67 | 0.66 |
| Gemma-2-2B | CoT (4-step) | 0.80 | 0.69 | 0.75 | 0.74 |
| Mistral-7B | 无微调 | 0.74 | 0.48 | 0.61 | 0.60 |
| Mistral-7B | SFT | 0.80 | 0.65 | 0.73 | 0.72 |
| Mistral-7B | CoT (4-step) | 0.85 | 0.76 | 0.81 | 0.80 |

### 关键观察
1. **CoT微调显著提升性能**: 4步CoT方法在所有模型和数据集上表现最佳
2. **平衡性能**: 多步推理产生更平衡的模型，能够处理可回答和不可回答的查询
3. **跨数据集迁移**: CoT方法的收益可迁移到ESG领域之外的现有QA基准
4. **GPT-4o自评估一致性**: 
   - GPT-4o初始输出与人工标注: 81.5%一致
   - GPT-4o事后判断与人工标注: 80.4%一致
   - GPT-4o内部一致性: 83.7%

---

## 策略示例

### 标准提示 vs CoT提示

**标准提示**:
```
背景: [ESG报告段落]
问题: 该公司在2023年的碳排放量是多少？
回答: [直接生成答案]
```

**Two-step CoT提示**:
```
背景: [ESG报告段落]
问题: 该公司在2023年的碳排放量是多少？

请按以下步骤回答:
1. 确定报告是否提供问题答案: [是/否]
2. 基于推理，正确答案应为: [答案或"未提供"]
```

**Four-step CoT提示**:
```
背景: [ESG报告段落]
问题: 该公司在2023年的碳排放量是多少？

请按以下步骤回答:
1. 识别问题中提到的关键主题或实体: [碳排放量、2023年]
2. 在报告中搜索与该主题相关的句子或段落: [相关段落摘要]
3. 确定报告是否提供问题答案: [是/否]
4. 基于推理，正确答案应为: [答案或"未提供"]
```

---

## 消融实验

### CoT步骤数的影响
- 2步CoT相比SFT有显著提升
- 4步CoT相比2步CoT进一步提升，特别是在WoA准确率上
- 更多步骤帮助模型更好地评估证据充分性

### 不同模型的表现
- Mistral-7B表现最佳，但较小的模型（Llama-3.2-3B, Gemma-2-2B）经过CoT微调后也能达到接近的性能
- CoT微调对不同规模的模型都有正面效果

### 跨数据集泛化
- 在ESG-Bench上训练的CoT模型在BioASQ和HaluEval上也表现良好
- 证明方法不仅限于ESG领域，具有通用性

---

## 局限性

1. **数据集规模**: 270个QA实例相对较小，可能无法覆盖所有ESG场景
2. **语言限制**: 主要关注英文ESG报告
3. **行业覆盖**: 虽然涵盖多个行业，但某些特定行业的ESG问题可能代表性不足
4. **模型依赖**: 使用GPT-4o生成初始回答，可能存在偏差
5. **幻觉类型**: 主要关注事实性幻觉，对其他类型幻觉（如逻辑幻觉）覆盖有限

---

## 伦理声明

- 本研究获得谢菲尔德大学研究伦理委员会批准（编号: 064356）
- 所有程序符合机构研究伦理标准
- 使用的ESG报告来自公开数据库

---

## 参考文献

1. Achiam et al. (2023). GPT-4 technical report. arXiv:2303.08774.
2. Ji et al. (2023). Survey of hallucination in natural language generation. ACM Computing Surveys.
3. Wei et al. (2022). Chain-of-thought prompting elicits reasoning in large language models. NeurIPS.
4. Kojima et al. (2022). Large language models are zero-shot reasoners. NeurIPS.
5. Farquhar et al. (2024). Detecting hallucinations in large language models using semantic entropy. Nature.
6. Dubey et al. (2024). The llama 3 herd of models. arXiv:2407.21783.
7. Jiang et al. (2023). Mistral 7b. arXiv:2310.06825.
8. Team et al. (2024). Gemma: open models based on gemini research and technology. arXiv:2403.08295.

---

## 总结

ESG-Bench是首个专门针对ESG报告长上下文QA和幻觉缓解的基准数据集。通过人工标注的幻觉标签和CoT微调策略，论文展示了在ESG这一高风险合规领域减轻LLM幻觉的有效方法。4步CoT方法在多个模型和数据集上均表现出色，证明了结构化推理在提高事实可靠性方面的价值。

**关键词**: ESG报告, 幻觉缓解, 长上下文QA, Chain-of-Thought, 事实可靠性, AAAI 2026
