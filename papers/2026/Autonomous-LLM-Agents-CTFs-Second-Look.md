# Autonomous LLM Agents & CTFs: A Second Look

## 1. 基本信息

| 项目 | 内容 |
|------|------|
| **论文标题** | Autonomous LLM Agents & CTFs: A Second Look |
| **作者** | Idilio Drago (Università di Torino), Thanh Minh Bui, Dario Rossi (Huawei Technologies France) |
| **会议** | EuroS&P 2026 (DeMeSSAI Workshop) |
| **等级** | CCF-B |
| **方向** | Agent Security / CTF |
| **arXiv** | [2605.21497](https://arxiv.org/abs/2605.21497) |
| **GitHub** | [SmartData-Polito/CTF_agent](https://github.com/SmartData-Polito/CTF_agent) |

---

## 2. 英文摘要原文（arXiv abstract原文）

> Large Language Model (LLM) agents are increasingly proposed to automate offensive security tasks, with recent studies reporting near human-level success rates in Capture-the-Flag (CTF) challenges. We here revisit these results, providing a second look at these claims. We engineer different agent architectures of increasing complexity and modularity on 30 web-based CTFs challenges spanning 14 vulnerability classes. We instantiate these agents with multiple LLM backbones, and compare them with claude-code, a general-purpose agent that automatically determines its internal architecture. Our evaluation yields three main findings. First, claude-code achieves performance comparable to the engineered architectures (19/30 solved tasks), suggesting that general-purpose agents are strong baselines for offensive security tasks. Second, both our architectures and claude-code struggle in the same challenge categories, revealing persistent barriers that keep current agents below human-level capability. Third, by leveraging our manually designed architectures we can systematically measure the impact of additional components, finding that structured orchestration of specialized roles outperforms monolithic designs, improving run-to-run consistency, and reducing execution costs.

---

## 3. 中文摘要翻译

大型语言模型（LLM）智能体正越来越多地被用于自动化攻击性安全任务，近期研究甚至报告其在夺旗（CTF）挑战中达到了接近人类水平的成功率。本文重新审视了这些研究成果，对相关声明进行了二次验证。我们在30个涵盖14个漏洞类别的Web CTF挑战上，设计并评估了复杂度递增、模块化程度不断提高的多种智能体架构。我们使用多种LLM后端实例化这些智能体，并与 claude-code（一种能够自动确定其内部架构的通用智能体）进行比较。我们的评估得出了三个主要发现：第一，claude-code取得了与精心设计的架构相当的表现（解决了19/30个任务），表明通用型智能体是攻击性安全任务的强基线。第二，我们的架构和 claude-code 在相同的挑战类别中都遇到了困难，揭示了当前智能体仍低于人类能力水平的持久性障碍。第三，通过利用我们手动设计的架构，我们能够系统性地衡量额外组件的影响，发现专门角色的结构化编排优于单体设计，提高了运行间一致性并降低了执行成本。

---

## 4. 研究背景

### 4.1 渗透测试的重要性与挑战

渗透测试（Penetration Testing）是一种系统性安全评估，用于识别和利用目标系统中的漏洞。尽管渗透测试对主动网络防御至关重要，但其自动化仍然困难重重。目前，全球网络安全人才缺口近480万人，而攻击者往往在CVE公布后15分钟内就开始利用新披露的漏洞。这凸显了自动化渗透测试的迫切需求。

### 4.2 LLM在渗透测试中的潜力

大型语言模型是自动化此过程的理想候选者，因为它们具备漏洞类别、攻击技术和安全工具的知识。然而，攻击性安全需要多步骤规划、自适应工具使用和长交互过程中的连贯上下文管理——这些都是当前基于LLM的智能体刚刚开始展示的能力。

早期工作表明，LLM可以协助渗透测试人员进行工具调用、输出解释和行动规划。多智能体架构——即中央规划器协调专门化子智能体——随后在网络和Web应用程序设置中优于单体方法。专用基准测试现在标准化了评估，涵盖了CTF风格套件和沙盒化真实世界CVE，智能体系统报告了接近人类的成功率。然而，许多方法仍然不公开源代码或评估代理任务（如漏洞识别）而非完整漏洞利用。

### 4.3 研究动机

本文对基于LLM的多智能体系统在攻击性安全方面的当前潜力进行了现实核查。具体研究问题包括：
- 先前声称能否得到证实？
- LLM智能体仍在哪些方面存在困难？
- 手工制作的多智能体架构是否比通用智能体工具提供实际优势？

研究聚焦于Web应用程序渗透测试（占近44%的安全事件），并使用基于Web的CTF挑战作为真实攻击场景的安全和可重现代理。

---

## 5. 核心贡献

### 5.1 三个主要发现

1. **通用智能体是强基线**：claude-code取得了与精心设计的工程架构相当的表现（均解决19/30个挑战），表明通用型智能体是攻击性安全任务的强基线。

2. **持久性能力障碍**：我们的架构和claude-code都在相同的挑战类别中遇到困难，包括业务逻辑缺陷、竞争条件攻击和盲SQL注入，揭示了当前智能体仍低于人类能力水平的持久性障碍。

3. **结构化编排的优势**：通过手工设计的架构系统性地衡量了架构组件的影响，发现专门角色的结构化编排优于单体设计，提高了运行间一致性并降低了执行成本。

### 5.2 设计的智能体架构

研究设计了三种领域特定的智能体架构：
- **Executor (E)**：单体执行器
- **Executor + Evaluator (E+E)**：增加评估器的多智能体架构
- **Planner + Executor + Evaluator (P+E+E)**：完整的三层结构化架构

### 5.3 可复现性贡献

研究公开发布了智能体实现和挑战痕迹（GitHub仓库），以促进可复现性和未来研究。

---

## 6. 研究方法

### 6.1 智能体设计的共同特性

所有智能体共享以下组件：

**Prompt设计**：
- 定义智能体角色为"CTF专家"
- 任务定义为"识别漏洞并获取旗帜"
- 提供可用工具说明
- 一般指导（"系统且脚踏实地"）
- 操作约束（"不要浏览主机文件系统"）
- 退出条件：成功时输出"FLAG {...}"；放弃时输出"GIVE_UP"

**工具**：
- `run_command`：直接运行任意bash命令
- `run_python`：创建并运行Python脚本
- 要求模型将工具调用与其内部思考过程配对解释

**记忆管理**：
- 通过将推理痕迹、工具调用和相应输出附加到草稿本来跟踪先前步骤
- 如果内容过长，要求智能体总结先前发现以产生更简洁的报告

### 6.2 三种领域特定架构

**Executor (E)**：
- 最简单的配置
- 单体智能体负责发现漏洞环境、制定利用计划并执行
- 研究表明这种设计倾向于使智能体过度负担，导致性能下降

**Executor + Evaluator (E+E)**：
- 多智能体架构
- 评估器以"LLM-as-a-judge"模式运行，在执行前对执行器的推理进行评分
- 如果评分低，评估器阻止执行并建议重试
- **局限性**：评估器经常在没有足够上下文的情况下做出判断——它单独评估每个动作，无法看到完整执行跟踪，因此无法可靠地确定整体执行逻辑是否连贯一致

**Planner + Executor + Evaluator (P+E+E)**：
- 引入Planner，由侦察节点支持
- Planner首先探索环境并制定计划
- 计划随后提供给执行器和评估器
- **优势**：(i) 将规划与执行解耦，简化执行器任务；(ii) 为评估器提供结构化参考，使其在接受或拒绝动作时能够做出更明智的决策

### 6.3 通用智能体基线：claude-code

作为外部基线，研究评估了claude-code：
- 一种自导向编码智能体，自主确定如何处理任务
- 通过原始工具集（bash、read、write、edit）与环境交互
- 支持自主多智能体实例化——主智能体可以自主生成子智能体
- 使用原生工具使用框架和内部记忆机制

### 6.4 基准测试数据集

使用XBOW基准测试的30个挑战子集：
- XBOW是Web CTF任务策划集合，旨在评估自动化漏洞检测和利用系统
- 挑战涵盖14个漏洞类别和多种难度级别
- 每个挑战由隔离的Docker镜像组成，实例化一个漏洞Web应用程序
- 智能体仅获得相应URL作为入口点

---

## 7. 实验设置

### 7.1 模型配置

使用GPT-4.1和GPT-5通过OpenAI API实例化架构；对于基线，直接通过claude-code的本地安装使用最佳Claude模型Opus 4.5。

### 7.2 运行配置

- 每个架构每个任务执行3次（90次运行/架构）
- claude-code每个任务执行1次（30次运行）
- 所有运行独立执行，执行间不共享内存
- 每个运行最多50次迭代
- 评估器每个动作最多中断执行器3次

### 7.3 评估指标

- **Success/Failure**：二元指标，表示是否成功解决基准
- **Steps**：完成任务所需的交互步骤数（不计算评估器调用）
- **Cost**：每个挑战的平均成本（美元）
- **Duration**：每次运行的墙上执行时间
- **Consistency**：跨独立执行解决相同挑战的可靠性

---

## 8. 实验结果

### 8.1 总体基准分析

| 模型/配置 | 成功率 | 平均步数 | 平均成本 | 平均时长 |
|-----------|--------|----------|----------|----------|
| GPT-4.1 | 9/30 | - | - | - |
| GPT-5 (E) | 19/30 | 31.56 | - | - |
| GPT-5 (E+E) | 19/30 | 28.76 | - | - |
| GPT-5 (P+E+E) | 19/30 | 24.09 | - | - |
| claude-code | 19/30 | - | - | - |

**关键发现**：
1. **LLM起决定性作用**：使用GPT-4.1，智能体仅解决9/30任务，而GPT-5达到19/30，巨大差距表明复杂多步CTF挑战需要更强的推理和规划能力。

2. **所有更强系统在19/30 CTF上成功**：远低于先前工作报告的结果（先前工作缺乏可验证的复现制品）。

3. **效率揭示架构趋势**：在GPT-5变体中，增加结构化组织逐步减少了平均交互步骤数（31.56 → 28.76 → 24.09），直接导致更低的平均成本，使Planner-Executor-Evaluator配置成为最成本高效的设计。

4. **时钟持续时间模式不同**：虽然完全结构化架构提高了步数和成本效率，但引入了运行时开销——因为规划器和评估器在每次执行时都会实例化。claude-code几乎不生成额外智能体，主要依赖read和bash工具，使其运行时与裸执行器大致相当。

### 8.2 一致性分析

更复杂的架构提高了跨运行的整体一致性。GPT-5变体的结果：
- 裸执行器一致性最低
- E+E架构提高了步级效率，但评估器无法看到完整轨迹
- P+E+E架构达到最高一致性

### 8.3 失败分析

失败一致地集中在同一组任务上：
- **业务逻辑缺陷**：需要理解应用程序的领域特定规则
- **竞争条件攻击**：需要精确的时序操作
- **盲SQL注入**：需要长期的迭代推理和观察

**技术障碍**：缺乏对长期依赖和精确时序的理解

**语义障碍**：无法可靠地将漏洞利用概念转化为具体行动

---

## 9. 策略示例

### 9.1 智能体协作模式

**单体架构（E）**的问题：
- 频繁产生局部可信的行动但缺乏全局计划
- 容易陷入振荡行为
- 在复杂多步挑战中迅速失去方向

**结构化多智能体架构（P+E+E）**的优势：
- Planner首先生成高级攻击计划
- Executor按照计划执行，不进行迭代重新规划
- 评估器基于结构化参考做出决策

### 9.2 工具使用策略

智能体通过SSH终端与环境交互：
- `run_command`：用于简单探索和检查
- `run_python`：用于结构化程序
- 所有工具调用都配有解释内部思考过程的文本

### 9.3 记忆压缩策略

当草稿本变得过长时，智能体被要求总结先前发现以产生更简洁的报告，解决LLM有限上下文窗口的限制。

---

## 10. 攻击流程

### 10.1 CTF挑战的标准攻击流程

1. **环境发现**：访问目标URL，识别运行的服务
2. **侦察**：端口扫描、目录枚举、漏洞扫描
3. **漏洞识别**：识别潜在漏洞类型（如SQL注入、XSS等）
4. **利用开发**：根据识别的漏洞开发针对性强利用代码
5. **权限提升**（如需要）：获取更高权限
6. **旗帜获取**：提取CTF旗帜

### 10.2 智能体执行流程

```
输入: 目标URL
while not 终止条件:
    1. Planner: 侦察环境 → 分类漏洞类型 → 制定攻击计划
    2. Executor: 基于计划执行行动
    3. Evaluator: 评估行动是否合理 → 批准或拒绝
    4. 如被拒绝 → Executor重试（最多3次）
    5. 观察结果 → 更新内部状态
    6. 如获取旗帜 → 输出 FLAG{...} → 终止
    7. 如确定无法解决 → 输出 GIVE_UP → 终止
```

### 10.3 失败案例分析

**业务逻辑缺陷挑战**：
- 智能体无法理解应用程序的特定业务规则
- 无法识别违反业务逻辑的漏洞
- **根本原因**：缺乏领域特定知识和常识推理

**竞争条件攻击**：
- 需要精确的时序操作
- 智能体在多步骤时序推理上表现不佳
- **根本原因**：缺乏对长期依赖和精确时序的理解

**盲SQL注入**：
- 需要长期的迭代推理和条件观察
- 智能体容易在长期探索中迷失方向
- **根本原因**：短视的决策策略和有限的记忆压缩能力

---

## 11. 消融实验

### 11.1 LLM后端的影响

| 后端 | 成功率 | 观察 |
|------|--------|------|
| GPT-4.1 | 9/30 | 明显较弱 |
| GPT-5 | 19/30 | 显著提升 |

**结论**：复杂多步CTF挑战需要更强的推理和规划能力，只有最新一代LLM才能提供。

### 11.2 架构组件的影响

**E → E+E的改进**：
- 评估器提供步级反馈
- 改善了步级效率
- 但评估器仅能看到局部上下文，无法评估整体连贯性

**E+E → P+E+E的改进**：
- 引入Planner后，规划与执行解耦
- 评估器获得结构化参考
- 步数减少约24%（31.56 → 24.09）
- 运行间一致性显著提高
- 降低了执行成本

### 11.3 claude-code vs 结构化架构

| 指标 | claude-code | P+E+E |
|------|-------------|-------|
| 成功率 | 19/30 | 19/30 |
| 解决任务集 | 相同 | 相同 |
| 步数/成本 | 较低 | 较低（效率更高） |
| 运行间一致性 | 较低 | 较高 |
| 执行时间 | 较短 | 较长（额外开销） |

**发现**：claude-code和精心设计的架构在可解决问题集上表现相当，但P+E+E更高效（更少步骤、更低成本），同时提供更高一致性。

### 11.4 组件贡献总结

| 组件 | 贡献 |
|------|------|
| Evaluator | 步级效率改进，但无法评估全局连贯性 |
| Planner | 简化Executor任务，提供结构化参考，实现约24%步数减少 |
| 记忆压缩 | 解决上下文窗口限制，支持长期任务 |

---

## 12. 局限性

### 12.1 方法论局限

1. **claude-code仅运行一次**：由于token消耗限制，claude-code每个任务仅执行一次，而其他架构执行三次，这可能影响比较的公平性。

2. **挑战选择**：使用XBOW的子集，可能无法完全代表真实世界渗透测试的复杂性。

3. **代理任务限制**：CTF挑战虽是安全评估的有用代理，但不能完全反映真实渗透测试的所有方面。

### 12.2 技术局限

1. **上下文窗口限制**：尽管使用记忆压缩策略，有限的上下文窗口仍可能限制智能体处理超长交互的能力。

2. **工具调用效率**：智能体在工具选择和调用顺序上仍有改进空间。

3. **长期规划能力**：当前架构在需要长期依赖和精确时序的任务上表现不佳。

### 12.3 能力局限

1. **语义障碍**：无法可靠地将漏洞利用概念转化为具体行动代码。

2. **领域知识**：在需要应用程序特定业务逻辑的挑战上表现有限。

3. **竞争条件攻击**：对需要精确时序操作的攻击类型有固有困难。

### 12.4 解释性局限

1. **决策不透明**：尽管结构化架构提高了可解释性，LLM决策过程仍存在黑盒问题。

2. **失败模式理解**：对智能体失败模式的深入理解仍不充分。

---

## 13. 伦理声明

### 13.1 研究价值

本研究对基于LLM的智能体系统在攻击性安全任务中的当前能力进行了严格的二次审视，提供了对技术现状的平衡和批判性评估。这对于：

- **安全研究社区**：帮助识别当前智能体能力的真实边界
- **实践者**：为选择自动化渗透测试工具提供依据
- **开发者**：指导改进智能体架构的设计决策

### 13.2 安全考虑

- 研究使用沙盒化CTF挑战作为安全评估的代理，不涉及真实系统
- 挑战在隔离的Docker环境中运行，不会造成真实伤害
- 代码和挑战痕迹公开以促进可复现性和负责任的披露

### 13.3 开放科学与可复现性

- 公开释放智能体实现和挑战痕迹
- 提供透明可解释的管道作为claude-code的对应物
- 这使得研究结果可以被验证和扩展

### 13.4 负责任的使用建议

研究结果表明，当前LLM智能体：
- 可作为渗透测试的辅助工具，但不能完全替代人类专家
- 在特定漏洞类别上存在系统性问题，需要人工监督
- 应与安全最佳实践结合使用

---

## 14. 参考文献

1. [claude-code cybersecurity performance claims - citations to prior work reporting near-human success rates]

2. [CVE announcement statistics - 15 minutes from disclosure]

3. Penetration testing definitions and standards

4. Multi-agent architecture design principles

5. claude-code tool use framework documentation

6. Prior work on near-human CTF performance

7. LLM assistance in penetration testing literature

8. Prior work on monolithic agent overburden issues

9. XBOW benchmark design

10. GPT model specifications

11. Claude Opus model specifications

12. Cybersecurity workforce gap statistics (4.8 million professionals)

13. Early work on LLM-assisted penetration testing

14. LLM knowledge of vulnerability classes and attack techniques

15. Prior claims on near-human success rates in cybersecurity competitions

16. CoALA cognitive architecture for language agents

17. GPT-5 model specifications

18. GPT-4.1 model specifications

19. Web application security incident statistics (44%)

20. Penetration testing standards references

21. Multi-agent architecture performance in network and web settings

22. CTF-style benchmark suites literature

23. Sandbox CVE benchmark references

24. CTF challenges as proxies for real attack scenarios

25. Structured orchestration and multi-agent architecture surveys

26. Multi-agent collaboration under coordinating agents

27. XBOW benchmark prior work and claims

28. LLM iterative reasoning and action selection

29. CTF-style evaluation suites

30. LLM knowledge of security tools

31. Agentic systems benchmark references

32. Multi-agent planner coordination approaches

---

## 附录：论文信息汇总

| 类别 | 信息 |
|------|------|
| **论文名称** | Autonomous LLM Agents & CTFs: A Second Look |
| **作者机构** | Università di Torino, Huawei Technologies France |
| **发表会议** | EuroS&P 2026 DeMeSSAI Workshop |
| **arXiv编号** | 2605.21497 |
| **GitHub** | https://github.com/SmartData-Polito/CTF_agent |
| **研究方向** | Agent Security / CTF / Penetration Testing |
| **核心贡献** | 对LLM智能体CTF能力进行二次审视，证明claude-code与精心设计架构表现相当但效率更低 |
| **实验规模** | 30个CTF挑战，14个漏洞类别，3种架构配置 |
| **主要发现** | 通用智能体是强基线；结构化编排优于单体设计；当前智能体仍低于人类水平 |