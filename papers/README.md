# 论文索引

<p align="center">
  <img src="https://img.shields.io/badge/Total-28%20Papers-blue?style=flat-square" alt="Total Papers">
  <img src="https://img.shields.io/badge/Complete-28%20Notes-success?style=flat-square" alt="Complete">
  <img src="https://img.shields.io/badge/Last%20Update-2026--03-21-informational?style=flat-square" alt="Last Update">
</p>

本目录包含 LLM 安全领域的论文阅读笔记，按类别和状态整理。

---

## 📋 快速索引表

| 序号 | 论文标题 | 会议/年份 | 类别 | 状态 |
|:----:|----------|:---------:|------|:----:|
| 1 | [Harnessing Task Overload: Scalable Jailbreak Attacks](./Harnessing-Task-Overload.md) | arXiv 2024 | 越狱攻击 | ✅ |
| 2 | [MLLM-Protector: Ensuring MLLM's Safety without Hurting Performance](./MLLM-Protector.md) | arXiv 2024 | 多模态安全 | ✅ |
| 3 | [AutoDAN: Generating Stealthy Jailbreak Prompts](./AutoDAN.md) | NeurIPS 2024 | 越狱攻击 | ✅ |
| 4 | [Nothing in Excess: Mitigating Exaggerated Safety](./Nothing-in-Excess.md) | ICLR 2025 | 安全对齐 | ✅ |
| 5 | [JailbreakBench: Open Robustness Benchmark](./JailbreakBench.md) | arXiv 2024 | 评估基准 | ✅ |
| 6 | [HarmBench: Standardized Evaluation Framework](./HarmBench.md) | ICLR 2024 | 评估基准 | ✅ |
| 7 | [APRT: Automated Progressive Red Teaming](./APRT.md) | COLING 2025 | 红队测试 | ✅ |
| 8 | [GCG: Universal and Transferable Adversarial Attacks](./GCG.md) | ICLR 2024 | 对抗攻击 | ✅ |
| 9 | [PAIR: Jailbreaking Black Box LLMs in Twenty Queries](./PAIR.md) | arXiv 2024 | 越狱攻击 | ✅ |
| 10 | [Tree of Attacks: Jailbreaking Black-Box LLMs Automatically](./Tree-of-Attacks.md) | arXiv 2024 | 红队测试 | ✅ |
| 11 | [Cold-Attack: Jailbreaking LLMs with Stealth and Controllability](./Cold-Attack.md) | arXiv 2024 | 越狱攻击 | ✅ |
| 12 | [Sleeper Agents: Training Deceptive LLMs](./Sleeper-Agents.md) | ICLR 2024 | 后门攻击 | ✅ |
| 13 | [Under the Influence](./Under-the-Influence.md) | arXiv 2024 | 提示注入 | ✅ |
| 14 | [Alignment-Weighted DPO](./Alignment-Weighted-DPO.md) | arXiv 2024 | 安全对齐 | ✅ |
| 15 | [AuditBench](./AuditBench.md) | arXiv 2024 | 评估基准 | ✅ |
| 16 | [LLMs know their vulnerabilities](./LLMs-know-their-vulnerabilities.md) | arXiv 2024 | 漏洞分析 | ✅ |
| 17 | [LLM Security and Privacy Survey](./LLM-Security-and-Privacy-Survey.md) | arXiv 2024 | 综述 | ✅ |
| 18 | [AgentDojo: Dynamic Environment for LLM Agent Security](./AgentDojo.md) | NeurIPS 2024 | 评估基准 | ✅ |
| 19 | [AutoDAN-Turbo: Lifelong Agent for Jailbreak Strategy](./AutoDAN-Turbo.md) | arXiv 2024 | 越狱攻击 | ✅ |
| 20 | [R-Judge: Benchmarking Safety Risk Awareness for LLM Agents](./R-Judge.md) | EMNLP 2024 | 评估基准 | ✅ |
| 21 | [TrustLLM: Trustworthiness in Large Language Models](./TrustLLM.md) | arXiv 2024 | 综述 | ✅ |
| 22 | [SafeGen: Mitigating Sexually Explicit Content in T2I Models](./SafeGen.md) | IEEE S&P 2024 | 多模态安全 | ✅ |
| 23 | [MultiJail: Jailbreaking T2I Models via Multi-Modal Attack](./MultiJail.md) | arXiv 2024 | 多模态攻击 | ✅ |
| 24 | [Jailbreak Attacks and Defenses Survey](./Jailbreak-Attacks-and-Defenses-Survey.md) | arXiv 2024 | 综述 | ✅ |
| 25 | [SIABench: Evaluating LLMs for Security Incident Analysis](./SIABench.md) | arXiv 2026 | 网络安全评估 | ✅ |
| 26 | [Crescendo: Multi-Turn LLM Jailbreak Attack](./Crescendo.md) | USENIX Security 2025 | 多轮越狱攻击 | ✅ |
| 27 | [Jailbroken: How Does LLM Safety Training Fail?](./Jailbroken.md) | NeurIPS 2023 | 安全训练分析 | ✅ |
| 28 | [ActorBreaker: Multi-turn LLM Jailbreak Attack](./ActorBreaker.md) | ACL 2025 | 多轮越狱攻击 | ✅ |

---

## 🏷️ 按标签分类

### 攻击类型

| 标签 | 论文数量 | 论文列表 |
|------|:--------:|----------|
| 🔓 越狱攻击 | 9 | Harnessing Task Overload, AutoDAN, PAIR, Cold-Attack, Tree of Attacks, GCG, AutoDAN-Turbo, Crescendo, ActorBreaker |
| 🎯 对抗攻击 | 2 | GCG, AutoDAN |
| 🧠 提示注入 | 1 | Under the Influence |
| 🎭 隐蔽攻击 | 2 | Cold-Attack, Sleeper Agents |
| 🚪 后门攻击 | 1 | Sleeper Agents |

### 防御类型

| 标签 | 论文数量 | 论文列表 |
|------|:--------:|----------|
| 🛡️ 安全对齐 | 2 | Nothing in Excess, Alignment-Weighted DPO |
| 🔍 输出检测 | 2 | MLLM-Protector, SafeGen |
| 🧪 红队测试 | 2 | APRT, Tree of Attacks |

### 评估基准

| 标签 | 论文数量 | 论文列表 |
|------|:--------:|----------|
| 📊 评估基准 | 6 | JailbreakBench, HarmBench, AuditBench, AgentDojo, R-Judge, SIABench |

### 其他标签

| 标签 | 论文数量 | 论文列表 |
|------|:--------:|----------|
| 🖼️ 多模态 | 3 | MLLM-Protector, SafeGen, MultiJail |
| ⚡ 资源攻击 | 1 | Harnessing Task Overload |
| 🔄 过度拒绝 | 1 | Nothing in Excess |
| 🔬 漏洞分析 | 2 | LLMs know their vulnerabilities, Jailbroken |
| 📚 综述 | 3 | LLM Security and Privacy Survey, Jailbreak Attacks and Defenses Survey, TrustLLM |
| 🤖 智能体安全 | 2 | AgentDojo, R-Judge |
| 🛡️ 风险意识 | 1 | R-Judge |
| 🔄 终身学习 | 1 | AutoDAN-Turbo |
| 🔒 网络安全 | 1 | SIABench |
| 🔍 安全训练分析 | 1 | Jailbroken |

---

## 📊 按类别详细分类

### 🔓 越狱攻击类（9篇）

| 论文 | 会议 | 核心思想 | 关键词 |
|------|------|----------|--------|
| [Harnessing Task Overload](./Harnessing-Task-Overload.md) | arXiv 2024 | 通过任务过载占用计算资源，使安全机制失效 | `资源饱和` `计算开销` `可扩展攻击` |
| [AutoDAN](./AutoDAN.md) | NeurIPS 2024 | 基于遗传算法自动生成隐蔽的越狱提示 | `对抗生成` `隐蔽攻击` `黑盒` `语义保持` |
| [PAIR](./PAIR.md) | arXiv 2024 | 仅需20次查询即可越狱黑盒LLM | `黑盒攻击` `查询高效` `自动优化` |
| [GCG](./GCG.md) | ICLR 2024 | 通用可迁移的对抗后缀攻击 | `对抗后缀` `白盒攻击` `可迁移` `贪心搜索` |
| [Tree of Attacks](./Tree-of-Attacks.md) | arXiv 2024 | 树状结构的红队攻击，分支探索多种攻击路径 | `红队测试` `树搜索` `自动化` `分支探索` |
| [Cold-Attack](./Cold-Attack.md) | arXiv 2024 | 隐蔽且可控的越狱攻击方法 | `隐蔽攻击` `可控性` `逃避检测` |
| [AutoDAN-Turbo](./AutoDAN-Turbo.md) | arXiv 2024 | 终身学习策略自探索代理，自动发现越狱策略 | `终身学习` `策略自探索` `黑盒` `自动化` |
| [Crescendo](./Crescendo.md) | USENIX Security 2025 | 多轮渐进式越狱攻击，利用良性输入突破安全对齐 | `多轮攻击` `渐进式` `良性输入` `黑盒` |
| [ActorBreaker](./ActorBreaker.md) | ACL 2025 | 基于行动者网络理论的多轮越狱攻击，通过自然分布偏移发现安全漏洞 | `多轮攻击` `行动者网络` `自然分布偏移` |

### 🛡️ 防御与安全对齐（4篇）

| 论文 | 会议 | 核心思想 | 关键词 |
|------|------|----------|--------|
| [MLLM-Protector](./MLLM-Protector.md) | arXiv 2024 | 多模态模型输出端轻量级检测与解毒 | `多模态` `输出检测` `轻量级` `性能无损` |
| [SafeGen](./SafeGen.md) | IEEE S&P 2024 | T2I模型性暗示内容生成防护 | `多模态` `内容过滤` `即插即用` |
| [Nothing in Excess](./Nothing-in-Excess.md) | ICLR 2025 | 缓解过度安全对齐导致的过度拒绝问题 | `过度拒绝` `安全对齐` `平衡` `有用性` |
| [Alignment-Weighted DPO](./Alignment-Weighted-DPO.md) | arXiv 2024 | 加权DPO优化安全对齐效果 | `DPO` `加权训练` `安全对齐` `样本重要性` |

### 📊 评估基准（6篇）

| 论文 | 会议 | 核心思想 | 关键词 |
|------|------|----------|--------|
| [JailbreakBench](./JailbreakBench.md) | arXiv 2024 | 越狱攻击的标准化评估基准 | `基准测试` `评估框架` `鲁棒性` `标准化` |
| [HarmBench](./HarmBench.md) | ICLR 2024 | 标准化安全评估框架 | `安全评估` `标准化` `自动化` `全面性` |
| [AuditBench](./AuditBench.md) | arXiv 2024 | 安全审计基准测试 | `安全审计` `评估基准` `合规性` |
| [AgentDojo](./AgentDojo.md) | NeurIPS 2024 | 动态提示注入攻击评估环境，支持97个真实世界任务 | `动态评估` `提示注入` `智能体` `多工具` |
| [R-Judge](./R-Judge.md) | EMNLP 2024 | 智能体风险意识评估基准，系统性评估风险识别能力 | `风险意识` `智能体` `评估基准` `多维度` |
| [SIABench](./SIABench.md) | arXiv 2026 | 安全事件分析评估框架，评估LLM在SOC任务中的能力 | `网络安全` `评估基准` `智能体` `SOC` |

### 🧪 红队测试（2篇）

| 论文 | 会议 | 核心思想 | 关键词 |
|------|------|----------|--------|
| [APRT](./APRT.md) | COLING 2025 | 自动化渐进式红队测试框架 | `红队测试` `渐进式` `自动化` `持续优化` |
| [Tree of Attacks](./Tree-of-Attacks.md) | arXiv 2024 | 树状结构的红队攻击方法 | `红队测试` `树搜索` `分支探索` |

### 🔬 其他重要论文（7篇）

| 论文 | 会议 | 核心思想 | 关键词 |
|------|------|----------|--------|
| [Jailbreak Attacks and Defenses Survey](./Jailbreak-Attacks-and-Defenses-Survey.md) | arXiv 2024 | 越狱攻击与防御全面综述，系统分类攻击和防御方法 | `综述` `攻击` `防御` `分类` `关系图谱` |
| [Sleeper Agents](./Sleeper-Agents.md) | ICLR 2024 | 训练具有欺骗性的持久化后门 | `后门攻击` `欺骗性` `持久化` `安全训练` |
| [Under the Influence](./Under-the-Influence.md) | arXiv 2024 | 提示注入攻击与上下文操控 | `提示注入` `上下文操控` `指令劫持` |
| [LLMs know their vulnerabilities](./LLMs-know-their-vulnerabilities.md) | arXiv 2024 | LLM对自身安全漏洞的认知能力 | `自我认知` `漏洞分析` `元认知` |
| [Jailbroken](./Jailbroken.md) | NeurIPS 2023 | 安全训练失败的两种模式：竞争目标与不匹配泛化 | `安全训练` `失败模式` `竞争目标` `不匹配泛化` |
| [LLM Security and Privacy Survey](./LLM-Security-and-Privacy-Survey.md) | arXiv 2024 | LLM安全与隐私全面综述 | `综述` `全景` `分类体系` |
| [TrustLLM](./TrustLLM.md) | arXiv 2024 | LLM可信度六维评估基准 | `综述` `可信度` `评估基准` |
| [MultiJail](./MultiJail.md) | arXiv 2024 | 多模态越狱攻击T2I模型 | `多模态` `视觉提示` `越狱` |

---

## 🔍 使用指南

### 查找论文

- **按攻击类型**：查看「按标签分类」→ 攻击类型
- **按防御方法**：查看「按标签分类」→ 防御类型
- **按完成状态**：所有论文均为 ✅ 完整笔记
- **按会议等级**：查看快速索引表的「会议/年份」列

### 阅读建议

**入门路径：**
1. 先读 [Jailbreak Attacks and Defenses Survey](./Jailbreak-Attacks-and-Defenses-Survey.md) 了解越狱攻击与防御全景
2. 再读 [LLM Security and Privacy Survey](./LLM-Security-and-Privacy-Survey.md) 了解LLM安全整体概况
3. 再看评估基准（JailbreakBench, HarmBench, AgentDojo, SIABench）了解评测方法

**攻击研究路径：**
1. [GCG](./GCG.md) - 经典的对抗后缀攻击
2. [AutoDAN](./AutoDAN.md) - 隐蔽的语义保持攻击
3. [PAIR](./PAIR.md) - 高效的黑盒攻击
4. [AutoDAN-Turbo](./AutoDAN-Turbo.md) - 终身学习的自动化攻击
5. [Crescendo](./Crescendo.md) - 多轮渐进式攻击
6. [ActorBreaker](./ActorBreaker.md) - 基于行动者网络的多轮攻击

**防御研究路径：**
1. [MLLM-Protector](./MLLM-Protector.md) - 输出层防御
2. [Nothing in Excess](./Nothing-in-Excess.md) - 安全与有用性平衡
3. [Alignment-Weighted DPO](./Alignment-Weighted-DPO.md) - 训练阶段优化

**智能体安全路径：**
1. [AgentDojo](./AgentDojo.md) - 智能体安全评估框架
2. [R-Judge](./R-Judge.md) - 智能体风险意识评估
3. [SIABench](./SIABench.md) - 安全事件分析评估

### 笔记格式

完整笔记包含以下章节：
- 基本信息（标题、作者、会议、链接）
- 研究背景与意义
- 所用数据集
- 研究方法
- 实验详细记录
- 结果分析
- 展望
- 代码资源
- 参考文献

---

## 📝 维护说明

- **最后更新**：2026-03-21
- **论文总数**：28 篇
- **完整笔记**：28 篇 (100%)
- **维护者**：AI 助手 + 人工审核
- **更新频率**：随阅读进度同步更新

---

*返回 [项目主页](../README.md)*
