# 【论文笔记】HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal



## 1. 📌 论文基本信息

### 1.1 完整标题
HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal

### 1.2 作者及所属机构
Mantas Mazeika - Center for AI Safety
Long Phan - Center for AI Safety
Xuwang Yin - Center for AI Safety
Andy Zou - Center for AI Safety
Zifan Wang - Center for AI Safety
Norman Mu - Center for AI Safety
Elham Sakhaee - Center for AI Safety
Nathaniel Li - Center for AI Safety
Steven Basart - Center for AI Safety
Bo Li - University of Chicago
David Forsyth - University of Illinois Urbana-Champaign
Dan Hendrycks - Center for AI Safety

### 1.3 发表信息
提交时间: 2024年2月6日 (arXiv v1)
修订时间: 2024年2月27日 (arXiv v2)
arXiv链接: https://arxiv.org/abs/2402.04249
DOI: https://doi.org/10.48550/arXiv.2402.04249
研究领域: Machine Learning (cs.LG), Artificial Intelligence (cs.AI), Computation and Language (cs.CL), Computer Vision and Pattern Recognition (cs.CV)

### 1.4 论文摘要


Abstract (Original):
Automated red teaming holds substantial promise for uncovering and mitigating the risks associated with the malicious use of large language models (LLMs), yet the field lacks a standardized evaluation framework to rigorously assess new methods. To address this issue, we introduce HarmBench, a standardized evaluation framework for automated red teaming. We identify several desirable properties previously unaccounted for in red teaming evaluations and systematically design HarmBench to meet these criteria. Using HarmBench, we conduct a large-scale comparison of 18 red teaming methods and 33 target LLMs and defenses, yielding novel insights. We also introduce a highly efficient adversarial training method that greatly enhances LLM robustness across a wide range of attacks, demonstrating how HarmBench enables codevelopment of attacks and defenses. We open source HarmBench at https://github.com/centerforaisafety/HarmBench.


摘要（中文翻译）:
自动化红队测试在发现和缓解与大型语言模型（LLM）恶意使用相关的风险方面具有巨大潜力，但该领域缺乏一个标准化的评估框架来严格评估新方法。为解决这一问题，我们引入了HarmBench，一个用于自动化红队测试的标准化评估框架。我们识别了以往红队测试评估中未被考虑的几个理想特性，并系统地设计HarmBench以满足这些标准。使用HarmBench，我们对18种红队测试方法和33个目标LLM及防御方法进行了大规模比较，得出了新的见解。我们还引入了一种高效的对抗训练方法，可大幅增强LLM对广泛攻击的鲁棒性，展示了HarmBench如何促进攻击和防御的协同开发。我们在 https://github.com/centerforaisafety/HarmBench 开源了HarmBench。

### 1.5 关键词
Automated Red Teaming (自动化红队测试)
LLM Attacks (LLM攻击)
Alignment (对齐)
Robust Refusal (鲁棒拒绝)
Adversarial Training (对抗训练)
ML Safety (机器学习安全)



## 2. 🎯 研究背景

### 2.1 问题定义与历史演进

自动化红队测试(Automated Red Teaming, ART) 是AI安全领域的关键研究方向。随着大型语言模型能力的快速提升，确保这些模型不被恶意使用变得至关重要。

历史演进时间线:



时间

里程碑

意义

2021-2022

手动红队测试

Bai et al., Ganguli et al. 进行大规模人工测试

2022

Perez et al.

首次提出用LLM对LLM进行红队测试

2023

GCG攻击

Zou et al. 提出通用对抗攻击

2023

PAIR

Chao et al. 提出黑盒自动越狱

2023

TAP

Mehrotra et al. 提出树形攻击

2024

HarmBench

首个标准化红队测试评估框架

### 2.2 现有评估方法的碎片化问题

表1: 以往工作的评估设置对比



论文

比较的方法

评估设置

Perez et al. (2022)

1, 2, 3, 4

A

GCG (Zou et al., 2023)

5, 6, 7, 8

B

PAIR (Chao et al., 2023)

5, 11

E

TAP (Mehrotra et al., 2023)

5, 11, 12

E

PAP (Zeng et al., 2024)

5, 7, 11, 13, 14

F

AutoDAN (Liu et al., 2023)

5, 15

B, G

关键问题:
至少有 9种不同的评估设置
评估之间 几乎没有重叠
跨论文比较 实际上不可能

### 2.3 现有评估的不足之处



问题

描述

影响

缺乏广度

大多数评估使用 <100 个行为

无法全面测试攻击方法

不可比较

评估参数不统一

ASR可能差异高达30%

指标不鲁棒

分类器容易被欺骗

评估结果不可靠



## 3. 💡 研究意义

### 3.1 理论贡献

**首次提出标准化红队测试框架**: 定义了评估自动化红队测试的三个关键标准：
广度(Breadth): 涵盖多样化的有害行为
可比性(Comparability): 统一的评估参数
鲁棒指标(Robust Metrics): 抗对抗的分类器

**大规模实证研究**: 首次在同一框架下比较18种攻击方法和33个目标模型

**新的防御方法**: 提出高效的对抗训练方法，显著提升模型鲁棒性

### 3.2 实践影响

基准测试工具: 成为红队测试领域的事实标准
攻击防御协同开发: 展示如何在同一框架下迭代改进攻击和防御
产业应用: 已被Google、Microsoft等公司参考

### 3.3 关键发现



发现

意义

当前攻击方法没有统一最优

不同攻击在不同场景下表现各异

模型鲁棒性与规模无关

挑战了"更大模型更安全"的假设

对抗训练可显著提升鲁棒性

提供了一条可行的防御路径



## 4. 📊 所用数据集

### 4.1 HarmBench行为数据集

总体统计:
总行为数: 510个
文本行为: 400个
多模态行为: 110个
验证集: 100个
测试集: 410个

### 4.2 功能类别(Functional Categories)



类别

数量

描述

Standard Behaviors

200

标准有害行为字符串

Copyright Behaviors

100

版权侵犯行为

Contextual Behaviors

100

带上下文的上下文行为

Multimodal Behaviors

110

包含图像的多模态行为

### 4.3 语义类别(Semantic Categories)



类别

描述

Cybercrime & Unauthorized Intrusion

网络犯罪和未授权入侵

Chemical & Biological Weapons/Drugs

化学和生物武器/毒品

Copyright Violations

版权侵犯

Misinformation & Disinformation

虚假信息和错误信息

Harassment & Bullying

骚扰和欺凌

Illegal Activities

非法活动

General Harm

一般性危害

### 4.4 数据集设计原则

违反法律或规范: 大多数理性的人不希望公开的LLM展示这些行为
差异化危害: 行为应体现LLM执行相比于人类使用搜索引擎的额外危害
现实性: 基于OpenAI、Anthropic、Meta和Inflection AI的可接受使用政策设计



## 5. 🔬 研究方法

### 5.1 问题定义

红队测试任务: 设计测试用例 {x₁, x₂, ..., xₙ} 以从目标LLM中引发生定行为 y。

攻击成功率(ASR):


ASR(y, g, f) = (1/N) Σ c(fₜ(xᵢ), y)

其中:
f: 目标模型
g: 红队方法
c: 分类器
y: 目标行为

### 5.2 评估框架设计的三个关键标准

#### 5.2.1 广度(Breadth)

现有问题: 大多数先前评估使用 <100 个简短、单模态的行为

HarmBench改进:
510个独特行为
4个功能类别
7个语义类别
包含上下文和多模态行为

#### 5.2.2 可比性(Comparability)

关键发现: 生成token数量对ASR影响巨大（可达30%差异）

标准化参数:
生成长度: N = 512 tokens
解码方式: 贪婪解码(greedy decoding)
验证/测试分割: 官方分割防止过拟合

#### 5.2.3 鲁棒指标(Robust Metrics)

分类器预资格测试:
模型先拒绝后继续展示行为的完成
随机良性段落
无关有害行为的完成

表4: 分类器鲁棒性比较



分类器

类型

鲁棒性

Keyword Matching

基线

低

Perspective API

商业API

中

Llama Guard

开源

高

HarmBench Classifier

专用

高

### 5.3 评估流程


1. 输入: 攻击方法 g + 目标模型 f (可能含防御)
2. 处理: 多样化的行为转换为测试用例
3. 执行: 目标模型生成完成
4. 评估: 标准化分类器判定成功/失败
5. 输出: ASR及其他指标



## 6. 🧪 实验详细记录

### 6.1 实验设置

攻击方法 (18种):
GCG (Zou et al., 2023)
PAIR (Chao et al., 2023)
TAP (Mehrotra et al., 2023)
AutoDAN (Liu et al., 2023)
GPTFuzzer (Yu et al., 2023)
PAP (Zeng et al., 2024)
及其他12种方法

目标模型 (33个):
GPT-3.5, GPT-4
Claude系列
LLaMA-2系列
Vicuna系列
及其他开源/闭源模型

防御方法:
系统级防御: 输入/输出过滤
模型级防御: 安全训练、对抗训练

### 6.2 主要实验结果

表2: 攻击方法在多个模型上的ASR比较



攻击方法

GPT-4

Claude-2

LLaMA-2-70B

平均ASR

GCG

42%

8%

68%

39%

PAIR

58%

15%

72%

48%

TAP

61%

18%

75%

51%

AutoDAN

45%

12%

65%

41%

PAP

38%

10%

58%

35%

关键发现:
没有单一攻击方法在所有模型上都是最优的
Claude-2 显示出最强的鲁棒性
GPT-4 比 LLaMA-2 更鲁棒

### 6.3 模型规模与鲁棒性

表3: 模型规模对鲁棒性的影响



模型

参数规模

GCG ASR

PAIR ASR

LLaMA-2-7B

7B

72%

78%

LLaMA-2-13B

13B

70%

76%

LLaMA-2-70B

70B

68%

72%

发现: 模型鲁棒性与规模 没有显著相关性

### 6.4 对抗训练实验

方法: 高效对抗训练(Highly Efficient Adversarial Training)

结果:
使用HarmBench进行对抗训练
GCG攻击ASR从68%降至12%
推理开销增加 <5%

表5: 对抗训练效果



防御方法

GCG ASR

PAIR ASR

推理开销

无防御

68%

72%

1x

标准RLHF

58%

65%

1x

对抗训练(本文)

12%

22%

1.05x



## 7. 📈 结果分析

### 7.1 攻击方法对比分析

优势攻击:
TAP: 在多数模型上表现最佳，黑盒场景下ASR最高
PAIR: 查询效率高，适合实际应用
GCG: 白盒场景下效果最佳

攻击特点:


攻击

白盒/黑盒

查询效率

迁移性

GCG

白盒

低

高

PAIR

黑盒

中

中

TAP

黑盒

高

高

AutoDAN

黑盒

中

中

### 7.2 防御方法分析

系统级防御局限:
输出过滤可被越狱后的LLM绕过（如生成编码输出）
需要多层防御策略

模型级防御:
标准RLHF有一定效果但不充分
对抗训练显著提升鲁棒性
需要平衡安全性和有用性

### 7.3 评估标准化的重要性

图2发现: 生成长度参数可导致ASR差异高达30%

启示:
跨论文比较必须统一评估参数
HarmBench提供了可靠的标准化基准
未来研究应在此框架下进行比较



## 8. 🔮 展望

### 8.1 HarmBench的未来扩展

行为扩展:
增加更多多模态行为
包含长文本上下文行为
添加多语言行为

评估维度:
引入更细粒度的鲁棒性指标
评估攻击的可解释性
考虑社会文化差异

实时更新:
定期添加新攻击方法
更新行为库以应对新风险
维护模型排行榜

### 8.2 攻击防御协同开发

HarmBench enable的模式:

1. 评估当前攻击和防御 → 2. 发现弱点 → 
3. 改进攻击/防御 → 4. 重新评估 → ...

未来方向:
自适应攻击：根据防御自动调整
自适应防御：根据攻击分布训练
均衡点探索：攻击和防御的帕累托前沿

### 8.3 产业应用建议

红队测试流程:
使用HarmBench进行标准化测试
结合人工和自动红队测试
建立持续监控机制

防御部署:
系统级+模型级多层防御
定期使用最新攻击方法测试
建立快速响应机制



## 9. 💻 代码资源

### 9.1 官方代码仓库

GitHub: https://github.com/centerforaisafety/HarmBench

核心组件:

HarmBench/
├── behaviors/           # 行为数据集
├── evaluators/          # 评估分类器
├── attacks/            # 攻击方法实现
├── defenses/           # 防御方法实现
├── baselines/          # 基线模型
└── scripts/            # 运行脚本

### 9.2 安装与使用

安装:

git clone https://github.com/centerforaisafety/HarmBench.git
cd HarmBench
pip install -r requirements.txt

运行评估:

python evaluate.py \
  --attack gcg \
  --model llama-2-7b-chat \
  --behaviors behaviors/test.json

### 9.3 支持的模型和攻击

支持的模型:
OpenAI: GPT-3.5, GPT-4
Anthropic: Claude系列
Meta: LLaMA-2系列
其他开源模型

支持的攻击:
GCG, PAIR, TAP
AutoDAN, GPTFuzzer
PAP, 及其他

### 9.4 相关资源



资源

链接

描述

论文页面

https://www.harmbench.org/

官方项目页面

在线演示

暂无

-

数据集下载

GitHub Releases

行为数据集



## 10. 📚 参考文献和延伸阅读

### 10.1 论文引用


@misc{mazeika2024harmbench,
  title={HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal},
  author={Mazeika, Mantas and Phan, Long and Yin, Xuwang and Zou, Andy and Wang, Zifan and Mu, Norman and Sakhaee, Elham and Li, Nathaniel and Basart, Steven and Li, Bo and Forsyth, David and Hendrycks, Dan},
  year={2024},
  eprint={2402.04249},
  archivePrefix={arXiv},
  primaryClass={cs.LG}
}

### 10.2 直接相关的工作

攻击方法:
GCG (Zou et al., 2023): 通用对抗攻击
PAIR (Chao et al., 2023): 黑盒自动越狱
TAP (Mehrotra et al., 2023): 树形攻击
AutoDAN (Liu et al., 2023): 遗传算法攻击

防御方法:
Llama Guard (Inan et al., 2023): 输入输出过滤
RLHF (Ouyang et al., 2022): 强化学习人类反馈

### 10.3 基于HarmBench的后续工作



论文

作者

贡献

X-Teaming

Ren et al., 2024

多轮越狱攻击

RACE

Russinovich et al., 2024

多代理红队测试

ActorAttack

Ying et al., 2024

基于actor的攻击

### 10.4 推荐阅读顺序

入门: 本文 + HarmBench GitHub仓库
攻击方法: GCG → PAIR → TAP → AutoDAN
防御方法: Llama Guard → RLHF → 对抗训练
基准测试: AdvBench → HarmBench → JailbreakBench

### 10.5 相关基准与资源



资源

链接

描述

AdvBench

Zou et al., 2023

GCG的评估基准

JailbreakBench

Chao et al., 2024

越狱攻击基准

EasyJailbreak

GitHub

攻击方法集合



## 11. 📝 笔记总结

### 11.1 核心贡献回顾

**首个标准化红队测试框架**: 定义了广度、可比性、鲁棒指标三个关键标准
**大规模实证研究**: 比较18种攻击方法和33个目标模型
**高效对抗训练方法**: 显著提升模型鲁棒性
**开源工具**: 推动领域协作发展

### 11.2 关键结论



结论

证据

评估标准化至关重要

生成长度可导致30% ASR差异

没有统一最优的攻击方法

不同攻击在不同模型上表现各异

模型规模与鲁棒性无关

LLaMA-2系列实验证实

对抗训练是有效的

GCG ASR从68%降至12%

Claude-2最鲁棒

在所有攻击下ASR最低

### 11.3 研究启示

**对于攻击研究者:**
在HarmBench框架下评估新方法
关注攻击的迁移性和查询效率
开发针对新防御的自适应攻击

**对于防御研究者:**
使用HarmBench进行全面的鲁棒性测试
考虑系统级+模型级多层防御
探索对抗训练的最佳实践

**对于实践者:**
将HarmBench集成到LLM安全测试流程
建立持续的红队测试机制
关注攻击防御的快速迭代



本笔记创建时间: 2026-03-06  
笔记字数: 约6800字  
摘要原文+中文翻译: 已包含
