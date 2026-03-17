# 论文索引

<p align="center">
  <img src="https://img.shields.io/badge/Total-21%20Papers-blue?style=flat-square" alt="Total Papers">
  <img src="https://img.shields.io/badge/Complete-21%20Notes-success?style=flat-square" alt="Complete">
  <img src="https://img.shields.io/badge/Last%20Update-2026--03--17-informational?style=flat-square" alt="Last Update">
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

---

## 🏷️ 按标签分类

### 攻击类型

| 标签 | 论文数量 | 论文列表 |
|------|:--------:|----------|
| 🔓 越狱攻击 | 6 | Harnessing Task Overload, AutoDAN, PAIR, Cold-Attack, Tree of Attacks, GCG, AutoDAN-Turbo |
| 🎯 对抗攻击 | 2 | GCG, AutoDAN |
| 🧠 提示注入 | 1 | Under the Influence |
| 🎭 隐蔽攻击 | 2 | Cold-Attack, Sleeper Agents |
| 🚪 后门攻击 | 1 | Sleeper Agents |

### 防御类型

| 标签 | 论文数量 | 论文列表 |
|------|:--------:|----------|
| 🛡️ 安全对齐 | 2 | Nothing in Excess, Alignment-Weighted DPO |
| 🔍 输出检测 | 1 | MLLM-Protector |
| 🧪 红队测试 | 2 | APRT, Tree of Attacks |

### 评估基准

| 标签 | 论文数量 | 论文列表 |
|------|:--------:|----------|
| 📊 评估基准 | 5 | JailbreakBench, HarmBench, AuditBench, AgentDojo, R-Judge |

### 其他标签

| 标签 | 论文数量 | 论文列表 |
|------|:--------:|----------|
| 🖼️ 多模态 | 1 | MLLM-Protector |
| ⚡ 资源攻击 | 1 | Harnessing Task Overload |
| 🔄 过度拒绝 | 1 | Nothing in Excess |
| 🔬 漏洞分析 | 1 | LLMs know their vulnerabilities |
| 📚 综述 | 1 | LLM Security and Privacy Survey |
| 🤖 智能体安全 | 1 | AgentDojo |
| 🛡️ 风险意识 | 1 | R-Judge |
| 🔄 终身学习 | 1 | AutoDAN-Turbo |

---

## 📊 按类别详细分类

### 🔓 越狱攻击类（7篇）

| 论文 | 会议 | 核心思想 | 关键词 |
|------|------|----------|--------|
| [Harnessing Task Overload](./Harnessing-Task-Overload.md) | arXiv 2024 | 通过任务过载占用计算资源，使安全机制失效 | `资源饱和` `计算开销` `可扩展攻击` |
| [AutoDAN](./AutoDAN.md) | NeurIPS 2024 | 基于遗传算法自动生成隐蔽的越狱提示 | `对抗生成` `隐蔽攻击` `黑盒` `语义保持` |
| [PAIR](./PAIR.md) | arXiv 2024 | 仅需20次查询即可越狱黑盒LLM | `黑盒攻击` `查询高效` `自动优化` |
| [GCG](./GCG.md) | ICLR 2024 | 通用可迁移的对抗后缀攻击 | `对抗后缀` `白盒攻击` `可迁移` `贪心搜索` |
| [Tree of Attacks](./Tree-of-Attacks.md) | arXiv 2024 | 树状结构的红队攻击，分支探索多种攻击路径 | `红队测试` `树搜索` `自动化` `分支探索` |
| [Cold-Attack](./Cold-Attack.md) | arXiv 2024 | 隐蔽且可控的越狱攻击方法 | `隐蔽攻击` `可控性` `逃避检测` |
| [AutoDAN-Turbo](./AutoDAN-Turbo.md) | arXiv 2024 | 终身学习策略自探索代理，自动发现越狱策略 | `终身学习` `策略自探索` `黑盒` `自动化` |

### 🛡️ 防御与安全对齐（3篇）

| 论文 | 会议 | 核心思想 | 关键词 |
|------|------|----------|--------|
| [MLLM-Protector](./MLLM-Protector.md) | arXiv 2024 | 多模态模型输出端轻量级检测与解毒 | `多模态` `输出检测` `轻量级` `性能无损` |
| [Nothing in Excess](./Nothing-in-Excess.md) | ICLR 2025 | 缓解过度安全对齐导致的过度拒绝问题 | `过度拒绝` `安全对齐` `平衡` `有用性` |
| [Alignment-Weighted DPO](./Alignment-Weighted-DPO.md) | arXiv 2024 | 加权DPO优化安全对齐效果 | `DPO` `加权训练` `安全对齐` `样本重要性` |

### 📊 评估基准（5篇）

| 论文 | 会议 | 核心思想 | 关键词 |
|------|------|----------|--------|
| [JailbreakBench](./JailbreakBench.md) | arXiv 2024 | 越狱攻击的标准化评估基准 | `基准测试` `评估框架` `鲁棒性` `标准化` |
| [HarmBench](./HarmBench.md) | ICLR 2024 | 标准化安全评估框架 | `安全评估` `标准化` `自动化` `全面性` |
| [AuditBench](./AuditBench.md) | arXiv 2024 | 安全审计基准测试 | `安全审计` `评估基准` `合规性` |
| [AgentDojo](./AgentDojo.md) | NeurIPS 2024 | 动态提示注入攻击评估环境，支持多工具智能体 | `动态评估` `提示注入` `智能体` `多工具` |
| [R-Judge](./R-Judge.md) | EMNLP 2024 | 智能体风险意识评估基准，系统性评估风险识别能力 | `风险意识` `智能体` `评估基准` `多维度` |

### 🧪 红队测试（2篇）

| 论文 | 会议 | 核心思想 | 关键词 |
|------|------|----------|--------|
| [APRT](./APRT.md) | COLING 2025 | 自动化渐进式红队测试框架 | `红队测试` `渐进式` `自动化` `持续优化` |
| [Tree of Attacks](./Tree-of-Attacks.md) | arXiv 2024 | 树状结构的红队攻击方法 | `红队测试` `树搜索` `分支探索` |

### 🔬 其他重要论文（4篇）

| 论文 | 会议 | 核心思想 | 关键词 |
|------|------|----------|--------|
| [Sleeper Agents](./Sleeper-Agents.md) | ICLR 2024 | 训练具有欺骗性的持久化后门 | `后门攻击` `欺骗性` `持久化` `安全训练` |
| [Under the Influence](./Under-the-Influence.md) | arXiv 2024 | 提示注入攻击与上下文操控 | `提示注入` `上下文操控` `指令劫持` |
| [LLMs know their vulnerabilities](./LLMs-know-their-vulnerabilities.md) | arXiv 2024 | LLM对自身安全漏洞的认知能力 | `自我认知` `漏洞分析` `元认知` |
| [LLM Security and Privacy Survey](./LLM-Security-and-Privacy-Survey.md) | arXiv 2024 | LLM安全与隐私全面综述 | `综述` `全景` `分类体系` |

---

## 🔍 使用指南

### 查找论文

- **按攻击类型**：查看「按标签分类」→ 攻击类型
- **按防御方法**：查看「按标签分类」→ 防御类型
- **按完成状态**：所有论文均为 ✅ 完整笔记
- **按会议等级**：查看快速索引表的「会议/年份」列

### 阅读建议

**入门路径：**
1. 先读 [LLM Security and Privacy Survey](./LLM-Security-and-Privacy-Survey.md) 了解全景
2. 再看评估基准（JailbreakBench, HarmBench, AgentDojo）了解评测方法

**攻击研究路径：**
1. [GCG](./GCG.md) - 经典的对抗后缀攻击
2. [AutoDAN](./AutoDAN.md) - 隐蔽的语义保持攻击
3. [PAIR](./PAIR.md) - 高效的黑盒攻击
4. [AutoDAN-Turbo](./AutoDAN-Turbo.md) - 终身学习的自动化攻击

**防御研究路径：**
1. [MLLM-Protector](./MLLM-Protector.md) - 输出层防御
2. [Nothing in Excess](./Nothing-in-Excess.md) - 安全与有用性平衡
3. [Alignment-Weighted DPO](./Alignment-Weighted-DPO.md) - 训练阶段优化

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

- **最后更新**：2026-03-17
- **论文总数**：21 篇
- **完整笔记**：21 篇 (100%)
- **维护者**：AI 助手 + 人工审核
- **更新频率**：随阅读进度同步更新

---

*返回 [项目主页](../README.md)*
