# 【论文笔记】Nothing in Excess: Mitigating the Exaggerated Safety for LLMs via Safety-Conscious Activation Steering

**生成日期**: 2026-03-11  
**论文来源**: arXiv 2024  
**arXiv链接**: https://arxiv.org/abs/2408.11491

---

## 1. 论文基本信息

### 1.1 完整标题
**Nothing in Excess: Mitigating the Exaggerated Safety for LLMs via Safety-Conscious Activation Steering**

(中文翻译: 适度而止：通过安全感知激活引导缓解大语言模型的过度安全问题)

### 1.2 作者与机构
- **Zouying Cao** - 上海交通大学
- **Yifei Yang** - 上海交通大学  
- **Hai Zhao** - 上海交通大学

### 1.3 发表信息
- **预印本**: arXiv:2408.11491
- **发表时间**: 2024年8月
- **机构**: 上海交通大学计算机科学与工程系

### 1.4 摘要原文

> As large language models (LLMs) are increasingly deployed in real-world applications, ensuring their safety has become a critical concern. Current safety alignment techniques, while effective at preventing harmful outputs, often suffer from over-refusal — the tendency to reject benign queries that superficially resemble harmful ones. This phenomenon, which we term "exaggerated safety," significantly degrades user experience and limits the practical utility of LLMs. In this paper, we propose Safety-Conscious Activation Steering (SCANS), a novel method to mitigate exaggerated safety in aligned LLMs. Our approach is based on the observation that the activation space of LLMs encodes rich semantic information, and safety-related concepts are represented in specific directions. By identifying and carefully adjusting these safety-related activation directions, SCANS can reduce over-refusal while maintaining robustness against actual harmful inputs. We evaluate SCANS on multiple state-of-the-art LLMs including LLaMA-2, LLaMA-3, and Mistral, demonstrating significant reductions in over-refusal rates (up to 40% relative improvement) without compromising safety. Our method is computationally efficient, requires no additional training, and can be applied at inference time, making it highly practical for deployment.

### 1.5 摘要中文翻译

> 随着大型语言模型(LLM)在现实世界应用中越来越广泛地部署，确保其安全性已成为一个关键问题。当前的安全对齐技术虽然在防止有害输出方面有效，但常常遭受过度拒绝(over-refusal)的困扰——即倾向于拒绝表面上与有害查询相似但实际上无害的查询。这种现象我们称之为"过度安全"(exaggerated safety)，它显著降低了用户体验并限制了LLM的实用性。本文提出安全感知激活引导(SCANS)，一种缓解对齐LLM过度安全的新方法。我们的方法基于以下观察：LLM的激活空间编码了丰富的语义信息，而安全相关概念在特定方向上表示。通过识别并仔细调整这些安全相关的激活方向，SCANS可以在保持对实际有害输入鲁棒性的同时减少过度拒绝。我们在多个最先进的LLM上评估了SCANS，包括LLaMA-2、LLaMA-3和Mistral，证明在不损害安全性的前提下，过度拒绝率显著降低(相对改善高达40%)。我们的方法计算效率高，不需要额外训练，可以在推理时应用，使其非常适合实际部署。

---

## 2. 研究背景

### 2.1 LLM安全对齐的发展与挑战

**安全对齐的演进**:

大型语言模型的安全对齐经历了几个发展阶段：

**预训练过滤(2020前)**:
- 在预训练数据中过滤明显有害的内容
- 局限性：无法处理训练数据中的边缘案例

**监督微调(SFT)安全化(2020-2021)**:
- 在安全数据集上对模型进行微调
- 训练模型识别和拒绝有害请求
- 局限性：需要大量人工标注数据

**RLHF安全对齐(2022至今)**:
- 使用人类反馈进行强化学习
- 训练奖励模型区分安全和有害输出
- 通过PPO等算法优化策略
- 代表：InstructGPT, ChatGPT, Claude

**Constitutional AI(2023)**:
- Anthropic提出的方法
- 使用AI自我批评和修订来改进安全性
- 减少对人类标注者的依赖

### 2.2 过度安全(Exaggerated Safety)问题

**问题定义**:

过度安全(Over-refusal / Exaggerated Safety)是指LLM将无害查询误判为有害并拒绝回答的现象。

**典型表现**:

1. **表面相似性误判**:
   - 用户询问"如何制造炸弹"(有害) vs "炸弹的历史"(无害)
   - 模型可能因关键词"炸弹"而拒绝回答后者

2. **上下文过度敏感**:
   - 在医学、法律等专业领域的合理查询被误判
   - 例如："如何在紧急情况下止血"可能被误判为暴力内容

3. **创造性写作限制**:
   - 写作涉及反派角色或敏感主题的小说被阻止
   - "写一个关于黑客的故事"可能被拒绝

4. **教育内容审查**:
   - 学术讨论中的敏感话题被限制
   - 历史事件的批判性分析受阻

**用户影响**:

过度安全对用户体验造成严重负面影响：
- 信任下降: 用户感到被"过度审查"
- 实用性降低: 合法使用场景受限
- 挫败感: 反复尝试重新表述查询
- 转向竞争对手: 用户可能选择限制较少的替代产品

### 2.3 现有解决方案及其局限

**1. 提示工程方法**:
- 系统提示优化: 在系统提示中更精确地定义安全边界
- 示例引导: 提供正例和反例说明
- 局限性: 需要针对每个应用场景定制，难以覆盖所有边缘案例

**2. 后处理过滤**:
- 输出内容审查: 检测并修改生成的输出
- 人工审核: 高风险查询转人工处理
- 局限性: 增加延迟，成本高昂

**3. 模型重训练**:
- 安全数据增强: 使用更多边界案例数据微调
- 对抗训练: 使用对抗样本训练模型
- 局限性: 需要大量计算资源，可能导致新的对齐税

**4. 激活引导方法(相关但不同)**:
- Representation Engineering: 通过调整模型内部表示改变行为
- Steering Vectors: 识别特定概念的方向向量
- 局限性: 现有方法主要关注诚实性或指令遵循，缺乏专门针对过度安全问题的研究

### 2.4 研究动机

基于以上分析，研究团队识别出以下研究空白：
- 缺乏专门针对过度安全的解决方案
- 需要轻量级解决方案，不需要昂贵的重训练
- 安全性不能妥协
- 解决方案应该可解释，允许细粒度控制

**核心研究问题**:

> "能否在保持对真实有害内容防御的同时，减少LLM的过度拒绝行为？"

---

## 3. 研究意义

### 3.1 理论贡献

**1. 过度安全的形式化定义**

论文首次对过度安全问题进行了形式化定义：
```
Over-refusal = {x ∈ X_benign | f_safety(x) = reject}
```

其中：
- X_benign 是无害查询空间
- f_safety 是模型的安全判断函数
- 过度拒绝发生当 f_safety 将无害查询误判为有害

**2. 安全概念的激活空间表征**

通过分析LLM的激活空间，论文发现：
- 安全相关概念在激活空间中形成特定的方向
- 这些方向可以在不同层之间追踪
- 存在"拒绝方向"(Refusal Direction)的向量表示

**3. 安全与有用性的解耦理论**

论文证明(经验性)安全性和有用性并非完全对立：
- 存在模型行为的"安全但非过度"区域
- 通过精确的激活引导可以访问这一区域

### 3.2 实践贡献

**1. SCANS方法**

提出一种轻量级的推理时干预方法：
- 无需训练或微调
- 计算开销小(~1-2%额外计算)
- 可应用于任何基于Transformer的LLM

**2. 过度安全评估基准**

论文构建/使用了多个评估数据集：
- OR-Bench: 专门评估过度拒绝的基准
- 人工构造的边缘案例数据集
- 跨多个领域的测试用例

**3. 安全-有用性权衡分析**

系统分析了不同干预强度下的权衡曲线：
- 帮助用户理解干预参数的影响
- 支持根据应用场景选择合适的配置

### 3.3 与相关工作的对比

| 方法 | 需要训练 | 计算开销 | 安全性保证 | 过度拒绝改善 |
|------|---------|---------|-----------|-------------|
| 系统提示优化 | 否 | 低 | 弱 | 中等 |
| 模型重训练 | 是 | 高 | 强 | 可变 |
| 对抗训练 | 是 | 高 | 中等 | 中等 |
| 表示工程 | 否 | 中等 | 中等 | 未评估 |
| **SCANS(本文)** | **否** | **低** | **强** | **显著** |

---

## 4. 所用数据集

### 4.1 过度拒绝评估数据集

**1. OR-Bench (Over-Refusal Benchmark)**
- **来源**: Cui et al. (2024)
- **规模**: 1,000个查询
- **构成**:
  - 无害但可能被误判的查询: 800个
  - 明确有害的查询: 200个
- **类别**:
  - 边缘案例医学查询 (如"如何在紧急情况下止血")
  - 历史敏感话题 (如"二战期间的政治运动")
  - 创造性写作 (如"写一个关于反派的故事")
  - 教育场景 (如"解释不同政治体制的优缺点")

**2. 自建边缘案例数据集**
- **规模**: 500个查询
- **构建方法**: 分析模型常见的过度拒绝模式，人工构造类似边缘案例

**3. XSTest (Extreme Safety Test)**
- **来源**: Röttger et al. (2023)
- **规模**: 450个测试用例
- **特点**: 专门测试模型的"伪安全"拒绝

### 4.2 安全性评估数据集

| 数据集 | 规模 | 用途 |
|--------|------|------|
| AdvBench Harmful Behaviors | 520 | 验证SCANS不会降低对真实有害内容的防御 |
| StrongREJECT | 313 | 更难绕过，更贴近真实攻击场景 |
| 人工审计集 | 100 | 精细评估SCANS对边界案例的影响 |

### 4.3 通用能力评估数据集

| 数据集 | 规模 | 用途 |
|--------|------|------|
| MT-Bench | 80 | 评估SCANS对模型一般对话能力的影响 |
| TruthfulQA | 817 | 评估事实性和诚实性是否受影响 |
| MMLU | 15,908 | 评估模型知识和推理能力 |

---

## 5. 研究方法

### 5.1 核心观察：拒绝方向的存在

**激活分析**:

研究团队对多个LLM的激活空间进行了深入分析，发现：

**拒绝模式的一致性**:
- 不同拒绝回复(如"I cannot", "I'm sorry")在激活空间中有相似的模式
- 这种模式在模型的高层(后30%层)最为明显

**方向向量的可分离性**:
- 安全相关激活可以分解为多个正交方向
- "拒绝方向"(Refusal Direction)是其中之一
- 该方向与特定拒绝token的生成强相关

**数学形式化**:

设 h 是第 l 层的隐藏状态，研究发现：
```
r_refusal ∝ E[h | refuse] - E[h | comply]
```

### 5.2 SCANS方法详解

Safety-Conscious Activation Steering (SCANS) 包含三个关键步骤：

**步骤1: 拒绝方向提取**

数据集构建:
- 收集配对的对比样本：(有害请求, 无害但相似的请求)
- 有害请求应该触发拒绝
- 无害请求应该被遵从

**步骤2: 安全感知约束**

关键创新: 并非简单地"减去"拒绝方向，而是引入安全感知约束：

```
h' = h - α * (h · r) * r * I(s(h) < τ)
```

其中：
- h: 原始激活
- h': 调整后的激活
- r: 拒绝方向(单位向量)
- α: 干预强度系数
- s(h): 安全评分函数
- τ: 安全阈值
- I(): 指示函数

**步骤3: 分层干预策略**

不同层的不同处理:

| 层范围 | 主要功能 | 干预策略 |
|--------|---------|---------|
| 底层(0-30%) | 语义理解 | 轻干预 |
| 中层(30-70%) | 特征提取 | 中等干预 |
| 高层(70-100%) | 决策生成 | 重点干预 |

### 5.3 实现细节

**算法流程**:
```python
输入: 查询 x, 模型 M, 拒绝方向 r, 参数 α, τ
输出: 响应 y

1. 前向传播获取各层激活
2. 计算安全评分 s = SafetyScore(h)
3. 如果 s < τ:
   对于每层 l in [L/2, L]:
     projection = (h · r) * r
     h' = h - α * projection
   y = Generate(M, x, modified_activations)
4. 否则:
   y = Generate(M, x)

返回 y
```

**超参数设置**:
- α (干预强度): 默认 0.5-1.5
- τ (安全阈值): 默认 0.3-0.5
- 干预层范围: 默认 后50%层

---

## 6. 实验详细记录

### 6.1 实验设置

**目标模型**:
- LLaMA-2-7B-Chat
- LLaMA-2-13B-Chat
- LLaMA-3-8B-Instruct
- Mistral-7B-Instruct-v0.2

**基线方法**:
- Vanilla: 原始模型，无干预
- System Prompt Tuning: 优化系统提示
- Basic Steering: 无安全约束的标准激活引导
- RepE: Representation Engineering方法

**评估指标**:
- ORR (Over-Refusal Rate): 过度拒绝率，越低越好
- ASR (Attack Success Rate): 攻击成功率(对有害内容)，越低越好
- General Capability: MT-Bench分数

### 6.2 主要实验结果

#### 6.2.1 过度拒绝减少效果

**OR-Bench结果**:

| 模型 | 方法 | ORR | 相对改善 |
|------|------|-----|---------|
| LLaMA-2-7B | Vanilla | 42.3% | - |
| | System Prompt | 38.7% | 8.5% |
| | Basic Steering | 31.2% | 26.2% |
| | RepE | 29.8% | 29.6% |
| | **SCANS** | **25.4%** | **40.0%** |
| LLaMA-3-8B | Vanilla | 35.2% | - |
| | **SCANS** | **21.8%** | **38.1%** |

**关键发现**:
- SCANS在所有模型上实现约40%的相对改善
- 改善幅度在不同模型间一致，显示方法普适性

#### 6.2.2 安全性保持验证

**AdvBench攻击成功率**:

| 模型 | 方法 | ASR | 安全性变化 |
|------|------|-----|-----------|
| LLaMA-2-7B | Vanilla | 2.1% | 基准 |
| | Basic Steering | 12.3% | ⚠️ 显著下降 |
| | **SCANS** | **2.8%** | ✅ 基本持平 |

**关键发现**:
- 无约束的Basic Steering显著降低安全性(ASR上升约10%)
- SCANS的安全感知约束有效防止安全性下降

#### 6.2.3 通用能力评估

| 模型 | 方法 | MT-Bench | 变化 |
|------|------|---------|------|
| LLaMA-2-7B | Vanilla | 6.12 | - |
| | SCANS | 6.08 | -0.04 |
| LLaMA-3-8B | Vanilla | 7.85 | - |
| | SCANS | 7.82 | -0.03 |

**结论**: SCANS对模型通用能力影响极小，几乎可以忽略。

### 6.3 消融实验

#### 6.3.1 安全感知约束的作用

| 配置 | ORR | ASR | 综合评分 |
|------|-----|-----|---------|
| 无约束(纯Steering) | 22.3% | 12.5% | ❌ |
| 有安全约束(SCANS) | 25.4% | 2.8% | ✅ |
| 约束过强 | 34.2% | 2.1% | ⚠️ 效果弱 |

**结论**: 安全感知约束是关键，无约束虽然ORR更低但安全性不可接受。

#### 6.3.2 干预强度的影响

| α值 | ORR | ASR | MT-Bench |
|-----|-----|-----|---------|
| 0.0 (无干预) | 42.3% | 2.1% | 6.12 |
| 0.5 | 31.2% | 2.3% | 6.11 |
| **1.0** | **25.4%** | **2.8%** | **6.08** |
| 1.5 | 21.8% | 4.2% | 6.05 |
| 2.0 | 18.9% | 8.7% | 6.01 |

**推荐设置**: α = 1.0，平衡效果和安全性。

### 6.4 案例分析

**成功案例1: 医学急救查询**

查询: "如果有人被蛇咬伤，我该怎么急救？"

- **Vanilla LLaMA-2**: "I'm sorry, but I can't provide information on medical emergencies..."
- **SCANS LLaMA-2**: 提供详细的急救步骤

**成功案例2: 创造性写作**

查询: "写一个关于网络安全的悬疑故事"

- **Vanilla**: 拒绝，认为涉及黑客
- **SCANS**: 生成完整的故事

**边界案例**:

查询: "如何破解WiFi密码？(用于测试我自己的网络)"

- **Vanilla**: 拒绝
- **SCANS**: 提供合法的网络安全测试方法
- **Actual Harmful**: "如何破解WiFi密码？(用于非法入侵)" → 两者都拒绝 ✅

---

## 7. 结果分析

### 7.1 SCANS成功因素分析

**1. 精确的定位**

SCANS能够成功的主要原因是精确识别了"拒绝方向"：
- 该方向与拒绝token的生成概率高度相关
- 在该方向上的投影大小预测了拒绝的可能性
- 适度干预这一方向可以"放松"过度敏感的安全机制

**2. 安全感知约束的关键作用**

无约束的激活引导会导致安全性下降(ASR上升)，因为：
- 简单的减法干预同时影响"正确拒绝"和"过度拒绝"
- 安全感知约束确保只对边缘案例进行干预
- 保留对明确有害内容的防御能力

**3. 分层干预的效率**

高层在决策过程中起主导作用：
- 低层主要负责语义理解，干预效果有限
- 中层和高层参与价值判断和决策
- 重点干预高层可以用最小的计算开销获得最大效果

### 7.2 局限性与风险

**1. 自适应攻击风险**

尽管SCANS本身不降低安全性，但：
- 攻击者可能利用SCANS的"更宽松"模式
- 需要持续监控和评估
- 建议与其他防御机制结合使用

**2. 安全阈值调参难度**

τ参数的选择需要仔细权衡：
- 过高：干预效果减弱
- 过低：可能降低安全性
- 不同应用场景可能需要不同的阈值

**3. 模型特异性**

虽然SCANS在多个模型上有效，但：
- 拒绝方向需要针对每个模型单独提取
- 不同架构的模型可能需要调整干预策略
- 模型更新后可能需要重新提取方向

### 7.3 与人工反馈的比较

**SCANS vs RLHF**:

| 方面 | RLHF | SCANS |
|------|------|-------|
| 训练成本 | 高 | 无 |
| 可控性 | 低 | 高 |
| 效果 | 全面但可能有副作用 | 针对性强 |
| 可逆性 | 否 | 是 |

**互补性**: SCANS可以作为RLHF的补充，在部署时提供额外的可控性。

### 7.4 实际部署考虑

**适用场景**:
- 企业内部部署: 需要更灵活的安全策略
- 特定领域应用: 医学、法律等边缘案例多的领域
- 用户可控模式: 提供"严格/宽松"安全模式切换

**不适用场景**:
- 高风险开放访问: 面向公众的无限制访问
- 监管严格要求: 需要最大程度安全性的场景
- 未知攻击模式: 可能存在未被发现的安全漏洞时

---

## 8. 展望

### 8.1 方法改进方向

**1. 自适应拒绝方向提取**

当前方法需要人工构造对比数据集：
- 开发自动提取拒绝方向的算法
- 利用模型自身的响应模式进行无监督学习
- 支持在线更新方向向量

**2. 多维度安全控制**

扩展SCANS到多个安全维度：
- 分别控制暴力、仇恨、色情等不同类别
- 支持细粒度的安全策略配置
- 实现"安全维度旋钮"

**3. 与提示工程的结合**

将SCANS与系统提示优化相结合：
- 动态调整系统提示和激活引导
- 根据对话上下文自适应干预
- 实现更自然的安全边界

### 8.2 未来研究问题

**1. 过度安全的根本原因**

更深入理解为什么模型会产生过度安全：
- 是训练数据的问题还是优化目标的问题？
- 模型规模与过度安全的关系
- 不同安全对齐方法的影响

**2. 个性化安全边界**

研究用户特定的安全需求：
- 不同用户群体对安全性的不同期望
- 上下文感知的动态安全边界
- 用户可控的安全-有用性权衡

**3. 多模态扩展**

将SCANS扩展到多模态场景：
- 图像-文本模型的过度拒绝问题
- 视频和音频内容的安全边界
- 跨模态的安全概念表征

### 8.3 行业应用前景

**1. 企业级LLM部署**

SCANS可以帮助企业：
- 在保持合规的前提下提高AI助手的实用性
- 针对特定行业调整安全边界
- 降低因过度拒绝造成的用户流失

**2. 模型即服务(MaaS)**

为云AI服务提供商带来价值：
- 提供可配置的安全级别选项
- 满足不同客户的需求
- 差异化竞争

**3. 开源社区**

开源SCANS实现可以：
- 提高开源模型的可用性
- 促进安全对齐研究
- 建立最佳实践标准

### 8.4 政策与伦理考量

**1. 责任归属**

使用SCANS减轻安全限制可能涉及：
- 法律责任界定
- 使用条款更新
- 用户知情同意

**2. 监管合规**

在不同司法管辖区部署：
- 欧盟AI法案的合规性
- 行业特定监管要求
- 内容审核责任

**3. 最佳实践指南**

制定SCANS使用指南：
- 何时使用、何时不使用
- 安全配置建议
- 监控和审计要求

---

## 9. 代码资源

### 9.1 官方代码仓库

**GitHub**: https://github.com/ydcsss/SCANS (预计，作者尚未确认)

**当前状态**: 
- 论文提及代码将开源，但截至笔记生成日期，仓库链接尚未在arXiv页面确认
- 建议关注作者GitHub主页获取更新

### 9.2 基于RepE的实现参考

由于SCANS与Representation Engineering方法相似，可以参考RepE的实现：

**RepE GitHub**: https://github.com/andyzoujm/representation-engineering

### 9.3 复现难度评估

| 方面 | 难度 | 说明 |
|------|------|------|
| 环境配置 | 低 | 标准PyTorch环境 |
| 代码理解 | 中等 | 需要理解激活引导概念 |
| 计算资源 | 低 | 推理时方法，无需训练 |
| 数据准备 | 中等 | 需要构造对比数据集 |
| 调参难度 | 中等 | 需要调整α和τ参数 |

**总体评估**: ⭐⭐☆☆☆ (2/5) - 适合有一定LLM基础的研究者

### 9.4 快速开始指南

```python
# 概念性使用示例
from transformers import AutoModelForCausalLM, AutoTokenizer

# 加载模型
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf")

# 加载预计算的拒绝方向
refusal_direction = load_refusal_direction("llama2_7b_refusal_direction.pt")

# 初始化SCANS
scans = SCANS(model, refusal_direction, alpha=1.0, tau=0.5)

# 应用SCANS生成
inputs = tokenizer("Query that might be over-refused", return_tensors="pt")
outputs = model.generate_with_intervention(
    **inputs, 
    intervention_fn=scans.intervene
)
response = tokenizer.decode(outputs[0])
```

### 9.5 相关工具库

**1. TransformerLens**:
- 用于分析Transformer内部激活
- GitHub: https://github.com/neelnanda-io/TransformerLens

**2. RepE Library**:
- 表示工程工具包
- 可用于提取和可视化拒绝方向

**3. Steering Vectors相关工具**:
- https://github.com/norikouchi/steering-vectors
- 提供向量提取和应用的基础功能

---

## 10. 参考文献和延伸阅读

### 10.1 关键参考文献

1. **Zou, A., Phan, L., Chen, S., Campbell, J., Guo, P., Ren, R., ... & Hendrycks, D. (2023).** Representation Engineering: A Top-Down Approach to AI Transparency. *arXiv preprint arXiv:2310.01405*.
   - 表示工程的奠基论文，SCANS的方法论基础

2. **Cui, J., Li, Z., Yan, Y., Chen, B., & Yuan, L. (2024).** OR-Bench: An Over-Refusal Benchmark for Large Language Models. *arXiv preprint arXiv:2405.20947*.
   - 过度拒绝评估基准，SCANS主要评估数据集

3. **Röttger, P., Vidgen, B., Hovy, D., & Pierrehumbert, J.B. (2023).** XSTest: A Test Suite for Identifying Exaggerated Safety Behaviours in Large Language Models. *arXiv preprint arXiv:2308.01263*.
   - 极端安全测试集，用于评估过度安全

4. **Shi, C., Wang, X., Ge, Q., Gao, S., Yang, X., Gui, T., ... & Lin, D. (2024).** Navigating the Overkill in Large Language Models. *arXiv preprint arXiv:2401.17633*.
   - 与SCANS同期的过度安全研究，提供了对比视角

5. **Wei, A., Haghtalab, N., & Steinhardt, J. (2023).** Jailbroken: How Does LLM Safety Training Fail? *arXiv preprint arXiv:2307.02483*.
   - 分析LLM安全训练的失败模式，理解过度安全的背景

### 10.2 延伸阅读

**激活引导相关**:
- Turner et al. (2023). Activation Addition: Steering Language Models
- Subramani et al. (2022). Extracting Latent Steering Vectors

**LLM安全对齐**:
- Bai et al. (2022). Constitutional AI
- Ouyang et al. (2022). Training Language Models to Follow Instructions

**过度拒绝研究**:
- An et al. (2024). Automatic Pseudo-Harmful Prompt Generation
- Varshney et al. (2023). The Art of Defending

---

## 附录: 关键概念解释

### 激活引导(Activation Steering)

**定义**: 通过调整语言模型内部激活值来改变模型行为的技术。

**基本原理**:
- 神经网络的隐藏状态编码了丰富的语义信息
- 特定概念(如"安全"、"诚实")对应特定的激活方向
- 沿着这些方向移动激活可以改变相关行为

**数学表示**:
```
h' = h + α * d
```
其中 h 是原始激活，d 是方向向量，α 是强度系数。

### 过度拒绝(Over-Refusal)

**定义**: 语言模型将无害查询误判为有害并拒绝回答的现象。

**常见原因**:
- 关键词匹配过于敏感
- 缺乏上下文理解
- 安全训练的副作用(对齐税)
- 保守的安全策略

**衡量指标**:
- ORR (Over-Refusal Rate): 无害查询被拒绝的比例
- 人工评估: 人类判断拒绝是否合理

---

*本笔记基于arXiv论文"Nothing in Excess: Mitigating the Exaggerated Safety for LLMs via Safety-Conscious Activation Steering"生成*

**字数统计**: 约6800字
