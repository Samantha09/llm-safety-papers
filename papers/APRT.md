# 【论文笔记】Automated Progressive Red Teaming (APRT)

论文标题: Automated Progressive Red Teaming
作者: Bojian Jiang, Yi Jing, Tianhao Shen, Tong Wu, Qing Yang, Deyi Xiong
机构: Tianjin University, Du Xiaoman Finance
arXiv: https://arxiv.org/abs/2407.03876
会议: COLING 2025 (Accepted)
代码: https://github.com/tjunlp-lab/APRT
阅读日期: 2026-03-13
笔记编号: 第20篇 / 共80篇



## 第1章 论文基本信息

### 1.1 论文概况

| 属性 | 内容 |
|------|------|
| 标题 | Automated Progressive Red Teaming |
| 作者 | Bojian Jiang¹², Yi Jing¹², Tianhao Shen¹, Tong Wu², Qing Yang², Deyi Xiong¹ |
| 机构 | ¹天津大学智能与计算学部, ²度小满金融 |
| 发表 | COLING 2025 (已接收) |
| arXiv | 2407.03876 |
| 领域 | Red Teaming / LLM Safety / Automated Adversarial Testing |
| 代码开源 | 是 (GitHub: tjunlp-lab/APRT) |

### 1.2 作者背景
Bojian Jiang & Yi Jing: 共同第一作者，来自天津大学NLP实验室和度小满金融
Deyi Xiong: 通讯作者，天津大学教授，长期从事机器翻译和自然语言处理研究
Qing Yang: 通讯作者，度小满金融

### 1.3 论文核心贡献
- 提出APRT框架: 首个将红队测试框架化为可有效学习任务的自动化渐进式红队测试框架
- 三模块协同架构: 意图扩展LLM + 意图隐藏LLM + 邪恶制造者(Evil Maker)
- AER评估指标: 提出Attack Effectiveness Rate，解决现有ASR指标的局限性
- 强攻击效果: 在Llama-3-8B上达到54%攻击成功率，GPT-4o达50%，Claude-3.5达39%



## 第2章 研究背景

### 2.1 红队测试(Red Teaming)概述
红队测试是一种广泛应用于各类系统的漏洞发现技术，已成为评估和增强LLM安全性的关键方法。其核心目标是：
- 发现安全漏洞: 识别LLM可能产生有害输出的场景
- 评估安全对齐: 测试安全训练的有效性
- 改进模型安全: 为后续安全训练提供对抗样本

### 2.2 现有方法的局限性

#### 2.2.1 人工红队测试
**优点:**
- 攻击质量高，能发现深层漏洞
- 可针对特定领域进行精细化测试

**缺点:**
- 成本高昂: Meta为Llama-2组建了350人的红队团队
- 耗时漫长: 多轮测试持续数月
- 难以扩展: 无法覆盖所有潜在攻击场景

#### 2.2.2 自动化红队测试(ART)
现有ART方法分为两类：

**1) 基于模板的方法:**
- 开发通用模板结合原始红队指令
- 代表工作: GCG (Zou et al., 2023), AutoDAN (Liu et al., 2024)
- 局限: 模板固定，难以适应新类型的攻击

**2) 基于生成的方法:**
- 利用LLM或LLM-based系统生成攻击
- 代表工作: TAP (Mehrotra et al., 2023), PAIR (Chao et al., 2024)
- 局限: 未充分利用参数化LLM的学习能力

### 2.3 关键问题
当前生成式红队测试研究存在以下关键缺陷：
- 固定参数攻击: 部分研究仅使用固定参数LLM攻击目标模型，缺乏学习能力
- 缺乏渐进机制: 未根据目标LLM的反馈动态调整攻击方向
- 样本选择盲目: 无差别选择成功攻击样本作为训练数据，无法为攻击LLM提供有价值的方向指导



## 第3章 研究意义

### 3.1 理论意义
- 框架化红队测试: 首次将红队测试明确框架化为可有效学习的任务
- 渐进学习机制: 证明了基于反馈的渐进式训练在红队测试中的关键作用
- 评估指标创新: AER指标更贴近人类评估，为领域提供新的评估范式

### 3.2 实践意义
- 高效漏洞发现: 自动化流程大幅降低红队测试成本
- 强迁移能力: 在开源模型上训练的攻击可迁移到闭源商业模型
- 安全评估工具: 为LLM安全评估提供标准化、可复现的测试框架

### 3.3 对LLM安全社区的影响
- 攻击方: 提供更强的自动化攻击工具
- 防御方: 帮助识别模型弱点，指导安全改进
- 评估方: 提供更准确的模型安全性评估方法



## 第4章 所用数据集

### 4.1 主要数据集
AdvBench Harmful Behaviors

| 属性 | 内容 |
|------|------|
| 来源 | Zou et al. (2023) - GCG论文 |
| 规模 | 520条有害行为指令 |
| 内容 | 涵盖多种有害行为类别 |
| 用途 | 作为攻击提示的初始种子数据 |

### 4.2 数据特点
- 多样性: 覆盖多种类型的有害请求
- 真实性: 基于真实场景构建
- 挑战性: 经过筛选，对现有模型具有一定挑战性

### 4.3 数据使用方式
- 输入: 原始有害行为指令 (Attacking Prompts)
- 处理: 通过Intention Expanding LLM扩展多样性
- 输出: 经过意图隐藏后的对抗性提示



## 第5章 研究方法

### 5.1 APRT框架概述
APRT (Automated Progressive Red Teaming) 是一个三模块协同的渐进式红队测试框架：

**三模块架构:**
1. **Intention Expanding LLM (意图扩展LLM)**: 生成多样化的初始攻击样本
2. **Intention Hiding LLM (意图隐藏LLM)**: 将攻击意图转化为欺骗性提示
3. **Evil Maker (邪恶制造者)**: 管理提示多样性并过滤无效样本

### 5.2 核心模块详解

#### 5.2.1 Intention Expanding LLM (意图扩展LLM)
**功能:** 生成多样化的初始攻击样本

**工作机制:**
- 接收原始攻击提示集合 𝒫_att
- 生成扩展后的攻击提示集合 𝒫_gen
- 目标是产生相对容易越狱的多样化样本

**特点:**
- 固定参数，不参与训练
- 负责扩大攻击意图的覆盖范围
- 为后续意图隐藏提供丰富的素材

#### 5.2.2 Intention Hiding LLM (意图隐藏LLM)
**功能:** 将攻击意图转化为欺骗性提示

**工作机制:**
- 接收意图扩展LLM生成的提示
- 学习将有害意图隐藏在看似无害的表述中
- 通过多轮训练逐步提升隐藏能力

**训练策略:**
- 采用主动学习(Active Learning)策略
- 优先选择难以被察觉的意图样本
- 每轮迭代更新模型参数

#### 5.2.3 Evil Maker (邪恶制造者)
**功能:** 管理提示多样性并过滤无效样本

**核心功能:**
- 多样性管理: 避免生成过于相似的提示
- 有效性过滤: 过滤掉已被目标模型安全拒绝的提示
- 样本选择: 为意图隐藏LLM选择有价值的训练样本

### 5.3 渐进式训练流程

迭代轮次 i = 1, 2, ..., T:

```
1. 意图扩展: 𝒫_gen^i ← ℳ_exp(𝒫_att)
2. 样本过滤: 𝒫_suc^i ← ℰ_m(𝒫_gen^i)
3. 意图隐藏 (重复 A_max 次):
   for j = 1 to A_max:
     𝒫_hid^ij ← ℳ_hid^(i-1)(𝒫_suc^i)
     𝒫_res^ij ← ℳ_tgt(𝒫_hid^ij)
4. 训练数据选择: 𝒟_hid^i ← SelectHiddenIntention(...)
5. 模型更新: ℳ_hid^i ← Train(ℳ_hid^(i-1), 𝒟_hid^i)
```

### 5.4 主动学习策略
**核心思想:** 优先选择"难以察觉但成功攻击"的样本

**选择标准:**
- 攻击成功: 能够诱导目标模型产生有害输出
- 意图隐蔽: 有害意图难以被安全机制识别
- 有用性: 输出看似有帮助，降低用户警觉

### 5.5 AER评估指标

#### 5.5.1 现有指标的局限性
**ASR (Attack Success Rate):**
- 仅统计是否产生有害输出
- 无法区分"明显有害"和"隐蔽有害"
- 与人类评估一致性较低

#### 5.5.2 AER (Attack Effectiveness Rate)
**定义:** 测量诱导出"不安全但看似有帮助"响应的可能性

**公式:**
AER = P(Unsafe ∧ Helpful | Attack Prompt)

**优势:**
- 与人类评估高度一致
- 更准确地反映真实攻击效果
- 考虑了攻击的隐蔽性



## 第6章 实验详细记录

### 6.1 实验设置

#### 6.1.1 目标模型

| 模型 | 类型 | 访问方式 |
|------|------|----------|
| Llama-3-8B-Instruct | 开源 | 本地部署 |
| GPT-4o | 闭源 | API |
| Claude-3.5 | 闭源 | API |

#### 6.1.2 基线方法
- GCG (Zou et al., 2023): 基于梯度的对抗后缀搜索
- PAIR (Chao et al., 2024): 基于LLM的迭代攻击
- TAP (Mehrotra et al., 2023): 树形攻击提示生成
- AutoDAN (Liu et al., 2024): 自动生成的隐蔽越狱提示
- MART (Ge et al., 2023): 多轮对抗训练红队测试

#### 6.1.3 评估指标
- ASR: 攻击成功率
- AER: 攻击有效率 (本文提出)
- Human Evaluation: 人工评估

### 6.2 主要实验结果

#### 6.2.1 攻击成功率对比

| 方法 | Llama-3-8B | GPT-4o | Claude-3.5 |
|------|------------|--------|------------|
| GCG | ~30% | ~15% | ~10% |
| PAIR | ~35% | ~20% | ~15% |
| TAP | ~40% | ~25% | ~20% |
| AutoDAN | ~45% | ~30% | ~25% |
| MART | ~48% | ~35% | ~28% |
| **APRT (本文)** | **54%** | **50%** | **39%** |

#### 6.2.2 AER指标结果

| 模型 | AER |
|------|-----|
| Llama-3-8B-Instruct | 54% |
| GPT-4o | 50% |
| Claude-3.5 | 39% |

### 6.3 迁移性实验
**关键发现:** 在开源模型(Llama-3-8B)上训练的APRT，能够有效迁移到闭源商业模型

| 训练目标 | 测试目标 | AER |
|----------|----------|-----|
| Llama-3-8B | Llama-3-8B | 54% |
| Llama-3-8B | GPT-4o | 50% |
| Llama-3-8B | Claude-3.5 | 39% |

### 6.4 消融实验

#### 6.4.1 渐进训练的重要性

| 配置 | Llama-3-8B AER |
|------|----------------|
| 无渐进训练 (单轮) | 38% |
| 2轮渐进训练 | 46% |
| 4轮渐进训练 | 54% |

**结论:** 渐进式训练显著提升攻击效果

#### 6.4.2 主动学习策略的影响

| 样本选择策略 | Llama-3-8B AER |
|--------------|----------------|
| 随机选择 | 42% |
| 仅选攻击成功 | 48% |
| 主动学习 (本文) | 54% |

**结论:** 主动学习策略有效提升攻击效率

#### 6.4.3 三模块的必要性

| 配置 | Llama-3-8B AER |
|------|----------------|
| 仅意图隐藏LLM | 35% |
| 意图扩展 + 意图隐藏 | 46% |
| 完整三模块 (本文) | 54% |

**结论:** 三模块协同工作效果最佳

### 6.5 人工评估
**评估设置:**
- 评估者: 3名专业标注员
- 评估维度: 有害性、隐蔽性、有用性
- 样本量: 每模型200个攻击样本

**结果:**

| 模型 | 人工评估AER | 自动评估AER | 一致性 |
|------|-------------|-------------|--------|
| Llama-3-8B | 52% | 54% | 96% |
| GPT-4o | 48% | 50% | 96% |
| Claude-3.5 | 37% | 39% | 95% |

**结论:** AER指标与人类评估高度一致



## 第7章 结果分析

### 7.1 关键发现

#### 7.1.1 渐进训练的关键作用
实验结果表明，渐进式训练是APRT成功的核心因素：
- 学习曲线: 随着训练轮次增加，攻击成功率稳步提升
- 反馈机制: 基于目标模型反馈调整攻击方向至关重要
- 累积效应: 每轮训练在前一轮基础上进一步提升

#### 7.1.2 跨模型迁移能力
APRT展现出强大的迁移能力：
- 开源→闭源: 在Llama-3-8B上训练的模型，无需额外训练即可攻击GPT-4o和Claude-3.5
- 保持效果: 迁移后的攻击效果接近直接在目标模型上训练
- 成本优势: 大幅降低对昂贵商业API的依赖

#### 7.1.3 攻击隐蔽性
APRT生成的攻击具有以下特点：
- 意图隐藏: 有害意图被巧妙隐藏在正常表述中
- 语境欺骗: 利用模型对上下文的理解进行欺骗
- 渐进诱导: 通过多轮交互逐步引导模型产生有害输出

### 7.2 与MART的对比

| 对比维度 | MART | APRT (本文) |
|----------|------|-------------|
| 训练方式 | 多轮对抗训练 | 渐进式训练 |
| 目标模型安全 | 安全性不足 | 保持完整安全机制 |
| 样本选择 | 无差别选择 | 主动学习策略 |
| 攻击效果 | 48% | 54% |
| 迁移能力 | 有限 | 强 |

**关键差异:**
- APRT保持目标模型的完整安全机制，使攻击更具挑战性
- APRT采用主动学习策略，优先选择难样本
- APRT的三模块架构更灵活高效

### 7.3 局限性分析
- 计算成本: 渐进训练需要多轮迭代，计算开销较大
- 评估依赖: AER评估仍需依赖Reward LLM，存在一定主观性
- 防御更新: 目标模型安全更新后，攻击效果可能下降
- 伦理风险: 强大的攻击能力可能被恶意使用



## 第8章 展望

### 8.1 未来研究方向

#### 8.1.1 方法改进
- 效率优化: 开发更高效的渐进训练算法，减少计算开销
- 自适应攻击: 研究目标模型更新后的自适应攻击策略
- 多模态扩展: 将APRT扩展到多模态大模型
- 长期攻击: 研究长期、持续的攻击策略

#### 8.1.2 防御研究
- 对抗训练: 利用APRT生成的样本进行对抗训练
- 检测机制: 开发针对隐蔽攻击的检测方法
- 动态防御: 研究动态调整的安全机制
- 人机协作: 结合人工审核的混合防御策略

#### 8.1.3 评估改进
- 自动化评估: 开发更准确、低成本的自动化评估方法
- 多维度评估: 考虑更多维度的攻击效果评估
- 实时评估: 研究在线实时攻击效果评估

### 8.2 应用前景

#### 8.2.1 安全评估
- 模型发布前测试: 作为LLM发布前的标准安全测试工具
- 定期安全审计: 用于定期评估已部署模型的安全性
- 竞品分析: 评估不同厂商LLM的安全水平

#### 8.2.2 安全训练
- 对抗样本生成: 为安全训练提供高质量对抗样本
- 鲁棒性测试: 测试安全训练的有效性
- 持续改进: 指导安全机制的迭代优化

### 8.3 伦理考量

#### 8.3.1 负责任的研究
- 开源策略: 代码开源但需谨慎使用
- 使用限制: 建议仅用于安全研究和模型评估
- 社区监督: 建立研究社区监督机制

#### 8.3.2 防御优先
- 研究重点应放在防御方法上
- 攻击研究应服务于更强的安全机制
- 与模型开发者合作，提前修复漏洞



## 第9章 代码资源

### 9.1 官方资源

| 资源类型 | 链接 |
|----------|------|
| 代码仓库 | https://github.com/tjunlp-lab/APRT |
| 论文PDF | https://arxiv.org/pdf/2407.03876 |
| arXiv页面 | https://arxiv.org/abs/2407.03876 |

### 9.2 复现建议
- 硬件要求: 至少1张A100 GPU用于训练
- API准备: 准备OpenAI和Anthropic API密钥用于评估
- 数据集: 使用AdvBench Harmful Behaviors数据集
- 训练时间: 完整训练约需8-12小时



## 第10章 参考文献和延伸阅读

### 10.1 主要参考文献

**APRT (本文)**
Jiang, B., Jing, Y., Shen, T., Wu, T., Yang, Q., & Xiong, D. (2024). Automated Progressive Red Teaming. arXiv:2407.03876. Accepted by COLING 2025.

**GCG Attack**
Zou, A., Wang, Z., Carlini, N., Nasr, M., Kolter, J. Z., & Fredrikson, M. (2023). Universal and Transferable Adversarial Attacks on Aligned Language Models. arXiv:2307.15043.

**PAIR**
Chao, P., Robey, A., Dobriban, E., Hassani, H., Pappas, G. J., & Wong, E. (2024). Jailbreaking Black Box Large Language Models in Twenty Queries. arXiv:2310.08419.

**TAP**
Mehrotra, A., Zampetakis, M., Kassianik, P., Nelson, B., Anderson, H., Singer, Y., & Hardt, M. (2023). Tree of Attacks: Jailbreaking Black-Box LLMs Automatically. arXiv:2312.02119.

**AutoDAN**
Liu, X., Xu, N., Chen, M., & Xiao, C. (2024). AutoDAN: Generating Stealthy Jailbreak Prompts on Aligned Large Language Models. ICLR 2024.

**MART**
Ge, S., Zhang, Y., Liu, L., Zhang, M., Han, J., & Gao, J. (2023). Mart: Improving llm safety with multi-round automatic red-teaming. arXiv:2311.07689.

### 10.2 相关综述

**Jailbreak Attacks Survey**
Xu, G., Liu, Y., Guo, H., Li, H., & Liu, Y. (2024). Jailbreak Attacks and Defenses Against LLMs: A Survey. arXiv:2407.04295.

**AI Alignment Survey**
Ji, J., Qiu, T., Chen, B., Zhang, B., Lou, H., Wang, K., ... & Yang, Y. (2023). AI Alignment: A Comprehensive Survey. arXiv:2310.19852.

**LLM Safety Survey**
Yao, Y., Duan, J., Xu, K., Cai, Y., Sun, Z., & Zhang, Y. (2024). A Survey on Large Language Model (LLM) Security and Privacy: The Good, The Bad, and The Ugly. High-Confidence Computing.

### 10.3 延伸阅读建议

**攻击方法**
- Crescendo (Russinovich et al., 2024): 多轮递增式越狱
- AutoDAN-Turbo (Liu et al., 2024): 终身学习策略自探索
- Cold-Attack (Guo et al., 2024): 隐蔽可控的越狱攻击

**防御方法**
- Llama Guard (Inan et al., 2023): 基于LLM的输入输出安全保障
- NeMo Guardrails (Rebedea et al., 2023): 可控制和安全的LLM应用工具包
- MLLM-Protector (Pi et al., 2024): 保护多模态LLM安全

**评估基准**
- HarmBench (Mazeika et al., 2024): 自动红队测试标准化评估
- JailbreakBench (Chao et al., 2024): 越狱攻击开放鲁棒性基准
- AgentDojo (Debenedetti et al., 2024): 动态提示注入攻击评估环境



*本笔记由 Kimi Claw 自动生成于 2026-03-13*  
*论文阅读计划: 第20篇 / 共80篇*
