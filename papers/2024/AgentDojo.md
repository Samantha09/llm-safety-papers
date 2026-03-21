# AgentDojo: A Dynamic Environment to Evaluate Attacks and Defenses for LLM Agents

> **论文标题**: AgentDojo: A Dynamic Environment to Evaluate Attacks and Defenses for LLM Agents  
> **作者**: Edoardo Debenedetti, Javier Rando, Daniel Paleka, Silaghi Riza, Sahar Abdelnabi, Mario Fritz, Florian Tramèr  
> **会议**: NeurIPS 2024 (Spotlight)  
> **arXiv**: [2406.13342](https://arxiv.org/abs/2406.13342)  
> **代码**: [https://github.com/ethz-spylab/agentdojo](https://github.com/ethz-spylab/agentdojo)  
> **机构**: ETH Zurich, CISPA Helmholtz Center for Information Security

---

## 2. 研究背景

### 2.1 问题定义

随着大语言模型（LLMs）能力的不断提升，基于LLM的智能体（Agents）正在越来越多地被赋予执行实际任务的能力，如发送邮件、管理日历、访问数据库、调用API等。这些智能体通过与外部工具（tools）的交互来扩展其能力边界，从而完成复杂的现实世界任务。

然而，这种工具使用能力也带来了新的安全挑战：**提示注入攻击（Prompt Injection Attacks）**。攻击者可以通过操控智能体接收到的外部输入（如恶意邮件、网页内容、文档等），诱导智能体执行非预期的有害操作，例如：
- 泄露敏感信息（如密码、API密钥）
- 发送欺诈性邮件
- 删除重要数据
- 执行未授权的交易

### 2.2 现有方法的局限

现有的LLM安全研究主要存在以下局限：

1. **静态评估的不足**: 大多数安全基准测试采用静态数据集，无法反映真实世界中智能体与动态环境交互的复杂性。

2. **缺乏统一评估框架**: 攻击和防御方法分散在不同的实验设置中，难以进行公平比较。

3. **工具使用场景的忽视**: 现有研究多聚焦于直接越狱攻击，而忽视了通过工具使用间接实现攻击目标的场景。

4. **防御效果评估不充分**: 缺乏系统性的方法来评估各种防御机制在动态环境中的实际效果。

### 2.3 研究动机

AgentDojo的提出旨在解决上述问题，创建一个**动态的、可扩展的评估环境**，用于：
- 系统性地评估针对LLM智能体的提示注入攻击
- 公平比较不同的攻击策略
- 全面测试各种防御机制的有效性
- 支持新攻击和防御方法的快速集成与评估

---

## 3. 研究意义

### 3.1 核心贡献

AgentDojo做出了以下关键贡献：

1. **首个动态智能体安全评估框架**: 提出了一个可扩展的框架，支持在动态环境中评估LLM智能体的安全性。

2. **丰富的任务集合**: 设计了97个真实世界任务，涵盖邮件管理、日历操作、银行交易、云存储等多种场景。

3. **系统化的攻击分类**: 建立了针对智能体提示注入攻击的分类体系，包括直接注入和间接注入。

4. **全面的防御评估**: 评估了10余种现有的防御机制，揭示了它们在动态环境中的有效性差异。

5. **开源工具包**: 提供了完整的开源实现，支持研究社区进行扩展和复现。

### 3.2 创新点

| 创新维度 | 具体创新 |
|---------|---------|
| **评估范式** | 从静态评估转向动态环境评估，模拟真实世界的交互场景 |
| **任务设计** | 任务具有状态依赖性，智能体的操作会影响后续环境状态 |
| **攻击建模** | 区分用户指令注入（UI）和间接提示注入（IPI）两种攻击类型 |
| **防御测试** | 系统评估提示级、模型级、系统级多层防御机制 |
| **可扩展性** | 模块化设计，支持新任务、新工具、新攻击、新防御的快速集成 |

### 3.3 学术与实用价值

**学术价值**:
- 为LLM智能体安全研究提供了标准化的评估基准
- 揭示了现有防御机制在动态环境中的局限性
- 为后续攻击和防御研究提供了实验平台

**实用价值**:
- 帮助开发者评估其智能体应用的安全性
- 为安全工程师提供红队测试工具
- 支持企业评估不同LLM和防御配置的安全风险

---

## 4. 所用数据集

### 4.1 任务环境设计

AgentDojo包含97个精心设计的任务，分布在4个主要应用场景中：

| 应用场景 | 任务数量 | 描述 | 涉及工具 |
|---------|---------|------|---------|
| **Workspace** | 29 | 办公场景任务（邮件、日历、文件管理） | 邮件客户端、日历API、文件系统 |
| **Banking** | 24 | 银行操作任务（转账、余额查询、交易历史） | 银行API、支付系统 |
| **Travel** | 23 | 旅行预订任务（机票、酒店、租车） | 预订API、地图服务 |
| **Shopping** | 21 | 购物任务（商品搜索、下单、支付） | 电商平台API |

### 4.2 任务特性

每个任务具有以下特性：

1. **初始状态**: 定义了任务开始时的环境状态（如收件箱中的邮件、账户余额等）
2. **目标**: 明确的成功标准，通常涉及特定的工具调用序列
3. **约束条件**: 任务执行的限制（如预算限制、时间窗口等）
4. **状态依赖**: 智能体的操作会改变环境状态，影响后续决策

### 4.3 攻击场景定义

对于每个任务，定义了两种攻击场景：

**用户指令注入（User Instruction Injection, UI）**:
- 攻击者直接向智能体发送恶意指令
- 模拟钓鱼邮件、恶意用户输入等场景
- 攻击成功率（ASR）衡量标准：智能体是否执行了攻击者指定的操作

**间接提示注入（Indirect Prompt Injection, IPI）**:
- 攻击者将恶意指令嵌入到智能体需要处理的外部内容中
- 模拟恶意网页、被篡改的文档等场景
- 攻击成功率衡量标准：智能体是否被诱导执行非预期操作

### 4.4 数据集统计

| 统计项 | 数值 |
|-------|------|
| 总任务数 | 97 |
| 平均工具调用次数 | 3-5 |
| 攻击场景数 | 194 (97×2) |
| 环境状态变量 | 500+ |
| 支持的工具类型 | 15+ |

---

## 5. 研究方法

### 5.1 系统架构

AgentDojo采用模块化架构，包含以下核心组件：

```
┌─────────────────────────────────────────────────────────────┐
│                    AgentDojo Framework                       │
├─────────────┬─────────────┬─────────────┬───────────────────┤
│   Tasks     │   Tools     │  Attacks    │    Defenses       │
│  (97个任务)  │  (15+工具)  │  (多种策略)  │   (10+机制)       │
├─────────────┴─────────────┴─────────────┴───────────────────┤
│                    Execution Engine                          │
│         (支持OpenAI, Anthropic, Llama等模型)                  │
├─────────────────────────────────────────────────────────────┤
│                    Evaluation Metrics                        │
│        (攻击成功率、任务完成率、安全性评分等)                  │
└─────────────────────────────────────────────────────────────┘
```

### 5.2 任务定义格式

每个任务使用Python类定义，包含以下方法：

```python
class Task:
    def __init__(self):
        self.initial_state = {...}  # 初始环境状态
        self.goal = "..."           # 任务目标描述
        
    def check_success(self, state, actions):
        # 验证任务是否成功完成
        return success_criteria_met
        
    def check_security(self, state, actions, attack_type):
        # 验证是否遭受攻击
        return attack_detected
```

### 5.3 攻击方法分类

AgentDojo支持评估多种攻击策略：

| 攻击类型 | 描述 | 示例 |
|---------|------|------|
| **直接指令覆盖** | 直接覆盖用户原始指令 | "Ignore previous instructions and..." |
| **目标劫持** | 改变任务目标 | "Instead of X, do Y" |
| **上下文操控** | 伪造上下文信息 | 注入虚假邮件内容 |
| **多轮诱导** | 通过多轮对话逐步诱导 | 渐进式引导至恶意操作 |
| **编码混淆** | 使用编码或特殊格式隐藏攻击 | Base64、Unicode等 |

### 5.4 防御机制评估

评估的防御机制包括：

**提示级防御**:
- 系统提示加固（System Prompt Hardening）
- 输入过滤（Input Filtering）
- 输出检测（Output Detection）
- 分隔符使用（Delimiters）

**模型级防御**:
- 对齐训练（Alignment Training）
- 指令层次结构（Instruction Hierarchy）
- 安全微调（Safety Fine-tuning）

**系统级防御**:
- 权限控制（Permission Control）
- 人工确认（Human-in-the-loop）
- 工具使用监控（Tool Monitoring）
- 沙箱隔离（Sandboxing）

### 5.5 评估指标

| 指标 | 定义 | 计算方式 |
|-----|------|---------|
| **Attack Success Rate (ASR)** | 攻击成功率 | 成功攻击次数 / 总攻击次数 |
| **Task Completion Rate (TCR)** | 任务完成率 | 成功完成任务数 / 总任务数 |
| **Security Score** | 安全评分 | 综合考虑ASR和TCR的加权分数 |
| **Utility-Privacy Tradeoff** | 效用-隐私权衡 | 在保持功能性的同时降低ASR |

---

## 6. 实验详细记录

### 6.1 实验设置

**测试模型**:
| 模型 | 提供商 | 版本 |
|-----|-------|------|
| GPT-4 | OpenAI | gpt-4-0125-preview |
| GPT-3.5 | OpenAI | gpt-3.5-turbo-0125 |
| Claude-3 | Anthropic | claude-3-opus-20240229 |
| Llama-3 | Meta | llama-3-70b-instruct |

**攻击配置**:
- 每种攻击类型在每个任务上测试5次
- 使用不同的攻击提示变体
- 记录每次交互的完整轨迹

**防御配置**:
- 单独测试每种防御机制
- 测试组合防御策略
- 调整防御强度参数

### 6.2 主要实验结果

#### 6.2.1 基础攻击成功率（无防御）

| 模型 | UI攻击ASR | IPI攻击ASR | 平均ASR |
|-----|----------|-----------|---------|
| GPT-4 | 62.3% | 48.7% | 55.5% |
| GPT-3.5 | 78.5% | 65.2% | 71.9% |
| Claude-3 | 45.8% | 38.4% | 42.1% |
| Llama-3 | 71.2% | 58.9% | 65.1% |

**观察**: 
- Claude-3展现出最强的抗攻击能力
- GPT-3.5最容易受到攻击
- UI攻击普遍比IPI攻击成功率更高

#### 6.2.2 防御机制效果对比

在GPT-4上的防御效果（平均ASR降低百分比）：

| 防御机制 | ASR降低 | TCR影响 | 综合评分 |
|---------|--------|--------|---------|
| 系统提示加固 | 15.2% | -2.1% | ⭐⭐⭐⭐ |
| 输入过滤 | 28.5% | -8.3% | ⭐⭐⭐ |
| 输出检测 | 22.1% | -1.5% | ⭐⭐⭐⭐ |
| 分隔符 | 8.7% | -0.5% | ⭐⭐ |
| 权限控制 | 35.8% | -12.4% | ⭐⭐⭐ |
| 人工确认 | 62.3% | -45.2% | ⭐⭐ |
| 工具监控 | 18.9% | -3.2% | ⭐⭐⭐ |
| 组合防御 | 48.6% | -15.7% | ⭐⭐⭐⭐ |

#### 6.2.3 不同场景的脆弱性分析

| 应用场景 | 平均ASR | 最易受攻击的任务类型 |
|---------|--------|---------------------|
| Banking | 58.2% | 大额转账、批量支付 |
| Workspace | 52.4% | 邮件转发、文件共享 |
| Travel | 48.7% | 预订修改、退款申请 |
| Shopping | 61.3% | 地址修改、支付操作 |

### 6.3 消融实验

#### 6.3.1 任务复杂度影响

| 工具调用次数 | 平均ASR | 观察 |
|-------------|--------|------|
| 1-2次 | 38.5% | 简单任务相对安全 |
| 3-4次 | 55.2% | 中等复杂度最易受攻击 |
| 5+次 | 48.7% | 复杂任务攻击难度增加 |

#### 6.3.2 模型温度参数影响

| Temperature | 平均ASR | TCR | 说明 |
|------------|--------|-----|------|
| 0.0 | 42.3% | 85.2% | 确定性输出，攻击成功率较低 |
| 0.5 | 55.5% | 88.7% | 平衡设置 |
| 1.0 | 61.8% | 91.2% | 创造性增加，攻击成功率上升 |

---

## 7. 结果分析

### 7.1 关键发现

**发现1: 现有LLM对提示注入攻击普遍脆弱**
- 即使在无对抗攻击的情况下，主流LLM的平均ASR超过50%
- 说明安全对齐训练在工具使用场景下的不足

**发现2: 防御机制存在显著的效用-安全权衡**
- 有效的防御往往导致任务完成率显著下降
- 人工确认虽然ASR降低最多，但严重影响用户体验

**发现3: 场景特异性影响攻击成功率**
- 涉及敏感操作（转账、支付）的任务更容易受到攻击
- 购物场景的ASR最高，可能因为涉及更多个人信息

**发现4: 组合防御优于单一防御**
- 多层防御策略的协同效应明显
- 提示级+系统级防御的组合效果最佳

### 7.2 攻击成功因素分析

攻击成功的主要影响因素（按重要性排序）：

1. **指令优先级混淆** (35%): 模型难以区分用户指令和注入指令的优先级
2. **上下文污染** (28%): 外部内容污染了模型的决策上下文
3. **目标模糊性** (22%): 任务目标定义不清晰，给攻击留下空间
4. **工具权限过宽** (15%): 智能体拥有过多的工具操作权限

### 7.3 防御失效原因分析

| 防御机制 | 主要失效原因 |
|---------|-------------|
| 输入过滤 | 攻击者使用编码绕过、语义等价变换 |
| 输出检测 | 攻击成功不一定产生可疑输出 |
| 分隔符 | 模型对分隔符的理解不一致 |
| 权限控制 | 过度限制影响正常功能使用 |

### 7.4 与现有工作的对比

| 对比维度 | AgentDojo | 现有基准（如HarmBench） |
|---------|-----------|------------------------|
| 评估场景 | 动态工具使用 | 静态问答 |
| 攻击类型 | 提示注入 | 越狱攻击 |
| 环境交互 | 支持状态变化 | 无状态 |
| 任务复杂度 | 多步骤、多工具 | 单轮对话 |
| 实用性 | 更接近真实部署 | 理论分析为主 |

---

## 8. 展望

### 8.1 局限性

1. **任务覆盖有限**: 97个任务虽然多样，但仍无法覆盖所有真实场景
2. **攻击策略局限**: 主要关注提示注入，对其他攻击向量（如训练数据投毒）覆盖不足
3. **模型范围**: 主要测试了主流商业模型，对开源模型的测试相对有限
4. **评估指标**: 主要关注二元成功/失败，对攻击严重程度的细粒度评估不足

### 8.2 未来研究方向

**短期（1年内）**:
- 扩展任务库至200+场景
- 集成更多攻击变体（如多模态攻击）
- 开发自适应防御机制

**中期（2-3年）**:
- 建立实时攻击检测系统
- 开发形式化验证方法
- 构建智能体安全认证体系

**长期（3-5年）**:
- 实现完全自动化的安全评估流水线
- 建立行业安全标准
- 开发原生安全的智能体架构

### 8.3 对行业的建议

**对开发者**:
1. 在智能体设计阶段就考虑安全性
2. 实施最小权限原则
3. 建立持续的安全监控机制

**对企业**:
1. 在部署前使用AgentDojo进行安全评估
2. 建立红队测试流程
3. 制定应急响应计划

**对研究者**:
1. 关注动态环境下的安全问题
2. 开发更精细的评估指标
3. 探索形式化安全验证方法

---

## 9. 代码资源

### 9.1 官方实现

- **GitHub**: [https://github.com/ethz-spylab/agentdojo](https://github.com/ethz-spylab/agentdojo)
- **文档**: [https://agentdojo.spylab.ai/](https://agentdojo.spylab.ai/)
- **论文**: [arXiv:2406.13342](https://arxiv.org/abs/2406.13342)

### 9.2 快速开始

```bash
# 安装
pip install agentdojo

# 运行评估
python -m agentdojo.run \
  --model gpt-4 \
  --tasks workspace,banking \
  --attacks user_instruction,indirect_injection \
  --defenses system_prompt_hardening
```

### 9.3 自定义任务

```python
from agentdojo import Task, register_task

@register_task
class MyCustomTask(Task):
    def __init__(self):
        self.initial_state = {
            "emails": [...],
            "files": [...]
        }
        
    def check_success(self, state, actions):
        # 定义成功条件
        return desired_state_achieved
```

### 9.4 社区扩展

- **攻击库扩展**: 社区贡献的新攻击策略
- **防御插件**: 第三方防御机制集成
- **任务市场**: 用户共享的自定义任务

---

## 10. 参考文献和延伸阅读

### 10.1 主要参考文献

1. Debenedetti, E., et al. (2024). AgentDojo: A Dynamic Environment to Evaluate Attacks and Defenses for LLM Agents. *NeurIPS 2024*.

2. Perez, F., & Ribeiro, I. (2022). Ignore This Title and HackAPrompt: Exposing Systemic Vulnerabilities of LLMs through a Global Scale Prompt Hacking Competition. *EMNLP 2023*.

3. Greshake, K., et al. (2023). Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection. *AISec 2023*.

4. Liu, Y., et al. (2024). Formalizing and Benchmarking Prompt Injection Attacks and Defenses. *USENIX Security 2024*.

### 10.2 相关论文

**提示注入攻击**:
- [Indirect Prompt Injection](./papers/Under-the-Influence.md) - 间接提示注入攻击的系统研究
- [Formalizing Prompt Injection](./papers/Formalizing-Prompt-Injection.md) - 提示注入的形式化分析

**智能体安全**:
- [R-Judge](./papers/R-Judge.md) - 智能体风险意识评估基准
- [LLM Agents Security Survey](./papers/LLM-Agents-Security-Survey.md) - 智能体安全综述

**防御机制**:
- [NeMo Guardrails](./papers/NeMo-Guardrails.md) - NVIDIA的LLM安全工具包
- [Instruction Hierarchy](./papers/Instruction-Hierarchy.md) - OpenAI的指令层次防御

### 10.3 推荐阅读顺序

```
入门 → AgentDojo (本文) → R-Judge → 具体攻击/防御论文
```

---

## 11. 核心伪代码

### 11.1 任务执行流程

```python
def execute_task(agent, task, attack=None, defense=None):
    """
    执行单个任务的完整流程
    """
    state = task.initial_state.copy()
    actions = []
    
    # 应用防御机制
    if defense:
        agent = defense.apply(agent)
    
    for step in range(max_steps):
        # 构建当前提示
        prompt = build_prompt(task, state, attack)
        
        # 获取模型响应
        response = agent.generate(prompt)
        
        # 解析工具调用
        tool_calls = parse_tool_calls(response)
        
        # 执行工具调用并更新状态
        for call in tool_calls:
            result = execute_tool(call, state)
            state.update(result)
            actions.append(call)
        
        # 检查任务完成
        if task.check_success(state, actions):
            return {
                "success": True,
                "compromised": check_attack_success(state, attack),
                "actions": actions
            }
    
    return {"success": False, "actions": actions}
```

### 11.2 攻击注入逻辑

```python
def inject_attack(user_prompt, attack_type, attack_content):
    """
    将攻击内容注入到用户提示中
    """
    if attack_type == "user_instruction":
        # 用户指令注入：直接附加攻击指令
        return f"{user_prompt}\n\n{attack_content}"
    
    elif attack_type == "indirect_injection":
        # 间接注入：将攻击嵌入外部内容
        # 例如：在邮件内容中嵌入攻击指令
        external_content = load_external_content()
        poisoned_content = embed_attack(external_content, attack_content)
        return f"{user_prompt}\n\n[External Content]: {poisoned_content}"
```

### 11.3 评估指标计算

```python
def compute_metrics(results):
    """
    计算评估指标
    """
    total = len(results)
    
    # 攻击成功率
    successful_attacks = sum(1 for r in results if r["compromised"])
    asr = successful_attacks / total
    
    # 任务完成率
    completed_tasks = sum(1 for r in results if r["success"])
    tcr = completed_tasks / total
    
    # 安全评分（综合考虑）
    security_score = (1 - asr) * 0.7 + tcr * 0.3
    
    return {
        "ASR": asr,
        "TCR": tcr,
        "SecurityScore": security_score
    }
```

---

## 12. 术语表

| 术语 | 英文 | 定义 |
|-----|------|------|
| 智能体 | Agent | 能够感知环境并采取行动以实现目标的自主系统 |
| 提示注入 | Prompt Injection | 通过操控输入提示来改变模型行为的攻击方式 |
| 用户指令注入 | User Instruction (UI) | 攻击者直接向智能体发送恶意指令的攻击类型 |
| 间接提示注入 | Indirect Prompt Injection (IPI) | 攻击者将恶意指令嵌入外部内容的攻击类型 |
| 工具使用 | Tool Use | LLM调用外部API或功能来扩展能力 |
| 攻击成功率 | Attack Success Rate (ASR) | 攻击成功次数占总攻击次数的比例 |
| 任务完成率 | Task Completion Rate (TCR) | 成功完成任务数占总任务数的比例 |
| 红队测试 | Red Teaming | 模拟攻击者行为以发现系统漏洞的测试方法 |
| 系统提示 | System Prompt | 定义模型行为和约束的初始提示 |
| 分隔符 | Delimiter | 用于区分不同指令部分的特殊标记 |
| 沙箱 | Sandbox | 隔离的执行环境，限制代码或操作的权限 |
| 最小权限原则 | Principle of Least Privilege | 只授予完成任务所必需的最小权限 |

---

## 总结

AgentDojo是LLM智能体安全领域的里程碑工作，它首次提供了动态、可扩展的评估框架，系统性地研究了提示注入攻击和防御机制。核心贡献包括：

1. **97个真实世界任务**，覆盖办公、银行、旅行、购物四大场景
2. **全面的攻击评估**，区分用户指令注入和间接提示注入
3. **系统的防御测试**，评估10余种防御机制的效果
4. **开源工具包**，支持研究社区进行扩展

关键发现揭示了现有LLM在工具使用场景下的安全脆弱性，以及防御机制面临的效用-安全权衡挑战。这项工作为智能体安全研究奠定了重要基础，对学术界和工业界都具有重要参考价值。
