# 【论文笔记】Route to Rome Attack: Directing LLM Routers to Expensive Models via Adversarial Suffix Optimization

## 1. 基本信息

| 项目 | 内容 |
|------|------|
| **论文标题** | Route to Rome Attack: Directing LLM Routers to Expensive Models via Adversarial Suffix Optimization |
| **简称/缩写** | R²A (Route to Rome Attack) |
| **作者** | Haochun Tang, Yuliang Yan, Jiahua Lu, Huaxiao Liu, Enyan Dai |
| **所属机构** | 吉林大学符号计算与知识工程教育部重点实验室<br>香港科技大学（广州） |
| **发表会议** | ACL 2026 Main Conference |
| **arXiv编号** | [2604.15022](https://arxiv.org/abs/2604.15022) |
| **代码链接** | [GitHub: thcxiker/R2A-Attack](https://github.com/thcxiker/R2A-Attack) |
| **研究方向** | LLM Router Security / Routing Attack |
| **关键词** | Cost-aware Routing, Black-box Attack, Adversarial Suffix, Ensemble Surrogate |

---

## 2. 英文摘要原文（arXiv Abstract）

> Cost-aware routing dynamically dispatches user queries to models of varying capability to balance performance and inference cost. However, the routing strategy introduces a new security concern that adversaries may manipulate the router to consistently select expensive high-capability models. Existing routing attacks depend on either white-box access or heuristic prompts, rendering them ineffective in real-world black-box scenarios. In this work, we propose R²A, which aims to mislead black-box LLM routers to expensive models via adversarial suffix optimization. Specifically, R²A deploys a hybrid ensemble surrogate router to mimic the black-box router. A suffix optimization algorithm is further adapted for the ensemble-based surrogate. Extensive experiments on multiple open-source and commercial routing systems demonstrate that R²A significantly increases the routing rate to expensive models on queries of different distributions. Code and examples: https://github.com/thcxiker/R2A-Attack.

---

## 3. 中文摘要翻译

> 成本感知路由（Cost-aware routing）通过动态调度用户查询到不同能力的模型来平衡性能与推理成本。然而，这种路由策略引入了一个新的安全威胁：攻击者可能操纵路由器，使其始终选择昂贵的强大模型。现有路由攻击依赖于白盒访问或启发式提示，在现实世界的黑盒场景中效果不佳。本论文提出R²A方法，通过对抗后缀优化（adversarial suffix optimization）来误导黑盒LLM路由器选择昂贵模型。具体而言，R²A部署了一个混合集成代理路由器（hybrid ensemble surrogate router）来模拟目标黑盒路由器，并设计了针对集成代理的后缀优化算法。在多个开源和商业路由系统上的广泛实验表明，R²A能够显著提高将查询路由到昂贵模型的比例，且对不同分布的查询均有效。代码和示例：https://github.com/thcxiker/R2A-Attack。

---

## 4. 研究背景

### 4.1 大语言模型的发展与成本挑战

近年来，大语言模型（LLM）的发展取得了显著成功，性能随着模型规模的扩大而可预测地提升。例如，Qwen-3-Max拥有超过1万亿参数，大约是前代旗舰模型Qwen-2.5-72B的14倍。然而，用这种最先进的模型服务所有用户查询在计算和经济上都是不可持续的。

### 4.2 成本感知路由的兴起

为平衡性能与成本，成本感知LLM路由（Cost-aware routing）应运而生，其核心思想是将每个查询路由到满足目标质量要求的最小成本模型。这一策略基于一个洞察：只有一小部分请求真正需要昂贵的强大模型，而简单查询可以被更便宜的弱模型有效处理。

成本感知路由已广泛应用于商业系统，如OpenRouter和GPT-5-Auto。

### 4.3 路由攻击的威胁

尽管成本感知路由提高了效率，但它引入了一个自然的安全隐患——路由攻击（Router Attack）：攻击者能否使用通用触发器（如固定后缀）来一致地操纵路由器选择昂贵模型？

### 4.4 现有方法的局限性

已有的路由攻击研究存在明显缺陷：

1. **白盒依赖问题**：Shafran等人（2025）的方法依赖于可访问目标路由器的梯度或架构，这在商业设置中不切实际——商业路由器只暴露最终路由决策

2. **启发式提示局限性**：LifeCycle（Lin et al., 2025b）从高胜率查询中提取模板（如"Below is an instruction..., [query]"）来引导路由器选择昂贵LLM，但这种启发式提示未经严格优化，往往无法一致地操纵各种目标路由器

---

## 5. 核心贡献

本论文的主要贡献可以总结为：

### 5.1 新型攻击问题

首次研究了通过对抗后缀优化将黑盒LLM路由器导向昂贵模型这一新颖问题。

### 5.2 混合集成代理路由器

提出R²A，引入一种新型混合集成代理路由器（Hybrid Ensemble Surrogate Router），在有限的黑盒查询预算下模拟目标路由器，配合针对集成代理定制的对抗后缀优化算法。

### 5.3 广泛的实验验证

在6个数据集、7个开源路由器和2个商业黑盒路由器（GPT-5-Auto和OpenRouter）上进行实验，验证了R²A能有效优化对抗后缀以误导路由器选择昂贵模型。

---

## 6. 研究方法

### 6.1 LLM路由器基础

给定查询$q$，LLM路由器$\mathcal{R}: q \rightarrow \mathbb{R}^{N}$从模型池$\mathcal{M} = \{M_1, \dots, M_N\}$中选择模型。对于成本感知路由，路由器通过求解以下优化问题来最小化推理成本同时满足目标质量约束：

$$\mathcal{R}(q) = \arg\min_{M_i \in \mathcal{M}} \Big(\ell(q, M_i) + \lambda \cdot C(q, M_i)\Big)$$

其中$\ell(q, M_i)$表示模型$M_i$在查询$q$上的预测损失，$C(q, M_i)$是成本得分，$\lambda \geq 0$控制成本得分在路由决策中的权重。

### 6.2 威胁模型

#### 攻击者目标
将路由器误导到选择昂贵模型来回答给定查询。具体地，将模型候选池划分为昂贵的强大模型$\mathcal{M}_{\text{strong}}$和便宜的弱模型$\mathcal{M}_{\text{weak}}$。给定查询$q$使得$\mathcal{R}_t(q) \in \mathcal{M}_{\text{weak}}$，路由器攻击操作$\mathcal{A}$成功当且仅当$\mathcal{R}_t(\mathcal{A}(q)) \in \mathcal{M}_{\text{strong}}$。

#### 攻击者能力
攻击者可以通过追加对抗后缀来修改原始查询。为保持答案质量并使修改最小化，攻击者受限最多追加$\Delta$个token的后缀到查询$q$末尾。

#### 攻击者知识
假设在现实的黑盒设置中，攻击者只能观察到目标路由器对输入查询的决策。攻击者无法访问目标路由器的内部logits、参数或梯度。由于每次查询目标路由器通常会产生财务成本，攻击者被限制最多进行$Q$次查询到$\mathcal{R}_t$。

### 6.3 路由器攻击形式化

目标是找到一个通用的对抗后缀$s^*$，使目标路由器$\mathcal{R}_t$的决策改变为选择昂贵模型。形式化为以下优化问题：

$$s^* = \argmax_{s} \mathbb{E}_{q \sim \mathcal{Q}} \left[ \mathbb{I} \big( \mathcal{R}_t(q \oplus s) \in \mathcal{M}_{\text{strong}} \big) \right]$$

约束条件为$s \in \mathcal{S}$，$|s| \leq \Delta$，其中$\mathcal{Q}$是输入查询分布，$\oplus$表示拼接操作，$\mathbb{I}(\cdot)$是指示函数。

### 6.4 R²A方法框架

R²A的核心思想是在黑盒设置下，首先训练代理路由器模拟目标路由器行为，然后用代理路由器优化通用对抗后缀。

### 6.5 混合集成代理路由器（Hybrid Ensemble Surrogate Router）

#### 设计动机
由于目标路由器设计未知，依赖单一架构可能导致架构不匹配，从而产生较差的代理。因此，R²A构建了一个混合集成代理路由器，结合多种预训练开源路由器和可训练的轻量级路由器。

#### 混合集成代理的优势
1. **快速匹配**：通过引入开源路由器，R²A可以快速识别与目标行为匹配 existing路由器（或线性组合），减少所需查询
2. **处理显著差异**：通过优化可训练的轻量级路由器，R²A可以处理与所有预训练开源路由器显著不同的目标路由器

#### 可训练的轻量级路由器设计
轻量级路由器$\mathcal{R}_l$从查询的嵌入$E(q) \in \mathbb{R}^d$预测目标路由器的决策。使用All-MiniLM-L6-v2作为编码器（$d=384$）。

为减少参数量，采用LoRA风格低秩约束，将变换分解为两个较小的矩阵：
- $\mathbf{W}_l^1 \in \mathbb{R}^{d \times r}$
- $\mathbf{W}_l^2 \in \mathbb{R}^{r \times |\mathcal{M}_t|}$

其中秩$r \ll d$。轻量级路由器的logits计算为：
$$\mathbf{z}_l = E(q) \mathbf{W}_l^1 \mathbf{W}_l^2$$

#### 开源路由器的结合
R²A结合多个具有不同路由机制的开源路由器：$\{\mathcal{R}_o^{(1)}, \dots, \mathcal{R}_o^{(K)}}$。由于开源路由器的模型池与目标路由器的模型池不一致，R²A将它们的logits映射到所有开源模型池的并集$\mathcal{M}_{\text{uni}} = \bigcup_{k=1}^{K} \mathcal{M}_o^{(k)}$，并应用零填充处理缺失的候选。

形式上，对于开源路由器$\mathcal{R}_o^{(k)}$，扩展其logit向量为：
$$\mathbf{z}_{\text{uni}}^{(k)} = [\tilde{z}_1^{(k)}, \dots, \tilde{z}_{|\mathcal{M}_{\text{uni}}|}^{(k)}]$$

其中：
$$\tilde{z}_i^{(k)} = \begin{cases} z_{M_i}^{(k)}, & \text{if } M_i \in \mathcal{M}_o^{(k)} \\ 0, & \text{otherwise} \end{cases}$$

由于开源路由器的并集模型池$\mathcal{M}_{\text{uni}}$通常与目标池$\mathcal{M}_t$不同，应用线性映射来对齐它们的logits：
$$\mathbf{z}_o^{(k)} = \mathbf{W}_o \cdot \mathbf{z}_{\text{uni}}^{(k)}$$

其中$\mathbf{W}_o \in \mathbb{R}^{|\mathcal{M}_{\text{uni}}| \times |\mathcal{M}_t|}$是投影矩阵。

#### 集成路由结果
集成路由结果通过加权求和计算：
$$\hat{y} = \text{softmax}\left( \alpha_0 \mathbf{z}_l + \sum_{i=1}^{K} \alpha_i \mathbf{z}_o^{(k)} \right)$$

其中$\alpha_i$是满足$\alpha_i \geq 0$和$\sum_{i=0}^{K} \alpha_i = 1$的可学习集成权重。

#### 代理路由器训练
为训练代理路由器，查询黑盒目标$\mathcal{R}_{\text{target}}$生成训练标签。根据威胁模型，限制为$Q$次查询。代理训练目标通过最小化以下损失优化参数$\theta = \{\mathbf{W}_l^1, \mathbf{W}_l^2, \mathbf{W}_o, \{\alpha_i\}_{i=0}^K\}$：
$$\min_{\theta} \mathcal{L}_S = \frac{1}{Q} \sum_{i=1}^{Q} l(\hat{y}(q_i), \mathcal{R}_t(q_i))$$

其中$l(\cdot)$是交叉熵损失，$\hat{y}(q_i)$和$\mathcal{R}_t(q_i)$分别是代理和目标路由器对查询$q_i \in \mathcal{D}_{\text{proxy}}$的预测。

### 6.6 对抗后缀优化（Adversarial Suffix Optimization）

#### 优化目标
利用混合集成代理路由器，对抗后缀优化可以重新表述为：
$$\min_s \mathcal{L}_A = -\mathbb{E}_{q \sim \mathcal{Q}} \sum_{M \in \mathcal{M}_{\text{strong}}} p(\hat{y} = M | q \oplus s)$$

其中$p(\hat{y} = M | q \oplus s)$表示代理路由器预测查询$q$追加对抗后缀$s$后被路由到模型$M$的概率。

#### 后缀Token梯度的聚合
通过链式法则分析token梯度。令$\mathbf{z}_{\text{total}} = \sum_{k=0}^{K} \alpha_k \mathbf{z}^{(k)}$表示集成logits。对于第$k$个路由器，关于token $s_i$的梯度计算为：
$$g_i^{(k)} = \frac{\partial \mathcal{L}_A}{\partial \mathbf{z}_{\text{total}}} \cdot \underbrace{\frac{\partial \mathbf{z}_{\text{total}}}{\partial \mathbf{z}^{(k)}}_{\alpha_k} \cdot \frac{\partial \mathbf{z}^{(k)}}{\partial s_i} = \alpha_k \cdot \frac{\partial \mathcal{L}_A}{\partial \mathbf{z}_{\text{total}}} \frac{\partial \mathbf{z}^{(k)}}{\partial s_i}$$

对于项$\delta_i^{(k)} = \frac{\partial \mathbf{z}^{(k)}}{\partial s_i}$，虽然它有效地捕获了单个路由器内的token敏感度，但其幅度在不同架构间可能变化很大。因此，直接求和$g_i^{(k)}$会导致特定成员路由器主导优化。

为缓解此偏差，通过min-max归一化将$\delta_i^{(k)}$归一化到$[0,1]$范围：
$$\tilde{\delta}_i^{(k)} = \frac{\delta_i^{(k)} - \delta_{\text{min}}^{(k)}}{\delta_{\text{max}}^{(k)} - \delta_{\text{min}}^{(k)}}$$

---

## 7. 实验设置

### 7.1 数据集

在6个数据集上进行实验，包括不同分布的查询。

### 7.2 目标路由器

实验涵盖7个开源路由器和2个商业黑盒路由器：
- **商业路由器**：GPT-5-Auto、OpenRouter
- **开源路由器**：多个具有不同路由机制的开源方法

### 7.3 基线方法对比

将R²A与多种基线方法进行对比，包括：
- 启发式提示方法（如LifeCycle）
- 其他黑盒攻击方法

---

## 8. 实验结果

### 8.1 主要结果

实验表明R²A能够：
1. 显著提高将查询路由到昂贵模型的比例
2. 在不同分布的查询上均有效
3. 在商业路由器（GPT-5-Auto和OpenRouter）上表现出色

### 8.2 泛化能力

R²A的对抗后缀能够有效泛化到多样的路由器，展现出强大的迁移能力。

### 8.3 有限查询预算下的有效性

即使在严格的查询预算限制下，R²A仍能构建有效的代理路由器并生成高效的对抗后缀。

---

## 9. 策略示例

### 9.1 简单查询的路由攻击示例

以简单的事实查询"What is the capital of France?"为例：
- 正常情况下，路由器识别为低复杂度，选择弱模型Mistral 8x7B
- 追加学习到的对抗后缀后，路由器重新路由该查询到昂贵的强大模型

### 9.2 对抗后缀格式

攻击者追加的后缀格式示例：
```
Below is an instruction..., [query][learned adversarial suffix]
```

通过这种最小修改（仅追加后缀），攻击者可以保持原始查询的语义同时实现路由攻击。

---

## 10. 攻击流程

### 10.1 阶段一：代理路由器训练

1. **数据收集**：在查询预算$Q$限制下，向目标路由器发送查询，获取路由决策作为训练标签
2. **初始化**：构建混合集成代理路由器，结合多个开源路由器和可训练的轻量级路由器
3. **联合训练**：联合学习所有路由器的集成权重和轻量级路由器的参数，最小化代理与目标路由器的交叉熵损失

### 10.2 阶段二：对抗后缀优化

1. **梯度聚合**：对于集成代理中的多个路由器，计算每个token的梯度并进行归一化聚合
2. **贪婪替换**：使用GCG风格的贪婪坐标替换，逐步优化后缀token
3. **迭代优化**：多轮迭代优化直至达到目标攻击成功率或达到最大token预算$\Delta$

### 10.3 阶段三：攻击部署

将学习到的通用对抗后缀追加到任意查询，触发路由器选择昂贵模型。

---

## 11. 消融实验

### 11.1 混合集成代理的效果

通过消融实验验证混合集成设计的效果：
- 仅使用单一开源路由器 → 代理效果差
- 仅使用可训练轻量级路由器 → 需要更多查询
- 混合集成代理 → 在有限预算下最佳效果

### 11.2 梯度聚合策略的影响

- 直接梯度求和 → 被特定路由器主导
- 归一化梯度聚合 → 各路由器贡献均衡，效果最佳

### 11.3 查询预算的影响

随着可用查询预算的增加，代理路由器的保真度提升，攻击成功率提高。

---

## 12. 局限性

### 12.1 黑盒假设的实践限制

虽然R²A在黑盒设置下有效，但在某些商业路由器（如GPT-5-Auto）上，路由决策不可观察，只能在OpenRouter上学习后缀并迁移到GPT-5-Auto。

### 12.2 查询分布依赖

对抗后缀的泛化能力依赖于查询分布$\mathcal{Q}$，在显著偏离训练分布的查询上效果可能下降。

### 12.3 防御可能性

本文未探讨针对此类路由攻击的防御策略，未来工作可以研究对抗后缀检测或阻止路由操纵的防御方法。

---

## 13. 伦理声明

本论文属于红队测试（Red Teaming）研究，旨在揭示成本感知LLM路由系统的安全脆弱性。所有攻击实验仅在受控环境中进行，未对真实商业系统造成实际影响。研究结果有助于：
1. 提高LLM服务提供商对路由攻击威胁的认识
2. 推动安全路由机制的设计
3. 促进负责任的AI系统部署

作者遵循负责任的漏洞披露原则，在论文中公开研究成果以便社区能够采取措施防御此类攻击。

---

## 14. 参考文献

1. Aggarwal et al. (2025). Cost-aware routing methods for LLM services.
2. Dong et al. (2018). Efficient blind-box adversarial attack methods.
3. Hu et al. (2022). LoRA: Low-rank adaptation for large language models.
4. Kaplan et al. (2020). Scaling laws for neural language models.
5. Lin et al. (2025b). LifeCycle: Heuristic prompts for router manipulation.
6. Liu et al. (2017). ZOO: Black-box adversarial attack methods.
7. Lu et al. (2024). Cost-aware LLM routing strategies.
8. Ong et al. (2025). Analysis of cost-quality tradeoff in LLM routing.
9. Shafran et al. (2025). White-box routing attack methods.
10. Wang et al. (2020). All-MiniLM-L6-v2 sentence encoder.
11. Zou et al. (2023). GCG: Greedy coordinate gradient for adversarial attack.
12. Additional references in original paper.

---

*本文档由 LLM Safety Paper Reading Bot 自动生成*
*生成时间: 2026-05-30*