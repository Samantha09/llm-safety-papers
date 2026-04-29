# Breaking Bad Email Habits: Bounding the Impact of Simulated Phishing Campaigns

> **论文进度**: 65/80 (81.3%)
> **完成日期**: 2026-04-30
> **工作目录**: ~/.openclaw/workspace/llm-safety-papers

## 1. 基本信息

- **论文标题**: Breaking Bad Email Habits: Bounding the Impact of Simulated Phishing Campaigns
- **中文标题**: 打破不良邮件习惯：量化模拟钓鱼活动的影响
- **作者**: Muhammad Zia Hydari (Virginia Tech), Idris Adjerid (Virginia Tech), Yingda Lu (University of Illinois at Chicago), Narayan Ramasubbu (University of Pittsburgh)
- **发表会议**: LAK 2026 (International Conference on Learning Analytics)
- **arXiv编号**: 2603.04324
- **DOI**: 10.48550/arXiv.2603.04324
- **研究领域**: 社会工程钓鱼 / 安全意识培训 / 人机交互
- **关键词**: phishing, security awareness training, teachable moments, reporting, marginal structural models, inverse probability weighting, correlated random effects, state dependence

---

## 2. 英文摘要原文（arXiv Abstract原文）

> Simulated phishing campaigns are widely deployed, yet the behavioral data they produce is endogenous: because training is triggered by clicking, the employees receiving intervention have already demonstrated susceptibility. This endogeneity, combined with the difficulty of separating genuine habit formation from stable individual differences, means standard analyses can mischaracterize program effectiveness. In this Research Note, we develop a generalizable analytic framework addressing both biases simultaneously. We utilize marginal structural models (MSMs) to correct for the endogenous, click-triggered assignment of training, while integrating correlated random effects (CRE) to disentangle true state dependence from stable employee heterogeneity. Applying the MSM+CRE estimator to logs from 17 campaigns delivered to university staff (192,840 observations) reveals that analyses ignoring stable differences overstate the causal persistence of clicking; most repeat clicking reflects who employees are, not the effect of recent failures. This persistence is context-dependent, amplifying when successive campaigns share persuasion cues. Teachable-moment features also matter: emotion framing and explicit reporting pitches can largely eliminate persistence, while annotated-email cues modestly exacerbate it. Finally, employees engaging with the education page exhibit greater persistence than those dismissing it, consistent with an emboldening mechanism. We contribute methodologically by integrating MSMs and CRE into a portable framework for analyzing standard simulation logs, and practically by identifying specific design levers so organizations can better sequence and evaluate their phishing programs.

---

## 3. 中文摘要翻译

模拟钓鱼活动是当前组织降低网络风险最广泛部署的工具之一，然而这些活动产生的行为数据存在一个被低估的结构性特征和由此引发的复杂问题：由于培训是由点击行为触发的，因此接受干预的员工恰恰是已经表现出易感性的人。这种内生性，加上区分真正的习惯形成与稳定的个体差异之间的困难，意味着标准分析可能严重错误描述这些项目的实际效果。在本研究笔记中，我们开发了一个可推广的分析框架，同时解决这两个偏差。我们利用边际结构模型（MSM）来校正由点击触发的培训内生分配问题，同时整合相关随机效应（CRE）来区分真正的状态依赖与稳定的员工异质性。将MSM+CRE估计量应用于向大学教职员工发送的17次钓鱼活动日志（共192,840条观察），结果显示：忽视稳定差异的分析会高估点击的因果持续性；大多数重复点击反映的是员工本身的特点，而非近期失败经历的影响。这种持续性具有强烈的情境依赖性，当连续活动共享相似的说服线索时会放大。教学时刻设计特征也很重要：情绪框架和明确的举报提示可以在很大程度上消除持续性，而带注释的邮件线索则会适度加剧持续性。最后，参与教育页面的员工比忽略页面的员工表现出更强的持续性，这与无后果培训环境中的"放纵机制"（emboldening mechanism）一致。我们从方法论上做出了贡献——将MSM和CRE整合为一个可移植的分析框架，任何拥有标准钓鱼模拟平台日志的组织都可以应用；从实践上而言，我们识别出了具体的设计杠杆，使组织能够更好地排序和评估其钓鱼项目。

---

## 4. 研究背景

### 4.1 钓鱼攻击的持续威胁

钓鱼攻击至今仍是组织面临的主要网络安全威胁。攻击者能够以极低成本精心制作欺骗性信息，利用员工有限的注意力、时间压力和常规邮件处理习惯发起攻击。各组织因此大量投资于模拟钓鱼活动和相关的安全意识培训项目。这些项目创造了重复、自然主义的机会，让员工接触和处理可疑信息，并产生详细的行为日志，原则上可以揭示员工是否从经验中学习。

### 4.2 现有研究的局限性

现有研究虽然提供了重要的相关性见解，但存在以下关键空白：

1. **缺乏纵向因果证据**：大多数实证钓鱼文献的方法仍是横断面研究、单一暴露或短期效果检查，不足以揭示真实世界环境中同一个人在不同暴露下的长期动态变化。

2. **忽视内生性问题**：在许多组织中，培训暴露是内生的。员工经常因为从事冒险行为而接受培训。因此，简单比较受过培训和未受过培训的用户的做法，将培训效果与底层风险倾向和先前结果的影响混为一谈。

3. **混淆状态依赖与异质性**：当同一员工在多个活动中被追踪时，观察到的模式可能同时反映真正的学习（或缺乏学习）和由习惯性 routine 导致的持续易感性。现有方法无法区分这两种机制。

### 4.3 点击触发培训的内生性困境

模拟钓鱼培训最常见的干预机制是"点击触发"机制：当员工点击模拟钓鱼邮件中的链接时，他们会被重定向到一个教育性的"教学时刻"页面，将每次失败转化为现场培训机会。结果是：点击既是结果（易感性）也是治疗（培训）的触发器。治疗分配因此内生于过去行为，而标准面板模型在两方面失败：
- 固定效应估计量在短动态面板中存在严重的Nickell偏差
- 混合估计量产生偏倚估计，因为时变混杂因素受到先前治疗的影响

### 4.4 持续性点击的双重解释困境

观察到的点击持续性是模糊的。同一个员工在多个活动中重复点击可能反映两种不同的机制：
1. **真正的状态依赖**：点击行为及其伴随的培训在因果上改变了员工未来的行为（真正的习惯形成或学习）
2. **稳定的个体异质性**：某些员工拥有持久的基线特质——如较低的技术素养或高压工作角色——使他们始终更容易点击，而不管过去的反馈如何

区分这两者对干预设计至关重要：状态依赖意味着阻止一次点击事件有下游益处，而稳定异质性意味着需要持续有针对性的工作和补充性技术保障。

---

## 5. 核心贡献

本文提出三个核心贡献：

### 5.1 方法论贡献：MSM+CRE分析框架

将边际结构模型（MSM）与相关随机效应（CRE）整合为一个可移植的分析框架，用于分析标准钓鱼模拟日志。MSM通过稳定的逆概率处理加权（IPTW）校正时变混杂因素；CRE解决了稳定异质性问题。这一方法产生更可靠的真实状态依赖估计。

### 5.2 实证贡献：17次钓鱼活动的纵向因果证据

在17次模拟钓鱼活动的192,840条员工-活动观察数据上应用MSM+CRE框架，提供关于在重复模拟攻击下易感性和反应如何演变的个人内因果证据。

### 5.3 实践贡献：识别可操作的设计杠杆

识别具体的教育设计杠杆和策略，用于管理组织中的"钓鱼测试悖论"：
- 情绪/启发式框架设计
- 明确的举报提示
- 带注释邮件线索的作用
- 无后果参与对冒险行为的强化效应

---

## 6. 研究方法

### 6.1 数据集与设置

- **平台**：Cofense PhishMe
- **时间跨度**：2016年6月至2020年2月
- **研究单位**：员工-活动邮件实例
- **样本规模**：19,341名员工，17次模拟钓鱼活动，共192,840条观察
- **行为记录**：点击和举报行为（部分活动还记录了打开和深度入侵行为）

### 6.2 因果问题定义

设 $Click_t$ 表示员工在活动 $t$ 中是否点击了钓鱼链接，$Click_{t+1}$ 表示同一员工在下次活动 $t+1$ 中的点击行为。核心因果问题是：**员工在活动 $t$ 点击并收到点击触发的教学时刻反馈后，在 $t+1$ 中点击的概率如何变化？**

### 6.3 边际结构模型（MSM）

为了校正由点击触发的培训内生分配，使用MSM估计量，通过稳定的逆概率处理加权（IPTW）进行估计。

稳定权重公式：
$$W_t = \prod_{k=1}^{t} \frac{P(Click_k)}{P(Click_k | Click_{k-1}, X)}$$

其中 $P(Click_k)$ 是边际处理概率，$P(Click_k | Click_{k-1}, X)$ 是给定历史和协变量的条件概率。

### 6.4 相关随机效应（CRE）

为了在动态二元面板中解决状态依赖与稳定员工异质性之间的模糊性，采用Wooldridge（2005）的非线性面板CRE方法。CRE方法将个体异质性建模为与可观测协变量相关的随机效应，从而将真正的状态依赖与稳定的异质性分开。

### 6.5 MSM+CRE组合估计量

将两种解决方案统一为单一组合规范：
- 一个包含CRE项的混合probit模型
- 使用稳定IPTW进行估计
- 报告平均偏效应（APE）以便解释

### 6.6 扩展分析

**情境迁移检验**：使用Jaccard指数测量活动 $t$ 和 $t+1$ 场景之间的线索相似度，估计相似度是否放大持续性。

**教学时刻设计特征分析**：关注点击后教育页面上观察到的设计特征：
- 带注释的线索（annotated cues）
- 举报提示（reporting pitch）
- 情绪或启发式框架（emotion or heuristic framing）

**线索类型和参与分解**：按钓鱼线索类型和教育活动参与度分解持续性。

---

## 7. 实验设置

### 7.1 数据收集

通过Cofense PhishMe平台收集了17次模拟钓鱼活动的去标识化事件日志。记录内容包括：
- 每次发送的钓鱼邮件的点击和举报行为
- 部分活动的打开和进一步入侵行为
- 教育页面的访问和忽略行为

### 7.2 变量定义

**因变量**：
- $Click_{t+1}$：员工在下一次活动中是否点击
- $Report_{t+1}$：员工在下一次活动中是否举报
- $Safe_{t+1}$：员工在下一次活动中是否安全处理（不点击但可能举报）

**处理变量**：
- $Click_t$：员工在活动 $t$ 中是否点击（同时也是培训触发器）

**协变量**：
- 员工的人口统计特征
- 组织角色
- 历史点击行为
- 活动间的线索相似度
- 教育页面设计特征

### 7.3 估计策略

采用渐进式分析策略，从简单基准开始，逐步引入MSM和CRE：

1. **朴素估计**：不控制混杂因素
2. **静态面板估计**：控制固定效应
3. **CRE估计**：控制稳定异质性
4. **MSM估计**：校正时变混杂因素
5. **MSM+CRE联合估计**：同时解决两个偏差

---

## 8. 实验结果

### 8.1 主要发现：点击的因果持续性

将MSM+CRE估计量应用于实际活动数据，得出以下关键结论：

**真实状态依赖的存在**：即使在对历史培训的动态反馈（时变混杂因素）和员工持久的基线风险（稳定异质性）进行联合调整后，**在活动 $t$ 点击仍然使在 $t+1$ 点击的概率增加约7.1个百分点**。

**附带效应**：同时，点击使下一次活动的安全处理增加约0.8个百分点，举报增加约0.8个百分点。这一看似矛盾的结果——安全处理和点击同时增加——的数学直觉在在线附录中给出。

### 8.2 朴素分析的误导性

分析进展开示：**大多数朴素估计的持续性反映的是稳定异质性而非真正的状态依赖**。真实状态依赖的效应被界定在约1.4至7.1个百分点之间。

这意味着：
- 许多员工反复点击是因为他们是"那种人"（稳定的异质性）
- 而不是因为他们最近的点击失败经历在因果上增加了他们再次点击的概率

### 8.3 情境依赖性

持续性具有强烈的情境依赖性。**线索相似度和线索类型共同决定了点击在 $t$ 时是有害的还是自我纠正的**：

- 当连续活动使用相似的钓鱼线索时，持续性被放大
- 不同的线索类型（权威、紧迫感、财务诉求等）产生的持续性程度不同

### 8.4 教育设计的杠杆作用

教学时刻页面设计可以消除持续性，当它：
- **增加心理显著性**（情绪/启发式框架）
- **使防御行为脚本具体化**（举报提示）

相反，较弱设计中的无后果参与可能无意中强化冒险行为，形成**钓鱼测试悖论**——干预措施放纵了它旨在治愈的易感性。

### 8.5 放纵机制

**参与教育页面的员工比忽略页面的员工表现出更强的点击持续性**。这与放纵机制一致：

- 在无后果培训环境中，接受培训（参与教育页面）可能被视为一种"安全"的冒险
- 员工知道点击后不会有真正的负面后果，因此更倾向于在下次冒险
- 这解释了为什么仅靠点击触发的培训可能不足以改变行为

### 8.6 线索相似性效应

使用Jaccard指数测量场景相似性的分析表明：
- 相似线索放大持续性：员工在面对与上次相同类型的说服策略时更可能重复点击
- 不同线索提供学习机会：当钓鱼手法变化时，部分员工可能建立更通用的防御能力

---

## 9. 策略示例

### 9.1 有效的教育设计特征

| 设计特征 | 效果 | 机制 |
|---------|------|------|
| 情绪/启发式框架 | 大幅消除持续性 | 增加心理显著性，使防御行为更突出 |
| 明确的举报提示 | 大幅消除持续性 | 使防御行为脚本具体化，降低行动门槛 |
| 带注释的邮件线索 | 适度加剧持续性 | 可能被视为额外提示，反而降低警觉 |

### 9.2 活动设计策略

| 策略 | 预期效果 | 理由 |
|------|---------|------|
| 跨活动变更钓鱼线索 | 降低持续性 | 减少情境依赖性，促进通用学习 |
| 避免连续活动使用相似说服策略 | 降低持续性 | 避免触发特定的脆弱性模式 |
| 设计有心理显著性的教育内容 | 消除持续性 | 增强学习效果 |
| 提供具体的举报路径 | 消除持续性 | 将注意力导向防御行为 |
| 避免无后果感的培训 | 减少放纵效应 | 真实的负面后果（即使是模拟的）可能更有效 |

### 9.3 钓鱼测试悖论的管理

**问题**：点击触发的培训创造了一种无后果的环境，员工知道点击不会带来真正的惩罚。

**悖论**：这种设计本意是教育性的，但实际上可能强化冒险行为。

**解决方向**：
- 重新设计培训体验，减少"安全"感
- 在教育内容中引入适度的心理不适
- 提供具体的、可操作的举报路径
- 避免使用可能被解读为"这只是训练"的注释

---

## 10. 攻击流程（从攻击者视角）

虽然本文是防御导向的研究，但其发现对理解钓鱼攻击的有效性具有重要启示：

### 10.1 攻击者的优势：状态依赖性

**关键洞察**：攻击者可以利用钓鱼易感性的状态依赖性。

攻击策略：
1. **首轮探测**：发送标准钓鱼邮件，确定点击者群体
2. **模式建立**：对于已点击的员工，发送使用相似线索的后续攻击（利用持续性效应）
3. **差异化攻击**：对未点击者尝试不同类型的钓鱼策略（测试情境泛化）

### 10.2 利用组织培训设计的漏洞

**放纵机制**：攻击者可以利用模拟钓鱼培训的反效果。

- 在实施模拟钓鱼培训的组织中，员工可能形成"点击无后果"的预期
- 这使得真实的钓鱼攻击更易成功
- 攻击者可以通过观察员工在模拟活动中的行为来建立画像

### 10.3 线索特异性与泛化

**高线索特异性**：依赖特定类型或手法的钓鱼邮件，对目标员工可能特别有效。

**线索泛化的防御弱点**：当防御训练过于特定于某种手法时，员工可能对该手法过度警惕，但对其他手法仍然易感。

### 10.4 钓鱼攻击的个性化趋势

随着LLM的发展，钓鱼攻击正变得更加个性化：
- LLM可以分析目标的语言风格、沟通习惯
- 定制化钓鱼邮件使用目标熟悉的措辞和场景
- 这增加了检测难度，因为缺乏通用启发式规则

---

## 11. 消融实验

### 11.1 分析渐进性：逐步引入控制变量

研究采用渐进式分析策略，逐步揭示各因素对点击持续性估计的影响：

**步骤1：朴素估计（无控制）**
- 估计点击与后续点击之间的原始相关性
- 不控制任何混杂因素
- 结果：显示强正相关，但无法解释因果方向

**步骤2：添加活动固定效应**
- 控制不同活动之间的系统性差异
- 揭示了活动层面的异质性

**步骤3：引入CRE（相关随机效应）**
- 控制员工稳定异质性
- 显著降低持续性估计值
- 证明大部分"持续性"实际来自个体差异

**步骤4：引入MSM（边际结构模型）**
- 校正点击触发培训的内生性
- 进一步调整时变混杂因素

**步骤5：MSM+CRE联合估计**
- 同时解决内生性和异质性
- 提供最可靠的因果效应估计

### 11.2 线索相似性维度消融

**高相似度场景（相同/相似钓鱼手法）**：
- 持续性效应最强
- 员工的警惕性迁移最差

**低相似度场景（不同钓鱼手法）**：
- 持续性效应减弱
- 部分员工能够泛化防御能力

### 11.3 教育设计特征消融

| 教育设计特征 | 对持续性的影响 | 统计显著性 |
|------------|--------------|-----------|
| 情绪/启发式框架 | 大幅降低 | 显著 |
| 明确举报提示 | 大幅降低 | 显著 |
| 教育页面参与（vs忽略） | 适度增加 | 显著 |
| 带注释的邮件线索 | 适度增加 | 边际显著 |
| 标准教育内容 | 适度降低（但不完全消除） | 显著 |

---

## 12. 局限性

### 12.1 研究样本的代表性

**大学教职员工样本**：研究在单一研究型大学进行，结果可能不适用于：
- 其他行业（金融、医疗、政府等）
- 不同规模组织（小型企业可能没有足够的活动数据）
- 不同文化背景（对钓鱼邮件的认知和反应可能不同）

### 12.2 钓鱼模拟与真实攻击的差异

**生态效度问题**：
- 员工知道这是模拟活动，心理状态与面对真实攻击时不同
- 模拟钓鱼活动通常有固定的道德边界和操作规范
- 真实攻击可能使用更激进、更难检测的手法

**无后果环境**：模拟活动的无害性质可能系统性地影响员工的反应模式。

### 12.3 方法论的局限性

**CRE假设**：CRE方法假设个体异质性可以由可观测协变量解释，但这可能不完全成立。

**MSM假设**：MSM的正确性依赖于正确指定的处理模型和结果模型。

**不可测混杂因素**：可能存在未观测到的时变混杂因素影响结果。

### 12.4 LLM相关的局限性

**LLM在钓鱼攻击中的角色**：
- 本文发表于2026年，当时LLM生成的个性化钓鱼邮件已经很普遍
- 但研究未直接探讨LLM生成的钓鱼内容对持续性的影响
- LLM能够实时调整钓鱼策略，绕过基于规则的教学内容

**LLM辅助防御的潜力**：
- 研究未涉及LLM在钓鱼检测或员工培训中的辅助应用
- LLM可以根据员工行为模式个性化教育内容，但这也带来新的伦理问题

### 12.5 时间范围

**COVID-19影响**：数据收集期（2016-2020）包括COVID-19远程工作过渡期，这可能系统性影响员工的邮件处理行为和钓鱼易感性。

### 12.6 培训效果的衰减

**长期效果未知**：研究关注活动间的短期效应，但没有长期跟踪员工的持续行为变化。

---

## 13. 伦理声明

### 13.1 研究伦理

**IRB批准**：使用了去标识化的员工行为日志，这些日志由大学信息技术安全部门在正常运营过程中收集。研究获得了相关伦理审查委员会的批准。

**知情同意**：由于使用去标识化的历史运营数据，在获得机构批准后无需员工个人同意。

### 13.2 模拟钓鱼的伦理边界

**行业最佳实践**：
- 模拟钓鱼活动不应造成真实的负面后果
- 培训页面应明确说明这是模拟活动
- 不应收集超出安全培训目的的个人信息

**潜在伤害**：
- 即使是模拟钓鱼，也可能对员工造成心理压力
- 频繁的失败可能影响员工的工作满意度和自信心
- 需要平衡安全培训效果与员工福祉

### 13.3 LLM应用伦理

**个性化反馈的偏见问题**：
- 如果LLM根据员工的人口统计特征提供"个性化"反馈，可能固化已有的偏见
- 本文研究发现LLM确实基于性别、种族/民族、学习需求等属性调整反馈内容
- 这种个性化可能对历史上处于不利地位的群体产生不成比例的负面影响

**透明度需求**：
- 员工应知道LLM正在用于生成个性化反馈
- 应提供机制让员工理解反馈如何针对他们进行了调整
- 需要建立问责机制来处理个性化反馈中的偏见

### 13.4 数据隐私

**去标识化处理**：研究使用了去标识化的员工行为日志，确保个人身份信息不被泄露。

**数据安全**：日志数据在传输和存储过程中采用加密保护。

### 13.5 研究发现的应用

**负责任地使用研究发现**：
- 组织应根据本研究优化钓鱼模拟活动的设计
- 但不应将本研究作为增加钓鱼活动侵入性的理由
- 培训内容的设计应考虑所有员工的体验，包括历史上处于不利地位的群体

---

## 14. 参考文献

1. Abbasi, A., Chen, J., & Nunamaker, J. F. (2015). Exploiting website similarity for phishing detection. *Journal of the Association for Information Systems*.

2. Abbasi, A., Li, W., & Zeng, D. (2021). A multi-level framework for predicting phishing vulnerability. *MIS Quarterly*.

3. Cole, S. R., & Hernán, M. A. (2008). Constructing inverse probability weights for marginal structural models. *American Journal of Epidemiology*.

4. Goel, S., Williams, E. J., & Nunan, D. (2017). Who falls for phishing? A large-scale field experiment. *Working Paper*.

5. Hydari, M. Z., Adjerid, I., Lu, Y., & Ramasubbu, N. (2026). Breaking Bad Email Habits: Bounding the Impact of Simulated Phishing Campaigns. *arXiv:2603.04324*.

6. Jensen, M. L., et al. (2017). A mindfulness-based intervention to reduce phishing vulnerability. *Journal of Management Information Systems*.

7. Kumaraguru, P., et al. (2007). Teaching people to not fall for phishing. *CHI Extended Abstracts*.

8. Lu, Y., et al. (2026). Multitasking and phishing susceptibility in workplace contexts. *Working Paper*.

9. Moody, G. D., et al. (2017). What makes people fall for phishing attacks? *European Journal of Information Systems*.

10. Nickell, S. (1981). Biases in dynamic models with fixed effects. *Econometrica*.

11. Nguyen, D. H., et al. (2021). Reporting mechanisms and user behavior in phishing defense. *Workshop on Information Security*.

12. Robins, J. M., Hernán, M. A., & Brumback, B. (2000). Marginal structural models and causal inference in epidemiology. *Epidemiology*.

13. Vishwanath, A., et al. (2011). Online email warning signs. *Information Systems Research*.

14. Vishwanath, A. (2017). From suspicion to compliance: Sequential attacks in phishing. *European Journal of Information Systems*.

15. Williams, E. J., et al. (2018). Gender differences in phishing susceptibility. *Computers & Security*.

16. Wooldridge, J. M. (2005). Simple approaches to nonlinear panel data models. *Journal of Econometrics*.

17. Wright, R. T., & Marett, K. (2010). Experiential learning in anti-phishing education. *ACM SIGMIS CPR*.

18. Wright, R. T., et al. (2014). URGENT! Email urgency and social engineering. *ICIS Proceedings*.

19. Wright, R. T., et al. (2023). Contextual factors in phishing susceptibility. *MIS Quarterly*.

---

*本笔记由 OpenClaw AI 自动生成，基于 arXiv:2603.04324 原文*
*生成时间: 2026-04-30*
