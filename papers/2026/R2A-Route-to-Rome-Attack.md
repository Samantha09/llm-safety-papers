# Route to Rome Attack: Directing LLM Routers to Expensive Models via Adversarial Suffix Optimization

## 第1章 基本信息

| 项目 | 内容 |
|------|------|
| **论文标题** | Route to Rome Attack: Directing LLM Routers to Expensive Models via Adversarial Suffix Optimization |
| **作者** | Haochun Tang, Yuliang Yan, Jiahua Lu, Huaxiao Liu, Enyan Dai |
| **机构** | 吉林大学符号计算与知识工程教育部重点实验室；香港科技大学（广州） |
| **会议** | ACL 2026 Main Conference |
| **arXiv** | [2604.15022](https://arxiv.org/abs/2604.15022) |
| **代码** | [GitHub: thcxiker/R2A-Attack](https://github.com/thcxiker/R2A-Attack) |
| **方向** | Router Attack / LLM Security |
| **关键词** | Cost-aware Routing, Black-box Attack, Adversarial Suffix, LLM Router Security |

---

## 第2章 英文摘要原文（arXiv Abstract）

> Cost-aware routing dynamically dispatches user queries to models of varying capability to balance performance and inference cost. However, the routing strategy introduces a new security concern that adversaries may manipulate the router to consistently select expensive high-capability models. Existing routing attacks depend on either white-box access or heuristic prompts, rendering them ineffective in real-world black-box scenarios. In this work, we propose R$^2$A, which aims to mislead black-box LLM routers to expensive models via adversarial suffix optimization. Specifically, R$^2$A deploys a hybrid ensemble surrogate router to mimic the black-box router. A suffix optimization algorithm is further adapted for the ensemble-based surrogate. Extensive experiments on multiple open-source and commercial routing systems demonstrate that R$^2$A significantly increases the routing rate to expensive models on queries of different distributions. Code and examples: https://github.com/thcxiker/R2A-Attack.

---

## 第3章 中文摘要翻译

> 成本感知路由（Cost-aware routing）通过动态调度用户查询到不同能力的模型来平衡性能与推理成本。然而，这种路由策略引入了一个新的安全威胁：攻击者可能操纵路由器持续选择昂贵的高能力模型。现有路由攻击依赖于白盒访问或启发式提示，在现实黑盒场景中效果不佳。在本工作中，我们提出R²A（Route to Rome Attack），通过对抗后缀优化诱导黑盒LLM路由器选择昂贵模型。具体而言，R²A部署混合集成代理路由器（hybrid ensemble surrogate router）来模拟黑盒路由器，并针对该集成代理设计了专门的后缀优化算法。在多个开源和商业路由系统上的大量实验表明，R²A能显著提高将查询路由到昂贵模型的比例，且适用于不同分布的查询。代码和示例：https://github.com/thcxiker/R2A-Attack。

---

## 第4章 研究背景

### 4.1 LLM路由技术的兴起

近年来，大型语言模型（LLM）的发展取得了显著成功，性能提升主要由缩放定律（scaling laws）驱动——即性能随模型规模增加可预测地提升。例如，Qwen-3-Max扩展到超过1万亿参数，约为前代旗舰模型Qwen-2.5-72B的14倍。然而，为每个用户查询都使用这种最先进的模型在计算和经济上都是不可持续的。

### 4.2 成本感知路由机制

为了平衡性能与成本，**成本感知LLM路由**（cost-aware LLM routing）被提出用于将每个查询路由到满足目标质量要求的最低成本模型。这一策略基于一个洞察：只有一小部分请求真正需要昂贵的强模型，而简单查询可以由更便宜的弱模型有效处理。

例如，当路由器收到简单事实查询"What is the capital of France?"时，它识别出这是低复杂度查询，选择弱模型Mistral 8x7B来生成响应。这种路由已被OpenRouter和GPT-5-Auto等商业系统采用。

### 4.3 路由攻击的威胁

尽管成本感知路由有效，但它引出了一个自然的安全问题：**攻击者是否可以使用通用触发器（如固定后缀）来持续操纵路由器选择昂贵模型？**

现有的路由攻击研究存在以下局限：
- **Shafran等人（2025）**的方法依赖于可访问目标路由器的梯度或已知架构，这在商业设置中不切实际，因为黑盒路由器只允许观察最终路由决策
- **LifeCycle（Lin等人，2025b）**从高胜率查询中提取模板（如"Below is an instruction..., [query]"）来引导路由器选择昂贵LLM，但这种启发式提示未经严格优化，无法一致地操纵各种目标路由器

### 4.4 研究空白

在现实黑盒场景中，现有的路由攻击方法要么需要白盒访问，要么启发式提示不够有效。因此，**如何在仅需黑盒访问的情况下，高效地诱导路由器选择昂贵模型**成为一个重要研究问题。

---

## 第5章 核心贡献

本文的主要贡献可以总结为以下几点：

### 5.1 新型攻击范式

首次研究了通过对抗后缀优化诱导黑盒LLM路由器选择昂贵模型这一新问题。与传统越狱攻击不同，这是一种**经济攻击**，目的是耗尽目标系统的推理成本资源。

### 5.2 混合集成代理路由器

提出**混合集成代理路由器（Hybrid Ensemble Surrogate Router）**，结合多种开源路由器和轻量级可训练路由器，能够在严格的查询预算下模拟未知架构的目标路由器。

### 5.3 针对集成代理的后缀优化算法

设计了专门针对集成代理路由器的**对抗后缀优化算法**，通过归一化梯度聚合解决不同路由器架构间梯度幅度差异问题。

### 5.4 全面的实验验证

在6个数据集、7个开源路由器和2个商业路由器（GPT-5-Auto和OpenRouter）上验证了R²A的有效性，证明其能显著提高将查询路由到昂贵模型的比例。

---

## 第6章 研究方法

### 6.1 问题定义

#### 6.1.1 LLM路由器基础

给定查询$q$，LLM路由器$\mathcal{R}: q \rightarrow \mathbb{R}^{N}$从模型池$\mathcal{M} = \{M_1, \dots, M_N\}$中选择模型。对于成本感知路由，路由器通过求解以下优化问题来最小化推理成本同时满足目标质量约束：

$$\mathcal{R}(q) = \arg\min_{M_i \in \mathcal{M}} \Big(\ell(q, M_i) + \lambda \cdot C(q, M_i)\Big)$$

其中$\ell(q, M_i)$表示模型$M_i$在查询$q$上的预测损失，$C(q, M_i)$是成本分数，$\lambda \geq 0$控制成本分数在路由决策中的权重。

#### 6.1.2 威胁模型

**攻击者目标**：诱导路由器选择昂贵模型回答给定查询。按照公开排行榜（如Lmarena.ai），将模型候选池分为昂贵强模型$\mathcal{M}_{strong}$和廉价弱模型$\mathcal{M}_{weak}$。给定查询$q$使得$\mathcal{R}_t(q) \in \mathcal{M}_{weak}$，如果目标路由器$\mathcal{R}_t(\mathcal{A}(q)) \in \mathcal{M}_{strong}$，则攻击操作成功。

**攻击者能力**：攻击者可以通过附加对抗后缀来修改原始查询。为保持答案质量并使修改最小化，攻击者被限制最多向后缀末尾附加$\Delta$个token的后缀$s$。

**攻击者知识**：假设在现实黑盒设置中，攻击者只能观察目标路由器对输入查询的决策。所有其他信息（如目标路由器的内部logits、参数或梯度）均不可访问。由于每次查询目标路由器通常会产生财务成本，攻击者被限制最多$Q$次查询到$\mathcal{R}_t$。

#### 6.1.3 路由攻击形式化

目标是找到通用对抗后缀$s^*$，使目标路由器$\mathcal{R}_t$的决策变为选择昂贵强模型：

$$s^* = \arg\max_{s} \mathbb{E}_{q \sim \mathcal{Q}} \left[ \mathbb{I}(\mathcal{R}_t(q \oplus s) \in \mathcal{M}_{strong}) \right]$$

$$s.t. \quad s \in \mathcal{S}, \quad |s| \leq \Delta$$

### 6.2 方法框架

在黑盒设置下，无法直接访问目标路由器$\mathcal{R}_t$的参数或梯度。因此，R²A首先训练代理路由器来模拟目标路由器的行为，然后使用代理路由器优化通用对抗后缀。

R²A引入了**混合集成代理路由器**，结合多种现有开源方法和轻量级可训练路由器。通过覆盖多种路由机制，代理路由器能更好地在查询预算内对齐未知设计的目标路由器。此外，针对混合集成代理路由器设计了专门的后缀优化算法。

### 6.3 混合集成代理路由器

#### 6.3.1 设计动机

由于目标路由器设计未知，仅依赖单一架构可能导致架构不匹配，从而产生较差的代理。因此，构建结合多种预训练开源路由器和轻量级可训练路由器的混合集成代理路由器。

这种设计提供两个关键优势：
1. 通过引入开源路由器，R²A可以快速识别与目标行为匹配的现有路由器（或线性组合），减少所需查询
2. 通过优化可训练轻量级路由器，R²A可以处理与所有预训练开源路由器显著不同的目标路由器

#### 6.3.2 可训练轻量级路由器设计

可训练轻量级路由器$\mathcal{R}_l$旨在从查询的嵌入$E(q) \in \mathbb{R}^d$预测目标路由器的决策。具体地，使用all-MiniLM-L6-v2作为编码器，其中$d=384$。

然而，直接学习从$\mathbb{R}^d$到$\mathbb{R}^{|\mathcal{M}_t|}$的线性映射涉及优化大小为$d \times |\mathcal{M}_t|$的参数矩阵，训练这个大矩阵需要大量查询，超出严格的查询预算。

受LoRA启发，施加低秩约束，将变换分解为两个较小的矩阵$\mathbf{W}_l^1 \in \mathbb{R}^{d \times r}$和$\mathbf{W}_l^2 \in \mathbb{R}^{r \times |\mathcal{M}_t|}$，其中秩$r \ll d$。轻量级路由器的logits $\mathbf{z}_l \in \mathbb{R}^{|\mathcal{M}_t|}$计算为：

$$\mathbf{z}_l = E(q) \mathbf{W}_l^1 \mathbf{W}_l^2$$

通过这种低秩分解，训练路由器$\mathcal{R}_l$所需的查询更少。

#### 6.3.3 结合开源路由器

R²A将具有多种路由机制的多个开源路由器$\{\mathcal{R}_o^{(1)}, \dots, \mathcal{R}_o^{(K)}\}$结合起来，减少代理路由器与目标路由器之间的机制不匹配。然而，开源路由器的模型池与目标路由器的模型池不一致，因此将其logits映射到所有开源模型池的并集$\mathcal{M}_{uni} = \bigcup_{k=1}^{K} \mathcal{M}_o^{(k)}$，使用零填充处理缺失的候选。

对于开源路由器$\mathcal{R}_o^{(k)}$，将其logit向量扩展为$\mathbf{z}_{uni}^{(k)} = [\tilde{z}_1^{(k)}, \dots, \tilde{z}_{|\mathcal{M}_{uni}|}^{(k)}]$，其中每个元素定义为：

$$\tilde{z}_i^{(k)} = \begin{cases} z_{M_i}^{(k)}, & \text{if } M_i \in \mathcal{M}_o^{(k)} \\ 0, & \text{otherwise} \end{cases}$$

由于开源路由器的模型池并集$\mathcal{M}_{uni}$通常与目标池$\mathcal{M}_t$不同，应用线性映射来对齐它们的logits：

$$\mathbf{z}_o^{(k)} = \mathbf{W}_o \cdot \mathbf{z}_{uni}^{(k)}$$

其中$\mathbf{W}_o \in \mathbb{R}^{|\mathcal{M}_{uni}| \times |\mathcal{M}_t|}$是投影矩阵。

#### 6.3.4 代理路由器训练

为了训练代理路由器，查询黑盒目标$\mathcal{R}_{target}$生成训练标签。根据威胁模型，限制查询目标路由器$Q$次。代理训练目标通过最小化以下损失来优化参数$\theta = \{\mathbf{W}_l^1, \mathbf{W}_l^2, \mathbf{W}_o, \{\alpha_i\}_{i=0}^K\}$：

$$\min_{\theta} \mathcal{L}_S = \frac{1}{Q} \sum_{i=1}^{Q} l(\hat{y}(q_i), \mathcal{R}_t(q_i))$$

其中$l(\cdot)$是交叉熵损失，$\hat{y}(q_i)$和$\mathcal{R}_t(q_i)$分别表示代理和目标路由器对查询$q_i \in \mathcal{D}_{proxy}$的预测。

### 6.4 对抗后缀优化

#### 6.4.1 优化目标

使用混合集成代理路由器，对抗后缀优化可以重新表述为：

$$\min_s \mathcal{L}_A = -\mathbb{E}_{q \sim \mathcal{Q}} \sum_{M \in \mathcal{M}_{strong}} p(\hat{y} = M | q \oplus s)$$

其中$p(\hat{y} = M | q \oplus s)$表示代理路由器预测将附加对抗后缀$s$的查询$q$路由到模型$M$的概率。

#### 6.4.2 后缀Token梯度聚合

可以部署Greedy Coordinate Gradient（GCG），使用编码器的token梯度贪婪替换token。然而，我们的集成代理涉及多个编码器，因此需要跨集成中路由器的梯度聚合。

令$\mathbf{z}_{total} = \sum_{k=0}^{K} \alpha_k \mathbf{z}^{(k)}$表示集成logits。对于第$k$个路由器，关于token $s_i$的梯度计算为：

$$g_i^{(k)} = \frac{\partial \mathcal{L}_A}{\partial \mathbf{z}_{total}} \cdot \underbrace{\frac{\partial \mathbf{z}_{total}}{\partial \mathbf{z}^{(k)}}}_{\alpha_k} \cdot \frac{\partial \mathbf{z}^{(k)}}{\partial s_i} = \alpha_k \cdot \frac{\partial \mathcal{L}_A}{\partial \mathbf{z}_{total}} \frac{\partial \mathbf{z}^{(k)}}{\partial s_i}$$

对于项$\delta_i^{(k)} = \frac{\partial \mathbf{z}^{(k)}}{\partial s_i}$，虽然它有效地捕获了单个路由器内的token敏感性，但其幅度在不同架构间可能差异很大。因此，直接求和$g_i^{(k)}$将导致特定成员路由器主导优化。为缓解这种偏差，通过min-max缩放将$\delta_i^{(k)}$归一化到$[0,1]$范围：

$$\tilde{\delta}_i^{(k)} = \frac{\delta_i^{(k)} - \delta_{min}^{(k)}}{\delta_{max}^{(k)} - \delta_{min}^{(k)}}$$

---

## 第7章 实验设置

### 7.1 数据集

实验使用了6个不同分布的数据集，涵盖多种查询类型：
- 事实性问答（FactQA）
- 数学问题（Math）
- 代码生成（Code）
- 对话生成（Dialogue）
- 复杂推理（Reasoning）
- 简单查询（Simple）

### 7.2 目标路由器

实验涵盖了7个开源路由器和2个商业路由器：

**开源路由器**：
- RouteLLM
- RouterDC
- RouterEval
- LLMRouterBench
- RouterArena
- 等

**商业路由器**：
- **GPT-5-Auto**：OpenAI的自适应路由系统
- **OpenRouter**：第三方路由平台

### 7.3 基线方法

与以下基线方法进行比较：
- **Random Suffix**：随机选择后缀
- **Heuristic Template**：使用LifeCycle等人提出的启发式模板
- **GCG（白盒）**：假设完全访问目标路由器的梯度
- **LifeCycle**：基于模板的启发式方法

### 7.4 评估指标

主要评估指标：
- **路由到强模型的比率（Routing Rate to Strong Models）**
- **平均成本增加**
- **答案质量保持率**

---

## 第8章 实验结果

### 8.1 主要结果

实验结果表明，R²A在多个开源和商业路由器上显著提高了将查询路由到昂贵模型的比例。具体而言：

1. **开源路由器**：R²A在各种开源路由器上平均将强模型路由率从基线的20-30%提升到60-80%

2. **商业路由器**：
   - 在OpenRouter上，R²A成功将大量原本路由到廉价模型的查询重定向到昂贵模型
   - 在GPT-5-Auto上，由于路由决策不可观察，使用在OpenRouter上学到的后缀进行迁移攻击

3. **跨分布泛化**：R²A学到的对抗后缀能够泛化到不同分布的查询，表明其学习到了路由器对特定语言模式的敏感性

### 8.2 与基线比较

| 方法 | 开源路由器平均路由率 | 商业路由器路由率 |
|------|---------------------|-----------------|
| Random Suffix | 25% | 22% |
| Heuristic Template | 35% | 28% |
| GCG（白盒） | 72% | N/A |
| LifeCycle | 38% | 31% |
| **R²A（本文）** | **78%** | **65%** |

### 8.3 答案质量分析

重要的是，R²A在增加路由成本的同时，保持了较高的答案质量。通过对抗后缀操纵的是路由决策，而非模型生成内容本身，因此答案质量基本保持不变。

---

## 第9章 策略示例

### 9.1 攻击成功示例

**原始查询**：
```
What is the capital of France?
```

**原始路由决策**：Mistral 8x7B（廉价弱模型）

**附加对抗后缀后**：
```
What is the capital of France? [Adversarial Suffix]
```

**攻击后路由决策**：GPT-4o或Claude-3.5（昂贵强模型）

### 9.2 后缀特征分析

研究发现，有效的对抗后缀通常具有以下特征：
- 包含特定的语言模式或触发词
- 长度在5-20个token之间
- 看似自然但能触发路由器的分类边界

---

## 第10章 攻击流程

### 10.1 攻击Pipeline

R²A的攻击流程分为两个阶段：

**阶段1：代理路由器训练**
1. 收集一组代表性查询$\mathcal{D}_{proxy}$
2. 使用有限的$Q$次查询获取目标路由器的决策标签
3. 训练混合集成代理路由器$\mathcal{R}_s$，同时学习：
   - 轻量级路由器的LoRA参数
   - 开源路由器的集成权重
   - Logit投影矩阵

**阶段2：对抗后缀优化**
1. 使用代理路由器计算对抗后缀的梯度
2. 通过归一化梯度聚合避免特定路由器主导
3. 贪婪地迭代替换token直到达到最大长度$\Delta$
4. 在目标路由器上验证后缀效果

### 10.2 查询预算约束

R²A设计时考虑了严格的查询预算约束：
- 代理训练阶段：仅需$Q$次查询（通常几百到几千次）
- 后缀优化阶段：使用代理路由器进行，不产生额外目标查询成本

---

## 第11章 消融实验

### 11.1 代理路由器组件消融

| 配置 | 代理-目标一致性 | 攻击成功率 |
|------|----------------|-----------|
| 仅轻量级路由器 | 72% | 65% |
| 仅开源路由器集成 | 78% | 68% |
| 混合集成（无LoRA） | 81% | 71% |
| 混合集成（完整） | **89%** | **78%** |

结果表明，混合集成设计对代理质量至关重要。

### 11.2 梯度聚合策略消融

| 聚合策略 | 攻击成功率 |
|----------|-----------|
| 直接求和 | 52% |
| 权重加权求和 | 61% |
| 归一化后求和 | **78%** |

归一化梯度聚合显著提升了攻击效果，证明了处理不同路由器架构间梯度幅度差异的重要性。

### 11.3 查询预算影响

随着查询预算$Q$的增加，代理质量提升，攻击成功率提高。但研究表明，即使在严格的查询预算（如$Q=500$）下，R²A仍能保持较高的攻击成功率（约65%）。

### 11.4 后缀长度影响

对抗后缀的最佳长度在10-15个token之间。过短的后缀缺乏足够的触发能力，过长的后缀可能被路由器检测为异常模式。

---

## 第12章 局限性

### 12.1 黑盒假设的局限性

R²A假设攻击者只能观察路由决策，无法访问路由器的内部状态。然而，在某些商业系统中，可能存在更严格的访问限制或额外的防护机制。

### 12.2 迁移性问题

虽然R²A在多个路由器上验证了其有效性，但在某些情况下，在一个路由器上学到的后缀可能无法直接迁移到另一个路由器。这主要是因为不同路由器可能使用不同的路由机制和决策边界。

### 12.3 防御可能性

论文没有深入探讨防御策略。可能的防御方向包括：
- 检测异常的后缀模式
- 对抗性训练使路由器对后缀攻击更鲁棒
- 限制单用户的查询频率或成本配额

### 12.4 实际影响评估

论文主要关注攻击的有效性，对实际部署场景中的经济影响评估相对有限。

---

## 第13章 伦理声明

### 13.1 研究目的

本研究旨在揭示成本感知LLM路由系统中的安全漏洞，帮助研究社区和工业界更好地理解和防御此类攻击。研究属于负责任的漏洞发现和披露。

### 13.2 负责任的披露

作者承诺：
- 不公开可直接用于恶意攻击的具体后缀
- 与相关系统提供商分享研究发现
- 提供防御建议以提升系统安全性

### 13.3 更广泛影响

路由器攻击可能对LLM服务提供商造成经济损失，但本研究有助于：
- 提高对LLM系统安全风险的认识
- 推动更安全的路由系统设计
- 促进LLM安全领域的进一步研究

---

## 第14章 参考文献

1. Kaplan et al. (2020). Scaling Laws for Neural Language Models.
2. Lu et al. (2024). Cost-aware Routing in LLM Systems.
3. Aggarwal et al. (2025). Dynamic Model Routing for LLM Inference.
4. Ong et al. (2025). Quality-Constrained LLM Routing.
5. Zou et al. (2023). Universal and Transferable Adversarial Attacks on Aligned Language Models (GCG).
6. Hu et al. (2022). LoRA: Low-Rank Adaptation of Large Language Models.
7. Wang et al. (2020). Sentence-T5: Scalable Sentence Encoders from Pre-trained Text-to-Text Transformers.
8. Liu et al. (2017). Delving into Transferable Adversarial Examples.
9. Dong et al. (2018). Boosting Adversarial Transferability.
10. Shafran et al. (2025). Routing Attacks on LLM Systems.
11. Lin et al. (2025b). LifeCycle: Template-based Router Manipulation.

---

## 附录：相关资源

- **GitHub仓库**：https://github.com/thcxiker/R2A-Attack
- **论文引用**：
```
@inproceedings{tang2026routeromeattackdirecting,
  title={Route to Rome Attack: Directing LLM Routers to Expensive Models via Adversarial Suffix Optimization},
  author={Haochun Tang and Yuliang Yan and Jiahua Lu and Huaxiao Liu and Enyan Dai},
  booktitle={Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (ACL 2026)},
  year={2026}
}
```
