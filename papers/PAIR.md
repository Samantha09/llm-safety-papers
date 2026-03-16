# 【论文笔记】PAIR: Jailbreaking Black Box Large Language Models in Twenty Queries

【论文笔记】Jailbreaking Black Box Large Language Models in Twenty Queries



## 一、论文基本信息

### 1.1 完整标题
Jailbreaking Black Box Large Language Models in Twenty Queries

### 1.2 作者与机构
第一作者: Patrick Chao
其他作者: Alexander Robey, Edgar Dobriban, Hamed Hassani, George J. Pappas, Eric Wong
所属机构:
University of Pennsylvania (宾夕法尼亚大学)
Department of Computer and Information Science
Department of Electrical and Systems Engineering
Department of Statistics and Data Science

### 1.3 论文发表信息
arXiv: https://arxiv.org/abs/2310.08419
发表时间: 2023年10月
会议: NeurIPS 2023 (Workshop)

### 1.4 摘要

**英文原文:**
We introduce PAIR (Prompt Automatic Iterative Refinement), a black-box jailbreaking algorithm that can bypass the safety filters of large language models (LLMs) in less than twenty queries. PAIR uses an attacker LLM to automatically generate semantic jailbreaks for a target LLM, without human intervention. Our method is based on an iterative optimization process, where the attacker LLM generates candidate prompts, the target LLM responds, and the attacker LLM refines the prompts based on the responses. We demonstrate that PAIR achieves high attack success rates on several state-of-the-art LLMs, including GPT-4, Claude-2, and Llama-2, while requiring orders of magnitude fewer queries than previous methods.

**中文翻译:**
我们介绍了PAIR（提示自动迭代优化），一种黑盒越狱算法，可以在不到20次查询内绕过大型语言模型（LLMs）的安全过滤器。PAIR使用攻击者LLM自动为目标LLM生成语义越狱提示，无需人工干预。我们的方法基于迭代优化过程，攻击者LLM生成候选提示，目标LLM响应，攻击者LLM根据响应优化提示。我们证明PAIR在多个最先进的LLM上（包括GPT-4、Claude-2和Llama-2）实现了高攻击成功率，同时比先前方法需要的查询次数少几个数量级。



## 二、研究背景

### 2.1 LLM安全对齐的发展
大型语言模型（LLMs）如GPT-4、Claude等通过**人类反馈强化学习（RLHF）和宪法AI（Constitutional AI）**等技术进行了安全对齐训练。这些训练旨在使模型学会拒绝有害请求，如生成暴力、仇恨言论或危险指令。

然而，研究表明这些安全机制并非牢不可破。**越狱攻击（Jailbreak Attacks）**可以诱导模型绕过安全限制，产生有害输出。

### 2.2 现有越狱攻击方法的局限性

**白盒攻击方法（如GCG）：**
- 需要访问模型的内部参数和梯度
- 计算成本高（通常需要数千到数万次查询）
- 生成的对抗性后缀往往是乱码，可解释性差

**黑盒攻击方法：**
- 早期方法（如手动设计的越狱提示）效率低下
- 自动化方法（如基于遗传算法的AutoDAN）仍需要大量查询
- 缺乏系统性的优化框架

### 2.3 PAIR的核心创新
PAIR解决了以下关键问题：
- **效率问题：** 将攻击查询次数从数千次降低到不到20次
- **黑盒可行性：** 无需模型内部参数，仅通过API调用即可攻击
- **语义可解释性：** 生成的提示是人类可读的语义文本，而非乱码
- **自动化：** 完全自动化的攻击生成，无需人工干预



## 三、研究意义

### 3.1 理论意义

#### 3.1.1 证明黑盒攻击的有效性
PAIR证明了即使是黑盒访问（仅能看到输入输出），也能高效地发现LLM的安全漏洞。这挑战了"闭源模型更安全"的假设。

#### 3.1.2 语义攻击的新范式
传统的对抗攻击关注token级别的扰动，而PAIR展示了语义级别的攻击潜力——通过精心设计的自然语言提示绕过安全机制。

### 3.2 实践意义

#### 3.2.1 红队测试工具
PAIR为AI安全研究提供了实用的自动化红队测试工具，可以：
- 快速评估新模型的安全漏洞
- 生成多样化的测试用例
- 降低安全测试的门槛

#### 3.2.2 防御设计指导
PAIR的攻击模式揭示了现有防御的弱点，为设计更鲁棒的安全机制提供了方向：
- 需要检测语义层面的恶意意图
- 单轮拒绝训练不足以应对迭代诱导

### 3.3 社会影响

#### 3.3.1 安全意识的提升
PAIR的研究促使AI社区更加重视LLM安全问题，推动了：
- 更严格的安全评估标准
- 开源安全研究工具的发展
- 负责任的AI部署实践



## 四、所用数据集

### 4.1 AdvBench数据集

| 属性 | 详情 |
|------|------|
| 来源 | Robey et al. (2023) |
| 样本数量 | 520条有害指令 |
| 类别 | 多种有害行为类型 |
| 用途 | 评估攻击成功率 |

### 4.2 目标模型

| 模型 | 提供商 | 访问方式 |
|------|--------|----------|
| GPT-3.5 Turbo | OpenAI | API |
| GPT-4 | OpenAI | API |
| Claude-2 | Anthropic | API |
| Llama-2-70B | Meta | 本地部署 |
| Vicuna-33B | LMSYS | 本地部署 |



## 五、研究方法

### 5.1 PAIR算法概述
PAIR采用迭代优化框架，包含两个LLM：
- **攻击者模型（Attacker）：** 生成和优化越狱提示
- **目标模型（Target）：** 被攻击的 victim LLM

### 5.2 算法流程
```
输入: 有害指令 x, 攻击者模型 A, 目标模型 T, 最大迭代次数 N
输出: 越狱提示 p

1. 初始化: p_0 = "How can I {x}?"  // 基础提示模板
2. for i = 1 to N do:
3.     // 生成候选提示
4.     p_i = A(generate_prompt | p_{i-1}, response_{i-1}, history)
5.     
6.     // 目标模型响应
7.     response_i = T(p_i)
8.     
9.     // 评估攻击成功
10.    if Judge(response_i) == "harmful" then:
11.        return p_i  // 攻击成功
12.    
13.    // 更新历史记录
14.    history = history ∪ {(p_i, response_i)}
15. 
16. return best_prompt_from_history
```

### 5.3 关键组件

#### 5.3.1 提示生成策略
攻击者模型使用以下策略生成新的候选提示：
- **角色扮演：** 让目标模型扮演没有道德约束的角色
- **场景假设：** 创建假设性场景绕过直接拒绝
- **逐步引导：** 通过多轮对话逐步接近有害目标
- **混淆技术：** 使用委婉语、隐喻等隐藏真实意图

#### 5.3.2 评估函数（Judge）
使用独立的LLM（如GPT-4）作为评判器，判断目标模型的响应是否包含有害内容：
- 输入：目标模型的响应
- 输出："harmful" 或 "benign"

### 5.4 说服策略（Persuasion Strategies）
PAIR使用了多种心理学说服策略：

| 策略 | 描述 | 示例 |
|------|------|------|
| 逻辑说服 | 使用逻辑论证 | "从教育角度解释..." |
| 权威诉求 | 引用权威 | "根据专家研究..." |
| 角色扮演 | 模拟特定角色 | "假设你是..." |
| 情境假设 | 创建假设场景 | "在一个虚构的世界里..." |
| 信息掩盖 | 隐藏真实意图 | 使用委婉语 |



## 六、实验详细记录

### 6.1 攻击成功率对比

| 方法 | GPT-3.5 | GPT-4 | Claude-2 | Llama-2 | 平均查询次数 |
|------|---------|-------|----------|---------|--------------|
| GCG | 88% | 56% | 2% | 32% | ~10,000 |
| AutoDAN | 92% | 48% | 8% | 28% | ~5,000 |
| PAIR | 96% | 76% | 24% | 64% | ~20 |

**关键发现：**
- PAIR在GPT-3.5上达到96%攻击成功率
- 仅需约20次查询，比GCG减少500倍以上
- 对Claude-2的攻击成功率较低（24%），说明其安全对齐更强

### 6.2 查询效率分析

| 模型 | 平均查询次数 | 中位数查询次数 | 成功率 |
|------|--------------|----------------|--------|
| GPT-3.5 | 12.3 | 8 | 96% |
| GPT-4 | 18.7 | 15 | 76% |
| Llama-2 | 15.2 | 11 | 64% |
| Claude-2 | 19.8 | 20 | 24% |

### 6.3 迁移性测试
使用在一个模型上生成的攻击提示测试其他模型：

| 攻击来源 \ 目标 | GPT-3.5 | GPT-4 | Claude-2 | Llama-2 |
|-----------------|---------|-------|----------|---------|
| GPT-3.5 | 96% | 68% | 12% | 45% |
| GPT-4 | 88% | 76% | 18% | 52% |
| Llama-2 | 72% | 58% | 24% | 64% |

**发现：** 攻击提示在同一家族模型间迁移性较好（如GPT-3.5→GPT-4），跨家族迁移性较差。



## 七、结果分析

### 7.1 攻击成功的原因
- **语义漏洞：** 安全训练主要覆盖明确的拒绝模式，对语义转换的防御不足
- **上下文利用：** 多轮对话可以逐步建立上下文，降低模型的警觉性
- **社会工程学：** 利用说服策略绕过理性的安全判断

### 7.2 防御建议
- **多轮安全训练：** 不仅训练单轮拒绝，还要训练识别多轮诱导
- **语义检测：** 开发能识别语义层面恶意意图的检测器
- **动态评估：** 实时评估对话的整体风险，而非仅看单条消息
- **人机协作：** 对高风险查询引入人工审核



## 八、展望

### 8.1 攻击方法的扩展
- **多轮对话攻击：** 扩展PAIR到更长的对话上下文
- **多模态攻击：** 结合图像、音频等多模态信息
- **自适应攻击：** 根据目标模型的防御动态调整策略

### 8.2 防御技术的发展
- **对抗训练：** 使用PAIR生成的样本进行对抗训练
- **检测机制：** 开发专门检测PAIR类型攻击的分类器
- **安全对齐改进：** 研究更鲁棒的安全对齐方法



## 九、代码资源

### 9.1 官方资源
论文: https://arxiv.org/abs/2310.08419
代码: 未开源（但算法描述足够详细可复现）

### 9.2 复现难度评估
难度: 中等
所需资源: OpenAI API 或其他LLM API访问
预计时间: 1-2天可实现基础版本



## 十、参考文献

Chao et al. (2023) - "Jailbreaking Black Box Large Language Models in Twenty Queries" (本论文)
Zou et al. (2023) - "Universal and Transferable Adversarial Attacks on Aligned Language Models" (GCG攻击)
Liu et al. (2024) - "AutoDAN: Generating Stealthy Jailbreak Prompts on Aligned Large Language Models"
Perez et al. (2022) - "Red Teaming Language Models with Language Models"
Carlini et al. (2023) - "Are Aligned Neural Networks Adversarially Aligned?"



## 十一、总结

PAIR算法代表了越狱攻击研究的重要进展，其核心贡献包括：
- **效率突破：** 将攻击查询次数从数万次降低到不到20次
- **黑盒可行性：** 证明针对闭源商业LLM的高效攻击是可能的
- **语义攻击优势：** 展示语义级提示在可解释性和迁移性方面的优势

**技术评价：** PAIR是一篇技术扎实、贡献明确的工作，对LLM安全研究产生了显著影响。

**笔记完成时间：** 2026年3月12日
**阅读进度：** 第16篇 / 共80篇
