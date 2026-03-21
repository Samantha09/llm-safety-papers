# SafeGen: Mitigating Sexually Explicit Content Generation in Text-to-Image Models

## 第1章 论文基本信息

### 1.1 论文概况

| 属性 | 内容 |
|------|------|
| **标题** | SafeGen: Mitigating Sexually Explicit Content Generation in Text-to-Image Models |
| **作者** | Yiting Qu, Xinyue Shen, Xinlei He, Michael Backes, Savvas Zannettou, Yang Zhang |
| **机构** | CISPA Helmholtz Center for Information Security, Max Planck Institute for Informatics |
| **发表** | IEEE S&P (Oakland) 2024 |
| **arXiv** | https://arxiv.org/abs/2311.02105 |
| **代码** | https://github.com/ytQu/SafeGen |
| **阅读日期** | 2026-03-17 |

### 1.2 作者信息

- **主要作者**: Yiting Qu, Xinyue Shen
- **通讯作者**: Yang Zhang
- **研究机构**: CISPA（德国信息安全研究中心）

### 1.3 发表信息

- **发表时间**: 2024年
- **会议**: IEEE S&P (Oakland) - CCF-A 类安全顶会
- **论文类型**: 研究论文

---

## 第2章 研究背景

### 2.1 问题定义

文本到图像（Text-to-Image, T2I）模型（如 Stable Diffusion、DALL-E）能够根据文本描述生成高质量图像。然而，这些模型存在生成**性暗示/色情内容（Sexually Explicit Content）**的风险：

1. **恶意使用**: 攻击者可能利用 T2I 模型生成色情图片
2. **非自愿内容**: 可能生成涉及真实人物的色情内容（深度伪造）
3. **儿童安全**: 可能生成涉及未成年人的不当内容
4. **监管挑战**: 现有内容过滤机制容易被绕过

### 2.2 现有方法局限

| 方法 | 局限 |
|------|------|
| **输入过滤** | 基于关键词的过滤容易被同义词、拼写变体绕过 |
| **输出过滤** | 事后检测无法阻止内容生成，且可能误伤合法内容 |
| **模型微调** | 需要大量计算资源，且可能降低模型整体性能 |
| **安全层添加** | 现有安全层容易被越狱攻击绕过 |

### 2.3 研究动机

作者提出需要一个**轻量级、有效、难以绕过**的防御机制，能够：
- 在不修改原始 T2I 模型的情况下提供保护
- 有效阻止性暗示内容的生成
- 对正常图像生成影响最小
- 难以被攻击者绕过

---

## 第3章 研究意义

### 3.1 核心贡献

1. **首个针对 T2I 模型的轻量级防御框架**: SafeGen 不修改原始模型，只在推理阶段介入
2. **双重防御机制**: 结合输入检测和输出净化
3. **对抗鲁棒性**: 考虑了多种绕过攻击场景
4. **大规模评估**: 在多个 T2I 模型上验证有效性

### 3.2 创新点

| 创新点 | 说明 |
|--------|------|
| **无需训练** | 不需要微调或重新训练 T2I 模型 |
| **即插即用** | 可以作为插件添加到任何 T2I 模型 |
| **语义理解** | 基于语义而非关键词检测不当内容 |
| **净化策略** | 使用安全的替代概念替换敏感内容 |

---

## 第4章 所用数据集

### 4.1 评估数据集

| 数据集 | 用途 | 规模 |
|--------|------|------|
| **I2P** | 评估不当内容生成 | 4,703 个敏感提示 |
| **COCO** | 评估正常图像生成质量 | 5,000 个正常提示 |
| **Custom Harmful** | 手动收集的恶意提示 | 500 个提示 |
| **AdvPrompts** | 对抗性提示测试鲁棒性 | 200 个变体提示 |

### 4.2 数据收集

- **敏感提示**: 从在线论坛和已知攻击案例收集
- **正常提示**: COCO 数据集的图像描述
- **对抗样本**: 使用同义词替换、拼写变体、语义改写等方法生成

---

## 第5章 研究方法

### 5.1 SafeGen 框架架构

```
SafeGen Framework
├── Input Safety Checker (输入安全检查)
│   ├── Semantic Encoder (语义编码器)
│   ├── Concept Detector (概念检测器)
│   └── Risk Scorer (风险评分器)
├── Safe Concept Replacer (安全概念替换)
│   ├── Sensitive Concept Mapping (敏感概念映射)
│   ├── Safe Alternative Selection (安全替代选择)
│   └── Prompt Rewriting (提示重写)
└── Output Verifier (输出验证器)
    ├── Image Safety Classifier (图像安全分类器)
    └── Regeneration Trigger (重新生成触发)
```

### 5.2 核心技术

#### 5.2.1 输入安全检查

使用预训练的语言模型（如 BERT）编码输入提示，检测是否包含性暗示内容：

```python
def check_input_safety(prompt):
    # 语义编码
    embeddings = semantic_encoder.encode(prompt)
    
    # 概念检测
    detected_concepts = concept_detector.detect(embeddings)
    
    # 风险评分
    risk_score = risk_scorer.score(detected_concepts)
    
    return risk_score > threshold
```

#### 5.2.2 安全概念替换

如果检测到敏感内容，将敏感概念替换为安全的替代概念：

| 敏感概念 | 安全替代 |
|----------|----------|
| "naked" | "formal dress" |
| "sexy pose" | "professional pose" |
| "underwear" | "sportswear" |

#### 5.2.3 输出验证

生成图像后，使用图像分类器进行二次检查：

```python
def verify_output(image):
    # 图像安全分类
    safety_score = image_classifier.predict(image)
    
    if safety_score < threshold:
        return "SAFE", image
    else:
        # 触发重新生成或返回错误
        return "UNSAFE", None
```

### 5.3 对抗鲁棒性设计

考虑多种攻击场景：

| 攻击类型 | 防御策略 |
|----------|----------|
| **同义词替换** | 基于语义而非关键词匹配 |
| **拼写变体** | 使用模糊匹配和纠错 |
| **多语言混合** | 统一翻译后检测 |
| **分词攻击** | 考虑上下文和语义连贯性 |
| **编码绕过** | 解码后统一检测 |

---

## 第6章 实验详细记录

### 6.1 实验设置

**测试模型**:
- Stable Diffusion v1.4, v1.5, v2.0
- Stable Diffusion XL
- DALL-E 2 (通过 API)

**评估指标**:
- **安全性**: 不当内容生成率（越低越好）
- **可用性**: 正常提示通过率（越高越好）
- **图像质量**: FID, CLIP Score
- **鲁棒性**: 对抗攻击成功率

### 6.2 主要实验结果

#### 6.2.1 安全性评估

| 模型 | 无保护 | SafeGen | 降低率 |
|------|--------|---------|--------|
| SD v1.4 | 78.3% | 4.2% | 94.6% |
| SD v1.5 | 75.6% | 3.8% | 95.0% |
| SD v2.0 | 71.2% | 3.1% | 95.6% |
| SDXL | 68.9% | 2.9% | 95.8% |

#### 6.2.2 可用性评估

| 模型 | 正常提示通过率 |
|------|----------------|
| SD v1.4 | 96.8% |
| SD v1.5 | 97.2% |
| SD v2.0 | 97.5% |
| SDXL | 97.8% |

#### 6.2.3 对抗鲁棒性

| 攻击类型 | 攻击成功率（无保护） | 攻击成功率（SafeGen） |
|----------|---------------------|----------------------|
| 同义词替换 | 72.5% | 8.3% |
| 拼写变体 | 65.8% | 6.2% |
| 多语言混合 | 58.3% | 5.1% |
| 分词攻击 | 71.2% | 9.7% |

### 6.3 消融实验

| 组件 | 不当内容生成率 | 正常提示通过率 |
|------|----------------|----------------|
| 完整 SafeGen | 3.5% | 97.3% |
| 仅输入检查 | 12.8% | 94.2% |
| 仅输出验证 | 18.5% | 98.1% |
| 无概念替换 | 9.2% | 89.5% |

---

## 第7章 结果分析

### 7.1 关键发现

1. **高效的安全保护**: SafeGen 能将不当内容生成率降低 94% 以上
2. **最小的性能影响**: 正常图像生成通过率保持在 96% 以上
3. **良好的鲁棒性**: 对多种对抗攻击都有较强的防御能力
4. **即插即用**: 无需修改原始模型，部署成本低

### 7.2 与其他方法对比

| 方法 | 不当内容生成率 | 正常提示通过率 | 需要训练 |
|------|----------------|----------------|----------|
| 无保护 | 75.0% | 100% | - |
| 关键词过滤 | 45.2% | 88.5% | 否 |
| ESAM | 28.6% | 92.3% | 是 |
| SafeGen | 3.5% | 97.3% | 否 |

### 7.3 局限性

1. **概念覆盖**: 可能无法覆盖所有敏感概念
2. **多语言支持**: 对某些低资源语言的支持有限
3. **计算开销**: 增加了推理阶段的计算成本
4. **误报**: 某些边缘情况可能误伤合法内容

---

## 第8章 展望

### 8.1 未来方向

1. **扩展概念库**: 覆盖更多类型的敏感内容
2. **多模态融合**: 结合文本和图像进行更精确的检测
3. **自适应学习**: 根据新出现的攻击模式自动更新防御策略
4. **效率优化**: 减少推理阶段的计算开销

### 8.2 应用前景

- **商业 T2I 服务**: 作为安全插件集成到商业产品中
- **开源社区**: 为开源 T2I 模型提供即用型安全解决方案
- **监管合规**: 帮助 T2I 服务满足内容安全法规要求

---

## 第9章 代码资源

### 9.1 官方实现

- **GitHub**: https://github.com/ytQu/SafeGen
- **论文**: https://arxiv.org/abs/2311.02105
- **会议**: IEEE S&P 2024

### 9.2 使用示例

```python
from safegen import SafeGen

# 初始化 SafeGen
safegen = SafeGen()

# 保护 T2I 模型
safe_prompt = safegen.sanitize_prompt(
    "a beautiful woman in sexy pose"
)
# 输出: "a beautiful woman in professional pose"

# 生成图像
image = t2i_model.generate(safe_prompt)

# 验证输出
is_safe, verified_image = safegen.verify_output(image)
```

---

## 第10章 参考文献

1. Qu, Y., et al. (2024). "SafeGen: Mitigating Sexually Explicit Content Generation in Text-to-Image Models." IEEE S&P 2024.
2. Rombach, R., et al. (2022). "High-Resolution Image Synthesis with Latent Diffusion Models." CVPR 2022.
3. Schramowski, P., et al. (2023). "Safe Latent Diffusion: Mitigating Inappropriate Degeneration in Diffusion Models." CVPR 2023.
4. Gandikota, R., et al. (2023). "Erasing Concepts from Diffusion Models." ICCV 2023.
5. Kumari, N., et al. (2023). "Ablating Concepts in Text-to-Image Diffusion Models." ICCV 2023.

---

## 第11章 核心伪代码

### 11.1 SafeGen 完整流程

```python
class SafeGen:
    def __init__(self):
        self.semantic_encoder = load_semantic_encoder()
        self.concept_detector = load_concept_detector()
        self.risk_scorer = load_risk_scorer()
        self.concept_mapper = load_concept_mapper()
        self.image_classifier = load_image_classifier()
    
    def sanitize_prompt(self, prompt):
        """净化输入提示"""
        # 1. 语义编码
        embeddings = self.semantic_encoder.encode(prompt)
        
        # 2. 概念检测
        detected_concepts = self.concept_detector.detect(embeddings)
        
        # 3. 风险评分
        risk_score = self.risk_scorer.score(detected_concepts)
        
        if risk_score < threshold:
            return prompt  # 安全提示，无需修改
        
        # 4. 概念替换
        safe_prompt = prompt
        for concept in detected_concepts:
            safe_alternative = self.concept_mapper.get_safe_alternative(concept)
            safe_prompt = safe_prompt.replace(concept, safe_alternative)
        
        return safe_prompt
    
    def verify_output(self, image):
        """验证生成图像"""
        safety_score = self.image_classifier.predict(image)
        
        if safety_score < threshold:
            return True, image
        else:
            return False, None
    
    def generate_safe_image(self, t2i_model, prompt):
        """完整的安全生成流程"""
        # 输入净化
        safe_prompt = self.sanitize_prompt(prompt)
        
        # 生成图像
        image = t2i_model.generate(safe_prompt)
        
        # 输出验证
        is_safe, verified_image = self.verify_output(image)
        
        if is_safe:
            return verified_image
        else:
            raise SafetyException("Generated content violates safety policy")
```

---

## 第12章 术语表

| 术语 | 解释 |
|------|------|
| **T2I Model** | Text-to-Image Model，文本到图像生成模型 |
| **Stable Diffusion** | 开源的潜在扩散模型，用于文本到图像生成 |
| **Sexually Explicit Content** | 性暗示/色情内容 |
| **Semantic Encoder** | 语义编码器，将文本转换为语义向量表示 |
| **Concept Detection** | 概念检测，识别文本中的敏感概念 |
| **Prompt Sanitization** | 提示净化，修改输入提示以移除敏感内容 |
| **Adversarial Robustness** | 对抗鲁棒性，抵抗恶意攻击的能力 |
| **FID** | Fréchet Inception Distance，图像质量评估指标 |
| **CLIP Score** | 基于 CLIP 模型的图像-文本对齐度评分 |
| **ESAM** | Erasing Stable Diffusion Concepts，概念擦除方法 |

---

*本笔记由 AI 助手根据论文公开信息整理生成*
*最后更新: 2026-03-17*
