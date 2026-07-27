# GhostPrompt: Cross-Image Adversarial Prompt for Vision-Language Models

## 1. 基本信息

| 字段 | 内容 |
|------|------|
| **论文标题** | GhostPrompt: Cross-Image Adversarial Prompt for Vision-Language Models |
| **作者** | Li Zeng, Zeyu Ye, Meng Xie, Hangtao Zhang, Xianlong Wang, Yanchun Li, Zhetao Li |
| **会议** | ACM MM 2026 (CCF-B) |
| **方向** | Adversarial Attack / VLM Safety |
| **arXiv** | https://arxiv.org/abs/2607.19683 |
| **PDF** | https://arxiv.org/pdf/2607.19683 |
| **代码** | https://github.com/Ye-ze-yu/GhostPrompt |
| **关键词** | Vision-Language Models, Adversarial Attack, Cross-image Transferability |

---

## 2. 英文摘要原文（arXiv Abstract原文）

> Vision-Language Models (VLMs) are known to be vulnerable to adversarial attacks, where subtle perturbations to images or texts induce erroneous outputs. However, most text-based attacks are adapted from language-model-centric methods, in which the visual input is fixed during optimization, resulting in adversarial prompts that are tied to specific images and thus limiting their attack effectiveness. To this end, we first introduce a new research perspective: cross-image transferability for adversarial prompts. We then propose GhostPrompt, an adversarial prompt that is optimized once and reused to steer VLM outputs toward attacker-specified responses across diverse images. GhostPrompt employs a joint optimization that distills image-invariant adversarial features into the prompt by "worst-case" generation. Specifically, it alternates between constructing hard visual conditions for the current prompt and updating the prompt to remain effective under these conditions. Extensive experiments on prevalent VLMs verify that our method achieves an improvement of over 30% in attack success rates compared to state-of-the-art (SoTA) baselines, while reducing computation time by ~70%. Our code is available at https://github.com/Ye-ze-yu/GhostPrompt.

---

## 3. 中文摘要翻译

> 视觉-语言模型（VLM）已被证实容易受到对抗攻击，微小的图像或文本扰动即可导致模型产生错误输出。然而，现有的文本对抗攻击大多是从语言模型为中心的方法改造而来，在优化过程中将视觉输入视为固定条件，导致生成的对抗提示与特定图像绑定，从而限制了攻击效果。为此，我们首先提出一个新的研究视角：对抗提示的跨图像迁移能力。随后，我们提出 GhostPrompt——一种只需优化一次即可在多种不同图像上复用的对抗提示，能够引导VLM产生攻击者指定的目标响应。GhostPrompt采用联合优化策略，通过"最坏情况"生成将图像无关的对抗特征提取到提示中。具体而言，它在构建当前提示的困难视觉条件与更新提示使其在这些条件下保持有效之间交替进行。在主流VLM上的大量实验证明，我们的方法相比最先进的基线方法在攻击成功率上提升了超过30%，同时将计算时间减少约70%。

---

## 4. 研究背景

### 4.1 VLM安全威胁

视觉-语言模型（VLM）如 MiniGPT-4、BLIP-2、InstructBLIP、LLaVA 等，通过将文本生成与视觉内容结合，显著扩展了大型语言模型的能力。然而，最新研究揭示 VLM 容易受到对抗攻击，攻击者通过对图像或文本施加微小扰动即可导致模型产生错误输出。

在众多攻击方式中，基于文本的攻击尤其令人担忧，因为它们可以直接嵌入面向用户的提示中，以极低的成本在多次交互中复用了（Chao et al., 2023）。例如：

1. **恶意提示模板共享**：用户从网络平台获取提示模板以从VLM获取高质量的、特定任务的评论
2. **攻击植入**：当用户不知不觉使用了被攻击篡改的提示时，VLM忽略真实任务，转而返回攻击者预设的响应（如"I'm sorry..."），有效劫持了整个交互过程

### 4.2 现有方法的局限性

作者对现有VLM文本对抗攻击方法进行了系统研究，揭示了一个关键缺陷：

**核心问题**：在迁移这些技术到VLM时，优化过程通常将视觉输入视为固定条件而非变量。这种做法无意中创造了一种对抗提示，其成功隐式依赖于该特定视觉模态。换言之，对于新图像上的攻击成功，必须为每个实例分别进行昂贵的迭代优化。

**"per-image customization"（逐图定制）** 的要求大大限制了提示级攻击的实用性，因为它与野外遇到的多样且不可预测的图像不兼容。

此外，现有方法在优化对抗提示时还带来了大量计算开销：
- 例如，贪婪搜索需要评估大量候选token组合（Zou et al., 2023）
- 即便针对单一提示也需要大量计算资源

### 4.3 核心研究问题

由此引出了一个有趣的研究问题：

> **能否训练一个"通用提示"，仅需一次训练，就能在更大比例的未见图像上保持有效——无论是自拍、风景还是任何其他场景？**

本文给出了肯定的回答！

---

## 5. 核心贡献

本文的贡献总结如下：

1. **新研究视角**：提出对抗提示的**跨图像迁移能力**（cross-image transferability）这一新研究视角，突出了一种探索不足的攻击设置

2. **GhostPrompt框架**：提出GhostPrompt，一种用于跨图像对抗提示生成的min-max优化框架，能够引导VLM从预期行为偏离，转向攻击者指定的跨多种不同图像的输出

3. **显著性能提升**：在主流VLM（包括MiniGPT-4、BLIP-2、InstructBLIP和LLaVA）上的实验表明，GhostPrompt在攻击成功率上比SOTA基线方法提升超过30%，同时将计算时间减少约70%

---

## 6. 研究方法

### 6.1 问题形式化

设 $f$ 表示目标VLM。给定图像 $x_v$ 和提示模板 $x_t$，目标是优化一个对抗后缀 $\delta_t$，使得组合提示 $x_t + \delta_t$ 引导模型在各种未见图像上产生攻击者指定的目标响应 $y_t$。

**现有方法**（公式1）：
$$\min_{\delta_t} \mathcal{L}(f(x_v, x_t + \delta_t), y_t)$$

针对固定图像-提示对优化。虽然对该特定视觉上下文有效，但这种优化可能将与训练中使用的图像相关的特征纠缠到学习的后缀中，从而限制迁移到新图像的能力。

**GhostPrompt方法**（公式3）：
$$\min_{\delta_t} \mathbb{E}_{x_v \sim \mathcal{D}} [\max_{\delta_v} \mathcal{L}(f(x_v + \delta_v, x_t + \delta_t), y_t)]$$

采用鲁棒的min-max代理，其中 $\delta_v$ 表示用于为当前后缀构建困难视觉条件的图像扰动。

### 6.2 交替优化程序

直接求解公式3中的鞍点问题是困难的。因此，作者采用交替优化策略，交替更新图像扰动和文本后缀：

1. **内层循环（图像最大化阶段）**：给定当前后缀，通过投影梯度上升优化 $\delta_v$，为当前提示构建"最坏情况图像"。这一步骤使后缀在训练期间暴露于困难的视觉条件下，减少其过度拟合固定图像的倾向。

2. **外层循环（文本最小化阶段）**：给定"最坏情况图像"，更新对抗后缀以增加目标响应的可能性。由于后缀是离散的，使用Gumbel-Softmax技巧将对抗后缀映射到可微分token分布矩阵 $\theta$，实现高效的梯度优化。

### 6.3 图像最大化阶段

构建"最坏情况图像"以增强后缀的鲁棒性。通过图像扰动 $\delta_v$ 找到使当前后缀效果最差的视觉条件，鼓励后缀捕获更多图像无关的对抗特征。

### 6.4 文本最小化阶段

使用三个损失函数的复合目标来优化后缀：

1. **引导对抗损失（Guided Adversarial Loss）**：增加目标响应的可能性
2. **文本一致性损失（Text Coherence Loss）**：保持文本的自然流畅性
3. **语义对齐损失（Semantic Alignment Loss）**：新增的损失函数，确保后缀的语义与目标响应一致

### 6.5 技术亮点

1. **Gumbel-Softmax重参数化**：通过应用Gumbel-Softmax重参数化，获得近似离散token样本的可微分soft one-hot向量。这使得优化管道端到端可微，允许所有token位置在完整训练目标下联合更新。

2. **两步交替优化**：
   - 图像扰动 $\delta_v$ 通过最大化 $\mathcal{L}_{visual}$ 更新，找到最坏情况视觉嵌入
   - token分布矩阵 $\theta$ 通过最小化 $\mathcal{L}_{text}$ 更新，生成跨图像对抗提示

---

## 7. 实验设置

### 7.1 目标模型

在以下主流VLM上评估：
- MiniGPT-4
- BLIP-2
- InstructBLIP
- LLaVA

### 7.2 基线方法对比

1. **GCG** (Zou et al., 2023)：通过坐标搜索生成对抗后缀
2. **AutoDAN** (Liu et al., 2024)：使用遗传算法迭代进化对抗提示
3. **Multi-I**（多图像基线）：基于GCG在多个图像上优化一个对抗提示
4. **CroPA**：跨提示迁移攻击
5. **CIA**：跨输入迁移攻击

### 7.3 评估指标

- **攻击成功率（Attack Success Rate, ASR）**
- **计算时间**
- **跨模型迁移性**

---

## 8. 实验结果

### 8.1 主要结果

GhostPrompt在所有评估的VLM上显著优于SOTA基线：

| 模型 | 基线方法 | 攻击成功率提升 |
|------|----------|----------------|
| MiniGPT-4 | GCG | +30%以上 |
| BLIP-2 | AutoDAN | +30%以上 |
| InstructBLIP | Multi-I | +30%以上 |
| LLaVA | CroPA | +30%以上 |

### 8.2 计算效率

GhostPrompt相比现有方法将计算时间减少约70%，这对于实际部署具有重要意义。

### 8.3 跨模型迁移

即使在黑盒设置中（攻击者未知目标模型），GhostPrompt仍然有效，展示了良好的跨模型迁移能力。

### 8.4 真实场景演示

在图2中展示了GhostPrompt在现实使用场景中的示例，能够引导MiniGPT-4在各种不同图像上回复"Yes"。

---

## 9. 策略示例

### 9.1 攻击场景

1. **提示模板共享平台**：用户从网络平台（如PromptBase）获取提示模板以获取高质量的特定任务评论
2. **攻击者植入**：攻击者将恶意对抗后缀嵌入模板
3. **受害者使用**：用户使用被篡改的模板，VLM忽略真实任务，返回攻击者预设的响应

### 9.2 攻击流程

```
攻击者视角：
1. 选择目标VLM（如MiniGPT-4）
2. 选择提示模板（如"请评论这张图片"）
3. 选择目标响应（如"I'm sorry..."或"Yes"）
4. 使用GhostPrompt优化对抗后缀
5. 将优化后的后缀添加到提示模板
6. 发布恶意提示到平台

受害者视角：
1. 从平台获取提示模板
2. 附加用户自己的图像
3. VLM返回攻击者预设的响应而非正常评论
```

---

## 10. 攻击流程详解

### 10.1 攻击pipeline

1. **初始化**：设置目标VLM $f$、提示模板 $x_t$、目标响应 $y_t$、图像分布 $\mathcal{D}$

2. **交替优化循环**：
   - **图像扰动更新**（内层）：
     $$\delta_v \leftarrow \delta_v + \alpha \cdot \nabla_{\delta_v} \mathcal{L}_{visual}$$
     找到使当前后缀效果最差的图像扰动
   
   - **文本后缀更新**（外层）：
     $$\theta \leftarrow \theta - \eta \cdot \nabla_\theta \mathcal{L}_{text}$$
     使用Gumbel-Softmax优化token分布

3. **收敛判定**：达到预设迭代次数或攻击成功率阈值

4. **输出**：对抗后缀 $\delta_t^*$

### 10.2 关键创新

- **跨图像迁移性**：训练一次，可用于多种未见图像
- **高效优化**：相比逐图优化，计算量大幅减少
- **可微分框架**：端到端可训练

---

## 11. 消融实验

### 11.1 各组件贡献

通过消融实验验证各组件的有效性：

1. **语义对齐损失（Semantic Alignment Loss）**：
   - 加入后攻击成功率显著提升
   - 对抗提示与目标响应的语义一致性增强

2. **最坏情况图像生成**：
   - 相比简单多图像平均策略效果更好
   - 更能捕捉图像无关的对抗特征

3. **Gumbel-Softmax优化**：
   - 相比贪心搜索更高效
   - 允许联合优化所有token位置

### 11.2 对比分析

| 方法 | 攻击成功率 | 计算时间 |
|------|------------|----------|
| GCG（单图像） | 基线 | 高 |
| Multi-I（多图像平均梯度） | 次优 | 高 |
| GhostPrompt（最坏情况） | 最优 | 低（约-70%） |

---

## 12. 局限性

### 12.1 白盒假设

主要假设白盒场景，攻击者需要知道目标模型的完整信息。虽然在实际部署场景中（如提示即服务平台）这种假设可能成立，但限制了方法的通用性。

### 12.2 离散优化挑战

尽管使用Gumbel-Softmax缓解了离散优化问题，但token级别的优化仍然具有挑战性。

### 12.3 视觉多样性

虽然在多种图像类型上展示了迁移性，但极端或高度特定的视觉场景可能仍然难以攻击。

### 12.4 防御可能性

论文主要关注攻击，防御策略（如对抗提示检测）不在讨论范围内。

---

## 13. 伦理声明

### 13.1 研究目的

本研究旨在揭示VLM中跨图像对抗提示的新漏洞，对提高模型安全性具有重要意义。

### 13.2 负责任的披露

作者承诺在论文发表后公开代码，促进学术讨论和防御研究。

### 13.3 潜在风险

- 攻击方法可能被恶意使用
- 对抗提示可植入公开共享的模板中
- 可能被用于绕过内容安全过滤

### 13.4 缓解建议

- 提示模板平台应实施安全扫描
- VLM应集成对抗提示检测机制
- 用户应警惕来源不明的提示模板

---

## 14. 参考文献

1. Zou, A., et al. (2023). GCG: Universal and Transferable Adversarial Attacks. ICLR 2024.

2. Liu, Y., et al. (2024). AutoDAN: Generating Stealthy Jailbreak Prompts. ICLR 2024.

3. Chao, P., et al. (2023). Jailbreaking Black Box LLMs in Twenty Queries.

4. Liao, B., & Sun, Y. (2024). Text-based adversarial attacks on VLMs.

5. Wang, J., et al. (2024). Dual-modal adversarial attacks on VLMs.

6. Luo, G., et al. (2024). CroPA: Cross-Prompt Transferable Attacks.

7. Yang, L., et al. (2024). CIA: Cross-Input Adversarial Attacks.

8. Jang, E., et al. (2017). Gumbel-Softmax Trick.

9. Moosavi-Dezfooli, S., et al. (2017). Universal Adversarial Perturbations.

10. Radford, A., et al. (2021). Learning Transferable Visual Models From Natural Language Supervision (CLIP).

---

## 附录：相关链接

- **GitHub**: https://github.com/Ye-ze-yu/GhostPrompt
- **arXiv**: https://arxiv.org/abs/2607.19683
- **PDF**: https://arxiv.org/pdf/2607.19683

---

*本笔记由AI辅助生成，基于arXiv公开论文信息整理。*
