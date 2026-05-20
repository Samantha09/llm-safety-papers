# Resource Consumption Threats in Large Language Models

## 1. 基本信息

| 项目 | 内容 |
|------|------|
| **论文标题** | Resource Consumption Threats in Large Language Models |
| **作者** | Yuanhe Zhang, Xinyue Wang, Zhican Chen, Weiliu Wang, Zilu Zhang, Zhengshuo Gong, Zhenhong Zhou, Kun Wang, Li Sun, Yang Liu, Sen Su |
| **机构** | 北京邮电大学、杭州电子科技大学、南洋理工大学、重庆邮电大学 |
| **arXiv链接** | https://arxiv.org/abs/2603.16068 |
| **PDF链接** | https://arxiv.org/pdf/2603.16068 |
| **代码链接** | https://github.com/shuita2333/resource-consumption-threats-in-llms |
| **研究方向** | LLM资源消耗威胁综述 (DoS & Resource Exhaustion) |
| **会议/期刊** | arXiv (2026) |
| **arXiv编号** | 2603.16068v3 |
| **领域** | Cryptography and Security (cs.CR); Artificial Intelligence (cs.AI); Computation and Language (cs.CL) |

---

## 2. 英文摘要原文 (arXiv Abstract)

> Given limited and costly computational infrastructure, resource efficiency is a key requirement for large language models (LLMs). Efficient LLMs increase service capacity for providers and reduce latency and API costs for users. Recent resource consumption threats induce excessive generation, degrading model efficiency and harming both service availability and economic sustainability. This survey presents a systematic review of threats to resource consumption in LLMs. We further establish a unified view of this emerging area by clarifying its scope and examining the problem along the full pipeline from threat induction to mechanism understanding and mitigation. Our goal is to clarify the problem landscape for this emerging area, thereby providing a clearer foundation for characterization and mitigation.

**引用格式:**
```
@article{resource2026survey,
  author={Zhang, Yuanhe and Wang, Xinyue and Chen, Zhican and Wang, Weiliu and Zhang, Zilu and Gong, Zhengshuo and Zhou, Zhenhong and Wang, Kun and Sun, Li and Liu, Yang and Su, Sen},
  title={Resource Consumption Threats in Large Language Models},
  journal={arXiv:2603.16068},
  year={2026}
}
```

---

## 3. 中文摘要翻译

> 在有限且昂贵的计算基础设施条件下，资源效率是大型语言模型（LLM）的核心需求。高效的LLM能够为服务提供商提升吞吐量，同时为用户降低延迟和API成本。然而，最新的资源消耗威胁通过诱导过度生成来降低模型效率，损害服务可用性和经济可持续性。本综述对LLM资源消耗威胁进行了系统性综述。我们通过明确界定研究范围、审视从威胁诱导到机制理解再到缓解策略的完整流程，进一步建立了该新兴领域的统一视图。我们的目标是澄清这一新兴领域的问题图景，从而为威胁的刻画和缓解奠定更清晰的基础。

---

## 4. 研究背景

### 4.1 LLM部署的资源挑战

大型语言模型在有限且昂贵的计算基础设施上运行，使得资源效率成为实际部署中的关键要求。高效的资源使用为服务提供商提升了吞吐量，同时也为用户降低了API成本。因此，提升计算效率一直是跨LLM、推理型LLM（RLLM）、多模态LLM（MLLM）和基于LLM的智能体环境的研究热点。

### 4.2 资源消耗攻击的兴起

然而，仅靠优化并不能解决这一威胁，因为许多对抗性资源消耗攻击仍然威胁着LLM的可用性和可持续性。资源消耗攻击旨在诱导LLM产生不成比例的计算开销。近期研究表明，此类攻击已成为重要的安全风险。与直接诱导有害输出或提取隐私信息不同，这些攻击触发过度且不必要的生成，降低模型吞吐量、膨胀运营成本，并对共享服务资源造成过度压力。

### 4.3 典型案例：DeepSeek-R1事件

2016年1月26日，DeepSeek-R1的发布吸引了大量流量，但其链式思维推理的计算成本被低估，导致可用算力饱和并引发服务中断。这一案例充分说明了供给侧风险——包括吞吐量下降和运营成本增加。更广泛地，这种压力也可能以更高延迟、不稳定可用性和增加使用成本的形式传导给用户。

### 4.4 研究空白

虽然相关研究已开始出现在不同模型设置中，但该领域仍因术语不一致和威胁假设差异而碎片化。因此，资源消耗攻击的范畴和核心研究问题尚未得到充分澄清。

---

## 5. 核心贡献

本文的三项核心贡献：

1. **全面综述**：提供了资源消耗威胁领域最新进展的全面概述
2. **统一分类法**：引入了统一分类法，将资源消耗风险组织为两个代表性机制——过度思考（Overthinking）和无界漂移（Unbounded Drift），澄清了这一安全问题的范畴
3. **开放挑战分析**：分析了这个新兴领域的开放挑战并展望了未来研究方向

---

## 6. 研究方法

### 6.1 统一视图框架

本文建立了一个统一视图，将资源消耗威胁按其效应进行分类。根据两个标准区分不同攻击形式：
- 扩展生成是否仍与原始任务目标对齐
- 生成过程是否保持在可控的终止路径上

### 6.2 分类体系

#### 过度思考（Overthinking）

指过度生成仍保持任务对齐、保留正常停止行为，但因冗长、重复推理或过度详细描述而产生不必要成本的机制。其持续主要由与任务相关但低效用的阐述维持。

#### 无界漂移（Unbounded Drift）

指过度生成中，解码轨迹不再可靠地受原始任务或正常收敛动态支配。典型表现为重复循环、递归自扩展或自强化交互链，削弱语义控制、扰乱及时终止，或两者兼有。

### 6.3 分类维度

该分类并非仅基于输出长度。某些情况可能从过度思考演变为漂移，在这种情况下，我们按主导持续机制对其进行分类。

---

## 7. 实验设置

### 7.1 综述覆盖范围

本文系统性地综述了LLM资源消耗威胁，覆盖了从威胁诱导到机制理解再到缓解的完整流程：

- **早期攻击形式**：包括Sloth（梯度优化诱导DNN进入最计算密集路径）、Sponge Examples（扰动神经激活以大幅增加能耗）
- **LLM中的攻击面**：包括Sponge Poisoning（训练时后门诱导持续输出延长）、Crabs（通过树结构查询的语义扩展增加输出长度）、ThinkTrap（低维子空间优化诱导过度生成）、BitHydra（位翻转推理成本攻击）
- **推理LLM中的攻击面**：包括BadReasoner、BadThink（后门触发器）、基于上下文的减速攻击
- **多模态LLM中的攻击面**：包括VLMInferSlow、EO-VLM、LingoLoop、RECITE
- **智能体系统中的攻击面**：包括LeechHijack（注入辅助工作负载）、CORBA（多智能体自复制提示传播）

### 7.2 评估维度

综述评估了多个维度的资源消耗威胁：
- 计算开销（能耗、延迟、吞吐量）
- 服务可用性影响
- 经济可持续性影响
- 对不同模型架构的适用性（LLM、RLLM、MLLM、Agent）

---

## 8. 实验结果（综述发现）

### 8.1 威胁态势概览

资源消耗威胁已扩展到多个层面：
- 从推理时扰动到训练时后门
- 从单模态到多模态
- 从单模型到多智能体系统

### 8.2 关键发现

#### Overthinking类攻击

- Sponge Poisoning：通过训练时后门诱导持续输出延长和资源耗尽
- Crabs：通过树结构查询的语义扩展有效增加输出长度
- ThinkTrap：将离散token映射到连续嵌入空间，在低维子空间中进行优化以诱导黑盒访问下的过度生成
- BitHydra：位级权重操控影响硬件相关效率
- RepetitionCurse：MoE中不平衡的专家路由诱导重复失败

#### Unbounded Drift类攻击

- Fixed points和Attention sinks：利用固有解码动力学使重复轨迹更易持续
- LoopLLM：通过熵搜索诱导重复生成循环
- GCG、Engorgio、LLMEffiChecker：通过操控关键token干扰终止
- LingoLoop：将模型困在语言约束的视觉描述中
- RECITE：诱导重复视觉召回，驱动视觉-语言交互进入自强化解码循环

#### 智能体系统攻击

- LeechHijack：将辅助工作负载注入智能体推理循环， covertly steering it to perform attacker-specified computation
- CORBA：在多智能体系统中传播自复制提示，诱导递归交互浪费计算资源
- 计算机使用智能体（如OpenClaw、Cloud Code）：可能生成无明确终止条件的持久后台进程

### 8.3 跨领域影响

资源消耗风险已扩展到自动驾驶（CP-FREEZER、SlowLiDAR）、边缘设备、协同感知等多个领域。

---

## 9. 策略示例

### 9.1 Overthinking策略示例

| 攻击名称 | 机制 | 目标模型 |
|----------|------|----------|
| Sponge Poisoning | 训练时后门 | LLM |
| Crabs | 树结构查询语义扩展 | LLM |
| ThinkTrap | 低维子空间优化 | 黑盒LLM |
| BitHydra | 位翻转权重操控 | LLM硬件层 |
| BadReasoner/BadThink | 后门触发器 | RLLM |
| VLMInferSlow | 视觉推理减速 | MLLM |

### 9.2 Unbounded Drift策略示例

| 攻击名称 | 机制 | 目标模型 |
|----------|------|----------|
| LoopLLM | 熵搜索诱导重复循环 | LLM |
| GCG | 关键token干扰终止 | LLM |
| LingoLoop | 语言约束视觉描述陷阱 | MLLM |
| RECITE | 重复视觉召回 | MLLM |
| Fixed points | 固有解码动力学利用 | LLM |

### 9.3 智能体系统攻击示例

| 攻击名称 | 机制 | 目标 |
|----------|------|------|
| LeechHijack | 注入辅助工作负载 | 单智能体 |
| CORBA | 多智能体自复制提示传播 | 多智能体系统 |
| 计算机使用智能体攻击 | 持久后台进程生成 | 计算机使用智能体 |

---

## 10. 攻击流程

### 10.1 资源消耗攻击的统一流程

```
威胁诱导 → 机制理解 → 缓解策略
```

### 10.2 攻击阶段详解

#### 阶段1：威胁诱导

**早期攻击形式**：
- Sloth Hong：梯度优化诱导DNN进入最计算密集路径
- Sponge Examples：扰动神经激活破坏硬件级执行，增加能耗

**扩展到LLM**：
- 推理时扰动（如Token级攻击）
- 训练时后门（如Sponge Poisoning）

#### 阶段2：机制分析

**Overthinking机制**：
- 概率级陷阱：模型持续生成低效用但与任务相关的输出
- 语义扩展：通过查询扩展诱导更长的响应
- 参数级操控：位级权重修改影响硬件效率

**Unbounded Drift机制**：
- 重复循环：熵驱动搜索诱导重复模式
- 终止破坏：关键Token干扰正常停止
- 自强化循环：视觉-语言交互进入非终止状态

#### 阶段3：缓解策略

综述提到需要建立统一视图来指导缓解策略开发，但具体缓解方法在本文中未详细展开（见第4节机制分析部分）。

---

## 11. 消融实验

（注：本综述为调研类文章，不包含传统意义上的消融实验。但综述系统性地分析了不同攻击类别的机制和效果，可视为"概念消融"分析。）

### 11.1 攻击面层级分析

| 层级 | Overthinking | Unbounded Drift |
|------|--------------|------------------|
| **语义层** | Crabs（查询扩展） | LoopLLM（熵搜索） |
| **参数层** | Sponge Poisoning | GCG（Token干扰） |
| **硬件层** | BitHydra | Fixed points |
| **系统层** | ThinkTrap | CORBA |

### 11.2 模型类型适用性

| 模型类型 | 主要Overthinking攻击 | 主要Unbounded Drift攻击 |
|----------|---------------------|------------------------|
| LLM | Crabs, ThinkTrap, BitHydra | LoopLLM, GCG, Fixed points |
| RLLM | BadReasoner, BadThink | RECUR（重复反思循环） |
| MLLM | VLMInferSlow, EO-VLM | LingoLoop, RECITE |
| Agent | LeechHijack | CORBA |

---

## 12. 局限性

### 12.1 综述范围局限

1. **机制分析不完整**：过度思考的机制分析仍然有限，因为过度思考通常保持任务相关，可能表现为正常生成的极端扩展，使其因果边界更难隔离，现有研究仅提供部分线索而非成熟的机制分类

2. **缓解策略尚未完善**：综述主要关注威胁诱导和机制理解，关于缓解策略的内容相对较少

### 12.2 研究空白

1. **缺乏统一的评估基准**：不同研究的评估标准和指标不一致，难以进行横向比较

2. **对新型模型的覆盖不足**：随着LLM的快速发展，新型攻击面可能不断出现

3. **实用缓解方案欠缺**：综述指出了问题但未提供充分的实践指导

### 12.3 术语和分类不一致

该领域仍因术语不一致和威胁假设差异而碎片化，导致：
- 相同攻击被不同研究者以不同名称发表
- 分类标准不统一，难以系统比较
- 威胁假设差异导致防御策略难以泛化

---

## 13. 伦理声明

### 13.1 论文伦理说明

本文为系统性综述论文，聚焦于对现有研究的分类和分析，而非提出新型攻击方法。

### 13.2 潜在社会影响

资源消耗威胁对LLM生态系统产生系统性安全影响：

**供给侧影响**：
- 降低服务吞吐量
- 增加运营成本
- 可能导致服务中断（如DeepSeek-R1案例）

**用户侧影响**：
- 更高延迟
- 可用性不稳定
- API成本增加

### 13.3 研究价值

通过系统性地梳理资源消耗威胁的分类和机制，本文为：
- 研究人员提供了清晰的问题图景
- 从业者提供了威胁评估参考
- 后续研究提供了缓解策略开发的基础

---

## 14. 参考文献

### 主要引用论文

1. Shumailov et al. (2021) - Sponge Examples: 首个资源消耗攻击工作
2. Hong et al. (2020) - Sloth: 梯度优化诱导DNN计算成本增加
3. Chen et al. (2021) - TranSlowDown: NMT中的资源消耗攻击
4. Chen et al. (2022) - NMTSloth: 延迟EOS token诱导最大长度输出
5. Cinà et al. (2025) - Sponge Poisoning in LLM: 训练时后门诱导输出延长
6. Zhang et al. (2025) - Crabs: 树结构查询语义扩展攻击
7. Li et al. (2025) - ThinkTrap: 低维子空间优化诱导过度生成
8. Yan et al. (2025) - BitHydra: 位翻转推理成本攻击
9. Huang et al. (2025) - RepetitionCurse: MoE专家路由不平衡诱导重复失败
10. Hammouri et al. (2025) - Fixed points: 固有解码动力学利用
11. Yona et al. (2025) - Attention sinks: 重复轨迹更容易持续
12. Li et al. (2025) - LoopLLM: 熵搜索诱导重复生成循环
13. Geiping et al. (2024) - GCG: 通用可迁移对抗攻击
14. Dong et al. (2024) - Engorgio: Token干扰终止攻击
15. Feng et al. (2024) - LLMEffiChecker: 终止机制干扰
16. Fu et al. (2025) - LingoLoop: 语言约束视觉描述陷阱
17. Gao et al. (2025) - RECITE: 重复视觉召回攻击
18. Zhang et al. (2025) - LeechHijack: 智能体工作负载注入
19. Zhou et al. (2025) - CORBA: 多智能体自复制提示传播
20. Wang et al. (2023) - Sponge攻击与边缘硬件

### 相关领域工作

21. Vaswani et al. (2017) - Transformer架构
22. Wei et al. (2022) - Chain-of-thought reasoning
23. Alayrac et al. (2022) - 多模态LLM
24. Yao et al. (2022) - LLM智能体环境

---

## 附录说明

本文还有以下补充材料：
- **附录A**：相关证据补充
- **附录D**：影响详细讨论
- **附录G**：机制分析技术细节

---

*本文档由 LLM Safety 论文阅读助手自动生成*
*论文来源：arXiv:2603.16068*
*生成日期：2026-05-21*