# LLM Safety Papers Reading Notes

<p align="center">
  <img src="https://img.shields.io/badge/Papers-80%20Total-blue?style=flat-square" alt="Total Papers">
  <img src="https://img.shields.io/badge/Completed-25%2F80-success?style=flat-square" alt="Completed">
</p>

<p align="center">
  <b>大模型安全论文阅读笔记</b> | 系统整理 LLM 安全领域的核心论文
</p>

---

## 📑 目录

- [项目概况](#-项目概况)
- [快速导航](#-快速导航)
- [论文分类](#-论文分类)
- [仓库结构](#-仓库结构)
- [阅读指南](#-阅读指南)
- [贡献方式](#-贡献方式)
- [相关资源](#-相关资源)

---

## 📊 项目概况

本项目系统整理大语言模型（LLM）安全领域的核心论文，涵盖攻击方法、防御机制、评估基准等方向。

| 指标 | 数值 |
|------|------|
| **计划完成** | 80 篇 |
| **已完成** | 25 篇 (31.25%) |
| **最后更新** | 2026-03-21 |

---

## 🧭 快速导航

### 按攻击类型

| 类型 | 说明 | 代表论文 |
|------|------|----------|
| 🔓 **越狱攻击** | 诱导模型输出有害内容 | [Harnessing Task Overload](./papers/2024/Harnessing-Task-Overload.md), [AutoDAN](./papers/2024/AutoDAN.md), [PAIR](./papers/2024/PAIR.md), [GCG](./papers/2024/GCG.md), [Tree of Attacks](./papers/2024/Tree-of-Attacks.md), [AutoDAN-Turbo](./papers/2024/AutoDAN-Turbo.md), [MultiJail](./papers/2024/MultiJail.md), [Crescendo](./papers/2025/Crescendo.md), [ActorBreaker](./papers/2025/ActorBreaker.md) |
| 🎯 **对抗攻击** | 构造对抗样本欺骗模型 | [GCG](./papers/2024/GCG.md), [AutoDAN](./papers/2024/AutoDAN.md) |
| 🧠 **提示注入** | 通过提示操控模型行为 | [Under the Influence](./papers/2024/Under-the-Influence.md) |
| 🎭 **隐蔽攻击** | 难以检测的攻击方式 | [Cold-Attack](./papers/2024/Cold-Attack.md), [Sleeper Agents](./papers/2024/Sleeper-Agents.md) |

### 按防御类型

| 类型 | 说明 | 代表论文 |
|------|------|----------|
| 🛡️ **安全对齐** | 训练阶段的安全优化 | [Nothing in Excess](./papers/2025/Nothing-in-Excess.md), [Alignment-Weighted DPO](./papers/2024/Alignment-Weighted-DPO.md) |
| 🔍 **输出检测** | 生成内容的实时检测 | [MLLM-Protector](./papers/2024/MLLM-Protector.md), [SafeGen](./papers/2024/SafeGen.md) |
| 🧪 **红队测试** | 主动发现安全漏洞 | [APRT](./papers/2025/APRT.md), [Tree of Attacks](./papers/2024/Tree-of-Attacks.md) |

### 按评估基准

| 基准 | 说明 | 论文 |
|------|------|------|
| 📊 **JailbreakBench** | 越狱攻击评估基准 | [JailbreakBench](./papers/2024/JailbreakBench.md) |
| ⚖️ **HarmBench** | 标准化安全评估框架 | [HarmBench](./papers/2024/HarmBench.md) |
| 🔎 **AuditBench** | 安全审计基准 | [AuditBench](./papers/2024/AuditBench.md) |
| 🤖 **AgentDojo** | 智能体安全评估环境 | [AgentDojo](./papers/2024/AgentDojo.md) |
| 🛡️ **R-Judge** | 智能体风险意识评估 | [R-Judge](./papers/2024/R-Judge.md) |
| 🔬 **SIABench** | 安全事件分析评估 | [SIABench](./papers/2026/SIABench.md) |
| 📊 **ESG-Bench** | 长上下文幻觉缓解评估 | [ESG-Bench](./papers/2026/ESG-Bench.md) |

### 其他重要方向

| 方向 | 说明 | 论文 |
|------|------|------|
| 📚 **综述** | 领域全面回顾 | [Jailbreak Attacks and Defenses Survey](./papers/2024/Jailbreak-Attacks-and-Defenses-Survey.md), [LLM Security and Privacy Survey](./papers/2024/LLM-Security-and-Privacy-Survey.md), [TrustLLM](./papers/2024/TrustLLM.md) |
| 🔬 **漏洞分析** | 模型自我认知漏洞 | [Jailbroken](./papers/2023/Jailbroken.md) |

---

## 📁 仓库结构

```
llm-safety-papers/
├── README.md                          # 项目主页（本文件）
├── PAPER_COLLECTION.md                # 论文汇总（约80篇）
├── papers/
│   ├── README.md                      # 论文索引与快速检索
│   ├── 2026/                          # 2026年论文 (2篇)
│   │   ├── SIABench.md
│   │   └── ESG-Bench.md
│   ├── 2025/                          # 2025年论文 (4篇)
│   │   ├── ActorBreaker.md
│   │   ├── APRT.md
│   │   ├── Crescendo.md
│   │   └── Nothing-in-Excess.md
│   ├── 2024/                          # 2024年论文 (18篇)
│   │   ├── AgentDojo.md
│   │   ├── Alignment-Weighted-DPO.md
│   │   ├── AuditBench.md
│   │   ├── AutoDAN.md
│   │   ├── AutoDAN-Turbo.md
│   │   ├── Cold-Attack.md
│   │   ├── GCG.md
│   │   ├── HarmBench.md
│   │   ├── Harnessing-Task-Overload.md
│   │   ├── Jailbreak-Attacks-and-Defenses-Survey.md
│   │   ├── JailbreakBench.md
│   │   ├── LLM-Security-and-Privacy-Survey.md
│   │   ├── MLLM-Protector.md
│   │   ├── MultiJail.md
│   │   ├── PAIR.md
│   │   ├── R-Judge.md
│   │   ├── SafeGen.md
│   │   ├── Sleeper-Agents.md
│   │   ├── TrustLLM.md
│   │   ├── Tree-of-Attacks.md
│   │   └── Under-the-Influence.md
│   └── 2023/                          # 2023年论文 (1篇)
│       └── Jailbroken.md
└── .github/                           # GitHub 配置
    └── workflows/                     # 自动化工作流
```

---

## 📚 论文列表

### 越狱攻击类（9篇）

| # | 论文 | 会议/年份 | 核心思想 | 标签 |
|---|------|----------|----------|------|
| 1 | [Harnessing Task Overload](./papers/2024/Harnessing-Task-Overload.md) | arXiv 2024 | 资源饱和攻击，占用计算资源绕过安全机制 | `资源饱和` `计算开销` |
| 2 | [AutoDAN](./papers/2024/AutoDAN.md) | NeurIPS 2024 | 遗传算法生成隐蔽的越狱提示 | `对抗生成` `隐蔽攻击` `黑盒` |
| 3 | [PAIR](./papers/2024/PAIR.md) | arXiv 2024 | 20次查询内越狱黑盒LLM | `黑盒攻击` `查询高效` |
| 4 | [GCG](./papers/2024/GCG.md) | ICLR 2024 | 通用可迁移的对抗攻击 | `对抗后缀` `白盒攻击` `可迁移` |
| 5 | [Tree of Attacks](./papers/2024/Tree-of-Attacks.md) | arXiv 2024 | 树状结构的红队攻击 | `红队测试` `自动化` `树搜索` |
| 6 | [Cold-Attack](./papers/2024/Cold-Attack.md) | arXiv 2024 | 隐蔽且可控的越狱攻击方法 | `隐蔽攻击` `可控性` |
| 7 | [AutoDAN-Turbo](./papers/2024/AutoDAN-Turbo.md) | arXiv 2024 | 终身学习策略自探索代理 | `终身学习` `策略自探索` `黑盒` |
| 8 | [Crescendo](./papers/2025/Crescendo.md) | USENIX Security 2025 | 多轮渐进式越狱攻击 | `多轮攻击` `渐进式` `良性输入` |
| 9 | [ActorBreaker](./papers/2025/ActorBreaker.md) | ACL 2025 | 基于行动者网络的多轮越狱攻击，通过自然分布偏移发现安全漏洞 | `多轮攻击` `行动者网络` `自然分布偏移` |

### 防御与安全对齐（4篇）

| # | 论文 | 会议/年份 | 核心思想 | 标签 |
|---|------|----------|----------|------|
| 10 | [MLLM-Protector](./papers/2024/MLLM-Protector.md) | arXiv 2024 | 多模态模型输出端检测与解毒 | `多模态` `输出检测` `轻量级` |
| 11 | [Nothing in Excess](./papers/2025/Nothing-in-Excess.md) | ICLR 2025 | 缓解过度安全对齐导致的过度拒绝 | `过度拒绝` `安全对齐` `平衡` |
| 12 | [Alignment-Weighted DPO](./papers/2024/Alignment-Weighted-DPO.md) | arXiv 2024 | 加权DPO优化安全对齐 | `DPO` `加权训练` `安全对齐` |
| 13 | [SafeGen](./papers/2024/SafeGen.md) | IEEE S&P 2024 | T2I模型性暗示内容生成防护 | `多模态` `内容过滤` `即插即用` |

### 评估基准（7篇）

| # | 论文 | 会议/年份 | 核心思想 | 标签 |
|---|------|----------|----------|------|
| 14 | [JailbreakBench](./papers/2024/JailbreakBench.md) | arXiv 2024 | 越狱攻击评估基准 | `基准测试` `评估框架` `鲁棒性` |
| 15 | [HarmBench](./papers/2024/HarmBench.md) | ICLR 2024 | 标准化安全评估框架 | `安全评估` `标准化` `自动化` |
| 16 | [AuditBench](./papers/2024/AuditBench.md) | arXiv 2024 | 安全审计基准测试 | `安全审计` `评估基准` |
| 17 | [AgentDojo](./papers/2024/AgentDojo.md) | NeurIPS 2024 | 动态提示注入攻击评估环境 | `动态评估` `提示注入` `智能体` |
| 18 | [R-Judge](./papers/2024/R-Judge.md) | EMNLP 2024 | 智能体风险意识评估基准 | `风险意识` `智能体` `评估基准` |
| 19 | [SIABench](./papers/2026/SIABench.md) | arXiv 2026 | 安全事件分析评估框架 | `网络安全` `评估基准` `智能体` |
| 20 | [ESG-Bench](./papers/2026/ESG-Bench.md) | AAAI 2026 | 长上下文ESG报告幻觉缓解评估 | `幻觉缓解` `长上下文` `事实可靠性` |

### 红队测试（2篇）

| # | 论文 | 会议/年份 | 核心思想 | 标签 |
|---|------|----------|----------|------|
| 21 | [APRT](./papers/2025/APRT.md) | COLING 2025 | 自动化渐进式红队测试 | `红队测试` `渐进式` `自动化` |
| 22 | [Tree of Attacks](./papers/2024/Tree-of-Attacks.md) | arXiv 2024 | 树状结构的红队攻击 | `红队测试` `树搜索` |

### 其他重要论文（3篇）

| # | 论文 | 会议/年份 | 核心思想 | 标签 |
|---|------|----------|----------|------|
| 23 | [Jailbreak Attacks and Defenses Survey](./papers/2024/Jailbreak-Attacks-and-Defenses-Survey.md) | arXiv 2024 | 越狱攻击与防御全面综述 | `综述` `攻击` `防御` `分类` |
| 24 | [Under the Influence](./papers/2024/Under-the-Influence.md) | arXiv 2024 | 提示注入攻击与防御 | `提示注入` `上下文操控` |
| 25 | [LLM Security and Privacy Survey](./papers/2024/LLM-Security-and-Privacy-Survey.md) | arXiv 2024 | LLM安全与隐私全面综述 | `综述` `全景` |
| 26 | [TrustLLM](./papers/2024/TrustLLM.md) | arXiv 2024 | LLM可信度六维评估基准 | `综述` `可信度` `评估基准` |
| 27 | [Jailbroken: How Does LLM Safety Training Fail?](./papers/2023/Jailbroken.md) | NeurIPS 2023 | LLM安全训练失败原因分析 | `安全训练` `漏洞分析` |

---

## 📝 阅读指南

### 笔记格式标准

每篇完整笔记包含以下章节：

1. **基本信息** - 标题、作者、会议、链接、引用
2. **研究背景** - 问题定义、现有方法局限
3. **核心贡献** - 主要创新点
4. **研究方法** - 技术细节、算法流程
5. **实验设置** - 数据集、评估指标
6. **实验结果** - 关键结果、性能对比
7. **策略示例** - 提示模板、攻击/防御流程
8. **消融实验** - 各组件贡献分析
9. **局限性** - 方法限制、改进方向
10. **伦理声明** - 研究伦理、数据使用
11. **参考文献** - 相关论文列表

### 快速阅读建议

- **想快速了解领域**：先看 [LLM Security and Privacy Survey](./papers/2024/LLM-Security-and-Privacy-Survey.md) 和评估基准类论文
- **关注攻击方法**：重点阅读 GCG、AutoDAN、PAIR、Harnessing Task Overload
- **关注防御方法**：重点阅读 MLLM-Protector、Nothing in Excess、Alignment-Weighted DPO
- **关注评估基准**：重点阅读 JailbreakBench、HarmBench、AuditBench、AgentDojo、SIABench、ESG-Bench
- **关注幻觉缓解**：重点阅读 ESG-Bench

### 进阶阅读路径

```
入门 → 综述 → 攻击方法 → 防御方法 → 评估基准 → 前沿研究
```

---

## 🤝 贡献方式

欢迎贡献！你可以通过以下方式参与：

1. **补充笔记** - 完善标记为 📝 的论文笔记
2. **上传新论文** - 将 PAPER_COLLECTION.md 中的论文整理上传到 papers/ 目录
3. **修正错误** - 发现笔记中的错误请提 Issue 或 PR
4. **添加分类** - 建议新的论文分类或标签

### 提交规范

- 使用 Markdown 格式
- 遵循现有笔记的结构模板
- 添加适当的标签和分类
- 注明参考来源

---

## 📖 相关资源

### 内部资源
- 📚 [论文汇总](./PAPER_COLLECTION.md) - 约80篇LLM Safety论文完整列表（2021-2026）

### 外部资源
- 📚 [arXiv CS.CR](https://arxiv.org/list/cs.CR/recent) - 最新安全论文
- 🔬 [HarmBench Leaderboard](https://harmbench.org) - 安全评估排行榜
- 🏆 [JailbreakBench](https://jailbreakbench.github.io) - 越狱攻击基准

---

## 📌 更新日志

| 日期 | 更新内容 |
|------|----------|
| 2026-03-21 | 添加论文：ESG-Bench - 长上下文ESG报告幻觉缓解评估 (AAAI 2026)，更新进度至 25/80 |
| 2026-03-21 | 重构 papers 目录: 按发表年份分目录整理 (2023/2024/2025/2026) |
| 2026-03-21 | 删除重复论文: LLMs-know-their-vulnerabilities.md (与ActorBreaker.md重复) |
| 2026-03-21 | 修正论文：ActorBreaker (v2最新版本) - 更新标题、方法名、代码链接 |
| 2026-03-21 | 添加论文：Jailbroken - LLM安全训练失败原因分析 (NeurIPS 2023) |
| 2026-03-20 | 添加论文：Crescendo - 多轮渐进式LLM越狱攻击 (USENIX Security 2025) |
| 2026-03-19 | 添加论文：SIABench - 安全事件分析评估框架 |
| 2026-03-19 | 更新论文：AgentDojo - 添加完整的12章详细阅读笔记 |
| 2026-03-18 | 添加论文：Jailbreak Attacks and Defenses Against LLMs - A Survey |
| 2026-03-17 | 初始化仓库，上传 23 篇论文笔记，完善 README 结构，添加论文汇总 |

---

<p align="center">
  <i>笔记由 AI 助手辅助整理，基于 arXiv 公开信息生成。</i><br>
  <i>如有问题或建议，欢迎提交 Issue。</i>
</p>
