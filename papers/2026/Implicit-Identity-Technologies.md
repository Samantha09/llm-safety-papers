# Implicit Identity Technologies for LLMs: Fingerprinting and Watermarking across Datasets, Models, and Generated Content

## 1. 基本信息

| 项目 | 内容 |
|------|------|
| **论文标题** | Implicit Identity Technologies for LLMs: Fingerprinting and Watermarking across Datasets, Models, and Generated Content |
| **作者** | Shunping Wang, Yufan Zhu, Xinyi Yu, Jing Huang, Linkang Du, Hongbin Pei, Wei Luo |
| **单位** | 西安交通大学、中国科学院信息工程研究所、迪肯大学 |
| **会议** | IJCAI-ECAI 2026 (CCF-B) |
| **arXiv编号** | 2605.29245 |
| **方向** | Fingerprinting / Watermarking / Security |
| **arXiv链接** | https://arxiv.org/abs/2605.29245 |
| **发表时间** | 2026年5月28日 |

---

## 2. 英文摘要原文（arXiv Abstract原文）

> This paper presents a survey and taxonomy of LLM fingerprinting and watermarking for identity, ownership verification, provenance, and generated-content attribution. Large language models (LLMs) require substantial investments in data, computation, and expertise, and are increasingly deployed in high-stakes settings, making it critical to protect LLM-related assets and trace their origins. Existing work has rapidly expanded across dataset provenance, model ownership, and generated-content detection, but the field remains fragmented: fingerprinting and watermarking are often used inconsistently, and methods are typically studied within isolated asset-specific settings. To address this gap, we introduce implicit identity as a unifying abstraction for verifiable but not directly observable identity signals in LLM systems. We distinguish fingerprinting as non-intrusive identity derived from intrinsic characteristics, and watermarking as intrusive identity deliberately embedded into data, models, or generated content. We then propose a lifecycle-based taxonomy that organises techniques across datasets, models, and generated content, and further separates them by verification semantics: similarity-based attribution and keyed verification. Finally, we establish an evaluation framework centred on identifiability, robustness, and deployability, summarising representative metrics under realistic access and transformation regimes. By unifying terminology, lifecycle stages, and evaluation objectives, this survey provides a structured foundation for studying LLM identity technologies and for developing more reliable mechanisms for asset protection and provenance.

---

## 3. 中文摘要翻译

本文系统性地综述了LLM指纹识别和水印技术，涵盖身份验证、所有权确认、溯源和生成内容归属等应用场景。大型语言模型（LLM）的研发需要投入大量的数据、算力和专业知识，且正越来越多地部署在高风险场景中，因此保护LLM相关资产并追溯其来源变得至关重要。现有研究已在数据集溯源、模型所有权和生成内容检测等领域快速扩展，但该领域仍处于碎片化状态：指纹识别与水印技术的概念常被混用，且相关方法通常在孤立的特定资产设置下进行研究。为解决这一问题，本文引入了**隐式身份（Implicit Identity）**作为统一抽象概念，指LLM系统中可验证但不可直接观测的身份信号。本文将指纹识别定义为基于LLM内在特征构建的**非侵入式**隐式身份，将水印定义为通过外部干预向数据、模型或生成内容中**故意嵌入**的可识别信号。随后，本文提出了一种基于生命周期的分类体系，按数据集、模型和生成内容三个阶段组织各类技术，并按验证语义进一步分类：**基于相似性的归因**和**基于密钥的验证**。最后，本文建立了以**可识别性（identifiability）、鲁棒性（robustness）和可部署性（deployability）**为中心的评估框架，在现实的访问和转换机制下总结代表性指标。通过统一术语、生命周朝阶段和评估目标，本综述为研究LLM身份技术提供了结构化基础，并为开发更可靠的资产保护和溯源机制指明了方向。

---

## 4. 研究背景

### 4.1 LLM资产保护的重要性

大型语言模型的开发需要巨额投资。以GPT-4为例，据报道其训练成本超过1亿美元。高昂的投资使得LLM相关资产成为需要保护的重要知识产权。同时，LLM的滥用和恶意利用也日益成为关键挑战——例如，恶意行为者已利用LLM生成内容构建自动化欺诈系统。

### 4.2 现有研究的两大问题

尽管LLM身份技术研究快速增长，但该领域存在两个关键问题：

1. **术语混乱（Terminological Confusion）**
   - 水印（watermarking）和指纹识别（fingerprinting）这两种主要身份技术未被明确区分
   - 例如，基于触发的特定响应机制在一些论文中被称为"指令指纹识别"，在另一些论文中被称为"后门水印"

2. **研究线路孤立（Isolated Research Lines）**
   - 现有身份研究主要在特定场景中独立发展
   - 数据集身份（dataset identity）、模型身份（model identity）和生成内容身份（generated content identity）三个方向缺乏统一理解

### 4.3 法律与监管背景

- **资产保护**：2024年Miqu模型在Hugging Face上的泄露事件凸显了模型资产保护的迫切需求
- **生成内容溯源**：中国、欧洲和美国等多个司法管辖区已建立生成内容强制标注要求，以应对虚假信息泛滥和合成欺诈问题

---

## 5. 核心贡献

本文做出了三大核心贡献：

### 5.1 统一关键概念的三层框架

提出三层概念框架来系统描述现有方法：

- **顶层**：引入**隐式身份（Implicit Identity, Implicit-ID）**作为统一抽象概念，指LLM的特定特征——不可直接观测但可验证并用于唯一标识模型
- **中间层**：区分指纹识别和 水印两种实现方式
  - **LLM指纹识别**：非侵入式隐式身份，由LLM内在特征构建
  - **LLM水印**：侵入式隐式身份，通过外部干预故意嵌入到模型、数据或生成内容中
- **底层**：按证据来源和验证路径总结现有方法，形成紧凑的设计空间视图

### 5.2 基于生命周期的分类体系

提出按验证语义组织的分类体系，涵盖数据集、模型和生成内容整个LLM生命周期：

- 揭示跨资产等价性（如数据集水印和微调水印之间共享的触发-响应逻辑）
- 支持跨层级推理：一个资产层级开发的技术可转移到另一个层级
- 为多层级LLM身份设计提供支持

### 5.3 技术目标体系

识别三个关键技术目标：

1. **可识别性（Identifiability）**：可靠区分不同LLM
2. **鲁棒性（Robustness）**：在合法部署后转换和对抗性操纵下保持稳定
3. **可部署性（Deployability）**：在现实环境中实际可行

提出按转换机制组织的通用评估模板，实现现有方法的系统性和可比性评估。

---

## 6. 研究方法

### 6.1 统一形式化框架

定义统一符号系统：
- **资产类型**：A ∈ {𝒟, ℳ, 𝒴}，其中𝒟是训练数据，ℳ是模型（如权重和内部状态），𝒴是生成内容
- **访问接口**：O_A 表示验证者与资产的交互接口，涵盖白盒（权重可访问）、灰盒（内部有限）和黑盒（仅查询）设置
- **转换函数**：τ ∈ 𝒯 表示资产发布后可能经历的转换，如数据集过滤、模型微调/量化/蒸馏/合并或输出重写

### 6.2 两种转换机制

区分两种反复出现的转换机制：

1. **所有者/良性转换（τ ∈ 𝒯_own）**
   - 反映合法的发布后适应（如过滤、微调、量化、蒸馏）
   - 主要测试身份信号在正常生命周期漂移下是否保持稳定

2. **对抗性转换（τ ∈ 𝒯_adv）**
   - 是移除、伪造或逃避身份的适应性尝试
   - 对密钥验证的可靠性有更高要求

### 6.3 两个核心任务

#### 6.3.1 资产保护任务（Asset Protection）

目标：检测和对抗未经授权使用和再分发

- **主动验证（水印）**：资产所有者通过E_k嵌入密钥标记，后期通过V_k(O_{A'})验证
- **追溯验证（指纹）**：验证者从资产中提取固有证据X(O_{A'})，通过相似性匹配V_x(O_A, O_{A'})确定所有权

#### 6.3.2 溯源任务（Provenance）

目标：追溯LLM相关资产的谱系和来源，加强数字信任和问责制

- **溯源绑定（主动）**：在创建时嵌入可验证证据
- **溯源推断（追溯）**：当不存在先验标记时，提取固有证据进行相似性匹配

### 6.4 验证维度

#### 6.4.1 基于相似性的归因（Similarity-based Attribution）

- 通过匹配器V_x(⋅,⋅)实现
- 对应非侵入式指纹识别
- 在𝒯_own下作为概率证据评估

#### 6.4.2 基于密钥的验证（Keyed Verification）

- 通过密钥标记和相应检测器V_k(⋅)实现
- 对应侵入式水印
- 额外针对𝒯_adv的可靠性

---

## 7. 实验设置

本文作为综述论文，主要贡献是系统性地整理和分类现有工作，而非进行新颖的实验评估。论文建立了评估框架，总结了代表性指标。

### 7.1 评估维度

论文建立了三个核心评估维度：

1. **Identifiability（可识别性）**
   - 可靠区分不同LLM的能力
   - 代表性指标：TPR、FPR、AUC等

2. **Robustness（鲁棒性）**
   - 在合法转换下保持身份信号稳定
   - 在对抗性操作下抵抗移除/逃避
   - 测试场景：微调、量化、蒸馏、重写等

3. **Deployability（可部署性）**
   - 在现实设置中的实际可行性
   - 考虑因素：计算开销、延迟影响、误报率等

### 7.2 访问条件设置

论文考虑了三种实际访问设置：

- **White-box**：权重可用
- **Grey-box**：内部状态有限
- **Black-box**：仅通过API查询

---

## 8. 实验结果

### 8.1 数据集身份技术

#### 8.1.1 统计数据集指纹识别

通过检测模型统计中的数据集特定记忆信号（如损失/困惑度差距、似然异常或聚合成员分数）来提供非密钥证据，证明模型已暴露于目标数据集。

**代表性工作**：
- Carlini et al. (2021)：序列或聚合级别的可检测成员效应
- Membership inference attacks：通过损失异常检测数据成员身份

**鲁棒性挑战**：
- 微调、蒸馏和分布偏移会稀释或掩盖成员痕迹
- 需要在语义相似语料库下评估并控制混杂因素

#### 8.1.2 特定响应数据集指纹识别

通过精心设计的成员敏感查询集探测模型，分析目标行为特征而非全局统计：

**典型信号**：
- 置信度/边缘模式
- 对特定触发器的特定响应

**挑战**：
- 需要大量实验性探测
- 触发器设计复杂

### 8.2 模型身份技术

#### 8.2.1 模型水印

**方法分类**：

1. **基于微调的水印**
   - 通过微调将触发-响应对嵌入模型
   - 类似后门攻击机制

2. **基于权重的签名**
   - 在模型权重中嵌入可验证信号
   - 需要白盒访问

3. **基于API的黑盒水印**
   - 通过查询-响应对建立水印
   - 无需访问模型内部

#### 8.2.2 模型指纹识别

1. **行为指纹**
   - 通过探测模型响应提取特征
   - 使用相似性匹配进行验证

2. **表示指纹**
   - 分析模型内部表示
   - 需要灰盒或白盒访问

### 8.3 生成内容身份技术

#### 8.3.1 水印方法

**统计水印**：
- 采样时的字母分布偏差
- Gumbel softmax等方法

**几何水印**：
- 在表示空间中嵌入信号
- 更鲁棒于文本重写

**语法水印**：
- 利用生成文本的语法特征
- 检测效率高

#### 8.3.2 指纹识别方法

**输出-only指纹**：
- 仅通过生成的文本识别模型
- 适用于黑盒场景

---

## 9. 策略示例

### 9.1 数据集指纹识别策略

```
资产: 训练数据集 D
目标: 确定嫌疑模型 M' 是否在 D 上训练
方法: 
  1. 从 M' 通过 API 获取 logprobs
  2. 计算成员分数统计
  3. 与对照语料库比较
  4. 判定相似性匹配结果
```

### 9.2 模型水印嵌入策略

```
所有者操作:
  1. 选择密钥 k
  2. 设计触发-响应对 (t_i, r_i)
  3. 通过 E_k 将水印嵌入模型 → M~
  4. 发布 M~

验证者操作:
  1. 获取嫌疑模型 M' (经过转换 τ)
  2. 使用密钥检测器 V_k(O_{M'})
  3. 判定所有权
```

### 9.3 生成内容水印策略

```
生成时嵌入:
  1. 采样时引入字母分布偏差
  2. 或在表示空间嵌入几何信号
  
检测时:
  1. 分析生成文本统计特征
  2. 运行统计假设检验
  3. 输出检测结果和置信度
```

---

## 10. 攻击流程

### 10.1 身份移除攻击

**目标**：移除或逃避隐式身份信号

1. **水印移除攻击**
   - 通过微调目标训练移除水印
   - 对抗性重写文本
   - 触发器抑制攻击

2. **指纹混淆攻击**
   - 使用模仿攻击模拟其他模型
   - 改变模型行为

### 10.2 身份伪造攻击

**目标**：伪造合法身份信号

1. **后门注入**
   - 向模型注入恶意触发器
   - 声称是"水印"

2. **模仿攻击**
   - 通过特定prompt诱导模型响应
   - 伪装成目标模型

### 10.3 逃避攻击

**目标**：避免被检测到

1. **查询策略优化**
   - 选择性查询避免触发水印
   - 最小化暴露风险

2. **混合策略**
   - 结合多种转换
   - 逐步侵蚀身份信号

---

## 11. 消融实验

本文作为综述，未进行传统意义上的消融实验。但论文的分类体系揭示了各技术的组件特性：

### 11.1 指纹识别方法组件分析

| 组件 | 作用 | 影响 |
|------|------|------|
| 证据来源 | 定义可验证信号 | 决定检测精度 |
| 访问条件 | 确定所需接口 | 影响部署场景 |
| 转换应力 | 测试信号稳定性 | 决定鲁棒性 |

### 11.2 水印方法组件分析

| 组件 | 作用 | 影响 |
|------|------|------|
| 密钥设计 | 保证唯一性和安全性 | 决定防伪能力 |
| 嵌入机制 | 信号插入方式 | 影响模型效用 |
| 检测器 | 验证信号存在 | 决定准确率 |

### 11.3 跨资产等价性发现

论文揭示的重要发现：

1. **数据集水印 ≈ 微调水印**
   - 共享触发-响应逻辑

2. **行为模型指纹 ≈ 输出指纹**
   - 共享归因逻辑

3. **技术可迁移性**
   - 一个资产层级开发的技术可应用于其他层级

---

## 12. 局限性

### 12.1 技术局限性

1. **黑盒场景挑战**
   - 许多技术需要白盒或灰盒访问
   - 现实部署主要黑盒场景受限

2. **鲁棒性与效用的权衡**
   - 更强的身份信号可能影响模型性能
   - 嵌入水印可能改变模型行为

3. **对抗性攻击**
   - 专门设计的移除攻击可能有效
   - 需要持续更新防御机制

### 12.2 实际部署挑战

1. **规模化问题**
   - 实时水印嵌入的计算开销
   - 大规模验证的延迟

2. **跨平台兼容性**
   - 不同模型的接口差异
   - 标准缺失

3. **法律认可**
   - 司法管辖区的法律差异
   - 证据效力认定

### 12.3 未来研究方向

1. **更强的鲁棒性**
   - 抵抗高级对抗性攻击
   - 适应多种转换机制

2. **更好的可部署性**
   - 降低计算开销
   - 减少延迟影响

3. **标准化**
   - 统一评估基准
   - 建立行业标准

---

## 13. 伦理声明

### 13.1 积极影响

1. **资产保护**
   - 保护LLM研发投资
   - 防止未经授权使用

2. **溯源追踪**
   - 应对虚假信息
   - 支持监管合规

3. **问责机制**
   - 建立明确责任链
   - 支持恶意行为追溯

### 13.2 潜在滥用风险

1. **识别技术用于监控**
   - 可能被用于追踪用户
   - 隐私风险

2. **水印技术用于审查**
   - 可能被用于压制言论
   - 限制信息流通

3. **指纹技术用于追踪**
   - 可能被用于定位异见人士
   - 侵犯公民自由

### 13.3 作者声明

作者声明本研究旨在促进LLM资产保护和溯源技术的良性发展，强调伦理考量应贯穿技术设计和部署全过程。

---

## 14. 参考文献

本文作为综述，引用了大量相关工作。以下为主要参考文献类别：

### 14.1 基础论文

1. Carlini et al. "Extracting Training Data from Large Language Models" (USENIX Security 2021)
2. Kirchenbauer et al. "A Watermark for Large Language Models" (ICML 2023)
3. Zhang et al. "REEF: Robust Watermark for Language Models" (2024)

### 14.2 数据集身份

4. Maini et al. "Dataset Identity" (2021)
5. Huang et al. "Generalization of Membership Inference" (2024)

### 14.3 模型身份

6. Zeng et al. "HUREF: Unremovable Watermarking" (2024)
7. Xu et al. "Instructional Fingerprinting" (2024)
8. Mo et al. "TIBW: Backdoor Watermarking" (2025)

### 14.4 生成内容身份

9. Hou et al. "SemStamp" (2024)
10. Hu et al. "Unbiased Watermarking" (2023)

### 14.5 综述论文

11. Liu et al. "Survey on Watermarking" (2024)
12. Wang et al. "Building Watermarking" (2025)
13. Liang et al. "Watermarking Technologies" (2026)
14. Xu et al. "Copyright Protection" (2025)
15. Ye et al. "Securing LLMs" (2025)

---

## 附录：论文分类体系概览

```
                    Implicit-ID 隐式身份
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
   Fingerprinting    Watermarking       (统一抽象)
    (非侵入式)         (侵入式)
        │                 │
        ▼                 ▼
  相似性归因         密钥验证
  (Matcher Vx)      (检测器 Vk)
        │                 │
   ┌────┴────┐       ┌────┴────┐
   │         │       │         │
 Dataset   Model   Dataset   Model   Content
   │         │       │         │         │
 统计指纹  行为指纹  微调水印  权重水印  统计水印
 响应指纹  表示指纹  API水印   黑盒水印  几何水印
```

---

**笔记完成日期**：2026年6月1日

**备注**：本笔记基于arXiv论文摘要和HTML全文提取内容整理，因PDF下载超时，完整内容可能有所遗漏。