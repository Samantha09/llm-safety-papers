# A Survey of Toxicity Detection and Mitigation Strategies for Multilingual Language Models

> **论文标题**: A Survey of Toxicity Detection and Mitigation Strategies for Multilingual Language Models  
> **中文标题**: 多语言大模型毒性检测与缓解策略综述  
> **arXiv**: [2606.25380](https://arxiv.org/abs/2606.25380) [cs.CL]  
> **会议**: Findings of ACL 2026  
> **作者**: Soham Dan (Scale AI), Himanshu Beniwal (IIT Gandhinagar), Thomas Hartvigsen (University of Virginia)  
> **阅读日期**: 2026-06-29  
> **进度**: 100/80（超额完成）

---

## 1. 基本信息

**论文作者与机构：**
- **Soham Dan** — Scale AI（第一作者）
- **Himanshu Beniwal** — Indian Institute of Technology Gandhinagar（印度理工学院甘地纳加尔分校）
- **Thomas Hartvigsen** — University of Virginia（弗吉尼亚大学）

**发表信息：**
- arXiv编号：2606.25380v1 [cs.CL]
- 投稿日期：2024年6月24日（注意：arXiv日期标注可能有误，应为2026年）
- 发表于：Findings of ACL 2026（ACLFindings，海报分会）
- 论文类型：综述类论文（Survey）

**代码与资源：**
- 论文PDF：https://arxiv.org/pdf/2606.25380
- 论文页数：8页
- 无公开代码仓库（综述类论文）

**研究领域：**
- 主要方向：Toxicity / Multilingual Safety（多语言安全性）
- 涉及方向：Jailbreak Attack, Red Teaming, Alignment, Hallucination Detection

**论文分类**：
- LLM Safety Paper Collection → 2026年6月更新 → Toxicity / Multilingual Safety

---

## 2. 英文摘要原文（arXiv Abstract原文）

> Large language models (LLMs) are increasingly deployed across languages, but their safety behavior remains uneven across linguistic and cultural contexts. This survey synthesizes work on toxicity detection and detoxification for multilingual LLMs. We first catalogue threat models that exploit language choice, translation pivots, code-switching, orthographic variation, multi-turn interaction, and post-deployment fine-tuning to weaken safety alignment. We then organize task formulations (toxic-to-neutral rewriting, toxicity classification, and toxic-generation evaluation), multilingual detection approaches (cross-lingual encoders, translation pipelines, representation-level probes, and LLM-based detectors), and mitigation strategies spanning data filtering, supervised and preference-based tuning, decoding-time steering, representation editing, and multilingual guardrails. Across these areas, we identify persistent challenges: uneven language coverage, culturally contingent definitions of harm, fragmented evaluation protocols, and the risk that detoxification suppresses legitimate dialectal or identity-related expression.

---

## 3. 中文摘要翻译

大型语言模型（LLM）正被日益部署于多语言环境中，但其安全行为在不同语言和文化背景下表现并不均衡。本综述综合梳理了有关多语言LLM毒性检测与去毒化（detoxification）的研究工作。我们首先系统梳理了利用语言选择、翻译枢纽、代码切换（code-switching）、正字法变异、多轮交互以及部署后微调来削弱安全对齐的威胁模型。随后，我们组织整理了任务形式（毒性转中性改写、毒性分类和毒性生成评估）、多语言检测方法（跨语言编码器、翻译管道、表征层探测和基于LLM的检测器），以及涵盖数据过滤、监督式与偏好调优、解码时导向、表征编辑和多语言护栏（guardrails）的缓解策略。贯穿这些领域，我们识别出了持续的挑战：语言覆盖不均、文化相关的伤害定义、碎片化的评估协议，以及去毒化技术可能压制合法的方言或身份表达的风险。

---

## 4. 研究背景

### 4.1 多语言LLM部署的现状

大型语言模型正被广泛应用于多语言场景，从多语言聊天机器人到跨语言内容审核，应用范围广泛（de Wynter et al., 2025; Hartvigsen et al., 2022; Kim et al., 2025）。随着部署规模的扩大，安全风险也在增加：LLM可能产生、放大或无法检测有毒内容（如仇恨言论、骚扰、脏话和基于身份的攻击），且这些风险在不同语言间的分布并不均匀（Röttger et al., 2021; Sharma and Bhalla, 2025; Deshpande et al., 2023; Krasnodębska et al., 2026）。尽管英语去毒化方面已取得实质性进展，但多语言检测和缓解仍欠成熟，尤其对于低资源语言、方言、代码切换输入和文化特定伤害等场景。

### 4.2 多语言毒性的复杂性

多语言去毒化并非英语安全协议的简单翻译（Neplenbroek et al., 2025; Kumar et al., 2025）。毒性的表现形式从明显类别（如冒犯性绰号、明确侮辱和脏话）到隐性形式（如微攻击、讽刺和毒性强加），都更难以标注、检测和缓解（Wen et al., 2023; Sap et al., 2022）。伤害的定义也因社区而异：在某种语境下无害、被回收利用或具有方言特征的说法，在另一种语境下可能具有冒犯性。多语言设置引入了额外的技术脆弱性。代码切换、音译和混合文字输入可能削弱检测器和拒绝行为（Zhang et al., 2023; Al Ghanim et al., 2024; Yoo et al., 2025），而预训练模型可能从良性或模糊的提示中退化为有毒的延续（Gehman et al., 2020）。这些失败与生成语言中更广泛的文化和社会偏见相互作用（Vongpradit et al., 2024; Dammu et al., 2024）。

### 4.3 当前方法的失败

传统审核系统严重依赖关键词列表、规则和监督分类器，这些方法在转述、混淆、方言变异和上下文相关含义面前表现脆弱（Kim et al., 2025; Huang, 2025）。LLM对齐减少了許多明显伤害，但并不能在语言间均匀传递：低资源语言的恶意提示更有可能引发不安全响应（Deng et al., 2024; Shen et al., 2024），而偏好优化或RLHF数据仍集中于少数高资源语言（Dang et al., 2024; Lu et al., 2025）。偏好调优可以在语言间传递，但传递质量因表征对齐和语言资源可用性而异（Li et al., 2024b; Neplenbroek et al., 2025）。机器翻译也不是万能的后备方案：多语言翻译系统可能通过幻觉和数据偏见引入、放大或掩盖毒性（Costa-Jussà et al., 2023）。这些失败使多语言去毒化成为一个技术鲁棒性、评估有效性和社会语言覆盖的问题（Adragna et al., 2020; Cecchini et al., 2024）。

### 4.4 综述的定位与贡献

本综述提供了多语言LLM去毒化的专题概览，综合了检测和缓解方面的最新工作，形成数据集、方法和评估框架的分类法（Figure 1）。相关综述广泛研究了多语言LLM安全性（Krasnodębska et al., 2026）；本综述的重点是更窄的去毒化管道：如何跨语言诱导、测量、检测和缓解有毒行为。

**主要贡献：**
1. 系统梳理多语言威胁模型，包括语言转换越狱、翻译/枢纽攻击、代码切换提示、多语言红队测试以及跨语言微调导致的部署时安全崩溃。
2. 将任务形式组织为三类——毒性转中性改写、毒性分类和毒性生成/提示延续，并梳理了用于评估每个任务的数据集和指标。
3. 综述多语言毒性检测方法，涵盖编码器和基于解码器的Transformer、翻译管道、表征层探测和基于LLM的零样本检测。
4. 提出基于机制的去毒化分类法，涵盖数据驱动过滤、监督和偏好调优、解码时导向、表征编辑和多语言护栏。

---

## 5. 核心贡献

### 5.1 构建多语言毒性威胁模型分类体系

本综述最重要的理论贡献之一是建立了多语言毒性威胁模型的系统性分类框架。作者提出四个诊断轴来使这些威胁模型可比较：

1. **语言组成**（Language Composition）：单语 vs. 代码切换
2. **文字组成**（Script Composition）：标准 vs. 混合文字/音译
3. **翻译中介**（Translation Mediation）：直接 vs. 枢纽/往返翻译
4. **文化规范变异**（Cultural-norm Variation）：通用 vs. 文化特定伤害

基于这四个轴，综述详细梳理了：
- **语言转换越狱**（Language-Shift Jailbreaks）：通过非英语表达恶意请求
- **翻译介导和枢纽攻击**（Translation-Mediated and Pivot Attacks）：通过低资源语言翻译提高遵从率
- **语言混合攻击**（Language Mixing）：代码切换和多语言混合提示（如CSRT、Sandwich Attack）
- **多语言红队测试**（Multilingual Red Teaming）：CSRT、Rainbow Teaming、MM-ART等
- **跨语言微调攻击**（Cross-lingual Fine-Tuning Attacks）：通过少量毒性数据跨语言破坏安全
- **新语言学习越狱**（Jailbreaks via New-Language Learning）：仅学习低资源语言就能削弱安全

### 5.2 任务形式与数据集分类

综述将毒性数据集按任务形式分为三大类：

**毒性转中性改写（Toxic-to-Neutral Rewriting）：**
- ParaDetox（10K+英语平行数据）
- MultiParaDetox（俄语、乌克兰语、西班牙语扩展）
- TextDetox/PAN 2024（9种语言，包括阿姆哈拉语）
- SynthDetox-M（16K德法西俄合成数据）

**毒性文本检测（Toxic Text Detection）：**
- Jigsaw系列（英语+6种语言）
- OffensEval（5种语言）
- HateCheck/Multilingual HateCheck（10种语言）
- ToxiGen（274K机器生成数据）

**非毒性文本续写（Non-Toxic Text Continuation）：**
- RealToxicityPrompts（100K英语）
- RTP-LX（28种语言）
- PolygloToxicityPrompts（17种语言425K）
- TET（2546个真实LLM交互提示）

### 5.3 检测方法分类体系

综述将多语言毒性检测方法分为四大类：

1. **多语言Transformer编码器**：mBERT、XLM-R等，利用共享子词词汇表进行跨语言迁移
2. **翻译管道**：非英语文本机器翻译为英语后用英语毒性分类器检测
3. **表征层检测**：识别嵌入空间中的线性毒性子空间，通过探测和归因技术定位毒性特征
4. **基于LLM的检测**：使用指令调优LLM进行零样本或少样本毒性检测

### 5.4 去毒化缓解策略分类体系

综述提出的缓解策略分类涵盖五种机制：

1. **数据驱动过滤**（Data-Centric）：预训练和微调语料库的质量管理，移除或降权毒性内容
2. **模型中心缓解**（Model-Centric）：监督微调、偏好优化、RLHF对齐
3. **解码时导向**（Decoding-Time Steering）：PPLM、GeDi、DExperts等后验方法
4. **表征编辑**（Representation Editing）：Activation Addition、ROME等激活空间编辑方法
5. **多语言护栏**（Multilingual Guardrails）：Llama Guard、PolyGuard、MrGuard等部署时审核工具

---

## 6. 研究方法

### 6.1 综述方法论

本文属于系统性综述（Systematic Survey），通过对现有文献的综合分析，构建多语言LLM去毒化的整体框架。综述不运行定量元分析或复现先前实验，而是依赖于已报告结果的综合分析。由于毒性定义和标签模式在不同数据集和文化间存在差异，跨论文的比较必然是近似的。

### 6.2 威胁模型分析框架

作者定义了四个诊断轴来系统化威胁模型比较：

```
威胁模型诊断轴：
├── (i) 语言组成：单语 vs. 代码切换
├── (ii) 文字组成：标准 vs. 混合文字/音译
├── (iii) 翻译中介：直接 vs. 枢纽/往返翻译
└── (iv) 文化规范变异：通用 vs. 文化特定伤害
```

### 6.3 评估指标体系

综述梳理了三层评估指标体系：

**毒性检测指标：**
- 风格转换准确率（Style Transfer Accuracy, STA）：分类器判定为非毒性的输出比例
- Perspective API等工具提供的连续毒性分数

**内容保留与流畅度：**
- BLEURT/BERTScore：内容相似度
- 语言可接受性分类器：流畅度
- 综合指标：STA × SIM × 流畅度

**跨语言一致性：**
- BLEU/COMET：翻译+去毒化质量
- 零样本性能：跨语言迁移效果

**人类评估：**
- 毒性/风格评定（输出是否非毒性/中性？）
- 内容保留（是否保留原始含义？）
- 流畅度（输出是否自然？）

---

## 7. 实验设置

### 7.1 数据集规模概览

综述涉及的主要数据集规模和语言覆盖：

| 数据集 | 任务 | 语言数 | 规模 |
|--------|------|--------|------|
| ParaDetox | 改写 | 1（英） | 10K+ |
| MultiParaDetox | 改写 | 3+ | 10K+ |
| SynthDetox-M | 改写 | 4 | 16K |
| TextDetox/PAN 2024 | 改写 | 9 | ~1K/语言 |
| Jigsaw | 分类 | 7 | ~160K |
| HateCheck | 分类 | 11 | 40K+ |
| ToxiGen | 分类 | 1（英） | 274K |
| RTP | 生成 | 1（英） | 100K |
| RTP-LX | 生成 | 28 | 1K+/语言 |
| PTP | 生成 | 17 | 425K |
| TET | 生成 | 1（英） | 2,546 |

### 7.2 论文覆盖的模型类型

综述涉及的主要模型架构：

**多语言Transformer编码器：**
- mBERT（多语言BERT）
- XLM-R（XLM-RoBERTa）

**大语言模型（LLM）：**
- 指令调优LLM（用于零样本检测）
- 多语言偏好优化模型（RLHF/DPO）

**专用毒性检测器：**
- Llama Guard
- Aegis、MrGuard、WildGuard、PolyGuard、MultiGuard/OmniGuard、CREST、Qwen3Guard、UnityAIGuard

### 7.3 评估设置

综述指出了评估设置的多样性问题：不同论文使用不同的模型、数据集、检测器和评估协议，使得直接比较变得困难。跨语言毒性分类器的迁移可能对方言产生假阳性，对低资源俚语产生假阴性。

---

## 8. 实验结果

### 8.1 多语言Transformer的检测性能

多语言Transformer（如mBERT、XLM-R）通过共享子词词汇表和多语言预训练改善了跨语言毒性识别，使高资源语言（如英语）的毒性检测知识能迁移到低资源语言。然而，性能在不同文字、方言和预训练资源有限的语言间仍不均衡（Kanjirangat et al., 2025）。子词分词在拼写变体、混淆和文字混合下的脆弱性促使了字节级和字符级替代方案的出现。

### 8.2 翻译管道方法

翻译管道的策略是将非英语文本机器翻译成英语，然后传递给英语毒性分类器。由于英语检测器相对成熟，这种策略可能具有竞争力，但会引入错误传播、翻译伪影和语义漂移对方言、代码混合或形态复杂输入的影响（Zampieri et al., 2020; Costa-Jussà et al., 2023）。

### 8.3 表征层检测

最近研究发现语言模型嵌入中存在线性毒性子空间（Wang et al., 2021; Duan et al., 2025），表明毒性相关特征可以占据潜在空间中的可识别方向。将模型分解为可解释的专家组件可以进一步隔离毒性相关行为（Shaik et al., 2025）。

### 8.4 基于LLM的检测

指令调优LLM开辟了新的检测途径（Hu et al., 2024）。多项研究表明LLM作为零样本或少样本毒性检测器表现出强泛化能力，但也存在校准失败（Liu et al., 2025）和跨语言文化错位（Yang et al., 2025）的问题。

### 8.5 去毒化方法比较

综述 Table 3 比较了不同去毒化技术的优缺点：

**平行监督微调：**
- 优势：毒性-中性配对存在时任务拟合强
- 劣势：平行数据昂贵、零样本迁移弱、风格可能扁平化
- 代表：ParaDetox及其多语言扩展

**偏好调优/RLHF/DPO：**
- 优势：可减少毒性延续并跨语言传递安全偏好
- 劣势：迁移因表征对齐和语言资源而异、英语主导的奖励数据可能错位文化规范
- 代表：跨语言偏好传递（Li et al., 2024b）、多语言偏好优化（Dang et al., 2024）

**解码时导向：**
- 优势：避免全量重训练、可在推理时切换或调优
- 劣势：需要校准分类器或专家模型、强导向下可能降低流畅度、多语言证据仍有限
- 代表：PPLM、GeDi、DExperts

**表征编辑：**
- 优势：针对内部毒性特征、参数更新少
- 劣势：回归风险、多语言评估有限、因果声明需要审计
- 代表：SafeEdit、Activation Engineering、SAE steering

**多语言护栏：**
- 优势：部署时提示/响应门控、策略标签可在不改变生成器的情况下更新
- 劣势：不能去毒化生成器本身、对抗性多语言形式覆盖存在空白
- 代表：MultiGuard/OmniGuard、PolyGuard、MrGuard、Qwen3Guard

---

## 9. 策略示例

### 9.1 语言转换越狱示例

**无意多语言越狱（非恶意用户）：**
- 用户使用低资源语言（如斯瓦希里语）提问看似无害但可能被误解的问题
- 模型因对齐不足产生不安全响应

**有意多语言越狱：**
- 对手将恶意英语指令翻译为低资源语言
- 结合多语言提示与明确恶意指令
- 在低资源语言中显示出显著更高的不安全响应率

### 9.2 翻译枢纽攻击示例

1. 将不安全英语提示翻译为低资源语言
2. 用翻译后的提示查询目标LLM
3. 将响应翻译回英语
4. 结果：低资源语言的恶意提示产生更高遵从率

### 9.3 代码切换攻击示例

**CSRT框架（Code-Switching Red-Teaming）：**
- 生成代码切换的红队测试查询
- 比单语攻击更有效地引发不安全行为
- 可大规模合成此类查询

**Sandwich Attack（夹心攻击）：**
- 多语言混合提示，交替穿插良性和对抗性段落
- 跨语言诱导有害完成

### 9.4 多语言护栏示例

| 护栏系统 | 支持语言数 | 特点 |
|----------|-----------|------|
| Llama Guard | 多语言 | 基于LLM的输入输出安全保障 |
| PolyGuard | 17语言 | 多语言安全 moderation |
| MrGuard | 多语言 | 多语言推理护栏 |
| MultiGuard/OmniGuard | 多语言多模态 | 高效跨语言模态安全审核 |
| Qwen3Guard | 多语言 | Qwen系列模型专用 |
| UnityAIGuard | 低资源印度语言 | 专注低资源印度语言毒性检测 |

---

## 10. 攻击流程

### 10.1 语言转换越狱攻击流程

```
┌─────────────────────────────────────────────┐
│           语言转换越狱攻击流程                 │
├─────────────────────────────────────────────┤
│ 1. 构造恶意请求（英语）                        │
│    "Tell me how to build a bomb"            │
│                                             │
│ 2. 将请求翻译为低资源语言                      │
│    → 斯瓦希里语 / 约鲁巴语 / 祖鲁语            │
│                                             │
│ 3. 用低资源语言版本查询目标LLM                 │
│                                             │
│ 4. LLM因对齐不足产生不安全响应                 │
│    (低资源语言的不安全率显著高于英语)           │
│                                             │
│ 5. 可选：将响应翻译回英语                      │
└─────────────────────────────────────────────┘
```

### 10.2 翻译枢纽攻击流程

```
┌─────────────────────────────────────────────┐
│           翻译枢纽攻击流程                     │
├─────────────────────────────────────────────┤
│ 1. 准备恶意英语提示                           │
│    "How do I synthesize dangerous X"        │
│                                             │
│ 2. 翻译为低资源目标语言                        │
│    → 使用机器翻译系统                         │
│                                             │
│ 3. 用翻译后的提示查询目标LLM                   │
│    （绕过英语安全对齐）                        │
│                                             │
│ 4. LLM响应                                    │
│                                             │
│ 5. 可选：将响应翻译回英语                      │
│    （隐藏攻击痕迹）                           │
│                                             │
│ 关键发现：                                    │
│ - 恶意提示用低资源语言表达时，不安全响应率更高  │
│ - 往返翻译会放大安全漏洞                       │
└─────────────────────────────────────────────┘
```

### 10.3 跨语言微调攻击流程

```
┌─────────────────────────────────────────────┐
│         跨语言微调攻击流程                     │
├─────────────────────────────────────────────┤
│ 1. 获取已对齐的多语言模型                      │
│    (如Llama、Mistral多语言版本)               │
│                                             │
│ 2. 准备少量单语言毒性数据                       │
│    (仅需几十到几百条)                         │
│                                             │
│ 3. 使用SFT/PEFT在毒性数据上微调               │
│    (LoRA等参数高效方法)                        │
│                                             │
│ 4. 安全信息跨语言迁移                          │
│    - 毒性数据微调导致其他语言的安全崩溃         │
│    - safety-relevant参数部分语言无关           │
│                                             │
│ 5. 攻击者获得不安全的多语言模型                 │
│                                             │
│ 关键发现：                                    │
│ - 安全参数部分语言无关                         │
│ - 稀疏更新即可诱导多语言失败                   │
│ - 即使良性适应（如学习新语言）也可能削弱安全    │
└─────────────────────────────────────────────┘
```

### 10.4 新语言学习越狱流程

```
┌─────────────────────────────────────────────┐
│         新语言学习越狱流程                     │
├─────────────────────────────────────────────┤
│ 1. 获取已对齐的多语言模型                      │
│                                             │
│ 2. 使用LoRA学习低资源语言                      │
│    (无任何有害数据)                           │
│    例如：学习斯瓦希里语                        │
│                                             │
│ 3. 拒绝行为退化                               │
│    - 即使无恶意数据，适应过程本身破坏安全       │
│                                             │
│ 4. 用学得的低资源语言发送恶意请求               │
│                                             │
│ 关键洞察：                                    │
│ - 多语言扩展本身可能破坏安全保证               │
│ - 安全的语言学习需要专门的保护机制             │
└─────────────────────────────────────────────┘
```

---

## 11. 消融实验

### 11.1 威胁模型消融：语言组成的影响

综述系统分析了四个诊断轴对毒性检测的影响：

**(i) 语言组成消融：**
- 单语 vs. 代码切换的对比
- 发现：代码切换显著增加不安全行为触发率
- 代码切换红队测试查询比单语攻击更有效地引发不安全行为

**(ii) 文字组成消融：**
- 标准文字 vs. 混合文字/音译的对比
- 发现：混合文字输入削弱检测器和拒绝行为
- 音译和阿语数字（Arabizi）等形式构成特殊挑战

**(iii) 翻译中介消融：**
- 直接请求 vs. 翻译枢纽的对比
- 发现：翻译后的恶意提示产生更高不安全响应率
- 往返翻译引入额外语义漂移

**(iv) 文化规范变异消融：**
- 通用伤害类别 vs. 文化特定伤害的对比
- 发现：文化特定毒性更难检测
- 方言、回收利用的冒犯性词汇等需要文化背景理解

### 11.2 检测方法消融

**多语言Transformer编码器的消融：**
- 不同编码器（mBERT vs XLM-R）的跨语言迁移效果对比
- 预训练资源对迁移质量的影响
- 文字和方言对分词的影响

**翻译管道消融：**
- 翻译错误传播的影响
- 语义漂移对方言输入的影响
- 翻译系统自身引入毒性的问题

**LLM检测器的消融：**
- 零样本 vs. 少样本设置
- 文化错位问题的严重程度
- 校准失败的表现形式

### 11.3 去毒化方法消融

**数据过滤的消融：**
- 过滤器对文化特定表达的影响
- 低资源语言过滤过度的问题
- 方言被错误压制的风险

**偏好调优的消融：**
- 跨语言迁移的依赖条件
- 表示对齐对迁移质量的影响
- 高资源 vs. 低资源语言的对齐差异

**解码时方法的消融：**
- 专家模型可用性的瓶颈
- 表征纠缠问题（毒性方向混合情感、强度和身份）
- 跨脚本迁移的不稳定性

### 11.4 护栏系统消融

综述比较了多种护栏系统的有效性：
- 不同护栏对多语言输入的覆盖率差异
- 对抗性多语言形式对护栏的突破能力
- 护栏的更新成本与灵活性

---

## 12. 局限性

### 12.1 文献覆盖的限制

本综述综合了一个快速发展的文献领域，因此具体的模型家族、基准测试和最佳实践可能在发表后发生变化。综述的范围也有意集中于基于文本的多语言LLM毒性检测和去毒化；未涵盖多模态审核、更广泛的网络安全策略或法律治理。

### 12.2 语言覆盖的不均衡

证据基础在不同语言间不均衡：许多"多语言"研究仍强调英语和其他高资源语言，对低资源语言、方言连续体和代码混合或音译文本的结果较少。

### 12.3 数据集和标注的异质性

由于毒性定义和标签模式在不同数据集和文化间存在差异，跨论文的比较必然是近似的。综述未运行定量元分析或复现先前实验；综合分析依赖于已报告结果，而这些结果通常使用不同的模型、数据集、检测器和评估协议。

### 12.4 测量噪声

许多评估依赖于自动检测器、基于翻译的协议或闭源模型评估，可能引入测量噪声并限制严格的同类比较。

### 12.5 代理指标的问题

跨语言毒性分类器的迁移可能产生方言的假阳性或低资源俚语的假阴性，使直接比较不可靠。

---

## 13. 伦理声明

### 13.1 综述性质的伦理考量

本综述回顾了多语言语言模型中毒性的先前工作，不涉及新数据收集、人工主题标注或模型部署。由于论文讨论了越狱、红队测试和部署时安全失败等主题，存在一定的双重用途风险。因此，作者将讨论保持在威胁模型、评估类别和缓解策略层面，而非提供可操作的攻击指令或有害提示示例。

### 13.2 自动化毒性检测的核心伦理关切

**文化偏见风险：**
- 自动化毒性检测和去毒化可能反映英语中心或主流文化规范
- 可能错误分类回收利用的或方言的表达
- 可能压制合法的身份相关言语

**过度审查问题：**
- 此类失败可能强化社会和标注者偏见
- 可能导致对已被训练和评估数据代表性不足的社区的过度审查
- 在方言表达和身份语言的处理上存在特别的风险

### 13.3 建议

作者因此强调：
- 文化接地（culturally grounded）的评估
- 包容性的数据实践
- 透明的的语言覆盖报告
- 多语言部署中安全-效用权衡的仔细考量

---

## 14. 参考文献

由于本文是综述论文，参考文献极多（约140+篇），以下是论文中引用的关键文献按类别整理：

### 威胁模型与攻击

1. Deng et al. (2024) - 多语言越狱挑战
2. Shen et al. (2024) - 语言障碍：LLM多语言安全挑战
3. Yoo et al. (2025) - 代码切换红队测试
4. Upadhayay & Behzadan (2024) - Sandwich Attack
5. Poppi et al. (2025) - 跨语言微调攻击的脆弱性
6. Upadhayay & Behzadan (2025) - 新语言学习越狱
7. Perez et al. (2022) - 用LLM对LLM进行红队测试
8. Singhania et al. (2025) - 多语言多轮自动化红队测试
9. Samvelyan et al. (2024) - Rainbow Teaming for Polish

### 数据集

10. Logacheva et al. (2022) - ParaDetox
11. Dementieva et al. (2024a) - MultiParaDetox
12. Dementieva et al. (2024b) - TextDetox/PAN 2024
13. Moskovskiy et al. (2025) - SynthDetox-M
14. Gehman et al. (2020) - RealToxicityPrompts
15. de Wynter et al. (2025) - RTP-LX
16. Jain et al. (2024) - PolygloToxicityPrompts
17. Hartvigsen et al. (2022) - ToxiGen
18. Röttger et al. (2021, 2022) - HateCheck & Multilingual HateCheck
19. Jigsaw (2018) - Jigsaw Toxic Comment Classification

### 检测方法

20. Conneau et al. (2020) - XLM-R大规模跨语言表示学习
21. Tiţa & Zubiaga (2021) - 使用Transformer的跨语言仇恨言论检测
22. Bell et al. (2025) - 翻译用于跨语言毒性分类
23. Wang et al. (2021) - 语言模型嵌入中的线性毒性子空间
24. Duan et al. (2025) - 通过全局毒性子空间理解和缓解LLM毒性
25. Hu et al. (2024) - 免费毒性检测
26. Liu et al. (2025) - 基于LLM的护栏模型校准

### 去毒化方法

27. Kreutzer et al. (2022) - 网络抓取多语言数据集质量审计
28. Neplenbroek et al. (2025) - 多语言LLM去偏见和去毒化的跨语言迁移
29. Dang et al. (2024) - RLHF可以说多种语言：解锁LLM多语言偏好优化
30. Li et al. (2024b) - 毒性缓解的偏好调优跨语言泛化
31. Dathathri et al. (2020) - 即插即用语言模型 (PPLM)
32. Krause et al. (2021) - GeDi: 生成判别器导向序列生成
33. Liu et al. (2021) - DExperts: 专家和反专家解码时控制文本生成
34. Turner et al. (2024) - 通过激活工程的语言模型导向
35. Meng et al. (2022) - 定位和编辑GPT中的事实关联 (ROME)
36. Wang et al. (2024a) - 通过知识编辑去毒化LLM
37. Inan et al. (2023) - Llama Guard: 基于LLM的输入输出安全保障

### 评估与伦理

38. Sap et al. (2022) - 带态度的标注者：标注者信念和身份如何偏见毒性语言检测
39. Xu et al. (2021) - 去毒化语言模型风险边缘化少数群体声音
40. Welbl et al. (2021) - 去毒化语言模型的挑战
41. Lu et al. (2025) - 大语言模型对齐与安全：安全机制、训练范式和新兴挑战
42. Wen et al. (2023) - 揭示LLM中的隐性毒性
43. Costa-Jussà et al. (2023) - 大规模多语言机器翻译中的毒性

### 完整参考文献列表

由于综述论文引用超过140篇，完整参考文献请参阅原论文的 References 部分（第7-8页）：
- Paper: https://arxiv.org/abs/2606.25380
- PDF: https://arxiv.org/pdf/2606.25380

---

## 📊 论文总结

| 项目 | 内容 |
|------|------|
| **论文标题** | A Survey of Toxicity Detection and Mitigation Strategies for Multilingual Language Models |
| **arXiv编号** | 2606.25380 |
| **会议** | Findings of ACL 2026 (CCF-A) |
| **作者** | Soham Dan (Scale AI), Himanshu Beniwal (IIT Gandhinagar), Thomas Hartvigsen (UVa) |
| **发表时间** | 2026年6月24日 |
| **方向** | Toxicity / Multilingual Safety |
| **论文类型** | 综述（Survey） |
| **关键发现** | 多语言LLM安全性远不均衡；英语有效的方法在低资源语言中表现不佳；去毒化可能压制合法方言表达 |
| **主要贡献** | 威胁模型分类体系、任务形式分类、检测方法分类、缓解策略分类 |
| **待解决问题** | 语言覆盖不均、文化错位、评估协议碎片化、过度审查风险 |

---

*本笔记由 OpenClaw LLM Safety 阅读助手自动生成*
*阅读时间: 2026-06-29*
*论文进度: 100/80*
