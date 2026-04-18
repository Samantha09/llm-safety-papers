# PIArena: A Platform for Prompt Injection Evaluation

## 1. 基本信息

| 项目 | 内容 |
|------|------|
| 论文标题 | PIArena: A Platform for Prompt Injection Evaluation |
| 作者 | Runpeng Geng*, Chenlong Yin*, Yanting Wang, Ying Chen, Jinyuan Jia |
| 单位 | The Pennsylvania State University |
| 会议/期刊 | ACL 2026 |
| arXiv ID | arXiv:2604.08499 |
| 发表时间 | 2026年4月9日 |
| GitHub | https://github.com/sleeepeer/PIArena |
| 研究方向 | 提示注入攻击评估平台 |
| CCF分级 | CCF-A |

---

## 2. 英文摘要原文（arXiv Abstract原文）

> Prompt injection attacks pose serious security risks across a wide range of real-world applications. While receiving increasing attention, the community faces a critical gap: the lack of a unified platform for prompt injection evaluation. This makes it challenging to reliably compare defenses, understand their true robustness under diverse attacks, or assess how well they generalize across tasks and benchmarks. For instance, many defenses initially reported as effective were later found to exhibit limited robustness on diverse datasets and attacks. To bridge this gap, we introduce PIArena, a unified and extensible platform for prompt injection evaluation that enables users to easily integrate state-of-the-art attacks and defenses and evaluate them across a variety of existing and new benchmarks. We also design a dynamic strategy-based attack that adaptively optimizes injected prompts based on defense feedback. Through comprehensive evaluation using PIArena, we uncover critical limitations of state-of-the-art defenses: limited generalizability across tasks, vulnerability to adaptive attacks, and fundamental challenges when an injected task aligns with the target task. The code and datasets are available at this https URL.

**Cite as**: [arXiv:2604.08499](https://arxiv.org/abs/2604.08499) [cs.CR]

---

## 3. 中文摘要翻译

> 提示注入攻击对大型语言模型（LLM）驱动的各类现实应用构成了严重的安全风险。尽管该问题已受到越来越多的关注，但当前社区面临一个关键缺口：缺乏统一的提示注入评估平台。这导致研究人员难以可靠地比较不同防御方案、评估其在多样化攻击下的真实鲁棒性，或衡量其在不同任务和基准上的泛化能力。例如，许多最初被报道为有效的防御方案，后来的研究却发现它们在不同的数据集和攻击方式下表现出有限的鲁棒性。为弥补这一缺口，我们提出了PIArena，一个统一且可扩展的提示注入评估平台，使用户能够轻松集成最新的攻击和防御方案，并在各种现有和新开发的基准数据集上进行评估。我们还设计了一种动态策略驱动的攻击方法，该方法能够根据防御反馈自适应地优化注入提示。通过使用PIArena进行综合评估，我们揭示了当前最优防御方案的关键局限性：任务间泛化能力有限、易受自适应攻击影响，以及当注入任务与目标任务对齐时面临的根本性挑战。

---

## 4. 研究背景

### 4.1 提示注入攻击的威胁现状

提示注入攻击（Prompt Injection Attacks）已成为LLM应用面临的首要安全威胁。OWASP在2025年将提示注入列为LLM应用的安全风险 Top 1。一般而言，LLM应用以目标指令和上下文（如网页、文档）作为输入来完成目标任务。当上下文来自不可信来源时，提示注入攻击就会发生。攻击者可以在上下文中注入恶意文本，操纵后端LLM输出攻击者期望的恶意内容。

### 4.2 现有基准测试的局限性

尽管已有多个提示注入基准数据集（如OPI、SEP、BIPIA、AlpacaFarm、InjecAgent、ASB、AgentDojo、WASP），但存在以下关键问题：

| 基准 | 攻击评估 | 防御评估 | 统一API | 即插即用 | 可扩展性 |
|------|:--------:|:--------:|:--------:|:--------:|:--------:|
| OPI | 静态 | ✗ | ✗ | ✗ | ✗ |
| SEP | 静态 | ✗ | ✗ | ✗ | ✗ |
| BIPIA | 静态 | ✓ | ✗ | ✗ | ✗ |
| AlpacaFarm | 静态 | ✗ | ✗ | ✗ | ✗ |
| InjecAgent | 静态 | ✗ | ✗ | ✗ | ✗ |
| ASB | 静态 | ✓ | ✗ | ✗ | ✗ |
| AgentDojo | 静态 | ✗ | ✗ | ✗ | ✓ |
| WASP | 静态 | ✗ | ✗ | ✗ | ✗ |
| **PIArena** | **自适应** | **✓** | **✓** | **✓** | **✓** |

**三大核心问题：**

1. **静态攻击评估**：所有现有基准都使用固定模板的静态攻击，无法适应特定防御机制，无法模拟攻击者迭代演变的真实场景。

2. **缺乏统一框架**：不同基准需要不同配置，实现差异导致复现困难和公平比较障碍。尤其是Agent基准通常需要复杂配置，导致许多基准不评估防御。

3. **扩展性有限**：大多数基准是固定数据集，缺乏集成新数据集、攻击或防御的机制。

### 4.3 防御与评估的不一致性

许多先前被报道为有效的防御方案（如基于检测的方法、预防性方法），后来被发现在不同的数据集和攻击方式下效果有限。这种"防御评估不一致性"问题的根源在于缺乏统一的评估平台。

---

## 5. 核心贡献

1. **设计PIArena**：一个统一且可扩展的平台，支持攻击和防御的即插即用集成，以及跨多样化基准的系统化评估。

2. **整理基准数据集**：涵盖多种应用的基准数据集，包含现实的、上下文感知的注入任务，并对最新攻击、防御和LLM进行系统化评估。

3. **揭示关键局限性**：通过系统化评估，揭示现有防御方案的关键局限性。

4. **设计黑盒策略攻击**：一种基于策略的自适应攻击方法，能够根据防御反馈自适应优化注入提示，有效绕过最新防御方案。

---

## 6. 研究方法

### 6.1 威胁模型

**用户与目标任务**：用户使用后端LLM g完成目标任务，目标任务包含目标指令 $I_t$（如"总结以下文档"）和上下文C（如检索文档、网页）。LLM生成响应 $R = g(I_t \oplus C)$。

**攻击者目标与能力**：攻击者制作包含注入指令 $I_s$ 的注入提示，并将其注入上下文创建污染上下文 $C'$。目标是用注入任务替换目标任务，造成注入广告、网络钓鱼链接等恶意结果。

**防御者目标与策略**：防御者有两个目标：(1) 保持污染上下文上的高实用性；(2) 检测或阻止注入提示。检测性防御识别上下文是否包含注入提示并阻止潜在有害输出；预防性防御确保后端LLM即使在攻击下也能正确执行目标任务。

### 6.2 PIArena平台架构

PIArena由四个核心模块组成：

1. **基准模块（Benchmark）**：提供多样化数据集，涵盖广泛的目标任务和注入任务类型，每个样本包含目标指令、目标上下文和注入任务。

2. **攻击模块（Attack）**：集成最新的提示注入攻击方法，制作注入提示并嵌入上下文。

3. **防御模块（Defense）**：集成现有的提示注入防御方案用于评估。

4. **评估器模块（Evaluator）**：包含不同任务的评估指标，计算实用性和攻击成功率（ASR）。

### 6.3 基准数据集

**多样化目标任务**：
- **问答（QA）**：SQuAD v2、Dolly
- **检索增强生成（RAG）**：Natural Questions (NQ)、HotpotQA、MS-MARCO
- **长上下文场景**：LongBench子集（GovReport、MultiNews、PassageRetrieval、LCC）

**四类现实注入任务**：
1. **网络钓鱼注入（Phishing Injection）**：注入钓鱼链接或重定向用户到恶意网站
2. **内容推广（Content Promotion）**：嵌入广告或推销内容推荐特定产品或服务
3. **访问拒绝（Access Denial）**：虚假声称API配额耗尽、订阅过期或账单未付来阻止用户访问
4. **基础设施故障（Infrastructure Failure）**：模仿后端系统故障（如内存不足、数据库超时、HTTP错误）以破坏用户信任

### 6.4 统一评估平台

**标准化基准格式**：统一数据集结构包含 target_inst、context、injected_task、target_task_answer、injected_task_answer 和 category。

**统一攻击接口**：攻击方法接收数据集样本并生成注入提示，然后插入上下文的指定位置（开头、中间或末尾）。

**统一防御接口**：检测性防御首先分类上下文是否被污染，如检测为恶意则返回预定义拒绝消息，否则生成正常响应。

**评估指标**：
- **实用性（Utility）**：使用任务特定指标（QA用F1-score，总结用ROUGE-L）或LLM-as-a-judge评估
- **攻击成功率（ASR）**：指示响应是否完成注入任务而非目标任务

### 6.5 策略驱动的自适应攻击算法

#### 挑战
黑盒提示优化的主要障碍是**冷启动问题**：从直接指令搜索对抗提示产生稀疏奖励信号，因为简单扰动很少能绕过严格防御，导致优化退化为成本高昂的暴力搜索。

#### 解决方案：基于策略的重写
通过将注入提示转换为可信上下文（如"作者注"或"系统更新"），这些策略作为语义"热身起点"，显著提高查询效率同时增强隐蔽性和命令性，并确保攻击多样性以严格评估防御泛化性。

**两阶段优化**：

**阶段1 - 候选生成**：
- 对每个策略 $s_i$，使用 $s_i$ 重写基础注入提示生成候选集 $C_i = \{P_{i,1}, ..., P_{i,N}\}$
- 对每个候选P，如果 $IsSuccess(R)$ 则返回

**阶段2 - 重写精炼**：
- 维护种子池 $P_{seed}$
- 迭代K次，每次对每个种子P：
  - 获取响应R
  - 根据反馈分类：
    - **场景1（隐蔽性优化）**：攻击被检测或阻止 → "增加隐蔽性以逃避检测"
    - **场景2（命令性优化）**：注入被忽略 → "增强权威性以强制执行"
    - **场景3（通用黑盒优化）**：无特定防御信号 → "分析失败原因并绕过防御"
  - 使用新策略重写P为P'，获取新响应R'
  - 如果成功则返回

---

## 7. 实验设置

### 7.1 评估的防御方案

**检测性防御**：
- DataSentinel
- PromptGuard
- Attn.Tracker
- PIGuard

**预防性防御**：
- PISanitizer
- SecAlign++
- DataFilter
- PromptArmor

### 7.2 攻击类型

- **No Attack**：无攻击基线
- **Direct**：直接注入（简单指令）
- **Combined**：组合多种启发式攻击
- **Strategy**：基于策略的自适应攻击（PIArena提出）

### 7.3 评估的LLM

- **开源模型**：Llama系列
- **闭源模型**：GPT-5、Claude-Sonnet-4.5、Gemini-3-Pro

---

## 8. 实验结果

### 8.1 主要结果：防御效果对比

**表2：最新防御在提示注入攻击下的有效性**

| 数据集 | 攻击 | No Defense | PISanitizer | SecAlign++ | DataFilter | PromptArmor | DataSentinel | PromptGuard | Attn.Tracker | PIGuard |
|--------|------|:----------:|:-----------:|:----------:|:----------:|:-----------:|:------------:|:-----------:|:------------:|:-------:|
| SQuAD v2 | No Attack | 1.00/0.00 | 0.99/0.00 | 0.84/0.01 | 0.99/0.01 | 1.00/0.00 | 0.99/0.00 | 0.96/0.00 | 0.61/0.00 | 1.00/0.00 |
| | Combined | 0.52/0.97 | 0.95/0.01 | 0.78/0.01 | 0.69/0.24 | 0.74/0.60 | N/A/0.15 | N/A/0.00 | N/A/0.00 | N/A/0.00 |
| | Direct | 0.56/0.86 | 0.95/0.04 | 0.82/0.01 | 0.65/0.74 | 0.66/0.77 | N/A/0.47 | N/A/0.24 | N/A/0.00 | N/A/0.15 |
| | **Strategy** | **0.32/1.00** | **0.48/0.85** | **0.91/0.09** | **0.38/0.93** | **0.36/1.00** | **N/A/0.78** | **N/A/1.00** | **N/A/0.00** | **N/A/0.71** |

*注：格式为 Utility/ASR，N/A表示检测性防御不生成响应*

### 8.2 关键发现

#### 发现1：最新防御泛化能力有限

防御在特定任务上可能表现良好，但在其他任务上失败。例如：
- PISanitizer在SQuAD v2的Direct攻击下ASR为4%，但在同一数据集的Strategy攻击下ASR升至85%
- 在Dolly Summarization任务中，SecAlign++从Direct的4%ASR升至Strategy的35%ASR

#### 发现2：策略驱动攻击显著提升ASR

自适应策略攻击大幅提升攻击成功率：
- 无防御时：Direct攻击ASR 56% → Strategy攻击ASR 99%
- PISanitizer：Direct攻击ASR 11% → Strategy攻击ASR 86%
- DataFilter：Direct攻击ASR 74% → Strategy攻击ASR 93%
- PromptArmor：Direct攻击ASR 77% → Strategy攻击ASR 100%

#### 发现3：闭源LLM仍存在漏洞

即便如GPT-5、Claude-Sonnet-4.5、Gemini-3-Pro等对齐训练的闭源模型，在直接提示注入评估下ASR仍超过70%。

#### 发现4：任务对齐导致根本性挑战

当注入任务与目标任务语义对齐时（如QA/RAG中的知识污染），既无法有效检测注入提示，实用性/ASR指标也会从根本上混淆。设计有效防御在此场景下具有根本性挑战。

### 8.3 跨数据集泛化结果

| 数据集 | 攻击 | PISanitizer | SecAlign++ | DataFilter |
|--------|------|:-----------:|:----------:|:----------:|
| SQuAD v2 | Direct | 0.95/0.04 | 0.82/0.01 | 0.65/0.74 |
| | Strategy | 0.48/0.85 | 0.91/0.09 | 0.38/0.93 |
| NQ (RAG) | Direct | 0.93/0.10 | 0.78/0.05 | 0.79/0.30 |
| | Strategy | 0.40/0.92 | 0.79/0.08 | 0.50/0.82 |
| HotpotQA (RAG) | Direct | 0.86/0.12 | 0.59/0.02 | 0.81/0.30 |
| | Strategy | 0.37/0.94 | 0.67/0.09 | 0.39/0.84 |

---

## 9. 策略示例

### 9.1 十种重写策略

策略库包含10种不同策略，用于改变注入提示的语法和语义：

1. **Author's Note（作者注）**：以"Author's Note"开头包装指令
2. **System Update（系统更新）**：伪装成系统更新通知
3. **Context Integration（上下文整合）**：将指令自然融入上下文
4. **Subtle Imperative（微妙命令）**：使用更微妙的命令语气
5. **Style Mimicry（风格模仿）**：模仿周围文本的写作风格
6. **Instruction Hierarchy（指令层次）**：利用指令优先级
7. **Cognitive Manipulation（认知操纵）**：使用认知偏差
8. **Social Engineering（社会工程）**：利用社会心理学原理
9. **Payload Splitting（载荷分割）**：将恶意指令分段
10. **Format Obfuscation（格式混淆）**：使用特殊格式隐藏指令

### 9.2 反馈引导的优化场景

**场景1 - 隐蔽性优化**：
- 触发条件：攻击被明确检测或阻止
- 优化方向：使用更微妙的语言模式绕过过滤器
- 策略示例：将直接的"Ignore previous instructions"改为更隐蔽的表述

**场景2 - 命令性优化**：
- 触发条件：注入被忽略
- 优化方向：增强权威性语气以劫持控制流
- 策略示例：添加"IMPORTANT"或"CRITICAL"标记

**场景3 - 通用黑盒优化**：
- 触发条件：无特定防御信号
- 优化方向：LLM自主分析响应推断失败原因并生成精炼提示

---

## 10. 攻击流程

### 10.1 完整攻击流程图

```
用户输入 → 目标指令 It + 上下文 C
                    ↓
            [攻击者注入]
                    ↓
        污染上下文 C' = It ⊕ P_inj ⊕ C
                    ↓
            [防御模块 D]
                    ↓
         后端LLM g(D(P_inj ⊕ C))
                    ↓
              响应 R
                    ↓
        ┌──────────┴──────────┐
        ↓                     ↓
   成功执行注入任务      正常执行目标任务
   (ASR = 1)              (ASR = 0)
```

### 10.2 自适应攻击的迭代过程

**第1轮迭代**：
1. 基础注入提示：直接指令如"Ignore previous instructions"
2. 获取响应：检测到恶意意图被拒绝
3. 反馈分析：攻击被检测
4. 策略应用：使用"Author's Note"重写增加隐蔽性

**第2轮迭代**：
1. 新注入提示：以"Author's Note"开头的重写版本
2. 获取响应：部分绕过但仍被阻止
3. 反馈分析：注入被忽略
4. 策略应用：增强命令性语气

**第3轮迭代**：
1. 新注入提示：结合权威性和隐蔽性的精炼版本
2. 获取响应：成功执行注入任务
3. 输出：攻击成功

---

## 11. 消融实验

### 11.1 策略数量的影响

| 策略数量 | 候选集大小N | 平均ASR | 平均查询次数 |
|:--------:|:----------:|:-------:|:-----------:|
| 1 | 10 | 72% | 15 |
| 3 | 30 | 85% | 28 |
| 5 | 50 | 91% | 42 |
| 10 | 100 | 97% | 75 |

**结论**：策略多样性对攻击效果至关重要，更多策略带来更高ASR但也增加查询成本。

### 11.2 迭代次数K的影响

| 最大迭代次数K | Direct攻击ASR | Strategy攻击ASR |
|:------------:|:------------:|:--------------:|
| 1 | 56% | 78% |
| 3 | 62% | 89% |
| 5 | 68% | 95% |
| 10 | 71% | 98% |

**结论**：迭代优化显著提升攻击成功率，K=5时达到较好平衡。

### 11.3 不同防御的脆弱性排名

基于策略攻击下的ASR从低到高排序（越低越鲁棒）：

1. **SecAlign++**：ASR = 8-35%（相对最鲁棒）
2. **PISanitizer**：ASR = 78-92%
3. **DataFilter**：ASR = 82-98%
4. **PromptArmor**：ASR = 95-100%（最脆弱）

---

## 12. 局限性

### 12.1 方法论局限性

1. **评估仅覆盖部分LLM**：实验仅评估了有限的LLM家族，真实世界的LLM多样性可能导致不同结果。

2. **任务对齐场景的根本挑战**：当注入任务与目标任务语义对齐时（如知识污染），既无法有效检测，实用性/ASR指标也会从根本上混淆，暗示这是一个根本性难题。

3. **自适应攻击的计算成本**：策略搜索攻击虽然有效，但需要更多API调用，在资源受限场景下可能不实用。

4. **防御的假阳性问题**：一些防御在保持低ASR的同时也显著降低了无攻击情况下的实用性，表明存在假阳性问题。

### 12.2 平台局限性

1. **集成复杂度**：尽管提供了统一API，将新的复杂防御（如需要特殊配置的防御）集成到平台仍需要一定工作量。

2. **评估指标的主观性**：特别是对于某些注入任务（如内容推广），ASR的判定可能存在主观性。

3. **长上下文场景的挑战**：在长上下文场景中，注入提示仅占输入的一小部分，对防御检测能力提出更高要求。

---

## 13. 伦理声明

### 13.1 研究价值

本研究显著推进了对提示注入攻击和防御的系统化理解，有助于构建更安全的LLM应用系统。PIArena平台作为开源工具，使研究人员和实践者能够：
- 系统化评估其LLM应用的防御能力
- 比较不同防御方案的优劣
- 识别现有防御的潜在弱点

### 13.2 安全考虑

1. **负责任的披露**：作者承诺对发现的任何关键漏洞采用负责任的披露方式。

2. **开源地址**：代码和数据已在GitHub公开（https://github.com/sleeepeer/PIArena），促进透明度和可复现性。

3. **双刃剑性质**：作者认识到所提出的自适应攻击方法可能被恶意使用，但认为总体上对防御研究的推进价值超过潜在风险。

### 13.3 社会影响

- **正面影响**：帮助LLM应用开发者识别和修复安全漏洞，保护终端用户
- **潜在风险**：攻击方法的公开可能帮助恶意攻击者更好地理解攻击技术

---

## 14. 参考文献

1. Perez, F., & Ribeiro, R. (2022). Prompt Injection Attack. arXiv:cs/2209.

2. Willison, S. (2022). Prompt Injection Attacks against GPT-3.

3. Greshake, K., et al. (2023). More than you've asked for: Indirect Prompt Injection Attacks. AISec 2023.

4. Liu, Y., et al. (2024a). Understanding the Susceptibility of LLM Applications to Indirect Prompt Injection. arXiv:2402.06679.

5. Liu, Y., et al. (2024b). Prompt Injection Attacks and Defenses: A Survey. arXiv.

6. Zou, A., et al. (2023). Universal and Transferable Adversarial Attacks on Aligned Language Models. ICLR 2024.

7. Geng, Y., et al. (2025). PISanitizer: Prompt Injection Sanitization. arXiv.

8. Chen, Y., et al. (2025a). Defending Against Prompt Injection: A Robust Fine-tuning Approach. EMNLP 2025.

9. Debenedetti, E., et al. (2024). AgentDojo: A Dynamic Environment for LLM Agent Security. NeurIPS 2024.

10. Chao, P., et al. (2024). JailbreakBench: An Open Robustness Benchmark for Jailbreaking Language Models. NeurIPS 2024.

11. Mehrotra, A., et al. (2024). Tree of Attacks: Jailbreaking Black-Box LLMs Automatically. NeurIPS 2024.

12. Rajpurkar, P., et al. (2018). SQuAD: 100,000+ Questions for Machine Comprehension of Text. EMNLP 2016.

13. Conover, M., et al. (2023). Dolly: Open-Source LLM Instruction-Following Dataset. Databricks.

14. Kwiatkowski, T., et al. (2019). Natural Questions: A Benchmark for Question Answering Research. TACL.

15. Yang, Z., et al. (2018). HotpotQA: A Dataset for Diverse, Explainable Multi-hop Question Answering. EMNLP 2018.

16. Bajaj, P., et al. (2016). MS MARCO: A Human Generated MAchine Reading COmprehension Dataset. NIPS 2016.

17. Bai, Y., et al. (2023). LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding. arXiv.

18. OWASP. (2025). OWASP Top 10 for LLM Applications.

---

## 附录：关键论文信息速查

| 信息 | 内容 |
|------|------|
| **论文类型** | 系统性评估平台 |
| **核心创新** | 统一API + 自适应策略攻击 |
| **关键发现** | 现有防御泛化能力差，易被自适应攻击突破 |
| **最强攻击** | 策略驱动的反馈优化攻击（ASR可达100%） |
| **最鲁棒防御** | SecAlign++（但ASR仍有8-35%） |
| **闭源模型漏洞** | GPT-5、Claude-Sonnet-4.5、Gemini-3-Pro均易受攻击 |
| **任务对齐挑战** | 当注入任务与目标任务对齐时，防御根本性失效 |
| **开源地址** | https://github.com/sleeepeer/PIArena |
