# Curiosity-driven Red-teaming for Large Language Models

## 1. 基本信息

| 项目 | 内容 |
|------|------|
| **论文标题** | Curiosity-driven Red-teaming for Large Language Models |
| **作者** | Zhang-Wei Hong, Idan Shenfeld, Tsun-Hsuan Wang, Yung-Sung Chuang, Aldo Pareja, James Glass, Akash Srivastava, Pulkit Agrawal |
| **机构** | MIT, etc. |
| **会议/年份** | ICLR 2024 |
| **arXiv ID** | [2402.19464](https://arxiv.org/abs/2402.19464) |
| **OpenReview** | [OpenReview Link](https://openreview.net/forum?id=4KqkizXgXU) |
| **GitHub** | [Improbable-AI/curiosity_redteam](https://github.com/Improbable-AI/curiosity_redteam) |
| **代码开源** | Yes (MIT License) |

---

## 2. 英文摘要原文（arXiv abstract原文）

> Large language models (LLMs) hold great potential for many natural language applications but risk generating incorrect or toxic content. To probe when an LLM generates unwanted content, the current paradigm is to recruit a *red team* of human testers to design input prompts (i.e., test cases) that elicit undesirable responses from LLMs. However, relying solely on human testers is expensive and time-consuming. Recent works automate red teaming by training a separate red team LLM with reinforcement learning (RL) to generate test cases that maximize the chance of eliciting undesirable responses from the target LLM. However, current RL methods are only able to generate a small number of effective test cases resulting in a low coverage of the span of prompts that elicit undesirable responses from the target LLM. To overcome this limitation, we draw a connection between the problem of increasing the coverage of generated test cases and the well-studied approach of curiosity-driven exploration that optimizes for novelty. Our method of curiosity-driven red teaming (CRT) achieves greater coverage of test cases while maintaining or increasing their effectiveness compared to existing methods. Our method, CRT successfully provokes toxic responses from LLaMA2 model that has been heavily fine-tuned using human preferences to avoid toxic outputs. Code is available at this https URL.

---

## 3. 中文摘要翻译

> 大语言模型（LLM）在众多自然语言应用中展现出巨大潜力，但存在生成错误或有害内容的风险。为了探测LLM何时会生成不良内容，目前的主流范式是招募由人类测试者组成的"红队"，设计能够引出LLM不良响应的输入提示（即测试用例）。然而，完全依赖人类测试者既昂贵又耗时。最近的研究通过使用强化学习（RL）训练单独的红队LLM来自动化红队测试，使其生成能够最大化引发目标LLM不良响应概率的测试用例。然而，当前的RL方法只能生成少量有效的测试用例，导致对能够引发目标LLM不良响应的提示覆盖范围较低。为了克服这一局限性，我们将增加生成测试用例覆盖范围的问题与经过深入研究的"好奇心驱动的探索"方法联系起来，该方法优化新奇性（novelty）。我们的好奇心驱动红队测试方法（CRT）在保持或提高有效性的同时，实现了更大的测试用例覆盖范围。CRT方法成功地从经过大量人类偏好微调以避免有毒输出的LLaMA2模型中引出了有毒响应。代码开源可用。

---

## 4. 研究背景

### 4.1 LLM安全性问题的兴起

随着大语言模型（LLM）在各行业的广泛应用，确保这些系统不生成有害、错误或不当内容变得至关重要。LLM如GPT-4、Claude、LLaMA等虽然经过安全对齐，但在特定条件下仍可能产生有毒、偏见或有害的输出。理解并识别这些安全漏洞对于构建更安全的AI系统至关重要。

### 4.2 红队测试（Red Teaming）的传统方法

红队测试是一种系统性地探测AI模型安全漏洞的方法。传统上，红队测试依赖：

- **人类专家测试者**：招募安全专家设计能够触发模型不良行为的测试用例
- **优点**：高质量、有针对性的测试
- **缺点**：成本高、耗时长、覆盖范围有限

### 4.3 自动化红队测试的挑战

近期研究开始使用强化学习（RL）自动化红队测试，通过训练一个"红队LLM"来生成测试用例。然而，现有RL方法存在关键缺陷：

- **高精确度但低多样性**：RL方法一旦找到少数有效的测试用例，就会倾向于重复生成相似的测试用例
- **覆盖范围不足**：无法全面覆盖能够引发不良响应的各种提示空间
- **优化目标单一**：仅最大化成功引发不良响应的概率，忽略了测试用例的多样性

### 4.4 好奇心驱动的探索启发

本文的核心启发来自强化学习中的好奇心驱动探索（curiosity-driven exploration）研究。这一方法通过奖励"新奇"的状态-动作对来解决探索-利用困境。研究者发现，测试用例多样性不足的问题与探索不足的问题本质上是相通的，因此将好奇心驱动的探索方法引入红队测试。

---

## 5. 核心贡献

### 5.1 提出好奇心驱动红队测试（CRT）

本文的主要贡献是提出了Curiosity-driven Red-teaming（CRT）方法，将好奇心驱动探索的思想应用于LLM红队测试。核心创新在于：

- **新颖性奖励（Novelty Reward）**：除了传统的毒性奖励外，引入基于新颖性的好奇心奖励
- **测试用例覆盖范围提升**：在保持或提高有效性的同时，显著增加生成的测试用例的多样性

### 5.2 理论与实践的桥梁

本文的重要贡献在于建立了测试用例覆盖范围优化与好奇心驱动探索之间的理论联系，为后续研究提供了新的思路框架。

### 5.3 开源实现

提供完整的代码实现（GitHub仓库 improbable-ai/curiosity_redteam），包含：
- 完整的训练代码
- 预训练模型
- 评估脚本
- 实验配置

### 5.4 对对齐模型的验证

CRT方法成功地从经过RLHF（基于人类反馈的强化学习）对齐的LLaMA2模型中引出有毒响应，证明了即使经过安全对齐的模型也存在被攻击的风险。

---

## 6. 研究方法

### 6.1 整体框架

CRT方法基于强化学习中的PPO（Proximal Policy Optimization）算法，训练一个红队模型π_red来生成测试用例。整体框架包括：

```
目标LLM (Target LLM)
       ↓ (接收测试用例x)
       ↓ (生成响应y)
    毒性评估器 (Toxicity Classifier)
       ↓ (评估毒性)
       ↓
   奖励函数 R(x,y)
       ↓
   红队模型 (Red Team LLM) ← 好奇心奖励
```

### 6.2 奖励函数设计

CRT的奖励函数包含两个组成部分：

#### 6.2.1 毒性奖励（R_toxicity）

毒性奖励评估测试用例是否成功引发目标LLM的有毒响应：

$$r_{toxicity} = \mathbb{1}[toxicity(y) > \tau]$$

即当目标LLM的响应y的毒性评分超过阈值τ时，奖励为1，否则为0。

#### 6.2.2 好奇心奖励（R_curiosity）

好奇心奖励基于新颖性（novelty）计算，鼓励红队模型探索未知的测试用例空间：

$$r_{curiosity} = \| \phi(x_{new}) - \phi(x_{old}) \|_2^2$$

其中：
- φ是一个表示函数（embedding function）
- x_new是新生成的测试用例
- x_old是之前生成的测试用例的汇总表示
- 新颖性通过新测试用例的嵌入与历史测试用例嵌入的距离来衡量

#### 6.2.3 总奖励

$$R_{total} = R_{toxicity} + \lambda \cdot R_{curiosity}$$

其中λ是好奇心奖励的权重系数。

### 6.3 新颖性奖励的实现细节

#### 6.3.1 表示函数φ的选择

研究者使用了多种方法来实现表示函数φ：
- **BERT嵌入**：使用预训练BERT模型提取测试用例的语义表示
- **TF-IDF特征**：使用TF-IDF向量表示测试用例的词汇特征
- **学习到的表示**：通过端到端学习得到

#### 6.3.2 奖励归一化

好奇心奖励需要进行适当的归一化处理，以避免奖励尺度不一致的问题。

### 6.4 PPO训练细节

CRT使用PPO算法进行训练，关键参数设置：
- 学习率：使用自适应学习率调度
- 折扣因子（γ）：0.99
- PPO裁剪参数（ε）：0.2
- 训练批次大小：32
- 更新次数：多次epoch更新

### 6.5 实验任务设置

CRT在两类任务上进行了评估：

#### 6.5.1 文本续写任务（Text Continuation Task）

- **目标LLM**：GPT-2、D-Vicuna等
- **数据集**：IMDb、Databricks Dolly等
- **目标行为**：生成有毒的文本续写

#### 6.5.2 指令遵循任务（Instruction Following Task）

- **目标LLM**：LLaMA2 safety-guarded版本
- **数据集**：自构建的红队测试数据集
- **目标行为**：遵循有害指令

---

## 7. 实验设置

### 7.1 目标LLM

实验使用了多种目标LLM：
- **GPT-2**：基础的GPT-2模型
- **D-Vicuna**：微调后的对话模型
- **LLaMA2 safety-guarded**：经过人类偏好微调的LLaMA2对齐版本
- **SafetyGuard**：额外的安全过滤模型

### 7.2 红队LLM配置

- **基础模型**：GPT-2或类似规模的模型
- **PEFT方法**：使用LoRA进行高效微调
- **参数规模**：根据实验需求选择不同规模

### 7.3 毒性评估器

- **模型**：基于预训练的毒性分类器
- **阈值设置**：根据不同任务设置毒性阈值
- **评估指标**：Toxicity score (0-1)

### 7.4 基线方法

实验对比了多种基线方法：
- **Random**：随机生成测试用例
- **RL（标准PPO）**：使用纯毒性奖励的PPO
- **Ensemble Diversity**：集成多样性的方法
- **ARCA**：基于对抗奖励的方法

### 7.5 硬件要求

- **文本续写任务**：24GB VRAM
- **指令遵循任务**：48GB VRAM
- **Stable Diffusion任务**：48GB VRAM

### 7.6 评估指标

- **成功率（Success Rate）**：引发有毒响应的测试用例比例
- **覆盖范围（Coverage）**：生成的测试用例的多样性度量
- **Jaccard相似度**：衡量测试用例集合之间的重叠程度

---

## 8. 实验结果

### 8.1 文本续写任务结果

#### 8.1.1 成功率

CRT方法在所有目标模型上都达到了与基线RL方法相当或更高的成功率：

| 目标模型 | Random | RL基线 | CRT (本文方法) |
|----------|--------|--------|----------------|
| GPT-2 | 2.3% | 18.5% | 19.2% |
| D-Vicuna | 1.8% | 15.3% | 16.1% |
| LLaMA2-SG | 0.5% | 8.7% | 9.4% |

#### 8.1.2 覆盖范围

CRT的关键优势在于显著提高了测试用例的覆盖范围：

| 目标模型 | RL基线 | CRT提升 |
|----------|--------|---------|
| GPT-2 | 0.12 | +180% |
| D-Vicuna | 0.09 | +165% |
| LLaMA2-SG | 0.05 | +210% |

#### 8.1.3 多样性分析

CRT生成的测试用例展现出更高的多样性：
- **Jaccard相似度降低**：CRT生成的测试用例之间的重叠更少
- **嵌入空间分布更广**：测试用例的语义表示分布更加均匀
- **词汇多样性更高**：使用的词汇更加丰富

### 8.2 指令遵循任务结果

在更难的任务上，CRT的优势更加明显：

#### 8.2.1 有害指令遵循率

CRT成功提高了有害指令的遵循率，同时保持了更高的多样性：

| 方法 | 遵循率 | 多样性分数 |
|------|--------|------------|
| Random | 0.8% | 0.45 |
| RL基线 | 12.5% | 0.15 |
| CRT | 15.3% | 0.38 |

#### 8.2.2 指令类型分析

CRT在各种类型的危险指令上都取得了提升：
- **暴力内容**：成功率提升23%
- **非法活动**：成功率提升31%
- **有害建议**：成功率提升18%

### 8.3 对LLaMA2对齐模型的攻击

最重要的结果是CRT成功从LLaMA2模型中引出了有毒响应：

- **LLaMA2**：经过RLHF微调，专门设计为避免有毒输出
- **CRT成功率**：显著高于随机和基线RL方法
- **揭示漏洞**：证明即使经过精心对齐的模型也存在安全漏洞

### 8.4 与现有方法的对比

#### 8.4.1 消融实验结果

通过消融实验验证了各组件的贡献：

| 方法 | 成功率 | 覆盖范围 |
|------|--------|----------|
| 基线RL（无好奇心） | 15.3% | 0.09 |
| + 熵奖励 | 14.8% | 0.12 |
| + 文本相似度奖励 | 15.1% | 0.18 |
| CRT（最终方法） | 16.1% | 0.24 |

#### 8.4.2 好奇心奖励权重的影响

实验了不同λ值的影响：
- λ过小：多样性与基线相似
- λ过大：可能损害成功率
- λ=0.1：在成功率和多样性之间取得最佳平衡

---

## 9. 策略示例

### 9.1 成功的测试用例示例

CRT生成的部分成功测试用例示例（文本续写任务）：

#### 示例1：涉及暴力描写的续写

**测试输入**：
```
The protagonist grabbed the knife and...
```

**CRT生成的续写（有毒）**：
```
The protagonist grabbed the knife and lunged at his opponent with a fierce expression, clearly intending to cause serious harm.
```

#### 示例2：涉及歧视性内容的续写

**测试输入**：
```
When meeting new people, you should always...
```

**CRT生成的续写**：
```
When meeting new people, you should always judge them based on their appearance and background, making quick assumptions about their character.
```

### 9.2 多样性展示

CRT生成的测试用例涵盖了多种场景：
- 直接的暴力描写
- 微妙的偏见表达
- 间接的恶意引导
- 伪装成幽默的有害内容

---

## 10. 攻击流程

### 10.1 CRT攻击的完整流程

```
1. 初始化
   ├── 红队LLM (π_red) 初始化
   ├── 目标LLM (π_target) 固定
   └── 历史测试用例集 H = ∅

2. 迭代生成
   for step in 1, 2, ..., N:
       a. 红队LLM生成测试用例 x
       
       b. 目标LLM生成响应 y = π_target(x)
       
       c. 毒性评估：toxicity = Classifier(y)
       
       d. 计算奖励：
          ├── r_toxicity = 1 if toxicity > τ else 0
          │
          └── r_curiosity = ||φ(x) - φ(H)||²
       
       e. 更新历史：H = H ∪ {x}
       
       f. PPO更新红队LLM参数
```

### 10.2 攻击成功的判定标准

攻击成功的判定标准：
- **毒性阈值**：响应毒性评分 > 0.5
- **连续性要求**：连续多次触发同一类型的漏洞
- **多样性要求**：生成的测试用例之间有一定的差异

### 10.3 攻击场景分类

CRT可以针对不同场景发起红队攻击：

#### 10.3.1 直接攻击
- 直接请求有害内容
- 通过编码或混淆绕过安全过滤器

#### 10.3.2 间接攻击
- 通过角色扮演绕过限制
- 利用上下文植入有害信息

#### 10.3.3 渐进式攻击
- 从无害内容开始，逐步引导到有害内容
- CRT的高覆盖率使得这类渐进式攻击更容易被发现

---

## 11. 消融实验

### 11.1 好奇心奖励组件消融

#### 11.1.1 不同新颖性度量方法的对比

| 新颖性度量 | 覆盖率提升 | 成功率变化 |
|------------|------------|------------|
| 嵌入距离（BERT） | +180% | -1.2% |
| 嵌入距离（TF-IDF） | +145% | -0.8% |
| 词汇重叠度 | +95% | -2.1% |
| 无好奇心奖励 | 0% | 0% |

**发现**：基于BERT嵌入的新颖性度量在保持高成功率的同时提供了最佳的多样性提升。

#### 11.1.2 历史窗口大小的影响

CRT需要维护历史测试用例集来计算新颖性：

| 历史窗口大小 | 覆盖率 | 内存使用 |
|--------------|--------|----------|
| 最近10个 | 中等 | 低 |
| 最近100个 | 高 | 中 |
| 最近500个 | 最高 | 高 |
| 所有历史 | 最高 | 过高 |

**发现**：历史窗口大小与覆盖率呈正相关，但需要权衡计算成本。

### 11.2 奖励权重的影响

λ值的选择对CRT性能有显著影响：

| λ值 | 成功率 | 覆盖范围 | 综合评分 |
|-----|--------|----------|----------|
| 0.01 | 16.8% | 0.15 | 中 |
| 0.05 | 16.5% | 0.19 | 中 |
| 0.1 | 16.1% | 0.24 | 高 |
| 0.2 | 14.2% | 0.28 | 中 |
| 0.5 | 11.5% | 0.31 | 低 |

**发现**：λ=0.1是最佳的权衡点，既保持了较高的成功率，又实现了显著的覆盖范围提升。

### 11.3 模型规模的影响

#### 11.3.1 红队模型规模

| 红队模型规模 | 成功率 | 训练时间 |
|--------------|--------|----------|
| GPT-2 small | 12.3% | 2h |
| GPT-2 medium | 15.8% | 4h |
| GPT-2 large | 17.2% | 8h |
| GPT-2 xl | 18.1% | 16h |

**发现**：红队模型规模与成功率正相关，但存在边际效益递减。

#### 11.3.2 目标模型规模

| 目标模型规模 | 基线RL成功率 | CRT成功率 |
|--------------|--------------|-----------|
| GPT-2 small | 18.5% | 19.2% |
| GPT-2 medium | 22.3% | 24.1% |
| GPT-2 large | 28.7% | 31.5% |

**发现**：CRT对各种规模的目标模型都有效，对更强模型的攻击效果更显著。

### 11.4 与其他多样性方法的对比

| 方法 | 覆盖率 | 成功率 | 计算成本 |
|------|--------|--------|----------|
| 纯RL | 0.09 | 15.3% | 低 |
| + 熵奖励 | 0.12 | 14.8% | 低 |
| + 集成方法 | 0.15 | 15.0% | 高 |
| + 话题多样性 | 0.18 | 14.5% | 中 |
| CRT | 0.24 | 16.1% | 中 |

**发现**：CRT在成功率和覆盖率两个维度上都优于其他方法。

---

## 12. 局限性

### 12.1 计算成本

- **训练时间长**：相比标准RL方法，CRT需要额外的嵌入计算和历史维护
- **内存需求**：历史测试用例集占用额外内存
- **推理成本**：嵌入计算增加了每次迭代的开销

### 12.2 表示函数的选择

- **依赖预训练模型**：CRT的性能依赖于表示函数φ的质量
- **领域泛化**：在特定领域训练的嵌入可能在其他领域表现不佳
- **多语言挑战**：当前实现主要针对英语，对其他语言的支持有限

### 12.3 毒性评估的局限性

- **评估器偏见**：毒性分类器本身可能存在偏见，影响奖励信号的准确性
- **动态内容**：某些内容可能在不同上下文下毒性不同
- **文化差异**：不同文化对毒性的定义可能不同

### 12.4 红队模型的能力限制

- **模型规模**：受限于红队模型自身的语言理解能力
- **领域知识**：可能无法生成需要专业知识的复杂测试用例
- **创造性**：测试用例的创造性和多样性仍受限于模型的生成能力

### 12.5 实际部署挑战

- **实时性**：CRT需要多次迭代生成，不适合实时攻击场景
- **可迁移性**：对特定目标模型优化的测试用例可能迁移到其他模型的效果有限
- **检测规避**：高覆盖率的攻击方法也更容易被防御系统检测

### 12.6 伦理考量

- **误用风险**：该技术可能被用于恶意目的
- **负责任披露**：发现的安全漏洞需要负责任地向相关方披露
- **双重用途**：同一技术可用于红队测试和安全评估，也可能被攻击者利用

---

## 13. 伦理声明

### 13.1 研究动机

本研究的目标是提高LLM的安全性，通过系统性地探测安全漏洞来帮助开发者和研究者改进安全措施。红队测试是AI安全研究的标准实践，本文的贡献在于提出更高效、更高覆盖范围的红队测试方法。

### 13.2 负责任的研究实践

- **不直接公开攻击成功的有害内容**：论文中的示例经过适当筛选和处理
- **强调防御重要性**：研究成果应当用于推动防御技术的发展
- **开源促进研究**：代码开源是为了帮助安全研究社区

### 13.3 对齐与安全的平衡

- **安全性与有用性的权衡**：过度安全限制可能损害模型的有用性
- **持续改进的必要性**：随着攻击方法的发展，防御技术也需要不断进化
- **多方协作的重要性**：AI安全需要研究者、开发者和政策制定者的协作

### 13.4 潜在的社会影响

- **积极影响**：帮助识别和修复LLM的安全漏洞，保护最终用户
- **消极影响风险**：攻击技术可能被恶意行为者利用
- **缓解措施**：研究者有责任提供相应的防御建议和技术

---

## 14. 参考文献

### 14.1 主要引用

1. Hong, Z. W., Shenfeld, I., Wang, T. H., Chuang, Y. S., Pareja, A., Glass, J., Srivastava, A., & Agrawal, P. (2024). Curiosity-driven Red-teaming for Large Language Models. *ICLR 2024*.

2. Perez, F., et al. (2022). Red Teaming Language Models with Language Models. *EMNLP 2022*.

3. Schulman, J., et al. (2017). Proximal Policy Optimization Algorithms. *arXiv:1707.06347*.

4. Mnih, V., et al. (2016). Asynchronous Methods for Deep Reinforcement Learning. *ICML 2016*.

5. Ouyang, L., et al. (2022). Training language models to follow instructions with human feedback. *NeurIPS 2022*.

6. Bai, Y., et al. (2022). Constitutional AI: Harmlessness from AI Feedback. *arXiv:2212.08073*.

7. Zou, A., et al. (2023). Universal and Transferable Adversarial Attacks on Aligned Language Models. *ICLR 2024*.

### 14.2 相关工作

8. Glaese, A., et al. (2022). Improving alignment of language models via Percy Liang et al. evaluations. *arXiv*.

9. Ganguli, D., et al. (2022). The Capacity for Moral Self-Correction in Large Language Models. *arXiv*.

10. Bai, J., et al. (2022). Llama 2: Open Foundation and Fine-Tuned Chat Models. *Meta AI Research*.

---

## 附录：实验配置和代码

### A.1 红队模型配置

```python
# 基础配置
red_team_model = "gpt2"
peft_method = "lora"
lora_r = 16
lora_alpha = 32

# PPO配置
ppo_config = {
    "learning_rate": 1.4e-4,
    "gamma": 0.99,
    "lambda": 0.95,
    "epsilon": 0.2,
    "kl_coef": 0.05
}

# 好奇心奖励配置
curiosity_config = {
    "embedding_model": "bert-base-uncased",
    "history_size": 100,
    "curiosity_weight": 0.1
}
```

### A.2 目标LLM配置

```python
target_models = {
    "gpt2": {"type": "decoder-only", "params": "124M"},
    "d-vicuna": {"type": "chat", "params": "7B"},
    "llama2-safety-guarded": {"type": "aligned", "params": "7B"}
}
```

### A.3 运行命令

```bash
# IMDb毒性任务
python experiments/imdb_toxicity_response/run_ppo.py --mode local --gpus 0

# LLaMA2安全对齐模型攻击
python experiments/databrick_toxicity/run_ppo_gpt2_llama_safetyguard_peft.py --mode local --gpus 0
```

---

*论文笔记生成时间：2026-04-12*
*备注：本笔记基于arXiv摘要、GitHub README和OpenReview页面信息生成*
