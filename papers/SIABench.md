# SIABench: Evaluating LLMs for Security Incident Analysis

## 基本信息

- **论文标题**: Before You Hand Over the Wheel: Evaluating LLMs for Security Incident Analysis
- **作者**: Sourov Jajodia, Madeena Sultana, Suryadipta Majumdar, Adrian Taylor, Grant Vandenberghe
- **发表时间**: 2026年3月 (arXiv:2603.06422)
- **论文链接**: https://arxiv.org/abs/2603.06422
- **研究方向**: LLM安全评估 / 安全事件分析 / 网络安全
- **会议/期刊**: arXiv预印本

---

## 研究背景

### 安全事件分析(SIA)的挑战

安全事件分析(Security Incident Analysis, SIA)是安全运营中心(SOC)的核心职责，但面临诸多挑战：

1. **告警量巨大**: SOC需要处理海量的安全告警，分析师面临严重的告警疲劳
2. **数据源多样化**: 需要分析网络日志、内存转储、恶意软件样本等多种异构数据
3. **工具链复杂**: 需要熟练使用Wireshark、Volatility、Oledump等专业工具
4. **专业知识要求高**: 需要深入理解系统内部、恶意软件分析和网络协议
5. **动态演变**: 安全事件不断演变，需要多步骤、多方面的推理能力

### 现有问题

- 缺乏针对SIA任务的LLM系统评估研究
- 缺乏LLM可用的SIA数据集
- 缺乏评估最佳实践和标准
- 新模型快速发布，需要可扩展的评估框架

---

## 核心贡献

### 1. SIABench基准数据集

**首个专门针对SIA任务评估LLM的基准数据集**，包含两个主要部分：

#### Part I: 安全事件分析任务 (SIA Tasks)
- **25个场景**，涵盖229个调查问题
- **4大类别**:
  - 网络取证 (Network Forensics): 8个场景，87个问题
  - 内存取证 (Memory Forensics): 7个场景，60个问题
  - 恶意软件分析 (Malware Analysis): 6个场景，46个问题
  - 其他 (Miscellaneous): 4个场景，36个问题
- **3个难度级别**: Easy, Medium, Hard
- **基于MITRE ATT&CK框架**的战术标注

#### Part II: 告警分类任务 (Alert Triaging)
- **135个告警场景**
- 包含真阳性(TP)和假阳性(FP)样本
- 基于TII-SSRC-23和CIC-IDS2017数据集构建

### 2. SIABench Agent

**自动化SIA任务执行代理**，具备以下能力：
- 动态访问工具和分析环境
- 多步骤推理处理复杂多目标场景
- 选择性过滤相关信息进行长期规划
- 支持11种主流LLM，可扩展至新模型

### 3. 系统性评估

- 评估了11种主流LLM（4种开源 + 7种闭源）
- 揭示了LLM在SIA任务中的能力边界
- 验证了模型在训练截止日期后发布的实际SIA任务上的表现

---

## 研究方法

### 数据集构建流程

```
数据选择 → 预处理 → 真实世界对齐 → 任务生成与验证
```

#### 1. 数据选择
- 来源: CyberDefenders, Blue Team Labs Online, TryHackMe
- 场景类型: 勒索软件攻击、Web服务器入侵、钓鱼驱动恶意软件感染等

#### 2. 预处理策略（减少数据污染）
- **内容改写**: 使用Gemini 1.5 Flash API改写场景描述
- **标识符中性化**: 移除公司名称、用户名等特定标识符
- **工件标准化**: 将文件名改为通用模式（如`capture.pcap`）

#### 3. 真实世界对齐（去偏见策略）
- **开放式重构**: 将事实性问题改为分析性提示
  - 原问题: "What is the IP responsible for conducting the port scan activity?"
  - 改写后: "Is there any evidence of port scanning in the network traffic? If so, what is the IP address responsible for the scanning activity?"
- **假设移除**: 消除可能引导模型得出特定结论的关键词假设
- **数字中性化**: 不预设工件数量，让LLM自行确定
- **外部知识移除**: 排除需要外部知识或记忆事实的问题

#### 4. 人工专家验证
- 14名安全专业人员参与验证研究
- 去偏见评分: 3.35/4 (有经验分析师), 3.22/4 (经验有限分析师)
- 战术标签评分: 3.43/4 (有经验分析师), 3.49/4 (经验有限分析师)

### Agent设计

#### 三状态工作流

```
┌─────────────┐     ┌─────────────────────────────────────┐     ┌─────────────┐
│  Init State │ ──→ │       Incident Analysis State       │ ──→ │Solved State │
│   (初始化)   │     │  ┌─────────┐ ┌─────────┐ ┌────────┐ │     │  (完成)     │
└─────────────┘     │  │Investigation│ │Action  │ │Summarize│ │     └─────────────┘
                    │  │   Plan    │ │Execute│ │        │ │
                    │  └─────────┘ └─────────┘ └────────┘ │
                    └─────────────────────────────────────┘
```

#### 核心模块

1. **事件调查计划 (Incident Investigation Plan)**
   - 使用ReAct (Reason+Act)框架
   - 迭代循环: Thought → Action → Observation

2. **动作执行 (Action Execute)**
   - Open/Close Shell: 创建隔离环境
   - Execute Tool: 执行安全工具（Tshark, Volatility等）
   - State Change: 决定何时结束或跳过问题

3. **摘要模块 (Summarize)**
   - 提取关键安全洞察(KSI)
   - 分段处理长输出（超过64k token）
   - 防止上下文长度耗尽和幻觉

---

## 实验设置

### 评估模型

| 类型 | 模型 |
|------|------|
| **闭源模型** | Claude-4.5-Sonnet, Claude-3.5-Sonnet, GPT-5, GPT-4o, GPT-4o-mini, o3-mini, Gemini-1.5-pro |
| **开源模型** | DeepSeek-Reasoner, Llama-3.1-8B, Llama-3.1-70B, Llama-3.1-405B |

### 实验环境
- Kali Linux虚拟机
- 16GB RAM, 12th Gen Intel Core i7
- 512GB虚拟磁盘

### 评估指标
- **FS (Fully Solved)**: 完全解决的场景数量
- **PS (Partially Solved)**: 部分解决的平均百分比

---

## 实验结果

### 总体性能 (RQ1)

| 模型 | 完全解决场景(FS) | 部分解决率(PS) |
|------|-----------------|----------------|
| Claude-4.5-Sonnet | 8/25 | 81.70% |
| GPT-5 | 5/25 | 80.70% |
| Claude-3.5-Sonnet | 4/25 | 71.03% |
| GPT-4o | 3/25 | 57.93% |
| DeepSeek-Reasoner | 1/25 | 49.33% |

**关键发现**:
- 即使是最佳模型(Claude-4.5-Sonnet)也只能完全解决8/25个场景
- 闭源模型显著优于开源模型
- 模型在18个月内持续进步，但在复杂SIA任务上仍有很大提升空间

### 按任务类别分析

#### 内存取证
- Claude-4.5-Sonnet表现最佳 (Easy: 86.74%)
- 使用Volatility等工具分析内存转储
- 小模型(Llama-3.1-8B/70B)在所有难度级别上表现都很差

#### 恶意软件分析
- GPT-5在Easy级别表现最佳 (91.67%)
- 涉及PDF、XML、二进制文件等恶意文件分析

#### 网络取证
- Claude-4.5-Sonnet在Hard级别达到100%
- 分析PCAP文件、检测端口扫描等

### 战术级别分析 (RQ2)

基于MITRE ATT&CK框架的分析显示：
- LLM在**侦察(Reconnaissance)**和**初始访问(Initial Access)**战术上表现较好
- 在**防御规避(Defense Evasion)**和**凭证访问(Credential Access)**等复杂战术上表现较差

### 失败因素分析 (RQ3)

主要失败原因：
1. **工具使用错误**: 选择错误的工具或参数
2. **上下文长度限制**: 无法处理大量日志输出
3. **推理错误**: 错误解读分析结果
4. **过早放弃**: 在找到正确答案前放弃调查

### 消融实验 (RQ6)

#### 多状态 vs 单状态工作流
- 多状态工作流显著优于单状态设置
- 单状态容易导致模型过度关注一个问题而忽略其他问题

#### 摘要模块的影响
- 没有摘要模块时，GPT-4o无法完成11/25个场景
- Claude-3.5-Sonnet在没有摘要模块时无法完成7个场景

### 告警分类性能 (RQ7)

| 模型 | 准确率 |
|------|--------|
| Claude-4.5-Sonnet | 92.6% |
| GPT-5 | 90.4% |
| GPT-4o | 85.2% |

- 告警分类任务相对简单，所有模型表现都较好
- 区分真阳性和假阳性告警的能力较强

---

## 策略示例

### 去偏见策略示例

**原始问题（有偏见）**:
> "What's the invoked PowerShell script used by the attacker for dumping credentials?"

**改写后（去偏见）**:
> "Is there any evidence of credential dumping by the attacker? If so, is there any invoked script used by the attacker for dumping credentials?"

### Agent工作流示例

**场景**: 端口扫描攻击分析

**Step 1 - Thought**: 
> "I need to analyze the PCAP file to identify potential port scanning activity."

**Step 2 - Action**:
> Execute: `tshark -r capture.pcap -Y "tcp.flags.syn==1 and tcp.flags.ack==0"`

**Step 3 - Observation**:
> 发现从172.20.10.4到172.20.10.5的多个端口的重复连接尝试

**Step 4 - Summary**:
> 提取关键安全洞察(KSI): 源IP 172.20.10.4对目标IP 172.20.10.5进行了端口扫描

---

## 局限性

1. **数据集规模**: 25个SIA场景可能无法覆盖所有类型的安全事件
2. **公开数据限制**: 使用公开训练平台数据存在数据污染风险
3. **工具限制**: 主要关注CLI工具，未涵盖所有商业安全工具
4. **评估范围**: 仅评估了初级SOC分析师能力，未涉及高级分析任务
5. **静态场景**: 场景是静态的，真实世界事件是动态演变的

---

## 伦理声明

- 所有数据集均来自公开可用的安全训练平台
- 人工验证研究已获得人类研究伦理委员会(HREC)批准
- 数据集仅用于研究目的，不包含真实敏感信息
- 遵循负责任披露原则

---

## 结论与展望

### 主要结论

1. **LLM在SIA任务上仍有很大提升空间**: 即使是最佳模型也只能完全解决32%的场景
2. **闭源模型显著优于开源模型**: Claude-4.5-Sonnet和GPT-5领先
3. **复杂任务仍是挑战**: 涉及多步骤推理和工具链协调的任务难度较大
4. **Agent设计至关重要**: 多状态工作流和摘要模块显著提升性能

### 未来研究方向

1. 扩展数据集覆盖更多类型的安全事件
2. 探索多模态LLM在SIA中的应用
3. 研究人机协作模式，而非完全自动化
4. 开发针对SIA任务的专门微调方法
5. 建立实时评估机制，跟踪新模型发布

---

## 参考文献

```bibtex
@article{jajodia2026siabench,
  title={Before You Hand Over the Wheel: Evaluating LLMs for Security Incident Analysis},
  author={Jajodia, Sourov and Sultana, Madeena and Majumdar, Suryadipta and Taylor, Adrian and Vandenberghe, Grant},
  journal={arXiv preprint arXiv:2603.06422},
  year={2026}
}
```

### 相关论文

1. **TrustLLM** (Liu et al., 2024) - LLM可信度综合评估
2. **AgentDojo** (Debenedetti et al., 2024) - 动态提示注入攻击评估
3. **JailbreakBench** (Chao et al., 2024) - 越狱攻击开放鲁棒性基准
4. **CyBench** (2024) - LLM网络安全能力评估框架
5. **PentestGPT** (Deng et al., 2024) - 渗透测试自动化

---

*本笔记由LLM Safety论文阅读助手自动生成*
*生成时间: 2026-03-19*
