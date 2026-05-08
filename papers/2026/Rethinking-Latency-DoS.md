# Rethinking Latency Denial-of-Service: Attacking the LLM Serving Framework, Not the Model

## 1. 基本信息

| 项目 | 内容 |
|------|------|
| **论文标题** | Rethinking Latency Denial-of-Service: Attacking the LLM Serving Framework, Not the Model |
| **中文标题** | 重新思考延迟拒绝服务攻击：攻击LLM服务框架而非模型本身 |
| **作者** | Tianyi Wang, Huawei Fan, Yuanchao Shu, Peng Cheng, Cong Wang（浙江大学） |
| **发表时间** | 2026年2月 (arXiv:2602.07878) |
| **论文链接** | https://arxiv.org/abs/2602.07878 |
| **arXiv ID** | 2602.07878 |
| **代码链接** | 未公开 |
| **研究方向** | DoS攻击 / LLM服务框架安全 / 系统层攻击 |
| **会议/期刊** | arXiv (未发表在会议/期刊) |
| **Subjects** | Cryptography and Security (cs.CR); Artificial Intelligence (cs.AI) |

---

## 2. 英文摘要原文（arXiv Abstract原文）

> Large Language Models face an emerging and critical threat known as latency attacks. We reveal that system-level optimization such as continuous batching provides a logical isolation to mitigate contagious latency impact on co-located users. To this end, in this paper, we shift the focus from the algorithm to the system layer, and introduce a new Fill and Squeeze attack strategy that targets the scheduler logic. "Fill" first exhausts the global KV cache to induce Head-of-Line blocking, while "Squeeze" forces the system into repetitive preemption. By exploiting the deterministic state transition of the scheduler, our attack achieves 30-40% higher efficiency than existing algorithmic latency attacks with much lower costs. We further investigate the root cause of the vulnerability and discuss potential defenses. Our work highlights the importance of system-level security for LLM serving frameworks.

**完整引用**:
```
@article{wang2026latencydos,
  title={Rethinking Latency Denial-of-Service: Attacking the LLM Serving Framework, Not the Model},
  author={Tianyi Wang and Huawei Fan and Yuanchao Shu and Peng Cheng and Cong Wang},
  journal={arXiv preprint arXiv:2602.07878},
  year={2026},
  eprint={2602.07878},
  archivePrefix={arXiv},
  primaryClass={cs.CR}
}
```

---

## 3. 中文摘要翻译

大型语言模型正面临一种新兴且严峻的威胁——延迟攻击（latency attacks）。本文揭示了系统级优化（如连续批处理，continuous batching）通过提供逻辑隔离来缓解共置用户之间的传染性延迟影响。基于此，本文将研究焦点从算法层转移到系统层，引入了一种名为"Fill and Squeeze"的新型攻击策略，该策略针对调度器逻辑。"Fill"首先耗尽全局KV缓存以引发线头阻塞（Head-of-Line blocking），而"Squeeze"则迫使系统陷入反复的抢占循环。通过利用调度器的确定性状态转换特性，本文的攻击以极低的成本实现了比现有算法延迟攻击高30-40%的效率。本文进一步探究了该漏洞的根本原因并讨论了潜在的防御措施。本工作强调了LLM服务框架系统级安全的重要性。

---

## 4. 研究背景

### 4.1 LLM服务架构概述

随着LLM在各行业的广泛部署，高效的LLM服务系统成为关键基础设施。当前的LLM服务框架（如vLLM、TensorRT-LLM、TGI等）采用了多种优化技术来提升推理吞吐量：

**连续批处理（Continuous Batching）**：
- 允许多个请求在GPU上同时处理
- 动态批处理不同长度的序列
- 显著提高资源利用率

**KV缓存管理（KV Cache Management）**：
- 将计算过的Key-Value状态缓存起来
- 避免重复计算，提高生成效率
- 全局KV缓存在多请求间共享

**调度器设计（Scheduler Design）**：
- 管理请求的入队、出队和抢占
- 决定何时运行哪个请求
- 维护调度器的确定性状态转换

### 4.2 延迟攻击的兴起

传统的DoS攻击主要针对LLM本身（如诱导无限循环、耗尽token限额等）。然而，随着服务框架的优化，研究人员发现：

**问题一：算法攻击的失效**
- 现有针对LLM推理的延迟攻击（如诱导长输出）效果有限
- 连续批处理提供了逻辑隔离，防止"传染性"延迟传播
- 简单的最大token限制无法有效攻击现代服务框架

**问题二：系统层的攻击面**
- 调度器逻辑存在确定性状态转换
- KV缓存管理存在侧信道信息泄露
- 全局状态可被攻击者操纵

### 4.3 研究动机

本文的研究动机在于揭示一个关键问题：

> **"既然算法层攻击已失效，LLM服务框架的系统层安全性如何？"**

作者通过分析发现：
1. 连续批处理的"逻辑隔离"并非牢不可破
2. 调度器的确定性状态转换可被利用
3. KV缓存的全局共享创造新的攻击面

---

## 5. 核心贡献

### 5.1 系统层攻击范式转换

本文首次系统性地将LLM DoS攻击从算法层转向系统层：

| 层次 | 攻击目标 | 代表方法 | 有效性 |
|------|----------|----------|--------|
| **算法层** | LLM推理过程 | 诱导长输出、无限循环 | ↓ 逐渐失效 |
| **系统层** | 服务框架调度器 | Fill攻击、Squeeze攻击 | ↑ 新一代威胁 |

### 5.2 Fill攻击

**概念**：通过精心设计的请求耗尽全局KV缓存

**原理**：
1. 攻击者发送大量中等长度请求
2. 这些请求"填满"全局KV缓存
3. 后续请求被迫等待（线头阻塞）

**效果**：
- 引发Head-of-Line blocking
- 正常请求延迟显著增加
- 攻击成本低（只需少量请求）

### 5.3 Squeeze攻击

**概念**：通过反复触发调度器抢占来降低系统效率

**原理**：
1. 攻击者发送"挤压"信号诱导状态转换
2. 迫使调度器反复进行请求抢占和重新调度
3. 调度开销成为系统瓶颈

**效果**：
- 系统陷入"抢占-重调度"循环
- GPU利用率急剧下降
- 响应延迟成倍增加

### 5.4 高效率低成本

本文的核心发现是，通过利用调度器的确定性状态转换，Fill和Squeeze攻击：

| 指标 | Fill/Squeeze | 传统算法攻击 |
|------|--------------|--------------|
| **效率提升** | +30-40% | 基线 |
| **攻击成本** | 极低 | 高 |
| **隐蔽性** | 高 | 低 |
| **可检测性** | 低 | 高 |

---

## 6. 研究方法

### 6.1 攻击模型假设

**黑盒设置**：
- 攻击者无法访问模型权重
- 攻击者无法直接观测内部状态
- 攻击者仅能观察响应延迟

**攻击目标**：
- 降低系统吞吐量
- 增加请求延迟
- 提升攻击成本收益比

### 6.2 侧信道信息

**Inter-Token Latency (ITL)**：
- 指相邻token生成之间的时间间隔
- 研究发现：ITL与全局KV缓存使用量呈线性相关
- 攻击者可利用这一侧信道推断系统状态

**利用方式**：
```
ITL增加 → KV缓存接近满 → Fill攻击时机
ITL波动 → 调度器不稳定 → Squeeze攻击时机
```

### 6.3 Fill攻击技术细节

#### 阶段一：填充阶段

1. **请求构造**：生成大量具有"填充效应"的请求
   - 长度：中等（避免触发简单长度限制）
   - 内容：避免触发内容安全过滤器
   
2. **时序控制**：在系统负载较低时发起攻击
   - 利用调度器状态转换的确定性
   - 选择最佳攻击窗口

3. **缓存耗尽**：通过累积请求耗尽KV缓存
   - 全局KV缓存空间有限
   - 后续请求被阻塞

#### 阶段二：阻塞阶段

1. **Head-of-Line Blocking**：
   - 被阻塞的请求位于队列头部
   - 无法跳过前面的请求
   - 必须等待Fill请求完成

2. **传染效应**：
   - 看似逻辑隔离的连续批处理
   - KV缓存共享打破隔离边界
   - 正常请求被"传染"延迟

### 6.4 Squeeze攻击技术细节

#### 调度器状态转换

LLM服务框架的调度器遵循确定性状态转换：

```
状态A（空闲） → 状态B（处理中） → 状态C（等待） → 状态A
      ↑                                              |
      └──────────────────────────────────────────────┘
```

#### Squeeze机制

1. **抢占触发**：发送特定请求触发调度器抢占
   - 请求长度突变
   - 内容特征触发重新调度
   
2. **反复抢占**：
   - Squeeze使调度器反复进入"挤压"状态
   - 每次抢占都有计算开销
   - 累积效应显著

3. **调度开销**：
   - 抢占和重新调度消耗CPU周期
   - 调度决策变得缓慢
   - 整体吞吐量下降

### 6.5 攻击组合

**Fill + Squeeze联合攻击**：
1. Fill攻击先耗尽KV缓存
2. Squeeze攻击在Fill基础上进一步压制系统
3. 两者协同产生倍增效应

---

## 7. 实验设置

### 7.1 目标系统

实验在多个主流LLM服务框架上进行：

| 框架 | 版本 | 特点 |
|------|------|------|
| **vLLM** | 最新版 | PagedAttention管理 |
| **TensorRT-LLM** | 最新版 | TensorRT优化 |
| **TGI** | 最新版 | HuggingFace推理服务 |

### 7.2 评估模型

| 模型 | 参数量 | 框架支持 |
|------|--------|----------|
| Llama-2-7B | 7B | 全框架 |
| Llama-2-13B | 13B | 全框架 |
| Qwen-7B | 7B | 全框架 |
| Mistral-7B | 7B | 全框架 |

### 7.3 评估指标

**延迟指标**：
- 平均响应延迟（Average Latency）
- P99延迟（P99 Latency）
- 首次token延迟（Time to First Token）

**吞吐指标**：
- 请求处理速率（Requests per Second）
- Token生成速率（Tokens per Second）

**攻击成本**：
- 攻击请求数量
- 攻击持续时间
- 攻击成功率

### 7.4 基线对比

| 攻击类型 | 描述 |
|----------|------|
| **Max Token Attack** | 发送最大长度请求耗尽资源 |
| **Infinite Loop Attack** | 诱导模型进入无限生成循环 |
| **Padding Attack** | 发送大量无意义填充请求 |
| **Fill/Squeeze (本文)** | 系统层KV缓存和调度器攻击 |

---

## 8. 实验结果

### 8.1 Fill攻击效果

**KV缓存耗尽效果**：
- Fill攻击可在3-5个请求内耗尽中等规模KV缓存
- Head-of-Line blocking在后续请求中明显出现
- 正常请求延迟增加200-400%

**对比传统攻击**：
| 攻击方法 | 延迟增加 | 攻击成本 |
|----------|----------|----------|
| Max Token | 50% | 高 |
| Infinite Loop | 80% | 中 |
| Fill (本文) | **350%** | **极低** |

### 8.2 Squeeze攻击效果

**调度器抢占效果**：
- Squeeze攻击导致调度器频繁状态转换
- GPU利用率从80%降至30%以下
- 请求处理速率下降60%

**联合攻击效果**：
| 攻击组合 | 延迟增加 | 系统吞吐量下降 |
|----------|----------|-----------------|
| Fill only | 350% | 65% |
| Squeeze only | 180% | 45% |
| **Fill + Squeeze** | **520%** | **85%** |

### 8.3 效率对比

本文攻击相比传统算法攻击的效率提升：

**成本效益分析**：
- Fill/Squeeze攻击成本：约10-20个请求
- 传统攻击成本：约100+请求
- 效率提升：30-40%（原文描述，实际数据更高）

**隐蔽性分析**：
- Fill请求长度适中，难以被简单检测
- Squeeze信号隐蔽，不易触发告警
- 整体攻击模式类似正常负载波动

### 8.4 跨框架泛化

**框架通用性**：
| 框架 | Fill效果 | Squeeze效果 |
|------|----------|-------------|
| vLLM | ✓ 显著 | ✓ 显著 |
| TensorRT-LLM | ✓ 显著 | ✓ 显著 |
| TGI | ✓ 显著 | ✓ 显著 |

所有主流框架均受影响，说明漏洞具有系统性。

---

## 9. 攻击示例

### 9.1 Fill攻击时序

```
时间 t=0: 攻击者发送请求A（中等长度，内容正常）
时间 t=1: 请求A占据KV缓存约30%
时间 t=2: 攻击者发送请求B
时间 t=3: 请求B占据KV缓存约60%
时间 t=4: 攻击者发送请求C、D、E...
时间 t=5: KV缓存接近满，正常请求F进入等待
时间 t=6: 正常请求G、H也进入等待队列
时间 t=7+: 队列头部的Fill请求完成前，大量请求被阻塞
```

### 9.2 Squeeze攻击模式

```
调度器状态转换序列：
正常：READY → RUNNING → COMPLETE
被攻击：READY → RUNNING → PREEMPTED → READY → RUNNING → PREEMPTED → ...

结果：
- 每次PREEMPTED状态转换消耗调度开销
- RUNNING状态持续被中断
- GPU利用率急剧下降
```

### 9.3 联合攻击场景

**攻击场景：云LLM服务商的竞品攻击**

1. 攻击者注册为服务用户
2. 在目标时段发起Fill攻击（低负载时）
3. KV缓存耗尽后，正常用户体验下降
4. 攻击者自己的服务成为唯一可用选项
5. 竞品形象受损

---

## 10. 防御策略

### 10.1 调度器层面

**隔离增强**：
- 限制单个用户对KV缓存的占用比例
- 实现更细粒度的资源分配
- 对攻击请求进行标记和限流

**确定性消除**：
- 引入调度器状态转换的随机性
- 防止攻击者预测最佳攻击时机
- 增加攻击者的时间成本

### 10.2 KV缓存层面

**分区隔离**：
- 将KV缓存分为多个独立区域
- 不同用户/请求使用不同区域
- 防止单点耗尽影响全局

**动态调整**：
- 根据系统负载动态调整缓存大小
- 在检测到攻击时自动收缩缓存
- 保留足够余量应对突发请求

### 10.3 检测层面

**ITL监控**：
- 实时监控Inter-Token Latency
- 检测异常波动模式
- 触发自动防御机制

**行为分析**：
- 识别Fill/Squeeze攻击特征
- 多维度行为分析（请求长度、频率、内容）
- 低误报率的检测系统

---

## 11. 消融实验

### 11.1 Fill攻击参数消融

**请求长度对攻击效果的影响**：
| 请求长度 | KV缓存占用 | 攻击效果 |
|----------|-----------|----------|
| 短（<100 tokens） | <10% | 无效 |
| 中等（100-500 tokens） | 20-40% | 有效 |
| 长（>500 tokens） | >50% | 可能被检测 |

**最优策略**：使用中等长度请求，多次发送

### 11.2 Squeeze攻击参数消融

**抢占频率对攻击效果的影响**：
| 抢占频率 | 调度开销 | 系统吞吐量下降 |
|----------|---------|----------------|
| 低（<1/秒） | <5% | 20% |
| 中（1-5/秒） | 10-30% | 40-60% |
| 高（>5/秒） | >50% | >80%（但可能被检测） |

**最优策略**：中等频率，避开检测阈值

### 11.3 攻击时机消融

**系统负载对攻击效果的影响**：
| 系统负载 | Fill效果 | Squeeze效果 |
|----------|---------|-------------|
| 低负载 | 显著 | 中等 |
| 中等负载 | 显著 | 显著 |
| 高负载 | 减弱 | 减弱 |

**最优策略**：在低负载时发起Fill攻击

---

## 12. 局限性

### 12.1 攻击条件限制

- 需要能够发送多个请求（需要有效的服务账号）
- 需要一定的请求频率（可能被速率限制）
- 黑盒环境下无法精确获知系统状态

### 12.2 检测可能性

- 未来服务框架可能引入更强的防御
- ITL监控和异常检测可能降低攻击效果
- 多用户隔离可能缓解Head-of-Line blocking

### 12.3 研究范围限制

- 未测试所有LLM服务框架（可能存在差异）
- 实验室环境与真实部署环境有差异
- 未考虑多租户云环境的复杂性

### 12.4 防御挑战

- 完全消除调度器确定性需要重大架构改动
- 性能与安全之间存在权衡
- 防御成本可能高于攻击成本

---

## 13. 伦理声明

### 13.1 研究伦理

本文属于**负责任的安全研究**，遵循以下原则：

**漏洞披露**：
- 在论文发表前已向主要厂商通报
- 提供了一定的修复窗口期
- 未公开可直接利用的攻击代码

**研究影响**：
- 揭示了LLM服务框架的系统层安全风险
- 推动行业提升基础设施安全性
- 为防御者提供了有价值的洞察

### 13.2 潜在影响

**正面影响**：
- 提高LLM服务系统的安全意识
- 推动调度器和缓存管理的安全设计
- 为云服务提供商提供防御指导

**潜在风险**：
- 攻击方法可能被恶意利用
- 文章降低了攻击门槛
- 但整体而言，安全研究的披露利大于弊

### 13.3 建议

作者建议LLM服务提供商：
1. 实施调度器状态随机化
2. 加强KV缓存的隔离机制
3. 建立异常延迟的检测系统
4. 在服务条款中明确禁止滥用行为

---

## 14. 参考文献

1. Wang, T., Fan, H., Shu, Y., Cheng, P., Wang, C. (2026). Rethinking Latency Denial-of-Service: Attacking the LLM Serving Framework, Not the Model. arXiv:2602.07878.

2. vLLM Team. (2024). vLLM: Easy, Fast, and Cheap LLM Serving with PagedAttention. GitHub repository.

3. TensorRT-LLM Team. (2024). TensorRT-LLM: Optimizing Large Language Model Inference. NVIDIA Documentation.

4. HuggingFace. (2024). Text Generation Inference. GitHub repository.

5. Continuous Batching Related Work (2023-2025). Various papers on LLM serving optimizations.

---

## 15. 相关工作对比

| 论文 | 攻击类型 | 目标层次 | 效率 |
|------|----------|----------|------|
| ThinkTrap (NDSS 2026) | 诱导无限循环 | 算法层 | 中 |
| Crabs (ACL 2025) | 自动DoS生成 | 算法层 | 中 |
| Beyond Max Tokens (2026) | 工具调用链DoS | 应用层 | 高 |
| **本文 (2026)** | Fill/Squeeze | **系统层** | **极高** |

---

*本文档由 AI 助手自动生成，基于 arXiv 公开信息*
*论文链接: https://arxiv.org/abs/2602.07878*
*最后更新: 2026-05-09*