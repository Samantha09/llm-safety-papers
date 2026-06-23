# A Holistic Approach to Undesired Content Detection in the Real World

## 论文信息

| 属性 | 内容 |
|------|------|
| 标题 | A Holistic Approach to Undesired Content Detection in the Real World |
| 作者 | Todor Markov*, Chong Zhang*, Sandhini Agarwal, Tyna Eloundou, Teddy Lee, Steven Adler, Angela Jiang, Lilian Weng* (*同等贡献) |
| 机构 | OpenAI |
| 会议 | AAAI-23 (Oral Presentation) |
| arXiv | 2208.03274v2 [cs.CL] |
| 发表日期 | 2023年2月14日 (最终版) |
| 论文链接 | https://arxiv.org/abs/2208.03274 |
| 代码/数据 | https://github.com/openai/moderation-api-release |

---

## 1. 基本信息

本文是OpenAI团队发表的一篇关于实际场景中不良内容检测的系统性论文。该研究提出了一个完整的内容审核解决方案，覆盖从分类体系设计、数据质量控制、主动学习、半监督域适应到模型探测和红队测试的全流程。论文发表在AAAI 2023会议并获得Oral presentation荣誉。

### 1.1 研究问题

构建一个能够检测多种不良内容类别的鲁棒分类系统，具体包括：
- 性相关内容（Sexual content）
- 仇恨内容（Hateful content）
- 暴力内容（Violence）
- 自残内容（Self-harm）
- 骚扰内容（Harassment）

### 1.2 核心挑战

1. **缺乏统一标准**：不良内容的定义和分类缺乏共识
2. **数据分布偏移**：学术数据集与实际生产环境存在显著差异
3. **稀有事件问题**：某些类别（如自残）在实际流量中极其罕见（仅0.04%）
4. **标注主观性**：不同标注者因社会文化背景不同产生分歧
5. **模型偏差**：深度学习模型容易过拟合常见短语或模板

### 1.3 开源贡献

- 数据集发布：包含来自CommonCrawl和模型生成数据的公开标注样本
- 模型可用：通过OpenAI Moderation API提供服务

---

## 2. 英文摘要原文

**Abstract:**

"We present a holistic approach to building a robust and useful natural language classification system for real-world content moderation. The success of such a system relies on a chain of carefully designed and executed steps, including the design of content taxonomies and labeling instructions, data quality control, an active learning pipeline to capture rare events, and a variety of methods to make the model robust and to avoid overfitting. Our moderation system is trained to detect a broad set of categories of undesired content, including sexual content, hateful content, violence, self-harm, and harassment. This approach generalizes to a wide range of different content taxonomies and can be used to create high-quality content classifiers that outperform off-the-shelf models."

**Full Introduction Excerpt:**

"Recent advances in deep learning have accelerated the adoption of language models for socioeconomically valuable tasks in the real world (Devlin et al. 2019; Brown et al. 2020; Cohen et al. 2022). Both the systems' builders and its users may benefit from a responsible deployment approach that includes moderating the models' outputs: First, model providers may want assurances that the models will not produce content that is disallowed by their policies. Second, customers of these models sometimes require control over content to mitigate the impact of sensitive use cases or to reduce brand risk. A principled, robust, and efficient moderation solution can track and measure the model inputs and outputs to ensure safety standards. It can also provide fine-grained control to enable use cases with sensitive needs, such as educational applications. We believe that a strong undesired content classifier lays the foundation for building safer AI systems in the wild, as it enables the capacity of moderating, evaluating, and guiding the models towards safer behavior."

**Key Conclusions from the Paper:**

"Based on our experimentation, we find the following conclusions to be especially noteworthy:
- Detailed instructions and quality control are needed to ensure data quality.
- Active learning is a necessity (up to 22× improvement for rare events).
- Use public datasets with care (can hurt performance at later stages when proper data is available).
- Imbalanced training data can lead to incorrect generalization.
- Mistakes in data will happen and need to be managed."

---

## 3. 中文摘要翻译

**摘要翻译：**

本文提出了一种构建鲁棒且实用的自然语言分类系统用于实际内容审核的整体方法。这类系统的成功依赖于一系列精心设计和执行的步骤，包括：内容分类体系的设计与标注说明、数据质量控制、捕获稀有事件的主动学习流程，以及多种使模型鲁棒且避免过拟合的方法。我们的审核系统经过训练，能够检测广泛的不良内容类别，包括性相关内容、仇恨内容、暴力、自残和骚扰。该方法能够泛化到多种不同的内容分类体系，可用于创建高质量的内容分类器，其性能优于现成的模型。

**研究背景要点翻译：**

"深度学习的最新进展加速了语言模型在现实世界中的经济价值应用（Devlin et al. 2019; Brown et al. 2020; Cohen et al. 2022）。系统构建者和用户都能从负责任的部署方法中获益，这种方法包括对模型输出的审核：首先，模型提供商可能需要确保模型不会产生违反其政策的内容。其次，模型的客户有时需要对内容进行控制，以减轻敏感用例的影响或降低品牌风险。一个原则性、鲁棒且高效的审核解决方案可以追踪和衡量模型的输入输出，确保安全标准。它还可以提供细粒度控制，使敏感需求的用例（如教育应用）成为可能。我们相信，一个强大的不良内容分类器为构建更安全的AI系统奠定了基础，因为它使审核、评估和引导模型行为更加安全的能力成为可能。"

---

## 4. 研究背景

### 4.1 内容审核的重要性

随着大语言模型（LLM）在各行业的广泛部署，内容审核成为确保AI安全的关键环节。本文的背景可以从以下几个维度理解：

**模型提供商的需求**：AI公司需要确保其模型不会产生违反平台政策的有害内容。GPT系列模型的强大生成能力带来了更大的责任，需要系统性地检测和过滤潜在的有害输出。

**企业客户的需求**：使用AI API的企业客户需要对内容进行控制，以满足合规要求或降低品牌风险。不同行业（教育、医疗、金融）对内容过滤有不同的细粒度需求。

**终端用户的安全**：，特别是在将AI系统部署到面向公众的应用时，需要保护用户免受有害内容的侵扰。

### 4.2 现有工作的局限性

**类别覆盖有限**：现有内容检测工作主要关注毒性（toxicity）、仇恨言论（hate speech）和滥用内容（abusive content），缺乏对自残、多种性相关内容亚类等更广泛类别的系统研究。

**泛化能力不足**：学术数据集（如Jigsaw Toxic Comment、Twitter Hate Speech数据集）与实际生产环境存在显著差异。学术数据往往更短、更正式，而生产环境数据包含更多的few-shot提示词和更长的文本。

**通用性受限**：如Perspective API等现有工具针对特定用例（在线毒性评论审核）进行优化，难以直接迁移到其他内容审核场景。

**标注质量问题**：标注者的主观性、跨文化差异以及缺乏详细的标注指南导致数据质量参差不齐。

### 4.3 本文定位

本文旨在提供构建实际内容审核系统的完整蓝图，覆盖从问题定义、数据采集、模型训练到部署的完整流程。特别关注：
- 稀有事件的处理（某些不良内容在实际流量中极其罕见）
- 数据分布偏移的应对
- 持续迭代改进的机制

---

## 5. 核心贡献

### 5.1 系统性方法论

本文的核心贡献是提出了一个完整的不良内容检测系统构建方法论，而非仅仅关注模型架构本身。主要贡献包括：

**1. 多层级分类体系（Taxonomy）**

论文设计了一个包含5个顶级类别和多个子类别的分类体系：
- **S (Sexual content)**：性相关内容，含S0-S3四个级别，其中S3（未成年人性内容）和S2（非法性行为）被标记为有害
- **H (Hateful content)**：仇恨内容，含H0-H2级别，其中H2（呼吁暴力）和H1（贬损性刻板印象）为有害
- **V (Violence)**：暴力内容，含V0-V2级别，其中V2（极端暴力）和V1（暴力威胁）为有害
- **SH (Self-harm)**：自残内容
- **HR (Harassment)**：骚扰内容

模型的最终输出是8个二分类标签（5个顶级类别 + S3、H2、V2三个严重子类别）。

**2. 主动学习pipeline**

论文设计了高效捕获稀有事件的主动学习策略，综合三种采样方法：
- 随机采样：保持数据分布的一致性
- 阈值采样：从模型得分高于特定阈值的数据中选择
- 不确定性采样：选择模型最不确定的样本（得分接近0.5的）

实验表明，主动学习比随机采样在稀有事件上提升可达22倍。

**3. 数据质量控制框架**

论文系统性地解决了标注质量问题：
- 详细、具体的标注指南设计
- 定期校准会议审阅标注不一致的边界案例
- 审计样本选择策略（优先选择标注为有害的样本和模型得分>50%的样本）
- F-1指标用于评估各分类的数据质量

**4. 合成数据增强**

针对数据不平衡和模型过拟合问题，论文提出：
- 模板生成：从手写模板生成合成数据
- 模型生成：利用LLM零样本/少样本生成训练数据
- 对比数据：使用模板对创建对比样本（如"black women" vs "black blanket"）

### 5.2 域适应技术

**Wasserstein距离引导的域对抗训练（WDAT）**

为解决公开数据集与生产数据分布差异，论文采用WDAT方法：
- 特征提取器：使用Transformer编码器
- 分类头：8个独立的MLP头（每个类别一个）
- 域判别器：学习域不变表示

实验表明，WDAT在数据稀缺的早期阶段效果显著，但在有充足in-distribution数据时效果减弱。

### 5.3 模型探测与红队测试

**关键token探测（Key Tokens Probing）**

使用输入约简技术（input reduction）识别模型过度依赖的token：
- 贪心删除token直到预测得分<0.8
- 平均将样本从722.3字符缩减到15.9字符
- 交叉验证约97%的关键token确实是敏感的

**人工红队（Human Red-teaming）**

系统性地通过人工测试发现模型弱点：
- 发现"#" token导致高仇恨得分（因学术数据集样本过短）
- 发现种族相关token的过度关联问题

---

## 6. 研究方法

### 6.1 数据选择与主动学习（三阶段迭代流程）

**第一阶段：数据筛选**
- 从生产流量中随机采样大量数据
- 掩码处理PII信息
- 使用当前最新审核模型对样本进行评分

**第二阶段：主动学习采样**
聚合三种采样策略的结果：
1. 随机采样：保持分布一致性
2. 阈值采样：选择模型得分>阈值的样本
3. 不确定性采样：选择得分最接近0.5的样本

**第三阶段：重加权与标注**
- 基于元数据统计对样本进行重加权
- 采样权重与样本计数的平方根成正比
- 根据不同阶段调整各子策略的混合比例

### 6.2 标注与质量控制

**标注指南设计原则**
- 尽可能互斥的类别定义，减少歧义
- 大量边界案例的示例
- 定期校准会议统一标注标准

**审计流程**
- 在每个类别中随机选择10个标注为有害的样本 + 10个模型得分>50%的样本
- 计算 auditor-assigned labels 作为 ground truth 的 F-1 分数
- 分指标报告便于识别特定类别的问题

**错误检测方法**
- 交叉验证：定期将训练集分成两部分，训练独立模型互相验证
- token减法分析：识别导致过拟合的常见短语

### 6.3 合成数据生成

**模板方法**
- 手写敏感短语模板（如"[subject] is selfish/foolish/narrow-minded"）
- [subject]可填入真实人口属性（如"Latino"）或随机对象（如"blanket"）
- 对比设置鼓励模型学习正确的特征表示

**模型生成方法**
- 零样本生成：要求模型生成有害/安全内容
- 少样本生成：根据few-shot示例的标签推断

**数据平衡实验发现**
- 添加69k对比合成样本后，仇恨内容平均AUPRC从0.417提升到0.551
- 但大量噪声合成数据（2倍现有训练数据）反而降低模型性能
- 原因：在有充足高质量数据的 regime 下，噪声会干扰学习

### 6.4 域对抗训练

**Wasserstein距离近似**
$$L_d(D_s, D_t) = |E_{x \in D_s} f_d(f_z(x)) - E_{x \in D_t} f_d(f_z(x))|$$

**总体目标（minimax问题）**
$$\min_{\theta_z, \theta_c} \{L_c + \lambda \max_{\theta_d} L_d\}$$

**实现细节**
- 使用绝对值处理初始负loss
- 梯度裁剪 $\theta_d \in [-0.01, 0.01]$ 满足Lipschitz约束
- 平衡系数 $\lambda = 0.01$

### 6.5 模型探测技术

**输入约简方法**
- 对训练数据应用贪心token删除
- 直到预测概率降至0.8以下
- 保留的token被认为是"关键token"

**红队测试**
- 内部人工测试发现未知弱点
- 构建合成数据集修补发现的问题
- 迭代过程持续改进模型鲁棒性

---

## 7. 实验设置

### 7.1 模型架构

**Transformer解码器架构**
- 基础：GPT预训练模型
- 修改：最终输出层替换为8个独立的MLP头
- 每个头的形状：[d_model, 256, 1]
- 独立头设计优于单一深MLP（避免类别间干扰，减少参数量）

**训练超参数**
- 学习率：0.05
- 批量大小：256
- Dropout率：0.1（仅在MLP头中使用）
- 训练轮数：最多3个epoch

### 7.2 评估数据集

**私有测试集**
- 来自生产流量的样本（无法公开分享）

**公开评估集**
- TweetEval：包含"hate"和"offensive"任务
- Stormfront数据集：白人至上主义论坛的仇恨言论
- Jigsaw毒性评论数据集
- Reddit评论数据集（性内容）

### 7.3 基准对比

**Perspective API（Jigsaw）**
- 行业标准的毒性检测API
- 用于对比基线性能

---

## 8. 实验结果

### 8.1 模型性能对比

| Category | Perspective API | Ours |
|----------|-----------------|------|
| Sexual (S) | 0.8709* | **0.9703** |
| Hate (H) | 0.6914 | **0.7968** |
| Violence (V) | 0.5201 | **0.7371** |
| Harassment (HR) | 0.3902* | **0.6191** |
| Self-harm (SH) | - | **0.8070** |
| Sexual/minors (S3) | - | **0.7638** |
| Hateful/threatening (H2) | - | **0.7268** |
| Graphic violence (V2) | - | **0.6061** |

**公开数据集对比**

| Dataset | Task | Perspective API | Ours |
|---------|------|-----------------|------|
| TweetEval | Hate | 0.5961 | **0.6473** |
| TweetEval | Offensive | 0.7919* | **0.7024** |
| Stormfront | Hate | 0.8754 | **0.9053** |
| Reddit | Sexual | 0.8961* | **0.9417** |
| Jigsaw | Toxicity | 0.6644 | **0.6890** |
| Jigsaw | Insult | 0.8814 | **0.8548** |
| Jigsaw | Obscene | 0.9500 | **0.8353*** |
| Jigsaw | Threat | 0.7492 | **0.6144*** |
| Jigsaw | Identity-hate | 0.9769 | **0.9304*** |

注：带*表示基于近似分类映射，不完全公平对比

### 8.2 主动学习效果

**采样效率对比**

| Category | Random Sampling | Active Learning | Multiplier |
|----------|----------------|-----------------|------------|
| Sexual | 1.49% | 25.53% | 17.1× |
| Hate | 0.17% | 3.09% | 18.2× |
| Violence | 0.48% | 9.92% | 20.7× |
| Harassment | 0.55% | 6.41% | 11.7× |
| Self-harm | 0.09% | 1.85% | 20.6× |
| Sexual/minors | 0.24% | 2.42% | 10.1× |
| Hateful/threatening | 0.03% | 0.67% | 22.3× |
| Graphic violence | 0.25% | 4.27% | 17.1× |

**关键发现**：
- 主动学习在所有类别上都实现了10倍以上改进
- 约40%的主动学习采样样本触发至少一个有害标签
- 随机采样仅3.4%样本有任何有害标签
- 经过3轮迭代，所有类别的AUPRC都有显著提升

### 8.3 域对抗训练效果

在不同数据配置下评估WDAT效果：

| Config | Setup | Baseline | DAT |
|--------|-------|----------|-----|
| PUB | 仅公开数据 | - | - |
| SYN | PUB + 69k合成数据 | - | - |
| MIX | SYN + 60k生产数据 | - | - |

**发现**：
- WDAT在数据稀缺的早期阶段（PUB）效果显著
- 随着in-distribution数据增加，WDAT的边际收益递减
- WDAT仍能帮助弱类别（如SH、V2）
- 但对于有充足数据的类别（如H、V），WDAT可能略微降低性能

---

## 9. 策略示例

### 9.1 仇恨内容分类细则

**H2 - 有害/威胁（Undesired）**
- 示例："I want to k1ll all immigrants."
- 示例："Why is it that all immigrants are repulsive?"
- 示例："D3ath to all immigrants."

**H1 - 贬损性刻板印象（Undesired）**
- 传播仇恨性刻板印象的内容

**H0.a - 中性陈述（Not Undesired）**
- 客观提及群体身份的中性陈述

**H0.b - 语境化仇恨言论（Not Undesired）**
- 如引用他人言论进行评论的场景

### 9.2 暴力内容分类细则

**V2 - 极端暴力（Undesired）**
- 详细描写极端暴力场景

**V1 - 暴力威胁或支持（Undesired）**
- 表达暴力意图或支持暴力

**V0 - 语境化暴力描述（Not Undesired）**
- 如新闻报道、小说中的暴力场景描述

### 9.3 模板对比数据示例

论文使用模板对创建对比合成数据：

**有害样本**：
- "Latino is selfish/foolish/narrow-minded"
- "black women is ..."

**安全样本**：
- "Latino is tall/short/..."
- "black blanket is ..."

这种对比设置帮助模型学习：
- 负面描述词 + 群体身份 ≠ 必然仇恨
- 需要更多语境信息才能做出判断

---

## 10. 攻击流程

### 10.1 发现的问题

**1. "#" Token问题**
- 模型对包含"#"的样本预测高仇恨得分
- 原因：学术数据集中很多仇恨样本是短推文，包含#标签

**2. 种族Token过度关联**
- "black" token导致高仇恨得分
- 问题在于区分：
  - "I hate black people!" → 应预测仇恨
  - "I hate black cats!" → 不应预测仇恨

### 10.2 对抗性漏洞

**输入约简发现的问题类型**：

1. **无关符号频率高**
   - 如"."符号贡献预测分数
   - 模型可能学习到与内容无关的模式

2. **长token接近原始样本**
   - 表明模型可能记忆了训练样本

3. **typo和对抗输入处理能力弱**
   - 如"w h o r e s" → "e s"
   - 模型无法正确处理空格插入的变体

### 10.3 缓解策略

**合成数据修补**
- 从手写模板构建数据集
- 利用合成模型生成补充数据
- 调整训练数据分布，确保多种来源文本的正确混合

**迭代红队流程**
- 发现新问题 → 构建合成数据 → 重新训练 → 验证
- 自然形成改进循环

---

## 11. 消融实验

### 11.1 合成数据量影响

| 配置 | 仇恨AUPRC | 说明 |
|------|-----------|------|
| 无合成数据 | 0.417 | 基线 |
| +69k对比合成 | **0.551** | 提升32% |
| +2倍噪声合成 | 下降 | 性能降低 |

**结论**：对比合成数据有效，但噪声合成数据有害

### 11.2 模板设计的作用

**发现**：
- 人口属性 + 负面词（如"black women is selfish"）→ 仇恨
- 随机对象 + 负面词（如"black blanket is selfish"）→ 安全
- 对比设置帮助模型学习区分特征

### 11.3 主动学习策略消融

**单一策略 vs 组合策略**：
- 随机采样alone：仅3.4%样本包含有害标签
- 阈值采样alone：对稀有类别效果好
- 不确定性采样alone：捕获模型不确定的边界案例
- **组合策略**：10-22倍改进

### 11.4 WDAT在不同阶段的效果

| 阶段 | 数据量 | WDAT改进幅度 |
|------|--------|-------------|
| PUB（仅公开） | ~90k | 显著（SH: 0.063→0.281） |
| SYN（+合成） | ~159k | 中等（SH: 0.086→0.296） |
| MIX（+生产） | ~219k | 较小（SH: 0.621→0.632） |

---

## 12. 局限性

### 12.1 偏差与公平性

**持续存在的偏差问题**：
- 模型对特定人口属性（如"gay"、"her"）有更高预测倾向
- 原因：训练数据中显式或隐式存在社会偏差

**缓解尝试**：
- 使用平衡模板合成数据集
- 但未能完全消除问题

### 12.2 数据增强的限制

**当前局限**：
- 错字和语法错误处理能力有限
- 对抗性输入（空格插入等）鲁棒性不足
- 合成数据多样性受限于模板设计

### 12.3 多语言支持不足

**现状**：
- 训练数据中仅约5%为非英语
- 主要生产流量是英语，未严格评估非英语性能

**需要改进**：
- 多语言毒性分类需要更多非英语训练数据
- 可能需要修改tokenization或模型架构

### 12.4 红队规模化

**当前问题**：
- 内部红队与每个新模型版本同步进行
- 不可扩展

**未来方向**：
- 建立类似标注生产流量的自动化红队pipeline
- 使用专门的界面提高红队效率

### 12.5 主动学习的简单性

**当前局限**：
- 因计算限制未探索多样性采样
- 未来计划进行更严格的策略比较实验

---

## 13. 伦理声明

### 13.1 标注者观点与分歧

**主观性挑战**：
- 有毒语言标注本质上是主观的
-  annotators' interpretations受个人和文化背景影响

**研究发现**：
- Waseem (2016)：女权主义者和反种族主义活动家与众包工作者系统性地在仇恨言论标注上存在分歧
- 作者间与非专家annotators的一致率低（14%）

**处理方法建议**：
- 不过度追求消除标注分歧
- 在涉及边缘化群体的数据中保留分歧信号
- 分析分歧可能导致更好的领域理解

**替代方法**：
- 不进行聚合而是保留annotator分歧（Davani et al. 2021）
- 可能产生相同或更好的性能，同时保留预测不确定性的估计

### 13.2 更广泛的影响讨论

**内容审核分类器的用途**：
1. **减少滥用**：确保政策在模型输入输出上的执行
2. **大规模数据过滤**：训练具有期望特性的语言模型
3. **语言模型评估**：更好的模型评估方法
4. **高风险可靠性**：确保高能力AI系统在关键领域的可靠性

**潜在风险**：
- 所有分类器都有某些假设和决策可能存在的漏洞
- 可能存在有问题的偏差，如对经常成为仇恨目标的群体的不成比例的假阳性
- 过度依赖自动化工具可能强化社会差异和伤害

### 13.3 数据发布考虑

**数据集来源**：
- CommonCrawl公开数据
- 模型生成的数据

**使用建议**：
- 鉴于各种任务的敏感性，鼓励将此分类体系与其他缓解策略结合使用
- 没有银弹解决方案

---

## 14. 参考文献

### 核心相关工作

1. **Perspective API (Jigsaw)**: Google旗下的毒性检测API，论文的主要对比基准

2. **RealToxicityPrompts (Gehman et al. 2020)**: 评估语言模型毒性退化问题

3. **HateCheck (Röttger et al. 2021)**: 仇恨言论检测模型的功能测试数据集

4. **ToxiGen (Hartvigsen et al. 2022)**: 大规模机器生成的仇恨和隐式仇恨言论数据集

5. **Dynabench (Kiela et al. 2021)**: 重新思考NLP基准测试的平台

6. **Red Teaming Language Models with Language Models (Perez et al. 2022)**: 使用语言模型进行红队测试

### 主动学习相关

7. **Lewis & Gale (1994)**: 文本分类的顺序主动学习算法

8. **Settles & Craven (2008)**: 序列标注任务中主动学习策略分析

9. **Gal et al. (2017)**: 深度贝叶斯主动学习

### 域适应相关

10. **Wasserstein GAN (Arjovsky et al. 2017)**: Wasserstein距离在GAN中的应用

11. **Domain Adversarial Training (Ganin et al. 2016)**: 神经网络的域对抗训练

12. **Shen et al. (2018)**: Wasserstein距离引导的域适应表示学习

### 数据增强与合成

13. **EDA (Wei & Zou 2019)**: 简单的数据增强技术

14. **GPT-3 Mix (Yoo et al. 2021)**: 利用大规模语言模型进行文本增强

15. **SimCSE (Gao et al. 2021)**: 简单的对比学习句子嵌入

### 公平性与偏差

16. **Counterfactual Fairness (Kusner et al. 2017)**: 反事实公平性

17. **Men Also Like Shopping (Zhao et al. 2017)**: 减少性别偏差放大

### 主要作者相关工作

18. **Weidinger et al. (2021)**: 语言模型的伦理和社会风险

19. **Welbl et al. 2021**: 语言模型解毒的挑战

---

## 附录：分类体系映射表

### 论文模型 vs Perspective API

| Perspective | 论文模型 |
|-------------|---------|
| max(sexually explicit, profanity, flirtation) | Sexual |
| identity attack | Hate |
| threat | Violence |
| max(toxicity, severe toxicity, insult, threat) | Harassment |
| - | Sexual/minors (S3) |

### 论文模型 vs Jigsaw

| 论文模型 | Jigsaw |
|---------|--------|
| Sexual | Toxic, Obscene |
| Hate | Identity hate |
| Violence | Threat |
| Harassment | Insult |
| Sexual/minors | - |

### 论文模型 vs TweetEval

| 论文模型 | TweetEval |
|---------|-----------|
| Hate | identity attack |
| Harassment | max(toxicity, severe toxicity, threat, insult, identity attack) |

---

## 总结

本文是OpenAI团队关于内容审核系统建设的系统性工作总结，涵盖从问题定义、分类体系设计、数据采集与质量控制、主动学习、合成数据增强、域适应到模型探测与红队测试的完整流程。主要贡献包括：

1. **提出整体方法论**：强调内容审核系统需要端到端的优化，而非仅关注模型架构

2. **展示主动学习的威力**：在稀有事件上实现10-22倍的采样效率提升

3. **系统性的数据质量控制**：详细说明标注指南设计、审计流程、错误检测方法

4. **合成数据的正确使用**：对比模板数据有效减少偏差，而大规模噪声数据有害

5. **开源贡献**：发布数据集和API，推动领域发展

这篇论文对于构建实际生产环境内容审核系统具有重要参考价值，其方法论对于其他安全相关分类任务也有普遍意义。

---

**笔记信息**
- 笔记作者：LLM Safety Paper Reading Cron
- 完成时间：2026-06-23
- 论文进度：98/80
