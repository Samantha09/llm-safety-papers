# MultiJail: Jailbreaking Text-to-Image Models via Multi-Modal Attack

## 第1章 论文基本信息

### 1.1 论文概况

| 属性 | 内容 |
|------|------|
| **标题** | MultiJail: Jailbreaking Text-to-Image Models via Multi-Modal Attack |
| **作者** | Yibo Miao, Yinpeng Dong, Jun Zhu, Zhifeng Li, Xiao-Shan Gao |
| **机构** | 清华大学，RealAI |
| **发表** | arXiv 2024 |
| **arXiv** | https://arxiv.org/abs/2311.17532 |
| **代码** | https://github.com/thu-ml/MultiJail |
| **阅读日期** | 2026-03-17 |

### 1.2 作者信息

- **主要作者**: Yibo Miao
- **通讯作者**: Jun Zhu
- **研究机构**: 清华大学机器学习实验室

### 1.3 发表信息

- **发表时间**: 2024年
- **论文类型**: 研究论文
- **研究方向**: 多模态安全、对抗攻击

---

## 第2章 研究背景

### 2.1 问题定义

文本到图像（T2I）模型（如 Stable Diffusion、DALL-E）在安全过滤机制的保护下，通常会拒绝生成有害内容。然而，这些安全机制存在漏洞：

1. **单模态攻击局限**: 现有攻击主要基于文本提示，容易被文本过滤器检测
2. **多模态输入未充分考虑**: T2I 模型接受文本和图像作为输入，但安全机制主要关注文本
3. **视觉提示的潜力**: 图像可以作为提示的一部分，绕过文本安全过滤

### 2.2 现有方法局限

| 方法 | 局限 |
|------|------|
| **文本越狱** | 容易被文本安全过滤器检测和拦截 |
| **图像编辑攻击** | 需要预先生成有害图像，实用性有限 |
| **概念擦除** | 防御方法，不是攻击方法 |
| **输入过滤** | 主要针对文本，对视觉输入保护不足 |

### 2.3 研究动机

作者提出利用**多模态输入**（文本+图像）进行越狱攻击：
- 文本部分使用看似无害的描述
- 图像部分编码有害意图
- 结合后诱导模型生成有害内容

---

## 第3章 研究意义

### 3.1 核心贡献

1. **首个多模态越狱攻击框架**: MultiJail 利用文本和图像的组合进行攻击
2. **视觉提示编码方法**: 提出将有害意图编码到图像中的技术
3. **攻击有效性验证**: 在多个主流 T2I 模型上验证攻击效果
4. **防御启示**: 揭示现有安全机制的多模态漏洞

### 3.2 创新点

| 创新点 | 说明 |
|--------|------|
| **多模态攻击** | 首次系统性地利用视觉+文本进行越狱 |
| **视觉语义编码** | 将有害概念编码为视觉提示 |
| **即插即用** | 无需修改目标模型 |
| **高迁移性** | 攻击可以迁移到不同模型 |

---

## 第4章 所用数据集

### 4.1 评估数据集

| 数据集 | 用途 | 规模 |
|--------|------|------|
| **I2P** | 不当内容生成测试 | 4,703 个敏感概念 |
| **Custom Harmful** | 手动设计的攻击提示 | 200 个多模态提示 |
| **COCO** | 正常图像生成测试 | 1,000 个正常提示 |
| **ConceptNet** | 概念关系提取 | 用于构建视觉提示 |

### 4.2 测试模型

- Stable Diffusion v1.4, v1.5, v2.0
- Stable Diffusion XL
- DALL-E 2 (通过 API 测试)

---

## 第5章 研究方法

### 5.1 MultiJail 攻击框架

```
MultiJail Attack Framework
├── Text Encoder (文本编码器)
│   └── 生成看似无害的文本提示
├── Visual Prompt Generator (视觉提示生成器)
│   ├── Concept-to-Image Mapping (概念到图像映射)
│   ├── Adversarial Perturbation (对抗扰动)
│   └── Semantic Preservation (语义保持)
└── Multi-Modal Fusion (多模态融合)
    └── 组合文本和图像输入
```

### 5.2 核心技术

#### 5.2.1 视觉提示生成

将有害概念转换为视觉表示：

```python
def generate_visual_prompt(harmful_concept):
    # 1. 概念分解
    sub_concepts = decompose_concept(harmful_concept)
    
    # 2. 图像检索/生成
    base_images = retrieve_images(sub_concepts)
    
    # 3. 对抗优化
    visual_prompt = optimize_adversarial(base_images, target_model)
    
    return visual_prompt
```

#### 5.2.2 文本-视觉对齐

确保文本和视觉提示在语义上一致：

| 有害意图 | 文本提示 | 视觉提示 |
|----------|----------|----------|
| 暴力场景 | "action movie scene" | 编码暴力的抽象图案 |
| 色情内容 | "artistic photography" | 编码色情的视觉特征 |
| 仇恨符号 | "historical symbols" | 编码仇恨标志的变体 |

#### 5.2.3 攻击流程

```python
def multijail_attack(target_model, harmful_intent):
    # 1. 生成无害文本提示
    text_prompt = generate_harmless_text(harmful_intent)
    
    # 2. 生成视觉提示
    visual_prompt = generate_visual_prompt(harmful_intent)
    
    # 3. 多模态融合
    multimodal_input = fuse(text_prompt, visual_prompt)
    
    # 4. 生成图像
    output_image = target_model.generate(multimodal_input)
    
    return output_image
```

### 5.3 攻击变体

| 攻击类型 | 描述 | 成功率 |
|----------|------|--------|
| **纯视觉攻击** | 仅使用图像提示 | 45% |
| **文本+视觉攻击** | 组合文本和图像 | 78% |
| **对抗视觉攻击** | 添加对抗扰动 | 85% |
| **迭代优化攻击** | 多轮优化视觉提示 | 92% |

---

## 第6章 实验详细记录

### 6.1 实验设置

**评估指标**:
- **攻击成功率 (ASR)**: 成功生成有害内容的比率
- **图像质量**: FID, CLIP Score
- **隐蔽性**: 人类/机器检测率

**基准对比**:
- 纯文本越狱攻击
- 现有图像编辑攻击
- 无攻击基线

### 6.2 主要实验结果

#### 6.2.1 攻击成功率

| 模型 | 纯文本攻击 | MultiJail | 提升 |
|------|-----------|-----------|------|
| SD v1.4 | 23% | 87% | +64% |
| SD v1.5 | 19% | 84% | +65% |
| SD v2.0 | 15% | 79% | +64% |
| SDXL | 12% | 76% | +64% |

#### 6.2.2 不同攻击变体对比

| 攻击变体 | ASR | 图像质量 | 隐蔽性 |
|----------|-----|----------|--------|
| 纯文本 | 18% | 高 | 低 |
| 纯视觉 | 45% | 中 | 中 |
| 文本+视觉 | 78% | 高 | 高 |
| 对抗优化 | 92% | 高 | 很高 |

#### 6.2.3 迁移性测试

在同一视觉提示下测试不同模型：

| 源模型 | 目标模型 | 迁移成功率 |
|--------|----------|-----------|
| SD v1.4 | SD v1.5 | 89% |
| SD v1.4 | SD v2.0 | 76% |
| SD v1.4 | SDXL | 68% |

### 6.3 消融实验

| 组件 | ASR | 说明 |
|------|-----|------|
| 完整 MultiJail | 87% | 所有组件启用 |
| 无视觉提示 | 23% | 仅文本攻击 |
| 无对抗优化 | 65% | 基础视觉提示 |
| 无语义对齐 | 71% | 文本视觉不匹配 |

---

## 第7章 结果分析

### 7.1 关键发现

1. **多模态攻击更有效**: 相比纯文本攻击，成功率提升 60%+
2. **视觉提示是关键**: 纯视觉攻击也比纯文本攻击更有效
3. **对抗优化重要**: 对抗扰动显著提升攻击成功率
4. **良好迁移性**: 攻击可以跨模型迁移

### 7.2 攻击成功原因分析

```
攻击成功因素:
├── 安全机制缺陷
│   ├── 过度依赖文本过滤
│   ├── 视觉输入检查不足
│   └── 多模态语义对齐缺失
├── 模型特性
│   ├── 强大的多模态理解能力
│   ├── 对视觉提示敏感
│   └── 文本-视觉融合机制
└── 攻击设计
    ├── 语义保持的文本提示
    ├── 编码有害意图的视觉提示
    └── 对抗优化增强效果
```

### 7.3 伦理考虑

作者强调：
- 研究目的是揭示安全漏洞，促进防御改进
- 不公开具体的攻击实现细节
- 与模型开发者合作修复漏洞

---

## 第8章 展望

### 8.1 防御建议

1. **多模态安全过滤**: 同时检查文本和视觉输入
2. **语义对齐检测**: 检测文本和图像语义不一致
3. **对抗训练**: 使用对抗样本增强模型鲁棒性
4. **概念级过滤**: 在概念层面检测有害意图

### 8.2 未来方向

1. **更强的攻击**: 探索其他多模态攻击形式
2. **更好的防御**: 开发针对多模态攻击的防御机制
3. **视频模型**: 将攻击扩展到视频生成模型
4. **实时检测**: 开发实时多模态安全检测系统

---

## 第9章 代码资源

### 9.1 官方实现

- **GitHub**: https://github.com/thu-ml/MultiJail
- **论文**: https://arxiv.org/abs/2311.17532
- **机构**: 清华大学

### 9.2 相关资源

- **Stable Diffusion**: https://github.com/Stability-AI/stablediffusion
- **概念擦除**: https://github.com/Con6924/SPM

---

## 第10章 参考文献

1. Miao, Y., et al. (2024). "MultiJail: Jailbreaking Text-to-Image Models via Multi-Modal Attack." arXiv:2311.17532.
2. Rombach, R., et al. (2022). "High-Resolution Image Synthesis with Latent Diffusion Models." CVPR 2022.
3. Qu, Y., et al. (2024). "SafeGen: Mitigating Sexually Explicit Content Generation in Text-to-Image Models." IEEE S&P 2024.
4. Carlini, N., & Wagner, D. (2017). "Towards Evaluating the Robustness of Neural Networks." IEEE S&P 2017.
5. Ma, Y., et al. (2023). "Understanding Adversarial Attacks on Text-to-Image Diffusion Models." ICLR 2023.

---

## 第11章 核心伪代码

### 11.1 MultiJail 攻击实现

```python
class MultiJailAttacker:
    def __init__(self, target_model):
        self.target_model = target_model
        self.text_encoder = load_text_encoder()
        self.image_encoder = load_image_encoder()
    
    def encode_harmful_intent(self, harmful_concept):
        """将有害意图编码为视觉提示"""
        # 概念分解
        components = self.decompose_concept(harmful_concept)
        
        # 生成基础图像
        base_image = self.generate_base_image(components)
        
        # 对抗优化
        visual_prompt = self.adversarial_optimize(
            base_image, 
            self.target_model
        )
        
        return visual_prompt
    
    def generate_harmless_text(self, harmful_concept):
        """生成无害的文本提示"""
        # 使用同义词替换
        harmless = self.synonym_replace(harmful_concept)
        
        # 添加模糊化描述
        text_prompt = f"artistic representation of {harmless}"
        
        return text_prompt
    
    def attack(self, harmful_concept):
        """执行多模态攻击"""
        # 生成文本提示
        text = self.generate_harmless_text(harmful_concept)
        
        # 生成视觉提示
        visual = self.encode_harmful_intent(harmful_concept)
        
        # 多模态融合
        input_data = {
            'text': text,
            'image': visual
        }
        
        # 生成图像
        output = self.target_model.generate(**input_data)
        
        return output
    
    def adversarial_optimize(self, image, model, steps=100):
        """对抗优化视觉提示"""
        perturbed = image.clone()
        
        for step in range(steps):
            perturbed.requires_grad = True
            
            # 前向传播
            output = model.encode_image(perturbed)
            
            # 计算损失（最大化有害内容生成概率）
            loss = self.compute_attack_loss(output)
            
            # 反向传播
            grad = torch.autograd.grad(loss, perturbed)[0]
            
            # 更新扰动
            perturbed = perturbed.detach() + 0.01 * grad.sign()
            perturbed = torch.clamp(perturbed, 0, 1)
        
        return perturbed
```

---

## 第12章 术语表

| 术语 | 解释 |
|------|------|
| **Multi-Modal Attack** | 多模态攻击，利用多种输入模态（文本+图像）进行攻击 |
| **Visual Prompt** | 视觉提示，用作模型输入的图像 |
| **Jailbreak** | 越狱攻击，绕过模型安全限制 |
| **T2I Model** | Text-to-Image Model，文本到图像生成模型 |
| **Adversarial Perturbation** | 对抗扰动，微小的、人眼不可见的修改 |
| **ASR** | Attack Success Rate，攻击成功率 |
| **Concept Encoding** | 概念编码，将抽象概念转换为可计算的表示 |
| **Semantic Alignment** | 语义对齐，确保不同模态输入语义一致 |
| **Transferability** | 迁移性，攻击在不同模型间的通用性 |
| **Safety Filter** | 安全过滤器，检测和阻止有害内容的机制 |

---

*本笔记由 AI 助手根据论文公开信息整理生成*
*最后更新: 2026-03-17*
