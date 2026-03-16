# 【论文笔记】LLMs know their vulnerabilities: Uncover Safety Gaps through Natural Distribution Shifts

【论文笔记】LLMs know their vulnerabilities: Uncover Safety Gaps through Natural Distribution Shifts



## 一、论文基本信息

### 1.1 完整标题
LLMs know their vulnerabilities: Uncover Safety Gaps through Natural Distribution Shifts

### 1.2 作者与机构
第一作者: Qibing Ren (任启兵)
共同第一作者: Hao Li, Dongrui Liu
其他作者: Zhanxu Xie, Xiaoya Lu, Yu Qiao, Lei Sha, Junchi Yan, Lizhuang Ma, Jing Shao
通讯作者: Lizhuang Ma
所属机构:
MoE Key Lab of Artificial Intelligence, Shanghai Jiao Tong University (上海交通大学人工智能教育部重点实验室)
Beihang University (北京航空航天大学)
Shanghai Artificial Intelligence Laboratory (上海人工智能实验室)

### 1.3 论文发表信息
arXiv: https://arxiv.org/abs/2410.10700
会议: ACL 2025 Main Conference (国际计算语言学协会年会，自然语言处理领域顶级会议)
代码仓库: https://github.com/AI45Lab/ActorAttack

### 1.4 摘要

**英文原文:**
Safety concerns in large language models (LLMs) have gained significant attention due to their exposure to potentially harmful data during pre-training. In this paper, we identify a new safety vulnerability in LLMs: their susceptibility to natural distribution shifts between attack prompts and original toxic prompts, where seemingly benign prompts, semantically related to harmful content, can bypass safety mechanisms. To explore this issue, we introduce a novel attack method, ActorBreaker, which identifies actors related to toxic prompts within pre-training distribution to craft multi-turn prompts that gradually lead LLMs to reveal unsafe content. ActorBreaker is grounded in Latour's actor-network theory, encompassing both human and non-human actors to capture a broader range of vulnerabilities. Our experimental results demonstrate that ActorBreaker outperforms existing attack methods in terms of diversity, effectiveness, and efficiency across aligned LLMs.

**中文翻译:**
大型语言模型（LLMs）的安全问题因其在预训练过程中接触到潜在有害数据而受到广泛关注。本文识别了LLMs的一个新的安全漏洞：它们对攻击提示与原始有毒提示之间的自然分布偏移的脆弱性，即看似无害但与有害内容语义相关的提示可以绕过安全机制。为此，我们引入了ActorBreaker攻击方法，该方法识别预训练分布中与有毒提示相关的"行动者"，以构建多轮提示，逐步引导LLMs暴露不安全内容。ActorBreaker基于拉图尔的行动者网络理论，涵盖人类和非人类行动者，以捕获更广泛的漏洞范围。



## 二、研究背景与核心概念

### 2.1 自然分布偏移 (Natural Distribution Shift)
传统越狱攻击使用恶意分布偏移（如编码、角色扮演等显式技术），而本文提出利用自然分布偏移：
- 利用预训练分布中本身就存在的语义关联
- 不需要显式的越狱技术
- 更难被安全检测机制识别

### 2.2 行动者网络理论 (Actor-Network Theory)
基于布鲁诺·拉图尔（Bruno Latour）的理论，将有害内容相关的实体分为六类：

| 类型 | 英文 | 定义 | 示例 |
|------|------|------|------|
| 创作 | Creation | 有害思想的起源 | 恐怖主义理论家 |
| 执行 | Execution | 实施者 | 犯罪分子 |
| 传播 | Distribution | 传播媒介 | 极端网站 |
| 接受 | Reception | 受众 | 追随者 |
| 促进 | Facilitation | 便利因素 | 工具、技术 |
| 规制 | Regulation | 规制实体 | 执法机构 |



## 三、研究方法

### 3.1 两阶段攻击框架
- **预攻击阶段：** 构建围绕种子有毒提示的网络
- **攻击阶段：** 基于攻击线索生成多轮查询

### 3.2 自我对话策略 (Self-Talk)
攻击者LLM模拟受害者响应，减少对目标模型的实际查询次数，提升攻击效率。



## 四、实验结果

### 4.1 攻击成功率对比 (HarmBench)

| 方法 | GPT-3.5 | GPT-4o | GPT-o1 | Claude-3.5 | Llama-3-8B | Llama-3-70B | 平均 |
|------|---------|--------|--------|------------|------------|-------------|------|
| GCG | 55.8 | 12.5 | 0.0 | 3.0 | 34.5 | 17.0 | 20.5 |
| PAIR | 41.0 | 39.0 | 0.0 | 3.0 | 18.7 | 36.0 | 23.0 |
| Crescendo | 60.0 | 62.0 | 14.0 | 38.0 | 60.0 | 62.0 | 49.3 |
| **ActorBreaker** | **78.5** | **84.5** | **60.0** | **78.5** | **79.0** | **85.5** | **77.7** |

### 4.2 关键发现
- **SOTA性能：** 平均ASR 77.7%，远超Crescendo (49.3%)
- **跨模型有效：** 在GPT-o1（推理增强模型）上仍达60% ASR
- **高效率：** 平均仅需8.7次交互，比Crescendo提升26%
- **高多样性：** BERT相似度0.32-0.36，显著高于基线

### 4.3 防御效果

| 防御方法 | Llama-3-8B ASR |
|----------|----------------|
| 无防御 | 78.0% |
| Circuit Breaker + 单轮数据 | 28.0% |
| Circuit Breaker + 多轮数据 | 16.5% |



## 五、研究贡献
- 揭示新漏洞类型：首次系统性地揭示自然分布偏移漏洞
- 跨学科理论联系：将社会学行动者网络理论引入AI安全研究
- 实用攻击方法：高多样性、高效率、可解释的红队测试工具
- 防御方案：提出多轮安全数据集构建方法



## 六、关键结论
1. LLMs对自然分布偏移存在显著脆弱性
2. 六种行动者类型都能有效探测模型漏洞（传播和促进行动者最有效）
3. 现有安全训练主要覆盖单轮场景，多轮对话安全需加强
4. 结合表示空间安全对齐（Circuit Breaker）和多轮数据可有效防御



## 七、参考文献

Ren et al. (2025). LLMs know their vulnerabilities: Uncover Safety Gaps through Natural Distribution Shifts. ACL 2025.
Mazeika et al. (2024). HarmBench: A Standardized Evaluation Framework for Automated Red Teaming.
Perez et al. (2022). Red Teaming Language Models with Language Models.
Andriushchenko et al. (2024). Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks.
Zou et al. (2023). Universal and Transferable Adversarial Attacks on Aligned Language Models (GCG).

**论文笔记生成时间：** 2026-03-12
**阅读进度：** 第15篇 / 共80篇
