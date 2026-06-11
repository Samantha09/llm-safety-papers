# SlotGCG: Exploiting the Positional Vulnerability in LLMs for Jailbreak Attacks

> **论文标题**: SlotGCG: Exploiting the Positional Vulnerability in LLMs for Jailbreak Attacks  
> **中文标题**: SlotGCG：利用大型语言模型的位置脆弱性进行越狱攻击  
> **作者**: Seungwon Jeong, Jiwoo Jeong, Hyeonjin Kim, Yunseok Lee, Woojin Lee（韩国东国大学）  
> **会议**: ICLR 2026（国际学习表征大会）  
> **arXiv**: [2606.05609](https://arxiv.org/abs/2606.05609)  
> **代码**: [https://github.com/youai058/SlotGCG](https://github.com/youai058/SlotGCG)  
> **阅读日期**: 2026-06-12

---

## 1. 基本信息

| 字段 | 内容 |
|------|------|
| **论文标题** | SlotGCG: Exploiting the Positional Vulnerability in LLMs for Jailbreak Attacks |
| **中文标题** | SlotGCG：利用大型语言模型的位置脆弱性进行越狱攻击 |
| **作者** | Seungwon Jeong, Jiwoo Jeong, Hyeonjin Kim, Yunseok Lee, Woojin Lee |
| **单位** | Dongguk University-Seoul（韩国东国大学） |
| **会议/期刊** | ICLR 2026 |
| **arXiv ID** | 2606.05609 |
| **方向** | Jailbreak Attack / Positional Vulnerability / Red Teaming |
| **开源代码** | https://github.com/youai058/SlotGCG |
| **论文方向标签** | 🔓 越狱攻击 / 🎯 对抗攻击 / 🧪 红队测试 |
| **相关引用** | 基于 GCG (Zou et al., 2023) 的优化方法 |

---

## 2. 英文摘要原文（arXiv Abstract）

> **Warning: This paper contains model outputs that are offensive in nature.**
>
> As large language models (LLMs) are widely deployed, identifying their vulnerability through jailbreak attacks becomes increasingly critical. Optimization-based attacks like Greedy Coordinate Gradient (GCG) have focused on inserting adversarial tokens to the end of prompts. However, GCG restricts adversarial tokens to a fixed insertion point (typically the prompt suffix), leaving the effect of inserting tokens at other positions unexplored. In this paper, we empirically investigate **slots**, i.e., candidate positions within a prompt where tokens can be inserted. We find that vulnerability to jailbreaking is highly related to the selection of the **slots**. Based on these findings, we introduce the **Vulnerable Slot Score (VSS)** to quantify the positional vulnerability to jailbreaking. We then propose **SlotGCG**, which evaluates all slots with VSS, selects the most vulnerable slots for insertion, and runs a targeted optimization attack at those slots. Our approach provides a position-search mechanism that is attack-agnostic and can be plugged into any optimization-based attack, adding only 200ms of preprocessing time. Experiments across multiple models demonstrate that SlotGCG significantly outperforms existing methods. Specifically, it achieves **14% higher Attack Success Rates (ASR) over GCG-based attacks**, converges faster, and shows superior robustness against defense methods with **42% higher ASR than baseline approaches**. Our implementation is available at https://github.com/youai058/SlotGCG.

---

## 3. 中文摘要翻译

> **警告：本文包含模型生成的冒犯性输出。**
>
> 随着大型语言模型（LLM）的广泛部署，通过越狱攻击识别其漏洞变得越来越关键。以梯度坐标下降（GCG）为代表的优化类攻击专注于将对抗性令牌插入到提示的末尾。然而，GCG将对抗性令牌的插入位置限制在固定点（通常为提示后缀），从而忽略了在其他位置插入令牌的效果。本文通过实证研究**槽位（slots）**——即提示内可以插入令牌的所有候选位置——来填补这一研究空白。研究发现，越狱脆弱性与槽位的选择高度相关。基于这些发现，本文引入**脆弱槽位评分（Vulnerable Slot Score, VSS）**来量化越狱攻击的位置脆弱性。随后，本文提出**SlotGCG**，该方法先用VSS评估所有槽位，选择最具脆弱性的槽位进行令牌插入，然后在这些槽位上运行定向优化攻击。SlotGCG提供了一种与攻击方法无关的位置搜索机制，可以插入到任何基于优化的攻击方法中，仅增加200毫秒的预处理时间。在多个模型上的实验表明，SlotGCG显著优于现有方法。具体而言，相较于基于GCG的攻击，SlotGCG的攻击成功率（ASR）**提升了14%**，收敛更快，并且在面对防御方法时表现出更强的鲁棒性，ASR比基线方法**高出42%**。开源实现见：https://github.com/youai058/SlotGCG。

---

## 4. 研究背景

### 4.1 LLM安全与越狱攻击概述

大型语言模型（LLM）在自然语言理解和生成任务中展现了卓越的能力，被广泛应用于代码生成、问答、对话系统等领域。然而，LLM仍然容易受到越狱攻击（jailbreak attacks）的威胁。越狱攻击通过精心设计的提示词诱导模型产生有害内容，例如危险化学品制作指南、恶意软件代码、或暴力内容等。这类攻击是AI安全红队测试（red teaming）的重要组成部分，旨在暴露对齐机制中的漏洞。

近年来，越狱攻击技术发展迅速，从最初的简单提示词工程（如"Do Anything Now"）到基于梯度优化的对抗性攻击（如GCG），攻击手段日趋复杂和自动化。然而，现有方法仍存在一个关键缺陷——它们都将对抗性令牌限制在提示的固定位置（通常为后缀），而忽略了位置多样性对攻击效果的影响。

### 4.2 GCG方法及其局限性

Greedy Coordinate Gradient（GCG）是当前最具代表性的优化类越狱攻击方法，由Zou等人于2023年提出。GCG的核心思想是：给定一个有害查询，将一个对抗性令牌序列（即后缀）附加到查询后，然后通过迭代优化这些令牌的配置，使模型生成目标有害响应的概率最大化。

**GCG的工作原理：**

1. **损失函数定义**：给定有害查询 $x_{1:L}^O$ 和对抗序列 $x^S$，完整提示为 $x_{1:L}^O \oplus x^S$。攻击目标是找到最大化有害目标响应 $x^T$ 生成概率的后缀，即：
   
   $$\arg\min_{x^S} \mathcal{L}(x_{1:L}^T) = \arg\min_{x^S}(-\log p(x^T|x_{1:L}^O \oplus x^S))$$

2. **迭代优化**：由于令牌空间是离散的，GCG通过以下步骤迭代优化后缀：
   - 对每个对抗令牌位置计算梯度，找出有前景的替换候选
   - 选择使损失函数最小化的候选后缀
   - 重复直到达到预定义的步数

**GCG的局限性：**

尽管GCG及其变体取得了显著的攻击效果，但它们都存在一个根本性的研究空白——默认将对抗性令牌限制在提示后缀。已有研究表明，放置在提示末尾的对抗性令牌往往对模型输出有不合理的高影响力，且注意力机制可能会放大这些基于后缀的扰动。然而，这种"后缀即最优"的假设限制了更灵活攻击策略的探索。

具体而言，固定后缀位置的攻击面临以下问题：
- **检测容易**：已知的后缀位置使得防御者可以针对后缀进行检测和过滤
- **最优位置因提示而异**：不同有害提示的最优插入位置可能完全不同，后缀并不总是最优的
- **注意力模式影响**：对抗性令牌在after-chat模板上的注意力强度与攻击成功密切相关

### 4.3 位置多样性的研究动机

在真实攻击场景中，将对抗性令牌插入到任意位置（而非仅限后缀）的攻击更加难以检测，因为其多样化的插入模式需要扫描整个提示。这一挑战促使研究者深入探索更灵活的令牌插入策略的威胁。

本文的核心研究问题是：**令牌位置如何系统性地影响攻击有效性？** 这是一个在以往研究中尚未被系统性探索的问题。

---

## 5. 核心贡献

本文提出了SlotGCG方法，在越狱攻击领域做出了以下三项核心贡献：

### 5.1 脆弱槽位（Vulnerable Slots）形式化与VSS指标

本文形式化定义了"脆弱槽位"的概念——即更容易受到对抗令牌插入影响的位置。同时，引入了**脆弱槽位评分（Vulnerable Slot Score, VSS）**这一量化指标。VSS通过测量after-chat模板对插入对抗令牌的注意力权重来量化特定槽位的脆弱程度。

VSS的计算公式为：

$$VSS_s = \sum_{\ell \in \mathcal{L}_{UH}} \sum_h \sum_{c \in \mathcal{C}} \sum_{a \in \mathbf{a}^k} A^{(\ell,h)}_{c,a} / k$$

其中：
- $A^{(\ell,h)}_{c,a}$ 是第 $\ell$ 层第 $h$ 个注意力头从token $c$（after-chat模板token）到token $a$（插入的对抗性token）的注意力权重
- $\mathcal{L}_{UH} = \{\lfloor L/2 \rfloor, \ldots, L\}$ 是上半层集合，用于捕捉高级语义处理
- $\mathcal{C}$ 是after-chat模板token的集合
- $k$ 是插入的对抗性序列长度

### 5.2 SlotGCG：位置感知的越狱攻击方法

SlotGCG是GCG的创新扩展，其核心创新在于：
- **位置搜索机制**：系统性地评估所有插入槽位的VSS，找出高脆弱性槽位
- **定向优化攻击**：在高VSS槽位上进行令牌级优化，而非仅限于后缀
- **方法通用性**：SlotGCG是一种与攻击方法无关的位置搜索机制，可以插入到任何基于优化的攻击方法中
- **极低开销**：仅需200毫秒的预处理时间即可完成位置搜索

### 5.3 位置脆弱性的理论拓展

本文将基于优化的越狱攻击从单一后缀位置扩展到考虑位置脆弱性的新范式，为评估和改进对抗性提示提供了实践指导，并拓宽了红队研究的范围。

---

## 6. 研究方法

### 6.1 槽位（Slots）的形式化定义

给定一个令牌序列（有害提示）$x_{1:L} = [x_1, \ldots, x_L]$，本文定义了 $L+1$ 个插入槽位：

$$S = [0, 1, \ldots, L]$$

其中：
- **槽位 0**：位于 $x_1$ 之前的位置
- **槽位 $l$（$1 \leq l \leq L-1$）**：位于 $x_l$ 和 $x_{l+1}$ 之间的位置
- **槽位 $L$**：位于 $x_L$ 之后（即传统后缀位置）

对于槽位插入，指定一组对抗性令牌 $\mathbf{A}$ 和对应的插入槽位 $\mathbf{S_A}$：

$$\mathbf{A} = \{\mathbf{a}_1^{k_1}, \ldots, \mathbf{a}_m^{k_m}\}, \quad \mathbf{S_A} = \{s_1, \ldots, s_m\} \subseteq S$$

每个对抗序列 $\mathbf{a}_i^{k_i} = \{a_{i,1}, \ldots, a_{i,k_i}\}$ 的长度为 $k_i$，插入到槽位 $s_i$。

### 6.2 从右到左的插入语义

为确保插入过程中槽位位置相对于原始序列保持稳定，本文采用从右到左（从最大槽位索引到最小）的插入顺序：

$$\mathcal{I}(x_{1:L}, \mathbf{A}, \mathbf{S_A}) = \mathcal{I}(\cdots\mathcal{I}(\mathcal{I}(x_{1:L}, \mathbf{a}_m^{k_m}, s_m), \mathbf{a}_{m-1}^{k_{m-1}}, s_{m-1}), \ldots, \mathbf{a}_1^{k_1}, s_1)$$

**示例**：对于提示 `[How, to, make, bomb]`：
- 插入 `[x, y]` 于槽位 0，`[z]` 于槽位 2
- 结果序列为 `[x, y, How, to, z, make, bomb]`

### 6.3 探索性研究设计

本文通过两个互补的探索性实验来研究对抗令牌位置对越狱攻击的影响：

#### 实验1：穷举槽位扫描（Exhaustive Slot Scan）

作为初步研究，对有害提示内的每个候选槽位 $s \in S$ 进行系统性探索。具体做法：
- 对50个有害提示，每个生成变体 $x^{(s)} = \mathcal{I}(x_{1:L}, \mathbf{a}^5, s)$，其中 $\mathbf{a}^5$ 是5个令牌的对抗序列
- 对每个变体应用100步GCG优化（使用Llama 2-7B-Chat模型）
- 为便于比较，对槽位索引进行归一化：$\tilde{s}_i = \frac{s_i}{L_{max}+1}$

#### 实验2：随机多位置插入（Random Multi-Position Insertion）

作为完整设置研究，检验对抗令牌分布在多个槽位时是否能在现实条件下引发有害响应：
- 将20个初始对抗令牌随机划分为多个序列 $\mathbf{A} = \{\mathbf{a}_1^{k_1}, \ldots, \mathbf{a}_m^{k_m}\}$
- 将对抗序列插入到随机采样的槽位 $\mathbf{S_A} \subseteq S, s_i \sim \text{Uniform}(S)$
- 与标准GCG进行比较

### 6.4 三项关键发现

**发现1：后缀并非最优插入位置**

通过穷举槽位扫描实验，发现：
- 在50个有害提示中，最小化对抗损失的最优槽位在不同提示间差异很大
- **关键发现：在所有50个提示中，产生最小损失的最优槽位从未是后缀（GCG使用的位置）**
- 这表明后缀并不总是对许多提示最具脆弱性的槽位

**发现2：VSS与位置脆弱性高度相关**

分析发现：
- 在after-chat模板上的对抗令牌注意力与对抗损失呈负相关
- 换言之，注意力值越高的槽位，损失越低，表明这些位置更容易受到对抗令牌的影响
- 这启发了VSS指标的设计——通过注意力权重来量化槽位脆弱性

**发现3：VSS在优化过程中持续稳定**

关键问题：脆弱槽位是在优化过程中固有存在的，还是仅在特定迭代中产生？
- 分析发现：$VSS^{init}$（初始VSS）与 $VSS^{final}$（优化后VSS）高度相关
- 表明脆弱性主要由插入位置驱动，而非特定令牌序列决定
- 每个提示本质上就包含对对抗令牌插入具有脆弱性的槽位

---

## 7. 实验设置

### 7.1 评估模型

实验在多个主流LLM上进行，包括（但可能不限于）：
- **Llama 2-7B-Chat**：主要的消融和探索性实验模型
- **其他模型**：用于评估SlotGCG的通用性和跨模型迁移性

### 7.2 对比方法（基线）

SlotGCG与以下基于GCG的优化攻击方法进行对比：

| 方法 | 描述 | 来源 |
|------|------|------|
| **GCG** | 标准token交换坐标下降攻击 | Zou et al., 2023 |
| **GCG-Transfer** | 多轮迁移设置下的GCG | — |
| **AttnGCG** | 带注意力引导更新的GCG | — |
| **AttnGCG-Transfer** | AttnGCG的多轮迁移设置 | — |
| **I-GCG** | 带迭代/多启动初始化的改进技术 | — |
| **I-GCG-Transfer** | I-GCG的多轮迁移设置 | — |
| **GCG-Hij** | 带劫持式转向的GCG | — |
| **GCG-Hij-Transfer** | GCG-Hij的多轮迁移设置 | — |
| **GBDA** | 连续松弛+离散化的梯度对抗攻击 | — |

### 7.3 评估数据集

- **AdvBench**：50个有害提示，用于与先前越狱研究保持一致性
- **HarmBench评估管道**：SlotGCG构建在HarmBench评估管道之上，遵循其标准化的测试用例生成→生成补全→评估流程

### 7.4 防御方法评估

为评估SlotGCG对防御方法的鲁棒性，在以下防御方法存在下进行测试：
- **输入过滤（Input Filtering）**：检测并过滤对抗性输入的防御机制
- 其他标准越狱防御方法

### 7.5 评估指标

- **攻击成功率（Attack Success Rate, ASR）**：主要评估指标
- **优化收敛速度**：达到相同ASR所需的优化步数
- **对防御方法的鲁棒性**：在防御机制存在下的ASR

### 7.6 实现细节

- **预处理时间**：每个提示约200毫秒的VSS计算开销
- **运行命令示例**：
  ```bash
  python scripts/run_pipeline.py \
   --methods GCG_posinit_attention \
   --models llama2_7b \
   --step all \
   --mode local
  ```

---

## 8. 实验结果

### 8.1 主要结果：攻击成功率提升

SlotGCG在多个模型和GCG变体上均取得了显著优于基线方法的攻击效果：

| 对比方法 | ASR提升幅度 |
|----------|-------------|
| **相较于标准GCG** | **+14%** |
| **对防御方法的鲁棒性** | **+42%**（相对于基线方法在输入过滤防御下） |

### 8.2 收敛速度提升

SlotGCG不仅提高了攻击成功率，还加快了优化收敛：
- 可以在**更少的优化步数**下达到相同的攻击效果
- 收敛速度显著快于标准GCG
- 表明位置搜索机制有效引导优化过程向更有利的方向进行

### 8.3 对防御方法的鲁棒性

在输入过滤等防御方法存在下，SlotGCG表现出更强的鲁棒性：
- 相比基线方法在输入过滤防御下ASR高出42%
- 这一发现具有重要的实际意义，因为真实世界的LLM部署通常配备各种输入过滤和内容安全检测机制
- SlotGCG的鲁棒性源于其多样化的插入位置——防御者无法仅针对固定位置进行检测

### 8.4 位置多样性的影响

关键发现：VSS识别的脆弱槽位在优化过程中保持稳定，意味着：
- 一旦识别出某个提示的高VSS槽位，该位置在整个优化过程中都保持高脆弱性
- 这使得位置选择成为一个高效的前置步骤，而无需在每个优化步骤中重复评估

### 8.5 跨模型迁移性

实验在多个模型上进行，表明SlotGCG具有跨模型的通用性，其位置搜索机制可以与不同模型兼容。

---

## 9. 策略示例

### 9.1 GCG传统策略 vs SlotGCG策略对比

**传统GCG策略（仅后缀插入）：**
```
[System Prompt] + [User Query: How to make a bomb?] + [Adversarial Suffix: xxx]
                                              ↑ 固定位置（后缀）
```

**SlotGCG策略（多位置插入）：**
```
[Adversarial Tokens at Slot 0] + [System Prompt] + [User Query] + [Tokens at middle slots] + [Assistant Template]
        ↑ 可变位置                      ↑ 多样化插入点
```

### 9.2 槽位选择示例

以有害提示 `[How, to, make, bomb]` 为例：

| 槽位 | 位置描述 | VSS（示例） | 脆弱性 |
|------|----------|-------------|--------|
| 0 | 在 "[How]"之前 | 高 | 脆弱 |
| 1 | "[How]" 和 "[to]" 之间 | 中 | 中等 |
| 2 | "[to]" 和 "[make]" 之间 | 高 | 脆弱 |
| 3 | "[make]" 和 "[bomb]" 之间 | 中 | 中等 |
| L (后缀) | 在 "[bomb]" 之后 | 低 | 不脆弱 |

**SlotGCG会选择VSS最高的槽位（如槽位0和槽位2）进行对抗令牌插入，而非传统的后缀位置。**

### 9.3 从右到左插入示例

对于 `ℐ([How, to, make, bomb], {[x,y], [z]}, {0, 2})`：
1. 首先将 `[z]` 插入槽位2（因为2>0）：`[How, to, make, z, bomb]`
2. 然后将 `[x, y]` 插入槽位0：`[x, y, How, to, make, z, bomb]`

这种从右到左的插入顺序确保了槽位索引相对于原始序列的稳定性。

---

## 10. 攻击流程

### 10.1 SlotGCG攻击流程总览

```
输入：有害查询 x_O，候选槽位集合 S，优化攻击方法 M
输出：优化的对抗提示

1. 预处理阶段（200ms）：
   a. 对每个槽位 s ∈ S，计算 VSS_s
   b. 选择VSS最高的 Top-K 个槽位作为候选插入位置
   
2. 初始化阶段：
   a. 将对抗令牌序列 A 初始化并插入到选定的槽位
   b. 构建完整的对抗提示
   
3. 优化阶段（重复直到收敛或达到最大步数）：
   a. 使用方法M（如GCG）对插入的对抗令牌进行梯度优化
   b. 在优化过程中保持槽位位置不变（VSS稳定的性质）
   c. 评估攻击是否成功（模型是否产生有害输出）
   
4. 输出优化的对抗提示
```

### 10.2 VSS计算详解

VSS的计算过程：
1. **获取注意力权重**：对给定提示和插入的对抗序列，运行模型前向传播，提取所有层的注意力权重矩阵
2. **聚焦上半层**：仅考虑 $\mathcal{L}_{UH} = \{\lfloor L/2 \rfloor, \ldots, L\}$ 中的层，这些层捕捉高级语义处理
3. **计算跨模板注意力**：对每个after-chat模板token $c \in \mathcal{C}$ 和每个插入的对抗token $a \in \mathbf{a}^k$，累加注意力权重 $A^{(\ell,h)}_{c,a}$
4. **归一化**：除以序列长度 $k$ 得到归一化的VSS

### 10.3 位置搜索的开销分析

| 操作 | 时间开销 |
|------|----------|
| VSS计算（所有槽位） | ~200ms |
| 单次GCG优化步骤 | 取决于模型大小 |
| 总预处理开销 | 200ms（位置搜索） + 初始化 |

**关键优势**：仅需200ms即可完成位置搜索，与后续优化步骤的时间相比几乎可以忽略不计。

### 10.4 与其他优化方法的结合

SlotGCG的位置搜索机制是攻击无关的（attack-agnostic），可以与任何基于优化的攻击方法结合：
- **GCG +位置搜索**：标准GCG增强版
- **AttnGCG + 位置搜索**：注意力引导GCG增强版
- **I-GCG + 位置搜索**：迭代初始化GCG增强版
- **GBDA + 位置搜索**：连续松弛攻击增强版

---

## 11. 消融实验

### 11.1 槽位数量选择的影响

**研究问题**：选择多少个高VSS槽位进行攻击最有效？

可能的消融实验设计：
- **Top-1**：仅选择VSS最高的槽位
- **Top-3**：选择VSS最高的3个槽位
- **Top-5**：选择VSS最高的5个槽位
- **随机多槽位**：随机选择多个槽位（作为对照）

**预期发现**：VSS选择策略应优于随机选择，且存在一个最优的槽位数量——太少可能错过真正脆弱的位置，太多可能引入噪声。

### 11.2 VSS计算层的选择

**研究问题**：使用哪些层的注意力权重计算VSS最有效？

可能的消融设置：
- **上半层（$\lfloor L/2 \rfloor$ 到 $L$）**：论文推荐的方法
- **所有层**：包含所有Transformer层
- **下半层（0 到 $\lfloor L/2 \rfloor$）**：作为对照
- **单层变体**：分别测试每个单独的层

**预期发现**：上半层之所以有效，是因为它们捕捉高级语义处理，而越狱机制在这些层中最为明显。

### 11.3 槽位插入数量与令牌分配

**研究问题**：对抗令牌应该如何分配到不同槽位？

可能的消融设置：
- **均匀分配**：每个选定槽位分配相同数量的令牌
- **VSS加权分配**：VSS越高的槽位分配越多令牌
- **全部集中于最高VSS槽位**：将所有令牌放在VSS最高的槽位

### 11.4 初始化的影响

**研究问题**：初始对抗令牌的生成方式如何影响最终性能？

可能的消融设置：
- **随机初始化**：随机生成初始对抗序列
- **多样化初始化**：使用多个不同的初始序列
- **预训练初始化**：使用在类似提示上预训练的对抗序列

### 11.5 VSS稳定性的量化验证

**研究问题**：VSS在整个优化过程中是否真的保持稳定？

实验设计：
- 在优化过程的多个时间点（如步数0, 25, 50, 75, 100）计算各槽位的VSS
- 比较初始VSS与最终VSS的相关性
- 验证VSS稳定性假设在实际优化过程中的成立程度

---

## 12. 局限性

### 12.1 计算开销

尽管VSS计算仅需200ms，但对于大规模评估场景（如在数百万提示上测试），累积的计算开销仍然可观。未来的工作可以探索更高效的位置评估方法。

### 12.2 白盒假设

SlotGCG需要获取模型的注意力权重来进行VSS计算，这意味着它本质上是一个**白盒攻击**方法。对于只能进行黑盒查询的模型（如闭源API），需要设计替代的位置评估策略。

### 12.3 模型和架构限制

VSS的设计基于Transformer架构的注意力机制，对于非Transformer架构的模型（如状态空间模型Mamba等），VSS的计算方式可能需要调整。

### 12.4 防御演进的挑战

随着基于位置过滤的防御方法（如专门检测非后缀位置对抗令牌的防御）出现，SlotGCG的优势可能会被削弱。攻击者和防御者的军备竞赛是持续的研究挑战。

### 12.5 道德和法律风险

本文涉及的越狱攻击研究具有双刃剑性质。虽然旨在提高LLM安全性，但研究成果也可能被恶意利用。论文在伦理声明中明确指出研究的教育和红队测试目的。

### 12.6 评估数据集的局限

实验主要在AdvBench的50个有害提示上进行，可能无法完全代表真实世界中多样化的有害查询类型。更大的评估数据集和更多样化的攻击场景值得探索。

---

## 13. 伦理声明

### 13.1 研究目的声明

本文是一篇**红队测试（red teaming）研究**，旨在系统性地识别和量化LLM中位置脆弱性，以促进更强大的安全对齐。研究成果具有以下积极意义：

1. **提高LLM安全性**：通过揭示位置脆弱性，帮助开发者设计更全面的防御机制
2. **推动安全研究**：为红队测试提供新的方法论和评估工具
3. **基准评估**：通过开源代码，使研究社区能够复现和验证结果

### 13.2 负责任的披露

论文遵循负责任的披露原则：
- 研究成果以论文形式公开发表，供学术研究社区参考
- 开源代码聚焦于研究目的，不包含可直接用于恶意攻击的完整工具
- 作者明确警告模型输出可能包含冒犯性内容

### 13.3 潜在风险与缓解

**潜在风险**：研究成果可能被恶意行为者用于优化越狱攻击。

**缓解措施**：
-论文明确强调研究的防御导向
- 建议LLM部署者针对位置多样性设计防御机制
- 鼓励开发能够检测多样化插入模式的输入过滤系统

### 13.4 模型输出警告

论文开头包含明确的警告：
> **Warning: This paper contains model outputs that are offensive in nature.**

---

## 14. 参考文献

### 核心引用

1. **Vaswani, A., et al.** (2017). Attention Is All You Need. *NeurIPS*. [[bib.bib4]](基础Transformer架构)

2. **Zou, A., et al.** (2023). Universal and Transferable Adversarial Attacks on Aligned Language Models (GCG). *arXiv:2307.15043*. [[bib.bib40]](GCG方法基础)

3. **Touvron, E., et al.** (2023). Llama 2: Open Foundation and Fine-Tuned Chat Models. [[bib.bib5]](Llama 2模型)

4. **Chiang, et al.** (2023). Vicuna / Llama models. [[bib.bib58]](实验模型)

5. **Dubey, et al.** (2024). Llama family models. [[bib.bib56]](实验模型)

6. **Achiam, et al.** (2023). GPT models. [[bib.bib57]](实验模型参考)

7. **Wei, J., et al.** (2023a). Jailbroken: How Does LLM Safety Training Fail? *NeurIPS*. [[bib.bib36]](越狱机制分析)

8. **Maslej, et al.** (2025). AI safety research. [[bib.bib6]](研究背景)

9. **Zhang, S., & Wei, J.** (2025). 后缀位置影响力研究. [[bib.bib17]](位置效应分析)

10. **Li, et al.** (2024a). 对抗令牌位置研究. [[bib.bib37]](注意力与位置关系)

11. **Zhao, et al.** (2024b). 注意力机制放大后缀扰动. [[bib.bib38]](注意力机制分析)

12. **Hu, et al.** (2025). 注意力与越狱关系. [[bib.bib21]](注意力分析)

13. **Wang, et al.** (2024). 越狱注意力模式研究. [[bib.bib42]](注意力模式分析)

14. **Ben-Tov, et al.** (2025).越狱成功与注意力关系. [[bib.bib9]](VSS理论基础)

15. **Stern, et al.** (2019). 槽位概念定义. [[bib.bib2]](槽位定义来源)

16. **Chao, et al.** (2025). AdvBench数据集. [[bib.bib34]](评估数据集)

17. **Yi, et al.** (2024). 提示注入与上下文操纵. [[bib.bib7]](攻击技术背景)

### 攻击方法相关

18. **Liu, et al.** (2024). AutoDAN. *ICLR*. 生成隐蔽越狱提示 [[AutoDAN]](相关工作)

19. **Liu, et al.** (2024). AutoDAN-Turbo. 终身学习策略自探索代理. [[AutoDAN-Turbo]](相关工作)

20. **Russinovich, et al.** (2024). Crescendo Multi-Turn Jailbreak. *USENIX Security*. [[Crescendo]](相关工作)

21. **Mehrotra, et al.** (2024). Tree of Attacks. *NeurIPS*. [[TAP]](相关工作)

22. **Chao, et al.** (2023). PAIR: Jailbreaking Black Box LLMs in Twenty Queries. [[PAIR]](相关工作)

### 防御方法相关

23. **Mazeika, et al.** (2024). HarmBench. 自动化红队测试标准化评估框架. [[HarmBench]](评估框架)

24. **Mazeika, et al.** (2024). JailbreakBench. 越狱攻击开放鲁棒性基准. [[JailbreakBench]](评估基准)

25. **Rebedea, et al.** (2023). NeMo Guardrails. 可控制和安全的LLM应用工具包. [[NeMoGuardrails]](防御相关)

---

## 📊 论文总结

| 维度 | 评价 |
|------|------|
| **创新性** | ⭐⭐⭐⭐⭐ 首次系统研究LLM位置脆弱性，提出VSS量化指标 |
| **技术深度** | ⭐⭐⭐⭐⭐ 基于注意力机制的理论分析严密 |
| **实验完整性** | ⭐⭐⭐⭐ 多模型、多方法对比，覆盖防御场景 |
| **实用价值** | ⭐⭐⭐⭐⭐ 200ms开销极低，方法通用性强 |
| **安全意义** | ⭐⭐⭐⭐⭐ 揭示新的攻击面，推动安全研究 |

### 核心要点速记

1. **后缀不是最优位置**：50个有害提示中，**没有一个**的最优插入位置是后缀
2. **VSS稳定性**：脆弱槽位在优化全过程保持稳定 →位置选择是一次性的高效前置步骤
3. **注意力是关键**：VSS基于after-chat模板对对抗令牌的注意力权重设计
4. **14% ASR提升**：相对于标准GCG，SlotGCG在多个模型上平均提升14%攻击成功率
5. **42%防御鲁棒性**：在输入过滤防御下仍比基线高42% ASR
6. **200ms预处理**：VSS计算开销极低，实用性高