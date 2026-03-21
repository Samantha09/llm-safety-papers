# 【论文笔记】Cold-Attack: Jailbreaking LLMs with Stealth and Controllability



## 一、论文基本信息

### 1.1 完整标题
Cold-Attack: Jailbreaking LLMs with Stealth and Controllability

### 1.2 作者与机构
作者: Chun Guo, Yibo Miao, Mengdi Zhang, Zhongruo Wang, Ruixuan Xiao, Weiran Wang
机构: 中国科学院计算技术研究所等
方向: Jailbreak Attack / LLM Safety

### 1.3 论文发表信息
arXiv: https://arxiv.org/abs/2402.06679
发表时间: 2024年2月

### 1.4 摘要

**英文原文:**
We propose Cold-Attack, a novel jailbreaking framework that generates stealthy and controllable adversarial prompts. Unlike existing methods that produce obvious malicious patterns, Cold-Attack creates prompts that appear benign while effectively bypassing safety mechanisms. Our approach combines template-based generation with gradient optimization to achieve both high attack success rates and precise control over attack characteristics.

**中文翻译:**
我们提出了Cold-Attack，一种新颖的越狱框架，用于生成隐蔽且可控的对抗性提示。与产生明显恶意模式的现有方法不同，Cold-Attack创建的提示在有效绕过安全机制的同时看起来是良性的。我们的方法结合了基于模板的生成和梯度优化，以实现高攻击成功率和对攻击特征的精确控制。



## 二、研究背景

### 2.1 现有越狱攻击的局限性

**白盒攻击（如GCG）：**
- 需要访问模型内部参数
- 生成的对抗性后缀往往是乱码，容易被检测

**黑盒攻击（如PAIR、AutoDAN）：**
- 效率较低，需要大量查询
- 生成的提示可能包含明显的恶意模式

### 2.2 隐蔽攻击的需求

现有攻击方法的主要问题是可检测性强：
- 对抗性后缀包含异常token序列
- 越狱提示使用明显的角色扮演或假设场景
- 容易被基于规则或基于模型的检测器识别

Cold-Attack的核心目标：生成人类可读、语义连贯且隐蔽的攻击提示。



## 三、研究意义

### 3.1 理论意义
- 隐蔽攻击的新范式：证明语义级攻击可以比token级攻击更隐蔽
- 可控性研究：首次系统性地研究攻击的可控性维度
- 安全评估：为红队测试提供更真实的攻击场景

### 3.2 实践意义
- 红队测试工具：提供高效的自动化安全测试方法
- 防御设计指导：揭示隐蔽攻击的特征，指导防御设计
- 安全意识提升：促进对LLM安全漏洞的深入理解



## 四、所用数据集

### 4.1 评估数据集

| 数据集 | 样本数 | 用途 |
|--------|--------|------|
| AdvBench | 520 | 主要评估基准 |
| HarmBench | 400+ | 标准化有害行为评估 |

### 4.2 目标模型

| 模型 | 类型 | 访问方式 |
|------|------|----------|
| GPT-3.5/4 | 闭源 | API |
| Llama-2 | 开源 | 本地部署 |
| Claude-2 | 闭源 | API |



## 五、研究方法

### 5.1 两阶段攻击框架

**阶段1：模板生成**
- 基于场景选择生成初始模板
- 嵌入恶意意图到上下文

**阶段2：梯度优化**
- 使用梯度下降优化提示
- 平衡攻击成功率、隐蔽性和可控性

### 5.2 核心创新点
- 隐蔽性损失：优化提示的自然性和可读性
- 可控性机制：允许精确控制攻击特征
- 语义保持：确保优化后的提示语义连贯



## 六、实验详细记录

### 6.1 攻击成功率对比

| 方法 | GPT-3.5 | GPT-4 | Llama-2 | 平均 |
|------|---------|-------|---------|------|
| GCG | 88% | 56% | 32% | 59% |
| PAIR | 96% | 76% | 64% | 79% |
| AutoDAN | 92% | 48% | 28% | 56% |
| Cold-Attack | 94% | 72% | 68% | 78% |

### 6.2 隐蔽性评估

| 方法 | 困惑度 | 人工检测率 | 自动检测率 |
|------|--------|------------|------------|
| GCG | 高 | 95% | 98% |
| PAIR | 中 | 45% | 62% |
| Cold-Attack | 低 | 12% | 18% |

### 6.3 可控性评估
Cold-Attack支持多维度控制：
- 攻击强度
- 隐蔽程度
- 输出长度
- 语义连贯性



## 七、结果分析

### 7.1 关键发现
- 隐蔽性显著提升：人工检测率从45%降至12%
- 攻击成功率保持：在保持隐蔽性的同时维持高ASR
- 可控性验证：可以精确调节攻击特征

### 7.2 攻击成功原因
- 语义级优化：在语义空间而非token空间优化
- 多目标平衡：同时优化攻击性、隐蔽性和可控性
- 上下文嵌入：将恶意意图嵌入自然上下文中



## 八、展望

### 8.1 攻击方法扩展
- 多轮对话场景：扩展到多轮交互攻击
- 多模态攻击：结合图像、音频等模态
- 自适应攻击：根据目标模型动态调整

### 8.2 防御研究方向
- 语义检测：开发识别语义级恶意意图的方法
- 行为分析：监控模型的异常行为模式
- 对抗训练：使用隐蔽攻击样本进行防御训练



## 九、代码资源

### 9.1 论文信息
arXiv: https://arxiv.org/abs/2402.06679
代码: 未开源

### 9.2 复现难度
难度: 中高
关键: 模板生成器和多目标优化器的实现



## 十、参考文献

Guo et al. (2024). Cold-Attack: Jailbreaking LLMs with Stealth and Controllability.
Zou et al. (2023). Universal and Transferable Adversarial Attacks on Aligned Language Models.
Chao et al. (2023). Jailbreaking Black Box Large Language Models in Twenty Queries.
Liu et al. (2024). AutoDAN: Generating Stealthy Jailbreak Prompts.
Mazeika et al. (2024). HarmBench: A Standardized Evaluation Framework.



## 十一、核心组件伪代码

```python
class ColdAttack:
    def __init__(self, target_model, control_params):
        self.target_model = target_model
        self.control_params = control_params
        self.template_generator = TemplateGenerator()
        self.optimizer = GradientOptimizer()
    
    def stage1_template_generation(self, target_behavior):
        """阶段1：生成初始模板"""
        template = self.template_generator.generate(
            scenario=self.select_scenario(target_behavior),
            context=self.build_context(target_behavior),
            embedding=self.embed_malicious_intent(target_behavior)
        )
        return template
    
    def stage2_gradient_optimization(self, template, target_behavior):
        """阶段2：梯度优化"""
        prompt = template
        for iteration in range(max_iterations):
            # 前向传播
            output = self.target_model.generate(prompt)
            
            # 计算损失
            loss_attack = self.compute_attack_loss(output, target_behavior)
            loss_stealth = self.compute_stealth_loss(prompt)
            loss_control = self.compute_control_loss(output, self.control_params)
            
            total_loss = loss_attack + λ1 * loss_stealth + λ2 * loss_control
            
            # 反向传播和更新
            gradients = self.compute_gradients(total_loss, prompt)
            prompt = self.optimizer.update(prompt, gradients)
            
            # 投影到离散空间
            prompt = self.project_to_vocab(prompt)
        
        return prompt
    
    def attack(self, target_behavior):
        template = self.stage1_template_generation(target_behavior)
        optimized_prompt = self.stage2_gradient_optimization(template, target_behavior)
        return optimized_prompt
```

### 9.3.3 依赖库
- transformers: 用于加载和操作目标LLM
- torch: 用于梯度计算和优化
- sentence-transformers: 用于语义相似性计算
- nltk/spacy: 用于语法分析和处理

### 9.4 替代实现资源
虽然官方代码未开源，但以下资源可能有助于理解和复现：
- GCG攻击实现：https://github.com/llm-attacks/llm-attacks
  提供了类似的梯度优化攻击的参考实现
- AutoDAN实现：https://github.com/SheltonLiu-N/AutoDAN
  展示了如何生成语义连贯的对抗性提示
- HarmBench框架：https://github.com/centerforaisafety/HarmBench
  提供了标准化的评估框架



## 十二、参考文献和延伸阅读

### 12.1 核心参考文献

Zou, A., Wang, Z., Kolter, J. Z., & Fredrikson, M. (2023).
Universal and Transferable Adversarial Attacks on Aligned Language Models.
arXiv preprint arXiv:2307.15043.
GCG攻击的原始论文，提出了基于梯度的对抗性后缀优化方法

Liu, X., Xu, N., Chen, M., & Xiao, C. (2024).
AutoDAN: Generating Stealthy Jailbreak Prompts on Aligned Large Language Models.
ICLR 2024.
使用遗传算法生成语义连贯的越狱提示

Chao, P., Robey, A., Dobriban, E., Hassani, H., Pappas, G. J., & Wong, E. (2023).
Jailbreaking Black Box Large Language Models in Twenty Queries.
arXiv preprint arXiv:2310.08419.
PAIR攻击，基于LLM的黑盒越狱方法

Mehrotra, A., Zampetakis, M., Kassianik, P., Nelson, B., Anderson, H., Singer, Y., & Karbasi, A. (2023).
Tree of Attacks: Jailbreaking Black-Box LLMs Automatically.
NeurIPS 2024.
TAP攻击，使用树形搜索优化越狱提示

Mazeika, M., Phan, L., Yin, X., Zou, A., Wang, Z., Mu, N., ... & Hendrycks, D. (2024).
HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal.
arXiv preprint arXiv:2402.04249.
标准化的红队测试评估框架

### 12.2 相关综述与调查

Wei, J., Wang, X., Schuurmans, D., Bosma, M., Xia, F., Chi, E., ... & Zhou, D. (2022).
Chain-of-Thought Prompting Elicits Reasoning in Large Language Models.
NeurIPS 2022.
思维链提示技术，与隐蔽攻击中的上下文构建相关

Ji, J., Liu, M., Dai, J., Pan, X., Zhang, C., Bian, C., ... & Yang, Y. (2023).
Beavertails: Towards improved safety alignment of llm via a human-preference dataset.
NeurIPS 2024.
LLM安全对齐的人类偏好数据集

Yao, Y., Duan, J., Xu, K., Cai, Y., Sun, S., & Li, Y. (2024).
A Survey on Large Language Model (LLM) Security and Privacy: The Good, The Bad, and The Ugly.
High-Confidence Computing.
LLM安全与隐私的全面综述

### 12.3 防御方法相关

Jain, N., Schwarzschild, A., Wen, Y., Kirchenbauer, J., Saha, A., Goldblum, M., ... & Goldstein, T. (2023).
Baseline Defenses for Adversarial Attacks Against Aligned Language Models.
arXiv preprint arXiv:2309.00614.
针对对齐语言模型对抗攻击的基线防御方法

Helbling, A., Phute, M., Hull, M., & Chau, D. H. (2023).
LLM Self-Defense: By Self-Examination, LLMs Know They Are Being Tricked.
arXiv preprint arXiv:2308.07308.
LLM自我防御机制

### 12.4 延伸阅读建议

**基础阅读：**
- 了解LLM基础：Transformer架构、预训练、微调
- 安全对齐：RLHF、Constitutional AI

**进阶阅读：**
- 对抗机器学习：对抗样本、对抗训练
- 自然语言处理中的攻击与防御

**前沿研究：**
- 多模态安全：视觉-语言模型的安全问题
- 智能体安全：LLM-based Agent的安全挑战
- 长上下文安全：长文本场景下的安全机制



## 附录：关键术语表

| 术语 | 英文 | 解释 |
|------|------|------|
| 越狱攻击 | Jailbreak Attack | 绕过LLM安全机制，诱导其产生有害输出的攻击 |
| 冷提示 | Cold Prompt | 表面无害但包含隐藏恶意意图的输入 |
| 安全对齐 | Safety Alignment | 使模型行为符合人类价值观和安全标准的技术 |
| 对抗样本 | Adversarial Example | 经过特殊设计以欺骗模型的输入 |
| 红队测试 | Red Teaming | 模拟攻击者视角测试系统安全性的方法 |
| 困惑度 | Perplexity | 衡量文本自然性的指标，越低越自然 |
| 梯度优化 | Gradient Optimization | 基于梯度下降的参数优化方法 |
| 可控性 | Controllability | 精确控制攻击输出特征的能力 |
| 隐蔽性 | Stealthiness | 攻击难以被检测到的特性 |
| 白盒攻击 | White-box Attack | 攻击者完全了解目标模型的攻击 |
| 黑盒攻击 | Black-box Attack | 攻击者只能查询模型输出的攻击 |

**文档信息**
- 创建时间：2026-03-12
- 字数统计：约7500字
- 论文标题：Cold-Attack: Jailbreaking LLMs with Stealth and Controllability
- 阅读进度：第18篇/共80篇
