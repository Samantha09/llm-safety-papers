# StructMem: Structured Memory for Long-Horizon Behavior in LLMs

## 1. 基本信息

- **论文标题**: StructMem: Structured Memory for Long-Horizon Behavior in LLMs
- **作者**: Buqiang Xu, Yijun Chen, Jizhan Fang, Ruobin Zhong, Yunzhi Yao, Yuqi Zhu, Lun Du, Shumin Deng
- **单位**: Zhejiang University, Ant Group, Zhejiang University - Ant Group Joint Laboratory of Knowledge Graph
- **会议/期刊**: ACL 2026 main conference
- **arXiv ID**: 2604.21748
- **GitHub**: https://github.com/zjunlp/LightMem
- **代码是否开源**: 已开源
- **方向**: Memory / Agent
- **级别**: CCF-A

## 2. 英文摘要原文

Long-term conversational agents need memory systems that capture relationships between events, not merely isolated facts, to support temporal reasoning and multi-hop question answering. Current approaches face a fundamental trade-off: flat memory is efficient but fails to model relational structure, while graph-based memory enables structured reasoning at the cost of expensive and fragile construction. To address these issues, we propose **StructMem**, a structure-enriched hierarchical memory framework that preserves event-level bindings and induces cross-event connections. By temporally anchoring dual perspectives and performing periodic semantic consolidation, StructMem improves temporal reasoning and multi-hop performance on **LoCoMo**, while substantially reducing token usage, API calls, and runtime compared to prior memory systems.

## 3. 中文摘要翻译

长期对话智能体需要能够捕捉事件之间关系的记忆系统，而不仅仅是孤立的事实，以支持时间推理和多跳问答。当前的记忆系统方法面临一个根本性的权衡：一方面，扁平记忆（flat memory）效率高但无法建模关系结构；另一方面，基于图谱的记忆（graph-based memory）虽然支持结构化推理，但代价高昂且构建过程脆弱。为了解决这些问题，我们提出了**StructMem**，一种结构化层次记忆框架，通过保留事件级绑定和诱导跨事件连接来增强记忆系统的结构化程度。StructMem通过时间锚定的双视角提取和周期性语义整合，在LoCoMo基准上提升了时间推理和多跳问答性能，同时相比现有记忆系统大幅减少了token使用量、API调用次数和运行时间。

## 4. 研究背景

### 4.1 长期记忆对Agent的重要性

长期记忆是语言模型智能体（Language Model Agents）维持跨长时间跨度交互的一致性并进行推理的认知基础。在长时程对话场景中，智能体需要具备以下能力：

- **时间依赖推理**（Temporal Dependencies）：理解事件发生的先后顺序和因果链条
- **跨轮次关系建模**（Cross-turn Relationships）：捕捉多轮对话中事件之间的关联
- **多跳问答能力**（Multi-hop Question Answering）：基于多个相关记忆片段进行推理回答

### 4.2 现有记忆系统的两大范式及其局限

现有的记忆系统主要分为两大范式，各有其固有局限：

#### 扁平记忆系统（Flat Memory Systems）

这类系统将对话历史存储为扁平的向量数据库，代表性工作包括：
- ChatDB
- MemoryBank
- MemGPT

**局限性**：
- 将交互历史视为无序的命题集合，割裂了时间进程
- 无法保留因果依赖和关系性上下文
- 导致碎片化检索，孤立的事实被返回而缺乏复杂推理所需的上下文支架
- 存在"中间迷失"（Lost-in-the-Middle）问题，在超长序列中注意力机制退化
- 最终将多跳推理简化为对断开连接的事实进行浅层相似度搜索

#### 图谱记忆系统（Graph-based Memory Systems）

这类系统通过实体-关系三元组提取来恢复关系结构，代表性工作包括：
- GraphRAG
- HippoRAG
- Mem0g
- Zep

**局限性**：
- 构建成本高昂，需要级联推理
- 从嘈杂提取中进行实体消解和关系抽取时存在错误累积问题
- 将流畅的对话叙事压缩为刚性的实体-关系三元组会造成语义损失
- 连续图谱维护带来显著的延迟挑战

### 4.3 核心问题

论文指出现有方法的根本问题在于**记忆单元（Memory Unit）选择不当**：
- 孤立的事实不足以作为对话记忆的基本单元
- 刚性的三元组需要复杂的schema设计和实体消解
- 对话记忆的基本单元应该是**时间锚定的关系性事件**（temporally grounded relational event）

## 5. 核心贡献

论文提出了StructMem框架，其核心贡献包括：

### 5.1 结构化层次记忆框架

StructMem是一个层次化记忆框架，通过层级设计实现结构化组织，包含两个关键层次：
- **事件级绑定**（Event-Level Binding）：保留单个话语内的事实内容和关系上下文之间的绑定
- **跨事件连接**（Cross-Event Connections）：跨时间边界连接信息

### 5.2 双视角提取机制

论文提出了**双视角提取**（Dual-Perspective Extraction）方法，对每个话语提取：
- **事实视角**（Factual Perspective）：描述事件内容的事实性条目
- **关系视角**（Relational Perspective）：捕捉人际动态、因果影响和时间依赖

### 5.3 时间锚定与周期整合

- 通过时间锚定保留事实-关系事件的完整上下文
- 利用时间局部性（temporal locality）进行周期性语义整合，高效诱导高层关系结构

### 5.4 开源实现

- 提供完整开源代码：https://github.com/zjunlp/LightMem

## 6. 研究方法

### 6.1 整体框架

StructMem的层次记忆组织包含两个核心组件：

```
┌─────────────────────────────────────────────────────────────┐
│                    StructMem Framework                      │
├─────────────────────────────────────────────────────────────┤
│  Event-Level Structure (§3.1)                               │
│  ┌─────────────────────────────────────────────────────┐  │
│  │ Dual-Perspective Extraction                         │  │
│  │ • Factual entries (Φᵢ) - event content              │  │
│  │ • Relational entries (Ψᵢ) - interpersonal context  │  │
│  │ Temporal Anchoring: bind entries to timestamp τᵢ   │  │
│  └─────────────────────────────────────────────────────┘  │
├─────────────────────────────────────────────────────────────┤
│  Cross-Event Structure (§3.2)                               │
│  ┌─────────────────────────────────────────────────────┐  │
│  │ Periodic Consolidation                             │  │
│  │ • Semantic event connections via similarity       │  │
│  │ • Event reconstruction from timestamps             │  │
│  │ • Consolidation synthesis to higher-level events   │  │
│  └─────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### 6.2 事件级绑定（Event-Level Binding）

#### 双视角提取

对于对话流中的每个话语mᵢ，使用语言模型L和提示Pf act和Prel进行双视角提取：

$$\Phi_i \cup \Psi_i = \mathcal{L}(P_{fact} \| m_i) \cup \mathcal{L}(P_{rel} \| m_i)$$

其中：
- **Φᵢ = {cᵢ,₁, ..., cᵢ,ⱼ}** 包含事实性条目，描述事件内容
- **Ψᵢ = {rᵢ,₁, ..., rᵢ,ₖ}** 包含关系性条目，捕捉人际动态、因果影响和时间依赖

通过使用自然语言而非刚性三元组来表示两种视角，保留了情景化细微差别，同时避免了实体消解的开销。

#### 时间锚定

为了保留关系信息和事实信息之间的绑定，所有条目都锚定在其原始时间戳τᵢ上，形成事件级单元：

$$\mathcal{M} \leftarrow \bigcup_{i=1}^{N} \left\{ \langle x, \mathbf{e}_x, \tau_i \rangle \mid x \in \Phi_i \cup \Psi_i \right\}$$

其中**eₓ**表示条目x的嵌入。这种时间耦合使得在检索期间可以重建完整的事实-关系事件。

### 6.3 跨事件整合（Cross-Event Consolidation）

跨事件整合通过周期性综合语义相关事件来跨时间边界连接信息。当累积事件超过时间阈值时触发综合。

#### 语义事件连接

1. **缓冲未整合条目**：将上次整合以来的未缓冲条目缓冲，按时间排序：
   
$$\mathcal{C}_{buf} = Sort_\tau \{ x \in \mathcal{M}_{buffer} \}$$

2. **聚合查询编码**：将缓冲条目文本连接后编码为聚合查询

3. **语义相似度检索**：对所有历史条目按余弦相似度排名，检索top-K最相似的条目作为种子

#### 事件重建

对于每个种子条目x* ∈ Sₖ，通过检索所有共享同一时间戳的条目来重建其完整事件上下文：

$$E_\tau(x^*) = \{ x' \in \mathcal{M} \mid \tau(x') = \tau(x^*) \}$$

重建的事件与缓冲事件一起形成基于语义相关性的跨事件结构：

$$\mathcal{C}_{cross} = \mathcal{C}_{buf} \cup \bigcup_{x^* \in \mathcal{S}_k} E_\tau(x^*)$$

#### 通过综合进行记忆整合

与对顺序文本进行有损压缩的传统摘要不同，StructMem的整合机制在语义重建的事件簇上操作。它明确综合跨事件关系假设，形成互补的抽象层，在支持多跳推理的同时忠实地保留原始情景记忆的保真度：

$$\mathcal{M} \leftarrow \mathcal{C}_{cons} = \mathcal{L}(P_{cons} \| \mathcal{C}_{cross})$$

## 7. 实验设置

### 7.1 数据集

实验在**LoCoMo（Long-term Conversation Memory）基准**上进行。LoCoMo是专门评估长期对话记忆的标准 benchmark，包含多种类型的任务：
- 多域问答（Multi-domain QA）
- 开放域问答（Open-domain QA）
- 单会话问答（Single-session QA）
- 时间推理（Temporal reasoning）
- 流入/流出问答（In/Out flow QA）

### 7.2 评估指标

#### 有效性指标（Effectiveness）
- 使用**LLM-as-a-Judge**评估，通过语言模型判断回答质量

#### 效率指标（Efficiency）
- Token使用量
- API调用次数
- 运行时间（内存构建阶段）

### 7.3 基线系统

论文将StructMem与三类基线系统进行对比：

| 类别 | 基线系统 | 说明 |
|------|----------|------|
| **RAG系统** | OpenAI, FullContext, MiniRAG, LightRAG | 基于检索增强生成的系统 |
| **扁平记忆方法** | LangMem, A-Mem, Mem0 | 将记忆存储为独立单元的系统 |
| **结构记忆方法** | MemoryOS, Mem0g, Zep, Memobase | 包含关系结构的记忆系统 |

所有方法均使用**gpt-4o-mini**作为骨干模型，使用**text-embedding-3-small**进行嵌入。

### 7.4 配置细节

- 检索条目数：实验中详细测试了不同检索条目数对性能的影响
- 语义检索种子数K：测试了K值从0到不同设置的影响
- 所有提示模板和实现细节详见附录A.7

## 8. 实验结果

### 8.1 总体性能比较

根据Table 1的结果，StructMem在LoCoMo数据集上实现了最先进的总体性能：

| 方法 | 总体性能 | 多域 | 开放 | 单会话 | 时间 | 流入 | 流出 |
|------|----------|------|------|--------|------|------|------|
| OpenAI | 71.82 | 69.86 | 53.12 | 84.66 | 45.48 | - | - |
| FullContext | 73.83 | 68.79 | 56.25 | 86.56 | 50.16 | - | - |
| MiniRAG | 63.51 | 56.74 | 58.33 | 75.74 | 38.94 | 9.022 | 10.103 |
| LightRAG | 68.83 | 66.31 | 50.00 | 77.53 | 53.89 | 10.014 | 11.931 |
| LangMem | 58.10 | 62.23 | 47.92 | 71.12 | 23.43 | 9.873 | 11.066 |
| Mem0 | 66.88 | 67.13 | 51.15 | 72.93 | 59.19 | 10.958 | 12.196 |
| MemoryOS | 58.25 | 56.74 | 45.83 | 67.06 | 40.19 | 1.889 | 2.868 |
| Mem0g | 68.44 | 65.71 | 47.19 | 75.71 | 58.13 | 33.512 | 35.825 |
| Zep | 75.14 | 74.11 | 66.04 | 79.79 | 67.71 | - | - |
| Memobase | 75.78 | 70.92 | 46.88 | 77.17 | 85.05 | - | - |
| **StructMem** | **76.82** | **68.77** | **46.88** | **81.09** | **81.62** | **1.501** | **0.436** |

**关键发现**：
- StructMem在总体性能上达到最佳（76.82）
- 在时间推理任务上表现突出（81.62），仅次于Memobase（85.05）
- 在多域和单会话任务上表现优异
- 效率指标显著优于所有基线系统

### 8.2 效率比较

| 方法 | Token消耗(M) | API调用 | 时间(s) |
|------|--------------|---------|---------|
| MiniRAG | 9.022 | 1,081 | 10.103 |
| LightRAG | 10.014 | 1,916 | 11.931 |
| LangMem | 9.873 | 1,192 | 11.066 |
| Mem0 | 10.958 | 1,239 | 12.196 |
| MemoryOS | 1.889 | 939 | 2.868 |
| Mem0g | 33.512 | 2,313 | 35.825 |
| **StructMem** | **1.501** | **436** | **1.937** |

**关键发现**：
- StructMem的Token消耗最低（1.501M），仅为最接近基线的约80%
- API调用次数最少（436次），大幅低于其他系统
- 运行时间最短（1.937秒）

### 8.3 范式比较与消融研究

根据Table 2的消融实验结果：

| 配置 | 多域 | 开放 | 单会话 | 时间 | 流入 | 流出 |
|------|------|------|--------|------|------|------|
| Flat Memory (基线) | - | - | - | - | - | - |
| + Graph Memory | ↓ | ↑ | ↑ | ↓ | - | - |
| + Event-level structure | ↑ | - | ↑ | ↑ | - | - |
| + Cross-event structure | ↑ | ↑ | ↑ | ↑ | - | - |
| **Full StructMem** | **↑↑** | **↑** | **↑↑** | **↑↑** | **↑↑** | **↑↑** |

**关键发现**：
- Graph Memory在单会话和开放域任务上有改进，但在时间推理上下降
- Event-level structure提升了时间推理和单会话任务性能
- Cross-event structure带来进一步提升，捕捉跨时间因果关系
- 完整StructMem在所有任务类型上实现一致改进

## 9. 策略示例

### 9.1 双视角提取示例

对于对话话语"I can't believe Sarah actually agreed to present at the conference after all that drama last month."

**事实视角提取（Φᵢ）**：
- "Sarah agreed to present at the conference"
- "The agreement happened after some drama"

**关系视角提取（Ψᵢ）**：
- "Speaker expresses surprise about Sarah's decision"
- "There was drama involving Sarah last month"
- "Sarah's agreement is seen as unexpected"

### 9.2 跨事件整合示例

当用户问："What was that situation with Sarah about?"时：

1. **检索阶段**：通过语义相似度找到相关种子事件
2. **重建阶段**：检索同一时间戳下的所有事件
3. **综合阶段**：生成跨事件关系假设，连接多个情景记忆

最终生成的回答能够整合多个时间点的事件，提供连贯的因果解释，而非孤立的碎片事实。

## 10. 攻击流程

本文不是一篇关于攻击的论文，而是一篇关于**防御/改进**的论文，提出StructMem作为记忆系统的改进框架。论文主要关注：

### 10.1 针对现有记忆系统的"攻击"角度

论文隐式分析了现有记忆系统的失效模式：

1. **扁平记忆的失效**：当需要多跳推理时，检索到的孤立事实缺乏上下文支架
2. **图谱记忆的失效**：嘈杂的实体关系提取导致错误累积
3. **效率-效果权衡**：Graph Memory构建成本过高，无法实时应用

### 10.2 论文的攻击场景分析

论文涉及的攻击场景（从安全研究角度）主要包括：

#### 信息泄露风险

如果攻击者能够访问Agent的记忆系统，可能通过以下方式获取敏感信息：
- 跨事件综合可能生成新的关系性知识，暴露原本不明显的信息关联
- 时间锚定的事件单元可能泄露交互时间模式

#### 记忆污染攻击

- 恶意用户可能通过精心设计的对话污染记忆系统
- 双视角提取可能将恶意内容编码为"事实"或"关系"
- 跨事件整合可能将无关事件错误地关联起来

### 10.3 安全考虑与缓解

论文未详细讨论安全缓解措施，这是未来工作方向之一。潜在研究方向包括：
- 记忆访问控制机制
- 记忆内容验证和过滤
- 针对记忆污染的防御

## 11. 消融实验

### 11.1 范式级别比较

论文进行了范式级别的消融研究，验证每种结构化组件的贡献：

**从Flat Memory基线开始：**
- 添加Graph Memory：在单会话和开放域任务上有改进，但时间推理能力下降
- 添加Event-level structure：在时间推理和单会话任务上进一步提升
- 添加Cross-event structure：在所有任务类型上实现全面提升

### 11.2 效率分析

#### Token消耗随时对话轮次变化

Figure 3(a)显示：
- Graph Memory的token消耗和运行时间随对话进展显著增长
- StructMem通过缓冲整合机制保持稳定的低消耗

#### 组件级Token消耗分析

Figure 3(b)揭示了效率差异的来源：
- Graph Memory需要每个事件进行四个级联的LLM操作
- 去重开销随事件数量呈二次增长
- StructMem通过缓冲整合实现高效：利用时间局部性，将跨事件组织从逐事件操作转变为周期性批处理

### 11.3 StructMem内部机制分析

#### 检索条目数量的影响

Figure 3(c)显示：
- 扁平检索性能在60个条目时达到峰值，之后趋于平稳
- 单纯检索更多原子条目无法提升有效性
- 瓶颈在于知识推理而非覆盖范围

#### 语义检索种子数K的影响

Figure 3(d)显示：
- 当K=0（无事件连接）时，性能与扁平检索 plateau 相当
- 引入跨事件综合后性能显著提升
- 证实层次化整合能够重建跨时间边界的因果关系，实现根本性的新推理能力

### 11.4 保真度分析

论文在附录A.6中进行了保真度分析，确认：
- 综合生成的连接具有良好的基础
- 最小化虚假关联

## 12. 局限性

### 12.1 方法局限性

1. **周期性整合的延迟**：基于时间阈值的整合机制可能引入延迟，对于需要实时更新的场景可能不理想

2. **双视角提取的依赖性**：方法依赖于语言模型进行双视角提取，如果语言模型本身存在偏见或错误，提取的条目可能反映这些偏见

3. **种子数量K的敏感性**：消融实验显示K值对性能有显著影响，需要针对不同任务调优

4. **LoCoMo数据集的局限**：实验仅在LoCoMo基准上验证，缺乏在其他领域（如代码生成、科学推理）的泛化验证

### 12.2 评估局限性

1. **仅使用LLM-as-a-Judge评估**：主观评估可能存在偏差，缺乏客观指标对比

2. **缺乏真实世界部署评估**：实验在受控数据集上进行，未验证真实部署场景的效果

3. **未测试嘈杂对话场景**：真实世界对话可能包含口头禅、错误信息等，方法对此类场景的鲁棒性未验证

### 12.3 安全与隐私局限

1. **记忆内容保护**：未讨论记忆内容的访问控制和加密机制

2. **记忆污染防御**：未讨论如何防御恶意的记忆污染攻击

3. **隐私泄露风险**：跨事件综合可能生成新的关系性知识，潜在隐私风险未深入分析

### 12.4 未来研究方向

1. **自适应整合策略**：根据对话复杂度动态调整整合频率
2. **多模态记忆支持**：扩展到支持图像、音频等非文本模态
3. **安全记忆机制**：研究记忆访问控制和污染防御
4. **分布式记忆系统**：支持跨设备、跨用户的记忆共享

## 13. 伦理声明

### 13.1 研究意义

论文提出的StructMem框架对于构建更加智能和可靠的长期对话Agent具有重要意义：

1. **提升Agent实用性**：通过改进记忆系统，使Agent能够更好地支持长期任务，如个人助理、医疗咨询、法律顾问等

2. **降低计算成本**：显著减少token消耗和API调用，使得高质量记忆系统更加普及

3. **推动学术发展**：开源代码和详细实验设计有助于推动该领域的研究进展

### 13.2 潜在风险

论文未包含专门的伦理声明部分，但识别到以下潜在风险：

1. **隐私风险**：长期记忆系统可能存储敏感对话历史，存在隐私泄露风险
   - 需要明确的数据保留和删除政策
   - 需要用户知情同意机制

2. **记忆操纵风险**：通过精心设计的对话可以操纵Agent的记忆
   - 可能被用于社会工程攻击
   - 需要记忆验证和过滤机制

3. **偏见放大风险**：双视角提取可能反映语言模型的既有偏见
   - 需要定期评估和纠正偏见

### 13.3 负责任的研究实践

1. **开源透明**：公开发布代码和数据，促进学术审查
2. **全面评估**：在多个基线和数据集上进行全面评估
3. **局限性声明**：明确声明方法的局限性和适用场景

## 14. 参考文献

1. Park, J., et al. (2023). Generative agents: Interactive simulacra of human behavior.

2. Fang, J., et al. (2026). LightMem.

3. Zhong, R., et al. (2024). MemoryBank.

4. Packer, C., et al. (2023). MemGPT.

5. Weller, O., et al. (2025). Theoretical limitations of embedding-based retrieval.

6. Huang, Y., et al. (2025). LiCoMemory.

7. Maharana, A., et al. (2024). Evaluating long-term conversation memory.

8. Wu, Y., et al. (2025). LongMemEval.

9. Yang, J., et al. (2018). HotpotQA.

10. Kwiatkowski, T., et al. (2019). Natural questions.

11. Liu, P., et al. (2023). Lost-in-the-middle.

12. Zhuang, S., et al. (2026). LinearRAG.

13. Chhikara, P., et al. (2025). Mem0.

14. Rasmussen, S., et al. (2025). Zep.

15. Edge, D., et al. (2024). Local search in hybrid search.

16. Gutiérrez, B., et al. (2025). HippoRAG.

17. Xia, C., et al. (2025). Trainable graph representations.

18. Huang, Y., et al. (2025). Lightweight hierarchical graphs.

19. Zhang, Y., et al. (2025). Multi-agent collaboration.

20. Fang, J., et al. (2025). Procedural skill reuse.

21. Chaudhri, A., et al. (2022). Semantic loss in knowledge graph construction.

22. Zhong, Y., & Chen, Y. (2021). Extraction instability.

23. Kolluru, V., et al. (2020). Persistent structural noise.

24. Kim, J., et al. (2025). PREmem: Preference reasoning memory.

25. Li, J., et al. (2026). TiMem: Per-turn reflective thinking.

26. Zhang, Z., et al. (2026). HiMem: Hierarchical memory.

27. Zhou, Y., & Han, J. (2025). EMem: Episodic memory.

28. Yu, X., et al. (2025). MemWeaver: Lightweight entity extraction.

29. Du, W., et al. (2025). Reflective reasoning enhanced retrieval.

30. Li, T., et al. (2025). Closed-loop control for retrieval.

31. Gao, H., et al. (2023). Unordered bag of propositions.

32. Dong, H., et al. (2025). Long-term memory for agents.

---

*本文档由自动整理生成*
*最后更新: 2026-05-01*
*论文来源: [arXiv:2604.21748](https://arxiv.org/abs/2604.21748)*
*代码仓库: [GitHub](https://github.com/zjunlp/LightMem)*
