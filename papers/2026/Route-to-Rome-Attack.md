# Route to Rome Attack: Directing LLM Routers to Expensive Models via Adversarial Suffix Optimization

## 1. 基本信息

| 项目 | 内容 |
|------|------|
| **论文标题** | Route to Rome Attack: Directing LLM Routers to Expensive Models via Adversarial Suffix Optimization |
| **简称** | R²A (Route to Rome Attack) |
| **作者** | Haochun Tang, Yuliang Yan, Jiahua Lu, Huaxiao Liu, Enyan Dai |
| **单位** | 吉林大学（Key Laboratory of Symbolic Computation and Knowledge Engineering, MoE）、香港科技大学（广州） |
| **arXiv ID** | 2604.15022 |
| **会议** | ACL 2026 Main Conference |
| **GitHub** | https://github.com/thcxiker/R2A-Attack |
| **提交时间** | 2026年4月16日 |
| **研究方向** | LLM路由器安全、路由攻击、对抗后缀优化 |
| **CCF等级** | CCF-A |

---

## 2. 英文摘要原文（arXiv abstract原文）

> **Cost-aware routing** dynamically dispatches user queries to models of varying capability to balance performance and inference cost. However, the routing strategy introduces a new security concern that adversaries may manipulate the router to consistently select expensive high-capability models. Existing routing attacks depend on either white-box access or heuristic prompts, rendering them ineffective in real-world black-box scenarios. In this work, we propose **R²A**, which aims to mislead black-box LLM routers to expensive models via **adversarial suffix optimization**. Specifically, R²A deploys a **hybrid ensemble surrogate router** to mimic the black-box router. A suffix optimization algorithm is further adapted for the ensemble-based surrogate. Extensive experiments on multiple open-source and commercial routing systems demonstrate that R²A significantly increases the routing rate to expensive models on queries of different distributions. Code and examples: this https URL.

**引用信息（arXiv）：**
```
arXiv:2604.15022 [cs.CR]
Journal reference: ACL 2026 Main Conference
Authors: Haochun Tang, Yuliang Yan, Jiahua Lu, Huaxiao Liu, Enyan Dai
Submitted: Thu, 16 Apr 2026
```

---

## 3. 中文摘要翻译

> **成本感知路由**（Cost-aware routing）是一种动态调度用户查询至不同能力级别模型的策略，旨在平衡性能与推理成本。然而，这一路由策略引入了一个新的安全威胁：攻击者可能操纵路由器持续选择昂贵的高能力模型。现有路由攻击依赖白盒访问或启发式提示，使得它们在现实黑盒场景中无效。在本文中，我们提出了**R²A**（Route to Rome Attack），通过**对抗后缀优化**来误导黑盒LLM路由器选择昂贵模型。具体而言，R²A部署了一个**混合集成替代路由器**（hybrid ensemble surrogate router）来模拟黑盒路由器的行为，并进一步为该集成替代路由器适配了后缀优化算法。在多个开源和商业路由系统上的广泛实验表明，R²A能够显著提高在不同分布查询上路由至昂贵模型的比率。代码和示例已开源。

---

## 4. 研究背景

### 4.1 LLM路由器的兴起

近年来，大型语言模型（LLM）的发展由缩放定律（Scaling Laws, Kaplan et al., 2020）驱动，性能随模型规模增大可预测地提升。例如，Qwen-3-Max扩展至超过1万亿参数，约为前代Qwen-2.5-72B的14倍。然而，为每个用户查询都部署最先进模型在计算和经济上均不可持续。

**成本感知路由**（Cost-aware Routing）应运而生，其核心思想是：只有一小部分请求真正需要昂贵的高能力模型，而简单查询可以由便宜的弱模型有效处理。商业系统如OpenRouter和GPT-5-Auto已广泛采用这种路由策略。

在路由系统中，当路由器收到简单的事实性问题"法国的首都是什么？"时，它识别出这是低复杂度查询，选择较弱的Mistral 8x7B模型来生成回答，从而节省成本。

### 4.2 路由攻击的威胁模型

成本感知路由引入了一个自然的安全问题：**路由攻击**（Router Attack）。攻击者的目标是使用通用触发器（如固定后缀）来持续操纵路由器选择昂贵模型。这可能导致：

1. **经济损失**：攻击者通过强制路由到昂贵模型来浪费目标用户的预算
2. **服务降级**：在高负载时强制路由到慢速模型造成延迟
3. **资源耗尽**：耗尽目标组织的计算预算

### 4.3 现有方法的局限性

| 方法 | 依赖条件 | 局限性 |
|------|----------|--------|
| Shafran et al. (2025) | 白盒访问（梯度/架构） | 商业黑盒路由器无法提供这些信息 |
| LifeCycle (Lin et al., 2025b) | 启发式提示模板 | 非严格优化，无法持续有效操纵各种路由器 |
| Chain-of-Thought | 简单提示工程 | 效果有限，缺乏系统性 |

**核心问题**：在现实黑盒场景中，攻击者只能观察到路由器的最终路由决策，无法访问其内部参数、梯度或架构。那么，如何仅通过查询黑盒路由器来优化对抗后缀？

---

## 5. 核心贡献

论文的三大核心贡献：

1. **新问题定义**：首次系统研究了在严格黑盒设置下，通过对抗后缀优化将LLM路由器引导至昂贵模型的问题。

2. **混合集成替代路由器（R²A）**：提出了一种结合多种开源路由器和轻量级可训练路由器的混合集成替代路由器，在有限查询预算下有效模拟目标黑盒路由器行为。

3. **适配于集成替代的梯度聚合算法**：设计了专门用于聚合多个路由器梯度（包括语义嵌入路由器和LLM-based路由器）的后缀优化算法，解决了不同架构间梯度规模异质性问题。

---

## 6. 研究方法

### 6.1 问题形式化

**LLM路由器定义**：给定查询 $q$，路由器 $\mathcal{R}: q \rightarrow \mathbb{R}^N$ 从模型池 $\mathcal{M} = \{M_1, ..., M_N\}$ 中选择模型。成本感知路由的目标是最小化推理成本同时满足目标质量约束：

$$\mathcal{R}(q) = \arg\min_{M_i \in \mathcal{M}} \Big( \ell(q, M_i) + \lambda \cdot C(q, M_i) \Big)$$

其中 $\ell(q, M_i)$ 是模型 $M_i$ 在查询 $q$ 上的预测损失，$C(q, M_i)$ 是成本分数，$\lambda \geq 0$ 控制成本权重。

**攻击者目标**：给定原本路由至弱模型 $\mathcal{R}_t(q) \in \mathcal{M}_{weak}$ 的查询 $q$，攻击操作 $\mathcal{A}$ 成功当且仅当 $\mathcal{R}_t(\mathcal{A}(q)) \in \mathcal{M}_{strong}$。

**攻击者能力**：攻击者只能在查询末尾附加最多 $\Delta$ 个token的对抗后缀 $s$，以保持答案质量且修改最小化。

**攻击者知识**：严格的**黑盒设置**——攻击者只能观察目标路由器对输入查询的路由决策，无法访问内部logit、参数或梯度。每个查询目标路由器都需支付费用，攻击者被限制为最多 $Q$ 次查询。

**路由攻击的优化目标**：

$$s^* = \arg\max_{s} \mathbb{E}_{q \sim \mathcal{Q}} \left[ \mathbb{I}(\mathcal{R}_t(q \oplus s) \in \mathcal{M}_{strong}) \right]$$

约束条件：$s \in \mathcal{S}$，$|s| \leq \Delta$

### 6.2 混合集成替代路由器（Hybrid Ensemble Surrogate Router）

由于目标路由器设计未知，依赖单一架构可能导致架构不匹配。R²A构建了一个混合集成替代路由器 $\mathcal{R}_s$，结合多种预训练开源路由器和可训练的轻量级路由器。

#### 6.2.1 可训练轻量级路由器设计

轻量级路由器 $\mathcal{R}_l$ 的目标是从查询的嵌入 $E(q) \in \mathbb{R}^d$ 预测目标路由器的决策。使用 all-MiniLM-L6-v2 作为编码器（$d=384$）。

直接学习线性映射 $\mathbb{R}^d \rightarrow \mathbb{R}^{|\mathcal{M}_t|}$ 需要优化参数矩阵规模为 $d \times |\mathcal{M}_t|$，训练需求超过严格查询预算。

受LoRA（Hu et al., 2022）启发，施加低秩约束，将变换分解为两个小矩阵：

$$\mathbf{z}_l = E(q) \mathbf{W}_l^1 \mathbf{W}_l^2$$

其中 $\mathbf{W}_l^1 \in \mathbb{R}^{d \times r}$，$\mathbf{W}_l^2 \in \mathbb{R}^{r \times |\mathcal{M}_t|}$，秩 $r \ll d$。低秩分解大幅减少了训练路由器所需的查询数量。

#### 6.2.2 开源路由器集成

R²A将具有多样化路由机制的多个开源路由器 $\{ \mathcal{R}_o^{(1)}, ..., \mathcal{R}_o^{(K)} \}$ 结合起来，减少替代路由器与目标路由器之间的机制不匹配。

由于开源路由器的模型池 $\{ \mathcal{M}_o^{(1)}, ..., \mathcal{M}_o^{(K)} \}$ 与目标路由器的模型池 $\mathcal{M}_t$ 不一致，应用线性映射对齐它们的logit：

$$\mathbf{z}_o^{(k)} = \mathbf{W}_o \cdot \mathbf{z}_{uni}^{(k)}$$

其中 $\mathbf{W}_o \in \mathbb{R}^{|\mathcal{M}_{uni}| \times |\mathcal{M}_t|}$ 是投影矩阵，$\mathbf{z}_{uni}^{(k)}$ 是扩展至所有开源模型并集 $\mathcal{M}_{uni} = \bigcup_{k=1}^{K} \mathcal{M}_o^{(k)}$ 的logit向量。

#### 6.2.3 集成与替代路由器训练

集成路由结果通过加权求和计算：

$$\hat{y} = \text{softmax}(\alpha_0 \mathbf{z}_l + \sum_{i=1}^{K} \alpha_i \mathbf{z}_o^{(k)})$$

其中 $\alpha_i$ 是满足 $\alpha_i \geq 0$ 和 $\sum_{i=0}^{K} \alpha_i = 1$ 的可学习集成权重。

替代路由器训练目标：最小化替代路由器与目标路由器路由决策之间的交叉熵损失

$$\min_{\theta} \mathcal{L}_S = \frac{1}{Q} \sum_{i=1}^{Q} l(\hat{y}(q_i), \mathcal{R}_t(q_i))$$

参数 $\theta = \{ \mathbf{W}_l^1, \mathbf{W}_l^2, \mathbf{W}_o, \{ \alpha_i \}_{i=0}^{K} \}$。

### 6.3 对抗后缀优化算法

基于混合集成替代路由器，对抗后缀优化重新形式化为：

$$\min_s \mathcal{L}_A = -\mathbb{E}_{q \sim \mathcal{Q}} \sum_{M \in \mathcal{M}_{strong}} p(\hat{y} = M | q \oplus s)$$

#### 6.3.1 后缀Token梯度的聚合

由于集成替代涉及多个编码器，需要跨路由器聚合梯度。令 $\mathbf{z}_{total} = \sum_{k=0}^{K} \alpha_k \mathbf{z}^{(k)}$ 表示集成logit。

第 $k$ 个路由器对token $s_i$ 的梯度：

$$g_i^{(k)} = \frac{\partial \mathcal{L}_A}{\partial \mathbf{z}_{total}} \cdot \underbrace{\frac{\partial \mathbf{z}_{total}}{\partial \mathbf{z}^{(k)}}}_{\alpha_k} \cdot \frac{\partial \mathbf{z}^{(k)}}{\partial s_i} = \alpha_k \cdot \frac{\partial \mathcal{L}_A}{\partial \mathbf{z}_{total}} \frac{\partial \mathbf{z}^{(k)}}{\partial s_i}$$

#### 6.3.2 梯度归一化问题

对于单个路由器，梯度项 $\delta_i^{(k)} = \frac{\partial \mathbf{z}^{(k)}}{\partial s_i}$ 有效捕获了token敏感性，但其幅度在不同架构间差异很大。直接求和 $g_i^{(k)}$ 会导致特定成员路由器主导优化。

通过min-max归一化解决：

$$\tilde{\delta}_i^{(k)} = \frac{\delta_i^{(k)} - \delta_{min}^{(k)}}{\delta_{max}^{(k)} - \delta_{min}^{(k)}}$$

归一化后聚合梯度：

$$\tilde{g}_i = \sum_{k=0}^{K} \alpha_k \cdot \tilde{\delta}_i^{(k)} \cdot \frac{\partial \mathcal{L}_A}{\partial \mathbf{z}_{total}}$$

#### 6.3.3 后缀优化算法流程

1. **初始化**：从第一个查询开始优化（$m_c = 1$）
2. **迭代优化**：
   - 对每个后缀位置 $i$，计算聚合梯度得分 $\tilde{g}_i$
   - 选取Top-K候选token集合 $C_i$
   - 采样 $B$ 个变体，通过从 $C_i$ 随机采样替换随机后缀token
   - 选择损失最低的变体更新 $s$
3. **递增式查询激活**：当当前后缀在前 $m_c$ 个查询上成功时，激活下一个查询（$m_c \leftarrow m_c + 1$）

---

## 7. 实验设置

### 7.1 目标路由器

测试了9个目标路由器：

| 路由器类型 | 名称 |
|-----------|------|
| 开源路由器 | RouteLLM-Bert, GraphRouter, P2L, RouterDC, RouteLLM-MF |
| 商业路由器 | OpenRouter（真实商业系统）, GPT-5-Auto |

集成池包含5个开源路由器。当目标路由器出现在集成池中时，先将其从集成池移除再训练替代路由器，以严格分离目标和替代路由器，防止数据泄露。

### 7.2 数据集

**分布内（In-Distribution）**：

| 数据集 | 用途 |
|--------|------|
| MMLU | 替代模型训练、分布内泛化评估 |
| GSM8K | 替代模型训练、后缀优化 |
| MT-Bench | 分布内泛化评估 |

每个数据集分为三个不相交的子集：$\mathcal{D}_{proxy}$（替代训练）、$\mathcal{D}_{suffix}$（后缀优化）、$\mathcal{D}_{eval}$（分布内评估）。查询预算统一设为120。

**分布外（Out-of-Distribution）**：

| 数据集 | 用途 |
|--------|------|
| SimpleQA | 分布外泛化评估 |
| ArenaHard | 分布外泛化评估 |
| RArena | 分布外泛化评估 |

分布外查询既不用于替代训练也不用于后缀优化。

### 7.3 基线方法

| 基线 | 描述 |
|------|------|
| **Rerouting** (Shafran et al., 2025) | 基于爬山发现查询无关对抗触发器，最大化路由器复杂度分数 |
| **LifeCycle (W)** | 通过梯度访问优化触发器以最大化强模型选择 |
| **LifeCycle (B)** | 从高胜率查询中提取固定领域无关触发器 |
| **Chain-of-Thought (CoT)** | 添加"Let's think step by step"增加感知推理复杂度 |
| **Clean** | 无攻击的原始查询 |

### 7.4 评估指标

**攻击成功率（Attack Success Rate, ASR）**：

$$ASR(s) = \frac{1}{|\mathcal{D}|} \sum_{q \in \mathcal{D}} \mathbb{I} \left( \mathcal{R}_t(q \oplus s) \in \mathcal{M}_{strong} \right)$$

ASR衡量附加后缀后查询被路由至高能力模型的比例，ASR越高表示攻击越有效。

---

## 8. 实验结果

### 8.1 主要结果：R²A持续优于所有基线

在6个数据集和9个路由器上的完整结果如下（以ASR衡量，数值越高越好）：

| 目标路由器 | Clean | LifeCycle (W) | LifeCycle (B) | Rerouting | CoT | **R²A (Ours)** |
|-----------|-------|--------------|--------------|-----------|-----|---------------|
| RouteLLM-Bert | 0.40 | 0.69 | 0.53 | 0.77 | 0.52 | **0.89** (+0.49↑) |
| GraphRouter | 0.64 | 0.69 | 0.60 | 0.63 | 0.65 | **0.87** (+0.23↑) |
| P2L | 0.67 | 0.67 | 0.66 | 0.59 | 0.74 | **0.74** (+0.07↑) |
| RouterDC | 0.72 | 0.90 | 0.91 | 0.87 | 0.79 | **0.94** (+0.22↑) |
| RouteLLM-MF | 0.56 | 0.77 | 0.64 | 0.88 | 0.54 | **0.95** (+0.39↑) |
| OpenRouter* | 0.27 | 0.44 | 0.42 | 0.44 | 0.42 | **0.74** (+0.47↑) |

> *OpenRouter是真实商业黑盒路由器

**关键发现**：

1. **SOTA性能**：R²A在所有路由器上均达到最先进的攻击成功率，大幅超越先前对抗方法
2. **跨路由器泛化**：R²A在分布内和分布外数据集上均维持高ASR，表明学习到的对抗后缀具有强泛化能力
3. **商业系统有效性**：在真实商业黑盒路由器OpenRouter上，R²A将路由至昂贵模型的比率从27%提升至74%

### 8.2 推理成本分析

**货币成本影响**（OpenRouter API报告）：

| 数据集 | Clean基线成本 | R²A攻击后成本 | 增幅 |
|--------|--------------|--------------|------|
| MMLU | ~1x | ~2.7x | **2.7倍** |
| RouterArena | ~1x | ~2.9x | **2.9倍** |

**攻击成本极低**：收集120个替代训练查询仅需约$0.98美元，而后缀引起的推理成本增加却是成倍的。

### 8.3 GPT-5路由器攻击评估

**设置**：由于GPT-5 Auto接口不暴露路由决策，直接应用在OpenRouter上训练的后缀。

**评估方法**：

1. **响应质量**：在固定GPT-4后端上测试，GSM8K上无性能下降
2. **Thinking模式指纹**：使用Bag-of-Words指纹将响应分类为"像强模型"或"像弱模型"

**结果**：

| 维度 | Clean胜率 | R²A攻击胜率 |
|------|----------|------------|
| 全面性（Comprehensiveness） | 36.0% | 64.0% |
| 多样性（Diversity） | 28.0% | 72.0% |
| 赋能性（Empowerment） | 36.0% | 64.0% |
| 整体（Overall） | 36.0% | 64.0% |

**案例研究**：附加对抗后缀后，路由器从生成简短错误答案切换为多步推理并给出正确答案，暗示R²A成功引导GPT-5路由器选择更强模型。处理时间也显著增加。

### 8.4 空格防御鲁棒性

评估R²A对空格防御（插入空格破坏后缀）的抵抗能力：

| 数据集 | RouteLLM-BERT | GraphRouter | RouterDC |
|--------|--------------|------------|----------|
| MT-Bench | 0.95 (↓0.00) | 0.71 (↓0.02) | 1.00 (0.00) |
| ArenaHard | 0.81 (↓0.03) | 0.73 (↓0.10) | 1.00 (0.00) |

R²A对空格防御展现出良好的抵抗能力，性能仅轻微下降。

---

## 9. 策略示例

### 9.1 攻击成功示例

**简单事实性问题**："法国的首都是什么？"

- **Clean路由**：Mistral 8x7B（弱模型，廉价）
- **R²A攻击后路由**：GPT-4o / Claude-3-Opus（强模型，昂贵）

### 9.2 后缀形式

R²A学习到的对抗后缀是**固定的通用字符串**，可以附加到任何简单查询末尾。形式上类似于：

```
[学习到的对抗后缀示例结构]
```

### 9.3 跨模型池迁移

由于使用了混合集成替代路由器，R²A学到的后缀能够泛化到：
- 不同的开源路由器（RouteLLM vs. GraphRouter）
- 不同的模型池配置
- 商业黑盒路由器（OpenRouter, GPT-5-Auto）

---

## 10. 攻击流程

```
┌─────────────────────────────────────────────────────────────────┐
│                    R²A 攻击流程                                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Step 1: 构建混合集成替代路由器                                   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  开源路由器池（5个）  ──┐                                │   │
│  │                         ├──→ 线性映射W₀ ──┐             │   │
│  │  可训练轻量路由器      ──┤  (对齐至目标池) │             │   │
│  │  (LoRA, all-MiniLM)   ──┘                │             │   │
│  │                                              ↓             │   │
│  │                                    加权集成 + softmax      │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                  │
│  Step 2: 替代路由器训练                                          │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  目标路由器 (黑盒)  ──[最多Q次查询]──→ 训练标签          │   │
│  │              ↑                        ↓                 │   │
│  │         交叉熵损失 ←──── 替代路由器预测                  │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                  │
│  Step 3: 对抗后缀优化                                           │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  初始后缀 s = [s₁, ..., sₗ]                              │   │
│  │       ↓                                                  │   │
│  │  对每个位置i: 计算聚合梯度 g̃ᵢ                          │   │
│  │       ↓                                                  │   │
│  │  Top-K候选集合 Cᵢ ← g̃ᵢ                                  │   │
│  │       ↓                                                  │   │
│  │  采样B个变体 s^(b)，选择loss最低的更新s                  │   │
│  │       ↓                                                  │   │
│  │  递增激活新查询（当前缀在前m_c个查询上成功）             │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                  │
│  Step 4: 最终攻击                                               │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  原始查询 q ──[附加优化后后缀 s*]──→ q ⊕ s*             │   │
│  │       → 路由器现在选择昂贵强模型 → 经济损失/服务降级     │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 11. 消融实验

### 11.1 核心组件消融

对R²A两个核心组件进行消融研究：

| 模型 | RouterDC | CausalLLM | MF | SW |
|------|---------|-----------|----|----|
| **R²A（完整）** | 0.83 | 0.83 | 0.95 | 0.81 |
| 无轻量级路由器 | **0.30** | 0.75 | 0.70 | 0.61 |
| 无梯度归一化 | 0.33 | 0.78 | **0.49** | 0.63 |

**关键发现**：

1. **无梯度归一化**：在RouterDC上从0.83降至0.33，在MF上从0.95降至0.49，证明梯度归一化对处理异构梯度规模的关键作用
2. **无轻量级路由器**：在RouterDC上从0.83降至0.30，表明参数高效适应（LoRA）在有限查询预算下的重要性

### 11.2 查询预算的影响

| 查询预算 | 替代准确率 | ASR (RouteLLM-Bert) |
|---------|-----------|-------------------|
| 50 | 低 | 0.52 |
| 80 | 中 | 0.58 |
| 100 | 高 | 0.72 |
| **120** | **高** | **0.87** |
| 150 | 饱和 | 0.89 |

**发现**：对于大多数目标路由器，性能在约120个查询时饱和，表明R²A具有极高的样本效率——仅需适度查询即可在不同路由器上获得强攻击效果。

---

## 12. 局限性

### 12.1 主要局限

1. **目标定向单一**：R²A主要研究将查询引导至更强/更昂贵模型，未系统研究其他目标（如针对特定模型、延迟或安全性）
2. **信息依赖**：攻击假设可访问路由器候选模型列表及每次查询所选模型的身份信息，某些部署场景中此假设不成立
3. **每个路由器独立优化**：需要为每个目标路由器训练单独的对抗后缀，无法跨路由器共享

### 12.2 潜在缓解方向

- 针对多目标攻击（延迟优化、成本最小化）的扩展研究
- 探索零样本迁移到未知路由器的方法
- 研究防御策略以保护成本感知路由系统

---

## 13. 伦理声明

本研究属于**对抗性安全研究**范畴，遵循负责任的披露原则：

1. **学术研究目的**：本文属于对LLM路由器安全性的学术研究，旨在揭示风险并促进防御
2. **低风险场景**：攻击需要攻击者能够修改用户查询，这本身已代表系统已被入侵
3. **促进防御**：研究结果为路由器系统的安全设计提供了重要参考，有助于构建更安全的成本感知路由系统
4. **防御建议**：论文建议对路由器进行更强监控，路由器设计应考虑对抗性操纵风险

---

## 14. 参考文献

### 核心引用

1. **Kaplan et al. (2020)** - Scaling Laws for Neural Language Models. arXiv:2001.08361
2. **Zou et al. (2023)** - Universal and Transferable Adversarial Attacks (GCG). arXiv:2307.15043, ICLR 2024
3. **Hu et al. (2022)** - LoRA: Low-Rank Adaptation of Large Language Models. ICLR 2022
4. **Liu et al. (2017)** - Delving into Transferable Adversarial Examples and Black-box Attacks. ICLR 2017
5. **Dong et al. (2018)** - Boosting Adversarial Attacks with Momentum. CVPR 2018
6. **Shafran et al. (2025)** - Routing attack (white-box approach). 2025
7. **Lin et al. (2025b)** - Life-cycle Routing Vulnerabilities of LLM Router. arXiv:2503.08704
8. **Hendrycks et al. (2021)** - Measuring Massive Multitask Language Understanding (MMLU). ICLR 2021
9. **Cobbe et al. (2021)** - Training Verifiers to Solve Math Word Problems (GSM8K). arXiv:2110.14168
10. **Wang et al. (2020)** - all-MiniLM-L6-v2 sentence transformer.

### LLM路由器相关

- Chen et al. (2024a) - FrugalGPT.TMLR 2024
- Jiang et al. (2023) - LLM-Blender. ACL 2023
- Ding et al. (2024) - Hybrid LLM. ICLR 2024
- Feng et al. (2024) - GraphRouter. ICLR 2024
- Chen et al. (2024b) - RouterDC. NeurIPS 2024
- Zhuang et al. (2025) - Compact Model Embeddings for routing
- Wang et al. (2025) - In-context-learning based routers

### 路由器攻击相关

- Kassem et al. (2025) - Router-LLM fragility analysis. arXiv:2504.07113
- Huang et al. (2025a) - Adversarial manipulation of Chatbot Arena. ICML 2025
- Kojima et al. (2022) - Chain-of-Thought prompting. NeurIPS 2022

---

## 📊 总结

| 维度 | 内容 |
|------|------|
| **论文主题** | 针对LLM成本感知路由器的黑盒对抗攻击 |
| **核心方法** | R²A：混合集成替代路由器 + 对抗后缀优化 |
| **创新点** | 首个在严格黑盒场景下实现路由攻击的系统性方法 |
| **实验规模** | 9个路由器 × 6个数据集（含2个商业系统） |
| **关键结果** | ASR最高提升+0.77，推理成本增加2.7-2.9倍 |
| **攻击成本** | 仅需$0.98的查询成本即可发起有效攻击 |
| **开源代码** | https://github.com/thcxiker/R2A-Attack |
| **安全启示** | 路由是安全关键边界，需要更强监控 |

---

*本笔记由 LLM Safety 论文阅读助手自动生成*
*生成时间: 2026-04-20 01:00 CST*
*阅读进度: 56/80 (70.00%)*
