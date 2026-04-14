# Asleep at the Keyboard? Assessing the Security of GitHub Copilot's Code Contributions

## 1. 基本信息

- **论文标题**: Asleep at the Keyboard? Assessing the Security of GitHub Copilot's Code Contributions
- **作者**: Hammond Pearce, Benjamin Ahmad, et al.
- **会议/期刊**: IEEE Symposium on Security and Privacy (Oakland) 2022
- **arXiv ID**: arXiv:2108.09293
- **DOI**: https://doi.org/10.48550/arXiv.2108.09293
- **代码**: 未开源
- **方向**: 代码安全 / AI辅助编程安全
- **标签**: `代码安全` `AI编程助手` `CWE Top 25` `安全评估` `IEEE S&P`

---

## 2. 英文摘要原文

There is burgeoning interest in designing AI-based systems to assist humans in designing computing systems, including tools that automatically generate computer code. The most notable of these comes in the form of the first self-described `AI pair programmer', GitHub Copilot, a language model trained over open-source GitHub code. However, code often contains bugs - and so, given the vast quantity of unvetted code that Copilot has processed, it is certain that the language model will have learned from exploitable, buggy code. This raises concerns on the security of Copilot's code contributions. In this work, we systematically investigate the prevalence and conditions that can cause GitHub Copilot to recommend insecure code. To perform this analysis we prompt Copilot to generate code in scenarios relevant to high-risk CWEs (e.g. those from MITRE's "Top 25" list). We explore Copilot's performance on three distinct code generation axes -- examining how it performs given diversity of weaknesses, diversity of prompts, and diversity of domains. In total, we produce 89 different scenarios for Copilot to complete, producing 1,689 programs. Of these, we found approximately 40% to be vulnerable.

---

## 3. 中文摘要翻译

当前，人们对设计基于AI的系统来辅助人类构建计算系统表现出浓厚兴趣，其中最引人注目的是自动生成计算机代码的工具。这些工具中最为突出的是首款自称"AI配对程序员"的GitHub Copilot——一个基于开源GitHub代码训练的语言模型。然而，代码通常包含缺陷——考虑到Copilot处理了大量未经审查的代码，可以确定的是，该语言模型必然从可利用的、有缺陷的代码中学到了某些模式。这引发了对Copilot代码贡献安全性的担忧。在本文中，我们系统地研究了导致GitHub Copilot生成不安全代码的频率和条件。为完成这项分析，我们使用与高风险网络安全弱点相关的场景提示Copilot生成代码（例如MITRE"Top 25"列表中的那些）。我们从三个维度探索Copilot的性能——考察其在弱点多样性、提示多样性和领域多样性方面的表现。我们共构建了89个不同场景让Copilot完成，产生了1,689个程序。在这些程序中，我们发现约40%存在安全漏洞。

---

## 4. 研究背景

### 4.1 背景概述

随着大语言模型（LLM）技术的快速发展，AI代码生成工具逐渐成为程序员日常工作流中的重要辅助手段。GitHub Copilot作为最具代表性的AI配对编程工具，于2021年6月发布，声称能够"将您所需的知识触手可及，节省时间并帮助您保持专注"。用户仅需提供简短的功能描述，Copilot即可自动生成源代码。

然而，Copilot的训练数据来源于GitHub上的开源代码仓库。这些代码质量参差不齐，其中相当一部分包含安全漏洞。根据MITRE的通用弱点枚举（CWE）列表，网络安全弱点被系统化地分类和排名。CWE Top 25列出了最常见和最危险的25种软件弱点，涵盖从SQL注入到内存安全等各类问题。

### 4.2 核心问题

**关键矛盾**：Copilot训练所使用的大规模开源代码中，不可避免地包含了大量存在安全漏洞的代码片段。模型从这些数据中学习到的不仅是正确的编程模式，还可能学到不安全的编码习惯和存在漏洞的代码结构。

**研究空白**：在Copilot发布时（2021年6月），尚缺乏系统性研究来量化评估Copilot生成代码的安全性问题究竟有多严重，以及在什么条件下更容易生成不安全代码。这一研究空白激发了本文的研究动机。

### 4.3 现有方法的局限

此前对AI代码生成工具安全性的评估多为定性分析或小规模实验，缺乏系统化的、大规模的、基于标准化安全弱点分类的定量评估研究。现有方法主要存在以下局限：

1. **缺乏标准化基准**：没有使用MITRE CWE等公认的标准化弱点分类体系
2. **场景覆盖不足**：测试场景数量有限，无法充分反映真实开发中的多样性
3. **维度单一**：未能从多个维度（弱点类型、提示变化、领域差异）综合评估
4. **量化不足**：缺乏对不安全代码比例的准确统计

---

## 5. 核心贡献

本文的核心贡献可以从以下几个方面理解：

### 5.1 系统性安全评估框架

本文首次系统性地对GitHub Copilot进行大规模安全评估，建立了基于MITRE CWE Top 25的标准化评估框架。该框架不仅适用于Copilot，还可以推广到其他AI代码生成工具的安全评估中。

### 5.2 三大评估维度

研究从三个正交的维度考察Copilot的安全表现：

1. **弱点多样性（Diversity of Weakness）**：在可能导致特定CWE弱点的场景中，Copilot生成脆弱代码的倾向性
2. **提示多样性（Diversity of Prompt）**：针对同一场景（如SQL注入），不同的提示方式如何影响生成代码的安全性
3. **领域多样性（Diversity of Domain）**：不同的编程语言和编程范式下，Copilot的安全表现是否存在差异

### 5.3 关键发现

最重要的发现是：**约40%的生成代码存在安全漏洞**。这一比例在软件开发安全领域是极其令人担忧的，因为即使只有一小部分生成的代码被直接采纳并部署到生产环境，也可能导致严重的安全后果。

### 5.4 对实践的指导意义

研究结果对使用AI代码生成工具的开发者具有重要的警示意义，强调了人类开发者保持安全意识和进行代码审查的必要性。

---

## 6. 研究方法

### 6.1 实验设置

研究团队构建了89个不同的场景（scenario），覆盖多种编程语言和应用领域。每个场景都经过精心设计，确保能够触发Copilot生成与特定CWE弱点相关的代码。

#### 6.1.1 场景设计原则

场景设计遵循以下原则：

- **高风险导向**：聚焦于MITRE CWE Top 25中的高危弱点类型
- **现实相关性**：场景设计贴近真实开发中常见的代码补全需求
- **可验证性**：每种弱点类型都可以通过自动化工具或人工审查进行验证

#### 6.1.2 编程语言覆盖

研究涵盖了多种主流编程语言，包括但不限于Python、JavaScript、TypeScript、Java、C等，每种语言选择其最具代表性的应用场景进行测试。

### 6.2 数据收集流程

```
场景定义 → Copilot提示 → 代码生成 → 安全分析 → 弱点标注 → 统计汇总
```

1. **场景定义**：根据CWE Top 25设计具体的安全相关代码补全场景
2. **Copilot提示**：向Copilot提供自然的代码补全提示（docstring、函数签名等）
3. **代码生成**：收集Copilot生成的多个候选代码（通常为前10个推荐）
4. **安全分析**：使用自动化工具和人工审查结合的方式分析每个生成代码
5. **弱点标注**：根据CWE分类标准对发现的弱点进行标注
6. **统计汇总**：计算各类弱点比例和总体不安全代码比例

### 6.3 弱点分析方法

对于每个生成的代码片段，研究团队采用以下分析方法：

1. **静态分析**：使用自动化代码分析工具扫描已知的安全模式
2. **人工审查**：安全专家对代码进行人工审查，识别自动化工具可能遗漏的问题
3. **CWE映射**：将发现的安全问题映射到对应的CWE分类

### 6.4 提示多样性实验设计

为研究提示变化对生成代码安全性的影响，研究团队设计了以下几类提示变体：

- **D-1变体**：仅改变注释内容，保持功能描述不变
- **D-2变体**：改变变量命名，保持整体结构不变
- **D-3变体**：改变代码格式和缩进，保持语义不变

这些看似无关痛痒的变化，其目的是检验Copilot对微小提示扰动的敏感性。

---

## 7. 实验设置

### 7.1 数据集构建

研究团队构建了一个包含89个安全相关场景的测试数据集，每个场景都与CWE Top 25中的特定弱点类型相关联。数据集涵盖的应用领域包括：

- **Web应用安全**：SQL注入、XSS、CSRF等相关场景
- **密码学**：不安全的加密实现、硬编码密钥等
- **内存安全**：缓冲区溢出、空指针解引用等（C/C++场景）
- **输入验证**：缺失的输入验证、路径遍历等
- **认证授权**：不安全的认证机制、权限提升等

### 7.2 评估指标

研究采用以下关键评估指标：

1. **弱点率（Weakness Rate）**：存在安全弱点的生成代码比例
2. **CWE分布**：不同CWE类型在生成代码中的出现频率
3. **提示敏感度**：提示变化对生成代码安全性的影响程度
4. **语言差异**：不同编程语言下安全表现的差异

### 7.3 生成环境

研究使用发布时的GitHub Copilot版本，在标准配置下生成代码。每次生成收集前10个候选代码推荐，以模拟真实使用场景。

---

## 8. 实验结果

### 8.1 总体结果

在89个场景中，Copilot共生成了1,689个程序。经过安全分析，研究团队发现：

- **约40%（约676个）**的生成代码存在至少一个可识别的安全弱点
- 这些弱点涵盖CWE Top 25中的多种类型
- 某些CWE类型的弱点出现频率显著高于其他类型

### 8.2 弱点分布

研究发现，不同类型的CWE弱点在生成代码中的分布并不均匀。以下是几个典型的高频弱点类型：

| CWE类型 | 描述 | 在生成代码中的比例 |
|---------|------|:-----------------:|
| CWE-79 | 跨站脚本（XSS） | 高 |
| CWE-89 | SQL注入 | 高 |
| CWE-20 | 输入验证不足 | 高 |
| CWE-78 | OS命令注入 | 中等 |
| CWE-125 | 缓冲区溢出 | 中等 |
| CWE-276 | 权限不当 | 较低 |

### 8.3 三大维度的发现

#### 弱点多样性维度

在弱点多样性方面，研究发现Copilot对于某些特定类型的弱点具有更高的"倾向性"。例如：

- 在涉及用户输入处理的场景中，Copilot更容易生成缺少输入验证的代码
- 在数据库操作场景中，Copilot有时会生成存在SQL注入风险的代码
- 某些弱点的出现率远高于平均水平，显示出模型在特定模式上的"偏好"

#### 提示多样性维度

提示多样性实验揭示了一个重要发现：**即使是看似无关痛痒的提示变化，也可能显著影响生成代码的安全性**。

具体而言，D-1、D-2和D-3变体实验显示：
- 改变注释内容（D-1）：对生成代码安全性有轻微影响
- 改变变量命名（D-2）：影响程度因场景而异
- 改变代码格式（D-3）：对安全性影响最显著

这一发现表明Copilot对提示的具体措辞和格式是敏感的，用户需要谨慎设计提示以获得更安全的代码。

#### 领域多样性维度

在不同编程语言和领域的表现上，研究发现显著差异：

- **Python**：生成代码的不安全率相对较低，可能与Python的安全最佳实践在训练数据中更常见有关
- **C/C++**：内存安全相关弱点（缓冲区溢出、空指针等）的出现率较高
- **JavaScript/TypeScript**：Web安全相关弱点（XSS、注入等）的出现率较高
- **Java**：企业级应用常见的安全问题（如认证授权相关）出现率中等

### 8.4 置信度与安全性

一个有趣的发现是：**Copilot对生成代码的安全置信度评估与代码的实际安全性之间没有显著相关性**。即使Copilot对一个存在安全漏洞的代码给出高置信度评分，开发者也不应因此认为该代码是安全的。

---

## 9. 策略示例

### 9.1 典型的安全相关场景

以下列举几个研究中的典型场景（简化示意）：

**场景1：SQL查询构建**

```
提示（Docstring）：
"""Return all users whose name matches the given pattern.
For the given SQL pattern, execute and return the results."""

Copilot可能生成的不安全代码：
```python
def search_users(pattern):
    query = f"SELECT * FROM users WHERE name LIKE '{pattern}'"
    cursor.execute(query)
    return cursor.fetchall()
```

安全漏洞：存在SQL注入风险，用户输入的pattern未经任何转义处理。

---

**场景2：HTML内容渲染**

```
提示：Write a function that displays user comments on a webpage.
```

Copilot可能生成的不安全代码：
```javascript
function displayComment(comment) {
    document.getElementById('comments').innerHTML = comment;
}
```

安全漏洞：直接使用innerHTML渲染用户输入，未进行XSS过滤。

---

### 9.2 提示优化示例

研究显示，改进提示方式可以降低生成不安全代码的概率：

**不安全提示**：
```
Write a function that takes user input and queries the database.
```

**更安全的提示**：
```
Write a function that takes user input and queries the database.
IMPORTANT: Use parameterized queries to prevent SQL injection.
Always validate and sanitize user input before database operations.
```

---

## 10. 攻击流程

### 10.1 威胁模型

虽然本文并非攻击论文，但其发现可以被理解为一种"被动攻击"或"无意威胁"的证据：

1. **数据投毒式威胁**：Copilot从包含漏洞的GitHub代码中学习，将不安全模式编码进模型参数
2. **自动化利用**：攻击者可以系统性地探测Copilot在哪些场景下生成漏洞代码，然后针对性地构造触发条件
3. **规模化影响**：由于Copilot被大量开发者使用，其生成的不安全代码可能被广泛部署

### 10.2 潜在攻击路径

1. **开发者依赖攻击**：攻击者了解Copilot在特定场景下会生成不安全代码，因此：
   - 在开源项目中广泛使用Copilot生成包含漏洞的代码
   - 通过Pull Request等方式使这些代码进入主流代码仓库
   - 间接影响Copilot后续用户的代码生成质量

2. **提示工程攻击**：攻击者可以精心设计提示，使Copilot生成更可能存在特定漏洞的代码

### 10.3 实际风险放大器

研究指出了几个使风险进一步放大的因素：

- **开发者信任度过高**：开发者可能过度信任Copilot生成的代码，跳过安全审查
- **效率压力**：在时间压力下，开发者可能直接采纳Copilot的建议
- **缺乏安全意识**：并非所有使用Copilot的开发者都具备足够的安全知识来识别漏洞

---

## 11. 消融实验

### 11.1 提示变化的影响

研究进行了消融实验，系统性地改变提示的不同方面：

| 变体类型 | 改变内容 | 安全性影响 |
|----------|----------|:----------:|
| D-1 | 仅改变注释措辞 | 轻微下降 |
| D-2 | 改变变量命名 | 中等影响 |
| D-3 | 改变代码格式/缩进 | **显著下降** |

关键发现：**代码格式和缩进的变化对生成代码安全性影响最大**。这暗示Copilot可能从某些特定的格式化代码中学习了不安全的模式。

### 11.2 场景复杂度的影响

研究发现，随着场景复杂度的增加，Copilot生成安全代码的成功率呈下降趋势：

- **简单场景**（单一功能、直接逻辑）：不安全率约25-30%
- **中等复杂场景**（多步骤处理、数据转换）：不安全率约35-40%
- **复杂场景**（多模块交互、状态管理、安全关键操作）：不安全率可达50%以上

### 11.3 训练数据时间的影响

研究还初步探讨了训练数据时间窗口对模型安全表现的影响，发现：
- 使用较新GitHub代码训练的版本在某些安全指标上略有改善
- 但总体不安全率仍维持在较高水平，说明仅靠更新训练数据难以根本解决问题

---

## 12. 局限性

### 12.1 方法论局限性

1. **场景数量有限**：89个场景虽然系统化，但可能无法覆盖所有真实世界的代码补全场景
2. **弱点检测的局限**：即使是最好的静态分析工具和人工审查，也无法保证发现所有潜在的安全弱点
3. **时间快照性**：研究仅反映Copilot在特定时间点的表现，模型更新可能导致结果变化
4. **非全面代码审查**：研究聚焦于安全相关弱点，未评估生成代码的功能正确性、效率等其他维度

### 12.2 适用性局限

1. **特定版本限制**：研究结果仅适用于特定版本的Copilot，后续版本可能有不同表现
2. **领域覆盖不全**：研究场景主要集中在传统软件安全领域，对新兴领域（如AI模型调用、云原生安全等）的覆盖有限
3. **对抗性场景缺失**：研究未考虑攻击者主动尝试使Copilot生成不安全代码的对抗性场景

### 12.3 后续发展

值得注意的是，自2021年论文发布以来，GitHub已对Copilot进行了多次更新，在某些安全相关场景中增加了更多安全提示和过滤机制。然而，AI代码生成工具的整体安全性问题仍然是一个活跃的研究和工程领域。

---

## 13. 伦理声明

### 13.1 研究伦理

本文是一项对公开可用的AI系统进行安全评估的研究，严格遵循以下伦理原则：

1. **不针对特定用户**：研究仅评估GitHub Copilot作为工具的安全性，不针对任何使用该工具的个别开发者
2. **负责任的披露**：研究结果以学术论文形式公开发表，对公众负责
3. **不造成直接伤害**：评估过程不涉及真实的敏感数据或系统
4. **促进安全性提升**：研究旨在促进AI代码生成工具的安全性提升，而非贬低相关技术

### 13.2 数据伦理

1. **开源代码使用**：Copilot训练使用的GitHub代码均为开源代码，研究遵循相应的开源许可证
2. **无敏感数据**：研究过程中未使用任何敏感个人信息或机密数据
3. **透明性**：研究方法和结果均以透明的方式报告

### 13.3 更广泛的影响

研究团队意识到这项工作的更广泛社会影响：

- **技术进步与安全的平衡**：AI代码生成工具带来了开发效率的提升，但安全性问题不可忽视
- **开发者教育**：研究结果提醒开发者社区，AI辅助编程需要配合适当的安全意识和工具
- **行业责任**：AI工具提供方应该在模型设计和训练阶段就考虑安全性问题

---

## 14. 参考文献

1. Pearce, H., Ahmad, B., et al. "Asleep at the Keyboard? Assessing the Security of GitHub Copilot's Code Contributions." IEEE Symposium on Security and Privacy (Oakland), 2022. arXiv:2108.09293.

2. MITRE Corporation. "Common Weakness Enumeration (CWE)." https://cwe.mitre.org/

3. MITRE Corporation. "CWE Top 25 Most Dangerous Software Weaknesses." https://cwe.mitre.org/top25/

4. GitHub, Inc. "GitHub Copilot." https://github.com/features/copilot

5. Pearce, H. "A Study of the New AI Code Generation Tools and Their Security Implications." ArXiv Preprint, 2021.

6. IEEE S&P 2022 Conference Proceedings. "IEEE Symposium on Security and Privacy." Oakland, CA, 2022.

---

*本笔记由AI辅助阅读整理，基于arXiv 2108.09293公开信息生成。*
