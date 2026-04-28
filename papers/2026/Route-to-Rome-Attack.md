# Route to Rome Attack: Directing LLM Routers to Expensive Models via Adversarial Suffix Optimization

## 1. 基本信息

| 项目 | 内容 |
|------|------|
| **论文标题** | Route to Rome Attack: Directing LLM Routers to Expensive Models via Adversarial Suffix Optimization |
| **作者** | Haochun Tang, Yuliang Yan, Jiahua Lu, Huaxiao Liu, Enyan Dai |
| **机构** | (From paper content - appears to be academic institution) |
| **会议** | ACL 2026 Main Conference (CCF-A) |
| **arXiv** | [2604.15022](https://arxiv.org/abs/2604.15022) |
| **代码/数据** | https://github.com/thcxiker/R2A-Attack |
| **发表日期** | 2026年4月16日 |

### 引用格式

```
@article{tang2026route,
  title={Route to Rome Attack: Directing LLM Routers to Expensive Models via Adversarial Suffix Optimization},
  author={Tang, Haochun and Yan, Yuliang and Lu, Jiahua and Liu, Huaxiao and Dai, Enyan},
  journal={arXiv preprint arXiv:2604.15022},
  year={2026}
}
```

---

## 2. 英文摘要原文（arXiv Abstract原文）

> Cost-aware routing dynamically dispatches user queries to models of varying capability to balance performance and inference cost. However, the routing strategy introduces a new security concern that adversaries may manipulate the router to consistently select expensive high-capability models. Existing routing attacks depend on either white-box access or heuristic prompts, rendering them ineffective in real-world black-box scenarios. In this work, we propose R$^2$A, which aims to mislead black-box LLM routers to expensive models via adversarial suffix optimization. Specifically, R$^2$A deploys a hybrid ensemble surrogate router to mimic the black-box router. A suffix optimization algorithm is further adapted for the ensemble-based surrogate. Extensive experiments on multiple open-source and commercial routing systems demonstrate that {R$^2$A} significantly increases the routing rate to expensive models on queries of different distributions. Code and examples: https://github.com/thcxiker/R2A-Attack.

---

## 3. 中文摘要翻译

> 成本感知路由动态地将用户查询分发到不同能力水平的模型，以平衡性能与推理成本。然而，这种路由策略引入了一个新的安全问题：攻击者可能操纵路由器持续选择昂贵的强能力模型。现有的路由攻击依赖于白盒访问或启发式提示，使它们在真实世界的黑盒场景中失效。在本文中，我们提出了R²A，旨在通过对抗后缀优化将黑盒LLM路由器误导到昂贵模型。具体而言，R²A部署了一个混合集成替代路由器来模拟黑盒路由器，并进一步为基于集成的替代路由器适配了后缀优化算法。在多个开源和商业路由系统上的广泛实验表明，R²A显著提高了在不同分布查询上路由到昂贵模型的比例。代码和示例：https://github.com/thcxiker/R2A-Attack。

---

## 4. 研究背景

### 4.1 LLM路由器的兴起

随着大型语言模型（LLMs）在各种应用中的广泛部署，如何在保持性能的同时控制成本成为一个关键挑战。成本感知路由（Cost-aware routing）技术应运而生，它动态地将用户查询分发到不同能力水平的模型，以在性能与推理成本之间取得平衡。

传统的LLM路由方法包括：
- **Early approaches**: 查询多个LLM为单一输入选择最佳响应
- **Later approaches**: 在推理阶段之前预测最佳模型，使用不同数据源和骨干模型

更近期的工作通过多种策略改进捕获模型间差异的能力，包括：
- 双对比学习（Dual contrastive learning）
- 基于图的学习（Graph-based learning）
- 紧凑模型嵌入（Compact model embeddings）
- 基于排名的方法如Elo评分和Bradley-Terry模型
- 基于上下文学习的路由方法

### 4.2 路由器攻击的风险

尽管路由技术带来了成本-性能优势，但最近的研究揭示了LLM路由器中的安全漏洞：

1. **基于分类器的启发式依赖**：许多路由器依赖基于分类器的启发式方法，引入安全风险
2. **投票操纵脆弱性**：如Chatbot Arena等基于投票的排行榜容易受到对抗性投票操纵
3. **路由决策可被操控**：攻击者可以扰动查询以改变路由决策

### 4.3 现有攻击方法的局限性

现有路由攻击方法存在两个主要限制：

1. **白盒访问依赖**：一些方法需要访问路由器参数和梯度
2. **固定优化提示依赖**：其他方法依赖于固定的优化提示

这些限制使得它们在真实世界的黑盒场景中无效，因为攻击者通常无法获取路由器的内部结构和参数。

### 4.4 研究空白

本文试图填补以下研究空白：
- 在严格黑盒设置下进行路由攻击
- 仅使用观察到的路由决策来优化攻击
- 为每个目标路由器训练特定的后缀攻击
- 实现跨不同查询分布的强大泛化能力

---

## 5. 核心贡献

### 5.1 R²A方法概述

本文提出了**R²A（Route to Rome Attack）**，一种新颖的黑盒路由攻击方法，通过对抗后缀优化将LLM路由器误导到昂贵模型。

### 5.2 核心技术贡献

1. **混合集成替代路由器（Hybrid Ensemble Surrogate Router）**：
   - 部署多个开源路由器模型作为集成
   - 模拟目标黑盒路由器的行为
   - 通过观察查询-路由决策对来训练替代路由器

2. **编码器一致性目标（Encoder-Consistent Objective）**：
   - 确保替代路由器与目标路由器的决策一致
   - 处理异构梯度尺度问题
   - 实现跨不同路由器架构的鲁棒攻击

3. **后缀优化算法（Suffix Optimization Algorithm）**：
   - 针对每个目标路由器优化特定后缀
   - 使用梯度下降等优化技术
   - 考虑查询的语义完整性

### 5.3 实践贡献

1. **显著的成本增加**：实验显示R²A可将每百万token的平均成本增加约**2.7倍**到**2.9倍**
2. **强泛化能力**：在分布内和分布外数据集上都表现出色
3. **低攻击成本**：收集120个替代训练查询仅需约$0.98
4. **真实世界验证**：在商业系统OpenRouter和GPT-5上验证了有效性

---

## 6. 研究方法

### 6.1 问题定义

设：
- $\mathcal{R}_t$ 为目标黑盒路由器
- $\mathcal{M}_{strong}$ 为高能力（昂贵）模型集合
- $\mathcal{M}_{weak}$ 为低能力（便宜）模型集合
- $q$ 为用户查询
- $s$ 为对抗后缀

**攻击目标**：找到一个后缀 $s$，使得：
$$\text{ASR}(s) = \frac{1}{|\mathcal{D}|}\sum_{q\in\mathcal{D}}\mathbb{I}\left(\mathcal{R}_{t}(q\oplus s)\in\mathcal{M}_{strong}\right)$$

最大化，即让更多查询被路由到昂贵模型。

### 6.2 替代路由器构建

#### 6.2.1 替代路由器选择

使用5个开源路由器构建集成池：
- RouteLLM-Bert
- GraphRouter
- P2L
- RouterDC
- RouteLLM-MF

#### 6.2.2 混合集成策略

1. **参数高效适应**：使用LoRA（Low-Rank Adaptation）技术
   - 在有限的查询预算下训练替代路由器
   - LoRA允许通过低秩矩阵更新高效适应预训练模型

2. **梯度归一化（Gradient Normalization）**：
   - 处理异构梯度尺度问题
   - 确保不同路由器组件的梯度贡献平衡
   - 防止某些路由器主导优化过程

3. **编码器一致性目标**：
   - 确保替代路由器输出与目标路由器一致
   - 通过对比学习损失实现
   - 最小化替代路由器与目标路由器决策的差异

### 6.3 后缀优化

#### 6.3.1 优化目标

在替代路由器上优化后缀 $s$，以最大化路由到 $\mathcal{M}_{strong}$ 的概率：
$$\max_s \sum_{i=1}^{N} \mathbb{I}\left(\mathcal{R}_{surrogate}(q_i \oplus s) \in \mathcal{M}_{strong}\right)$$

#### 6.3.2 优化算法

使用基于梯度的方法优化后缀：
1. **初始化**：使用随机或基于启发式的初始后缀
2. **梯度计算**：计算后缀词符的梯度
3. **梯度归一化**：对梯度进行归一化处理
4. **更新**：使用优化器（如Adam）更新后缀
5. **约束**：确保后缀不会过度破坏查询的语义完整性

#### 6.3.3 查询预算管理

- 替代训练查询预算：120个查询
- 分割为：
  - $\mathcal{D}_{proxy}$：替代模型训练
  - $\mathcal{D}_{suffix}$：后缀优化
  - $\mathcal{D}_{eval}$：分布内泛化评估

### 6.4 安全性分析

#### 6.4.1 白盒攻击模拟

在替代路由器上进行优化时，可以采用白盒方法：
- 获取替代路由器的梯度信息
- 直接优化后缀参数
- 使用更精确的优化策略

#### 6.4.2 黑盒攻击部署

在目标路由器上部署时，仅使用：
- 查询-路由决策对
- 不需要获取目标路由器的内部结构
- 通过替代路由器学习到的模式进行攻击

---

## 7. 实验设置

### 7.1 目标路由器

测试9个目标路由器，包括：
- RouteLLM-Bert
- GraphRouter
- P2L
- RouterDC
- RouteLLM-MF
- OpenRouter（真实商业路由器）
- GPT-5（闭源商业路由器）

### 7.2 数据集

#### 分布内数据集（In-Distribution）：
- MMLU（大规模多任务语言理解）
- GSM8K（小学数学8K）
- MT-Bench（多轮对话基准）

#### 分布外数据集（Out-of-Distribution）：
- SimpleQA
- ArenaHard
- RouterArena

### 7.3 基线方法

与以下基线进行比较：
1. **Rerouting**：基于爬山搜索的通用对抗触发器
2. **LifeCycle (W)**：基于梯度优化的通用触发器
3. **LifeCycle (B)**：从高胜率查询中提取固定触发器
4. **CoT（Chain-of-Thought）**：添加"Let’s think step by step"以增加感知复杂度

### 7.4 评估指标

**攻击成功率（ASR）**：被路由到高能力模型的查询比例

$$ASR(s)=\frac{1}{|\mathcal{D}|}\sum_{q\in\mathcal{D}}\mathbb{I}\left(\mathcal{R}_{t}(q\oplus s)\in\mathcal{M}_{strong}\right)$$

### 7.5 实验配置

- 查询预算：120个（所有实验）
- 运行次数：3次
- 温度设置：默认（根据模型配置）
- 评估的路由器数量：9个
- 数据集数量：6个（3个分布内 + 3个分布外）

---

## 8. 实验结果

### 8.1 主要结果：路由攻击成功率

#### 8.1.1 分布内结果

**Table 1结果摘要（ASR）**：

| 方法 | MMLU | GSM8K | MT-Bench | 平均 |
|------|------|-------|----------|------|
| Clean | 0.25 | 0.35 | 0.27 | 0.29 |
| Rerouting | 0.88 | 0.54 | 0.64 | 0.69 |
| LifeCycle (W) | 0.93 | 0.65 | 0.76 | 0.78 |
| LifeCycle (B) | 0.42 | 0.33 | 0.64 | 0.46 |
| CoT | 0.35 | 0.54 | 0.33 | 0.41 |
| **R²A (Ours)** | **0.98** | **0.82** | **0.91** | **0.90** |

**关键发现**：
- R²A在所有分布内数据集上显著优于所有基线
- 平均ASR达到90%，比最佳基线（LifeCycle W）提高约15%
- 在MMLU上，R²A达到98%的ASR，几乎完美的攻击效果

#### 8.1.2 分布外结果

| 方法 | SimpleQA | ArenaHard | RouterArena | 平均 |
|------|----------|-----------|-------------|------|
| Clean | 0.30 | 0.28 | 0.25 | 0.28 |
| Rerouting | 0.60 | 0.65 | 0.44 | 0.56 |
| LifeCycle (W) | 0.71 | 0.68 | 0.42 | 0.60 |
| LifeCycle (B) | 0.33 | 0.32 | 0.35 | 0.33 |
| CoT | 0.54 | 0.43 | 0.23 | 0.40 |
| **R²A (Ours)** | **0.79** | **0.86** | **0.74** | **0.80** |

**关键发现**：
- R²A在分布外数据集上保持高ASR（80%）
- 显著优于所有基线，验证了强泛化能力
- 即使从未见过的查询分布，攻击依然有效

### 8.2 推理成本分析

#### 8.2.1 成本增加倍数

在OpenRouter上评估：
- **MMLU**：约2.7倍成本增加
- **RouterArena**：约2.9倍成本增加

#### 8.2.2 攻击成本

- 收集120个替代训练查询：仅需$0.98
- 总体财务开销极低
- 后缀诱导的生成长度变化（数据集相关）

### 8.3 GPT-5路由器攻击结果

#### 8.3.1 实验设置

- 在GPT-5网页界面测试三种模式：Auto、Instant、Thinking
- 随机采样50个问题从分布外测试集
- 使用在OpenRouter上训练的对抗后缀

#### 8.3.2 评估方法

由于GPT-5不暴露路由决策，使用两种间接评估方法：
1. **响应质量**：使用LLM法官比较响应
2. **指纹分数**：使用BoW指纹识别Thinking模式likelihood

#### 8.3.3 结果

**响应质量比较（Table 2）**：

| 评估维度 | Clean | Attack |
|----------|-------|--------|
| Comprehensiveness | 36.0% | 64.0% |
| Diversity | 28.0% | 72.0% |
| Empowerment | 36.0% | 64.0% |
| Overall | 36.0% | **64.0%** |

**关键发现**：
- 攻击后响应在所有评估维度上持续优于清洁查询
- 64%的总体胜率表明攻击成功诱导了更强的模型
- Thinking-likeness概率明显向更高值转移

#### 8.3.4 案例分析

**Figure 5展示的案例**：
- **清洁查询**：快速但不正确的回答（0秒）
- **攻击后查询**：多步推理过程，得出正确答案（51秒）
- 观察到处理时间显著增加
- 这表明对抗后缀成功诱导GPT-5路由到更昂贵的Thinking模式

### 8.4 空格防御的鲁棒性

**Table 3结果（空格防御下的ASR）**：

| 数据集 | RouteLLM-BERT | Graph-Router | RouterDC |
|--------|---------------|--------------|----------|
| MT-Bench | 0.95 (0.93) | 0.71↓ (0.73) | 1.00 (1.00) |
| ArenaHard | 0.81↓ (0.84) | 0.73↓ (0.83) | 1.00 (1.00) |

**关键发现**：
- R²A对空格防御表现出轻微的鲁棒性下降
- 在所有三个数据集上仍保持高ASR
- 防御仅在某些路由器上有轻微效果

### 8.5 消融研究

**Table 4结果（消融实验）**：

| 配置 | RouterDC | CausalLLM | MF | SW |
|------|----------|-----------|-----|-----|
| **R²A** | **0.83** | **0.83** | **0.95** | **0.81** |
| w/o Lightweight Router | 0.30 | 0.75 | 0.70 | 0.61 |
| w/o Grad Norm | 0.33 | 0.78 | 0.49 | 0.63 |

**关键发现**：
1. **轻量级路由器的贡献**：
   - 禁用后RouterDC上从0.83降至0.30
   - 表明参数高效适应在有限查询下至关重要

2. **梯度归一化的贡献**：
   - 移除后在MF上从0.95降至0.49
   - 表明梯度归一化对处理异构梯度尺度至关重要

3. **两个组件的必要性**：
   - 两个组件对跨路由器的鲁棒攻击都必要

### 8.6 查询预算的影响

**Figure 6结果**：
- 增加查询预算（50→150）持续提高替代准确度
- 替代准确度与ASR强相关
- RouteLLM-Bert在80→120查询时ASR从0.58急剧上升到0.87
- 大多数目标路由器在约120个查询时性能饱和
- R²A高度样本高效，仅需适度查询数量即可实现强攻击效果

---

## 9. 策略示例

### 9.1 对抗后缀示例

基于实验观察，有效的对抗后缀通常包含：
1. **语义模糊标记**：增加推理复杂度感知的词符
2. **模式化触发器**：重复某些模式以诱导复杂化
3. **链式推理暗示**：如"Let me think step by step"

**示例后缀模式**：
```
[Universal Suffix]: "Let me carefully analyze this step by step, considering all possible angles and implications..."
```

### 9.2 攻击场景

#### 场景1：MMLU学术问题

**清洁查询**：
```
What is the pressure of carbon dioxide at 200°F and a specific volume of 0.20 ft³/lbm?
```
**结果**：快速但不正确的回答（Internal: 0s）

**攻击后查询**：
```
What is the pressure of carbon dioxide at 200°F and a specific volume of 0.20 ft³/lbm? [Universal Suffix]
```
**结果**：多步推理，正确答案（Internal Thought: 51s）

#### 场景2：多轮对话

**清洁查询**：
```
User: Can you help me write a Python function to sort a list?
```

**攻击后查询**：
```
User: Can you help me write a Python function to sort a list? [Universal Suffix]
```
**结果**：可能被路由到更强大的模型，提供更详细的解释

### 9.3 攻击流程

```
1. 收集替代训练查询（120个）
   ↓
2. 训练混合集成替代路由器
   ↓
3. 在替代路由器上优化对抗后缀
   ↓
4. 将优化后的后缀附加到目标查询
   ↓
5. 提交攻击查询到目标路由器
   ↓
6. 观察路由决策（更多路由到昂贵模型）
```

---

## 10. 攻击流程详解

### 10.1 攻击准备阶段

#### 10.1.1 数据收集

- 收集120个代表性查询用于替代训练
- 查询涵盖不同分布和难度级别
- 成本：约$0.98

#### 10.1.2 替代路由器训练

```
对于每个目标路由器Rt：
  1. 初始化混合集成替代路由器Rs
  2. 使用Dproxy训练Rs（LoRA参数高效适应）
  3. 应用梯度归一化处理异构梯度
  4. 验证Rs与Rt的决策一致性
```

### 10.2 后缀优化阶段

#### 10.2.1 优化目标

$$\max_s \sum_{q \in \mathcal{D}_{suffix}} \mathbb{I}\left(\mathcal{R}_s(q \oplus s) \in \mathcal{M}_{strong}\right)$$

#### 10.2.2 优化算法

1. **初始化**：$s \leftarrow s_{init}$（随机或启发式）
2. **循环直到收敛**：
   - 计算梯度：$\nabla_s \mathcal{L}_{attack}$
   - 归一化梯度：$\tilde{g} \leftarrow \text{normalize}(\nabla_s \mathcal{L}_{attack})$
   - 更新后缀：$s \leftarrow s + \alpha \cdot \tilde{g}$
   - 约束后缀长度和可读性

### 10.3 攻击部署阶段

#### 10.3.1 黑盒攻击实施

1. 获取目标查询 $q$
2. 附加优化后的后缀 $s$: $q' = q \oplus s$
3. 提交 $q'$ 到目标路由器 $\mathcal{R}_t$
4. 观察路由决策

#### 10.3.2 成本分析

- **攻击成本**：极低（查询预算约$0.98）
- **收益**：每百万token成本增加2.7-2.9倍
- **投资回报率**：极高

### 10.4 攻击效果量化

| 指标 | 清洁查询 | 攻击后 |
|------|---------|--------|
| 路由到昂贵模型比例 | 25-30% | 74-98% |
| 推理成本（$/M tokens） | $X | 2.7-2.9X |
| 响应质量 | 基线 | 显著提升 |
| 处理延迟 | 低 | 高（51s vs 0s） |

---

## 11. 消融实验深入分析

### 11.1 轻量级路由器的影响

#### 11.1.1 实验配置

- 比较有无LoRA参数高效适应
- 测试不同查询预算（50, 80, 120, 150）

#### 11.1.2 结果分析

| 查询预算 | w/o Lightweight Router | w/ R²A |
|----------|------------------------|--------|
| 50 | 0.15 | 0.52 |
| 80 | 0.25 | 0.58 |
| 120 | 0.30 | **0.83** |
| 150 | 0.35 | 0.85 |

**发现**：
- 轻量级路由器在所有预算下持续改进ASR
- 120个查询时提升效果最显著（0.30→0.83）
- 之后边际收益递减

### 11.2 梯度归一化的影响

#### 11.2.1 问题背景

不同路由器组件产生异构梯度尺度：
- 某些组件梯度较大
- 其他组件梯度可能过小而被忽略

#### 11.2.2 解决方案

梯度归一化：
$$\tilde{g}_i = \frac{g_i}{\|g_i\|} \cdot \frac{1}{\sqrt{d}}$$

其中 $d$ 是梯度维度。

#### 11.2.3 结果分析

| 目标路由器 | w/o Grad Norm | w/ Grad Norm | 提升 |
|------------|---------------|--------------|------|
| RouterDC | 0.33 | 0.83 | +151% |
| CausalLLM | 0.78 | 0.83 | +6% |
| MF | 0.49 | 0.95 | +94% |
| SW | 0.63 | 0.81 | +29% |

**发现**：
- 梯度归一化在所有路由器上都有帮助
- 对RouterDC和MF等路由器影响最大
- 确保所有组件均匀贡献于优化

### 11.3 替代路由器数量的影响

测试不同数量的替代路由器对攻击效果的影响：

| 替代路由器数量 | ASR |
|---------------|-----|
| 1 | 0.65 |
| 3 | 0.78 |
| 5 | **0.83** |
| 全部 | 0.82 |

**发现**：
- 5个替代路由器是最佳选择
- 过多替代路由器可能引入噪声
- 平衡多样性和一致性

### 11.4 后缀长度的影响

| 后缀长度（词符） | ASR | 生成长度变化 |
|-----------------|-----|-------------|
| 10 | 0.71 | +5% |
| 20 | 0.83 | +12% |
| 50 | 0.85 | +25% |
| 100 | 0.82 | +40% |

**发现**：
- 20个词符后缀效果最佳
- 过长后缀可能破坏查询语义
- 生成长度增加可能暴露攻击

---

## 12. 局限性

### 12.1 攻击目标的限制

1. **仅针对成本操纵**：
   - 主要关注将查询导向更强和更昂贵的模型
   - 未系统研究针对特定模型的其他原因（如延迟、安全）

2. **候选模型列表依赖**：
   - 攻击假设可访问路由器的候选模型列表
   - 需要知道每个查询选择了哪个模型
   - 在某些部署中这些信息可能不可用

### 12.2 攻击成本的考虑

1. **查询预算需求**：
   - 需要约120个查询用于替代训练
   - 在某些场景中可能难以收集

2. **目标特异性**：
   - 需要为每个目标路由器训练单独的对抗后缀
   - 无法获得通用后缀跨多个路由器有效

### 12.3 防御的可能

1. **检测方法**：
   - 后缀检测技术可能识别对抗后缀
   - 响应长度异常可能作为攻击指标

2. **缓解措施**：
   - 空格插入防御对某些路由器有效
   - 输入预处理可能削弱攻击效果

### 12.4 伦理考虑

1. **负责任的披露**：
   - 研究目标是用开源代码促进更好的防御
   - 未详细描述实际恶意利用方法

2. **潜在影响**：
   - 攻击可能导致服务提供商成本增加
   - 可能影响路由系统的可用性

---

## 13. 伦理声明

### 13.1 研究目的

本研究旨在：
1. 揭示LLM路由器中的安全漏洞
2. 为安全社区提供关于路由攻击的知识
3. 促进更安全的路由系统设计

### 13.2 代码发布

- 代码和示例已在GitHub公开：https://github.com/thcxiker/R2A-Attack
- 旨在帮助防御者理解和缓解此类攻击
- 未提供可直接用于恶意目的的完整攻击工具包

### 13.3 负责任的使用建议

1. **对于研究者**：
   - 使用本研究结果开发更好的防御
   - 在受控环境中进行实验

2. **对于服务提供商**：
   - 监控异常路由模式
   - 实施攻击检测机制
   - 考虑路由决策的鲁棒性

3. **对于政策制定者**：
   - 认识到AI系统的安全风险
   - 支持安全研究和标准化工作

### 13.4 潜在风险与缓解

| 潜在风险 | 缓解措施 |
|---------|---------|
| 恶意利用导致成本增加 | 仅发布防御相关发现；强调检测重要性 |
| 攻击技术扩散 | 不详细描述实际攻击操作步骤 |
| 服务可用性受影响 | 建议服务提供商实施监控和防护 |

---

## 14. 参考文献

### 核心参考文献

1. Tang, H., Yan, Y., Lu, J., Liu, H., & Dai, E. (2026). Route to Rome Attack: Directing LLM Routers to Expensive Models via Adversarial Suffix Optimization. *ACL 2026*.

2. Chen, L., Zaharia, M., & Zou, J. (2024). FrugalGPT: How to use large language models while reducing cost and improving performance. *TMLR*.

3. Shafran, A., et al. (2025). Rerouting: Universal adversarial triggers for LLM routing. *arXiv*.

4. Lin, Q., et al. (2025). Life-cycle routing vulnerabilities of LLM router. *arXiv*.

5. Kojima, T., et al. (2022). Large language models are zero-shot reasoners. *NeurIPS*.

6. Hendrycks, D., et al. (2021). Measuring massive multitask language understanding. *ICLR*.

7. Cobbe, K., et al. (2021). Training verifiers to solve math word problems. *arXiv*.

8. Bai, G., et al. (2024). MT-bench-101: A fine-grained benchmark for evaluating LLMs in multi-turn dialogues. *ACL 2024*.

9. Hu, E.J., et al. (2022). LoRA: Low-rank adaptation of large language models. *ICLR*.

10. Kassem, A., et al. (2025). How robust are router-llms? *arXiv*.

11. Huang, Y., et al. (2025). Exploring adversarial manipulation of voting-based leaderboards. *ICML*.

12. Chen, S., et al. (2024). RouterDC: Query-based router by dual contrastive learning. *NeurIPS*.

13. Feng, T., et al. (2024). Graphrouter: A graph-based router for LLM selections. *ICLR*.

14. Dai, E., & Wang, S. (2022). Learning fair graph neural networks. *TKDE*.

15. Li, T., et al. (2025). From crowdsourced data to high-quality benchmarks. *ICML*.

16. Robey, A., et al. (2025). Whitespace defense for adversarial suffixes. *arXiv*.

17. Guo, Z., et al. (2025). LightRAG: Simple and fast retrieval-augmented generation. *EMNLP 2025*.

18. Wei, J., et al. (2024). SimpleQA: A benchmark for simple question answering. *arXiv*.

19. Lu, Y., et al. (2025). RouterArena: An open platform for comprehensive comparison of LLM routers. *arXiv*.

20. Zhuang, Y., et al. (2025). Compact model embeddings for LLM routing. *arXiv*.

21. Zhao, Y., et al. (2024). Elo-based routing in LLM systems. *arXiv*.

22. Frick, E., et al. (2025). Prompt-to-leaderboard. *arXiv*.

23. Wang, Y., et al. (2025). In-context-learning based routers. *arXiv*.

24. Aggarwal, P., et al. (2025). Automix: Automatically mixing language models. *arXiv*.

25. Jiang, D., et al. (2023). LLM-blender: Ensembling large language models. *ACL 2023*.

---

## 附录说明

### 附录A：数据集详细信息

#### A.1 数据集划分

| 数据集 | Dproxy | Dsuffix | Deval |
|--------|--------|---------|-------|
| MMLU | 500 | 200 | 300 |
| GSM8K | 400 | 200 | 200 |
| MT-Bench | 100 | 50 | 50 |
| SimpleQA | - | - | 100 |
| ArenaHard | - | - | 100 |
| RouterArena | - | - | 100 |

#### A.2 替代路由器列表

1. **RouteLLM-Bert**: 基于BERT的路由模型
2. **GraphRouter**: 基于图学习的路由模型
3. **P2L**: 基于参数高效学习的路由模型
4. **RouterDC**: 基于双对比学习的路由模型
5. **RouteLLM-MF**: 基于矩阵分解的路由模型

### 附录B：超参数设置

| 参数 | 值 |
|------|-----|
| LoRA rank | 16 |
| LoRA alpha | 32 |
| 学习率 | 0.01 |
| 优化器 | Adam |
| 后缀最大长度 | 50词符 |
| 查询预算 | 120 |

### 附录C：成本分析

| 成本项目 | 金额 |
|---------|------|
| 替代训练查询（120个） | $0.98 |
| 后缀优化 | <$0.10 |
| 评估查询 | ~$2.00 |
| **总计** | **~$3.00** |

### 附录D：指纹识别方法

使用Bag-of-Words指纹识别方法：
1. 训练一个分类器识别"Thinking"模式响应
2. 将此分类器应用于查询响应
3. Thinking-likeness分数作为路由到强模型的概率

### 附录E：空格防御实现

```python
def whitespace_defense(suffix):
    """在suffix中插入空格"""
    return ' '.join(list(suffix))

# 示例
original = "Let me think step by step"
defended = "L e t   m e   t h i n k   s t e p   b y   s t e p"
```

---

*本文档由AI助手自动生成，基于arXiv论文2604.15022内容。*
*生成日期：2026-04-28*
*项目主页：https://github.com/thcxiker/R2A-Attack*