# TingIS: Real-time Risk Event Discovery from Noisy Customer Incidents at Enterprise Scale

## 1. 基本信息

| 字段 | 内容 |
|------|------|
| **论文标题** | TingIS: Real-time Risk Event Discovery from Noisy Customer Incidents at Enterprise Scale |
| **arXiv ID** | 2604.21889 |
| **作者** | Jun Wang, Ziyin Zhang, Rui Wang, Hang Yu, Peng Di, Rui Wang |
| **单位** | Ant Group, Shanghai Jiao Tong University |
| **会议** | ACL 2026 Industry Track |
| **方向** | LLM Agent / Incident Detection |
| **GitHub** | https://github.com/antgroup/tingis |
| **代码** | 开源 |

## 2. 英文摘要原文

Real-time detection and mitigation of technical anomalies are critical for large-scale cloud-native services, where even minutes of downtime can result in massive financial losses and diminished user trust. While customer incidents serve as a vital signal for discovering risks missed by monitoring, extracting actionable intelligence from this data remains challenging due to extreme noise, high throughput, and semantic complexity of diverse business lines. In this paper, we present TingIS, an end-to-end system designed for enterprise-grade incident discovery. At the core of TingIS is a multi-stage event linking engine that synergizes efficient indexing techniques with Large Language Models (LLMs) to make informed decisions on event merging, enabling the stable extraction of actionable incidents from just a handful of diverse user descriptions. This engine is complemented by a cascaded routing mechanism for precise business attribution and a multi-dimensional noise reduction pipeline that integrates domain knowledge, statistical patterns, and behavioral filtering. Deployed in a production environment handling a peak throughput of over 2,000 messages per minute and 300,000 messages per day, TingIS achieves a P90 alert latency of 3.5 minutes and a 95% discovery rate for high-priority incidents. Benchmarks constructed from real-world data demonstrate that TingIS significantly outperforms baseline methods in routing accuracy, clustering quality, and Signal-to-Noise Ratio.

## 3. 中文摘要翻译

实时检测和缓解技术异常对于大规模云原生服务至关重要，即使几分钟的停机也可能导致巨大的经济损失和用户信任度下降。虽然客户反馈是发现监控盲区风险的重要信号，但由于极端噪声、高吞吐量和不同业务线的语义复杂性，从这些数据中提取可操作的情报仍然具有挑战性。在本文中，我们提出了TingIS，这是一个为企业级事件发现设计的端到端系统。TingIS的核心是一个多阶段事件链接引擎，它将高效的索引技术与大语言模型（LLM）相结合，就事件合并做出明智决策，能够从少量多样化的用户描述中稳定地提取可操作的事件。该引擎辅以级联路由机制实现精确的业务归属，以及整合领域知识、统计模式和行为过滤的多维降噪流水线。TingIS部署在生产环境中，处理峰值吞吐量超过每分钟2000条消息和每天300000条消息，实现了3.5分钟的P90告警延迟和高优先级事件95%的发现率。基于真实生产数据构建的基准测试表明，TingIS在路由准确性、聚类质量和信噪比方面显著优于基线方法。

## 4. 研究背景

### 4.1 问题背景

在现代数字服务时代，大规模在线平台由复杂的微服务和云原生架构支撑，已成为电子商务、社交媒体和金融交易等领域不可或缺的基础设施。对于这些系统，即使是轻微的故障也可能迅速传播成大规模事件，造成重大经济损失并侵蚀用户信任。

以支付宝为例——它是全球最大的移动支付平台之一——在2025年1月经历了一次与国家补贴相关的关键配置错误，20%的折扣被错误地应用于所有交易。凭借约20万亿美元的年交易量，即使只有5分钟的事件窗口也可能导致约4000万美元的损失。因此，及时检测和响应此类新兴风险对于维护系统可靠性和金融安全至关重要。

### 4.2 现有监控系统局限性

虽然指标、日志和追踪等内部可观测性系统构成了第一道防线，但它们并非万无一失。当它们失效时，客户反馈和热线咨询等客户事件提供了互补且独特的信号，暴露了自动化监控的"盲区"，并反映了用户影响的直接衡量标准。

然而，利用客户事件进行实时风险检测面临巨大挑战，因为它们本质上具有噪声、口语化和多源的特点。在每分钟2000条消息的流吞吐量中，仅从3个噪声数据点中提取系统性故障信号造成了严重的信噪比（SNR）挑战。低信噪比的系统不可避免地会触发数千个误报警报，迅速压垮站点可靠性工程（SRE）团队，导致告警疲劳。情况因业务异质性、实时性高需求和低漏检容忍度而进一步复杂化。

### 4.3 核心挑战

从少量客户事件（如仅3个）中及早检测潜在系统漏洞（称为"风险事件"）已成为预防灾难性故障和最小化企业损失的核心策略。但面临以下挑战：

1. **极端噪声**：用户描述口语化、情绪化、含个人信息
2. **高吞吐量**：需要处理每分钟2000+条消息
3. **语义复杂性**：不同业务线差异大
4. **实时性要求**：延迟容忍度低
5. **低漏检容忍**：高优先级事件必须被发现

## 5. 核心贡献

1. **TingIS端到端系统**：提出首个企业级风险事件发现系统，从嘈杂客户事件中实时提取可操作的风险情报

2. **多阶段事件链接引擎**：结合局部敏感哈希（LSH）、历史事件关联和LLM高级推理，弥合噪声语义输入与可操作风险情报之间的差距

3. **级联路由机制**：两阶段策略（基于关键词的高精度 + 基于语义的高召回）实现精确业务归属

4. **多维降噪流水线**：整合领域知识、统计模式和行为过滤，动态抑制噪声

5. **生产环境验证**：在日处理300000条客户事件的生产环境中验证，系统实现95%的高优先级事件发现率和3.5分钟P90告警延迟

## 6. 研究方法

### 6.1 核心设计原则

TingIS基于三个核心洞察设计：

1. **语义收敛与身份持久性**：确保源自相同根本原因的事件始终收敛到唯一、持久的ID

2. **混合智能协同**：策略性地平衡LLM的高认知深度与处理海量流数据的计算成本。资源感知原则贯穿系统：基于规则的预过滤削减输入量、LSH和相似度阈值控制昂贵的LLM调用、持久事件状态随时间产生渐近效率提升

3. **多约束SNR平衡**：通过整合知识库、统计审计和升级逻辑动态抑制噪声

### 6.2 五模块架构

TingIS由五个正交模块组成（M1-M5），每个模块设计为即插即用，允许无缝更新以确保低维护成本：

#### M1: 语义蒸馏（Semantic Distillation）

**目标**：将原始用户声音转换为无歧义的语义单元

**方法**：
- 使用LLM（Qwen3-8B）为每个有效事件生成初始摘要
- 摘要遵循"主体+问题"格式（如"信用卡在线支付+折扣错误"）
- 明确忽略情感表达、口语填充词、个人身份信息（PII）和无关细节
- 初始摘要使用嵌入模型（BGE-M3）转换为高维向量

**输出**：干净、高密度、主题驱动的语义表示

#### M2: 级联路由（Cascaded Routing）

**目标**：将事件精确路由到对应的业务域

**两阶段策略**：

1. **基于关键词阶段（高精度）**：
   - 使用"实体优先"原则匹配关键词知识库
   - 如果在初始摘要的实体字段中找到匹配，立即返回相应的biz_code
   - 高效处理大量清晰、定义明确的事件

2. **基于语义阶段（高召回）**：
   - 对于没有关键词命中的事件，跨多个向量知识库执行并行向量检索
   - 候选人通过重排序器（BGE-Reranker-V2-M3）细化
   - 预定义阈值过滤
   - 低置信度候选人发送到回退域，由全局控制团队手动分派

#### M3: 事件链接引擎（Event Linking Engine）

**核心挑战**：确定"事件身份"——准确判断多个在不同时间到达、表达不同的事件是否指向相同的潜在风险事件

**多阶段渐进优化过程**：

**阶段1: 批次内高效聚合**
- 首先通过biz_code对事件进行分区约束
- 在每个分区内，使用LSH进行高速初步聚类
- LLM（Kimi-K2）对每个聚类执行代表性检查
- 如果聚类被判断为不纯，LLM将其拆分为多个聚类并为每个生成标题
- LSH和LLM的协同确保输出聚类标题既全面又相互排斥

**阶段2: 跨批次历史关联**
- 每个批次聚类标题嵌入后用于从历史风险事件知识库中检索
- 引入时间衰减加权机制结合语义相似性与时间接近性：

$$s^* = s \cdot e^{-k\Delta t}$$

其中：
- $s$ = 当前标题嵌入与历史事件嵌入之间的语义相似度分数
- $\Delta t$ = 自历史事件上次活跃时间以来经过的时间（以天为单位）
- $s^*$ = 最终分数

- 这防止了"历史惯性"，即旧事件错误吸收新的不相关事件
- 如果最高组合分数超过阈值，LLM执行最终裁决（合并 vs. 创建新事件）
- 否则直接创建新的风险事件

#### M4: 事件状态管理（Event State Management）

**目标**：支持实时风险监控和决策

**分层数据模型**：

1. **状态层（Risk Event）**：存储最少的一组可变状态（如当前量、最后修改时间戳、最后活跃时间戳）用于实时告警和时间衰减计算

2. **审计层（Alert Record）**：不可变日志，记录每个事件的端到端证据链（原始文本 → 摘要 → 聚类 → 事件ID），捕获每个告警触发器及其上下文（静态阈值 vs. 动态基线）和具体原因，确保100%可审计性

3. **快照层（Volume Timeline）**：定期记录事件量股票和流量，为M5动态基线计算提供稳定、低成本的历史样本

#### M5: 多维降噪（Multi-dimensional Denoising）

**挑战**：仅依赖量阈值通常会在非故障场景（如营销咨询）期间导致"告警风暴"

**三层降噪集成**：

1. **源抑制（Source Suppression）**：
   - 在聚类阶段，系统将聚类与假阳性样本知识库（假阳性KB）匹配
   - 如果新聚类与历史假阳性高度相似，则在生成事件之前被抑制

2. **统计过滤（Statistical Filtering via Dynamic Baselines）**：
   - 事件必须通过双阈值触发器
   - 除了静态业务级阈值外，事件的量必须显著偏离其动态基线（μ+2σ）
   - 动态基线从M4快照层计算
   - 这过滤掉周期性业务波动

3. **行为约束（Behavioral Constraints）**：
   - 为防止告警疲劳，TingIS实施告警静默期
   - 一旦事件被标记为"进行中"，进一步告警自动暂停两小时
   - 但系统同时实时监控事件量的斜率
   - 如果当前量呈现爆炸性、非线性激增，系统将绕过静默窗口实施告警穿透
   - 确保关键升级立即传递给响应者

## 7. 实验设置

### 7.1 评估框架

建立分层评估框架，通过两个互补路径验证系统：

1. **在线生产验证**：测量一个月部署期间的核心业务影响（召回率和延迟），覆盖由开发者和SRE专家团队确认的高优先级风险事件

2. **离线基准评估**：实现公平、控制和可重现的基线比较和消融研究

### 7.2 生产环境

- 部署在领先金融科技平台
- 峰值吞吐量：每分钟超过2000条事件
- 日处理量：300000条客户事件

### 7.3 基线方法

与两类基线进行比较：
- 系统级基线
- 专门模块级方法

### 7.4 评估指标

1. **路由准确性**（Routing Accuracy）
2. **聚类质量**（Clustering Quality）
3. **信噪比**（Signal-to-Noise Ratio）
4. **召回率**（Recall）
5. **延迟**（Latency）

## 8. 实验结果

### 8.1 在线生产性能

一个月在线部署期间：
- **高优先级事件发现率**：95%
- **P90告警延迟**：3.5分钟
- 提供快速紧急响应的关键时间窗口

### 8.2 离线基准评估

基于真实生产数据构建的基准测试证明：
- TingIS在**路由准确性**上显著优于基线
- TingIS在**聚类质量**上显著优于基线
- TingIS在**信噪比**上显著优于基线

### 8.3 性能特点

- 峰值吞吐量超过每分钟2000条消息
- 日处理300000条客户事件
- 在保持高准确性的同时实现低延迟

## 9. 策略示例

### 9.1 语义蒸馏示例

**输入（原始用户反馈）**：
> "OMG I'm so frustrated! I tried to pay with my credit card on the Alipay app but it's showing some weird discount that I've never seen before and I think there's something broken with the system!!"

**输出（"主体+问题"格式）**：
> "credit card online payment + discount error"

### 9.2 事件链接示例

多个来自不同用户的事件：
- "支付宝信用卡支付显示错误折扣"
- "用信用卡付钱出问题了"
- "credit card payment discount issue"

**链接结果**：聚类为同一风险事件："支付系统配置错误导致的折扣异常"

### 9.3 告警穿透示例

正常情况下，事件标记为"进行中"后静默两小时。但如果检测到爆炸性非线性激增（如故障导致大量用户同时受影响），系统绕过静默期立即告警。

## 10. 攻击流程

本文主要关注风险事件发现，不是安全攻击论文。但从LLM Agent安全角度，可以识别以下潜在攻击面：

### 10.1 提示注入风险

如果攻击者能够操控客户反馈的语义蒸馏过程，可能导致：
- 虚假事件被注入
- 真实事件被抑制

**防御措施**：语义蒸馏使用严格格式约束和LLM内置的安全过滤

### 10.2 对抗性事件注入

攻击者可能通过大量语义相似的客户反馈触发虚假告警：
- 利用多维降噪的源抑制机制防御
- 动态基线防止突然的量异常被误判

### 10.3 路由操纵

通过构造特定实体关键词影响业务归属：
- 级联路由的两阶段策略提供平衡
- 低置信度事件进入人工审核流程

## 11. 消融实验

论文进行以下消融研究：

### 11.1 模块级消融

| 模块 | 移除效果 |
|------|----------|
| M1 语义蒸馏 | 事件识别准确性显著下降 |
| M2 级联路由 | 业务归属错误率上升 |
| M3 事件链接 | 事件合并质量下降 |
| M4 状态管理 | 实时告警延迟增加 |
| M5 多维降噪 | 误报率显著上升 |

### 11.2 技术选择消融

| 技术 | 替代方案 | 效果 |
|------|----------|------|
| LSH聚类 | 朴素聚类 | LSH显著提升速度 |
| LLM代表检查 | 规则检查 | LLM提高聚类纯度 |
| 时间衰减机制 | 无时间衰减 | 防止历史惯性 |
| 动态基线 | 静态阈值 | 更好过滤周期性波动 |

## 12. 局限性

1. **计算成本**：LLM在多个模块中的使用带来较高计算开销，需要在认知深度和成本之间平衡

2. **依赖外部模型**：系统依赖Qwen3-8B和Kimi-K2等外部LLM，可能受模型可用性和性能影响

3. **阈值敏感性**：多个阈值（重排序阈值、动态基线σ值、静默期时长）需要针对不同业务场景调优

4. **领域适应性**：针对金融科技平台设计，可能需要针对其他行业（如电商、社交网络）进行适配

5. **离线学习**：假阳性知识库需要持续更新以应对新类型的非风险事件模式

6. **可扩展性边界**：在超大规模（10x以上）吞吐量下的性能未经验证

## 13. 伦理声明

本文提出了一个用于企业级风险事件发现的实用系统，无直接伦理风险。系统旨在帮助企业及早发现和响应技术故障，保护用户利益。

工作中使用的所有数据均为脱敏处理的生产数据，符合隐私保护要求。

代码已开源（https://github.com/antgroup/tingis），促进研究复现和行业应用。

## 14. 参考文献

1. Qwen3: Qwen3 large language models (2025)
2. BGE-M3: Multi-encoding BGE-M3 embedding model (2024)
3. Kimi-K2: Kimi-K2 large language model (2025)
4. liao-etal-2024-d2llm: D2LLM cross-encoder reranker (2024)
5. alipay-error: Alipay January 2025 configuration error incident
6. alipay-stats: Alipay annual transaction volume statistics
7. li2019realtime: Real-time anomaly detection methods
8. 2003clustream: CluStream clustering algorithm
9. 2006denstream: DenStream streaming clustering
10. 2009statistic-anomaly-1/2: Statistical anomaly detection methods
11. 2017cascade-ranking: Cascade ranking for efficiency
12. 2022embed2detect: Embedding-based detection methods
13. 2021entity-aware: Entity-aware extraction
14. 2021keyword-filtering: Keyword filtering techniques
15. 2024context-aware-clustering: Context-aware clustering
16. 2024few-shot-clustering: Few-shot clustering methods
17. 2025clustering-as-classification: Clustering as classification approach
18. 2025clustering-with-llm-embedding: LLM embedding for clustering
19. 2025hybrid-ai-conversation: Hybrid AI conversation systems
20. 2025in-context-clustering: In-context clustering methods