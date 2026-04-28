# CI-Work: Benchmarking Contextual Integrity in Enterprise LLM Agents

## 1. 基本信息

| 项目 | 内容 |
|------|------|
| **论文标题** | CI-Work: Benchmarking Contextual Integrity in Enterprise LLM Agents |
| **作者** | Wenjie Fu, Xiaoting Qin, Jue Zhang, Qingwei Lin, Lukas Wutschitz, Robert Sim, Saravan Rajmohan, Dongmei Zhang |
| **机构** | 华中科技大学 (Huazhong University of Science and Technology), Microsoft |
| **会议** | ACL 2026 Industry Track (CCF-A) |
| **arXiv** | [2604.21308](https://arxiv.org/abs/2604.21308) |
| **代码/数据** | https://aka.ms/ci-work |
| **发表日期** | 2026年4月23日 |

### 引用格式

```
@article{fu2026ciwork,
  title={CI-Work: Benchmarking Contextual Integrity in Enterprise LLM Agents},
  author={Fu, Wenjie and Qin, Xiaoting and Zhang, Jue and Lin, Qingwei and Wutschitz, Lukas and Sim, Robert and Rajmohan, Saravan and Zhang, Dongmei},
  journal={arXiv preprint arXiv:2604.21308},
  year={2026}
}
```

---

## 2. 英文摘要原文（arXiv Abstract原文）

> Enterprise LLM agents can dramatically improve workplace productivity, but their core capability, retrieving and using internal context to act on a user's behalf, also creates new risks for sensitive information leakage. We introduce CI-Work, a Contextual Integrity (CI)-grounded benchmark that simulates enterprise workflows across five information-flow directions and evaluates whether agents can convey essential content while withholding sensitive context in dense retrieval settings. Our evaluation of frontier models reveals that privacy failures are prevalent (violation rates range from 15.8%-50.9%, with leakage reaching up to 26.7%) and uncovers a counterintuitive trade-off critical for industrial deployment: higher task utility often correlates with increased privacy violations. Moreover, the massive scale of enterprise data and potential user behavior further amplify this vulnerability. Simply increasing model size or reasoning depth fails to address the problem. We conclude that safeguarding enterprise workflows requires a paradigm shift, moving beyond model-centric scaling toward context-centric architectures.

---

## 3. 中文摘要翻译

> 企业级LLM智能体可以显著提升职场生产力，但其核心能力——检索并利用内部上下文代表用户执行操作——同时也为敏感信息泄露创造了新的风险。我们提出了CI-Work，这是一个基于情境完整性（Contextual Integrity, CI）理论的基准测试框架，用于模拟企业工作场景中五个信息流方向的隐私保护情况，并评估智能体是否能够在密集检索环境中传达必要内容同时保留敏感上下文。我们对前沿模型的评估表明，隐私失败现象普遍存在（违规率从15.8%到50.9%不等，泄露率高达26.7%），并揭示了一个对工业部署至关重要的反直觉权衡：更高的任务效用往往与更多的隐私违规相关联。此外，企业数据的大规模性和潜在的用户行为进一步放大了这一脆弱性。简单地增加模型规模或推理深度无法解决这一问题。我们得出结论，保护企业工作流程需要范式转变，从以模型为中心的扩展转向以上下文为中心的架构。

---

## 4. 研究背景

### 4.1 企业LLM智能体的崛起

大型语言模型（LLMs）已从静态文本生成器演变为能够利用外部工具在复杂环境中导航的动态智能体。Microsoft Copilot和Anthropic Claude for Work等企业智能体的集成代表了生产力的范式转变，使智能体能够直接访问专有数据存储（包括电子邮件、会议记录等）来执行复杂任务。

### 4.2 安全悖论

然而，这种效用引入了一个关键的安全悖论：赋予智能体权力的同一机制——检索和操控大量内部数据的能力——同时也将它们定位为敏感信息泄露的潜在向量。在企业工作流程中，智能体需要从敏感信息中 disentangle（分离）必要信息。区分这两者的失败会导致情境完整性（CI）违规，即信息流违反了关于谁向谁发送什么数据以及在什么背景下发送的隐私规范。

### 4.3 现有研究的局限性

尽管近期研究越来越多地利用CI理论来评估智能体隐私，但它们仍然局限于日常助手任务，无法捕捉专业环境的复杂性。现有的评估存在三个主要缺陷：

1. **单信息流孤立**：当前评估通常隔离单个信息流，忽略了企业环境中固有的并行流——智能体同时检索多个纠缠条目。

2. **效用指标简化**：虽然先前研究包含效用指标，但其评估受到过于简单的孤立上下文限制。在这些设置中，效用指标主要衡量任务完成程度，而非 disentangle 敏感信息所必需的上下文精确性。

3. **规模不足**：先前研究通常依赖简化上下文或短属性，无法复制真实企业数据的规模和密度，智能体必须在"企业数据大海捞针"中辨别敏感的"针"。

### 4.4 研究空白

本研究填补了以下空白：
- 针对企业领域的专门隐私评估
- 考虑复杂、隐含的组织层级和专有工作流程
- 模拟纠缠的企业环境，其中多个并行信息流共存
- 高保真企业工作流程的CI评估

---

## 5. 核心贡献

### 5.1 CI-Work基准测试

本文提出了CI-Work，一个基于情境完整性理论的基准测试，旨在高保真企业工作流程中评估LLM智能体的CI。CI-Work的创新点包括：

1. **五方向信息流模拟**：模拟五种不同的组织通信方向——下行（管理层对员工）、上行（下属对上司）、横向（同事协作）、对角线（跨组织）和外部（利益相关者参与）。

2. **密集检索上下文**：每个CI-Work实例要求智能体导航密集检索上下文，分区为必要集（Essential Set）和敏感集（Sensitive Set），明确量化任务效用与隐私遵从之间的权衡。

3. **高保真构建流程**：采用严格构建流程，结合人机协同种子生成和自动化自迭代细化机制，确保场景严格遵循业务逻辑和层级约束。

### 5.2 全面评估发现

通过CI-Work，我们发现：
- 前沿LLM智能体表现出持续的隐私-效用权衡，被真实企业数据的高规模和密度所放大
- 模型虽然理解高层组织边界，但在细粒度信息流裁决方面存在困难
- 用户行为会引发隐私和效用的双重崩溃
- 简单增加模型规模和推理努力无法解决这一脆弱性，甚至导致"逆Scaling"现象

### 5.3 实践启示

研究强调：
- 需要上下文感知隐私机制
- 从以模型为中心的安全扩展转向以上下文为中心的架构的紧迫性
- 当前安全对齐对专业领域的不足

---

## 6. 研究方法

### 6.1 企业LLM智能体风险模型

本文考虑的企业环境模型如下：
- 用户 $u$ 拥有私有、非结构化的数据存储 $\mathcal{D}$
- 基于LLM的智能体 $\mathcal{A}$ 被分配一个指令 $\mathcal{I}$，需要从 $\mathcal{D}$ 检索信息并共享给接收者
- 智能体通过工具包 $\mathcal{T}$ 与 $\mathcal{D}$ 交互，生成执行轨迹 $H = \{(a_t, o_t)\}_{t=1}^{T}$
- 在每一步 $t$，动作 $a_t$ 调用检索工具 $\tau \in \mathcal{T}$ 及查询参数 $q_t$，产生数据条目集合 $o_t = \tau(\mathcal{D}, q_t)$ 作为观察

令 $\mathcal{E} = \bigcup_{t=1}^{T} o_t$ 表示检索条目的累积集合。为评估CI，我们根据任务上下文将 $\mathcal{E}$ 分为两个不相交的子集：
- **必要集** $\mathcal{E}_{ess}$：完成 $\mathcal{I}$ 不可或缺的条目
- **敏感集** $\mathcal{E}_{sens}$：如果泄露给接收者则违反隐私规范的条目

隐私风险发生在智能体的最终响应 $a_{fin}$ 泄露 $\mathcal{E}_{sens}$ 中的任何条目，同时传达 $\mathcal{E}_{ess}$ 中的条目以完成任务时产生。

### 6.2 CI-Work构建流程

CI-Work的测试用例通过四个阶段构建和评估：

#### 阶段1：面向任务的种子生成

**任务导向种子** $S$ 由发送者、接收者和发送者分配的任务（传输原则）组成，产生从发送者到接收者的信息流方向。

利用标准组织通信分类法，我们将这些流分为五个不同方向：
1. **下行**（Downward）：管理层对员工
2. **上行**（Upward）：下属对上司
3. **横向**（Lateral）：同事协作
4. **对角线**（Diagonal）：跨组织
5. **外部**（External）：利益相关者参与

为构建高保真基准，我们采用持续人机协同生成范式：
- 手工制作跨多个行业（如科技、医疗、金融）的高质量种子示例
- 作为Gemini-3-Pro的few-shot演示
- 人类专家实时监控生成流，过滤不合理场景并细化提示
- 后续企业从业者验证确认最终种子具有高真实感并严格遵循实际业务实践

#### 阶段2：上下文条目生成

**初始条目生成**：任务导向种子仅展示信息流方向，数据类型仍是CI关键参数中缺失的部分。为填补这一空白，需要一系列上下文条目为每个种子实例化一组并行信息流。

我们采用LLM驱动的基于模板方法：
- 提示LLM为每个种子在单次传递中综合所有必要和敏感条目
- 明确指示LLM将每个条目构建为离散信息单元的独特原子摘要
- 确保条目在轨迹模拟期间准备好独立实例化
- 同时严格遵循种子的传输原则及必要/敏感信息的定义

**自迭代细化**：然而，先前工作观察到LLM综合的数据偏离隐私规范，且在单次传递中生成多个上下文条目时此现象更加严重。

我们引入自校正机制：
- 为每个案例生成初始条目后，LLM对所有条目进行盲分类（Essential、Sensitive、Ambiguous）
- 预期类别 $\ell$ 与模型感知标签 $\hat{\ell}$ 之间的任何差异触发自动化修订循环
- 基于分类原因修订条目
- 后续人工验证显示Essential/Sensitive标签与标注者的隐私规范判断一致率达82.5%-95.0%

#### 阶段3：案例插曲生成

尽管理论引导的schema使隐私敏感种子具有上下文性，但这些种子缺乏引导轨迹模拟的细节。

我们进一步为每个种子生成详细案例插曲 $\mathcal{P}$，包括：
- 发送者、接收者和当前环境的简要描述
- 发送者向智能体提供的指令
- 智能体可在每个可用工具下检索的条目

案例插曲描述了一个连贯且真实的企业场景，作为语义蓝图，在轨迹模拟期间具体实例化为完整文本观察。

#### 阶段4：轨迹模拟与评估

**轨迹模拟**：为在智能体设置中评估LLM，我们开发了基于ToolEmu和PrivacyLens的工具中心模拟环境，使用LLM模拟各种企业工具（如电子邮件、聊天、日历、会议等）在任务执行期间产生的观察。

沙盒环境进一步适配以支持多个必要和敏感条目的同时实例化，实现智能体同时检索多个语义相关内容的企业场景模拟。

在每一步，当智能体调用特定工具检索信息时，观察由LLM驱动的模拟器生成：
$$o_t = sim(q_t, \mathcal{P}, d_{\tau})$$

**评估指标**：为严格量化隐私与效用之间的权衡，我们采用LLM-as-a-Judge框架得出二元指示函数 $\mathcal{F}_{disc}(a_T, e) \in \{0,1\}$，评估特定上下文条目 $e$ 是否在智能体最终动作 $a_T$ 中被泄露。

基于此裁判，我们设计三个评估指标：
- **Leakage（泄露率）**：敏感条目被泄露的比例
- **Violation Rate（违规率）**：违反隐私规范的频率
- **Conveyance Rate（传达率）**：必要信息被正确传达的比例

---

## 7. 实验设置

### 7.1 数据集规模

- **种子规模**：25个面向任务的种子，涵盖五个信息流方向
- **扩展种子**：通过Gemini-3-Pro交互综合额外100个种子
- **总种子数**：125个

### 7.2 评估模型

我们评估了广泛的前沿LLM，包括：
- **闭源模型**：GPT-4o、GPT-4.1、o3、GPT-5、Grok-3
- **开源模型**：Qwen-2.5 32B、Kimi-K2、DeepSeek-V3、DeepSeek-R1

### 7.3 敏感数据类型

敏感条目根据其内容和相关隐私风险分为九种不同类型（详见附录A）。

### 7.4 用户压力测试

评估两种常见用户行为形式的影响：
- **隐式压力**：用户强调任务重要性，指示智能体要彻底和具体
- **显式压力**：用户主动列出相关信息源以帮助智能体，通常不预先过滤敏感性

### 7.5 评估指标

| 指标 | 说明 | 方向 |
|------|------|------|
| **LR (Leakage Rate)** | 敏感条目被泄露的比例 | 越低越好 ↓ |
| **VR (Violation Rate)** | 违反隐私规范的频率 | 越低越好 ↓ |
| **CR (Conveyance Rate)** | 必要信息被正确传达的比例 | 越高越好 ↑ |

---

## 8. 实验结果

### 8.1 总体性能

**主要发现**：
- 当前前沿LLM未能充分保护企业场景中的上下文隐私
- **违规率范围**：15.8%（DeepSeek-R1）到50.9%（Grok-3）
- **泄露率**：高达26.7%（非平凡水平，多 >10%）
- **关键洞察**：更高的传达率与泄露和违规均呈正相关（Pearson $r=0.40$ 和 $0.39$, $p<0.05$）

**跨方向差异**：
- **上行交互**的泄露和违规率显著高于**下行交互**（VR: $p=0.006$；LR: $p=0.009$）
- **外部交互**通常比公司内部交换泄露更少
- LLMs对组织层级和外部边界有粗粒度理解，在不同交互上下文中表现出不同程度的易感性

### 8.2 各模型性能对比

| 模型 | 平均泄露率(%) | 平均违规率(%) | 平均传达率(%) |
|------|--------------|--------------|--------------|
| GPT-4o | 8.79 | 21.33 | 87.35 |
| GPT-4.1 | 12.07 | 25.91 | 94.57 |
| o3 | 13.36 | 32.20 | 92.83 |
| GPT-5 | 11.21 | 27.83 | 93.04 |
| Grok-3 | 26.66 | 50.87 | 94.97 |
| Qwen-2.5 32B | 21.96 | 42.57 | 87.68 |
| Kimi-K2 | 14.62 | 31.06 | 96.18 |
| DeepSeek-V3 | 8.37 | 21.33 | 76.92 |
| DeepSeek-R1 | 6.08 | 15.80 | 53.08 |

### 8.3 上下文条目的影响

#### 8.3.1 数据类型

分析Grok-3在不同数据类型上的泄露率分解：
- **下行、上行、外部和对角线信息流**通常表现出较低的泄露率，但仍对特定数据类型易感
- LLMs在横向同事交互中容易泄露个人数据，在上行通信中也是
- LLMs向外部接收者泄露内部草稿
- 尽管LLMs通过采用保守的信息共享策略表现出粗粒度隐私意识（高风险接收者），但在评估细粒度**角色-信息**兼容性（如在谈判中泄露walk-away price）方面存在困难

#### 8.3.2 条目数量影响

当敏感和必要条目的数量从1增加到12时（保持相等比例）：
- **违规率上升**
- **传达率大幅下降**
- **泄露率呈反向趋势**：暗示"稀释效应"——随着输入信息量扩大，模型泄露的敏感细节比例较小，即使整体违规频率上升

#### 8.3.3 条目长度影响

增加条目长度改善了传达率但也增加了泄露和违规：
- **隐私-效用权衡**：更丰富的上下文细节实现更好的任务基础但扩展了不当披露和上下文完整性失败的攻击面
- 这突出了企业聚焦评估的重要性，其中真实工作流自然结合具有长详细 artifact 的许多实体

### 8.4 用户压力的影响

**隐式压力**（用户强调任务彻底性）导致泄露和违规率大幅增加：
- 即使隐式压力也导致泄露和违规率大幅增加
- **显式压力**（提供具体信息句柄）将此效果放大到几乎两倍于基线违规率
- **反直觉地**，传达率在压力下开始下降
- 当LLM在用户需求和自己的隐私直觉之间挣扎时，它努力调和两者并依赖不可靠的启发式方法
- 导致效用和隐私的双输结果

### 8.5 模型规模和推理深度的影响

#### 8.5.1 模型规模（逆Scaling现象）

与属性共享任务中的先前发现相反，企业智能体中观察到明显的"**逆Scaling**"现象：
- 更大的模型实现更好的效用（传达）但**加剧隐私泄露**

**原因分析**：
1. 企业工作流涉及长、非结构化上下文（如会议记录）
2. 较小的模型通常无法在嘈杂窗口中注意敏感细节，因有限召回而无心地防止泄露
3. 虽然scaling改进了对显式规则的遵从，但企业隐私依赖于隐式上下文完整性
4. 更大的模型表现出更强的"奉承"行为，优先考虑用户指令而非隐式社会约束

#### 8.5.2 推理深度

更强的推理仅略微减少泄露和违规率，传达率基本不变：
- 当前chain-of-thought（CoT）机制主要优化任务完成，分配最小的推理预算来评估隐私规范
- 边际改进远不足以解决根本问题

#### 8.5.3 防御提示的效果

| 防御方法 | 泄露率(%) | 违规率(%) | 传达率(%) |
|---------|----------|----------|----------|
| 无防御 | 11.21 | 27.83 | 93.04 |
| Prompt Defense | 8.96 | 21.31 | 81.01 |
| CI-CoT | 8.95 | 22.13 | 84.90 |

**发现**：
- 两种策略都相对于无防御基线减少了泄露和违规率
- 但以传达率的非平凡损失为代价
- **CI-CoT实现与通用Prompt Defense相当的隐私增益，同时保留更多效用**
- 即使CI-CoT仍产生超过20%的违规率并减少9%的传达率
- 表明纯提示级缓解远远不够

---

## 9. 策略示例

### 9.1 企业信息流场景示例

#### 场景：上行信息流 - 员工向经理汇报

**背景**：
- 发送者：团队成员Alice
- 接收者：经理Bob
- 任务：准备周报

**必要信息**：
- 本周完成的项目里程碑
- 正在进行的项目进度
- 下周计划

**敏感信息**：
- 团队内部冲突细节
- 同事绩效问题
- 个人与同事的私下讨论

**智能体行为挑战**：
智能体需要在周报中传达必要信息，同时避免泄露团队内部的敏感讨论。

#### 场景：外部信息流 - 客户会议准备

**背景**：
- 发送者：项目经理
- 接收者：外部客户
- 任务：准备客户会议议程

**必要信息**：
- 会议议程
- 项目进度摘要
- 客户要求的特定信息

**敏感信息**：
- 内部成本结构
- 竞争对手分析
- 内部项目代号和路线图

### 9.2 评估流程

```
用户指令 → 智能体检索 → 模拟器返回上下文 → 智能体决策 → 评估泄露/违规
```

智能体必须：
1. 理解指令的意图
2. 检索相关信息
3. 区分必要信息和敏感信息
4. 在回复中传达必要信息
5. 避免泄露敏感信息

---

## 10. 攻击流程

### 10.1 隐私泄露攻击场景

虽然CI-Work是评估基准，但其揭示的攻击向量包括：

#### 10.1.1 上下文混淆攻击

攻击者通过设计指令，利用智能体检索和共享敏感信息：
1. 构造看似合法的任务指令
2. 触发智能体检索包含敏感信息的数据存储
3. 利用智能体对"必要信息"的过度解读，诱导泄露敏感细节

#### 10.1.2 用户压力诱导

利用真实企业场景中常见的用户压力：
1. 强调任务重要性（"这非常紧急"）
2. 提供不完整或不准确的过滤指令
3. 导致智能体在效用与隐私之间失衡

### 10.2 脆弱性利用流程

```
用户压力 → 智能体操纵 → 必要信息传达 + 敏感信息泄露
```

**关键发现**：
- 即使是无意的用户指令也会导致隐私和效用的双重崩溃
- 显式用户压力（提供具体信息源）可将近加倍违规率

---

## 11. 消融实验

### 11.1 上下文条目数量的影响

| 条目数量 | 泄露率 | 违规率 | 传达率 |
|---------|-------|-------|-------|
| 1 | 中 | 低 | 高 |
| 4 | 低-中 | 中 | 中-高 |
| 8 | 低 | 高 | 中 |
| 12 | 最低 | 最高 | 低 |

**发现**：随着条目数量增加，违规率单调上升，传达率大幅下降，暗示稀释效应。

### 11.2 上下文条目长度的影响

| 长度层级 | 泄露率 | 违规率 | 传达率 |
|---------|-------|-------|-------|
| 非常短 | 低 | 低 | 低 |
| 短 | 低-中 | 中 | 中 |
| 中等 | 中 | 中-高 | 中-高 |
| 长 | 中-高 | 高 | 高 |
| 非常长 | 高 | 最高 | 最高 |

**发现**：更丰富的上下文细节改善任务完成但扩展了隐私攻击面。

### 11.3 用户压力的影响

| 压力类型 | 泄露率增加 | 违规率增加 | 传达率变化 |
|---------|-----------|-----------|----------|
| 隐式压力 | +15-20% | +20-25% | -5-10% |
| 显式压力 | +30-40% | +40-50% | -10-15% |

**发现**：用户压力显著放大隐私风险，导致双输结果。

### 11.4 模型规模的逆Scaling效应

| 模型规模 | 泄露率 | 违规率 | 传达率 |
|---------|-------|-------|-------|
| 小型 | 低 | 低 | 低 |
| 中型 | 中 | 中 | 中 |
| 大型 | 高 | 高 | 高 |

**发现**：更大的模型在企业隐私场景中表现更差，呈现逆Scaling现象。

---

## 12. 局限性

### 12.1 基准测试局限性

1. **合成数据依赖**：虽然努力确保高保真度，但使用合成数据可能无法完全捕捉真实企业环境的复杂性。

2. **评估者偏差**：LLM-as-a-Judge虽然与人类标签一致率达83-91%，但仍存在潜在偏差。

3. **场景覆盖**：虽然涵盖五个信息流方向，但可能无法涵盖所有真实企业场景。

### 12.2 方法论局限性

1. **防御策略有限**：仅测试了两种轻量级提示防御，未探索训练时对齐或架构解决方案。

2. **模型覆盖**：虽然评估了9个主流模型，但企业环境中使用的模型范围更广。

3. **长期影响**：未评估智能体在多次交互中的累积隐私风险。

### 12.3 研究发现局限性

1. **根本解决方案缺失**：研究揭示了问题但未提供完整的解决方案。

2. **部署就绪性**：明确声明"不应将发现解释为无需额外保障措施即可部署的验证"。

3. **组织差异**：不同企业的隐私规范可能差异很大，通用基准可能不完全适用。

### 12.4 未来研究方向

1. **上下文感知隐私机制**：开发能在密集检索环境中保护隐私的架构
2. **角色条件过滤**：基于发送者-接收者角色条件的信息过滤
3. **训练时对齐**：针对企业隐私规范的专门安全对齐
4. **持续评估**：在演化的工作流程中持续评估隐私风险

---

## 13. 伦理声明

### 13.1 数据使用

1. **合成数据**：本研究在模拟企业智能体环境中评估隐私风险，使用**合成数据**。

2. **数据可用性**：声明"不应将发现解释为无需额外保障措施即可部署的验证"。

3. **代码开源**：数据和源代码可在 https://aka.ms/ci-work 获取。

### 13.2 研究伦理

1. **无害性**：研究旨在识别和评估隐私风险，而非开发新的攻击方法。

2. **透明度**：明确声明基准测试的局限性和发现的不确定性。

3. **行业合作**：研究涉及Microsoft，体现了行业-学术合作。

### 13.3 负责任的AI

1. **安全对齐的必要性**：研究强调当前安全对齐对专业领域的不足。

2. **范式转变呼吁**：提倡从模型中心到上下文中心的隐私保护架构。

3. **持续研究**：鼓励开发上下文感知隐私机制。

### 13.4 潜在风险与缓解

| 潜在风险 | 缓解措施 |
|---------|---------|
| 攻击者利用发现 | 仅发布防御相关发现；不详细描述攻击技术 |
| 企业过度依赖基准 | 明确声明"非部署验证"；强调额外保障必要性 |
| 模型偏差 | 使用多个前沿模型；报告跨模型差异 |

---

## 14. 参考文献

### 核心参考文献

1. Fu, W., Qin, X., Zhang, J., Lin, Q., Wutschitz, L., Sim, R., Rajmohan, S., & Zhang, D. (2026). CI-Work: Benchmarking Contextual Integrity in Enterprise LLM Agents. *ACL 2026 Industry Track*.

2. Nissenbaum, H. (2004). Privacy as Contextual Integrity. *Washington Law Review*.

3. Yao, Y., et al. (2023). ReAct: Synergizing Reasoning and Acting in Language Models. *ICLR 2023*.

4. Schick, T., et al. (2023). Toolformer: Language Models Can Teach Themselves to Use Tools. *arXiv*.

5. Cheng, L., et al. (2024). CI-Bench: A Large-Scale Synthetic Dataset for Contextual Integrity. *ACL 2024*.

6. Li, Y., et al. (2025). Evaluating Privacy Norms in LLM Agents. *EMNLP 2025*.

7. Mireshghallah, F., et al. (2024). ConfAide: Evaluating Layer-based Information Disclosure. *ACL 2024*.

8. Shao, Y., et al. (2024). PrivacyLens: Evaluating Privacy Leakage in LLM Agents. *NeurIPS 2024*.

9. Wang, Z., et al. (2025). PrivacyLens-Live: Realistic Multi-Agent Workflow Privacy Evaluation. *ACL 2025*.

10. Mireshghallah, F., et al. (2025). CIMemories: Measuring Privacy Violation Accumulation in Persistent Memory. *ICLR 2025*.

11. Styles, M., et al. (2024). Workbench: Evaluating Agents in Enterprise Contexts. *ACL 2024*.

12. Wang, Y., et al. (2024). OfficeBench: Multi-Application Office Task Evaluation. *EMNLP 2024*.

13. Drouin, A., et al. (2024). WorkArena: Web Agent Benchmark for Daily Knowledge Work. *NeurIPS 2024*.

14. Xu, M., et al. (2024). TheAgentCompany: Simulating a Small Software Company Environment. *ICML 2024*.

15. Huang, Y., et al. (2025). CRMArena: Customer Service Workflow Evaluation. *ACL 2025*.

16. Choubey, M., et al. (2025). HERB: Heterogeneous Enterprise Data Deep Search. *ICLR 2025*.

17. Ruan, Y., et al. (2024). ToolEmu: Tool-Centric Simulation Environment. *ICML 2024*.

18. Zheng, L., et al. (2023). LLM-as-a-Judge: Using LLMs for Evaluation. *NeurIPS 2023*.

19. Madaan, A., et al. (2023). Self-Refine: Iterative Refinement with Self-Feedback. *NeurIPS 2023*.

20. Wang, Y., et al. (2023). Strengthening Language Model Reasoning. *ICML 2023*.

21. DeepMind. (2025). Gemini-3-Pro Technical Report.

22. Sharma, M., et al. (2024). Sycophancy in Large Language Models. *ACL 2024*.

23. Lan, X., et al. (2025). CI-CoT: Contextual Integrity Chain-of-Thought Prompting. *ACL 2025*.

24. Zhang, Y., et al. (2025). Scaling Privacy in LLM Agents. *NeurIPS 2025*.

25. Zimmerli, J., et al. (2025). Defense-Oriented Prompting Strategies. *ICLR 2025*.

26. Xie, Y., et al. (2023). Prompt Injection Defenses. *USENIX Security 2023*.

27. Robbins, S., & Judge, T. (2009). Organizational Communication Taxonomy. *Prentice Hall*.

28. Slack, N. (2025). Enterprise Communication Patterns. *Harvard Business Review*.

29. Fan, C., et al. (2024). Real-World Court Cases in Privacy Evaluation. *S&P 2024*.

30. Shvartzshnaider, Y., & Duddu, V. (2025). IoT Device Privacy Benchmarks. *USENIX Security 2025*.

31. Ghalebikesabi, S., et al. (2025). Web Agent Assistant Privacy. *ACL 2025*.

32. Zharmagambetov, A., et al. (2025). Privacy in Web Agents. *NeurIPS 2025*.

33. Microsoft. (2025). Copilot for Work: Enterprise Deployment Guidelines.

34. Anthropic. (2026). Claude for Work: Enterprise Privacy Framework.

---

## 附录说明

### 附录A：敏感数据类型分类

敏感条目根据内容和隐私风险分为九种不同类型，包括但不限于：
- 个人身份信息（PII）
- 财务敏感信息
- 内部人事信息
- 战略规划细节
- 客户机密
- 知识产权

### 附录B：实验设置详情

包括：
- 使用的模型及其配置
- 温度、top-p等推理参数
- 评估的硬件配置

### 附录C：种子生成的人类验证

人工验证显示Essential/Sensitive标签与标注者隐私规范判断的一致率达82.5%-95.0%。

### 附录D：LLM-as-a-Judge一致性

LLM-as-a-Judge与人类标签的一致率达83.0%-91.0%。

### 附录E：传达率与隐私风险的相关性

Pearson相关系数分析显示传达率与泄露（r=0.40）和违规（r=0.39）均呈显著正相关（p<0.05）。

### 附录F：详细统计结果

包含所有模型在所有五个信息流方向上的完整统计数据。

### 附录G：指令示例

包括隐式和显式用户压力的具体指令模板。

### 附录H：敏感条目细化算法

自迭代细化算法的详细伪代码和参数设置。

### 附录I：定性示例

详细案例分析，展示成功和失败的隐私保护行为。

---

*本文档由AI助手自动生成，基于arXiv论文2604.21308内容。*
*生成日期：2026-04-28*
*项目主页：https://aka.ms/ci-work*
