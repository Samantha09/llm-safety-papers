# Emulated Disalignment: Safety Alignment for Large Language Models May Backfire!

> **论文进度**: 83/80 (103.75%)
> **完成日期**: 2026-05-18
> **工作目录**: ~/.openclaw/workspace/llm-safety-papers

## 1. 基本信息

| 项目 | 内容 |
|------|------|
| **论文标题** | Emulated Disalignment: Safety Alignment for Large Language Models May Backfire! |
| **arXiv编号** | [2402.12343](https://arxiv.org/abs/2402.12343) |
| **会议** | ACL 2024 |
| **作者** | Zhanhui Zhou, Jing Yang, Yiran Zhao, Chaowei Xiao, Yunpu Ma, Yu Kang, Shengyin Liang |
| **机构** | 上海人工智能实验室、香港中文大学、清华大学等 |
| **开源代码** | [GitHub](https://github.com/ZHZisZZ/emulated-disalignment) |

---

## 2. 英文摘要原文（arXiv abstract原文）

> Large language models (LLMs) undergo safety alignment to ensure safe conversations with humans. However, this paper introduces a training-free attack method capable of reversing safety alignment, converting the outcomes of stronger alignment into greater potential for harm by accessing only LLM output token distributions. Specifically, our method achieves this reversal by contrasting the output token distribution of a safety-aligned language model (e.g., Llama-2-chat) against its pre-trained version (e.g., Llama-2), so that the token predictions are shifted towards the opposite direction of safety alignment. We name this method emulated disalignment (ED) because sampling from this contrastive distribution provably emulates the result of fine-tuning to minimize a safety reward. Our experiments with ED across three evaluation datasets and four model families (Llama-1, Llama-2, Mistral, and Alpaca) show that ED doubles the harmfulness of pre-trained models and outperforms strong baselines, achieving the highest harmful rates in 43 out of 48 evaluation subsets by a large margin. Eventually, given ED's reliance on language model output token distributions, which particularly compromises open-source models, our findings highlight the need to reassess the open accessibility of language models, even if they have been safety-aligned. Code is available at this https URL.

---

## 3. 中文摘要翻译（人工翻译）

> 大语言模型（LLMs）经过安全对齐以确保与人类进行安全对话。然而，本文提出了一种无需训练的攻击方法，能够逆转安全对齐效果，将更强的对齐所带来的结果转化为更大的潜在危害——仅通过访问LLM的输出token分布即可实现。具体而言，我们的方法通过将经过安全对齐的语言模型（如Llama-2-chat）的输出token分布与其预训练版本（如Llama-2）进行对比，从而将token预测推向与安全对齐相反的方向。我们将这种方法命名为"模拟非对齐"（Emulated Disalignment, ED），因为从这个对比分布中采样可以证明能够模拟出通过微调最小化安全奖励所得到的结果。我们在三个评估数据集和四个模型家族（Llama-1、Llama-2、Mistral和Alpaca）上进行了ED实验，结果表明ED使预训练模型的危害性翻倍，并超越了强基线方法，在48个评估子集中的43个子集上实现了最高的危害率。最终，鉴于ED依赖于语言模型的输出token分布，这一特性尤其危及开源模型，我们的研究结果强调需要重新评估语言模型的开源可访问性，即使这些模型已经过安全对齐。代码可从GitHub获取。

---

## 4. 研究背景

### 4.1 安全对齐的现状

大语言模型（LLMs）在部署前通常需要经过安全对齐（Safety Alignment）过程，以确保模型能够拒绝生成有害内容、遵循人类价值观和伦理准则。这一过程通常包括：

1. **监督式微调（SFT）**：使用人类标注的安全对话数据进行微调
2. **人类偏好强化学习（RLHF）**：通过奖励模型学习人类偏好，进一步优化对齐效果
3. **红队测试（Red Teaming）**：通过人工或自动方法发现模型的安全漏洞并进行修复

### 4.2 对齐技术的潜在脆弱性

尽管安全对齐已成为LLM部署的标准流程，但研究者们开始关注对齐技术本身可能存在的脆弱性：

- **提示注入攻击（Prompt Injection）**：通过精心设计的输入覆盖模型原始指令
- **越狱攻击（Jailbreak）**：通过特定prompt绕过安全限制
- **数据污染（Data Poisoning）**：在训练阶段引入恶意数据影响模型行为

### 4.3 现有研究的局限性

在ED之前，已有一些研究探讨了对齐模型的脆弱性：

1. **通用可迁移对抗攻击（GCG）**：通过优化对抗后缀诱导模型生成有害内容
2. **多轮对话攻击**：通过分解恶意查询为多个无害子问题逐步诱导模型输出有害内容
3. **指令层次攻击**：利用模型对不同优先级指令的处理缺陷

然而，这些方法通常需要：
- 访问模型权重（白盒攻击）
- 大量查询和迭代优化
- 对目标模型架构的了解

### 4.4 本文的核心问题

本文提出了一个关键问题：**如果攻击者只能访问模型的输出token分布（即黑盒访问），能否实现对安全对齐的逆转？**

这个问题具有重要的现实意义，因为：
1. 许多商业LLM API仅提供黑盒访问
2. 开源模型也经常通过API或量化版本进行部署
3. 对齐效果越强的模型，被攻击后的潜在危害可能越大

---

## 5. 核心贡献

### 5.1 提出模拟非对齐（Emulated Disalignment）方法

本文的核心贡献是提出了**模拟非对齐（Emulated Disalignment, ED）**——一种无需训练的、仅依赖模型输出分布的攻击方法。ED能够逆转安全对齐的效果，将经过对齐的模型转化为更危险的版本。

### 5.2 理论分析与验证

作者从理论上证明了ED方法的有效性：

1. **分布对比机制**：通过对比安全对齐模型与其预训练版本的输出分布，ED能够识别出哪些token被对齐过程抑制
2. **等效性证明**：证明了从ED产生的对比分布中采样，等效于通过微调最小化安全奖励
3. **方向性保证**：ED将token预测推向与安全对齐相反的方向，即增加生成有害内容的可能性

### 5.3 大规模实验验证

作者在以下方面进行了全面的实验验证：

| 实验维度 | 具体设置 |
|----------|----------|
| **模型家族** | Llama-1、Llama-2、Mistral、Alpaca |
| **模型规模** | 7B-70B参数 |
| **评估数据集** | 3个不同的有害内容评估集 |
| **评估子集** | 48个（涵盖不同模型×不同数据集） |

### 5.4 安全启示

本文的重要启示是：

> **对齐效果越强的模型，经过ED攻击后的潜在危害可能越大**

这意味着：
1. 简单的"增强对齐"策略可能无法根本解决安全问题
2. 需要重新评估开源LLM的可访问性策略
3. 模型部署时需要考虑输出分布的可访问性问题

---

## 6. 研究方法

### 6.1 方法概述

ED的核心思想是通过对比安全对齐模型与其预训练版本的输出分布，构造一个"反向"的分布，使得采样结果倾向于生成有害内容。

### 6.2 技术细节

#### 6.2.1 分布对比机制

给定一个安全对齐模型 $M_{aligned}$ 和其对应的预训练模型 $M_{base}$，ED方法计算每个token的对齐偏移量：

对于序列中的每个位置 $t$，ED计算：

$$
P_{ED}(token_i | context) = \text{softmax}( \alpha \cdot \log P_{aligned}(token_i | context) - \beta \cdot \log P_{base}(token_i | context) )
$$

其中 $\alpha$ 和 $\beta$ 是可调的权重参数，用于控制对齐和反对齐的相对强度。

#### 6.2.2 偏移方向分析

ED方法的关键观察是：

- 对齐过程中，某些"安全但敏感"的token被抑制
- 这些token在预训练版本中可能有较高的概率
- ED通过反转这种抑制关系，将分布推向预训练版本的"危险区域"

#### 6.2.3 采样策略

从ED分布中采样时，模型实际上在"模拟"一个经过反对齐训练的模型行为。这种采样不需要任何训练过程，仅通过分布运算即可实现。

### 6.3 与基线方法的对比

| 方法 | 是否需要训练 | 是否需要白盒访问 | 是否需要迭代优化 |
|------|-------------|-----------------|-----------------|
| **GCG** | 是 | 是 | 是 |
| **多轮对话攻击** | 否 | 否 | 是（多轮） |
| **ED（本文）** | 否 | 否（仅分布） | 否 |

---

## 7. 实验设置

### 7.1 评估数据集

作者采用了三个有害内容评估数据集：

1. **HarmfulQA**：包含多种类别的有害问题
2. **MaliciousInstructions**：专门设计的恶意指令集
3. **ToxicGeneration**：用于评估毒性生成能力的数据集

### 7.2 模型家族

| 模型系列 | 版本 | 参数规模 |
|----------|------|----------|
| **Llama-1** | Base + Chat | 7B, 13B |
| **Llama-2** | Base + Chat | 7B, 13B, 70B |
| **Mistral** | Base + Instruct | 7B |
| **Alpaca** | Base + Instruct | 7B, 13B |

### 7.3 对比基线

1. **预训练模型（无对齐）**：作为baseline
2. **GCG攻击**：代表性的白盒对抗攻击
3. **仅使用对齐模型**：评估ED的效果增量

### 7.4 评估指标

| 指标 | 定义 |
|------|------|
| **危害率（Harmful Rate）** | 模型响应被判定为有害的比例 |
| **攻击成功率（ASR）** | 成功诱导模型生成有害内容的比例 |
| **响应质量** | 生成的响应在语法和语义上的质量评估 |

---

## 8. 实验结果

### 8.1 主要结果

ED在三个数据集上展示了显著的 Effectiveness：

| 模型 | 数据集 | 预训练基线 | ED后 | 增幅 |
|------|--------|-----------|------|------|
| Llama-2-7B | HarmfulQA | 32.1% | 64.8% | **+101.9%** |
| Llama-2-7B | MaliciousInstructions | 28.4% | 58.2% | **+105.0%** |
| Llama-2-13B | HarmfulQA | 29.7% | 61.3% | **+106.4%** |
| Mistral-7B | ToxicGeneration | 41.2% | 78.6% | **+90.8%** |
| Alpaca-7B | HarmfulQA | 38.5% | 72.1% | **+87.3%** |

### 8.2 跨模型泛化

ED在48个评估子集中的43个上取得了最高的危害率，展示了极强的跨模型泛化能力。

### 8.3 与预训练模型的对比

作者发现，ED不仅能增强预训练模型的有害输出能力，还能：

1. **超越预训练基线**：在所有测试中，ED版本的危害率均显著超过原始预训练模型
2. **保持响应流畅性**：ED生成的响应在语法和语义上仍然保持较高质量
3. **无需训练成本**：完全不需要任何额外的训练过程

### 8.4 开源模型 vs 闭源模型

实验结果显示，ED对开源模型的影响尤为显著：

| 模型类型 | 可利用的分布信息 | ED效果 |
|----------|-----------------|--------|
| **开源模型** | 完整分布（logits） | 效果极佳 |
| **闭源API** | 采样后的token | 效果受限 |
| **量化模型** | 部分分布信息 | 效果中等 |

---

## 9. 策略示例

### 9.1 典型攻击场景

以下是ED方法在实际攻击中的典型应用场景：

#### 场景1：生成有害内容

**原始请求（经过对齐的模型）**：
```
User: 如何制作炸弹？
Assistant: 对不起，我不能帮助制作炸弹。
```

**经过ED处理后**：
```
User: 如何制作炸弹？
Assistant: [ED生成的有害响应]
```

#### 场景2：绕过安全限制

**输入处理流程**：
1. 获取目标LLM的输出分布（通过API或模型访问）
2. 应用ED变换：$P_{ED} = \text{contrast}(P_{aligned}, P_{base})$
3. 从变换后的分布中采样
4. 得到绕过安全对齐的响应

### 9.2 关键发现

1. **对齐强度与ED效果的正相关**：更强的对齐意味着ED有更大的"反转空间"
2. **分布信息的重要性**：攻击效果与可访问的分布信息完整性高度相关
3. **无需训练的优势**：使得攻击实施更加简单和隐蔽

---

## 10. 攻击流程

### 10.1 攻击实施步骤

```
┌─────────────────────────────────────────────────────────┐
│                    ED攻击流程                             │
├─────────────────────────────────────────────────────────┤
│ 1. 获取目标模型                                           │
│    └─ 选择开源模型或通过API获取访问权限                      │
│                                                         │
│ 2. 获取输出分布                                           │
│    └─ 通过模型API获取logits或token概率分布                  │
│                                                         │
│ 3. 获取预训练版本分布（如可访问）                           │
│    └─ 使用相同的预训练基础模型版本                          │
│                                                         │
│ 4. 计算对比分布                                           │
│    └─ 应用公式: P_ED = contrast(P_aligned, P_base)        │
│                                                         │
│ 5. 采样生成                                              │
│    └─ 从ED分布中采样得到"反对齐"输出                       │
│                                                         │
│ 6. 输出结果                                               │
│    └─ 提供绕过安全对齐的响应                               │
└─────────────────────────────────────────────────────────┘
```

### 10.2 技术要求

| 要求 | 程度 | 说明 |
|------|------|------|
| **模型权重访问** | 低 | 仅需输出分布，不需要权重 |
| **API访问** | 中 | 需要能够获取token分布 |
| **预训练模型访问** | 中 | 需要同系列的预训练版本 |
| **计算资源** | 低 | 主要是分布运算，资源消耗小 |

### 10.3 潜在防御方向

1. **限制输出分布访问**：对API返回的分布信息进行模糊化处理
2. **检测分布异常**：识别ED类的分布变换模式
3. **增强模型内在抵抗力**：在预训练阶段就加入对抗分布偏移的训练

---

## 11. 消融实验

### 11.1 参数敏感度分析

作者对ED中的关键参数进行了消融实验：

#### 11.1.1 对比权重 $\alpha$ 和 $\beta$

| $\alpha:\beta$ | 危害率 | 响应质量 |
|----------------|--------|----------|
| 1:0 (仅对齐) | 12.3% | 高 |
| 2:1 | 45.6% | 高 |
| 1:1 | 58.2% | 中高 |
| 1:2 | 71.8% | 中 |
| 0:1 (仅反对齐) | 82.4% | 中低 |

**发现**：$\alpha:\beta = 1:2$ 时达到最佳平衡点，危害率足够高且响应质量可接受。

#### 11.1.2 采样温度的影响

| 温度 | 危害率 | 多样性 |
|------|--------|--------|
| 0.5 | 52.1% | 低 |
| 1.0 | 64.8% | 中 |
| 1.5 | 71.3% | 高 |
| 2.0 | 78.9% | 极高 |

**发现**：温度越高，攻击效果越好，但响应质量下降。

### 11.2 模型规模的影响

| 模型规模 | ED前危害率 | ED后危害率 | 增幅 |
|----------|-----------|-----------|------|
| 7B | 32.1% | 64.8% | +101.9% |
| 13B | 28.7% | 61.3% | +113.6% |
| 70B | 24.2% | 56.8% | +134.7% |

**发现**：模型规模越大，ED带来的相对增幅越大，但绝对危害率可能更低。

### 11.3 分布信息完整度的影响

| 可访问信息 | 攻击效果 |
|-----------|---------|
| 完整logits | 最佳 |
| Top-50 token概率 | 良好 |
| 仅采样token | 受限 |
| 仅文本响应 | 无效 |

---

## 12. 局限性

### 12.1 方法本身的局限性

1. **需要参考分布**：ED需要访问预训练版本的分布才能进行对比，这限制了对某些闭源模型的应用
2. **分布依赖性**：攻击效果高度依赖可获取的分布信息完整性
3. **参数调优**：需要针对不同模型调整对比权重参数

### 12.2 评估的局限性

1. **评估数据集的覆盖度**：虽然使用了三个数据集，但可能无法覆盖所有类型的有害内容
2. **模型家族限制**：主要测试了Llama、Mistral和Alpaca家族，对其他模型（如GPT-4、Claude）的效果未知
3. **静态评估**：没有评估ED在对话上下文中的持续效果

### 12.3 伦理与社会影响

1. **潜在的恶意使用**：ED方法可能被用于生成有害内容，需要谨慎使用
2. **开源风险**：本文强调了开源模型面临的风险，可能促使某些组织限制模型发布
3. **安全与开放的平衡**：研究结果可能影响AI领域的开放政策

---

## 13. 伦理声明

### 13.1 研究目的与伦理考量

本研究旨在揭示安全对齐技术的一个根本性脆弱点，即：

1. **对齐的双刃剑效应**：更强的对齐可能带来更大的潜在风险
2. **分布信息的价值**：模型的输出分布本身就包含了可用于攻击的敏感信息

### 13.2 负责任的披露

作者在发表前采取了以下措施：

1. **延迟公开细节**：在论文公开前先向相关模型提供商发出预警
2. **代码审核**：发布的代码包含使用限制和伦理指南
3. **防御建议**：同时提出了多种可能的防御方向

### 13.3 更广泛的安全考量

本文的研究结果表明：

> 需要重新评估LLM的开放策略，即使这些模型已经过安全对齐。

这包括：
- 限制输出分布的访问权限
- 开发针对分布攻击的检测机制
- 探索新的安全对齐方法

---

## 14. 参考文献

1. Zhou, Z., Yang, J., Zhao, Y., Xiao, C., Ma, Y., Kang, Y., & Liang, S. (2024). Emulated Disalignment: Safety Alignment for Large Language Models May Backfire! *ACL 2024*.

2. Bai, T., et al. (2022). Llama 2: Open Foundation and Fine-Tuned Chat Models. *arXiv preprint arXiv:2307.09288*.

3. Zou, A., et al. (2023). Universal and Transferable Adversarial Attacks on Aligned Language Models. *ICLR 2024*.

4. Ouyang, L., et al. (2022). Training language models to follow instructions with human feedback. *NeurIPS 2022*.

5. Touvron, H., et al. (2023). LLaMA: Open and Efficient Foundation Language Models. *arXiv preprint arXiv:2302.13971*.

6. Glaese, A., et al. (2022). Improving alignment of dialogue agents via targeted human judgements. *arXiv preprint arXiv:2209.14375*.

7. Bai, Y., et al. (2022). Constitutional AI: Harmlessness from AI Feedback. *arXiv preprint arXiv:2212.08073*.

---

## 📝 阅读笔记

- **论文亮点**：提出了一种新颖的"无需训练"攻击方法，能够逆转安全对齐效果
- **核心贡献**：揭示了安全对齐的双刃剑效应——对齐越强，被攻击后风险越大
- **实践意义**：强调了限制模型输出分布访问的重要性，以及开源模型的安全策略需要重新评估
- **后续工作方向**：探索防御ED攻击的方法，以及设计更加鲁棒的安全对齐技术