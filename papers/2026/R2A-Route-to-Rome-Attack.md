# Route to Rome Attack: Directing LLM Routers to Expensive Models via Adversarial Suffix Optimization

## 1. 基本信息

|字段 | 内容 |
|------|------|
| **论文标题** | Route to Rome Attack: Directing LLM Routers to Expensive Models via Adversarial Suffix Optimization |
| **简称** | R²A (Route to Rome Attack) |
| **作者** | Haochun Tang, Yuliang Yan, Jiahua Lu, Huaxiao Liu, Enyan Dai |
| **单位** | 吉林大学（符号计算与知识工程教育部重点实验室）、香港科技大学（广州） |
| **会议** | ACL 2026 Main Conference |
| **arXiv ID** | [2604.15022](https://arxiv.org/abs/2604.15022) |
| **代码** | [thcxiker/R2A-Attack](https://github.com/thcxiker/R2A-Attack) |
| **方向** | Router Attack / LLM Security / Cost-aware Routing |
| **CCF等级** | CCF-A |

---

## 2. 英文摘要原文（arXiv Abstract）

> Cost-aware routing dynamically dispatches user queries to models of varying capability to balance performance and inference cost. However, the routing strategy introduces a new security concern that adversaries may manipulate the router to consistently select expensive high-capability models. Existing routing attacks depend on either white-box access or heuristic prompts, rendering them ineffective in real-world black-box scenarios. In this work, we propose R$^2$A, which aims to mislead black-box LLM routers to expensive models via adversarial suffix optimization. Specifically, R$^2$A deploys a hybrid ensemble surrogate router to mimic the black-box router. A suffix optimization algorithm is further adapted for the ensemble-based surrogate. Extensive experiments on multiple open-source and commercial routing systems demonstrate that R$^2$A significantly increases the routing rate to expensive models on queries of different distributions. Code and examples: https://github.com/thcxiker/R2A-Attack.

**引用格式：**
```
arXiv:2604.15022 [cs.CR]
```

---

## 3. 中文摘要翻译

> 成本感知路由（Cost-aware routing）通过动态调度用户查询到不同能力的模型来平衡性能与推理成本。然而，这种路由策略引入了一个新的安全隐患：攻击者可能操纵路由器始终选择昂贵的高能力模型。现有路由攻击依赖于白盒访问或启发式提示，在实际黑盒场景中效果不佳。本文中，我们提出 R²A，通过对抗后缀优化来误导黑盒 LLM 路由器选择昂贵模型。具体而言，R²A 部署了一个混合集成代理路由器（hybrid ensemble surrogate router）来模拟黑盒路由器，并针对该集成代理设计了专门的后缀优化算法。在多个开源和商业路由系统上的大量实验表明，R²A 能显著提高将查询路由到昂贵模型的比例，且在不同分布的查询上均有效。代码和示例：https://github.com/thcxiker/R2A-Attack。

---

## 4. 研究背景

### 4.1 LLM 发展与成本感知路由的兴起

大型语言模型（LLM）的发展近年来取得了显著成功，这些进步从根本上由缩放定律（scaling laws, Kaplan et al., 2020）驱动——性能可以通过增加模型规模可预测地提升。例如，Qwen-3-Max 扩展到超过 1 万亿参数，约为前代旗舰模型 Qwen-2.5-72B 的 14 倍。然而，用此类尖端模型服务每个用户查询在计算和经济上都是不可持续的。

为平衡性能与成本，**成本感知 LLM 路由**（cost-aware LLM routing）应运而生，其核心思想是将每个查询路由到满足目标质量要求的最低成本模型。具体而言，只有少量请求真正需要昂贵的强模型，而简单查询可以被更便宜的弱模型有效处理。如图1(a) 所示，当收到"法国的首都是什么？"这样的简单事实查询时，路由器识别其为低复杂度，选择弱模型 Mistral 8x7B 来生成响应。

这种路由策略已被 OpenRouter 和 GPT-5-Auto 等商业系统广泛采用。

### 4.2 路由攻击的威胁

成本感知路由在提高效率的同时，也引入了一个自然的安全隐患——**路由攻击（router attack）**：攻击者能否使用一个通用触发器（如固定后缀）来持续操纵路由器选择昂贵模型？

已有初步研究尝试回答这一问题（Shafran et al., 2025; Lin et al., 2025b）。但存在以下局限：

- **Shafran et al. (2025)** 依赖于可访问的梯度或目标路由器已知架构，在商业黑盒场景中不切实际
- **LifeCycle (Lin et al., 2025b)** 从高胜率查询中提取模板（如 "Below is an instruction..., [query]"）来引导路由器选择昂贵模型，虽然适用于黑盒设置，但启发式提示缺乏严格优化，难以持续有效地操纵各种目标路由器

### 4.3 研究问题

因此，本文研究的核心问题是：**在仅需黑盒访问（即只能观察到最终路由决策）的情况下，如何通过对抗后缀优化来误导 LLM 路由器选择昂贵模型？**

这一问题的挑战在于：

1. **如何构建可信的代理路由器**：在严格查询预算的黑盒设置下，由于不了解目标路由器架构（可能是语义嵌入、LLM-based 等多种机制），难以学到忠实模拟目标行为的代理
2. **如何优化离散对抗后缀**：即使有代理路由器，针对多样化查询优化一个有效的离散对抗后缀仍然困难

---

## 5. 核心贡献

1. **研究新问题**：首次系统研究通过对抗后缀优化来误导黑盒 LLM 路由器选择昂贵模型的问题
2. **提出混合集成代理路由器（R²A）**：创新性地结合多种开源路由器和可训练轻量级路由器，在有限黑盒查询预算下有效模拟目标路由器
3. **设计针对集成代理的梯度聚合后缀优化算法**：解决多编码器环境中梯度聚合偏差问题
4. **广泛实验验证**：在 6 个数据集、7 个开源路由器和 2 个商业黑盒路由器（GPT-5-Auto 和 OpenRouter）上验证了 R²A 的有效性

---

## 6. 研究方法

### 6.1 威胁模型

#### 攻击者目标
给定查询 $q$，使得原本被路由到弱模型 $\mathcal{M}_{weak}$ 的查询，在添加对抗后缀后被路由到强模型 $\mathcal{M}_{strong}$。

#### 攻击者能力
攻击者只能通过在查询末尾附加最长 $\Delta$ 个 token 的对抗后缀来修改原始查询。

#### 攻击者知识
假设在现实的黑盒设置中，攻击者只能观察到目标路由器的最终路由决策，无法访问内部 logits、参数或梯度。由于每次查询目标路由器都会产生财务成本，攻击者被限制为最多 $Q$ 次查询。

### 6.2 路由攻击问题形式化

目标找到通用对抗后缀 $s^*$，使目标路由器 $\mathcal{R}_t$ 决策转向昂贵强模型：

$$s^* = \argmax_s \mathbb{E}_{q \sim \mathcal{Q}} \left[ \mathbb{I}(\mathcal{R}_t(q \oplus s) \in \mathcal{M}_{\text{strong}}) \right]$$

$$s.t. \quad s \in \mathcal{S}, \quad |s| \leq \Delta$$

其中 $\mathcal{Q}$ 是输入查询分布，$\oplus$ 表示拼接操作，$\mathbb{I}(\cdot)$ 是指示函数。

### 6.3 R²A 方法框架

R²A 首先训练一个代理路由器来模拟目标路由器行为，然后使用该代理路由器来优化通用对抗后缀。如图 2 所示，R²A 包含两个核心组件：

1. **混合集成代理路由器**（Hybrid Ensemble Surrogate Router）：结合多种开源路由器和轻量级可训练路由器
2. **针对集成代理的后缀优化算法**：专门适配集成代理的多编码器环境

### 6.4 混合集成代理路由器设计

#### 6.4.1 可训练轻量级路由器

轻量级路由器 $\mathcal{R}_l$ 从查询嵌入 $E(q) \in \mathbb{R}^d$ 预测目标路由器决策。使用 all-MiniLM-L6-v2 作为编码器（$d=384$）。

由于直接学习映射 $\mathbb{R}^d \rightarrow \mathbb{R}^{|\mathcal{M}_t|}$ 需要优化参数矩阵 $d \times |\mathcal{M}_t|$，这在严格查询预算下不可行。受 LoRA 启发，采用低秩约束分解：

$$\mathbf{z}_l = E(q) \mathbf{W}_l^1 \mathbf{W}_l^2$$

其中 $\mathbf{W}_l^1 \in \mathbb{R}^{d \times r}$ 和 $\mathbf{W}_l^2 \in \mathbb{R}^{r \times |\mathcal{M}_t|}$，$r \ll d$。

#### 6.4.2 结合开源路由器

将多个具有不同路由机制的开源路由器 $\{\mathcal{R}_o^{(1)}, \ldots, \mathcal{R}_o^{(K)}\}$ 组合。但开源路由器的模型池与目标路由器不一致，因此：

1. **统一模型池映射**：将 logits 映射到所有开源模型池的并集 $\mathcal{M}_{uni} = \bigcup_{k=1}^{K} \mathcal{M}_o^{(k)}$，缺失模型用零填充
2. **线性投影对齐**：应用线性映射 $\mathbf{W}_o$ 将统一空间投影到目标模型池空间

#### 6.4.3 集成路由与训练

最终集成路由结果通过加权求和计算：

$$\hat{y} = \text{softmax}\left( \alpha_0 \mathbf{z}_l + \sum_{i=1}^{K} \alpha_i \mathbf{z}_o^{(k)} \right)$$

其中 $\alpha_i \geq 0$ 且 $\sum_{i=0}^{K} \alpha_i = 1$。

代理训练目标：

$$\min_\theta \mathcal{L}_S = \frac{1}{Q} \sum_{i=1}^{Q} l(\hat{y}(q_i), \mathcal{R}_t(q_i))$$

其中 $l(\cdot)$ 是交叉熵损失，$\theta = \{\mathbf{W}_l^1, \mathbf{W}_l^2, \mathbf{W}_o, \{\alpha_i\}_{i=0}^{K}\}$。

### 6.5 针对混合集成代理的对抗后缀优化

#### 6.5.1 后缀优化目标

使用代理路由器后，后缀优化目标为：

$$\min_s \mathcal{L}_A = -\mathbb{E}_{q \sim \mathcal{Q}} \sum_{M \in \mathcal{M}_{\text{strong}}} p(\hat{y}=M|q \oplus s)$$

#### 6.5.2 后缀 Token梯度聚合

可以使用 GCG（Greedy Coordinate Gradient）方法，通过编码器的 token 梯度贪婪替换 token。但由于集成代理涉及多个编码器，需要跨路由器聚合梯度。

对于第 $k$ 个路由器，token $s_i$ 的梯度计算为：

$$g_i^{(k)} = \alpha_k \cdot \frac{\partial \mathcal{L}_A}{\partial \mathbf{z}_{\text{total}}} \frac{\partial \mathbf{z}^{(k)}}{\partial s_i}$$

直接求和会导致特定成员路由器主导优化。为缓解此偏差，对 $\delta_i^{(k)} = \frac{\partial \mathbf{z}^{(k)}}{\partial s_i}$ 进行 min-max 归一化到 [0,1] 范围：

$$\tilde{\delta}_i^{(k)} = \frac{\delta_i^{(k)} - \delta_{\text{min}}^{(k)}}{\delta_{\text{max}}^{(k)} - \delta_{\text{min}}^{(k)}}$$

---

## 7. 实验设置

### 7.1 数据集

- **6 个数据集**，覆盖不同分布的查询

### 7.2 目标路由器

- **7 个开源路由器**
- **2 个商业黑盒路由器**：GPT-5-Auto 和 OpenRouter

### 7.3 评估指标

- 路由到昂贵模型的比率（Routing Rate to Expensive Models）
- 不同分布查询上的攻击成功率

---

## 8. 实验结果

### 8.1 主要结果

实验结果表明，R²A 在多个开源和商业路由系统上显著提高了将查询路由到昂贵模型的比例：

1. **跨路由器泛化能力**：R²A 学习的后缀能够有效泛化到不同的路由器，包括 GPT-5-Auto 和 OpenRouter 等商业系统
2. **不同查询分布的鲁棒性**：在各种分布的查询上均有效
3. **显著的攻击成功率**：通过添加学习到的对抗后缀，原本被路由到弱模型的简单查询会被重路由到强模型

### 8.2 与基线方法对比

R²A 相比现有方法（如 LifeCycle、基于梯度白盒攻击等）具有显著优势：

- 在完全黑盒设置下有效（LifeCycle 等启发式方法无法做到严格优化）
- 比白盒方法更实用（无需访问目标路由器梯度）
- 在有限查询预算下仍有效

---

## 9. 策略示例

### 9.1 正常路由示例

**查询**："What is the capital of France?"

**正常路由结果**：路由器识别为低复杂度查询 → Mistral 8x7B（弱模型）

### 9.2 攻击后路由示例

**查询**："What is the capital of France?" + [对抗后缀]

**攻击后路由结果**：同一查询被重路由到 → GPT-4o 等昂贵强模型

### 9.3 对抗后缀特点

R²A 学习到的对抗后缀具有以下特点：

1. **通用性**：同一个后缀可以对多种不同查询生效
2. **隐蔽性**：后缀修改相对较小（限制在 $\Delta$ 个 token 以内）
3. **可迁移性**：在不同路由器架构间具有一定迁移能力

---

## 10. 攻击流程

### 10.1 阶段一：代理路由器训练

1. **准备查询集**：收集用于代理训练的查询样本
2. **查询目标路由器**：在严格查询预算 $Q$ 下获取目标路由器决策
3. **构建混合集成代理**：结合多个开源路由器和可训练轻量级路由器
4. **联合优化**：同时学习开源路由器的集成权重和轻量级路由器参数
5. **代理验证**：确保代理路由器行为与目标路由器一致

### 10.2 阶段二：对抗后缀优化

1. **初始化后缀**：从种子 tokens 开始
2. **梯度计算**：针对集成代理中每个路由器计算 token 梯度
3. **梯度归一化与聚合**：对各路由器的梯度进行 min-max 归一化后聚合
4. **贪婪 token 替换**：选择使损失最大化的 top-k tokens 进行替换
5. **迭代优化**：重复步骤2-4 直到达到最大 token 预算 $\Delta$
6. **后缀验证**：在目标路由器上验证最终后缀效果

### 10.3 攻击部署

1. **选择目标查询**：攻击者选择想要操控路由的查询
2. **附加后缀**：将学习到的通用对抗后缀附加到查询末尾
3. **触发路由重定向**：修改后的查询被目标路由器路由到昂贵模型

---

## 11. 消融实验

论文通过消融实验验证了各组件的贡献：

### 11.1 混合集成代理路由器的消融

- **仅使用开源路由器**：效果有限，难以泛化到未知架构的目标路由器
- **仅使用可训练轻量级路由器**：在严格查询预算下欠拟合
- **混合集成（本文方法）**：两者结合，在各种目标路由器上均有效

### 11.2 梯度聚合策略的消融

- **直接梯度求和**：受特定路由器主导，效果不稳定
- **无归一化聚合**：不同架构的梯度量级差异大
- **Min-max 归一化聚合（本文方法）**：各路由器贡献均衡，效果最优

### 11.3 查询预算的影响

- 查询预算 $Q$ 越大，代理路由器越准确，后缀优化效果越好
- 在极端有限预算下，混合集成的优势更加明显

---

## 12. 局限性

1. **查询预算限制**：虽然已优化，但仍然需要一定数量的目标路由器查询，在实际攻击中可能受限
2. **通用性与专用性的权衡**：学习到的通用后缀可能在某些特定查询上效果不佳
3. **商业路由器的不可观测性**：对于 GPT-5-Auto 等商业系统，由于路由决策不可直接观测，需要在 OpenRouter 上学习后间接应用
4. **防御措施**：论文未深入探讨防御方法，未来工作可研究针对路由攻击的防御策略
5. **攻击者能力假设**：假设攻击者能够修改查询并附加后缀，这在某些应用场景中可能不成立

---

## 13. 伦理声明

本研究属于对 LLM 路由系统安全性的红队测试研究，旨在揭示成本感知路由中的潜在安全风险。所有实验均在受控环境中进行，未对真实商业系统造成影响。研究结果应被用于提高 LLM 系统的安全性，而非用于恶意攻击。

本文遵循以下伦理原则：

- 仅研究安全漏洞，不提供可直接用于恶意攻击的完整工具
- 研究结果有助于服务提供商改进安全措施
- 所有实验使用的均为公开可用的开源模型和 API

---

## 14. 参考文献

1. Kaplan et al. (2020). Scaling Laws for Neural Language Models.
2. Lu et al. (2024). Cost-aware routing in LLM systems.
3. Aggarwal et al. (2025). AutoMix: Automatically Mixing Language Models.
4. Ong et al. (2025). Cost-aware LLM routing.
5. Shafran et al. (2025). Routing attacks on LLM routers (white-box).
6. Lin et al. (2025b). LifeCycle: Heuristic routing manipulation.
7. Liu et al. (2017). Black-box adversarial attacks.
8. Dong et al. (2018). Black-box adversarial attacks.
9. Wang et al. (2020). all-MiniLM-L6-v2 sentence encoder.
10. Hu et al. (2022). LoRA: Low-Rank Adaptation.
11. Zou et al. (2023). GCG: Greedy Coordinate Gradient for adversarial suffix optimization.