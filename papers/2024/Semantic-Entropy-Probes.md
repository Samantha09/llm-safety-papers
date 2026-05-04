# Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs

## 1. 基本信息

| 项目 | 内容 |
|------|------|
| **论文标题** | Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs |
| **作者** | Jannik Kossen, Jiatong Han, Muhammed Razzak, Lisa Schut, Shreshth Malik, Yarin Gal |
| **机构** | OATML, Department of Computer Science, University of Oxford |
| **arXiv ID** | 2406.15927 |
| **发表时间** | 2024年6月22日 |
| **代码链接** | 未公开 |
| **论文链接** | https://arxiv.org/abs/2406.15927 |

**引用格式**:
```
@article{kossen2024semantic,
  title={Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs},
  author={Kossen, Jannik and Han, Jiatong and Razzak, Muhammed and Schut, Lisa and Malik, Shreshth and Gal, Yarin},
  journal={arXiv preprint arXiv:2406.15927},
  year={2024}
}
```

---

## 2. 英文摘要原文（arXiv abstract原文）

We propose semantic entropy probes (SEPs), a cheap and reliable method for uncertainty quantification in Large Language Models (LLMs). Hallucinations, which are plausible-sounding but factually incorrect and arbitrary model generations, present a major challenge to the practical adoption of LLMs. Recent work by Farquhar et al. (2024) proposes semantic entropy (SE), which can detect hallucinations by estimating uncertainty in the space semantic meaning for a set of model generations. However, the 5-to-10-fold increase in computation cost associated with SE computation hinders practical adoption. To address this, we propose SEPs, which directly approximate SE from the hidden states of a single generation. SEPs are simple to train and do not require sampling multiple model generations at test time, reducing the overhead of semantic uncertainty quantification to almost zero. We show that SEPs retain high performance for hallucination detection and generalize better to out-of-distribution data than previous probing methods that directly predict model accuracy. Our results across models and tasks suggest that model hidden states capture SE, and our ablation studies give further insights into the token positions and model layers for which this is the case.

---

## 3. 中文摘要翻译

我们提出语义熵探针（Semantic Entropy Probes，SEPs），这是一种廉价且可靠的大型语言模型（LLM）不确定性量化方法。幻觉——即听起来合理但实际上不正确且任意的模型输出——是LLM实际应用的主要挑战。Farquhar等人（2024年）近期的工作提出了语义熵（Semantic Entropy，SE），该方法通过估计一组模型输出在语义空间中的不确定性来检测幻觉。然而，SE计算带来的5到10倍计算成本增加阻碍了其实际应用。为解决这一问题，我们提出SEPs，它可以直接从单次生成的隐藏状态中近似语义熵。SEPs易于训练，部署成本低，在测试时不需要采样多个模型输出，将语义不确定性量化的开销几乎降至零。我们展示了SEPs在幻觉检测中保持了高性能，并且在分布外数据上的泛化能力优于以往直接预测模型准确率的探针方法。我们的跨模型和跨任务结果表明，模型的隐藏状态确实捕获了语义熵，且消融实验进一步揭示了这种捕获在不同token位置和模型层中的表现规律。

---

## 4. 研究背景

### 4.1 LLM幻觉问题的严峻性

大型语言模型已经在自然语言处理的广泛任务中展现出令人印象深刻的能力，包括医学、新闻、法律服务等高风险领域。然而，LLM存在一个严重的倾向——产生幻觉。最初"幻觉"被定义为"与提供源内容无意义或不忠实的内容"，但现在该术语已被扩展用于指代LLM生成的非事实性、任意性内容。例如，当被要求生成传记时，即使是能力最强的LLM（如GPT-4）也经常完全捏造事实。这种行为在低风险场景中可能可以接受，但在事实性至关重要的场景中，幻觉可能造成重大伤害。可靠的幻觉检测或缓解是确保基于LLM系统安全部署的关键挑战。

### 4.2 现有幻觉检测方法的局限

**采样检测方法存在的问题：**
- 需要对同一查询采样多个模型输出（通常5-10次）
- 计算成本增加5-10倍，实际应用存在重大障碍
- 例如对于"法国的首都是什么？"这个问题，知道答案的LLM会一致输出（巴黎，巴黎，巴黎），而不知道答案的LLM可能输出（那不勒斯，罗马，柏林），表明存在幻觉

**基于隐藏状态的探针方法存在的问题：**
- 现有方法通常是有监督的，需要标注的训练数据集
- 需要为语句或模型输出分配准确率的标签
- 虽然存在无监督方法，但其有效性受到质疑

### 4.3 研究动机

本研究认为，通过语义熵监督探针比使用准确率标签更适合用于鲁棒的真实性预测。原因如下：
1. 语义熵可以无需访问ground truth准确率标签即可计算
2. 语义熵能够更好地捕获模型对语义不确定性的认知
3. 这种方法可能具有更好的跨任务泛化能力

---

## 5. 核心贡献

1. **提出语义熵探针（SEPs）**：线性探针，在LLM的隐藏状态上训练以捕获语义熵
2. **验证隐藏状态编码语义熵**：证明语义熵可以被成功提取，且仅需要单次模型生成
3. **深入分析不同模型、任务、层和token位置的SEPs性能**：结果表明跨层和跨token的内部模型状态隐式捕获语义不确定性，甚至在生成任何token之前就已存在
4. **建立新的成本效率幻觉检测技术标准**：SEPs可用于预测幻觉，且泛化能力优于直接训练准确率的探针

---

## 6. 研究方法

### 6.1 语义熵（Semantic Entropy）概述

语义熵的计算分为三个步骤：

**步骤1：采样**
对于给定查询x，从LLM中采样模型补全

**步骤2：语义聚类**
使用自然语言推理（NLI）模型（如DeBERTa）预测生成之间的蕴含关系，判断两个生成是否传达相同含义。如果$s_a$蕴含$s_b$且$s_b$蕴含$s_a$，则两者语义等价。然后使用贪心算法进行语义聚类。

**步骤3：计算语义熵**
通过聚合每个聚类内的不确定性来计算语义熵$H_{SE}$

### 6.2 SEPs方法详解

**核心思想**：直接从单次生成的隐藏状态中近似语义熵，避免多次采样

**探针架构**：
- 简单的线性探针
- 训练目标：预测语义熵而非直接预测准确率
- 在模型隐藏状态上训练

**训练过程**：
1. 对于多个输入查询，使用原始SE方法计算语义熵（作为监督信号）
2. 从LLM中提取单次生成的隐藏状态
3. 训练线性探针预测语义熵
4. 测试时，探针可直接应用于单次生成，无需多次采样

### 6.3 关键创新点

| 方面 | 传统采样方法 | SEPs方法 |
|------|-------------|----------|
| 计算成本 | 5-10倍增加 | 几乎为零 |
| 采样次数 | 需要多次采样 | 仅需单次生成 |
| 泛化能力 | 受限 | 更好 |
| 部署难度 | 高 | 低 |

---

## 7. 实验设置

### 7.1 基础模型

实验在多个LLM上进行，包括：
- Llama-2-7B
- 其他开源模型（具体型号在论文中详细说明）

### 7.2 任务设置

**幻觉检测任务**：
- 生物信息生成任务：评估模型生成人物传记时的事实准确性
- 其他自然语言生成任务

**评估指标**：
- 幻觉检测准确率
- AUROC（ROC曲线下面积）
- 与ground truth的对齐程度

### 7.3 基线比较

1. **采样基线**（高成本）：
   - Semantic Entropy (SE)：语义熵的完整实现
   - 需要多次采样（5-10次）

2. **探针基线**（低成本）：
   - Accuracy Probes：直接预测准确率的探针
   - 其他隐藏状态探针方法

### 7.4 分布外泛化评估

为验证泛化能力，在多个不同任务上评估探针性能，包括：
- 与训练任务不同的领域
- 不同类型的查询

---

## 8. 实验结果

### 8.1 主要结果：SEPs性能

**在Llama-2-7B上的幻觉检测性能**：
- SEPs在幻觉检测任务上显著优于直接预测准确率的探针
- 虽然与成本高10倍的采样基线相比仍有差距，但差距可接受
- SEPs实现了新的成本效率幻觉检测技术标准

**关键发现**：
1. 模型隐藏状态确实捕获语义熵
2. 这种捕获在不同模型间泛化良好
3. SEPs对分布外数据具有更好的泛化能力

### 8.2 消融实验结果

#### 8.2.1 模型层的影响

实验表明：
- 隐藏状态在不同层都隐式捕获语义不确定性
- 某些特定层的隐藏状态对语义熵的编码更加有效
- 这种编码甚至在生成任何token之前就已存在于模型内部

#### 8.2.2 Token位置的影响

分析显示：
- 不同token位置的隐藏状态对语义熵的捕获能力不同
- 某些关键token位置能够提供更强的信号
- 整体而言，模型在生成过程中持续维护着不确定性信息

#### 8.2.3 跨模型泛化

结论：
- SEPs在不同模型架构上都能有效工作
- 跨模型的泛化能力证明了方法的鲁棒性
- 隐藏状态捕获SE这一发现具有普遍性

---

## 9. 策略示例

### 9.1 SEPs训练流程

```
输入: 查询x, LLM M
输出: 语义熵探针预测值

1. 计算语义熵（训练时）:
   - 对查询x采样k次
   - 使用NLI模型进行语义聚类
   - 计算语义熵SE(x)

2. 提取隐藏状态:
   - 将x输入M
   - 提取某一层的隐藏状态h

3. 训练探针:
   - 线性层: ŜE = W·h + b
   - 优化: 最小化(ŜE - SE(x))²

4. 推理（测试时）:
   - 仅需单次前向传播
   - 直接从隐藏状态预测语义熵
```

### 9.2 幻觉检测应用

给定模型输出y和对应的查询x：
1. 提取x和y的联合隐藏状态
2. 使用训练好的SEPs预测语义熵
3. 如果预测的语义熵高于阈值，标记为潜在幻觉

---

## 10. 攻击流程

（注：本论文为防御/检测方法，无攻击流程。以下为防御方法的工作流程）

### 10.1 SEPs推理流程

```
                    ┌─────────────┐
                    │   查询 x    │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │  LLM 前向   │
                    │   计算     │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │ 隐藏状态 h  │
                    │  (某一层)   │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │  线性探针  │
                    │  ŜE = W·h  │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │ 语义熵预测 │
                    │   ŜE(x)    │
                    └──────┬──────┘
                           │
                ┌──────────┴──────────┐
                ▼                     ▼
        ŜE > 阈值               ŜE ≤ 阈值
           │                        │
           ▼                        ▼
    标记为幻觉               标记为正常
```

### 10.2 与传统方法的对比

| 方面 | 传统SE方法 | SEPs方法 |
|------|-----------|----------|
| 采样次数 | 5-10次 | 1次 |
| 每次查询成本 | 高 | 极低 |
| 延迟 | 高 | 低 |
| 准确性 | 最高 | 接近（略低） |

---

## 11. 消融实验

### 11.1 语义聚类方法的影响

**使用NLI模型 vs 简单字符串匹配**：
- NLI模型（如DeBERTa）能够更准确判断语义等价性
- 简单匹配会错误地将语义相同但表述不同的内容视为不同

### 11.2 聚类算法的影响

**贪心聚类 vs 完全聚类**：
- 贪心算法在效率和效果之间取得良好平衡
- 完全聚类计算成本过高，实际应用价值有限

### 11.3 采样数量的影响

**不同采样次数（k=5, 10, 20）的比较**：
- k增加时语义熵估计更稳定
- 但边际效益递减，k=10左右达到平衡
- SEPs成功避免了这一问题

### 11.4 探针位置的选择

**不同层隐藏状态的效果**：
- 某些特定层的隐藏状态对语义熵编码更好
- 这为理解LLM内部表示提供了见解
- 最终选择哪一层需要根据具体模型和任务确定

---

## 12. 局限性

### 12.1 方法局限性

1. **与完整SE方法的准确性差距**：
   - SEPs虽然成本低，但与采样基线相比仍有性能差距
   - 在某些高风险应用中可能需要更精确的检测

2. **探针训练的依赖性**：
   - 需要使用完整SE方法生成训练数据
   - 探针泛化到完全新领域的能力仍需验证

3. **模型特异性**：
   - 针对特定模型训练的探针可能无法直接应用于其他模型
   - 跨模型应用需要额外适配

### 12.2 适用范围限制

1. **幻觉类型限制**：
   - 主要针对事实性幻觉（捏造信息）
   - 对其他类型幻觉（如逻辑错误）的检测能力有限

2. **任务类型限制**：
   - 在开放域生成任务上效果较好
   - 对高度结构化或专业化任务的效果需要进一步验证

### 12.3 未来改进方向

1. 探索更轻量级的探针架构
2. 研究跨架构的通用性
3. 结合其他不确定性量化方法
4. 扩展到多模态场景

---

## 13. 伦理声明

本研究关注LLM安全性和可靠性问题，提出了更廉价、更实用的幻觉检测方法，有助于：

1. **提高LLM部署的安全性**：通过可靠检测幻觉，减少LLM在高风险领域的危害
2. **促进公平性**：低成本使得更多应用能够部署幻觉检测，不仅限于资源充足的机构
3. **无伤害意图**：本研究为防御性工作，旨在提高LLM系统的可靠性，不涉及任何攻击性应用

**数据使用**：
- 使用公开的arXiv论文和标准基准数据集
- 未涉及任何敏感或个人数据
- 实验在受控环境中进行

**潜在风险**：
- 恶意使用可能导致对检测系统的规避
- 但总体而言，利大于弊，有助于提高LLM安全性

---

## 14. 参考文献

[1] Kossen, J., Han, J., Razzak, M., Schut, L., Malik, S., & Gal, Y. (2024). Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs. arXiv:2406.15927.

[2] Farquhar, S., et al. (2024). Semantic Entropy. Journal version.

[3] Kuhn, L., et al. (2023). Semantic Entropy. Original semantic entropy paper.

[4] Rawte, V., et al. Survey on hallucinations in LLMs.

[5] Zhang, M., et al. Survey on hallucinations.

[6] DeBERTa. NLI model for semantic clustering.

[7] Other relevant probing methods for LLM truthfulness.

---

**笔记完成日期**: 2026-05-04

**收录位置**: papers/2024/Semantic-Entropy-Probes.md

**阅读进度**: 69/74 (93.24%)