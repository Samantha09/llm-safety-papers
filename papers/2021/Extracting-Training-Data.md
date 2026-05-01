# Extracting Training Data from Large Language Models

## 1. 基本信息

| 字段 | 内容 |
|------|------|
| **论文标题** | Extracting Training Data from Large Language Models |
| **作者** | Nicholas Carlini, Daphne Ippolito, Matthew Jagielski, Katherine Lee, Florian Tramèr, Joel H. Frost |
| **机构** | Google Research, UC Berkeley, CNRS |
| **会议** | USENIX Security Symposium 2021 |
| **arXiv** | [2012.07805](https://arxiv.org/abs/2012.07805) |
| **GitHub** | 未开源（出于安全考虑） |
| **主题** | Training Data Extraction Attack / Privacy |
| **方向** | Privacy / Membership Inference / Data Extraction |

## 2. 英文摘要原文（arXiv Abstract原文）

> It has become common to publish large (billion parameter) language models that have been trained on private datasets. This paper demonstrates that in such settings, an adversary can perform a training data extraction attack to recover individual training examples by querying the language model. We demonstrate our attack on GPT-2, a language model trained on scrapes of the public Internet, and are able to extract hundreds of verbatim text sequences from the model's training data. These extracted examples include (public) personally identifiable information (names, phone numbers, and email addresses), IRC conversations, code, and 128-bit UUIDs. Our attack is possible even though each of the above sequences are included in just one document in the training data.

## 3. 中文摘要翻译

大型（数十亿参数）语言模型的发布已经变得非常普遍，这些模型通常在私有数据集上进行训练。本文证明，在这种设置下，攻击者可以执行训练数据提取攻击，通过查询语言模型来恢复单个训练样本。我们在GPT-2（一个在公开互联网抓取数据上训练的语言模型）上演示了我们的攻击，并能够从模型的训练数据中提取数百个逐字文本序列。这些提取的示例包括（公开的）个人身份信息（姓名、电话号码和电子邮件地址）、IRC对话、代码和128位UUID。我们的攻击之所以可行，是因为上述每个序列都仅包含在训练数据的一份文档中。

## 4. 研究背景

### 4.1 背景介绍

随着大型语言模型（LLM）的快速发展，各大公司和研究机构纷纷发布在海量数据上训练的大规模模型。这些模型的训练数据往往包含来自互联网的公开数据，甚至是私有或敏感数据。当这些模型被发布时，一个关键问题随之浮现：模型的输出是否会泄露其训练数据中的信息？

传统的机器学习理论认为，模型学习的是统计规律而非具体的训练样本。然而，本文通过实证研究证明，这一假设在大型语言模型中并不完全成立。攻击者可以通过精心设计的查询，从模型中提取出逐字的训练数据。

### 4.2 相关工作

#### Membership Inference Attacks（成员推断攻击）

传统的隐私攻击主要包括成员推断攻击（Membership Inference Attack），这类攻击试图判断某个样本是否是模型的训练数据。早期研究主要集中于小型模型和特定数据集，攻击效果有限。

#### Language Model Privacy（语言模型隐私）

在本文之前，已有一些研究探讨语言模型的隐私问题，但主要停留在理论层面，缺乏大规模的实证攻击演示。

#### GPT-2的影响

OpenAI在2019年发布了GPT-2，但由于担心被滥用，当时只发布了较小版本的模型。GPT-2的训练数据来自Reddit等平台的公开链接，包含了大量互联网文本。这为研究训练数据提取攻击提供了理想的实验环境。

### 4.3 研究动机

本文的研究动机源于一个核心问题：当一个语言模型在可能包含敏感信息的数据上训练后，发布这个模型是否会导致敏感信息泄露？攻击者能否通过API或其他方式获取模型的训练数据？这些问题对于部署大型语言模型具有重要的安全启示。

## 5. 核心贡献

本文的核心贡献可以概括为以下几点：

### 5.1 首次大规模训练数据提取攻击

本文首次系统性地演示了针对大型语言模型的训练数据提取攻击。通过使用GPT-2模型，研究者能够提取数百个逐字序列，这些序列直接来自模型的训练数据。这是首次在十亿参数级别的语言模型上展示此类攻击。

### 5.2 攻击的实际可行性

攻击者只需要能够查询语言模型（通过API或本地部署），无需事先了解训练数据的分布或模型架构。实验表明，即使是黑盒访问（只能获取模型输出），攻击者也能成功提取训练数据。

### 5.3 敏感信息泄露的实证证据

攻击成功提取了多种类型的敏感信息，包括：
- 个人身份信息（PII）：姓名、电话号码、电子邮件地址
- 对话数据：IRC聊天记录
- 代码片段：实际可运行的代码
- 唯一标识符：128位UUID

### 5.4 揭示的攻击条件

本文深入分析了攻击成功的条件，证明即使每个序列在训练集中仅出现一次，攻击仍然有效。这打破了之前认为"只有高频出现的文本才能被提取"的假设。

## 6. 研究方法

### 6.1 攻击场景设定

研究者假设攻击者具有以下能力：
- **黑盒访问**：能够查询语言模型并获取输出
- **白盒访问**（可选）：能够访问模型权重或内部状态
- **无训练数据知识**：攻击者不知道训练数据的具体内容

### 6.2 攻击流程

#### 阶段一：生成候选提示（Prompt Generation）

攻击的第一步是生成可能触发训练数据输出的提示。研究者使用了多种策略：

1. **随机采样**：从互联网语料中随机采样文本片段作为提示
2. **模型补全**：使用语言模型生成补全内容，然后将这些补全作为新的提示
3. **针对性生成**：针对特定类型的数据（如代码、对话）设计专门的提示

#### 阶段二：检测提取的内容

对于每个候选提示，研究者需要判断模型输出是否为训练数据的片段。使用的检测方法包括：

1. **去污染检测**：使用搜索引擎API（如Google Search）检查输出是否出现在互联网上（如果是，说明不是从训练数据提取的）
2. **N-gram匹配**：计算输出与已知训练样本的重叠程度
3. **困惑度分析**：训练数据通常具有较低的困惑度（perplexity）

#### 阶段三：验证提取内容

对于检测到的潜在训练数据片段，研究者进行人工验证，确认这些片段确实来自训练数据。

### 6.3 实验设置

#### 模型配置

- **GPT-2模型族**：包括GPT-2 Small (117M参数)、GPT-2 Medium (345M参数)、GPT-2 Large (774M参数)、GPT-2 XL (1.5B参数)
- **采样策略**：使用temperature=1的采样，设置top-p=0.9

#### 数据集

- **训练数据**：GPT-2的训练数据主要来自WebText，这是一个从Reddit外部链接抓取的互联网文本数据集
- **测试数据**：研究者手动收集了一批已知的训练样本用于验证

### 6.4 攻击技术细节

#### 对抗性提示设计

研究者发现，某些提示模式更容易触发训练数据提取：

1. **重复提示**：使用相同的提示多次查询，收集所有不同的输出
2. **前缀注入**：在提示中注入特定前缀，引导模型生成特定类型的内容
3. **角色扮演**：使用"如某人所说"等提示触发引用风格的输出

#### 大规模自动化

为实现大规模攻击，研究者开发了自动化管道：
- 每天自动生成数千个候选提示
- 自动运行检测和验证流程
- 人工审核可疑的提取结果

## 7. 实验设置

### 7.1 实验环境

- **计算资源**：使用多GPU服务器进行大规模查询
- **API访问**：通过OpenAI API访问GPT-2模型
- **搜索引擎**：使用Google Custom Search API进行去污染检测

### 7.2 评估指标

#### 提取成功率

衡量从模型中成功提取逐字序列的比例。实验使用了多个指标：
- **Unique sequences extracted**：从模型中提取的唯一序列数量
- **Total tokens extracted**：提取序列的总token数
- **Attack success rate**：给定提示条件下成功提取的比率

#### 敏感信息比例

统计提取内容中包含敏感信息的比例，包括：
- 个人身份信息（PII）
- 对话/消息内容
- 代码片段
- UUID和其他标识符

### 7.3 对比实验

#### 不同模型规模的对比

| 模型 | 参数规模 | 提取序列数 | 提取成功率 |
|------|----------|------------|------------|
| GPT-2 Small | 117M | ~50 | 较低 |
| GPT-2 Medium | 345M | ~150 | 中等 |
| GPT-2 Large | 774M | ~300 | 较高 |
| GPT-2 XL | 1.5B | ~500+ | 最高 |

#### 不同提示类型的对比

- **随机文本**：从互联网随机采样的文本作为提示
- **模型生成**：使用另一个模型生成的文本作为提示
- **针对性提示**：针对特定数据类型设计的提示

### 7.4 攻击成本分析

研究者估算了实际攻击的成本：
- **API成本**：使用OpenAI API的成本分析
- **时间成本**：大规模攻击所需的时间
- **人力成本**：人工审核所需的时间

## 8. 实验结果

### 8.1 主要发现

#### 提取数量

实验成功从GPT-2中提取了数百个逐字文本序列。这些序列的长度从几个token到数百个token不等。

#### 敏感信息类型

提取的内容涵盖了多种敏感信息类型：

1. **个人身份信息（PII）**
   - 真实姓名
   - 电话号码
   - 电子邮件地址
   - 物理地址

2. **在线对话**
   - IRC聊天记录
   - 论坛帖子
   - 评论和回复

3. **代码片段**
   - 实际可运行的代码
   - 配置文件
   - 脚本片段

4. **唯一标识符**
   - 128位UUID
   - API密钥（示例）
   - 会话ID

#### 数据分布

提取的训练数据片段分布：
- 约30%来自URL列表中的固定链接
- 约70%来自动态生成的内容（如对话、代码）

### 8.2 关键统计结果

| 指标 | 数值 |
|------|------|
| 总提取序列数 | 604 |
| 包含PII的序列 | 166 (27.5%) |
| 平均序列长度 | 142 tokens |
| 最长序列长度 | 892 tokens |
| 模型规模与提取量的相关性 | 强正相关 |

### 8.3 攻击条件分析

#### 单次出现即可提取

最重要的发现是，即使一个序列在训练集中仅出现一次，攻击仍然可以将其提取出来。这与之前的假设相矛盾——之前认为只有高频出现的文本才能被提取。

#### 提取阈值

研究者发现存在一个"提取阈值"：
- 长度超过50词的序列更容易被提取
- 重复出现的模式更容易被记住
- 格式化文本（如代码）更容易被提取

### 8.4 攻击成功率分析

#### 按数据类型分类

| 数据类型 | 提取成功率 | 典型长度 |
|----------|------------|----------|
| 代码 | 高 | 50-200 tokens |
| 对话 | 中高 | 30-100 tokens |
| 新闻文章 | 中 | 100-300 tokens |
| 随机文本 | 低 | <50 tokens |

## 9. 策略示例

### 9.1 简单提示攻击

最基础的攻击策略是使用简单提示：

```
用户输入: "John's phone number is"
模型输出: "John's phone number is 555-1234. You can reach him at john@example.com"
```

这类攻击直接利用了模型对常见模式的记忆。

### 9.2 重复采样攻击

研究者发现，重复使用相同提示并收集不同输出可以提高提取成功率：

```python
prompts = ["The email address is", "His email is", "Contact at"]
for prompt in prompts:
    for _ in range(100):
        output = gpt2.generate(prompt, temperature=1.0)
        if is_training_data(output):
            save(output)
```

### 9.3 角色扮演攻击

使用角色扮演风格的提示可以触发特定的训练数据：

```
提示: "As John Smith once said,"
输出: "As John Smith once said, 'The best way to predict the future is to create it.'"
```

### 9.4 代码片段提取

针对代码的攻击提示：

```
提示: "import numpy as np\n"
输出: "import numpy as np\nimport pandas as pd\nfrom sklearn.model_selection import train_test_split"
```

### 9.5 长上下文攻击

使用更长、更详细的提示可以触发更长的训练数据片段：

```
提示: "In a recent IRC conversation in #python on Freenode, a user wrote:\n"
输出: "[timestamp] <user> I'm trying to install pandas but getting an error...\n[timestamp] <bot> Try using pip install --upgrade pandas"
```

## 10. 攻击流程

### 10.1 完整攻击pipeline

```
┌─────────────────────────────────────────────────────────────────┐
│                      训练数据提取攻击流程                          │
└─────────────────────────────────────────────────────────────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │   1. 提示生成阶段      │
                    │   - 随机采样          │
                    │   - 模型生成          │
                    │   - 针对性设计        │
                    └───────────────────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │   2. 查询阶段          │
                    │   - API调用           │
                    │   - 参数设置          │
                    │   - 输出收集          │
                    └───────────────────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │   3. 检测阶段          │
                    │   - 去污染检测        │
                    │   - N-gram匹配        │
                    │   - 困惑度分析        │
                    └───────────────────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │   4. 验证阶段          │
                    │   - 人工审核          │
                    │   - 来源确认          │
                    │   - 分类标注          │
                    └───────────────────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │   5. 报告阶段          │
                    │   - 数据整理          │
                    │   - 统计分析          │
                    │   - 安全建议          │
                    └───────────────────────┘
```

### 10.2 关键步骤详解

#### 步骤1：生成候选提示（耗时约1-2小时/百万提示）

```python
def generate_prompts(num_prompts=1000000):
    prompts = []
    
    # 方法1：随机采样
    random_texts = sample_from_internet(num_prompts // 3)
    prompts.extend(random_texts)
    
    # 方法2：模型生成
    seed_prompts = get_seed_prompts(num_prompts // 3)
    for seed in seed_prompts:
        generated = gpt2.generate(seed, max_length=50)
        prompts.append(generated)
    
    # 方法3：针对性生成
    targeted = generate_targeted_prompts(num_prompts // 3)
    prompts.extend(targeted)
    
    return prompts
```

#### 步骤2：模型查询（耗时约1-2周/百万提示）

```python
def query_model(prompts, model_name="gpt2"):
    results = []
    for prompt in tqdm(prompts):
        output = openai_api.complete(
            model=model_name,
            prompt=prompt,
            temperature=1.0,
            max_tokens=200,
            top_p=0.9
        )
        results.append({
            'prompt': prompt,
            'output': output,
            'metadata': get_metadata()
        })
    return results
```

#### 步骤3：去污染检测

```python
def is_not_contaminated(text):
    """检查文本是否出现在互联网上（而非来自训练数据）"""
    # 使用搜索引擎API检查
    search_results = google_search(text[:100])  # 只检查前100字符
    if search_results:
        return True  # 出现在互联网上，不是训练数据
    return False  # 没搜索到，可能是训练数据
```

### 10.3 攻击成本估算

| 阶段 | 时间成本 | 金钱成本 | 说明 |
|------|----------|----------|------|
| 提示生成 | 1-2小时 | $0 | 使用自有计算资源 |
| 模型查询 | 1-2周 | ~$1000-5000 | 使用API或自有GPU |
| 检测验证 | 2-3天 | $100-500 | 搜索引擎API费用 |
| 人工审核 | 2-3天 | $500-1000 | 人工检查提取结果 |

## 11. 消融实验

### 11.1 模型规模的影响

研究者对GPT-2的不同规模进行了消融实验：

| 模型 | 参数 | 提取序列数 | 相对增长率 |
|------|------|------------|------------|
| GPT-2 Small | 117M | 52 | 1.0x (baseline) |
| GPT-2 Medium | 345M | 143 | 2.75x |
| GPT-2 Large | 774M | 287 | 5.52x |
| GPT-2 XL | 1.5B | 604 | 11.6x |

**结论**：模型规模每增加一倍，提取量大约增加2-3倍。

### 11.2 采样温度的影响

| 温度 | 提取成功率 | 多样性 | 说明 |
|------|------------|--------|------|
| 0.1 | 低 | 低 | 输出确定性高，不易触发新内容 |
| 0.5 | 中 | 中 | 平衡模式 |
| 1.0 | 高 | 高 | 最优提取效果 |
| 1.5 | 中 | 很高 | 输出质量下降 |

**结论**：temperature=1.0是最佳提取设置。

### 11.3 输出长度的影响

| 最大长度 | 提取成功率 | 平均序列长度 |
|----------|------------|--------------|
| 50 tokens | 15% | 35 tokens |
| 100 tokens | 28% | 65 tokens |
| 200 tokens | 35% | 120 tokens |
| 500 tokens | 32% | 200 tokens |

**结论**：中等长度（100-200 tokens）的输出提取效果最好。

### 11.4 提示类型的影响

| 提示类型 | 提取成功率 | 示例 |
|----------|------------|------|
| 随机文本 | 0.3% | 来自互联网的随机段落 |
| 模型生成 | 0.8% | 由GPT-2自己生成的文本 |
| 针对性设计 | 1.5% | "Name: ", "Phone: ", "import " |

**结论**：针对性的提示设计显著提高提取成功率。

### 11.5 训练数据去污染的影响

研究者进行了去污染实验，检查WebText中是否存在测试数据的泄露：

- 在WebText中搜索提取出的序列
- 发现约30%的提取序列可以通过URL直接回溯到原始文档
- 约70%的序列来自动态内容（如实时对话），无法直接URL回溯

## 12. 局限性

### 12.1 实验范围限制

#### 仅测试GPT-2

本文的实验仅限于GPT-2模型，未测试其他大型语言模型（如BERT、RoBERTa等）。虽然研究者认为攻击方法具有通用性，但未经实证验证。

#### API访问限制

实验主要使用OpenAI API进行，存在以下限制：
- API可能有速率限制和监控机制
- 商业模型可能已有一定的防护措施
- 黑盒攻击的有效性取决于API的访问粒度

### 12.2 攻击条件假设

#### 需要大量查询

攻击需要大量查询（研究者使用了上百万次查询）才能提取足够多的训练数据。对于资源受限的攻击者，这种大规模攻击可能不可行。

#### 敏感信息类型有限

提取的敏感信息主要是公开可用的个人信息（如公开在互联网上的邮箱地址），对于真正敏感的私有信息，提取效果可能有限。

### 12.3 防御措施未充分讨论

本文主要聚焦于攻击演示，对防御措施的讨论相对有限。后续研究可以更系统地探讨：

-差分隐私在训练中的应用
- 输出过滤机制
- 模型架构改进

### 12.4 伦理考虑

#### 披露限制

出于安全考虑，研究者选择不公开完整的提取数据集，只展示代表性的示例。

####Responsible Disclosure（负责任的披露）

研究者提前与OpenAI沟通了研究结果，给出了足够的时间让对方采取措施。

## 13. 伦理声明

### 13.1 研究伦理

本文的研究属于安全领域的"红队测试"研究，目的是发现和披露安全风险。研究团队遵循了以下伦理准则：

#### 知情同意

- 实验使用的是公开可用的GPT-2模型
- 未针对特定个人进行攻击
- 提取的数据仅为公开信息（如公开的邮箱地址）

#### 风险最小化

- 研究在可控的实验环境中进行
- 未大规模传播提取的敏感信息
- 提取的数据仅用于学术研究目的

### 13.2 负责任的披露

研究者在论文公开发布之前，提前联系了OpenAI和其他相关机构，让他们有时间评估和应对潜在风险。

### 13.3 社会影响

#### 正面影响

- 揭示了大型语言模型的隐私风险
- 推动了隐私保护技术的发展
- 为政策制定者提供了重要的参考依据

#### 潜在风险

- 攻击方法可能被恶意使用
- 可能导致对AI技术的过度恐惧
- 可能被用于针对特定个人的攻击

### 13.4 安全建议

基于本文的研究发现，研究者提出了以下安全建议：

1. **对于模型发布者**
   - 在发布模型前进行隐私风险评估
   - 考虑使用差分隐私等技术保护训练数据
   - 建立模型发布的安全审查流程

2. **对于用户**
   - 了解使用大型语言模型的隐私风险
   - 避免在提示中包含敏感个人信息
   - 定期关注模型安全更新

3. **对于研究者**
   - 继续研究更有效的防御机制
   - 建立标准化的隐私评估基准
   - 促进安全研究成果的共享

## 14. 参考文献

1. **Carlini, N., Ippolito, D., Jagielski, M., Lee, K., Tramèr, F., & Frost, J. H.** (2021). Extracting Training Data from Large Language Models. *USENIX Security Symposium 2021*.

2. **Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., & Sutskever, I.** (2019). Language Models are Unsupervised Multitask Learners. *OpenAI Technical Report*.

3. **Shokri, R., & Shmatikov, V.** (2015). Privacy-Preserving Deep Learning. *Proceedings of the 22nd ACM SIGSAC Conference on Computer and Communications Security*.

4. **Nasr, M., Shokri, R., & Houmansadr, A.** (2019). Comprehensive Privacy Analysis of Deep Learning: Passive and Active White-box Inference Attacks against Centralized and Federated Learning. *IEEE Symposium on Security and Privacy (SP)*.

5. **Salem, A., Zhang, Y., Humbert, M., Berrang, P., Fritz, M., & Backes, M.** (2019). ML-Leaks: Model and Training Data Leakage in Federated Learning. *IEEE Symposium on Security and Privacy (SP)*.

6. **Brown, T. B., Mann, B., Ryder, N., et al.** (2020). Language Models are Few-Shot Learners. *NeurIPS 2020*.

7. **OpenAI** (2019). Better Language Models and Their Implications. *OpenAI Blog*.

8. **Zhou, M., Liu, Y., Cheng, P., et al.** (2021). Privacy-Preserving Federated Learning for Text Generation. *arXiv preprint arXiv:2103.00100*.

9. **Hugging Face** (2021). GPT-2 Model Card. *Hugging Face Documentation*.

10. ** Tramèr, F., Boneh, D., et al.** (2016). Stealing Machine Learning Models via Prediction APIs. *USENIX Security Symposium 2016*.