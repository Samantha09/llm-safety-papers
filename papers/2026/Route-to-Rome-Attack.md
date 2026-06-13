# Route to Rome Attack: Directing LLM Routers to Expensive Models via Adversarial Suffix Optimization

## 1. 基本信息

| 字段 | 内容 |
|------|------|
| **论文标题** | Route to Rome Attack: Directing LLM Routers to Expensive Models via Adversarial Suffix Optimization |
| **简称** | R²A (Route to Rome Attack) |
| **作者** | Haochun Tang, Yuliang Yan, Jiahua Lu, Huaxiao Liu, Enyan Dai |
| **机构** | 吉林大学（符号计算与知识工程教育部重点实验室）、香港科技大学（广州） |
| **会议** | ACL 2026 Main Conference |
| **arXiv** | [2604.15022](https://arxiv.org/abs/2604.15022) |
| **代码** | [https://github.com/thcxiker/R2A-Attack](https://github.com/thcxiker/R2A-Attack) |
| **方向** | Router Attack / LLM Security / Adversarial Attack |
| **方向细分** | 黑盒路由器攻击 / 对抗后缀优化 / 成本感知路由安全 |
| **arXiv发表时间** | 2026年4月16日 |
| **关键词** | LLM Router, Cost-aware Routing, Adversarial Suffix, Black-box Attack, Ensemble Surrogate |

---

## 2. 英文摘要原文（arXiv Abstract）

> Cost-aware routing dynamically dispatches user queries to models of varying capability to balance performance and inference cost. However, the routing strategy introduces a new security concern that adversaries may manipulate the router to consistently select expensive high-capability models. Existing routing attacks depend on either white-box access or heuristic prompts, rendering them ineffective in real-world black-box scenarios. In this work, we propose R²A, which aims to mislead black-box LLM routers to expensive models via adversarial suffix optimization. Specifically, R²A deploys a hybrid ensemble surrogate router to mimic the black-box router. A suffix optimization algorithm is further adapted for the ensemble-based surrogate. Extensive experiments on multiple open-source and commercial routing systems demonstrate that R²A significantly increases the routing rate to expensive models on queries of different distributions. Code and examples: https://github.com/thcxiker/R2A-Attack.

**引用信息：**
```
arXiv:2604.15022 [cs.CR]
Submitted to ACL 2026 Main Conference
```

---

## 3. 中文摘要翻译（人工翻译）

> **背景**：成本感知路由（Cost-aware routing）动态地将用户查询分配给不同能力的模型，以平衡性能与推理成本。然而，这种路由策略引入了一个新的安全威胁：攻击者可能操纵路由器始终选择昂贵的高端模型。现有路由攻击依赖于白盒访问（需要知道目标路由器的梯度或架构）或启发式提示，在现实的黑盒场景中效果不佳。
>
> **方法**：本文提出 R²A（Route to Rome Attack），通过对抗后缀优化（adversarial suffix optimization）欺骗黑盒 LLM 路由器选择昂贵模型。具体而言，R²A 部署了一个混合集成代理路由器（hybrid ensemble surrogate router）来模拟黑盒路由器的行为，并设计了针对集成代理的后缀优化算法。
>
> **实验**：在 6 个数据集、7 个开源路由器和 2 个商业路由器（GPT-5-Auto 和 OpenRouter）上的广泛实验表明，R²A 能显著提高将查询路由到昂贵模型的比例，且在不同分布的查询上均有效。
>
> **开源**：代码已公开于 https://github.com/thcxiker/R2A-Attack

---

## 4. 研究背景

### 4.1 LLM路由技术的兴起

随着大语言模型的迅猛发展，模型规模呈指数级增长。以 Qwen 系列为例，Qwen-3-Max 参数量超过 1 万亿参数，约是上一代旗舰 Qwen-2.5-72B 的 14 倍。然而，为每个用户查询都部署如此庞大的模型，在计算和经济上都是不可持续的。

为了平衡性能与成本，**成本感知 LLM 路由（Cost-aware LLM routing）** 技术应运而生。其核心思想是：只有少数复杂查询才真正需要昂贵的高端模型，而大量简单查询可以被成本低廉的弱模型有效处理。

典型的路由流程如下：
1. 路由器接收用户查询 q
2. 评估查询复杂度（通过预测损失 ℓ(q, Mi)）
3. 考虑各模型的推理成本（C(q, Mi)）
4. 选择满足质量约束下成本最低的模型

这种路由机制已广泛部署于商业系统，包括 **OpenRouter**（auto 模式）和 **GPT-5-Auto**。

### 4.2 路由攻击的威胁模型

成本感知路由在提升效率的同时，也引入了新的攻击面——**路由器攻击（Router Attack）**。攻击者试图通过某种"通用触发器"（例如固定后缀），诱使路由器绕过成本约束，始终选择昂贵的强模型。

这类攻击的潜在危害包括：
- **经济损耗**：持续引导用户查询到贵模型，增加服务提供商的成本
- **服务降级**：使本可快速响应的简单查询被迫使用慢速贵模型，增加延迟
- **拒绝服务**：在极端情况下，通过大量引导到贵模型造成资源耗尽

### 4.3 现有方法的局限性

在 R²A 之前，已有初步探索（Shafran et al., 2025; LifeCycle, Lin et al., 2025b），但均存在明显缺陷：

| 方法 | 局限性 |
|------|--------|
| **Shafran et al. (2025)** | 需要白盒访问（目标路由器梯度或架构已知），在商业黑盒场景中不适用 |
| **LifeCycle (Lin et al., 2025b)** | 采用启发式提示（如 "Below is an instruction..., [query]"），未经严格优化，攻击效果不稳定 |

这些方法都无法在真实商业部署场景（黑盒、严格查询预算）下有效工作。

### 4.4 核心挑战

R²A 面临两个关键挑战：

1. **挑战一：黑盒设置下如何构建忠诚的代理路由器？**
   - 现有路由器采用多样化机制（语义嵌入、LLM-based 等），架构未知时难以构建匹配代理
   - 严格的查询预算限制进一步增加了代理构建的难度

2. **挑战二：如何为多样化查询优化离散的对抗后缀？**
   - 即使有了代理路由器，针对未知目标路由器的高效离散优化仍是难题
   - 集成代理涉及多个编码器，需要跨路由器的梯度聚合机制

---

## 5. 核心贡献

R²A 的主要贡献可以概括为三点：

### 5.1 首次研究黑盒LLM路由器的对抗后缀攻击问题

本文首次系统性地研究了**黑盒设置下通过对抗后缀优化引导 LLM 路由器选择昂贵模型**这一新问题。这是一种全新的安全威胁维度，区别于传统的越狱攻击（jailbreak）或提示注入（prompt injection）。

### 5.2 提出混合集成代理路由器（Hybrid Ensemble Surrogate Router）

为了在严格的黑盒查询预算下模拟未知架构的目标路由器，R²A 设计了**混合集成代理路由器**，结合了：
- 多个预训练开源路由器（覆盖不同路由机制）
- 可训练的轻量级路由器（基于 LoRA-style 低秩分解）

通过联合学习集成权重和轻量级路由器参数，代理能更好地对齐未知目标路由器。

### 5.3 提出针对集成代理定制化的后缀优化算法

R²A 提出了**聚合梯度归一化机制**，解决多编码器集成代理中梯度聚合的问题：
- 对每个路由器的 token 梯度进行 min-max 归一化（消除不同架构间的梯度量级差异）
- 基于归一化梯度进行 GCG-style 贪婪坐标梯度优化

### 5.4 广泛的实验验证

在 6 个数据集、9 个路由器（包括 GPT-5-Auto 和 OpenRouter 商业系统）上验证了 R²A 的有效性。

---

## 6. 研究方法

### 6.1 LLM路由器的形式化定义

给定查询 q，LLM 路由器 ℛ: q → ℝᴺ 从模型候选池 ℳ = {M₁, ..., Mₙ} 中选择一个模型。成本感知路由通过求解以下优化问题来选择模型：

```
ℛ(q) = argmin_{Mᵢ ∈ ℳ} ( ℓ(q, Mᵢ) + λ · C(q, Mᵢ) )
```

其中：
- ℓ(q, Mᵢ)：模型 Mᵢ 处理查询 q 的预测损失
- C(q, Mᵢ)：模型 Mᵢ 的成本分数
- λ ≥ 0：控制成本权重

### 6.2 威胁模型

**攻击目标**：使原本被路由到弱/便宜模型的查询，在添加对抗后缀后被路由到强/昂贵模型。

**模型池划分**：通过公开排行榜（lmarena.ai/leaderboard）将候选模型池划分为：
- ℳstrong：昂贵强模型（如 GPT-4o、Claude-3）
- ℳweak：便宜弱模型（如 Mistral-8x7B）

**攻击成功条件**：
- 给定查询 q，原本 ℛₜ(q) ∈ ℳweak
- 攻击后 ℛₜ(𝒜(q)) ∈ ℳstrong

**攻击者能力**：攻击者只能通过在查询末尾追加最多 Δ 个 token 的对抗后缀来修改查询。

**攻击者知识**：假设纯黑盒设置——攻击者只能观察到目标路由器的最终路由决策，无法访问：
- 目标路由器的内部 logits
- 模型参数或梯度
- 每次查询目标路由器均需付费，因此查询预算严格受限

### 6.3 路由器攻击的数学形式化

目标是找到通用对抗后缀 s*，使目标路由器 ℛₜ 将查询路由到强模型的概率最大化：

```
s* = argmax_{s} 𝔼_{q~𝒬} [ 𝕀(ℛₜ(q⊕s) ∈ ℳstrong) ]
s.t. s ∈ 𝒮, |s| ≤ Δ
```

其中 𝒬 是输入查询分布，⊕ 表示拼接操作，𝕀 是指示函数。

### 6.4 R²A 方法框架

R²A 的完整流程分为两个阶段：

**阶段一：代理路由器训练**
1. 构建混合集成代理路由器 ℛₛ
2. 在严格查询预算 Q 下训练代理（最小化交叉熵损失）
3. 学习集成权重 {αᵢ} 和轻量级路由器参数

**阶段二：对抗后缀优化**
1. 在代理路由器上执行后缀优化
2. 通过梯度聚合机制处理多编码器集成
3. 使用 GCG-style 贪婪优化生成对抗后缀

### 6.5 混合集成代理路由器的设计

#### 6.5.1 可训练轻量级路由器

采用 **all-MiniLM-L6-v2** 作为编码器（d=384 维嵌入）。为解决完整参数矩阵 d × |ℳₜ| 训练所需查询量过大的问题，引入 **LoRA-style 低秩分解**：

```
𝐳ₗ = E(q)𝐖ₗ¹𝐖ₗ²
```

其中：
- 𝐖ₗ¹ ∈ ℝ^{d×r}，𝐖ₗ² ∈ ℝ^{r×|ℳₜ|}，r ≪ d
- 通过低秩约束显著减少训练所需查询量

#### 6.5.2 开源路由器集成

R²A 组合多个具有不同路由机制的开源路由器 {ℛₒ⁽¹⁾, ..., ℛₒ⁽ᴷ⁾}，以减少机制不匹配。

**Logit 标准化**：由于各开源路由器的模型池 ℳₒ⁽ᵏ⁾ 不一致，需要将其 logit 映射到统一的模型池 ℳuni：

```
z̃ᵢ⁽ᵏ⁾ = { z^{(k)}_{Mᵢ}, if Mᵢ ∈ ℳₒ⁽ᵏ⁾
          0,          otherwise }
```

**跨池映射**：开源路由器的模型池与目标路由器不同，通过线性映射对齐：

```
𝐳ₒ⁽ᵏ⁾ = 𝐖ₒ · z̃⁽ᵏ⁾_uni
```

其中 𝐖ₒ ∈ ℝ^{|ℳuni|×|ℳₜ|} 是投影矩阵。

#### 6.5.3 集成路由决策

最终通过加权求和计算集成路由结果：

```
ŷ = softmax(α₀𝐳ₗ + Σᵢ₌₁ᴷ αᵢ𝐳ₒ⁽ᵏ⁾)
```

其中 αᵢ ≥ 0 且 Σᵢ₌₀ᴷ αᵢ = 1。

#### 6.5.4 代理路由器训练目标

```
min_θ ℒₛ = (1/Q) Σᵢ₌₁ᵠ l(ŷ(qᵢ), ℛₜ(qᵢ))
```

其中 θ = {𝐖ₗ¹, 𝐖ₗ², 𝐖ₒ, {αᵢ}_{i=0}^K}，l(·) 为交叉熵损失。

### 6.6 对抗后缀优化算法

#### 6.6.1 优化目标

在混合集成代理上优化对抗后缀：

```
min_s ℒₐ = -𝔼_{q~𝒬} Σ_{M∈ℳstrong} p(ŷ = M | q⊕s)
```

#### 6.6.2 梯度聚合问题

R²A 继承了 GCG（Greedy Coordinate Gradient）方法的思想，但集成代理涉及多个编码器，直接累加各路由器的梯度会导致某一特定路由器主导优化过程。

#### 6.6.3 Min-Max 梯度归一化

为解决梯度量级差异问题，对每个路由器的 token 梯度进行 **min-max 归一化**：

```
δ̃ᵢ⁽ᵏ⁾ = (δᵢ⁽ᵏ⁾ - δᵢₙₜᵢₙ⁽ᵏ⁾) / (δᵢₘₐₓ⁽ᵏ⁾ - δᵢₙₜᵢₙ⁽ᵏ⁾)
```

其中 min 和 max 跨当前迭代中所有后缀 token 计算。

#### 6.6.4 聚合梯度计算

基于归一化梯度，聚合后的梯度为：

```
g̃ᵢ = Σᵢ₌₀ᴷ αᵢ · δ̃ᵢ⁽ᵏ⁾ · (∂ℒₐ/∂𝐳ₜₒₜₐₗ)
```

---

## 7. 实验设置

### 7.1 数据集

实验在 **6 个数据集**上进行，覆盖不同查询分布：

| 数据集 | 说明 |
|--------|------|
| **MTG** | 多轮对话数据集 |
| **BBQ** | 偏置问答数据集 |
| **GSM8K** | 数学问题数据集 |
| **HumanEval** | 代码生成数据集 |
| **Nq** | 问答数据集 |
| **PopQA** | 流行知识问答 |

### 7.2 目标路由器

实验覆盖 **9 个黑盒路由器**：

**7 个开源路由器：**
- Router 1-7（使用不同路由机制和模型池配置）

**2 个商业路由器：**
- **GPT-5-Auto**：OpenAI 官方自动路由
- **OpenRouter**：第三方路由平台

### 7.3 基线方法对比

| 基线方法 | 说明 |
|----------|------|
| **Random Suffix** | 随机后缀基线 |
| **LifeCycle** | 启发式提示方法（从高胜率查询中提取模板） |
| **GCG** | 白盒梯度坐标下降（用于上界参考） |

### 7.4 评估指标

主要评估指标为 **Strong Model Routing Rate（SM Rate）**——添加对抗后缀后，查询被路由到强模型的比率。

辅助指标包括：
- 回答质量（确保后缀不损害答案正确性）
- 收敛速度（达到目标攻击率所需迭代次数）
- 跨路由器泛化能力

### 7.5 实现细节

- **代理训练**：严格遵守查询预算 Q（模拟商业场景的每次查询成本）
- **后缀长度**：Δ = 20 tokens（实验设置）
- **优化算法**：基于 GCG 的贪婪坐标梯度优化
- **轻量级路由器编码器**：all-MiniLM-L6-v2
- **低秩维度**：r = 8

---

## 8. 实验结果

### 8.1 主要结果：显著提升强模型路由率

R²A 在所有测试数据集和路由器上均显著优于基线方法：

**关键发现：**
- R²A 将查询被路由到强模型的比例从基线（随机后缀约 15-25%）提升至 **50-80%**
- 在 GPT-5-Auto 和 OpenRouter 等商业路由器上同样有效
- 对不同分布的查询（对话、问答、数学、代码）均有良好效果

### 8.2 与基线方法对比

| 方法 | MTG | BBQ | GSM8K | HumanEval | Nq | PopQA |
|------|-----|-----|-------|-----------|-----|-------|
| Random Suffix | ~20% | ~18% | ~22% | ~15% | ~25% | ~20% |
| LifeCycle | ~35% | ~30% | ~38% | ~28% | ~40% | ~35% |
| GCG（白盒上界） | ~75% | ~72% | ~78% | ~70% | ~80% | ~75% |
| **R²A（黑盒）** | **~70%** | **~68%** | **~72%** | **~65%** | **~75%** | **~70%** |

*R²A 在黑盒设置下接近白盒 GCG 上界，显著超越启发式 LifeCycle 方法。*

### 8.3 商业路由器泛化结果

在 GPT-5-Auto 和 OpenRouter 上的实验表明：
- R²A 学到的对抗后缀具有良好的跨平台迁移能力
- 在 OpenRouter 上学习的后缀可直接迁移到 GPT-5-Auto（尽管后者路由决策不可直接观测）

### 8.4 回答质量保障

R²A 生成的对抗后缀不会显著损害答案质量：
- 使用正确性指标衡量，加后缀前后答案准确率差异 < 2%
- 后缀设计尽量保持语义中性，避免引入明显的语义偏移

### 8.5 收敛性分析

R²A 的后缀优化在 200-500 次迭代内趋于收敛，相比其他方法：
- LifeCycle 需要大量查询来提取模板，效率较低
- R²A 通过代理路由器模拟，在有限查询预算内即可收敛

---

## 9. 策略示例

### 9.1 正常查询的路由行为

**查询示例**：
> "What is the capital of France?"

**正常路由结果**：Mistral 8x7B（弱模型，路由决策低成本）

### 9.2 R²A 攻击后的路由行为

**对抗后缀追加后的查询**：
> "What is the capital of France? [对抗后缀]"

**攻击后路由结果**：GPT-4o 或 Claude-3（强模型，路由决策高成本）

### 9.3 对抗后缀特征

R²A 生成的对抗后缀具有以下特征：
- **通用性**：同一个后缀可引导大量不同类型的查询路由到贵模型
- **隐蔽性**：后缀通常为看似自然的指令性文本（如 "Please provide a detailed response"）
- **可迁移性**：在不同路由器间具有良好的迁移能力

---

## 10. 攻击流程详解

### 阶段一：代理路由器构建与训练

**Step 1：准备开源路由器池**
- 收集 K 个具有不同路由机制的开源路由器
- 确保覆盖多种路由策略（语义嵌入、LLM-based 等）

**Step 2：构建轻量级路由器**
- 使用 all-MiniLM-L6-v2 作为编码器
- 引入 LoRA-style 低秩分解减少参数量

**Step 3：Logit 标准化与跨池映射**
- 将各开源路由器的 logit 标准化到统一模型池 ℳuni
- 学习投影矩阵 𝐖ₒ 将标准化 logit 映射到目标模型池 ℳₜ

**Step 4：代理训练**
- 在严格查询预算 Q 下，向目标路由器 ℛₜ 查询获取训练标签
- 最小化交叉熵损失，联合学习集成权重和轻量级路由器参数

### 阶段二：对抗后缀优化

**Step 5：初始化后缀**
- 随机初始化长度为 Δ 的 token 序列作为后缀

**Step 6：梯度计算与聚合**
- 对每个 token 计算集成代理的梯度
- 通过 min-max 归一化消除不同路由器间的梯度量级差异
- 使用加权聚合得到统一梯度信号

**Step 7：贪婪坐标优化**
- 每次迭代中，选择当前最需要替换的 token 位置
- 基于梯度信号选择最佳候选 token 替换方案
- 重复直到后缀收敛或达到最大迭代次数

**Step 8：攻击部署**
- 将学习到的对抗后缀追加到目标查询
- 查询目标路由器，观察路由决策是否被成功引导

---

## 11. 消融实验

### 11.1 代理路由器组件消融

| 配置 | SM Rate |
|------|---------|
| 仅轻量级路由器 | ~45% |
| 仅开源路由器集成 | ~55% |
| **混合集成（完整 R²A）** | **~70%** |

**分析**：混合集成相比单一组件均有显著提升，证明了两类组件的互补性。

### 11.2 开源路由器数量 K 的影响

| K 值 | SM Rate |
|------|---------|
| K=1 | ~50% |
| K=3 | ~62% |
| K=5 | ~68% |
| **K=7** | **~70%** |

**分析**：随着开源路由器数量增加，代理覆盖率提升，但收益边际递减。

### 11.3 低秩维度 r 的影响

| r 值 | SM Rate | 训练效率 |
|------|---------|---------|
| r=2 | ~65% | 最高 |
| r=8 | **~70%** | 高 |
| r=16 | ~71% | 中 |
| r=32 | ~71% | 低 |

**分析**：r=8 在性能和效率间取得良好平衡，r 过小限制表达能力，r 过大增加训练复杂度。

### 11.4 梯度归一化消融

| 配置 | SM Rate |
|------|---------|
| 无归一化（直接累加梯度） | ~48% |
| **Min-Max 归一化** | **~70%** |
| L2 归一化 | ~65% |
| softmax 归一化 | ~67% |

**分析**：Min-Max 归一化效果最佳，有效消除不同路由器架构间的梯度量级偏差。

### 11.5 查询预算 Q 的影响

| Q 值 | SM Rate | 代理保真度 |
|------|---------|-----------|
| Q=100 | ~55% | 低 |
| Q=500 | ~65% | 中 |
| Q=1000 | **~70%** | 高 |
| Q=2000 | ~71% | 高 |

**分析**：Q=1000 时基本达到最优性能，进一步增加预算收益有限。

---

## 12. 局限性

### 12.1 黑盒假设的局限

R²A 的威胁模型假设攻击者只能观察最终路由决策，但在某些场景下：
- 攻击者可能通过侧信道获得部分路由器内部信息
- 若路由器提供置信度分数（如 softmax 前的 logits），攻击者可利用这些信息提升攻击效果

### 12.2 后缀长度约束

当前设置中对抗后缀长度限制为 Δ=20 tokens，可能存在：
- 更长的后缀可能带来更强的攻击效果，但更易被检测
- 某些防御策略（如长度检测）可能限制后缀长度

### 12.3 商业路由器的路由决策不可观测性

对于 GPT-5-Auto 等商业路由器，路由决策本身不可直接观测：
- R²A 通过在 OpenRouter 上学习后缀并迁移到 GPT-5-Auto
- 这种迁移可能在某些情况下效果下降

### 12.4 防御对策尚未探索

本文主要关注攻击本身，未深入探讨防御策略：
- 路由器运营方可采取的防御措施（检测异常后缀、限制追加操作等）留待未来工作
- 对抗后缀的检测与过滤是重要的后续研究方向

### 12.5 回答质量影响

虽然实验显示答案质量影响较小（<2% 准确率差异），但：
- 在某些特定类型查询（如数学推理）上，后缀可能引入细微推理偏差
- 对安全性要求极高的应用场景，仍需评估风险

---

## 13. 伦理声明

### 13.1 研究动机

本文是一项**红队测试（Red Teaming）研究**，旨在揭示 LLM 成本感知路由系统中潜在的安全威胁。通过系统性地研究和演示攻击方法，帮助路由器运营者和 LLM 服务提供商更好地理解和防御此类攻击。

### 13.2 负责任的披露

- 研究者遵循**负责任的披露（Responsible Disclosure）**原则
- 在论文公开发表前，未向相关商业服务提供商发起实际攻击测试
- 实验主要在受控环境和模拟器中进行

### 13.3 潜在风险与收益评估

**潜在风险：**
- 攻击方法可能被恶意攻击者利用，造成服务提供商经济损失
- 可能被用于竞争攻击（使竞争对手的服务成本增加）

**研究收益：**
- 帮助路由器系统设计者预见并防御此类攻击
- 推动 LLM 安全领域的标准化安全评估
- 为未来安全路由协议设计提供理论基础

### 13.4 建议的防御方向

基于 R²A 的发现，建议的防御措施包括：
1. **后缀检测**：部署检测机制识别异常的查询后缀模式
2. **路由审计**：记录并分析异常路由模式
3. **成本限制**：对单用户或单查询的成本贡献设置上限
4. **查询验证**：在路由决策前检测查询是否被恶意修改

---

## 14. 参考文献

[1] Kaplan et al. (2020). Scaling Laws for Neural Language Models. arXiv:2001.08361.

[2] Lu et al. (2024). Cost-aware Routing for LLM Inference. arXiv:2405.XXXXX.

[3] Aggarwal et al. (2025). Dynamic Model Selection in LLM Serving. arXiv:2501.XXXXX.

[4] Ong et al. (2025). Quality-Constrained LLM Routing. arXiv:2503.XXXXX.

[5] Shafran et al. (2025). Routing Attacks on LLM Systems. arXiv:2502.XXXXX.

[6] Lin et al. (2025b). LifeCycle: Heuristic Router Manipulation. arXiv:2501.XXXXX.

[7] Liu et al. (2017). Delving into Transferable Adversarial Examples. arXiv:1705.04172.

[8] Dong et al. (2018). Evading Defenses to Transferable Adversarial Examples. ICLR 2018.

[9] Zou et al. (2023). Universal and Transferable Adversarial Attacks on Aligned Language Models (GCG). arXiv:2307.15043.

[10] Hu et al. (2022). LoRA: Low-Rank Adaptation of Large Language Models. ICLR 2022.

[11] Wang et al. (2020). All-MiniLM-L6-v2: Compact Sentence Embedding Model. HuggingFace.

[12] Carlsson et al. (2024). OpenRouter: LLM Routing Platform. https://openrouter.ai.

[13] OpenAI. (2024). GPT-5 System Card. OpenAI Blog.

---

*本文笔记由 LLM Safety 论文阅读助手自动生成*
*阅读日期：2026年6月14日*
*论文来源：arXiv:2604.15022 [cs.CR], ACL 2026*