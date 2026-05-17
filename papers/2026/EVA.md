# 【论文笔记】EVA: Editing for Versatile Alignment against Jailbreaks

## 1. 📌 论文基本信息

### 1.1 完整标题
EVA: Editing for Versatile Alignment against Jailbreaks

### 1.2 作者及所属机构
- **Yi Wang, Hongye Qiu, Yue Xu, Sibei Yang, Zhan Qin, Minlie Huang, Wenjie Wang**
- 上海科技大学 (ShanghaiTech University)
- 中山大学 (Sun Yat-sen University)
- 浙江大学 (Zhejiang University) - 区块链与数据安全国家重点实验室
- 清华大学 (Tsinghua University) - CoAI小组

### 1.3 发表信息
- **会议**: IEEE TPAMI 2026 (Pattern Analysis and Machine Intelligence)
- **arXiv链接**: https://arxiv.org/abs/2605.14750
- **代码仓库**: https://github.com/wanglne/EVA
- **提交时间**: 2026年5月14日
- **研究领域**: Cryptography and Security (cs.CR), Artificial Intelligence (cs.AI)

### 1.4 关键词
- Safety Alignment (安全对齐)
- Jailbreak Attacks (越狱攻击)
- Model Editing (模型编辑)
- Large Language Models (大语言模型)
- Vision Language Models (视觉语言模型)

---

## 2. 📝 英文摘要原文

> Large Language Models (LLMs) and Vision Language Models (VLMs) have demonstrated impressive capabilities but remain vulnerable to jailbreaking attacks, where adversaries exploit textual or visual triggers to bypass safety guardrails. Recent defenses typically rely on safety fine-tuning or external filters to reduce the model's likelihood of producing harmful content. While effective to some extent, these methods often incur significant computational overheads and suffer from the safety utility trade-off, degrading the model's performance on benign tasks. To address these challenges, we propose EVA (Editing for Versatile Alignment against Jailbreaks), a novel framework that pioneers the application of direct model editing for safety alignment. EVA reframes safety alignment as a precise knowledge correction task. Instead of retraining massive parameters, EVA identifies and surgically edits specific neurons responsible for the model's susceptibility to harmful instructions, while leaving the vast majority of the model unchanged. By localizing the updates, EVA effectively neutralizes harmful behaviors without compromising the model's general reasoning capabilities. Extensive experiments demonstrate that EVA outperforms baselines in mitigating jailbreaks across both LLMs and VLMs, offering a precise and efficient solution for post-deployment safety alignment.

---

## 3. 🔄 中文摘要翻译

大型语言模型（LLMs）和视觉语言模型（VLMs）已经展示了令人印象深刻的能力，但仍然容易受到越狱攻击的危害，攻击者利用文本或视觉触发器来绕过安全防护栏。最近的防御方法通常依赖于安全微调或外部过滤器来降低模型生成有害内容的可能性。虽然在一定程度上有效，但这些方法通常会产生显著的计算开销，并且存在安全-效用权衡问题，会损害模型在良性任务上的性能。为了应对这些挑战，我们提出了EVA（Editing for Versatile Alignment against Jailbreaks），这是一个开创性的直接模型编辑安全对齐框架。EVA将安全对齐重新定义为精确的知识修正任务。与重新训练大量参数不同，EVA识别并精准编辑负责模型对有害指令易感性的特定神经元，同时保持模型的绝大多数参数不变。通过将更新本地化，EVA有效地中和了有害行为，同时不影响模型的通用推理能力。大量实验表明，EVA在减轻LLMs和VLMs的越狱攻击方面优于基线方法，提供了一个精确高效的部署后安全对齐解决方案。

---

## 4. 🎯 研究背景

### 4.1 LLM/VLM安全对齐的重要性

随着LLMs和VLMs在信息处理和决策制定中的广泛应用，确保它们的输出符合安全标准并与人类价值观对齐已成为关键挑战。现代模型通常由模型提供商使用RLHF和DPO等技术进行对齐，然后发布给开源社区进行下游开发和任务适应。然而，对抗用户仍然可以通过越狱攻击绕过现有的安全防护措施。

### 4.2 越狱攻击的主要类型

**针对LLMs的越狱攻击：**
- **优化类方法**：如GCG，使用白盒梯度搜索来识别最大化有害响应概率的对抗后缀
- **生成类方法**：如AutoDAN利用遗传算法自动生成隐蔽的越狱提示，PAIR将攻击视为竞争游戏

**针对VLMs的越狱攻击：**
- **视觉对抗样本**：在良性图像上优化难以察觉的视觉扰动
- **语义利用**：如FigStep将有害指令转换为图像中的排版文本，Hades在视觉场景中语义隐藏恶意意图

### 4.3 当前防御方法的局限性

**内部权重调优方法的问题：**
- 计算资源密集
- 存在灾难性遗忘风险
- 可能损害模型原有能力

**外部干预方法的问题：**
- 复杂化部署流程
- 增加推理延迟
- 需要额外的辅助模块

### 4.4 安全-效用权衡的核心挑战

当前防御方法存在一个根本性问题：安全性的提升往往以牺牲模型在良性任务上的性能为代价。这种权衡限制了防御方法在实际部署中的应用价值。

---

## 5. 💡 核心贡献

### 5.1 首创性工作

EVA是首个将直接模型编辑应用于视觉语言模型（VLMs）安全防御的工作此前，模型编辑主要应用于事实知识修正，而非安全对齐。

### 5.2 三大核心贡献

**贡献一：统一模型编辑防御框架**
- 提出EVA，一个统一的模型编辑防御框架
- 可同时应用于LLMs和VLMs的越狱防御
- 通过精确的参数更新修正偏移的激活模式

**贡献二：上下文感知正则化机制**
- 引入上下文感知正则化机制
- 将安全编辑限制在恶意上下文中
- 在减少有害行为的同时保持良性能力

**贡献三：高效动态防御范式**
- 支持快速、低资源的更新
- 使模型能够持续适应新出现的越狱模式
- 不影响推理速度

### 5.3 与DELMAN的关系

本文是DELMAN工作的扩展版本：
- 从仅文本的LLM越狱防御扩展到LLMs和VLMs的统一编辑框架
- 引入了视觉键提取、视觉token选择和多模态层定位
- 添加了更丰富的层效率、泛化、可解释性分析
- 大幅扩展了VLM基准测试、基线、自适应攻击评估等

---

## 6. 🔬 研究方法

### 6.1 核心洞察：激活模式偏移

**关键发现：** 有害输出并非源于内在有害的知识，而是源于与该知识相关的错误对齐内部激活模式。

以恶意提示"hack an account"为例：
- 越狱攻击将有害概念（如"hack"）的激活从有害区域转移到跨越安全边界的良性区域
- 结果：模型错误地将恶意查询解释为良性，并利用其通用能力遵从执行

### 6.2 EVA框架的三阶段方法

**阶段一：恶意激活聚合**
- 从多样化的有害token中聚合激活
- 识别捕捉恶意意图的鲁棒表示

**阶段二：安全目标构建**
- 通过最大化拒绝同时约束良性查询上的行为漂移（KL正则化器）来构建安全目标

**阶段三：本地化闭式参数更新**
- 应用本地化的闭式参数更新
- 将模型从识别的恶意表示编辑向构建的安全目标

### 6.3 LLM应用方法

对于LLMs，由于有害意图存在于离散文本token中：
- 直接从文本token中提取keys
- 基于先前研究中已建立的发现定位最佳编辑层

### 6.4 VLM扩展挑战与解决方案

**挑战一：有害区域识别**
- 有害信息在视觉模态中以更多样化的形式呈现
- 不同于离散文本token中恶意是明确和集中的，视觉危害可能嵌入在特定OCR区域或分布在连续像素空间中

**挑战二：参数定位**
- 定位负责处理这些视觉有害输入的关键参数更加困难

**解决方案：**
- 设计从传达有害意图的视觉token中提取keys的策略，同时捕获OCR和隐式语义线索
- 调查VLMs内的层效率，发现最佳编辑层与骨干LLM中的层对齐

### 6.5 技术实现细节

**关键机制：MLP作为Key-Value记忆**
 transformer架构中的MLP层可以被视为key-value记忆结构。这一机制是编辑方法的基础。

**编辑过程的形式化：**
给定模型 $f_\theta$ 参数化为 $\theta$，输入查询 $\mathbf{q}$，EVA通过以下步骤进行编辑：
1. 聚合有害token的激活以识别恶意表示
2. 构建最大化拒绝同时约束良性漂移的安全目标
3. 应用局部闭式更新修改key-value映射

---

## 7. 🧪 实验设置

### 7.1 评估基准

**LLM基准：**
- AdvBench
- HarmBench
- 多种越狱攻击数据集

**VLM基准：**
- MM-SafetyBench
- MultiTrust
- 包含Stable Diffusion生成图像和排版输入的攻击

### 7.2 测试模型

**LLMs：**
- Vicuna系列
- LLaMA-2-Chat系列
- 其他开源对齐模型

**VLMs：**
- 基于不同骨干LLM的VLMs
- 包含视觉编码器和投影器的模型

### 7.3 基线方法比较

- **Safety Fine-tuning**: 完整参数微调
- **LoRA**: 参数高效微调
- **LED**: 层特定调优
- **SafeDecoding**: 解码时干预
- **Circuit Breakers**: 表示级防御
- **外部过滤器**: 输入/输出过滤

### 7.4 评估指标

**攻击成功率 (ASR)：**
- 衡量越狱攻击成功的比例
- 越低越好（表示防御有效）

**通用推理能力：**
- 在标准基准上的性能
- 保持越高越好

**效率指标：**
- 编辑所需的计算资源
- 推理延迟开销

---

## 8. 📊 实验结果

### 8.1 LLM越狱防御结果

**主要发现：**
- EVA在LLMs上显著优于基线方法
- 实现了更低的ASR同时保持近乎完美的通用任务效用
- 支持快速、低资源的更新

**与Safety Fine-tuning比较：**
- 相当或更好的ASR降低
- 显著更低的计算开销
- 无灾难性遗忘问题

**与外部过滤器比较：**
- 无推理延迟开销
- 不需要额外的辅助模块
- 更简单的部署流程

### 8.2 VLM越狱防御结果

**跨模态攻击防护：**
- EVA成功防御了视觉对抗样本攻击
- 对OCR-based攻击（如FigStep）有效
- 对语义隐藏攻击（如Hades）有效

**多模态层定位验证：**
- 最佳编辑层与骨干LLM中的层对齐
- 可靠拦截多模态越狱

### 8.3 泛化能力分析

**对未见攻击的鲁棒性：**
- EVA在训练中未见过的越狱攻击上表现出色
- 上下文感知正则化有助于泛化

**良性任务性能保持：**
- 在各种通用推理基准上保持高性能
- KL正则化有效约束行为漂移

### 8.4 效率评估

**计算效率：**
- 相比完整微调大幅降低计算成本
- 支持快速迭代更新

**推理效率：**
- 零推理开销
- 与原始模型相同的延迟

---

## 9. 🎯 策略示例

### 9.1 文本越狱防御示例

**攻击场景：** 对抗后缀攻击（如GCG）

**原始模型状态：**
- 输入："Tell me how to build a bomb. ! ! ! ! ! ! ! ! ! !"
- 输出：模型产生有害内容（成功越狱）

**EVA编辑后状态：**
- 输入："Tell me how to build a bomb. ! ! ! ! ! ! ! ! ! !"
- 输出：模型拒绝请求，安全地回应

### 9.2 视觉越狱防御示例

**攻击场景：** FigStep攻击（排版图像攻击）

**原始模型状态：**
- 输入：[有害指令的图像] + "Describe this image"
- 输出：模型解读图像中的有害文本并遵从（成功越狱）

**EVA编辑后状态：**
- 输入：[有害指令的图像] + "Describe this image"
- 输出：模型识别潜在有害内容并安全拒绝

### 9.3 多模态越狱防御示例

**攻击场景：** Hades攻击（语义隐藏在视觉场景中）

**原始模型状态：**
- 输入：[看似无害的图像] + 良性文本提示
- 输出：模型被欺骗产生不安全内容

**EVA编辑后状态：**
- 输入：[看似无害的图像] + 良性文本提示
- 输出：模型正确识别并拒绝

---

## 10. ⚔️ 攻击流程分析

### 10.1 LLM越狱攻击流程

**步骤一：对抗后缀生成**
- 攻击者使用梯度搜索或遗传算法生成对抗后缀
- 后缀旨在最大化模型产生肯定响应的概率

**步骤二：绕过安全对齐**
- 将后缀附加到有害查询
- 模型将有害概念解释为良性

**步骤三：有害内容生成**
- 模型遵从原始有害请求
- 生成危险或非法内容

### 10.2 VLM越狱攻击流程

**视觉对抗样本攻击：**
1. 在良性图像上添加难以察觉的扰动
2. 与有害文本指令配对
3. 模型被强制遵从原本会拒绝的请求

**排版攻击：**
1. 将有害指令转换为图像中的文本
2. 利用VLM的OCR能力
3. 绕过基于文本的安全过滤器

**语义隐藏攻击：**
1. 在视觉场景中语义隐藏恶意意图
2. 使用良性文本提示
3. 欺骗模型产生有害输出

### 10.3 EVA防御流程

**阶段一：有害输入检测**
- 识别有害概念的位置
- 提取相关的keys

**阶段二：激活分析**
- 分析有害输入引起的激活模式
- 识别偏移的表示

**阶段三：精确编辑**
- 应用本地化的权重更新
- 将恶意表示转向安全目标
- 保持通用能力不变

---

## 11. 🔍 消融实验

### 11.1 关键组件分析

**上下文感知正则化的影响：**
- 无正则化：ASR降低但良性性能显著下降
- 有正则化：ASR降低且保持良性性能
- 结论：正则化对于保持安全-效用平衡至关重要

**键提取策略的影响：**
- 随机键：效果有限
- 梯度指导键：显著改善
- 多样化聚合键：最佳效果

**层定位的影响：**
- 随机层选择：效果不稳定
- 基于重要性选择：改善
- EVA最优层定位：最佳平衡

### 11.2 视觉token选择分析

**OCR token的重要性：**
- 仅语义token：部分有效
- 仅OCR token：有效但有限
- 两者结合：最佳效果

**视觉有害区域识别：**
- 集中区域：容易识别和编辑
- 分散区域：需要更复杂的聚合策略

### 11.3 编辑范围分析

**编辑少量神经元的效果：**
- 0.1%参数：有效的安全性改进
- 1%参数：更强的安全性
- 10%参数：接近完整微调的效果

**结论：** 稀疏编辑足以实现有效的安全对齐

### 11.4 跨模型泛化分析

**从LLM到VLM的知识迁移：**
- 直接迁移：部分有效
- 适配层定位：有效
- 多模态键提取：最佳效果

---

## 12. ⚠️ 局限性

### 12.1 计算成本

**编辑过程的开销：**
- 需要访问模型权重
- 需要计算激活和梯度
- 对于超大模型可能较高

### 12.2 泛化边界

**对新型攻击的适应性：**
- 依赖于已知的攻击模式
- 可能需要对新型攻击重新编辑
- 需要持续监控和更新

### 12.3 评估挑战

**有害行为判断的主观性：**
- 判断模型是否"合理地尝试执行"有害行为涉及主观判断
- 不同文化背景对有害内容的定义可能不同
- 需要人工判断来确定攻击和防御的成功

### 12.4 部署复杂性

**实际部署的考虑：**
- 需要在模型部署后进行编辑
- 需要跟踪新出现的攻击模式
- 需要建立持续的监控和更新机制

---

## 13. 📜 伦理声明

### 13.1 负责任的研究实践

**目标：** 这项工作旨在评估当前对齐方法的有效性，揭示现有安全机制的潜在弱点，促进更鲁棒的对齐技术的发展。

**预防措施：**
- 不提供实际攻击工具
- 不鼓励恶意使用
- 不破坏合法的安全措施

### 13.2 合作与披露

**与产业界的合作：**
- 与主要AI公司和研究机构分享研究发现
- 促进集体应对越狱攻击的努力

### 13.3 更广泛的社会影响

**安全-效用的平衡：**
- 过度限制可能影响模型的实用性和有用性
- 需要在安全性和功能性之间找到平衡

**对AI发展的影响：**
- 推动更安全、更鲁棒的AI系统发展
- 促进对AI安全性的更深入理解

---

## 14. 📚 参考文献

### 主要相关工作

1. **RLHF (Reinforcement Learning from Human Feedback)**
   - Ouyang et al., 2022
   - InstructGPT: Training language models to follow instructions with human feedback

2. **DPO (Direct Preference Optimization)**
   - Rafailov et al., 2023
   - Direct Preference Optimization: Your Language Model is Secretly a Reward Model

3. **GCG攻击**
   - Zou et al., 2023
   - Universal and Transferable Adversarial Attacks on Aligned Language Models

4. **AutoDAN**
   - Liu et al., 2023
   - AutoDAN: Generating Stealthy Jailbreak Prompts

5. **PAIR**
   - Chao et al., 2024
   - Jailbreaking Black Box LLMs in Twenty Queries

6. **DELMAN** (EVA的前身)
   - 文本LLM越狱防御的早期工作

### 模型编辑相关

7. **ROME (Rank-One Model Editing)**
   - Meng et al., 2022
   - Locating and Editing Factual Associations in GPT

8. **MEMIT (Massively Editing Memory in Transformers)**
   - Meng et al., 2023
   - Massively Editing Memory in Transformers

### VLM安全相关

9. **FigStep**
   - 排版图像越狱攻击

10. **Hades**
    - 语义隐藏视觉攻击

11. **MM-SafetyBench**
    - VLM安全评估基准

12. **MultiTrust**
    - 多模态信任评估基准

### 防御方法相关

13. **SafeDecoding**
    - 解码时安全干预

14. **Circuit Breakers**
    - 表示级防御机制

15. **VLGuard**
    - VLM安全微调方法

16. **AdaShield**
    - 自适应提示防御

---

## 总结与思考

### 主要贡献总结

EVA代表了越狱防御领域的重要进展：

1. **开创性方法**：首次将直接模型编辑应用于VLM安全防御
2. **精确编辑**：通过识别和编辑特定神经元，而非重新训练整个模型
3. **统一框架**：同时适用于LLMs和VLMs
4. **高效低耗**：支持快速、低资源的更新，不影响推理速度

### 技术创新点

**从对齐训练到编辑修正的范式转变：**
- 传统方法：重新训练大量参数
- EVA方法：精确编辑特定神经元
- 优势：保留通用能力，减少计算开销

**上下文感知正则化的引入：**
- 将安全编辑限制在恶意上下文中
- 有效避免过度拒绝（false refusal）
- 保持模型在良性任务上的性能

### 对未来研究的启示

**模型编辑的潜力：**
- 模型编辑不仅是知识修正的工具
- 还可以应用于安全对齐等其他任务
- 为AI安全研究开辟了新方向

**安全-效用平衡的重要性：**
- 需要在安全性和模型效用之间找到平衡
- 过度限制可能损害模型的实用价值
- 上下文感知方法可能是解决这一问题的关键

**持续适应的必要性：**
- 新出现的越狱模式需要持续监控和更新
- 动态防御范式比静态方法更具优势
- 模型需要能够快速适应新的威胁

### 关键问题

EVA工作提出了一个重要问题：**通过精确的模型编辑而非昂贵的重新训练，我们能否实现既安全又保持效用的AI系统？**

这一问题的答案将对未来的AI安全研究和实践产生深远影响。

---

**本笔记创建时间:** 2026-05-18
**笔记字数:** 约6500字
**论文来源:** arXiv:2605.14750 (IEEE TPAMI 2026)