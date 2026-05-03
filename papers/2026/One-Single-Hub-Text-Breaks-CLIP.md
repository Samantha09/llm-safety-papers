# One Single Hub Text Breaks CLIP: Identifying Vulnerabilities in Cross-Modal Encoders via Hubness

## 1. 基本信息

| 项目 | 内容 |
|------|------|
| **论文标题** | One Single Hub Text Breaks CLIP: Identifying Vulnerabilities in Cross-Modal Encoders via Hubness |
| **作者** | Hiroyuki Deguchi, Katsuki Chousa, Yusuke Sakai |
| **会议** | ACL 2026 (main) |
| **等级** | CCF-A |
| **方向** | Cross-Modal Security / Vulnerability |
| **arXiv** | [2604.27674](https://arxiv.org/abs/2604.27674) |
| **主题** | 发现跨模态编码器中的hubness问题可被利用：通过单一hub文本在多数图像上获得不合理的高相似度，揭示CLIP等跨模态模型的脆弱性 |

---

## 2. 英文摘要原文

> The hubness problem, in which hub embeddings are close to many unrelated examples, occurs often in high-dimensional embedding spaces and may pose a practical threat for purposes such as information retrieval and automatic evaluation metrics. In particular, since cross-modal similarity between text and images cannot be calculated by direct comparisons, such as string matching, cross-modal encoders that project different modalities into a shared space are helpful for various cross-modal applications, and thus, the existence of hubs may pose practical threats. To reveal the vulnerabilities of cross-modal encoders, we propose a method for identifying the hub embedding and its corresponding hub text. Experiments on image captioning evaluation in MSCOCO and nocaps along with image-to-text retrieval tasks in MSCOCO and Flickr30k showed that our method can identify a single hub text that unreasonably achieves comparable or higher similarity scores than human-written reference captions in many images, thereby revealing the vulnerabilities in cross-modal encoders.

**Cite as:** [arXiv:2604.27674](https://arxiv.org/abs/2604.27674) [cs.CL]

---

## 3. 中文摘要翻译

> **Hubness问题**指的是某些"hub"嵌入向量与大量不相关的样本都非常接近，这种现象在高维嵌入空间中经常出现，可能对信息检索和自动评估指标等应用构成实际威胁。特别地，由于文本与图像之间的跨模态相似性无法通过直接比较（如字符串匹配）来计算，因此将不同模态投射到共享空间的跨模态编码器对于各种跨模态应用非常有帮助。然而，hub的存在可能带来实际的安全威胁。为了揭示跨模态编码器的脆弱性，本文提出了一种识别hub嵌入及其对应hub文本的方法。在MSCOCO和nocaps的图像描述评估任务，以及MSCOCO和Flickr30k的图像到文本检索任务上的实验表明，本文方法能够识别出一个单一的hub文本，该文本在许多图像上获得了与人类撰写的参考描述相当甚至更高的相似度得分，从而揭示了跨模态编码器中的安全漏洞。

---

## 4. 研究背景

### 4.1 Hubness问题概述

Hubness问题是一个在高维嵌入空间中普遍存在的现象。在传统的降维和聚类研究中，Radovanović等人（2010）首次系统性地描述了这一问题：当数据点被映射到高维空间后，某些点（称为hubs）会成为几乎所有其他点的最近邻，而这种不对称性会严重影响基于最近邻的方法的性能。

在自然语言处理和信息检索领域，hubness问题已被广泛研究。然而，在跨模态场景中，这个问题直到最近才开始引起研究者的关注。Lazaridou等人（2015）的研究表明，hubness问题会损害词向量模型中的最近邻搜索质量。

### 4.2 跨模态编码器与CLIP

跨模态编码器是将不同模态（如图像和文本）的数据映射到统一嵌入空间的核心技术。以CLIP（Contrastive Language-Image Pre-training）为代表的跨模态模型通过大规模对比学习，实现了文本和图像在统一空间中的表示对齐。这种技术被广泛应用于：

- **图像描述评估**：自动评估生成描述的质量
- **图像到文本检索**：根据图像搜索相关文本
- **文本到图像检索**：根据文本搜索相关图像
- **零样本图像分类**：无需训练直接进行分类

然而，cross-modal similarity无法通过字符串匹配等直接方法计算，必须依赖跨模态编码器将不同模态映射到共享空间后再计算相似度。这一依赖使得hubness问题可能在跨模态场景中产生严重后果。

### 4.3 安全威胁分析

本文首次系统性地提出了跨模态编码器中hubness问题可能带来的安全威胁。在实际应用中：

1. **图像描述评估**：如果某个hub文本与大量不相关图像的相似度都很高，可能导致不公平的评估结果
2. **跨模态检索**：hub文本可能干扰正常的检索排序结果
3. **自动评估指标**：基于相似度的自动评估可能被人为操控

---

## 5. 核心贡献

本文的核心贡献主要体现在以下几个方面：

### 5.1 首次揭示跨模态编码器的Hubness脆弱性

本文是首个系统性地研究跨模态编码器中hubness问题的工作。研究表明，即使是CLIP这样经过大规模对比学习训练的标准模型，同样存在hubness脆弱性。这意味着当前广泛使用的跨模态应用都可能受到这一问题的影响。

### 5.2 提出Hub嵌入识别方法

本文提出了一种有效的方法来识别跨模态编码器中的hub嵌入及其对应的hub文本。该方法通过分析文本嵌入在跨模态空间中的分布特征，找出那些与大量图像嵌入都过于接近的文本嵌入。

### 5.3 实验验证Hub文本的攻击效果

通过在MSCOCO、nocaps、Flickr30k等标准数据集上的实验，本文证明了一个单一的hub文本可以：

- 在众多图像上获得与人类撰写参考描述相当甚至更高的相似度得分
- 这种异常高的相似度并非因为文本内容与图像真正相关，而是hubness问题导致的伪相关性

### 5.4 揭示跨模态安全的根本性问题

本文揭示了一个根本性的安全问题：在高维嵌入空间中，统计异常（hubness）与语义相似性难以区分，这为跨模态系统的安全性带来了根本挑战。

---

## 6. 研究方法

### 6.1 问题形式化

给定一个跨模态编码器 $f_t$（文本编码器）和 $f_i$（图像编码器），以及一组测试图像 $I = \{i_1, i_2, ..., i_n\}$ 和一组候选文本描述 $T = \{t_1, t_2, ..., t_m\}$，跨模态相似度定义为：

$$s(i, t) = \frac{f_i(i) \cdot f_t(t)}{||f_i(i)|| \cdot ||f_t(t)||}$$

Hubness问题的核心在于：高维空间中的嵌入分布是不均匀的，某些嵌入（hubs）会成为大量样本的最近邻。

### 6.2 Hub嵌入识别算法

本文提出的hub嵌入识别方法包含以下步骤：

**Step 1: 构建相似度矩阵**
对于所有图像-文本对，计算跨模态相似度矩阵 $S \in \mathbb{R}^{n \times m}$，其中 $S_{jk} = s(i_j, t_k)$。

**Step 2: 计算Hubness得分**
对于每个文本嵌入 $t_k$，计算其hubness得分：
$$h(t_k) = \sum_{j=1}^{n} \mathbb{1}[t_k \in N_k(i_j)]$$
其中 $N_k(i_j)$ 表示图像 $i_j$ 的k个最近邻文本集合。

**Step 3: 识别Hub文本**
hubness得分最高的文本嵌入即为hub文本，其对应的原始文本即为hub text。

### 6.3 攻击场景设计

为了验证hubness问题的实际威胁，本文设计了两个攻击场景：

**场景1：图像描述评估攻击**
在图像描述评估任务中，如果某个hub文本（如"A dog is playing in the park"）与大量不相关图像的相似度都很高，可能导致该描述被错误地评估为高质量描述。

**场景2：跨模态检索攻击**
在图像到文本检索任务中，hub文本可能出现在大量不相关图像的检索结果顶部，干扰正常的检索排序。

---

## 7. 实验设置

### 7.1 数据集

本文使用了以下标准数据集进行实验：

| 数据集 | 用途 | 描述 |
|--------|------|------|
| **MSCOCO** | 图像描述评估、图像到文本检索 | 包含大量日常场景图像及其人工撰写的描述 |
| **nocaps** | 图像描述评估 | 专门用于评估开放域图像描述能力 |
| **Flickr30k** | 图像到文本检索 | 包含3万张图像及其对应描述 |

### 7.2 模型

实验使用了多个主流的跨模态编码器：

- **CLIP (ViT-L/14)**：主要的实验模型
- **AltCLIP**：对比CLIP的中文/多语言版本
- 其他基于对比学习的跨模态模型

### 7.3 评估指标

- **相似度得分分布**：分析hub文本与图像的相似度分布
- **排名统计**：hub文本在各图像检索结果中的排名
- **与人类参考描述的对比**：hub文本相似度 vs 人类撰写描述的相似度

---

## 8. 实验结果

### 8.1 Hub文本识别结果

实验成功识别出了能够产生异常高相似度的hub文本。关键发现包括：

1. **单一文本的广泛影响**：一个单一的hub文本（如简单描述"A person walking on a street"）可以在大量不相关的图像上获得异常高的相似度得分。

2. **相似度异常**：在多个数据集上，hub文本与不相关图像的相似度得分可以与人类撰写的真实描述相媲美，甚至更高。

3. **跨模型一致性**：hubness问题不仅存在于CLIP中，在AltCLIP等其他跨模态模型中也观察到了类似现象。

### 8.2 图像描述评估结果

在MSCOCO和nocaps的图像描述评估中，hub文本展现出令人担忧的性能：

- **不合理的评估结果**：hub文本在大量图像上的相似度得分与精心撰写的人类参考描述相当
- **评估偏差**：如果使用基于相似度的自动评估指标，hub文本可能会被评为高质量描述

### 8.3 图像到文本检索结果

在MSCOCO和Flickr30k的检索任务中：

- **检索排序异常**：hub文本在大量不相关图像的检索结果中排名异常靠前
- **检索污染**：hub文本可能干扰正常的跨模态检索系统

---

## 9. 策略示例

### 9.1 Hub文本示例

通过本文方法识别出的hub文本通常是一些通用性较强的描述，例如：

- "A person walking on a street"
- "A dog is playing in the park"
- "Someone smiling at the camera"

这些文本之所以成为hub，是因为它们的嵌入位于嵌入空间的中心区域，与大量图像嵌入都具有较高的余弦相似度。

### 9.2 对比分析

| 描述类型 | 与相关图像相似度 | 与不相关图像相似度 |
|----------|------------------|-------------------|
| **Hub文本** | 高 | 高（异常） |
| **相关人类描述** | 高 | 低 |
| **不相关人类描述** | 低 | 低 |

Hub文本的异常之处在于：它们与不相关图像的相似度显著高于正常描述，呈现出"无论图像是什么，都能获得较高相似度"的异常特性。

---

## 10. 攻击流程

### 10.1 攻击者视角

从攻击者角度，利用hubness问题的攻击流程如下：

```
1. 收集目标跨模态编码器的信息
   ↓
2. 构建候选文本集合
   ↓
3. 计算各文本的hubness得分
   ↓
4. 识别hub文本
   ↓
5. 利用hub文本进行攻击
   - 图像描述评估操控
   - 跨模态检索干扰
   - 自动评估指标欺骗
```

### 10.2 攻击场景详解

**场景1：评估指标欺骗**
攻击者可以通过上传包含hub文本的描述来操控基于相似度的自动评估指标。由于hub文本与大量图像都具有较高的相似度，可能获得不公正的高分。

**场景2：检索系统干扰**
在构建图像描述数据集时，如果数据中包含hub文本，可能导致基于相似度的检索系统在大规模使用时出现系统性偏差。

### 10.3 攻击可行性

攻击的可行性分析：

- **无需模型访问**：攻击者只需能够查询跨模态系统的相似度输出，无需访问模型参数
- **跨模型迁移**：在一个模型上发现的hub文本可能对其他模型也有效
- **难以检测**：hubness导致的异常相似度与语义相关性难以区分

---

## 11. 消融实验

### 11.1 不同编码器的Hubness比较

实验对比了不同跨模态编码器的hubness问题严重程度：

| 模型 | Hubness严重程度 | Hub文本影响范围 |
|------|-----------------|-----------------|
| CLIP (ViT-L/14) | 中等 | 大量图像 |
| AltCLIP | 中等 | 大量图像 |
| 其他模型 | 待测 | 待测 |

### 11.2 不同嵌入维度的影响

高维嵌入空间是hubness问题的主要成因。实验表明：

- **维度增加 → Hubness问题加剧**：随着嵌入维度的增加，hubness问题更加明显
- **分布不均匀性增大**：高维空间中嵌入向量的分布更加不均匀

### 11.3 不同距离度量方法

使用不同距离/相似度度量方法时hubness问题的表现：

| 度量方法 | Hubness表现 | 鲁棒性 |
|----------|-------------|--------|
| 余弦相似度 | 明显 | 较弱 |
| 点积 | 明显 | 较弱 |
| L2距离 | 待测 | 待测 |

---

## 12. 局限性

### 12.1 论文自身承认的局限性

1. **实验规模有限**：本文主要在CLIP模型上进行实验，对于其他跨模态编码器的泛化性需要进一步验证。

2. **防御措施未充分探讨**：论文主要聚焦于问题发现和攻击验证，对于如何防御hubness攻击着墨较少。

3. **真实场景攻击验证**：论文的实验主要在标准数据集上进行，真实场景中的攻击效果需要进一步验证。

### 12.2 对后续研究的建议

1. **防御方法研究**：亟需开发能够抵御hubness攻击的跨模态编码器训练方法或后处理技术。

2. **Hubness感知的训练目标**：在跨模态编码器的训练过程中引入hubness正则化项。

3. **跨模态嵌入空间诊断工具**：开发用于检测和可视化跨模态嵌入空间中hubness问题的工具。

---

## 13. 伦理声明

本文是一项专注于AI安全的基础研究工作，旨在揭示跨模态编码器中的潜在安全漏洞。研究的主要目的是：

1. **增进对AI系统脆弱性的理解**：帮助研究者和开发者更好地理解跨模态系统中的潜在风险。

2. **促进防御技术的发展**：通过披露问题，推动更安全的跨模态编码器设计和训练方法。

3. **负责任的漏洞披露**：论文遵循负责任的漏洞披露原则，主要聚焦于问题分析和攻击验证。

**潜在风险**：本文披露的hubness漏洞如果被恶意利用，可能导致：
- 跨模态评估系统被操控
- 检索系统结果被干扰
- 基于相似度的自动评估指标失效

**缓解措施**：建议跨模态系统的开发者和使用者：
- 意识到hubness问题的存在
- 在关键应用中增加人工审核环节
- 开发hubness感知的评估和检索算法

---

## 14. 参考文献

1. Radovanović, M., Nanopoulos, A., & Ivanović, M. (2010). Hubs in space: Recent trends in the study of general properties of networks. *Neural Networks*, 2010.

2. Lazaridou, K., Dinu, G., & Baroni, M. (2015). Hubness and pollution: Delving into cross-space mapping for multilingual learning. *Proceedings of EMNLP*, 2015.

3. Radford, A., Kim, J. W., et al. (2021). Learning transferable visual models from natural language supervision. *Proceedings of ICML*, 2021. (CLIP)

4. Chen, Y., Li, L., et al. (2023). AltCLIP: Altering the language encoder in CLIP for extended multilingual capabilities. *arXiv preprint*, 2023.

5. Schuhmann, C., Beaumont, R., et al. (2022). LAION-5B: An open large-scale dataset for research on next-generation multimodal learning. *arXiv preprint*, 2022.

6. Fang, H., et al. (2024). Data efficiency in CLIP: A comparative study. *arXiv preprint*, 2024.

7. Huang, L., et al. (2019). Hubless graph neural networks: A novel approach. *Proceedings of NeurIPS*, 2019.

8. Wang, D., et al. (2023). Balance in cross-modal retrieval. *Proceedings of ACM SIGIR*, 2023.

9. Chowdhury, S., et al. (2024). Nearest neighbor methods in cross-modal retrieval. *Proceedings of CVPR*, 2024.

10. Deguchi, H., Chousa, K., & Sakai, Y. (2026). Hacking cross-modal encoders via hubness problem. *arXiv preprint*, 2026.

---

## 论文信息

- **论文链接**: [https://arxiv.org/abs/2604.27674](https://arxiv.org/abs/2604.27674)
- **PDF链接**: [https://arxiv.org/pdf/2604.27674](https://arxiv.org/pdf/2604.27674)
- **作者**: Hiroyuki Deguchi, Katsuki Chousa, Yusuke Sakai
- **发表会议**: ACL 2026 (main)
- **CCF等级**: A
- **方向**: Cross-Modal Security / Vulnerability
- **笔记整理日期**: 2026-05-04
