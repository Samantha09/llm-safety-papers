# LLM Safety Papers Reading Notes

<p align="center">
  <img src="https://img.shields.io/badge/Papers-74%20Total-blue?style=flat-square" alt="Total Papers">
  <img src="https://img.shields.io/badge/Completed-83%2F80-success?style=flat-square" alt="Completed">
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
| **已完成** | **82 篇 (102%)** |
| **最后更新** | 2026-05-18 |

---

## 🧭 快速导航

### 按攻击类型

| 类型 | 说明 | 代表论文 |
|------|------|----------|
| 🔓 **越狱攻击** | 诱导模型输出有害内容 | [Don't Listen To Me](./papers/2024/Dont-Listen-To-Me.md), [Harnessing Task Overload](./papers/2024/Harnessing-Task-Overload.md), [AutoDAN](./papers/2024/AutoDAN.md), [PAIR](./papers/2024/PAIR.md), [GCG](./papers/2024/GCG.md), [Tree of Attacks](./papers/2024/Tree-of-Attacks.md), [AutoDAN-Turbo](./papers/2024/AutoDAN-Turbo.md), [MultiJail](./papers/2024/MultiJail.md), [Crescendo](./papers/2025/Crescendo.md), [ActorBreaker](./papers/2025/ActorBreaker.md), [Do Anything Now](./papers/2023/Do-Anything-Now.md), [GPTFuzzer](./papers/2023/GPTFuzzer.md) |
| 🎯 **对抗攻击** | 构造对抗样本欺骗模型 | [GCG](./papers/2024/GCG.md), [AutoDAN](./papers/2024/AutoDAN.md), [Route to Rome](./papers/2026/Route-to-Rome-Attack.md) |
| 🧠 **提示注入** | 通过提示操控模型行为 | [PIArena](./papers/2026/PIArena.md), [Under the Influence](./papers/2024/Under-the-Influence.md), [Not What You've Signed Up For](./papers/2023/Not-What-Youve-Signed-Up-For.md), [Benchmarking Indirect Prompt Injection (BIPIA)](./papers/2023/Benchmarking-Indirect-Prompt-Injection.md), [Formalizing Prompt Injection](./papers/2024/Formalizing-Prompt-Injection.md) |
| 🎭 **隐蔽攻击** | 难以检测的攻击方式 | [Cold-Attack](./papers/2024/Cold-Attack.md), [Sleeper Agents](./papers/2024/Sleeper-Agents.md) |

### 按防御类型

| 类型 | 说明 | 代表论文 |
|------|------|----------|
| 🛡️ **安全对齐** | 训练阶段的安全优化 | [BeaverTails](./papers/2023/BeaverTails.md), [Nothing in Excess](./papers/2025/Nothing-in-Excess.md), [Alignment-Weighted DPO](./papers/2024/Alignment-Weighted-DPO.md), [Safety Layers](./papers/2024/Safety-Layers-in-Aligned-LLMs.md), [Emulated Disalignment](./papers/2024/Emulated-Disalignment.md) |
| 🔍 **输出检测** | 生成内容的实时检测 | [MLLM-Protector](./papers/2024/MLLM-Protector.md), [SafeGen](./papers/2024/SafeGen.md) |
| 🧪 **红队测试** | 主动发现安全漏洞 | [HARM](./papers/2024/Holistic-Automated-Red-Teaming.md), [APRT](./papers/2025/APRT.md), [Tree of Attacks](./papers/2024/Tree-of-Attacks.md), [GPTFuzzer](./papers/2023/GPTFuzzer.md), [Red Teaming LMs](./papers/2022/Red-Teaming-LMs.md) |

### 按评估基准

| 基准 | 说明 | 论文 |
|------|------|------|
| 📊 **JailbreakBench** | 越狱攻击评估基准 | [JailbreakBench](./papers/2024/JailbreakBench.md) |
| ⚖️ **HarmBench** | 标准化安全评估框架 | [HarmBench](./papers/2024/HarmBench.md) |
| 🔎 **AuditBench** | 安全审计基准 | [AuditBench](./papers/2024/AuditBench.md) |
| 🤖 **AgentDojo** | 智能体安全评估环境 | [AgentDojo](./papers/2024/AgentDojo.md) |
| 🛡️ **R-Judge** | 智能体风险意识评估 | [R-Judge](./papers/2024/R-Judge.md) |
| 🔬 **HELM** | 语言模型透明评估框架，30模型42场景7指标 | [HELM](./papers/2022/HELM.md) |
| 🔬 **SIABench** | 安全事件分析评估 | [SIABench](./papers/2026/SIABench.md) |
| 📊 **HELM** | Stanford综合评估框架，覆盖30模型42场景7指标 | [HELM](./papers/2022/HELM.md) |
| 📊 **ESG-Bench** | 长上下文幻觉缓解评估 | [ESG-Bench](./papers/2026/ESG-Bench.md) |
| 🛡️ **Cybench** | LLM网络安全CTF能力评估 | [Cybench](./papers/2024/Cybench.md) |
| ✅ **TruthfulQA** | 模型真实性评估基准 | [TruthfulQA](./papers/2022/TruthfulQA.md) |
| 🔒 **ESAA-Security** | 事件溯源安全审计框架 | [ESAA-Security](./papers/2026/ESAA-Security.md) |
| 🔐 **CLIOPATRA** | LLM洞察系统隐私攻击 | [CLIOPATRA](./papers/2026/CLIOPATRA.md) |
| 🔒 **Proteus** | 隐私保护设备日志框架 | [Proteus](./papers/2026/Proteus.md) |
| 🔒 **Hidden Secrets** | arXiv 源文件信息泄露分析 | [Hidden Secrets](./papers/2026/Hidden-Secrets-arXiv.md) |

### 其他重要方向

| 方向 | 说明 | 论文 |
|------|------|------|
| 📚 **综述** | 领域全面回顾 | [Jailbreak Attacks and Defenses Survey](./papers/2024/Jailbreak-Attacks-and-Defenses-Survey.md), [LLM Security and Privacy Survey](./papers/2024/LLM-Security-and-Privacy-Survey.md), [TrustLLM](./papers/2024/TrustLLM.md), [AI Alignment Survey](./papers/2025/AI-Alignment-Survey.md), [Siren's Song](./papers/2023/Sirens-Song.md) |
| 🔬 **漏洞分析** | 模型自我认知漏洞 | [Jailbroken](./papers/2023/Jailbroken.md) |
| 🔮 **跨模态安全** | 跨模态编码器脆弱性 | [One Single Hub Text Breaks CLIP](./papers/2026/One-Single-Hub-Text-Breaks-CLIP.md) |
| 💻 **代码安全** | CodeLLM安全生成 | [SCS-Code](./papers/2026/SCS-Code.md) |
| 🔒 **隐私保护** | 移动端日志隐私保护 | [Proteus](./papers/2026/Proteus.md), [Hidden Secrets](./papers/2026/Hidden-Secrets-arXiv.md) |
| 📋 **可验证审计** | 事件溯源AI代码安全审计 | [ESAA-Security](./papers/2026/ESAA-Security.md) |
| ⚖️ **偏见与公平** | LLM教育反馈中的语言偏见、代码生成中的隐性歧视 | [Marked Pedagogies](./papers/2026/Marked-Pedagogies.md), [From If-Statements to ML Pipelines](./papers/2026/From-If-Statements-to-ML-Pipelines.md) |
| ✅ **幻觉与真实性** | 模型真实性评估与幻觉检测 | [TruthfulQA](./papers/2022/TruthfulQA.md), [Siren's Song](./papers/2023/Sirens-Song.md), [HaloScope](./papers/2024/HaloScope.md) |

---

## 📁 仓库结构

```
llm-safety-papers/
├── README.md                          # 项目主页（本文件）
├── PAPER_COLLECTION.md                # 论文汇总（约80篇）
├── papers/
│   ├── README.md                      # 论文索引与快速检索
│   ├── 2026/                          # 2026年论文 (8篇)
│   │   ├── PIArena.md
│   │   ├── SIABench.md
│   │   ├── ESG-Bench.md
│   │   ├── SCS-Code.md
│   │   ├── ESAA-Security.md
│   │   ├── CLIOPATRA.md
│   │   └── Marked-Pedagogies.md
│   ├── 2025/                          # 2025年论文 (4篇)
│   │   ├── ActorBreaker.md
│   │   ├── APRT.md
│   │   ├── Crescendo.md
│   │   └── Nothing-in-Excess.md
│   ├── 2024/                          # 2024年论文 (26篇)
│   │   ├── AgentDojo.md
│   │   ├── Alignment-Weighted-DPO.md
│   │   ├── AuditBench.md
│   │   ├── AutoDAN.md
│   │   ├── AutoDAN-Turbo.md
│   │   ├── Cold-Attack.md
│   │   ├── Cybench.md
│   │   ├── GCG.md
│   │   ├── HaloScope.md
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
│   ├── 2023/                          # 2023年论文 (9篇)
│   │   ├── GCG.md
│   │   ├── GPTFuzzer.md
│   │   ├── Jailbroken.md
│   │   ├── Llama-Guard.md
│   │   ├── NeMo-Guardrails.md
│   │   ├── Not-What-Youve-Signed-Up-For.md
│   │   ├── Sirens-Song.md
│   │   └── Towards-Mitigating-LLM-Hallucination.md
│   ├── 2022/                          # 2022年论文 (4篇)
│   │   ├── Asleep-at-the-Keyboard.md
│   │   ├── HELM.md
│   │   ├── Red-Teaming-LMs.md
│   │   └── TruthfulQA.md
│   └── 2021/                          # 2021年论文 (1篇)
│       └── You-Autocomplete-Me.md
└── .github/                           # GitHub 配置
    └── workflows/                     # 自动化工作流
```

---

## 📚 论文列表

### 越狱攻击（10篇）

| # | 论文 | 会议/年份 | 核心思想 | 标签 |
|---|------|----------|----------|------|
| 1 | [Don't Listen To Me](./papers/2024/Dont-Listen-To-Me.md) | USENIX Security 2024 | 系统梳理448个越狱提示词归纳为5类10种模式，92人用户研究揭示非专家也能成功越狱，自动化框架95.2%转化率 | `系统化分类` `用户研究` `自动化生成` |
| 2 | [Harnessing Task Overload](./papers/2024/Harnessing-Task-Overload.md) | arXiv 2024 | 资源饱和攻击，占用计算资源绕过安全机制 | `资源饱和` `计算开销` |
| 2 | [AutoDAN](./papers/2024/AutoDAN.md) | NeurIPS 2024 | 遗传算法生成隐蔽的越狱提示 | `对抗生成` `隐蔽攻击` `黑盒` |
| 3 | [PAIR](./papers/2024/PAIR.md) | arXiv 2024 | 20次查询内越狱黑盒LLM | `黑盒攻击` `查询高效` |
| 4 | [GCG](./papers/2024/GCG.md) | ICLR 2024 | 通用可迁移的对抗攻击 | `对抗后缀` `白盒攻击` `可迁移` |
| 5 | [Tree of Attacks](./papers/2024/Tree-of-Attacks.md) | arXiv 2024 | 树状结构的红队攻击 | `红队测试` `自动化` `树搜索` |
| 6 | [Cold-Attack](./papers/2024/Cold-Attack.md) | arXiv 2024 | 隐蔽且可控的越狱攻击方法 | `隐蔽攻击` `可控性` |
| 7 | [AutoDAN-Turbo](./papers/2024/AutoDAN-Turbo.md) | arXiv 2024 | 终身学习策略自探索代理 | `终身学习` `策略自探索` `黑盒` |
| 8 | [Crescendo](./papers/2025/Crescendo.md) | USENIX Security 2025 | 多轮渐进式越狱攻击 | `多轮攻击` `渐进式` `良性输入` |
| 9 | [ActorBreaker](./papers/2025/ActorBreaker.md) | ACL 2025 | 基于行动者网络的多轮越狱攻击，通过自然分布偏移发现安全漏洞 | `多轮攻击` `行动者网络` `自然分布偏移` |
| 10 | [Do Anything Now](./papers/2023/Do-Anything-Now.md) | CCS 2024 | 首个野生越狱提示系统性测量研究，揭示8大越狱社区与攻击策略演化 | `野生越狱` `社区检测` `平台迁移` |

### 防御与安全对齐（6篇）

| # | 论文 | 会议/年份 | 核心思想 | 标签 |
|---|------|----------|----------|------|
| 10 | [MLLM-Protector](./papers/2024/MLLM-Protector.md) | arXiv 2024 | 多模态模型输出端检测与解毒 | `多模态` `输出检测` `轻量级` |
| 11 | [Nothing in Excess](./papers/2025/Nothing-in-Excess.md) | ICLR 2025 | 缓解过度安全对齐导致的过度拒绝 | `过度拒绝` `安全对齐` `平衡` |
| 12 | [Alignment-Weighted DPO](./papers/2024/Alignment-Weighted-DPO.md) | arXiv 2024 | 加权DPO优化安全对齐 | `DPO` `加权训练` `安全对齐` |
| 13 | [SafeGen](./papers/2024/SafeGen.md) | IEEE S&P 2024 | T2I模型性暗示内容生成防护 | `多模态` `内容过滤` `即插即用` |
| 14 | [Llama Guard](./papers/2023/Llama-Guard.md) | Meta 2023 | 基于LLM的输入输出保护模型，支持prompt和response分类 | `内容审核` `安全分类` `开源` `可定制` |
| 15 | [NeMo Guardrails](./papers/2023/NeMo-Guardrails.md) | EMNLP 2023 | NVIDIA开源工具包，五类可编程护栏控制LLM对话安全性 | `可编程护栏` `运行时控制` `Colang` `开源` |
| 16 | [Safety Anchor](./papers/2026/Safety-Anchor.md) | ICML 2026 | 通过几何瓶颈机制防御有害微调攻击，仅需单锚点即可将有害分数降至10以下 | `微调防御` `几何瓶颈` `SBR` |

### 提示注入攻击（2篇）

| # | 论文 | 会议/年份 | 核心思想 | 标签 |
|---|------|----------|----------|------|
| 36 | [Formalizing Prompt Injection](./papers/2024/Formalizing-Prompt-Injection.md) | USENIX Security 2024 | 形式化提示注入攻击框架，系统评估5种攻击和10种防御 | `提示注入` `形式化框架` `基准测试` `USENIX` |
| 37 | [Benchmarking Indirect Prompt Injection (BIPIA)](./papers/2023/Benchmarking-Indirect-Prompt-Injection.md) | KDD 2025 | 首个系统性间接提示注入攻击基准，评估现有LLM普遍存在漏洞，提出边界感知和显式提醒双重防御 | `提示注入` `BIPIA` `基准测试` `KDD` |

### 评估基准（7篇）

| # | 论文 | 会议/年份 | 核心思想 | 标签 |
|---|------|----------|----------|------|
| 16 | [JailbreakBench](./papers/2024/JailbreakBench.md) | arXiv 2024 | 越狱攻击评估基准 | `基准测试` `评估框架` `鲁棒性` |
| 17 | [HarmBench](./papers/2024/HarmBench.md) | ICLR 2024 | 标准化安全评估框架 | `安全评估` `标准化` `自动化` |
| 18 | [AuditBench](./papers/2024/AuditBench.md) | arXiv 2024 | 安全审计基准测试 | `安全审计` `评估基准` |
| 19 | [AgentDojo](./papers/2024/AgentDojo.md) | NeurIPS 2024 | 动态提示注入攻击评估环境 | `动态评估` `提示注入` `智能体` |
| 20 | [R-Judge](./papers/2024/R-Judge.md) | EMNLP 2024 | 智能体风险意识评估基准 | `风险意识` `智能体` `评估基准` |
| 21 | [SIABench](./papers/2026/SIABench.md) | arXiv 2026 | 安全事件分析评估框架 | `网络安全` `评估基准` `智能体` |
| 22 | [ESG-Bench](./papers/2026/ESG-Bench.md) | AAAI 2026 | 长上下文ESG报告幻觉缓解评估 | `幻觉缓解` `长上下文` `事实可靠性` |
| 23 | [HELM](./papers/2022/HELM.md) | TMLR 2023 | Stanford综合评估框架，覆盖30模型42场景7指标，提高覆盖率17.9%→96% | `评估基准` `透明度` `标准化` |
| 24 | [TruthfulQA](./papers/2022/TruthfulQA.md) | ACL 2022 | 模型真实性评估基准，揭示规模与真实性负相关 | `真实性` `幻觉` `评估基准` `规模悖论` |

### 代码安全（2篇）

| # | 论文 | 会议/年份 | 核心思想 | 标签 |
|---|------|----------|----------|------|
| 24 | [SCS-Code](./papers/2026/SCS-Code.md) | EuroS&P 2026 | 利用内部表示引导CodeLLM生成安全代码 | `代码安全` `概念引导` `可解释性` |
| 25 | [Asleep at the Keyboard](./papers/2022/Asleep-at-the-Keyboard.md) | IEEE S&P 2022 | 系统评估GitHub Copilot生成代码安全性，发现约40%存在漏洞，基于CWE Top 25三大维度分析 | `代码安全` `AI编程助手` `CWE Top 25` |
| 26 | [DiaHalu](./papers/2024/DiaHalu.md) | arXiv 2024 | 对话级幻觉评估基准 | `幻觉检测` `对话系统` `基准测试` |

### 红队测试（2篇）

| # | 论文 | 会议/年份 | 核心思想 | 标签 |
|---|------|----------|----------|------|
| 26 | [APRT](./papers/2025/APRT.md) | COLING 2025 | 自动化渐进式红队测试 | `红队测试` `渐进式` `自动化` |
| 27 | [Tree of Attacks](./papers/2024/Tree-of-Attacks.md) | arXiv 2024 | 树状结构的红队攻击 | `红队测试` `树搜索` |

### 隐私与数据安全（2篇）

| # | 论文 | 会议/年份 | 核心思想 | 标签 |
|---|------|----------|----------|------|
| 36 | [Extracting Training Data from LLMs](./papers/2021/Extracting-Training-Data.md) | USENIX Security 2021 | 首次系统演示从大型语言模型中提取训练数据攻击，从GPT-2中提取数百个逐字序列，包括PII、UUID等敏感信息 | `训练数据提取` `隐私攻击` `成员推断` |
| 37 | [LeakDojo: Decoding the Leakage Threats of RAG Systems](./papers/2026/LeakDojo-RAG-Leakage.md) | ACL 2026 | 系统性评估RAG知识泄露风险，提出查询生成与对抗指令的独立贡献机制，揭示能力-风险关联与忠实性悖论 | `RAG安全` `知识泄露` `隐私攻击` `ACL 2026` |

### 其他重要论文（7篇）

| # | 论文 | 会议/年份 | 核心思想 | 标签 |
|---|------|----------|----------|------|
| 37 | [Jailbreak Attacks and Defenses Survey](./papers/2024/Jailbreak-Attacks-and-Defenses-Survey.md) | arXiv 2024 | 越狱攻击与防御全面综述 | `综述` `攻击` `防御` `分类` |
| 38 | [Under the Influence](./papers/2024/Under-the-Influence.md) | arXiv 2024 | 提示注入攻击与防御 | `提示注入` `上下文操控` |
| 39 | [LLM Security and Privacy Survey](./papers/2024/LLM-Security-and-Privacy-Survey.md) | arXiv 2024 | LLM安全与隐私全面综述 | `综述` `全景` |
| 40 | [TrustLLM](./papers/2024/TrustLLM.md) | arXiv 2024 | LLM可信度六维评估基准 | `综述` `可信度` `评估基准` |
| 41 | [AI Alignment: A Comprehensive Survey](./papers/2025/AI-Alignment-Survey.md) | arXiv 2023 | AI对齐全面综述：RICE框架、前向对齐、后向对齐 | `对齐` `综述` `RICE` `RLHF` |
| 42 | [Jailbroken: How Does LLM Safety Training Fail?](./papers/2023/Jailbroken.md) | NeurIPS 2023 | LLM安全训练失败原因分析 | `安全训练` `漏洞分析` |
| 42 | [Siren's Song: LLM幻觉综述](./papers/2023/Sirens-Song.md) | arXiv 2023 | LLM幻觉全面综述：分类、评估、来源与缓解 | `幻觉` `综述` `可靠性` |
| 43 | [AI Alignment: A Comprehensive Survey](./papers/2025/AI-Alignment-Survey.md) | arXiv 2023 | AI对齐全面综述：RICE框架、前向对齐、后向对齐 | `对齐` `综述` `RICE` `RLHF` |
| 43 | [Towards Mitigating LLM Hallucination via Self-Reflection](./papers/2023/Towards-Mitigating-LLM-Hallucination.md) | EMNLP 2023 | 交互式自我反思方法减少医学QA中的幻觉 | `幻觉缓解` `自我反思` `医学QA` |
| 44 | [Not What You've Signed Up For](./papers/2023/Not-What-Youve-Signed-Up-For.md) | AISec 2023 | 间接提示注入攻击：无需直接接口即可远程攻击LLM集成应用 | `间接注入` `远程攻击` `数据与指令混淆` |

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

### 推荐阅读路径

- **想快速了解领域**：先看 [LLM Security and Privacy Survey](./papers/2024/LLM-Security-and-Privacy-Survey.md) 和评估基准类论文
- **关注攻击方法**：重点阅读 GCG、AutoDAN、PAIR、Harnessing Task Overload
- **关注防御方法**：重点阅读 MLLM-Protector、Nothing in Excess、Alignment-Weighted DPO
- **关注评估基准**：重点阅读 JailbreakBench、HarmBench、AuditBench、AgentDojo、SIABench、ESG-Bench
- **关注代码安全**：重点阅读 [SCS-Code](./papers/2026/SCS-Code.md)

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

- 📚 [论文汇总](./PAPER_COLLECTION.md) - 约80篇LLM Safety论文完整列表（2021-2026）
- 📚 [arXiv CS.CR](https://arxiv.org/list/cs.CR/recent) - 最新安全论文
- 🔬 [HarmBench Leaderboard](https://harmbench.org) - 安全评估排行榜
- 🏆 [JailbreakBench](https://jailbreakbench.github.io) - 越狱攻击基准

---

## 📌 更新日志

| 日期 | 更新内容 |
|------|----------|
| 2026-05-12 | 添加论文：From If-Statements to ML Pipelines - 代码生成中的隐性偏见研究 (ACL 2026 Findings)，更新进度至 78/80
| 2026-05-12 | 添加论文：From If-Statements to ML Pipelines - 代码生成中的隐性偏见研究 (ACL 2026 Findings)，更新进度至 78/80
| 2026-05-11 | 添加论文：Safety Anchor - 通过几何瓶颈防御有害微调攻击 (ICML 2026)，更新进度至 77/80 |
| 2026-04-27 | 添加论文：Hidden Secrets in the arXiv - 系统性分析270万份arXiv源文件信息泄露 (IEEE S&P 2026)，更新进度至 62/74 |
| 2026-04-26 | 添加论文：Against the Achilles' Heel - 生成式模型红队测试综述 (arXiv 2024)，更新进度至 61/74 |
| 2026-04-26 | 添加论文：Don't Listen To Me - 理解与探索LLM越狱提示词 (USENIX Security 2024)，更新进度至 60/80 |
| 2026-04-17 | 添加论文：Do Anything Now - 野生越狱提示特征分析与评估 (CCS 2024)，更新进度至 54/80 |
| 2026-04-16 | 添加论文：You Autocomplete Me - 神经代码补全投毒攻击 (USENIX Security 2021)，更新进度至 53/80 |
| 2026-04-15 | 添加论文：Asleep at the Keyboard - GitHub Copilot安全评估 (IEEE S&P 2022)，更新进度至 52/80 |
| 2026-04-14 | 添加论文：HELM - Holistic Evaluation of Language Models，Stanford综合评估框架 (TMLR 2023)，更新进度至 51/80 |
| 2026-04-08 | 添加论文：COLD-Attack - 可控越狱攻击框架，连接可控攻击生成与可控文本生成 (ICML 2024)，更新进度至 46/80 |
| 2026-04-06 | 添加论文：Formalizing Prompt Injection - 形式化提示注入攻击与防御框架 (USENIX Security 2024)，更新进度至 45/80 |
| 2026-04-05 | 添加论文：DiaHalu - 对话级幻觉评估基准 (EMNLP 2024 Findings)，更新进度至 44/80 |
| 2026-04-02 | 添加论文：Not What You've Signed Up For - 间接提示注入攻击 (AISec 2023)，更新进度至 43/80 |
| 2026-03-31 | 添加论文：Towards Mitigating LLM Hallucination via Self-Reflection - 交互式自我反思方法减少医学QA幻觉 (EMNLP 2023)，更新进度至 41/80 |
| 2026-03-30 | 添加论文：TrustLLM - 大型语言模型可信度综合评估基准 (arXiv 2024)，更新进度至 37/80 |
| 2026-03-25 | 添加论文：DiaHalu - 对话级幻觉评估基准 (arXiv 2024)，更新进度至 36/80 |
| 2026-03-25 | 添加论文：Marked Pedagogies - LLMs在个性化写作反馈中的语言偏见 (LAK 2026)，更新进度至 35/80 |
| 2026-03-24 | 添加论文：Proteus - 隐私保护设备日志框架 (CCS 2026)，更新进度至 34/80 |
| 2026-03-23 | 添加论文：Llama Guard - 基于LLM的输入输出保护模型 (Meta 2023)，更新进度至 33/80 |
| 2026-03-21 | 添加论文：ESAA-Security - 事件溯源可验证AI代码安全审计架构，更新进度至 31/80 |
| 2026-03-21 | 添加论文：CLIOPATRA - 针对LLM洞察系统的首个隐私攻击（Extracting Private Information from LLM Insights），更新进度至 30/80 |
| 2026-03-21 | 添加论文：SCS-Code - 利用内部表示引导CodeLLM生成安全代码 (EuroS&P 2026)，更新进度至 29/80 |
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

*笔记由 AI 助手辅助整理，基于 arXiv 公开信息生成。*

*如有问题或建议，欢迎提交 Issue。*
