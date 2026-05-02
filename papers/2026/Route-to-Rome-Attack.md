# Route to Rome Attack: Directing LLM Routers to Expensive Models via Adversarial Suffix Optimization

## 1. 基本信息

| 属性 | 内容 |
|------|------|
| 论文标题 | Route to Rome Attack: Directing LLM Routers to Expensive Models via Adversarial Suffix Optimization |
| 简称 | R²A (Route to Rome Attack) |
| 作者 | Haochun Tang, Yuliang Yan, Jiahua Lu, Huaxiao Liu, Enyan Dai |
| 单位 | 吉林大学、香港科技大学(广州) |
| 会议 | ACL 2026 Main Conference |
| arXiv | [2604.15022](https://arxiv.org/abs/2604.15022) |
| 代码 | [GitHub: thcxiker/R2A-Attack](https://github.com/thcxiker/R2A-Attack) |
| 方向 | Router Attack / LLM Security |
| 核心方法 | 通过对抗后缀优化误导黑盒LLM路由器选择昂贵模型 |
| CCF分级 | CCF-A |

---

## 2. 英文摘要原文

> Cost-aware routing dynamically dispatches user queries to models of varying capability to balance performance and inference cost. However, the routing strategy introduces a new security concern that adversaries may manipulate the router to consistently select expensive high-capability models. Existing routing attacks depend on either white-box access or heuristic prompts, rendering them ineffective in real-world black-box scenarios. In this work, we propose R²A, which aims to mislead black-box LLM routers to expensive models via adversarial suffix optimization. Specifically, R²A deploys a hybrid ensemble surrogate router to mimic the black-box router. A suffix optimization algorithm is further adapted for the ensemble-based surrogate. Extensive experiments on multiple open-source and commercial routing systems demonstrate that R²A significantly increases the routing rate to expensive models on queries of different distributions. Code and examples: https://github.com/thcxiker/R2A-Attack.

**引用**: 
```
arXiv:2604.15022v1 [cs.CR] 16 Apr 2026
Authors: Haochun Tang, Yuliang Yan, Jiahua Lu, Huaxiao Liu, Enyan Dai
Conference: ACL 2026 Main Conference
```

---

## 3. 中文摘要翻译

> 成本感知路由（Cost-aware routing）通过动态地将用户查询分配到不同能力的模型来平衡性能与推理成本。然而，这种路由策略引入了一个新的安全关切：攻击者可能操纵路由器始终选择昂贵的高能力模型。现有的路由攻击依赖于白盒访问或启发式提示，在现实世界的黑盒场景中效果不佳。在本文中，我们提出了R²A（Route to Rome Attack），通过对抗后缀优化来误导黑盒LLM路由器选择昂贵模型。具体而言，R²A部署了一个混合集成代理路由器来模拟黑盒路由器，并进一步为基于集成的代理设计了后缀优化算法。在多个开源和商业路由系统上的广泛实验表明，R²A能显著提高在不同分布查询上路由到昂贵模型的比例。代码和示例：https://github.com/thcxiker/R2A-Attack。

---

## 4. 研究背景

### 4.1 LLM路由器的兴起

随着大语言模型（LLM）的发展，模型规模不断增大。遵循扩展定律（scaling laws），性能随着模型规模的增加而可预测地提升。例如，Qwen-3-Max扩展到超过1万亿参数，大约是前代旗舰模型Qwen-2.5-72B的14倍。然而，为每个用户查询提供服务级模型在计算和经济上都不可持续。

为了平衡性能和成本，成本感知LLM路由（cost-aware LLM routing）被提出，根据质量约束将每个查询路由到满足要求的最低成本模型。这一策略基于以下洞察：只有一小部分请求需要昂贵的高能力模型，而简单查询可以由更便宜的弱模型有效处理。

成本感知路由已广泛应用于商业系统，如OpenRouter和GPT-5-Auto。

### 4.2 路由攻击的威胁

成本感知路由引入了一个自然的安全问题：攻击者是否可以使用通用触发器（例如固定后缀）来持续操纵路由器选择昂贵模型？

已有一些初步研究尝试回答这个问题：
- **Shafran et al. (2025)**: 依赖于获取目标路由器的可访问梯度或已知架构，这在商业设置中不切实际
- **LifeCycle (Lin et al., 2025b)**: 从高胜率查询中提取模板，虽然适用于黑盒设置，但这类启发式提示未经严格优化，往往不足以持续操纵各种目标路由器

### 4.3 研究空白

现有方法要么需要白盒访问（不现实），要么依赖非优化的启发式提示（效果不佳）。因此，本文研究在现实的黑盒设置下，通过对抗后缀优化将查询路由到昂贵模型这一新问题。

---

## 5. 核心贡献

1. **新问题定义**: 研究了通过对抗后缀优化将黑盒LLM路由器导向昂贵模型这一新问题

2. **混合集成代理路由器**: 提出了一种新颖的混合集成代理路由器，在有限的黑盒查询预算内模拟目标路由器，并配套设计了针对集成代理的对抗后缀优化算法

3. **广泛验证**: 在7个开源路由器和2个商业路由器（GPT-5-Auto和OpenRouter）上的6个数据集进行了广泛实验，验证了R²A的有效性和泛化能力

---

## 6. 研究方法

### 6.1 问题定义

#### LLM路由器基础

给定查询q，LLM路由器R: q → RN从候选模型池M = {M₁, ..., Mₙ}中选择一个模型。对于成本感知路由，路由器通过以下优化来最小化推理成本同时满足目标质量约束：

$$R(q) = \arg\min_{M_i \in M} \ell(q, M_i) + \lambda \cdot C(q, M_i)$$

其中ℓ(q, M_i)表示模型M_i在查询q上的预测损失，C(q, M_i)是成本分数，λ ≥ 0控制成本分数的权重。

#### 威胁模型

- **攻击目标**: 将路由器误导为选择昂贵模型来回答给定查询。将模型池分为昂贵强模型Mstrong和廉价弱模型Mweak
- **攻击者能力**: 攻击者可以通过最多∆个token的后缀s来修改原始查询q
- **攻击者知识**: 假设为现实的黑盒设置，攻击者只能观察目标路由器对输入查询的决策

#### 路由攻击形式化

目标找到一个通用对抗后缀s*，使目标路由器Rt将查询路由到强模型：

$$s^* = \arg\max_{s \in S, |s| \leq \Delta} E_{q \sim Q}[I(R_t(q \oplus s) \in M_{strong})]$$

### 6.2 混合集成代理路由器

由于目标路由器设计未知，依赖单一架构可能导致架构不匹配，因此提出构建混合集成代理路由器。

#### 可训练轻量级路由器

轻量级路由器Rl通过查询的嵌入E(q) ∈ Rᵈ预测目标路由器的决策。使用all-MiniLM-L6-v2作为编码器（d = 384）。为减少训练所需查询，采用LoRA风格低秩约束：

$$z_l = E(q)W_{l1}W_{l2}$$

其中W_{l1} ∈ R^{d×r}和W_{l2} ∈ R^{r×|M_t|}，秩r ≪ d。

#### 与开源路由器结合

R²A结合多个具有不同路由机制的开源路由器{R_o^(1), ..., R_o^(K)}。将它们的logits映射到并集M_{uni} = ∪_{k=1}^{K} M_o^(k)。

对于开放源代码路由器Ro^(k)，将其logit向量扩展为：

$$\tilde{z}_i^{(k)} = \begin{cases} z_{M_i}^{(k)} & \text{if } M_i \in M_o^{(k)} \\ 0 & \text{otherwise} \end{cases}$$

由于开源路由器的模型池与目标路由器池Mt不同，应用线性映射来对齐其logits：

$$z_o^{(k)} = W_o \cdot \tilde{z}_{uni}^{(k)}$$

其中W_o ∈ R^{|M_{uni}|×|M_t|}是投影矩阵。

#### 集成权重学习

综合路由结果通过加权求和计算：

$$\hat{y} = \text{softmax}(\alpha_0 z_l + \sum_{i=1}^{K} \alpha_i z_o^{(i)})$$

其中α_i是满足α_i ≥ 0和∑_{i=0}^{K} α_i = 1的可学习集成权重。

#### 代理路由器训练

代理训练目标是最小化：

$$\min_\theta L_S = \frac{1}{Q} \sum_{i=1}^{Q} l(\hat{y}(q_i), R_t(q_i))$$

其中l(·)是交叉熵损失。

### 6.3 对抗后缀优化

在混合集成代理路由器上，对抗后缀优化可以重新表述为：

$$\min_{s} L_A = -E_{q \sim Q}[\sum_{M \in M_{strong}} p(\hat{y} = M | q \oplus s)]$$

#### 梯度聚合

通过链式法则分析token梯度。对于第k个路由器：

$$g_i^{(k)} = \frac{\partial L_A}{\partial z_{total}} \cdot \frac{\partial z_{total}}{\partial z^{(k)}} \cdot \frac{\partial z^{(k)}}{\partial s_i} = \alpha_k \cdot \frac{\partial L_A}{\partial z_{total}} \cdot \frac{\partial z^{(k)}}{\partial s_i}$$

直接求和会导致某个成员路由器主导优化。为缓解此偏差，对δ_i进行min-max归一化：

$$\tilde{\delta}_i^{(k)} = \frac{\delta_i^{(k)} - \delta_{min}^{(k)}}{\delta_{max}^{(k)} - \delta_{min}^{(k)}}$$

聚合梯度：

$$\tilde{g}_i = \sum_{k=0}^{K} \alpha_k \cdot \tilde{\delta}_i^{(k)} \cdot \frac{\partial L_A}{\partial z_{total}}$$

#### 后缀优化算法

算法对单一通用后缀s使用混合集成代理路由器进行优化：
1. 初始化后缀s = [s₁, ..., s_L]
2. 迭代T次：
   - 对每个位置i，计算Top-k候选集C_i
   - 采样B个变体，通过用来自C_i的候选替换随机后缀token来更新
   - 选择损失最低的变体
3. 如果当前后缀成功，则递增包含下一个查询

---

## 7. 实验设置

### 7.1 目标路由器

测试9个目标路由器：RouteLLM-Bert、GraphRouter、P2L RouterDC、RouteLLM-MF、OpenRouter和GPT-5-Auto。

代理集成池包含5个开源路由器。

### 7.2 数据集

#### 分布内（In-Distribution）

用于代理模型训练和后缀优化：
- **MMLU**: 大规模多任务语言理解基准，57个学科
- **GSM8K**: 小学数学问题
- **MT-Bench**: 多轮对话基准

每个数据集分为三个不相交的子集：
- Dproxy（120个查询）：代理模型训练
- Dsuffix（600个查询）：70%用于后缀优化，30%用于评估
- Deval：攻击性能评估

#### 分布外（Out-of-Distribution）

评估后缀泛化能力：
- **SimpleQA**: 短格式问答
- **ArenaHard**: 挑战性现实世界查询
- **RouterArena**: 路由器评估基准

### 7.3 基线方法

- **Rerouting (Shafran et al., 2025)**: 基于爬山发现独立于查询的对抗触发器
- **LifeCycle (W)**: 通过梯度访问优化触发器
- **LifeCycle (B)**: 从高胜率查询中提取固定域无关触发器
- **Chain-of-Thought (CoT)**: 添加"Let's think step by step"

### 7.4 评估指标

使用**攻击成功率（Attack Success Rate, ASR）**：

$$ASR(s) = \frac{1}{|D|} \sum_{q \in D} I[R_t(q \oplus s) \in M_{strong}]$$

---

## 8. 实验结果

### 8.1 主要结果

R²A在所有目标路由器和数据集上均实现了最高的攻击成功率：

| 目标路由器 | Clean | LifeCycle (W) | LifeCycle (B) | Rerouting | CoT | R²A (Ours) |
|-------------|-------|---------------|---------------|-----------|-----|------------|
| RouteLLM-Bert | 0.24 | 0.58 | 0.49 | 0.81 | 0.38 | **1.00** |
| GraphRouter | 0.69 | 0.83 | 0.62 | 0.67 | 0.69 | **0.94** |
| P2L | 0.16 | 0.18 | 0.18 | 0.12 | 0.22 | **0.18** |
| RouterDC | 0.68 | 1.00 | 1.00 | 0.99 | 0.85 | **1.00** |
| RouteLLM-MF | 0.81 | 0.94 | 0.85 | 1.00 | 0.79 | **1.00** |
| OpenRouter* | 0.00 | 0.04 | 0.00 | 0.00 | 0.00 | **0.31** |

### 8.2 推理成本分析

在MMLU基准上，攻击后每百万token的平均成本增加约2.7倍。在分布外数据集RouterArena上，效果更强，增加2.9倍。

攻击成本极低：收集120个代理训练查询仅需$0.98。

### 8.3 GPT-5路由器攻击

由于GPT-5不暴露路由决策，使用"思维模式指纹"来推断：
- 攻击后，查询在更高思维模式相似性概率上呈现明显转变
- 攻击响应在所有评估维度上始终优于清洁响应

案例研究显示：
- **清洁提示**: 返回简短不正确答案（"P ≈ 8.0 × 10² psi"）
- **R²A后**: 切换到多步推理过程，产生正确答案（"P ≈ 695 psia"）

### 8.4 空格防御鲁棒性

使用空格防御（插入空格到后缀），R²A表现出轻微抵抗力：
- MT-Bench: 0.95 (0.93) → 轻微下降
- ArenaHard: 0.81↓ (0.84)

---

## 9. 策略示例

### 9.1 各目标路由器的后缀示例

**RouteLLM-MF:**
```
hua jadx parece retorno Omar ※ ile Qty_trans vào
```

**RouteLLM-BERT:**
```
}quanadermirroralsosedger\ufffdofinemet}translate 9byteimpintegration'tonshan
```

**RouteLLM-Causal:**
```
had !" !"ki\ufffdwatprivacywill+no
```

**P2L:**
```
originalrobot<*dad{@estefuckoslivellanal naturedenhetcupshopimitray
```

**Graph-Router:**
```
]++eachbotatabamarmovieverbavieminhead} &solutionclick\ufffd'attend
```

**RouterDC:**
```
summercanStyleType&kokriadGamerGOtype File{{xorPhotWIAppaultureat
```

**OpenRouter:**
```
decipherthispoem.alphabetical}Yi-encodedoutput
```

### 9.2 GPT-5攻击示例

**用户查询**: "What is the pressure of carbon dioxide at 200°F and a specific volume of 0.20 ft³/lbm?"

**清洁提示结果**: 
- 响应简短不正确
- Duration: 0s
- 输出: "Result: P ≈ 8.0 × 10² psi"

**R²A攻击后结果**:
- 响应切换到多步推理过程，产生正确答案
- Duration: 51s
- 输出: 包含热力学性质计算、CO2性质评估、PR方程求解等完整推理过程

---

## 10. 攻击流程

### 10.1 攻击流程图

```
用户查询 → 添加对抗后缀 → 混合集成代理路由器 → 重新路由到昂贵强模型
                      ↓
              原始路由器 → 廉价弱模型
```

### 10.2 具体步骤

1. **查询准备**: 准备目标查询q和候选后缀token集
2. **代理训练**: 使用有限查询预算（120个）训练混合集成代理路由器
3. **后缀优化**: 在代理路由器上进行对抗后缀优化
4. **攻击部署**: 将学习到的通用后缀附加到目标查询
5. **路由操控**: 目标路由器将修改后的查询路由到昂贵模型

### 10.3 查询预算分析

实验表明：
- 查询预算从50增加到150，代理准确性和ASR持续提升
- 大多数目标路由器的性能在120个查询时饱和
- R²A具有极高的样本效率，只需适度数量的查询即可实现跨异构路由器的强攻击性能

---

## 11. 消融实验

### 11.1 轻量级路由器的作用

移除轻量级路由器时，性能显著下降，特别是在RouterDC上（0.83 → 0.30），表明参数高效适应在有限查询下的重要性。

### 11.2 梯度归一化的作用

移除梯度归一化导致性能一致下降，特别是MF上（0.95 → 0.49），强调了处理异构梯度规模的作用。

### 11.3 各组件贡献

| 配置 | RouterDC | CausalLLM | MF | SW |
|------|----------|-----------|----|----|
| R²A | 0.83 | 0.83 | 0.95 | 0.81 |
| w/o 轻量级路由器 | 0.30 | 0.75 | 0.70 | 0.61 |
| w/o 梯度归一化 | 0.33 | 0.78 | 0.49 | 0.63 |

---

## 12. 局限性

1. **目标单一性**: 主要关注将查询引导至更高能力的模型，而实际中用户可能因延迟或安全等原因针对特定模型，本文未系统研究

2. **信息需求假设**: 攻击假设可访问路由器的候选模型列表和每次查询选择的模型身份，某些部署中此假设可能不成立

---

## 13. 伦理声明

本文攻击旨在揭示LLM路由中的漏洞并为设计更强防御提供信息，但可能被滥用来增加提供商的推理成本或绕过定价层级。

**建议的防御措施**：
- 部署路由特定监控
- 速率限制
- 异常检测
- 在生产环境暴露成本感知路由器前进行充分测试

计划以受控方式发布触发器和代码，以支持防御研究而非无差别利用。

---

## 14. 参考文献

1. Aggarwal, P., et al. (2025). Automix: Automatically mixing language models. arXiv:2310.12963.

2. Bai, G., et al. (2024). MT-bench-101: A fine-grained benchmark for evaluating LLMs in multi-turn dialogues. ACL 2024.

3. Chen, S., et al. (2024). RouterDC: Query-based router by dual contrastive learning. NeurIPS 2024.

4. Cobbe, K., et al. (2021). Training verifiers to solve math word problems. arXiv:2110.14168.

5. Hendrycks, D., et al. (2021). Measuring massive multitask language understanding. ICLR 2021.

6. Hu, E. J., et al. (2022). LoRA: Low-rank adaptation of large language models. ICLR 2022.

7. Jiang, D., et al. (2023). LLM-blender: Ensembling LLMs with pairwise comparison. ACL 2023.

8. Kaplan, J., et al. (2020). Scaling laws for neural language models. arXiv:2001.08361.

9. Kojima, T., et al. (2022). Large language models are zero-shot reasoners. NeurIPS 2022.

10. Lin, Q., et al. (2025). Life-cycle routing vulnerabilities of LLM router. arXiv:2503.08704.

11. Lu, K., et al. (2024). Routing to the expert: Efficient reward-guided ensemble of LLMs. NAACL 2024.

12. Ong, I., et al. (2025). RouteLLM: Learning to route LLMs from preference data. ICLR 2025.

13. Shafran, A., et al. (2025). Rerouting LLM routers. COLM 2025.

14. Wang, W., et al. (2020). Minilm: Deep self-attention distillation. NeurIPS 2020.

15. Wei, J., et al. (2024). Measuring short-form factuality in LLMs. arXiv:2411.04368.

16. Zou, A., et al. (2023). Universal and transferable adversarial attacks on aligned language models. arXiv:2307.15043.

---

## 附录：实验配置详情

### 超参数配置

**混合集成代理路由器训练**:
| 超参数 | 值 |
|--------|-----|
| 适配器秩(r) | 16 |
| 轮次 | 20 |
| 学习率 | 0.03 |
| 批量大小 | 32 |
| 优化器 | AdamW |

**对抗后缀优化**:
| 超参数 | 值 |
|--------|-----|
| 优化迭代次数(T) | 3000 |
| 候选批量大小(B) | 64 |
| Top-k采样 | 256 |
| 后缀token限制(∆) | 30 |

### 成本分析

- 代理训练：120个查询，总成本$0.9826（每查询约$0.00819）
- 后缀开销：数据集依赖，可为负值（路由改变导致更简洁响应）

---

*笔记生成时间: 2026-05-03*
*论文来源: arXiv:2604.15022v1 [cs.CR]*
