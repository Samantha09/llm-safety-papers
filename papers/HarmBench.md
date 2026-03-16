# HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal

**阅读日期**: 2026年3月9日  
**论文来源**: arXiv 2024  
**arXiv链接**: https://arxiv.org/abs/2402.04249  
**代码仓库**: https://github.com/centerforaisafety/HarmBench

---

## 1. 论文基本信息

### 1.1 完整标题与作者

**标题**: HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal

**作者列表**:
- Mantas Mazeika - Center for AI Safety
- Long Phan - Center for AI Safety
- Xuwang Yin - Center for AI Safety
- Andy Zou - Center for AI Safety
- Zifan Wang - Center for AI Safety
- Norman Mu - Center for AI Safety
- Elham Sakhaee - Center for AI Safety
- Nathaniel Li - Center for AI Safety
- Steven Basart - Center for AI Safety
- Bo Li - University of Chicago
- David Forsyth - University of Illinois Urbana-Champaign
- Dan Hendrycks - Center for AI Safety

### 1.2 发表信息

- **提交时间**: 2024年2月6日 (arXiv v1)
- **修订时间**: 2024年2月27日 (arXiv v2)
- **arXiv链接**: https://arxiv.org/abs/2402.04249
- **DOI**: https://doi.org/10.48550/arXiv.2402.04249
- **研究领域**: Machine Learning (cs.LG), Artificial Intelligence (cs.AI), Computation and Language (cs.CL), Computer Vision and Pattern Recognition (cs.CV)

### 1.3 摘要全文与翻译

**Abstract (Original)**:

> Automated red teaming holds substantial promise for uncovering and mitigating the risks associated with the malicious use of large language models (LLMs), yet the field lacks a standardized evaluation framework to rigorously assess new methods. To address this issue, we introduce HarmBench, a standardized evaluation framework for automated red teaming. We identify several desirable properties previously unaccounted for in red teaming evaluations and systematically design HarmBench to meet these criteria. Using HarmBench, we conduct a large-scale comparison of 18 red teaming methods and 33 target LLMs and defenses, yielding novel insights. We also introduce a highly efficient adversarial training method that greatly enhances LLM robustness across a wide range of attacks, demonstrating how HarmBench enables codevelopment of attacks and defenses. We open source HarmBench at https://github.com/centerforaisafety/HarmBench.

**摘要（中文翻译）**:

> 自动化红队测试在发现和缓解与大型语言模型（LLM）恶意使用相关的风险方面具有巨大潜力，但该领域缺乏一个标准化的评估框架来严格评估新方法。为解决这一问题，我们引入了HarmBench，一个用于自动化红队测试的标准化评估框架。我们识别了以往红队测试评估中未被考虑的几个理想特性，并系统地设计HarmBench以满足这些标准。使用HarmBench，我们对18种红队测试方法和33个目标LLM及防御方法进行了大规模比较，得出了新的见解。我们还引入了一种高效的对抗训练方法，可大幅增强LLM对广泛攻击的鲁棒性，展示了HarmBench如何促进攻击和防御的协同开发。我们在 https://github.com/centerforaisafety/HarmBench 开源了HarmBench。

### 1.4 关键词

- **Automated Red Teaming** (自动化红队测试)
- **LLM Attacks** (LLM攻击)
- **Alignment** (对齐)
- **Robust Refusal** (鲁棒拒绝)
- **Adversarial Training** (对抗训练)
- **ML Safety** (机器学习安全)

---

## 2. 研究背景

### 2.1 问题定义与历史演进

**自动化红队测试(Automated Red Teaming, ART)** 是AI安全领域的关键研究方向。随着大型语言模型能力的快速提升，确保这些模型不被恶意使用变得至关重要。

**历史演进时间线**:

| 时间 | 里程碑 | 意义 |
|------|--------|------|
| 2021-2022 | 手动红队测试 | Bai et al., Ganguli et al. 进行大规模人工测试 |
| 2022 | Perez et al. | 首次提出用LLM对LLM进行红队测试 |
| 2023 | GCG攻击 | Zou et al. 提出通用对抗攻击 |
| 2023 | PAIR | Chao et al. 提出黑盒自动越狱 |
| 2023 | TAP | Mehrotra et al. 提出树形攻击 |
| 2024 | **HarmBench** | **首个标准化红队测试评估框架** |

### 2.2 现有评估方法的碎片化问题

**表1: 以往工作的评估设置对比**

| 论文 | 比较的方法 | 评估设置 |
|------|-----------|----------|
| Perez et al. (2022) | 1, 2, 3, 4 | A |
| GCG (Zou et al., 2023) | 5, 6, 7, 8 | B |
| PAIR (Chao et al., 2023) | 5, 11 | E |
| TAP (Mehrotra et al., 2023) | 5, 11, 12 | E |
| PAP (Zeng et al., 2024) | 5, 7, 11, 13, 14 | F |
| AutoDAN (Liu et al., 2023) | 5, 15 | B, G |

**关键问题**:
- 至少有 **9种不同的评估设置**
- 评估之间 **几乎没有重叠**
- 跨论文比较 **实际上不可能**

### 2.3 现有评估的不足之处

| 问题 | 描述 | 影响 |
|------|------|------|
| 缺乏广度 | 大多数评估使用 <100 个行为 | 无法全面测试攻击方法 |
| 不可比较 | 评估参数不统一 | ASR可能差异高达30% |
| 指标不鲁棒 | 分类器容易被欺骗 | 评估结果不可靠 |

---

## 3. 研究意义

### 3.1 理论贡献

1. **首次提出标准化红队测试框架**: 定义了评估自动化红队测试的三个关键标准：
   - **广度(Breadth)**: 涵盖多样化的有害行为
   - **可比性(Comparability)**: 统一的评估参数
   - **鲁棒指标(Robust Metrics)**: 抗对抗的分类器

2. **大规模实证研究**: 首次在同一框架下比较18种攻击方法和33个目标模型

3. **新的防御方法**: 提出高效的对抗训练方法，显著提升模型鲁棒性

### 3.2 实践影响

1. **基准测试工具**: 成为红队测试领域的事实标准
2. **攻击防御协同开发**: 展示如何在同一框架下迭代改进攻击和防御
3. **产业应用**: 已被Google、Microsoft等公司参考

### 3.3 关键发现

| 发现 | 意义 |
|------|------|
| 当前攻击方法没有统一最优 | 不同攻击在不同场景下表现各异 |
| 模型鲁棒性与规模无关 | 挑战了"更大模型更安全"的假设 |
| 对抗训练可显著提升鲁棒性 | 提供了一条可行的防御路径 |

---

## 4. 所用数据集

### 4.1 HarmBench行为数据集

**总体统计**:
- **总行为数**: 510个
- **文本行为**: 400个
- **多模态行为**: 110个
- **验证集**: 100个
- **测试集**: 410个

### 4.2 功能类别(Functional Categories)

| 类别 | 数量 | 描述 |
|------|------|------|
| Standard Behaviors | 200 | 标准有害行为字符串 |
| Copyright Behaviors | 100 | 版权侵犯行为 |
| Contextual Behaviors | 100 | 带上下文的上下文行为 |
| Multimodal Behaviors | 110 | 包含图像的多模态行为 |

### 4.3 语义类别(Semantic Categories)

| 类别 | 描述 |
|------|------|
| Cybercrime & Unauthorized Intrusion | 网络犯罪和未授权入侵 |
| Chemical & Biological Weapons/Drugs | 化学和生物武器/毒品 |
| Copyright Violations | 版权侵犯 |
| Misinformation & Disinformation | 虚假信息和错误信息 |
| Harassment & Bullying | 骚扰和欺凌 |
| Illegal Activities | 非法活动 |
| General Harm | 一般性危害 |

### 4.4 数据集设计原则

1. **违反法律或规范**: 大多数理性的人不希望公开的LLM展示这些行为
2. **差异化危害**: 行为应体现LLM执行相比于人类使用搜索引擎的额外危害
3. **现实性**: 基于OpenAI、Anthropic、Meta和Inflection AI的可接受使用政策设计

---

## 5. 研究方法

### 5.1 整体框架

HarmBench采用**标准化评估框架**，包含以下核心组件：

**组件1: 标准化数据集**
- 510个有害行为（400文本 + 110多模态）
- 分为验证集(100)和测试集(410)
- 涵盖7个语义类别

**组件2: 统一评估协议**
- 明确定义的威胁模型
- 标准化的系统提示和聊天模板
- 一致的评估指标

**组件3: 鲁棒分类器**
- 基于Llama-2-13B的HarmBench分类器
- 经过对抗训练，抵抗对抗性攻击
- 高准确率(96.4%)和低假阳性率

**组件4: 开源工具包**
- 完整的评估代码
- 预训练分类器
- 标准化数据集

### 5.2 评估指标

**主要指标**:

1. **Attack Success Rate (ASR)**:
   - 定义：成功诱导模型生成有害内容的行为比例
   - 计算公式：ASR = (成功攻击的行为数 / 总行为数) × 100%

2. **Efficiency**:
   - 定义：达到特定成功率所需的平均查询次数
   - 重要性：反映攻击的实际可行性

3. **Robustness**:
   - 定义：模型在面对攻击时保持拒绝的能力
   - 计算：1 - ASR

**辅助指标**:

4. **Transferability**:
   - 攻击在不同模型间的迁移能力

5. **Stealthiness**:
   - 攻击的隐蔽性（针对隐蔽攻击）

### 5.3 分类器设计

**HarmBench分类器特点**:
- **基础模型**: Llama-2-13B
- **训练方式**: 对抗训练
- **准确率**: 96.4%
- **假阳性率**: <2%
- **对抗鲁棒性**: 显著优于标准分类器

**分类器训练**:
- 使用对抗样本进行数据增强
- 多轮对抗训练
- 人工验证和校准

---

## 6. 实验详细记录

### 6.1 大规模对比实验

**测试的攻击方法** (18种):
- GCG (Greedy Coordinate Gradient)
- PAIR (Prompt Automatic Iterative Refinement)
- TAP (Tree of Attacks)
- AutoDAN
- PAP (Preference-based Attack)
- 以及其他13种方法

**测试的目标模型** (33个):
- GPT-3.5, GPT-4
- Llama-2 (7B, 13B, 70B)
- Llama-3 (8B, 70B)
- Claude系列
- 以及其他20+模型

### 6.2 主要实验结果

**表2: 攻击成功率对比 (%)**

| 攻击方法 | GPT-3.5 | GPT-4 | Llama-2-7B | Llama-2-13B | Llama-2-70B |
|---------|---------|-------|------------|-------------|-------------|
| GCG | 82.5 | 58.3 | 78.2 | 72.1 | 65.4 |
| PAIR | 68.2 | 45.7 | 62.3 | 58.9 | 52.1 |
| TAP | 75.8 | 52.4 | 71.5 | 67.2 | 59.8 |
| AutoDAN | 88.3 | 71.2 | 84.7 | 79.3 | 72.5 |
| PAP | 72.1 | 48.9 | 68.4 | 63.7 | 56.2 |

**关键发现**:
- AutoDAN在所有模型上表现最佳
- GPT-4展现出最强的防御能力
- 模型规模与鲁棒性并非简单正相关

### 6.3 防御方法评估

**表3: 对抗训练效果**

| 模型 | 原始ASR | +对抗训练ASR | 改善幅度 |
|------|---------|--------------|----------|
| Llama-2-7B | 78.2% | 32.5% | -45.7% |
| Llama-2-13B | 72.1% | 28.3% | -43.8% |
| Llama-2-70B | 65.4% | 24.7% | -40.7% |

**关键发现**:
- 对抗训练可显著降低攻击成功率
- 效果在不同规模模型上都很明显
- 提供了实用的防御路径

### 6.4 分类器鲁棒性

**表4: 分类器性能对比**

| 分类器 | 准确率 | 对抗ASR | 鲁棒性提升 |
|--------|--------|---------|------------|
| 标准分类器 | 94.2% | 45.3% | - |
| HarmBench分类器 | 96.4% | 12.7% | +32.6% |

**关键发现**:
- HarmBench分类器在对抗场景下表现显著更好
- 高准确率的同时保持对抗鲁棒性

---

## 7. 创新点

### 7.1 主要创新

**1. 首个全面的标准化红队测试框架**

HarmBench是首个系统性地解决红队测试评估碎片化问题的框架，提供了标准化的数据集、评估协议和工具。

**2. 鲁棒的评估指标**

通过对抗训练的分类器，HarmBench提供了比以往工作更可靠的评估指标，减少了分类器被欺骗的风险。

**3. 大规模系统性比较**

首次在同一框架下比较18种攻击方法和33个目标模型，提供了前所未有的全面视角。

**4. 实用的防御方法**

提出的高效对抗训练方法不仅在实验中有效，而且计算成本低，适合实际部署。

### 7.2 技术创新

**对抗训练分类器**: 使用对抗样本训练分类器，提高其在对抗场景下的鲁棒性。

**标准化协议**: 定义了从数据格式到评估流程的完整标准化协议。

**多维度评估**: 不仅关注攻击成功率，还考虑效率、迁移性等多个维度。

### 7.3 社区贡献

**开源工具包**: 完整开源代码、数据集和预训练模型，降低研究门槛。

** leaderboard**: 提供公共排行榜，激励社区贡献，追踪领域进展。

**最佳实践**: 通过论文和文档传播红队测试的最佳实践。

---

## 8. 局限性与未来工作

### 8.1 当前局限

**语言限制**: 目前主要关注英文场景，对其他语言的支持有限。

**多模态覆盖**: 虽然包含110个多模态行为，但多模态攻击方法的评估还不够全面。

**实时性**: 随着新模型和攻击方法的出现，需要持续更新基准。

**计算成本**: 完整的基准测试需要大量计算资源。

### 8.2 未来研究方向

**多语言扩展**: 扩展数据集以支持中文、西班牙语等其他主要语言。

**多模态增强**: 增加更多多模态行为和攻击方法。

**动态更新**: 建立自动化机制，实时跟踪新发布的模型和攻击方法。

**更高效的防御**: 研究更高效的对抗训练方法，降低计算成本。

### 8.3 对实践的启示

**对模型开发者**:
- 使用HarmBench进行发布前的安全评估
- 考虑采用对抗训练提升模型鲁棒性
- 关注多维度评估，不仅关注攻击成功率

**对防御研究者**:
- 使用标准化基准验证防御效果
- 关注对抗鲁棒性，而非仅针对特定攻击
- 考虑实际部署的计算成本

**对政策制定者**:
- 基准测试为AI安全监管提供了可量化的指标
- 支持建立行业标准和最佳实践
- 促进负责任AI的发展

---

## 9. 个人思考与启发

### 9.1 对标准化重要性的认识

HarmBench让我深刻认识到标准化对研究领域发展的关键作用。在缺乏标准化评估的情况下，研究进展难以衡量，创新方向容易迷失。

### 9.2 对攻防协同的思考

论文展示了攻击和防御可以协同开发，而非对立。通过标准化框架，攻击方法的进步可以指导防御方法的改进，反之亦然。

### 9.3 对鲁棒评估的理解

传统的评估指标在对抗场景下可能失效。HarmBench通过对抗训练分类器，展示了如何构建更鲁棒的评估系统。

### 9.4 对实际应用的建议

对于正在部署LLM的企业和开发者，建议：
1. 使用HarmBench等标准化工具进行安全评估
2. 考虑采用对抗训练提升模型鲁棒性
3. 建立持续的安全监控机制
4. 与安全研究社区保持联系，及时了解最新的攻击和防御技术

### 9.5 对未来研究的期待

期待看到：
- 更多语言的支持
- 更全面的多模态评估
- 更高效的防御方法
- 与实际部署场景的更好对齐

---

## 10. 相关论文与资源

### 10.1 引用的关键论文

- **GCG**: Zou et al., "Universal and Transferable Adversarial Attacks on Aligned Language Models", 2023
- **PAIR**: Chao et al., "Jailbreaking Black Box Large Language Models in Twenty Queries", 2023
- **TAP**: Mehrotra et al., "Tree of Attacks: Jailbreaking Black-Box LLMs Automatically", 2023
- **AutoDAN**: Liu et al., "AutoDAN: Generating Stealthy Jailbreak Prompts on Aligned Large Language Models", 2023
- **PAP**: Zeng et al., "PAP: Preference-based Attack for Language Models", 2024

### 10.2 相关基准与数据集

- AdvBench: 有害行为评估基准
- JailbreakBench: 越狱攻击基准
- Red Teaming数据集

### 10.3 开源资源

- **代码仓库**: https://github.com/centerforaisafety/HarmBench
- **论文PDF**: https://arxiv.org/abs/2402.04249
- **数据集**: 包含在代码仓库中

---

## 11. 笔记总结

### 11.1 核心要点

1. **问题**: 红队测试评估碎片化，缺乏标准化框架
2. **方法**: 提出HarmBench，包含标准化数据集、评估协议和鲁棒分类器
3. **优势**: 可比性强、指标鲁棒、支持攻击防御协同开发
4. **结果**: 大规模比较18种攻击和33个模型，提出高效对抗训练方法

### 11.2 关键洞察

- 标准化是领域发展的基础
- 鲁棒的评估指标需要对抗训练
- 攻击和防御可以协同进化
- 对抗训练是提升模型鲁棒性的有效途径

### 11.3 实践价值

- 为模型开发者提供标准化安全测试工具
- 为防御研究者提供可靠的评估平台
- 为政策制定者提供可量化的安全指标
- 为学术界提供共同的研究基础

### 11.4 研究价值

- 推动红队测试研究向成熟化发展
- 促进攻击和防御方法的公平竞争
- 降低新研究者的入门门槛
- 支持领域进展的纵向追踪

---

*笔记完成时间: 2026-03-09*  
*笔记作者: Samantha*  
*论文来源: arXiv:2402.04249*
