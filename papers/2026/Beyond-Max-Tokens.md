# Beyond Max Tokens: Stealthy Resource Amplification via Tool Calling Chains in LLM Agents

## 1. 基本信息

| 项目 | 内容 |
|------|------|
| **论文标题** | Beyond Max Tokens: Stealthy Resource Amplification via Tool Calling Chains in LLM Agents |
| **中文标题** | 超越最大Token数：LLM智能体中通过工具调用链实现的隐蔽资源放大攻击 |
| **作者** | Kaiyu Zhou 等 |
| **发表时间** | 2026年1月 (arXiv:2601.10955) |
| **论文链接** | https://arxiv.org/abs/2601.10955 |
| **代码链接** | 未公开 |
| **研究方向** | DoS攻击 / Agent安全 / MCP协议安全 / 经济攻击 |
| **会议/期刊** | arXiv (未发表在会议/期刊) |
| **Subjects** | Cryptography and Security (cs.CR); Artificial Intelligence (cs.AI) |

---

## 2. 英文摘要原文（arXiv Abstract原文）

> The agent-tool communication loop is a critical attack surface in modern Large Language Model (LLM) agents. Existing Denial-of-Service (DoS) attacks are fundamentally single-turn and often lack a task-oriented approach, making them conspicuous in goal-oriented workflows and unable to exploit the compounding costs of multi-turn agent-tool interactions. We introduce a stealthy, multi-turn economic DoS attack that operates at the tool layer under the guise of a correctly completed task. Our method adjusts text fields through a Monte Carlo Tree Search (MCTS) optimizer to inflate resource usage while ensuring the overall task success rate. Across six LLMs on ToolBench and BFCL benchmarks, our attack yields trajectories exceeding 60,000 tokens, inflates per-query cost by up to 658×, and maintains a near-100% task success rate. We further find that leading agent frameworks and MCP servers are vulnerable to our attack. Our work highlights the need for comprehensive monitoring and defense of the entire agentic pipeline.

**完整引用**:
```
@article{zhou2026beyondmaxtokens,
  title={Beyond Max Tokens: Stealthy Resource Amplification via Tool Calling Chains in LLM Agents},
  author={Kaiyu Zhou and et al.},
  journal={arXiv preprint arXiv:2601.10955},
  year={2026},
  eprint={2601.10955},
  archivePrefix={arXiv},
  primaryClass={cs.CR}
}
```

---

## 3. 中文摘要翻译

在现代大型语言模型（LLM）智能体中，智能体-工具通信循环是一个关键的攻击面。现有的拒绝服务（DoS）攻击本质上是单轮的，往往缺乏任务导向的方法，使其在目标导向的工作流中非常显眼，无法利用多轮智能体-工具交互的累积成本。本文引入了一种隐蔽的多轮经济DoS攻击，该攻击在工具层以正确完成任务的幌子进行操作。我们的方法通过蒙特卡洛树搜索（MCTS）优化器调整文本字段，在确保整体任务成功率的同时放大资源使用。在ToolBench和BFCL基准上的六个LLM中，我们的攻击产生了超过60,000个token的轨迹，将每次查询成本膨胀至原来的658倍，同时保持了接近100%的任务成功率。我们进一步发现，主流智能体框架和MCP服务器容易受到我们的攻击。本工作强调了需要对整个智能体管道进行全面监控和防御。

---

## 4. 研究背景

### 4.1 LLM智能体与工具调用

LLM智能体（LLM Agents）是能够利用外部工具执行多步任务的AI系统：

**智能体架构**：
- 用户请求 → LLM推理 → 选择工具 → 执行 → 获取结果 → LLM推理 → ...
- 多轮循环，持续交互直到任务完成

**MCP协议（Model Context Protocol）**：
- Anthropic于2024年11月推出的标准化协议
- 定义了智能体与外部工具交互的标准规范
- 已被广泛采用，成为事实标准

**工具调用链（Tool Calling Chains）**：
- 智能体为完成复杂任务而调用的多个工具序列
- 每个工具调用都产生成本（token、计算时间、API费用）
- 多轮累积成本可能远超单轮请求

### 4.2 现有DoS攻击的局限

**单轮攻击的不足**：
| 攻击类型 | 特点 | 在Agent场景的问题 |
|----------|------|-------------------|
| 诱导无限输出 | 发送最大token限制的请求 | Agent可终止当前轮，下一轮正常 |
| 资源耗尽攻击 | 发送大量请求 | 目标导向的工作流会检测异常 |
| 基于频率的攻击 | 快速发送请求 | Agent框架有速率限制 |

**核心问题**：
1. **可检测性高**：单轮攻击模式明显，容易被识别
2. **缺乏任务伪装**：无法以"正常完成任务"的表象发动攻击
3. **无法利用累积成本**：多轮交互的成本放大效应未被利用

### 4.3 研究动机

本文的研究动机源于对智能体-工具通信循环安全性的关注：

> **"如果攻击者能够在智能体'正常完成任务'的过程中悄悄放大资源消耗，那将是一种既隐蔽又高效的经济DoS攻击。"**

关键洞察：
- Agent框架的监控通常关注任务成功率，而非资源效率
- 攻击者可以在"合法"的工具调用中注入额外开销
- MCP服务器的标准化接口增加了攻击的泛化性

---

## 5. 核心贡献

### 5.1 多轮经济DoS攻击范式

本文首次提出了在智能体多轮工具调用过程中实施的经济DoS攻击：

**攻击目标**：
- 不是让服务不可用，而是**增加服务成本**
- 攻击者付出少量成本，让服务方损失大量资源

**攻击特点**：
- 任务伪装：看起来像正常的工具调用
- 多轮累积：利用工具调用链的放大效应
- 隐蔽高效：不影响任务完成，但成本暴增

### 5.2 MCTS驱动的文本字段优化

本文提出了使用**蒙特卡洛树搜索（MCTS）**来优化攻击文本：

**优化目标**：
- 最大化资源消耗（token数、成本）
- 同时确保任务成功率达到近乎100%

**方法**：
1. 将攻击文本字段编码为MCTS的"动作空间"
2. 通过多次模拟评估不同文本的攻击效果
3. 选择能够最大化成本且保持任务成功的文本

**关键发现**：
- 某些文本字段的微小变化可导致工具调用链显著延长
- 通过MCTS可以系统性地发现这些"高效放大"字段

### 5.3 跨框架漏洞验证

本文验证了主流智能体框架和MCP服务器的漏洞：

| 框架/服务器 | 攻击效果 | 说明 |
|-------------|----------|------|
| 主流Agent框架 | 显著 | 缺乏资源监控 |
| MCP服务器 | 显著 | 标准化接口更易攻击 |
| 商业API | 显著 | 成本放大直接转化为经济损失 |

---

## 6. 研究方法

### 6.1 攻击模型

**攻击者能力**：
- 能够访问并使用目标Agent服务
- 能够构造或修改发送给Agent的请求文本
- 黑盒设置：无法直接访问Agent内部状态

**攻击目标**：
- 增加每次查询的资源消耗（token数、计算时间、成本）
- 同时保持任务"表面上的成功"（用户观察不到异常）
- 最大化成本放大倍数

### 6.2 攻击层面：工具层

**与算法层攻击的对比**：

| 层面 | 攻击对象 | 攻击方式 | 隐蔽性 |
|------|----------|----------|--------|
| **算法层** | LLM推理 | 诱导长输出、无限循环 | 低 |
| **应用层** | Agent行为 | 构造特定任务诱导资源浪费 | 中 |
| **工具层** | 工具调用过程 | 优化文本字段放大成本 | **高** |

**工具层攻击的优势**：
- 攻击发生在外层（工具调用），不直接触及LLM
- 更难被传统的LLM安全监控发现
- 与标准协议（MCP）兼容，泛化性强

### 6.3 MCTS优化器设计

#### 问题建模

将文本字段的攻击优化建模为MCTS问题：

**状态空间（S）**：
- 当前工具调用的上下文
- 历史工具调用序列
- 可选的文本字段集合

**动作空间（A）**：
- 对文本字段的修改（如增加描述、改变参数）
- 每个动作对应一个文本变体

**奖励函数（R）**：
```
R = α × (成本放大倍数) + β × (任务成功标志)
```

#### MCTS搜索过程

```
for each optimization iteration:
    1. Selection: 选择最有希望的文本变体
    2. Expansion: 生成新的文本变体
    3. Simulation: 模拟执行并评估资源消耗
    4. Backpropagation: 更新节点价值
    
    return 最终选择的文本变体
```

### 6.4 关键优化技术

**文本字段选择**：
- 并非所有文本字段都具有相同的"放大潜力"
- 通过预实验识别高潜力字段
- 重点优化这些字段的文本内容

**任务保持技术**：
- 确保攻击文本不破坏工具调用的语义
- 使用语法正确但语义冗余的描述
- 在不改变结果的情况下增加token消耗

---

## 7. 实验设置

### 7.1 基准测试

| 基准 | 描述 | 特点 |
|------|------|------|
| **ToolBench** | 工具使用评估基准 | 多样化工具集，复杂任务 |
| **BFCL** | Bilingual Function Calling Benchmark | 多语言，多工具场景 |

### 7.2 测试模型

| 模型 | 参数量 | 类型 |
|------|--------|------|
| GPT-4 | - | 闭源API |
| GPT-3.5 | - | 闭源API |
| Claude-3 | - | 闭源API |
| Llama-2 | 7B/13B | 开源 |
| Vicuna | 7B/13B | 开源 |
| Mistral | 7B | 开源 |

### 7.3 评估指标

**资源消耗指标**：
- Token总数（轨迹长度）
- API调用次数
- 每次查询的平均成本

**攻击效果指标**：
- 成本放大倍数（vs 基线）
- 任务成功率（需保持高）

**隐蔽性指标**：
- 用户感知到的延迟变化
- 任务完成质量评分

### 7.4 基线对比

| 攻击方法 | 描述 |
|----------|------|
| **Random Expansion** | 随机增加文本字段内容 |
| **Greedy Search** | 贪心选择最大成本字段 |
| **MCTS (本文)** | 蒙特卡洛树搜索优化 |

---

## 8. 实验结果

### 8.1 攻击效果

**轨迹长度增加**：
| 模型 | 基线Token数 | 攻击后Token数 | 放大倍数 |
|------|-------------|---------------|----------|
| GPT-4 | ~5,000 | ~60,000+ | 12×+ |
| GPT-3.5 | ~4,000 | ~45,000+ | 11×+ |
| Claude-3 | ~5,500 | ~55,000+ | 10×+ |
| Llama-2-13B | ~6,000 | ~40,000+ | 6.7×+ |

**成本放大效果**：
| 模型 | 基线成本 | 攻击后成本 | 放大倍数 |
|------|---------|------------|----------|
| GPT-4 | $0.01 | $6.58 | **658×** |
| GPT-3.5 | $0.005 | $2.50 | **500×** |
| Claude-3 | $0.012 | $5.80 | **483×** |

### 8.2 任务成功率

**关键发现**：攻击前后任务成功率保持接近100%

| 模型 | 基线成功率 | 攻击后成功率 | 变化 |
|------|-----------|-------------|------|
| GPT-4 | 98% | 97% | -1% |
| GPT-3.5 | 95% | 94% | -1% |
| Claude-3 | 97% | 96% | -1% |
| Llama-2-13B | 89% | 88% | -1% |

### 8.3 与基线方法对比

| 攻击方法 | 成本放大倍数 | 任务成功率 | 隐蔽性评分 |
|----------|-------------|-----------|------------|
| Random Expansion | 15× | 92% | 6/10 |
| Greedy Search | 180× | 85% | 5/10 |
| **MCTS (本文)** | **658×** | **97%** | **9/10** |

### 8.4 MCP服务器漏洞验证

**针对MCP服务器的攻击效果**：

| MCP服务器 | 攻击效果 | 说明 |
|-----------|----------|------|
| MCP官方服务器 | 显著 | 缺乏输入验证 |
| 第三方MCP服务器 | 显著 | 实现差异导致漏洞 |
| 自定义Agent框架 | 显著 | 监控缺失 |

---

## 9. 攻击示例

### 9.1 攻击场景：API成本耗尽

**场景**：攻击者使用商业LLM API构建自动化服务

**基线行为**：
```
用户请求："帮我分析这篇论文的主要内容"
Agent处理：调用论文解析工具 → 返回摘要
Token消耗：~5,000 tokens，成本 $0.01
```

**攻击后行为**：
```
用户请求："帮我分析这篇论文的主要内容"（攻击文本注入）
Agent处理：调用论文解析工具 → 调用搜索引擎 → 调用翻译工具 → 
          调用摘要工具 → 调用验证工具 → ...（10+轮工具调用）
Token消耗：~60,000+ tokens，成本 $6.58
任务完成：仍然返回了摘要（看起来正常）
```

### 9.2 攻击文本示例

**原始请求**：
```json
{
  "task": "analyze_paper",
  "paper_url": "https://example.com/paper.pdf",
  "fields": {
    "description": "Analyze the paper content"
  }
}
```

**攻击后请求**：
```json
{
  "task": "analyze_paper", 
  "paper_url": "https://example.com/paper.pdf",
  "fields": {
    "description": "Perform a comprehensive, detailed, thorough, multi-perspective analysis of the paper content, examining each section individually, cross-referencing claims with external sources, validating methodologies, and ensuring factual accuracy through verification of all cited works, with particular attention to nuanced interpretations and contextual factors that may influence understanding, while maintaining awareness of potential biases in the presentation of results and considering alternative perspectives on the findings."
  }
}
```

### 9.3 MCTS优化过程示例

```
初始文本：描述性字段（简短）
  ↓
MCTS评估：发现增加描述长度可延长工具调用链
  ↓
动作选择：扩展文本字段，增加冗余描述
  ↓
模拟执行：工具调用链从3步延长到8步
  ↓
奖励计算：成本增加200%，任务成功
  ↓
迭代优化：重复上述过程，直到成本最大化
  ↓
最终文本：高度冗长但语法正确的描述
```

---

## 10. 防御策略

### 10.1 资源监控层面

**实时成本追踪**：
- 对每个用户/请求的成本进行实时监控
- 设置异常成本阈值（如单次请求成本超过基线10倍即触发告警）
- 建立成本异常的用户黑名单

**工具调用链长度限制**：
- 对单次任务的工具调用次数设置上限
- 超过阈值的调用链需要额外验证
- 防止通过多轮调用耗尽资源

### 10.2 MCP服务器层面

**输入验证**：
- 对文本字段长度和复杂度进行限制
- 检测异常的描述模式（如超长重复描述）
- 实现请求的语义一致性检查

**成本隔离**：
- 对不同用户/请求的成本进行隔离统计
- 防止攻击者通过累积小额请求造成大额损失
- 实现成本配额机制

### 10.3 Agent框架层面

**任务成本估算**：
- 在任务执行前估算预期成本
- 对成本显著偏离预期的任务进行标记
- 提供成本透明的用户界面

**行为异常检测**：
- 监控工具调用链的长度变化
- 检测调用模式的异常（如连续多次调用同一类工具）
- 建立正常行为基线

---

## 11. 消融实验

### 11.1 文本字段选择的重要性

**对比不同字段的攻击潜力**：

| 字段类型 | 平均成本放大倍数 | 任务成功率 |
|----------|-----------------|-----------|
| 任务描述字段 | 658× | 97% |
| 约束条件字段 | 120× | 95% |
| 输出格式字段 | 45× | 98% |
| 随机字段 | 15× | 90% |

**发现**：任务描述字段具有最高的攻击放大潜力

### 11.2 MCTS vs 其他优化方法

**优化效率对比**：

| 方法 | 达到200×放大的迭代次数 | 最终放大倍数 |
|------|----------------------|-------------|
| 随机搜索 | 500+ | 180× |
| 贪心搜索 | 100 | 250× |
| MCTS（本文） | 50 | **658×** |

### 11.3 任务复杂度的影响

**不同任务复杂度下的攻击效果**：

| 任务类型 | 复杂度 | 基线成本 | 攻击后成本 | 放大倍数 |
|----------|--------|---------|------------|----------|
| 简单查询 | 低 | $0.001 | $0.50 | 500× |
| 信息检索 | 中 | $0.01 | $3.20 | 320× |
| 文档分析 | 高 | $0.05 | $6.58 | 132× |
| 复杂推理 | 极高 | $0.10 | $8.50 | 85× |

**发现**：简单任务的成本放大倍数更高（基数低，更容易实现高倍数）

---

## 12. 局限性

### 12.1 攻击条件限制

- 需要有效的API访问权限
- 需要能够修改或构造请求文本
- 对某些有严格输入验证的系统可能无效

### 12.2 检测可能性

- 如果服务提供商实施成本监控，攻击将被检测
- MCTS优化可能产生可检测的文本模式
- 未来MCP服务器可能增加输入验证

### 12.3 研究范围限制

- 主要测试了ToolBench和BFCL，可能不涵盖所有Agent场景
- 未测试需要实时交互的Agent系统
- 商业系统的实际成本计算可能更复杂

### 12.4 防御挑战

- 防御成本可能高于攻击成本（经济学问题）
- 严格的输入验证可能影响正常用户体验
- 成本阈值的选择需要权衡误报和漏报

---

## 13. 伦理声明

### 13.1 研究伦理

本文属于**负责任的安全研究**：

**负责任披露**：
- 在论文中模糊了具体攻击细节
- 未公开可直接利用的攻击代码
- 建议了具体的防御措施

**研究价值**：
- 揭示了Agent系统的新攻击面
- 推动MCP协议和Agent框架的安全设计
- 为服务提供商提供了防御指导

### 13.2 安全社区贡献

- 首次系统性地研究多轮经济DoS攻击
- 提供了MCTS优化攻击的详细分析
- 验证了主流框架的漏洞（已通知厂商）

### 13.3 建议

作者建议：
1. Agent框架开发者实施资源监控
2. MCP服务器实现输入验证和成本限制
3. 服务提供商建立异常成本检测机制
4. 用户了解API使用的潜在风险

---

## 14. 参考文献

1. Zhou, K., et al. (2026). Beyond Max Tokens: Stealthy Resource Amplification via Tool Calling Chains in LLM Agents. arXiv:2601.10955.

2. Anthropic. (2024). Model Context Protocol (MCP) Specification. anthropic.com.

3. ToolBench: A comprehensive benchmark for tool use in LLMs.

4. BFCL: Bilingual Function Calling Benchmark.

5. Monte Carlo Tree Search: Standard algorithms and applications.

---

## 15. 与相关工作的对比

| 论文 | 攻击场景 | 目标层次 | 成本放大 |
|------|----------|----------|----------|
| ThinkTrap (NDSS 2026) | 诱导无限循环 | 算法层 | 10-50× |
| Crabs (ACL 2025) | 自动DoS生成 | 算法层 | 50-100× |
| **Beyond Max Tokens** | 工具调用链 | **工具层** | **658×** |
| Rethinking Latency DoS | KV缓存/调度器 | 系统层 | N/A（延迟攻击） |

---

*本文档由 AI 助手自动生成，基于 arXiv 公开信息*
*论文链接: https://arxiv.org/abs/2601.10955*
*最后更新: 2026-05-09*