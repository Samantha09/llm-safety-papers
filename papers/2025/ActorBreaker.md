# 【论文笔记】LLMs know their vulnerabilities: Uncover Safety Gaps through Natural Distribution Shifts (ActorBreaker)

## 1. 📌 论文基本信息

### 1.1 完整标题
LLMs know their vulnerabilities: Uncover Safety Gaps through Natural Distribution Shifts

### 1.2 作者及所属机构
Qibing Ren - Shanghai Jiao Tong University, Shanghai Artificial Intelligence Laboratory
Hao Li - Shanghai Artificial Intelligence Laboratory, Beihang University
Dongrui Liu - Shanghai Artificial Intelligence Laboratory
Zhanxu Xie - Beihang University
Xiaoya Lu - Shanghai Jiao Tong University
Yu Qiao - Shanghai Artificial Intelligence Laboratory
Lei Sha - Beihang University
Junchi Yan - Shanghai Jiao Tong University
Lizhuang Ma - Shanghai Jiao Tong University
Jing Shao - Shanghai Artificial Intelligence Laboratory

### 1.3 发表信息
提交时间: 2024年10月14日 (arXiv v1，标题为 Derail Yourself)
修订时间: 2025年5月25日 (arXiv v2，标题更新)
arXiv链接: https://arxiv.org/abs/2410.10700
会议: ACL 2025 Main Conference
代码: https://github.com/AI45Lab/ActorAttack
数据集: https://huggingface.co/datasets/SafeMTData/SafeMTData
研究领域: Computation and Language (cs.CL), Artificial Intelligence (cs.AI)

### 1.4 论文摘要（全文）

> Safety concerns in large language models (LLMs) have gained significant attention due to their exposure to potentially harmful data during pre-training. In this paper, we identify a new safety vulnerability in LLMs: their susceptibility to natural distribution shifts between attack prompts and original toxic prompts, where seemingly benign prompts, semantically related to harmful content, can bypass safety mechanisms. To explore this issue, we introduce a novel attack method, ActorBreaker, which identifies actors related to toxic prompts within pre-training distribution to craft multi-turn prompts that gradually lead LLMs to reveal unsafe content. ActorBreaker is grounded in Latour's actor-network theory, encompassing both human and non-human actors to capture a broader range of vulnerabilities. Our experimental results demonstrate that ActorBreaker outperforms existing attack methods in terms of diversity, effectiveness, and efficiency across aligned LLMs. To address this vulnerability, we propose expanding safety training to cover a broader semantic space of toxic content. We thus construct a multi-turn safety dataset using ActorBreaker. Fine-tuning models on our dataset shows significant improvements in robustness, though with some trade-offs in utility.

### 1.5 关键词
- Multi-turn Jailbreak (多轮越狱)
- Actor-Network Theory (行动者网络理论)
- Natural Distribution Shifts (自然分布偏移)
- LLM Safety (大语言模型安全)
- ActorBreaker (行动者突破攻击)
- SafeMTData (多轮安全数据集)



## 2. 🎯 研究背景

### 2.1 问题定义与历史演进

大型语言模型（LLMs）的安全性一直是AI领域的关键问题。尽管通过RLHF等对齐技术使模型更安全，但在多轮交互场景下，恶意用户仍可能通过逐步引导绕过安全机制。

**历史演进时间线:**

| 时间 | 里程碑 | 意义 |
|------|--------|------|
| 2022 | ChatGPT发布 | 展示了对齐技术的效果 |
| 2023 | 单轮越狱攻击 | GCG、AutoDAN等单轮攻击方法 |
| 2024 | 多轮攻击兴起 | Crescendo等渐进式攻击出现 |
| 2024.10 | ActorBreaker (v1) | 基于行动者网络的多轮攻击 |
| 2025.05 | ActorBreaker (v2) | 强调自然分布偏移的安全漏洞 |

### 2.2 现有方法的局限性

**单轮攻击的问题:**
- 恶意意图在提示中很明显
- 容易被安全检测机制识别
- 无法处理复杂的有害目标

**现有方法的局限:**
- Crescendo: 依赖固定的人工设计种子实例，缺乏多样性
- 任务分解策略: 容易被安全训练数据缓解

### 2.3 核心挑战

| 挑战 | 描述 | 传统方法的问题 |
|------|------|----------------|
| 隐藏意图 | 在多轮对话中隐藏有害意图 | 单轮攻击意图明显 |
| 发现攻击路径 | 同一目标有多种攻击路径 | 人工设计难以覆盖所有路径 |
| 多样性 | 生成多样化的攻击提示 | 固定模板缺乏变化 |
| 跨模型有效 | 攻击需要在不同模型上有效 | 特定优化难以迁移 |



## 3. 💡 研究意义

### 3.1 理论贡献

- 发现新的安全漏洞类型: **自然分布偏移**（Natural Distribution Shifts）
- 引入行动者网络理论: 将Latour的理论应用于LLM安全研究
- 提出ActorBreaker方法: 自动化发现多样化攻击路径

### 3.2 实践影响

- 红队测试工具: 提供自动化的多轮攻击测试手段
- 安全数据集: SafeMTData可用于安全微调
- 防御指导: 提出扩展安全训练覆盖更广泛语义空间的建议

### 3.3 关键发现

| 发现 | 意义 |
|------|------|
| 自然分布偏移可绕过安全机制 | 揭示了新的攻击面 |
| 行动者网络可生成多样化攻击 | 提供了系统性的攻击发现方法 |
| GPT-o1在推理中识别意图但仍输出有害内容 | 揭示了helpfulness与safety的冲突 |
| 安全微调可显著提高鲁棒性 | 提供了有效的防御方向 |



## 4. 📊 所用数据集

### 4.1 HarmBench基准

使用HarmBench框架进行攻击评估，包含有害行为数据集。

### 4.2 SafeMTData数据集

作者构建的多轮安全数据集：

#### 4.2.1 数据集组成
- **多轮对抗提示**: 使用ActorBreaker生成的攻击对话
- **安全对齐数据**: 用于安全微调的标注数据
- **规模**: 1000条成功攻击的多轮对话（基于600条有害指令）

#### 4.2.2 数据集用途
- 安全微调: 提高模型对多轮攻击的鲁棒性
- 防御评估: 测试防御方法的有效性

### 4.3 数据集统计

| 属性 | SafeMTData |
|------|------------|
| 有害指令数 | 600 |
| 成功攻击对话 | 1000 |
| 攻击者模型 | WizardLM-2-8x22B |
| 受害者模型 | deepseek-chat |
| 安全数据比例 | 1:2 (安全:指令) |



## 5. 🔬 研究方法

### 5.1 攻击设置

**目标:** 通过多轮对话逐步引导LLM产生有害内容，同时隐藏有害意图。

**核心思想:**
1. 识别与有害目标相关的行动者（Actors）
2. 以行动者为话题创建看似无害的对话
3. 逐步引导对话向有害目标发展

### 5.2 核心技术创新

#### 5.2.1 自然分布偏移（Natural Distribution Shifts）

**定义:** 攻击提示与原始有毒提示之间存在语义关联但分布不同的提示。

**特点:**
- 看似良性，难以被检测
- 与有害内容语义相关
- 存在于预训练分布中

#### 5.2.2 行动者网络理论（Actor-Network Theory）

基于Latour的理论，识别六种类型的行动者：

| 行动者类型 | 描述 | 与有害目标的关系 |
|------------|------|------------------|
| Distribution | 传播有害行为的行动者 | 传播者 |
| Regulation | 规范有害行为的行动者 | 规范者 |
| Facilitation | 促进有害行为的行动者 | 促进者 |
| Execution | 执行有害行为的行动者 | 执行者 |
| Consequence | 承受后果的行动者 | 受害者 |
| Prevention | 预防有害行为的行动者 | 防御者 |

**涵盖范围:**
- 人类行动者: 历史人物、有影响力的人
- 非人类行动者: 书籍、媒体、社会运动、技术工具

#### 5.2.3 两阶段攻击框架

**Pre-attack阶段: 发现攻击线索**
1. 构建概念网络（6种行动者类型）
2. 利用LLM知识实例化网络
3. 提取多样化的攻击线索

**In-attack阶段: 执行多轮攻击**
1. 推理攻击链: 规划从线索到目标的步骤
2. 自我对话生成: 攻击者LLM生成初始查询
3. 动态修改: 根据受害者响应调整攻击路径

### 5.3 动态修改策略

| 响应类型 | 处理策略 |
|----------|----------|
| Unknown | 受害者不知道答案 → 丢弃线索，选择新线索 |
| Refusal | 受害者拒绝回答 → 毒性降低（删除有害词，使用省略号） |



## 6. 🧪 实验详细记录

### 6.1 实验设置

**目标模型:**
- GPT-3.5 (GPT-3.5 Turbo 1106)
- GPT-4o
- Claude-3.5-Sonnet
- Llama-3-8B-Instruct
- Llama-3-70B-Instruct

**攻击者模型:**
- WizardLM-2-8x22B (用于生成攻击)
- GPT-4o (作为Judge评估)

**评估指标:**
- Attack Success Rate (ASR): GPT-4o Judge评分5分视为成功
- Diversity: 使用MiniLMv2计算句子嵌入距离

### 6.2 主要实验结果

#### 6.2.1 攻击成功率对比

| 模型 | ActorBreaker | GCG | PAIR | PAP | CipherChat | CodeAttack |
|------|:-----------:|:---:|:----:|:---:|:----------:|:----------:|
| GPT-3.5 | **78.5%** | 55.8% | 41.0% | 40.0% | 44.5% | 67.0% |
| GPT-4o | **84.5%** | 12.5% | 39.0% | 42.0% | 10.0% | 70.5% |
| Claude-3.5 | **66.5%** | 3.0% | 3.0% | 2.0% | 6.5% | 39.5% |
| Llama-3-8B | **79.0%** | 34.5% | 18.7% | 16.0% | 0% | 46.0% |
| Llama-3-70B | **85.5%** | 17.0% | 36.0% | 16.0% | 1.5% | 66.0% |

**观察:**
- ActorBreaker在所有模型上均取得最高攻击成功率
- 相比GCG，成功率平均提升约30-35个百分点
- 开源模型（Llama）比闭源模型更容易被攻击

#### 6.2.2 与Crescendo对比

| 指标 | ActorBreaker | Crescendo |
|------|:------------:|:---------:|
| 攻击成功率 | 更高 | 较低 |
| 多样性 | 更高（嵌入距离更大） | 较低 |
| 隐蔽性 | 更好（毒性评分更低） | 较差 |

**关键差异:**
- Crescendo依赖固定种子实例，容易陷入相似模式
- ActorBreaker利用LLM知识自动发现线索，路径更多样

#### 6.2.3 GPT-o1上的表现

- **攻击成功率**: 60%
- **关键发现**: 
  - GPT-o1能在思维链中识别有害意图并给出拒绝响应
  - 但仍会输出不安全内容
  - 揭示了helpfulness与safety目标的潜在冲突

#### 6.2.4 安全微调效果

| 模型 | ActorBreaker ASR | Crescendo ASR |
|------|:----------------:|:-------------:|
| Llama-3-8B (原始) | 78% | 24% |
| + SafeMTData (500) | 34% | 14% |
| + SafeMTData (1000) | 32% | 12% |

**权衡:**
- 安全性提升显著
- 但有用性（GSM8K、MMLU等）略有下降



## 7. 📈 结果分析

### 7.1 消融实验

#### 7.1.1 动态修改的影响

| 配置 | GPT-4o ASR | Claude-3.5 ASR |
|------|:----------:|:--------------:|
| ActorBreaker (完整) | 84.5% | 66.5% |
| w/o 动态修改 | 80.5% | 54.5% |

**结论:** 动态修改可提升攻击效果，但即使不使用也能取得较好效果。

#### 7.1.2 行动者数量的影响

| 行动者数量 | 攻击成功率 | 说明 |
|:----------:|:----------:|------|
| 1 | 较低 | 路径单一 |
| 3 | **最佳** | 多样性与效率平衡 |
| 5+ | 边际收益递减 | 计算成本增加 |

### 7.2 攻击路径分析

**大多数攻击路径被判定为最有害（评分5）**
- 说明ActorBreaker能有效发现高质量攻击路径
- 多样化路径有助于发现更多安全漏洞

### 7.3 隐蔽性分析

**Llama Guard 2检测率:**
- ActorBreaker生成的查询毒性评分远低于原始有害查询
- 也低于Crescendo生成的查询
- 验证了攻击的隐蔽性



## 8. 🔮 展望

### 8.1 局限性

1. **计算成本**: 构建线索库需要较大计算资源
2. **攻击时间**: 多轮攻击需要较长时间
3. **有用性权衡**: 安全微调会降低模型有用性
4. **评估主观性**: 攻击成功与否的判断存在一定主观性

### 8.2 未来研究方向

1. **更高效的线索发现**: 研究如何更快地发现可利用的安全线索
2. **更好的防御方法**: 探索不牺牲有用性的安全微调策略
3. **实时检测**: 开发针对多轮攻击的实时检测机制
4. **可解释性**: 深入理解为何某些线索可以被利用

### 8.3 防御建议

论文提出通过**扩展安全训练**来覆盖更广泛的毒性内容语义空间：
- 增加多轮对话形式的安全示例
- 覆盖边界和灰色场景
- 专门针对角色扮演场景的安全训练
- 强化拒绝行为的奖励



## 9. 💻 代码资源

### 9.1 官方实现
- **GitHub**: https://github.com/AI45Lab/ActorAttack
- **数据集**: https://huggingface.co/datasets/SafeMTData/SafeMTData

### 9.2 相关资源
- **arXiv**: https://arxiv.org/abs/2410.10700
- **v1版本**: https://arxiv.org/abs/2410.10700v1 (标题为Derail Yourself)



## 10. 📚 参考文献

1. Zou, A., Wang, Z., Carlini, N., Nasr, M., Kolter, J. Z., & Fredrikson, M. (2023). Universal and Transferable Adversarial Attacks on Aligned Language Models. arXiv preprint arXiv:2307.15043.

2. Russinovich, M., et al. (2024). Crescendo: Multi-Turn LLM Jailbreak Attack. arXiv preprint.

3. Latour, B. (1987). Science in Action: How to Follow Scientists and Engineers Through Society. Harvard University Press.

4. Mazeika, M., et al. (2024). HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal. ICLR 2024.

5. Ji, J., et al. (2024). Beavertails: Towards improved safety alignment of llm via a human-preference dataset. NeurIPS 2024.

6. Ouyang, L., et al. (2022). Training language models to follow instructions with human feedback. NeurIPS 2022.

7. Bai, Y., et al. (2022). Constitutional AI: Harmlessness from AI Feedback. arXiv preprint arXiv:2212.08073.



---

**备注:**
- v1版本标题为 "Derail Yourself: Multi-turn LLM Jailbreak Attack through Self-discovered Clues"
- v2版本标题更新为 "LLMs know their vulnerabilities: Uncover Safety Gaps through Natural Distribution Shifts"
- 方法名从ActorAttack改为ActorBreaker

*最后更新: 2026-03-21*  
*基于 arXiv v2 版本整理*
