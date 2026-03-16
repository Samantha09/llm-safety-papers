# LLM Security and Privacy Survey

> **论文笔记**: LLM-Safety-Survey
> **来源**: 飞书文档
> **上传时间**: 2026-03-17 00:59:38

---

## 基本信息

- **论文标题**: A Survey on Large Language Model (LLM) Security and Privacy: The Good, the Bad, and the Ugly
- **作者**: Yifan Yao, Jinhao Duan, Kaidi Xu, Yuanfang Cai, Zhibo Sun, Yue Zhang
- **机构**: Drexel University
- **arXiv**: 2312.02003v3

## 核心框架

论文将LLM安全隐私研究分为三个方面：

### The Good (正面应用)

LLM在安全领域的积极应用：
- **漏洞检测**: GPT-3在代码仓库中发现213个安全漏洞（仅4个误报）
- **测试生成**: 比传统方法提升36.8%覆盖率
- **恶意软件检测**: 准确率87.19%，每秒539次预测

### The Bad (攻击性应用)

LLM被滥用的风险：
- **数据投毒** (Data Poisoning)
- **后门攻击** (Backdoor Attacks)
- **训练数据提取** (Training Data Extraction)
- **网络钓鱼** (网络级攻击)
- **恶意软件创建** (软件级攻击)

### The Ugly (自身漏洞)

LLM自身的安全漏洞：
- **提示注入** (Prompt Injection)
- **越狱攻击** (Jailbreak Attacks)
- **模型提取** (Model Extraction)
- **参数提取** (Parameter Extraction)
- **侧信道攻击** (硬件级攻击)

## 关键发现

### 文献统计发现

- 共分析281篇文献
- 大多数研究倾向于使用LLM增强安全（漏洞检测、测试生成）
- 用户级攻击最普遍（32篇）：虚假信息、社会工程、学术不端

### 代码/数据安全实验对比

| 发现 | 结果 |
|------|------|
| 与SOTA方法对比 | 17/25的研究认为LLM方法更优 |
| 漏洞检测 | 检测能力是传统工具的4倍 |
| 代码覆盖率 | 比之前SOTA平均提升36.8% |

## 研究局限性

- 理论到实践的转化：模型提取等攻击仍停留在理论阶段
- LLM与操作系统/硬件的深度集成可能带来新的安全威胁
- 安全指令微调作为新兴领域需要更多研究

## 未来研究方向

1. 安全指令微调的深入探索
2. 防御机制强化（针对提示注入和越狱攻击）
3. LLM与操作系统/硬件深度集成的安全研究
4. 模型架构对安全的影响研究

## 结论

- **LLM对安全隐私的净贡献是正面的** (Good > Bad)
- 展示了LLM在防御端的巨大潜力
- 揭示了自身存在的脆弱性
- 警示了其被滥用的风险
