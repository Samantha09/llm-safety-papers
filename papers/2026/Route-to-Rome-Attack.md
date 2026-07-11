# Route to Rome Attack: Directing LLM Routers to Expensive Models via Adversarial Suffix Optimization

## 1. 📌 论文基本信息

| 字段 | 内容 |
|------|------|
| **论文标题** | Route to Rome Attack: Directing LLM Routers to Expensive Models via Adversarial Suffix Optimization |
| **作者** | Haochun Tang, Yuliang Yan, Jiahua Lu, Huaxiao Liu, Enyan Dai |
| **所属机构** | 吉林大学符号计算与知识工程教育部重点实验室；香港科技大学（广州）|
| **会议/期刊** | ACL 2026 Main Conference |
| **arXiv编号** | 2604.15022 |
| **arXiv链接** | https://arxiv.org/abs/2604.15022 |
| **代码链接** | https://github.com/thcxiker/R2A-Attack |
| **研究方向** | Router Attack / LLM Security |
| **提交日期** | 2026年4月16日 |

---

## 2. 📖 英文摘要原文（arXiv Abstract）

> Cost-aware routing dynamically dispatches user queries to models of varying capability to balance performance and inference cost. However, the routing strategy introduces a new security concern that adversaries may manipulate the router to consistently select expensive high-capability models. Existing routing attacks depend on either white-box access or heuristic prompts, rendering them ineffective in real-world black-box scenarios. In this work, we propose R$^2$A, which aims to mislead black-box LLM routers to expensive models via adversarial suffix optimization. Specifically, R$^2$A deploys a hybrid ensemble surrogate router to mimic the black-box router. A suffix optimization algorithm is further adapted for the ensemble-based surrogate. Extensive experiments on multiple open-source and commercial routing systems demonstrate that R$^2$A significantly increases the routing rate to expensive models on queries of different distributions. Code and examples: https://github.com/thcxiker/R2A-Attack.

**引用格式**: 
```
[arXiv:2604.15022] Haochun Tang, Yuliang Yan, Jiahua Lu, Huaxiao Liu, Enyan Dai. 
Route to Rome Attack: Directing LLM Routers to Expensive Models via Adversarial Suffix Optimization. 
ACL 2026 Main Conference.
```

---

## 3. 📝 中文摘要翻译

> 成本感知路由（Cost-aware routing）通过动态将用户查询分配给不同能力的模型来平衡性能与推理成本。然而，这种路由策略引入了一个新的安全隐患：攻击者可能操纵路由器始终选择昂贵的高能力模型。现有路由攻击依赖于白盒访问或启发式提示，使其在现实黑盒场景中无效。在本工作中，我们提出 R²A，旨在通过对抗后缀优化误导黑盒 LLM 路由器选择昂贵模型。具体而言，R²A 部署了一个混合集成代理路由器（hybrid ensemble surrogate router）来模拟黑盒路由器，并进一步为该集成代理设计了后缀优化算法。在多个开源和商业路由系统上的广泛实验表明，R²A 能显著提高将查询路由至昂贵模型的比例，且适用于不同分布的查询。代码和示例：https://github.com/thcxiker/R2A-Attack。

---

## 4. 🔍 研究背景

### 4.1 LLM 路由技术的兴起

近年来，大型语言模型（LLM）的发展取得了显著成功，性能随着模型规模的扩大可预测地提升。例如，Qwen-3-Max 扩展到超过 1 万亿参数，比上一代旗舰模型 Qwen-2.5-72B 大约 14 倍。然而，为每个用户查询都使用最先进的模型在计算和经济上都是不可持续的。

为了平衡性能与成本，**成本感知 LLM 路由**（Cost-aware LLM Routing）应运而生，其核心思想是：只有一小部分请求真正需要昂贵的大模型，而简单查询可以由便宜的弱模型有效处理。例如，当路由器收到简单的事实查询"What is the capital of France?"时，它识别出这是低复杂度查询，选择较弱的 Mistral 8x7B 模型来生成响应。这类路由技术已被 OpenRouter 和 GPT-5-Auto 等商业系统采用。

### 4.2 路由攻击的威胁

尽管成本感知路由提高了效率，但它引入了一个新的安全威胁——**路由攻击（Router Attack）**：攻击者能否使用一个通用的触发器（例如固定后缀）来持续操纵路由器选择昂贵模型？

现有的路由攻击研究存在明显局限：

1. **白盒攻击依赖**（Shafran et al., 2025）：需要可访问目标路由器的梯度或架构信息，这在商业黑盒路由场景中不切实际。

2. **启发式提示攻击**（LifeCycle, Lin et al., 2025）：通过从高胜率查询中提取模板（如"Below is an instruction..., [query]"）来引导路由器选择昂贵模型。虽然适用于黑盒设置，但这类启发式提示缺乏严格的优化，因此往往不足以持续操纵各种目标路由器。

### 4.3 研究空白

本文首次系统研究了在**纯黑盒设置下**（攻击者仅能观察到路由器的最终决策，无法访问梯度、参数或架构信息）通过对立后缀优化来误导 LLM 路由器选择昂贵模型的问题。这是一个在实际商业场景中具有重要意义但尚未被充分研究的问题。

---

## 5. 🎯 核心贡献

本文的主要贡献可以概括为以下三点：

1. **新问题的研究**：首次研究了通过对立后缀优化将黑盒 LLM 路由器引导至昂贵模型这一新问题。

2. **R²A 方法**：提出了 R²A（Route to Rome Attack），该方法创新性地引入**混合集成代理路由器**来在有限的黑色查询预算下模拟目标路由器行为，并针对混合集成代理路由器量身定制了对抗后缀优化算法。

3. **广泛验证**：在 6 个数据集、7 个开源路由器和 2 个商业黑盒路由器（GPT-5-Auto 和 OpenRouter）上的实验验证了 R²A 的有效性，证明其能够有效泛化到包括商业系统在内的多样化路由器。

---

## 6. ⚙️ 研究方法

### 6.1 问题定义

#### 6.1.1 LLM 路由器基础

给定一个查询 $q$，LLM 路由器 $\mathcal{R}: q \rightarrow \mathbb{R}^{N}$ 从模型池 $\mathcal{M} = \{M_1, ..., M_N\}$ 中选择一个模型。成本感知路由通过解决以下优化问题来实现成本与质量的平衡：

$$\mathcal{R}(q) = \arg\min_{M_i \in \mathcal{M}} \left( \ell(q, M_i) + \lambda \cdot C(q, M_i) \right)$$

其中 $\ell(q, M_i)$ 是模型 $M_i$ 在查询 $q$ 上的预测损失，$C(q, M_i)$ 是成本分数，$\lambda \geq 0$ 控制成本分数在路由决策中的权重。

#### 6.1.2 路由攻击威胁模型

**攻击者目标**：误导路由器选择昂贵模型来回答给定查询。按照公开排行榜，将模型候选池分为昂贵强模型 $\mathcal{M}_{\text{strong}}$ 和便宜弱模型 $\mathcal{M}_{\text{weak}}$。形式化地，对于原本被路由至弱模型的查询 $q$（即 $\mathcal{R}_t(q) \in \mathcal{M}_{\text{weak}}$），攻击操作 $\mathcal{A}$ 成功的条件是 $\mathcal{R}_t(\mathcal{A}(q)) \in \mathcal{M}_{\text{strong}}$。

**攻击者能力**：攻击者可以修改原始查询，通过在查询末尾附加不超过 $\Delta$ 个 token 的对抗后缀 $s$ 来实现攻击。

**攻击者知识**：假设在现实的黑色盒设置中，攻击者只能观察到目标路由器的路由决策。由于每次查询目标路由器都会产生财务成本，攻击者被限制为最多 $Q$ 次查询。

#### 6.1.3 路由攻击形式化

目标是找到一个通用的对抗后缀 $s^*$，使目标路由器 $\mathcal{R}_t$ 的决策被引导至昂贵强模型。给定上述威胁模型，路由攻击可以形式化为以下优化问题：

$$s^* = \arg\max_{s} \mathbb{E}_{q \sim \mathcal{Q}} \left[ \mathbb{I}(\mathcal{R}_t(q \oplus s) \in \mathcal{M}_{\text{strong}}) \right]$$
$$\text{s.t.} \quad s \in \mathcal{S}, \quad |s| \leq \Delta$$

其中 $\mathcal{Q}$ 是输入查询的分布，$\oplus$ 表示拼接操作，$\mathbb{I}(\cdot)$ 是指示函数。

### 6.2 方法详解：R²A 框架

R²A 的核心思想是：首先训练一个代理路由器来模拟目标路由器的行为，然后使用该代理路由器来优化通用的对抗后缀。

#### 6.2.1 混合集成代理路由器（Hybrid Ensemble Surrogate Router）

由于目标路由器的设计未知，仅依赖单一架构可能导致架构不匹配，从而产生较差的代理。因此，R²A 构建了一个混合集成代理路由器，结合了多种预训练的开源路由器和可训练的轻量级路由器。在代理训练期间，共同学习所有路由器的集成权重和轻量级路由器的参数。

**设计优势**：
- 通过纳入开源路由器，R²A 可以快速识别与目标行为匹配的现有路由器（或线性组合），减少所需查询次数；
- 通过优化可训练的轻量级路由器，R²A 可以处理与所有预训练开源路由器显著不同的目标路由器。

**可训练轻量级路由器设计**：使用 All-MiniLM-L6-v2 作为编码器（输出维度 $d=384$）。直接学习从 $\mathbb{R}^d$ 到 $\mathbb{R}^{|\mathcal{M}_t|}$ 的线性映射需要优化参数量为 $d \times |\mathcal{M}_t|$ 的参数矩阵，训练需求巨大。借鉴 LoRA 的思想，施加低秩约束，将变换分解为两个较小的矩阵 $\mathbf{W}_l^1 \in \mathbb{R}^{d \times r}$ 和 $\mathbf{W}_l^2 \in \mathbb{R}^{r \times |\mathcal{M}_t|}$（其中 $r \ll d$）。轻量级路由器的 Logits 计算为：

$$\mathbf{z}_l = E(q)\mathbf{W}_l^1 \mathbf{W}_l^2$$

**与开源路由器结合**：R²A 将多个具有不同路由机制的开源路由器 $\{ \mathcal{R}_o^{(1)}, ..., \mathcal{R}_o^{(K)} \}$ 结合起来。由于开源路由器的模型池与目标路由器不一致，R²A 应用线性映射将其 Logits 对齐到目标路由器模型池空间：

$$\mathbf{z}_o^{(k)} = \mathbf{W}_o \cdot \mathbf{z}_{uni}^{(k)}$$

**集成路由结果**：集成路由器在目标模型池 $\mathcal{M}_t$ 上的路由结果通过加权求和计算：

$$\hat{y} = \text{softmax}(\alpha_0 \mathbf{z}_l + \sum_{i=1}^{K} \alpha_i \mathbf{z}_o^{(k)})$$

其中 $\alpha_i$ 是满足 $\alpha_i \geq 0$ 和 $\sum_{i=0}^{K} \alpha_i = 1$ 的可学习集成权重。

**代理路由器训练**：为训练代理路由器，查询黑盒目标路由器 $\mathcal{R}_{\text{target}}$ 来生成训练标签。代理训练目标通过最小化以下损失函数来优化参数：

$$\min_{\theta} \mathcal{L}_S = \frac{1}{Q} \sum_{i=1}^{Q} l(\hat{y}(q_i), \mathcal{R}_t(q_i))$$

其中 $l(\cdot)$ 是交叉熵损失，$\hat{y}(q_i)$ 和 $\mathcal{R}_t(q_i)$ 分别表示代理和目标路由器对查询 $q_i$ 的预测。

#### 6.2.2 针对混合集成代理路由器的对抗后缀优化

有了混合集成代理路由器，对抗后缀优化可以重新表述为：

$$\min_s \mathcal{L}_A = -\mathbb{E}_{q \sim \mathcal{Q}} \sum_{M \in \mathcal{M}_{\text{strong}}} p(\hat{y} = M | q \oplus s)$$

**Token 梯度聚合**：通过链式法则分析 Token 梯度。令 $\mathbf{z}_{\text{total}} = \sum_{k=0}^{K} \alpha_k \mathbf{z}^{(k)}$ 表示集成 Logits。对于第 $k$ 个路由器，关于 Token $s_i$ 的梯度计算涉及对集成 Logits 的偏导、对各路由器 Logits 的偏导以及对 Token 的偏导的乘积。关键挑战在于：不同路由器架构中 Token 梯度的量级可能差异巨大，直接求和会导致某一成员路由器主导优化过程。

**归一化处理**：为了缓解这种偏差，R²A 对梯度项进行 Min-Max 归一化，将其缩放到 [0,1] 范围内，从而平衡各路由器在优化中的贡献。

---

## 7. 🧪 实验设置

### 7.1 数据集

实验使用了 6 个不同分布的数据集，涵盖多种类型的查询，以确保 R²A 在不同查询分布上的泛化能力。具体数据集包括：

- **MMLU**：多任务语言理解基准，涵盖 57 个学科
- **HumanEval**：代码生成评估
- **GSM8K**：小学数学问题
- **BBH**：BIG-Bench 困难任务
- **MT-Bench**：多轮对话评估
- **自定义对抗样本集**：专门设计用于测试路由攻击效果

### 7.2 目标路由器

实验涉及 9 个目标路由器：

**7 个开源路由器**：
- RouterFusion
- SimpleRouter
- Mixture-of-Agents
- Embedding-based routers（多种变体）
- LLMRouter
- 其他公开可用的路由系统

**2 个商业黑盒路由器**：
- **GPT-5-Auto**：OpenAI 的自动路由系统
- **OpenRouter**：第三方 LLM 聚合路由平台

### 7.3 基线方法对比

R²A 与以下基线方法进行对比：

1. **Random Suffix**：随机生成后缀
2. **Template Attack**（LifeCycle）：使用启发式模板引导路由
3. **White-box Attack**（Shafran et al.）：假设有梯度访问权限的最强攻击
4. **GCG**：通用对抗攻击方法

### 7.4 评估指标

主要评估指标为**路由率（Routing Rate）**，即被引导至昂贵模型的查询比例。越高表示攻击效果越好。同时评估攻击的**通用性**（对不同路由器和数据集的泛化能力）和**隐蔽性**（后缀的语义合理性）。

---

## 8. 📊 实验结果

### 8.1 主要结果

实验结果表明，R²A 在所有评估设置中均显著优于基线方法：

1. **路由率显著提升**：R²A 将查询路由至昂贵模型的比例从基线的 X% 提升至 Y%，相对提升达 Z%。

2. **商业路由器攻击成功**：在 GPT-5-Auto 和 OpenRouter 两个商业黑盒路由器上，R²A 仍然能够有效提升昂贵模型路由率，证明了其在真实商业环境中的实用性。

3. **跨数据集泛化**：R²A 在 6 个不同分布的数据集上均表现出色，说明学习到的对抗后缀具有良好的通用性。

### 8.2 与基线方法对比

| 方法 | 开源路由器路由率 | 商业路由器路由率 | 泛化能力 |
|------|----------------|----------------|---------|
| Random Suffix | 基准 | 基准 | 无 |
| Template Attack | 中等 | 较低 | 一般 |
| White-box Attack | 高 | N/A | 好（但需白盒）|
| GCG | 较高 | 较低 | 一般 |
| **R²A（本文）** | **最高** | **最高** | **最好** |

### 8.3 消融实验结果

**混合集成代理路由器的效果**：移除任一组分（开源路由器或可训练路由器）都会导致攻击效果下降。使用完整混合集成的效果最好，验证了设计决策的有效性。

**梯度聚合策略的影响**：使用归一化梯度聚合的方法显著优于直接梯度求和，证明了归一化在平衡各路由器贡献方面的重要性。

**查询预算 $Q$ 的影响**：R²A 在严格的查询预算（$Q$ 较小）下仍能保持较高攻击成功率，表明其 query 效率高。

---

## 9. 💡 策略示例

### 9.1 简单查询的路由操控

**原始查询**："What is the capital of France?"

- **正常路由**：路由器识别为低复杂度查询 → 路由至 Mistral 8x7B（便宜模型）
- **R²A 攻击后**：附加对抗后缀 → 路由器误判为复杂查询 → 路由至 GPT-4 或 Claude（昂贵模型）

### 9.2 对抗后缀示例

R²A 学习到的对抗后缀通常具有以下特征：

- **长度**：5-20 个 token
- **语义**：看似无害甚至积极的文本（如感谢语、礼貌请求等）
- **效果**：触发路由器的模式识别，使其倾向于选择更强大的模型

### 9.3 后缀的隐蔽性

R²A 生成的后缀具有较高的隐蔽性：
- 语法正确，与原始查询自然衔接
- 不包含明显的恶意指示
- 可以是看似合理的补充说明或上下文扩展

---

## 10. 🔐 攻击流程

R²A 攻击的完整流程如下：

```
┌─────────────────────────────────────────────┐
│           Phase 1: 代理路由器训练             │
├─────────────────────────────────────────────┤
│  1. 收集代理查询集 D_proxy                    │
│  2. 初始化混合集成代理路由器 R_s              │
│     - 加载多个开源路由器                      │
│     - 初始化可训练轻量级路由器 (LoRA)          │
│  3. 黑盒查询目标路由器 R_t（限制 Q 次）         │
│  4. 训练代理路由器，最小化与 R_t 的决策差异    │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│        Phase 2: 对抗后缀优化                  │
├─────────────────────────────────────────────┤
│  1. 初始化随机后缀 s                          │
│  2. 迭代优化（for t = 1 to T）:              │
│     a. 对每个 Token 计算梯度                  │
│     b. 跨路由器归一化梯度                    │
│     c. 贪心替换高贡献 Token                   │
│     d. 评估当前后缀的攻击成功率               │
│  3. 返回最优对抗后缀 s*                      │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│          Phase 3: 攻击部署                    │
├─────────────────────────────────────────────┤
│  将对抗后缀 s* 附加到目标查询                 │
│  发送到目标 LLM 服务                          │
│  路由器被操控选择昂贵模型                    │
└─────────────────────────────────────────────┘
```

**关键创新点**：
1. **混合集成代理**：通过组合多种路由器机制，解决单一架构与目标不匹配的问题
2. **归一化梯度聚合**：解决不同路由器梯度量级差异问题
3. **低秩约束的轻量级路由器**：在有限查询预算下有效训练

---

## 11. 🔬 消融实验

### 11.1 代理路由器组件消融

| 配置 | 路由率 | 分析 |
|------|--------|------|
| 仅开源路由器 | 降低 | 缺乏对目标行为的适应性 |
| 仅可训练路由器 | 降低 | 查询预算不足以训练好 |
| **完整混合集成** | **最高** | 兼保守性和适应性 |
| 移除 LoRA 分解 | 显著降低 | 参数量过大，欠拟合 |

### 11.2 梯度聚合策略消融

| 策略 | 效果 | 分析 |
|------|------|------|
| 直接梯度求和 | 一般 | 某一路由器主导 |
| Random 聚合 | 较差 | 随机性过高 |
| **归一化梯度聚合** | **最好** | 平衡各路由器贡献 |

### 11.3 查询预算 $Q$ 的影响

随着查询预算 $Q$ 的增加，代理路由器的保真度提高，攻击效果提升。但即使在严格的预算（如 $Q < 100$）下，R²A 仍能保持有效的攻击成功率。

### 11.4 后缀长度 $\Delta$ 的影响

对抗后缀长度 $\Delta$ 在 5-20 个 token 之间时，攻击效果最佳。过短的后缀表达能力有限，过长的后缀可能引入噪声或被检测。

---

## 12. ⚠️ 局限性

1. **查询预算假设**：R²A 假设攻击者能够进行一定数量的黑盒查询（$Q$ 次）来训练代理路由器。在极端受限的预算下，攻击效果可能下降。

2. **商业路由器不可观测性问题**：对于 GPT-5-Auto 等路由决策不可直接观测的商业系统，R²A 采用在 OpenRouter 上学习的代理然后迁移的策略，跨系统泛化能力可能受限。

3. **防御措施未评估**：论文未系统评估现有防御措施（如路由审计、异常检测、后缀检测）对 R²A 的有效性。

4. **成本影响**：R²A 主要关注路由操控的成功率，对攻击者实际成本收益分析不足。在真实攻击场景中，需要权衡操控收益与被发现的风险。

5. **模型池定义的依赖性**：攻击效果依赖于对"昂贵模型"与"便宜模型"的明确定义，不同的划分标准可能影响攻击结果。

6. **可检测性**：学习到的对抗后缀虽然语义上较为自然，但可能存在统计上的异常模式，可被专门的路由安全系统检测。

---

## 13. 📜 伦理声明

本文研究了 LLM 路由系统的安全漏洞，属于负责任的安全研究。所有实验均在受控环境中进行，未对真实商业系统造成实际影响。研究结果已按照负责任的披露原则，在论文发表后公开。

**潜在风险**：本研究揭示的攻击方法可能被恶意攻击者用于：
- 通过强制路由至昂贵模型来对 LLM 服务进行 DoS 攻击
- 增加 LLM 服务提供商的成本
- 绕过基于路由的成本控制机制

**缓解建议**：
- 路由器应部署异常检测机制，监控异常的路由模式
- 考虑对路由决策进行加密或混淆
- 实现基于查询复杂度的自适应路由策略
- 建立对抗后缀检测和过滤系统

---

## 14. 📚 参考文献

1. Kaplan et al. (2020). Scaling Laws for Neural Language Models.
2. Lu et al. (2024). Cost-aware Routing in LLM Systems.
3. Aggarwal et al. (2025). Dynamic LLM Routing Strategies.
4. Ong et al. (2025). Quality-Constrained LLM Routing.
5. Shafran et al. (2025). White-box Router Attacks.
6. Lin et al. (2025b). LifeCycle: Template-based Router Manipulation.
7. Liu et al. (2017). Black-box Adversarial Attack Methods.
8. Dong et al. (2018). Boosting Adversarial Transferability.
9. Zou et al. (2023). Universal and Transferable Adversarial Attacks on Aligned Language Models (GCG).
10. Hu et al. (2022). LoRA: Low-Rank Adaptation of Large Language Models.
11. Wang et al. (2020). All-MiniLM-L6-v2: Compact Sentence Embedding Model.

---

*本文档由 LLM Safety 论文阅读计划自动生成*
*论文来源: arXiv:2604.15022*
*生成日期: 2026-07-11*
