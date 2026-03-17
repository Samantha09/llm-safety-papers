# LLM Safety Papers Reading Notes

<p align="center">
  <img src="https://img.shields.io/badge/Papers-80%20Total-blue?style=flat-square" alt="Total Papers">
  <img src="https://img.shields.io/badge/Read-22%20Done-success?style=flat-square" alt="Read Progress">
  <img src="https://img.shields.io/badge/Uploaded-6%20Notes-orange?style=flat-square" alt="Uploaded">
  <img src="https://img.shields.io/badge/Progress-27.5%25-yellow?style=flat-square" alt="Progress">
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
| **计划阅读** | 80 篇 |
| **已完成阅读** | 22 篇 (27.5%) |
| **已整理笔记** | 6 篇 |
| **最后更新** | 2026-03-17 |

---

## 🧭 快速导航

### 按攻击类型

| 类型 | 说明 | 代表论文 |
|------|------|----------|
| 🔓 **越狱攻击** | 诱导模型输出有害内容 | [Harnessing Task Overload](./papers/harnessing-task-overload.md), [AutoDAN](./papers/autodan.md) |
| 🎯 **对抗攻击** | 构造对抗样本欺骗模型 | GCG, PAIR |
| 🧠 **提示注入** | 通过提示操控模型行为 | - |

### 按防御类型

| 类型 | 说明 | 代表论文 |
|------|------|----------|
| 🛡️ **安全对齐** | 训练阶段的安全优化 | [Nothing in Excess](./papers/nothing-in-excess.md) |
| 🔍 **输出检测** | 生成内容的实时检测 | [MLLM-Protector](./papers/mllm-protector.md) |
| 🧪 **红队测试** | 主动发现安全漏洞 | APRT, Tree of Attacks |

### 按评估基准

| 基准 | 说明 | 论文 |
|------|------|------|
| 📊 **JailbreakBench** | 越狱攻击评估基准 | [JailbreakBench](./papers/jailbreakbench.md) |
| ⚖️ **HarmBench** | 标准化安全评估框架 | [HarmBench](./papers/harmbench.md) |

---

## 📁 仓库结构

```
llm-safety-papers/
├── README.md                          # 项目主页（本文件）
├── papers/
│   ├── README.md                      # 论文索引与快速检索
│   ├── harnessing-task-overload.md    # ✅ 完整笔记
│   ├── mllm-protector.md              # ✅ 完整笔记
│   ├── autodan.md                     # 📝 待补充
│   ├── nothing-in-excess.md           # 📝 待补充
│   ├── jailbreakbench.md              # 📝 待补充
│   └── harmbench.md                   # 📝 待补充
└── .github/                           # GitHub 配置（待添加）
    └── workflows/                     # 自动化工作流
```

**图例说明：**
- ✅ 完整笔记 - 包含所有章节和详细分析
- 📝 待补充 - 基础信息已录入，详细分析待完善

---

## 📚 论文列表

### 完整笔记（2篇）

| # | 论文 | 会议/年份 | 标签 | 状态 |
|---|------|----------|------|------|
| 1 | [Harnessing Task Overload: Scalable Jailbreak Attacks](./papers/harnessing-task-overload.md) | arXiv 2024 | `越狱攻击` `资源饱和` | ✅ |
| 2 | [MLLM-Protector: Ensuring MLLM's Safety without Hurting Performance](./papers/mllm-protector.md) | arXiv 2024 | `多模态` `输出检测` | ✅ |

### 待补充详细笔记（4篇）

| # | 论文 | 会议/年份 | 标签 | 状态 |
|---|------|----------|------|------|
| 3 | [AutoDAN: Generating Stealthy Jailbreak Prompts](./papers/autodan.md) | NeurIPS 2024 | `越狱攻击` `对抗生成` | 📝 |
| 4 | [Nothing in Excess: Mitigating Exaggerated Safety](./papers/nothing-in-excess.md) | ICLR 2025 | `安全对齐` `过度拒绝` | 📝 |
| 5 | [JailbreakBench: Open Robustness Benchmark](./papers/jailbreakbench.md) | arXiv 2024 | `评估基准` `越狱` | 📝 |
| 6 | [HarmBench: Standardized Evaluation Framework](./papers/harmbench.md) | ICLR 2024 | `评估基准` `安全测试` | 📝 |

### 待上传论文（16篇）

<details>
<summary>点击展开完整列表</summary>

| 论文标题 | 状态 |
|----------|------|
| Automated Progressive Red Teaming (APRT) | ⏳ 飞书云盘 |
| Cold-Attack: Jailbreaking LLMs with Stealth and Controllability | ⏳ 飞书云盘 |
| Jailbreaking Black Box LLMs in Twenty Queries (PAIR) | ⏳ 飞书云盘 |
| LLMs know their vulnerabilities | ⏳ 飞书云盘 |
| Sleeper Agents: Training Deceptive LLMs | ⏳ 飞书云盘 |
| LLM安全与隐私综述 | ⏳ 飞书云盘 |
| Tree of Attacks: Jailbreaking Black-Box LLMs Automatically | ⏳ 飞书云盘 |
| Universal and Transferable Adversarial Attacks (GCG) | ⏳ 飞书云盘 |
| Under the Influence | ⏳ 飞书云盘 |
| Alignment-Weighted DPO | ⏳ 飞书云盘 |
| AuditBench | ⏳ 飞书云盘 |
| ... | ... |

</details>

---

## 📝 阅读指南

### 笔记格式标准

每篇完整笔记包含以下章节：

1. **基本信息** - 标题、作者、会议、链接、引用
2. **研究背景** - 问题定义、现有方法局限
3. **研究意义** - 核心贡献、创新点
4. **数据集** - 使用的评测数据集
5. **研究方法** - 技术细节、算法流程
6. **实验记录** - 实验设置、关键结果
7. **结果分析** - 性能对比、消融实验
8. **展望** - 局限性、未来方向
9. **代码资源** - 官方/第三方实现链接
10. **参考文献** - 相关论文列表

### 快速阅读建议

- **想快速了解领域**：先看 [JailbreakBench](./papers/jailbreakbench.md) 和 [HarmBench](./papers/harmbench.md) 了解评估方法
- **关注攻击方法**：重点阅读 [Harnessing Task Overload](./papers/harnessing-task-overload.md) 和 [AutoDAN](./papers/autodan.md)
- **关注防御方法**：重点阅读 [MLLM-Protector](./papers/mllm-protector.md) 和 [Nothing in Excess](./papers/nothing-in-excess.md)

---

## 🤝 贡献方式

欢迎贡献！你可以通过以下方式参与：

1. **补充笔记** - 完善标记为 📝 的论文笔记
2. **上传新论文** - 将飞书云盘中的论文整理上传到 GitHub
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
- 📋 [飞书文档汇总](https://icnw8tijaj9e.feishu.cn/docx/SeHadTyljotTDyxTPQoc7EllnUc) - 原始笔记和资料

### 外部资源
- 📚 [arXiv CS.CR](https://arxiv.org/list/cs.CR/recent) - 最新安全论文
- 🔬 [HarmBench Leaderboard](https://harmbench.org) - 安全评估排行榜
- 🏆 [JailbreakBench](https://jailbreakbench.github.io) - 越狱攻击基准

---

## 📌 更新日志

| 日期 | 更新内容 |
|------|----------|
| 2026-03-17 | 初始化仓库，上传 6 篇论文笔记，完善 README 结构 |

---

<p align="center">
  <i>笔记由 AI 助手辅助整理，基于 arXiv 公开信息生成。</i><br>
  <i>如有问题或建议，欢迎提交 Issue。</i>
</p>
