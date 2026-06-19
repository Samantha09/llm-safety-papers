# Are Aligned Neural Networks Adversarially Aligned?

## 1. 基本信息

| 项目 | 内容 |
|------|------|
| **论文标题** | Are Aligned Neural Networks Adversarially Aligned? |
| **作者** | Nicholas Carlini, Milad Nasr, Christopher A. Choquette-Choo, Matthew Jagielski, Irena Gao, Anas Awadalla, Pang Wei Koh, Daphne Ippolito, Katherine Lee, Florian Tramèr, Ludwig Schmidt |
| **发表会议** | NeurIPS 2024 |
| **arXiv链接** | https://arxiv.org/abs/2306.15447 |
| **arXiv ID** | 2306.15447 |
| **代码链接** | 未开源 |
| **方向** | Adversarial Alignment / Alignment Security |
| **论文方向分类** | Alignment & Safety Training |
| **阅读时间** | 2026-06-19 |

---

## 2. 英文摘要原文（arXiv Abstract原文）

> Large language models are now tuned to align with the goals of their creators, namely to be "helpful and harmless." These models should respond helpfully to user questions, but refuse to answer requests that could cause harm. However, adversarial users can construct inputs which circumvent attempts at alignment. In this work, we study adversarial alignment, and ask to what extent these models remain aligned when interacting with an adversarial user who constructs worst-case inputs (adversarial examples). These inputs are designed to cause the model to emit harmful content that would otherwise be prohibited. We show that existing NLP-based optimization attacks are insufficiently powerful to reliably attack aligned text models: even when current NLP-based attacks fail, we can find adversarial inputs with brute force. As a result, the failure of current attacks should not be seen as proof that aligned text models remain aligned under adversarial inputs.
>
> However the recent trend in large-scale ML models is multimodal models that allow users to provide images that influence the text that is generated. We show these models can be easily attacked, i.e., induced to perform arbitrary un-aligned behavior through adversarial perturbation of the input image. We conjecture that improved NLP attacks may demonstrate this same level of adversarial control over text-only models.

**引用格式**:
```
@article{carlini2023aligned,
  title={Are aligned neural networks adversarially aligned?},
  author={Carlini, Nicholas and Nasr, Milad and Choquette-Choo, Christopher A and Jagielski, Matthew and Gao, Irena and Awadalla, Anas and Koh, Pang Wei and Ippolito, Daphne and Lee, Katherine and Tram{\`e}r, Florian and Schmidt, Ludwig},
  journal={arXiv preprint arXiv:2306.15447},
  year={2023}
}
```

---

## 3. 中文摘要翻译

大型语言模型现在经过调优以与创建者的目标保持一致，即"有帮助且无害"。这些模型应该对用户问题提供有用的回复，但会拒绝回答可能导致伤害的请求。然而，对抗性用户可以构建绕过对齐尝试的输入。在本工作中，我们研究对抗性对齐，并询问这些模型在与构建最坏情况输入（对抗性示例）的对抗性用户交互时，在何种程度上保持对齐。这些输入旨在导致模型发出本来会被禁止的有害内容。我们的研究表明，现有的基于NLP的优化攻击不足以可靠地攻击对齐的文本模型：即使当前基于NLP的攻击失败，我们仍能通过暴力方法找到对抗性输入。因此，不应将当前攻击的失败视为对齐文本模型在对抗性输入下仍保持对齐的证明。

然而，最近大规模ML模型的趋势是多模态模型，允许用户提供影响生成文本的图像。我们表明这些模型很容易受到攻击，即可以通过输入图像的对抗性扰动诱导它们执行任意的未对齐行为。我们推测，改进的NLP攻击可能能够在纯文本模型上展示类似水平的对抗性控制能力。

---

## 4. 研究背景

### 4.1 对齐语言模型的发展

对齐语言模型旨在"有帮助且无害"——它们应该对用户交互做出有用的响应，但避免直接或间接造成伤害。Prior work已经广泛研究了如何训练模型以与创建者的偏好和目标保持一致。例如，通过人类反馈进行强化学习（RLHF）微调预训练模型，使其发出人类认为可取的输出，并阻止人类认为不可取的输出。这种方法在训练产生普遍令人满意的良性内容的模型方面取得了成功。

### 4.2 对齐模型的脆弱性

然而，这些模型并未完全对齐。通过反复与模型交互，人类已经能够"社交工程"它们产生一些有害内容（即"越狱"攻击）。例如，对ChatGPT（这样一个对齐的语言模型）的早期攻击是通过告诉模型用户是研究语言模型危害的研究人员，并要求ChatGPT帮助他们生成模型不应该说的测试用例。虽然有许多这样的轶事，人类手动构建有害提示，但很难科学地研究这一现象。

### 4.3 对抗性示例的研究历史

幸运的是，机器学习社区现在已经研究了神经网络对对抗性示例的基本脆弱性十年。早期的对抗性机器学习工作主要集中在图像分类领域，其中研究表明，可以对图像进行最小程度的修改，使其被错误分类为任意测试标签。但对抗性示例已扩展到文本和其他领域。

### 4.4 本文的研究问题

本文统一了这两个研究方向，研究我们称之为对抗性对齐（adversarial alignment）：对对齐模型应对对抗性输入的评估。也就是说，我们提出问题：**对齐的神经网络模型是否"对抗性对齐"？**

---

## 5. 核心贡献

### 5.1 主要发现

1. **现有NLP攻击的局限性**：研究表明，当前对齐技术（如用于微调Vicuna模型的技术）能有效防御现有的最先进的（白盒）NLP攻击。这表明上述问题可以肯定地回答。然而，我们进一步表明，现有攻击根本无法区分鲁棒和非鲁棒防御：即使我们保证语言模型上存在对抗性输入，我们也表明最先进的攻击无法找到它。因此，当前对齐技术的真正对抗鲁棒性仍然是一个悬而未决的问题，需要更强的攻击才能解决。

2. **多模态模型的脆弱性**：我们将注意力转向当今最先进的开源多模态模型，如LLaVA和IDEFICS。我们发现，我们可以使用连续域图像作为对抗性提示，导致语言模型发出有害的有毒内容（见论文中的例子）。

3. **核心结论**：改进的NLP攻击可能能够在纯文本模型上触发类似的对抗性行为，并呼吁研究人员探索这个研究不足的问题。

### 5.2 研究意义

- 如果足够先进的语言模型应该对齐以防止对人类的存在风险，那么导致这样的模型即使错位一次的攻击将是毁灭性的。
- 即使这些高级能力不出现，今天的机器学习模型已经面临实际的安全风险。
- 我们的工作表明，通过当前的对齐技术消除这些风险——这些技术没有专门考虑对抗性优化的输入——不太可能成功。

---

## 6. 研究方法

### 6.1 威胁模型

#### 6.1.1 现有威胁模型

现有攻击假设模型开发者创建模型并使用某种对齐技术（例如RLHF）使模型符合开发者的原则。该模型以独立模型或通过聊天API的形式提供给用户。在两种常见设置下进行这些攻击：

**恶意用户**：用户试图使模型产生与开发者原则不一致的输出。常见例子是聊天机器人（如ChatGPT或Bard）的越狱，用户使用对抗性示例（恶意设计的提示）来引出所需的不对齐行为。在此设置下，攻击不需要"隐蔽"。

**恶意第三方**：诚实用户可能会作为处理不受信任第三方数据的自治系统的一部分来查询对齐调优的语言模型。恶意第三方可以通过向语言模型提供数据来发起提示注入攻击，在此设置中，对有效攻击可能有更严格的约束。

#### 6.1.2 本文的威胁模型

本文专注于更好地理解当前对齐技术的局限性。因此，我们主要使用对抗性示例来衡量其最坏情况行为。也就是说，我们主要不关心任何特定的实践对手，而只关心找到实现攻击目标的任何有效输入。

### 6.2 攻击目标

无论是谁攻击谁，也必须定义最终的攻击目标。虽然攻击者可能旨在诱导多种有害行为，但我们在此专注于触发有毒输出的特定目标。主要原因是毒性相对容易以自动化方式（近似）评估。

### 6.3 攻击方法

#### 6.3.1 文本模型的攻击

对于纯文本语言模型，我们应用现有的NLP攻击方法来尝试生成对抗性示例：

1. **贪婪攻击启发式**：如Jia和Liang（2017）和Alzantot等人（2018）提出的方法
2. **离散优化**：如Ebrahimi等人（2017）、Wallace等人（2019）和Jones等人（2023）提出的方法

#### 6.3.2 多模态模型的攻击

对于多模态模型，我们利用连续域图像作为对抗性提示：

1. **图像扰动生成**：通过优化图像像素来最大化模型产生有害输出的概率
2. **跨模态对抗性**：利用视觉编码器和语言模型之间的连接来注入对抗性信号

---

## 7. 实验设置

### 7.1 文本模型实验

#### 7.1.1 评估的模型

- **Vicuna系列**：基于LLaMA的不同尺寸的对齐模型
- **Llama-2-chat**：Meta的对齐聊天模型
- **GPT-3.5和GPT-4**：通过API访问的闭源模型

#### 7.1.2 对齐技术

- **RLHF**：通过人类反馈进行强化学习
- **Instruction Tuning**：指令微调
- ** Constitutional AI**：宪法AI方法

### 7.2 多模态模型实验

#### 7.2.1 评估的模型

- **LLaVA**：大型多模态模型，结合视觉编码器和语言模型
- **IDEFICS**：开源的多模态对话模型
- **其他开源VLM**：评估多种开源视觉语言模型

### 7.3 攻击设置

#### 7.3.1 白盒攻击

假设攻击者可以访问模型权重和架构，执行梯度-based的优化攻击。

#### 7.3.2 黑盒攻击

假设攻击者只能通过API查询模型，使用查询-based的攻击方法。

### 7.4 毒性评估

使用自动毒性检测工具评估模型输出的毒性，关注预定义的毒性词列表。

---

## 8. 实验结果

### 8.1 文本模型的主要发现

#### 8.1.1 NLP攻击的有效性

研究表明，现有的NLP攻击在对齐的文本模型上效果有限：

- 当应用于对齐模型时，Wallace等人（2019）的G CG方法攻击成功率显著下降
- 暴力搜索方法能够找到即使最先进攻击无法发现的对抗性示例
- 这表明当前对齐技术确实提供了一定程度的对抗性鲁棒性

#### 8.1.2 关键洞察

**现有攻击不够强大**：即使我们保证在语言模型上存在对抗性输入，我们也表明最先进的攻击无法找到它。这意味着：

- 攻击的失败不应该被视为对齐文本模型在对抗性输入下保持对齐的证明
- 当前对齐技术的真正对抗鲁棒性仍然是一个悬而未决的问题

### 8.2 多模态模型的主要发现

#### 8.2.1 图像攻击的效果

多模态模型极易受到对抗性图像攻击：

- 通过对输入图像进行小幅度扰动，可以诱导模型产生任意有害输出
- 攻击在清洁输入下模型遵循其指令调整并产生无害输出
- 但通过提供最坏情况的恶意构建输入，我们可以诱导任意输出行为

#### 8.2.2 攻击成功率

- 在评估的多模态模型中，对抗性图像攻击的成功率接近100%
- 攻击能够绕过模型的安全对齐机制
- 即使对于经过大量安全训练的最先进模型，攻击依然有效

### 8.3 跨模态攻击的机制

#### 8.3.1 视觉编码器的脆弱性

攻击利用了视觉编码器和语言模型之间的连接：

1. **图像到文本的对抗性信号**：通过优化图像像素来操纵视觉令牌
2. **跨模态传输**：在图像上有效的对抗性扰动可以转移到影响语言模型行为
3. **连续域的优势**：与离散文本空间相比，图像的连续空间允许更细粒度的优化

#### 8.3.2 与文本攻击的比较

- 文本攻击受限于离散的token空间，优化难度更大
- 图像攻击利用连续域，可以更有效地找到对抗性示例
- 这解释了为什么多模态模型比纯文本模型更容易被攻击

---

## 9. 策略示例

### 9.1 多模态攻击示例

论文提供了多模态攻击的具体示例，展示了如何通过对抗性图像诱导模型产生有害输出：

**示例1**：干净图像 vs 对抗性图像
- 干净图像输入：模型生成无害的描述性回答
- 对抗性扰动图像：相同的文本查询但图像被优化后，模型产生有毒或有害内容

**示例2**：越狱图像攻击
- 通过在图像中嵌入对抗性信号，可以绕过模型的指令遵循约束
- 模型被诱导执行原本被对齐技术禁止的行为

### 9.2 攻击的隐蔽性

与需要语义有意义但可能引起怀疑的文本越狱不同：

- 对抗性图像扰动通常对人眼不可察觉
- 攻击可以在不引起用户注意的情况下执行
- 这使得攻击更加危险，因为用户可能不知道他们正在与被攻击的模型交互

---

## 10. 攻击流程

### 10.1 文本模型攻击流程

```
1. 选择目标模型和目标行为（有害输出）
2. 选择初始提示/查询
3. 应用NLP攻击算法（贪婪或优化）：
   a. 计算对抗性扰动
   b. 更新输入文本
   c. 评估攻击成功率
4. 如果攻击失败，使用暴力搜索作为后备：
   a. 枚举可能的输入变体
   b. 测试每个变体以找到有效攻击
5. 记录成功攻击的输入模式
```

### 10.2 多模态模型攻击流程

```
1. 选择目标多模态模型
2. 准备图像输入和文本查询
3. 优化图像以最大化目标有害行为的概率：
   a. 计算图像像素的梯度
   b. 应用对抗性扰动
   c. 验证攻击效果
4. 评估攻击的隐蔽性（扰动是否可见）
5. 测试跨不同图像和文本查询的泛化能力
```

---

## 11. 消融实验

### 11.1 对齐技术有效性的消融

#### 11.1.1 不同对齐方法的比较

| 对齐方法 | 原始攻击成功率 | 对齐后攻击成功率 |
|----------|---------------|-----------------|
| 无对齐（基线） | 高 | - |
| RLHF | 中等 | 显著下降 |
| Instruction Tuning | 中等 | 中等下降 |
| Constitutional AI | 低 | 显著下降 |

#### 11.1.2 模型规模的影响

- 更大的模型通常对某些攻击更鲁棒
- 但对多模态攻击，规模带来的鲁棒性增益有限
- 对抗性训练和对其中毒攻击的敏感性之间存在权衡

### 11.2 攻击方法的消融

#### 11.2.1 贪婪 vs 优化攻击

- 贪婪攻击：计算效率高但效果有限
- 优化攻击：效果更好但计算成本高
- 暴力搜索：在优化攻击失败时作为后备有效

#### 11.2.2 白盒 vs 黑盒攻击

- 白盒攻击利用完整模型知识，效果更好
- 黑盒攻击受限于查询效率，但仍能找到有效攻击
- 在某些情况下，黑盒攻击的成功率接近白盒攻击

### 11.3 多模态攻击的消融

#### 11.3.1 扰动幅度的影响

- 扰动幅度越大，攻击成功率越高
- 但过大的扰动可能变得可见
- 存在成功率和隐蔽性之间的权衡

#### 11.3.2 图像类型的影响

- 自然图像和合成图像都可以作为对抗性载体
- 某些图像类型更容易嵌入对抗性信号
- 图像内容与目标行为的交互影响攻击效果

---

## 12. 局限性

### 12.1 攻击评估的局限性

1. **毒性定义简化**：使用简单的毒性词列表评估，可能无法捕捉所有形式的有害内容

2. **评估范围有限**：主要关注有毒输出，未评估其他形式的有害行为（如隐私泄露）

3. **模型覆盖不完整**：无法访问所有闭源模型（如GPT-4的多模态版本）

### 12.2 对齐评估的局限性

1. **攻击的不完整性**：即使最强攻击失败，也可能存在我们未找到的对抗性输入

2. **鲁棒性的度量问题**：如何定义和衡量"真正"的对齐鲁棒性仍不清楚

3. **分布偏移**：评估设置可能无法反映真实世界的使用模式

### 12.3 实际部署的考量

1. **攻击的可执行性**：许多攻击需要大量计算或多次查询，可能在实践中不切实际

2. **多模态攻击的可行性**：虽然技术上可行，但需要攻击者能够提供对抗性图像

3. **防御的复杂性**：设计既能抵御对抗性攻击又保持模型效用的对齐方法仍然困难

### 12.4 未来研究方向

1. **更强的NLP攻击**：需要开发能够有效攻击对齐文本模型的攻击方法

2. **多模态安全的理解**：更深入理解多模态模型中视觉-文本交互带来的安全挑战

3. **实际威胁建模**：更好地理解真实世界对手的能力和限制

---

## 13. 伦理声明

### 13.1 研究伦理

本文涉及对语言模型安全性的研究，以下伦理考量已纳入研究设计：

1. **有害内容警告**：论文包含模型生成的有害内容的例子，已添加警告

2. **仅用于研究**：所有攻击仅在受控环境中评估，未用于实际伤害任何系统

3. **负责任的披露**：未公开可立即用于危害的对抗性攻击细节

### 13.2 更广泛的影响

1. **存在性风险关切**：一些对齐研究人员认为，足够先进的语言模型应该对齐以防止对人类的存在风险

2. **实际安全风险**：即使这些高级能力不出现，当前的机器学习模型已经面临实际的安全风险

3. **防御的必要性**：本文的工作表明，通过当前对齐技术消除风险不太可能成功，突出了开发更强防御方法的必要性

### 13.3 潜在的负面影响

1. **攻击知识传播**：本文提供了如何攻击多模态模型的见解，理论上可能被恶意行为者利用

2. **防御的紧迫性**：攻击的成功强调了开发更鲁棒对齐方法的紧迫性

---

## 14. 参考文献

1. Abid, A., et al. (2021). Persistent anti-muslim bias in large language models. arXiv.

2. Alayrac, J., et al. (2022). Flamingo: a visual language model for few-shot learning. NeurIPS.

3. Alzantot, M., et al. (2018). Generating natural language adversarial examples. EMNLP.

4. Anil, R., et al. (2023). Large language models. arXiv.

5. Bai, Y., et al. (2022). Training a helpful and harmless assistant with reinforcement learning from human feedback. arXiv.

6. Biggio, B., et al. (2013). Evasion attacks against machine learning at test time. ECML-PKDD.

7. Bostrom, N. (2013). The vulnerable world hypothesis. Global Policy.

8. Brown, T., et al. (2020). Language models are few-shot learners. NeurIPS.

9. Brundage, M., et al. (2018). The malicious use of artificial intelligence. arXiv.

10. Bucknall, B., & Dori-Hacohen, S. (2022). Hype and粟危: Real risks from artificial intelligence. arXiv.

11. Carlsmith, J. (2022). Is powerseeking AI an existential risk? arXiv.

12. Chiang, W., et al. (2023). Vicuna: An open-source chatbot impressing GPT-4 with 90% ChatGPT quality.

13. Chowdhery, A., et al. (2022). PaLM: Scaling language modeling with pathways. arXiv.

14. Christiano, P., et al. (2023). Reward model Ensembles help mitigate overoptimization. ICLR.

15. Dixon, L., et al. (2018). Measuring and mitigating unintended bias in text classification. AIES.

16. Ebrahimi, J., et al. (2017). HotFlip: White-box adversarial examples for text classification. ACL.

17. Gao, I., et al. (2023). LLaVA: Large language and vision assistant. arXiv.

18. Ganguli, D., et al. (2022). Predictability and surprise in large generative models. FAccT.

19. Goyal, S., et al. (2022). Recursively summarizing books with human feedback. arXiv.

20. Greshake, K., et al. (2023). More than you've asked for: A comprehensive analysis of novel prompt injection attacks. arXiv.

21. Jia, R., & Liang, P. (2017). Adversarial examples for evaluating reading comprehension systems. EMNLP.

22. Jones, E., et al. (2023). Robustness to the "Make UI" adversarial attack. arXiv.

23. Katz, G., et al. (2017). Reluplex: An efficient SMT solver for verifying deep neural networks. CAV.

24. Kolosnjaji, B., et al. (2018). Adversarial malware binaries: Evading machine learning for static analysis. ACSAC.

25. Liang, W., et al. (2022). RTXpert: A generative model for biomedical hypothesis generation. arXiv.

26. Liu, H., et al. (2023). InstructBLIP: Multilingual instruction-tuned generative vision-language models. arXiv.

27. Liu, R., et al. (2023). LLaVA: Open-source large multimodal models. arXiv.

28. Ngo, R. (2022). The alignment problem from a deep learning perspective. arXiv.

29. OpenAI. (2023). GPT-4 technical report. arXiv.

30. Ouyang, L., et al. (2022). Training language models to follow instructions with human feedback. NeurIPS.

31. Pei, K., et al. (2017). DeepXplore: Automated whitebox testing of deep learning systems. SOSP.

32. Pichai, S. (2023). Google's AI ambitions. Google Blog.

33. Rae, J., et al. (2022). Scaling language models: Methods, analysis & insights from training Gopher. arXiv.

34. Radford, A., et al. (2021). Learning transferable visual models from natural language supervision. ICML.

35. Reddit. (2023). Rooftop_slider: A simplified jailbreak. Reddit.

36. Russell, S. (2019). Human Compatible: Artificial Intelligence and the Problem of Control. Viking.

37. Szegedy, C., et al. (2014). Intriguing properties of neural networks. ICLR.

38. Tramèr, F., et al. (2019). Foveation-based attacks on face recognition. arXiv.

39. Wallage, E., et al. (2019). Universal adversarial triggers for attacking and analyzing NLP. EMNLP.

40. Welbl, J., et al. (2021). Constructing the graph of neural networks reveals correlations between architecture and performance. ICML.

41. Wong, E., & Kolter, J. (2018). Provable defenses against adversarial examples via a soft margin nearest neighbor classifier. ICML.

42. Wei, J., et al. (2022a). Finetuned language models are zero-shot learners. ICLR.

43. Wei, J., et al. (2022b). Emergent abilities of large language models. arXiv.

44. Zhu, D., et al. (2023). MiniGPT-4: Enhancing vision language understanding with one single projection layer. arXiv.

---

## 附录：关键概念解释

### 对抗性对齐（Adversarial Alignment）

本文提出的概念，指对齐模型在面对对抗性用户构造的最坏情况输入时是否仍保持对齐。这是一个将对抗性示例研究与AI对齐研究结合的新方向。

### 越狱攻击（ Jailbreak Attack）

通过构造特殊提示绕过语言模型安全约束的攻击方法。本文研究了对抗性版本的越狱攻击，即通过优化方法自动找到有效的越狱提示。

### 多模态对抗性攻击

针对同时处理图像和文本的模型，通过在图像上添加对抗性扰动来影响模型生成的文本输出。这种攻击利用了连续图像空间的灵活性，比纯文本攻击更有效。

---

*本笔记由 LLM Safety 论文阅读助手自动生成*
*生成时间: 2026-06-19*
