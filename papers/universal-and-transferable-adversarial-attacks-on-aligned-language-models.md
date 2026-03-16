# Universal and Transferable Adversarial Attacks on Aligned Language Models (GCG攻击)

> **论文笔记**: GCG
> **来源**: 飞书文档
> **上传时间**: 2026-03-17 01:00:47

---

## 基本信息

- **论文标题**: Universal and Transferable Adversarial Attacks on Aligned Language Models
- **简称**: GCG (Greedy Coordinate Gradient)
- **作者**: Andy Zou, Zifan Wang, Nicholas Carlini, Milad Nasr, J. Zico Kolter, Matt Fredrikson
- **机构**: Carnegie Mellon University, Center for AI Safety, Google DeepMind
- **arXiv**: https://arxiv.org/abs/2307.15043

## 核心贡献

1. **GCG算法**: 结合贪婪坐标下降与梯度信息的离散优化方法
2. **可迁移攻击**: 首次证明自动生成的对抗提示可以跨模型迁移
3. **AdvBench基准**: 新的对抗攻击评估基准
4. **揭示脆弱性**: 证明当前对齐方法在对抗攻击面前不够鲁棒

## 研究方法

### GCG算法

**关键洞察**: 如果能让模型以"Sure, here is..."开始响应，模型就会切换到"执行模式"

**算法流程**:
```
输入: 初始提示 x_{1:n}, 可修改位置 I, 迭代次数 T
对于 t = 1 到 T:
    对于每个 i ∈ I:
        X_i = Top-k(-∇_{e_{x_i}} L(x_{1:n}))
    
    对于 b = 1 到 B:
        x̃_{1:n}^{(b)} = x_{1:n}
        x̃_i^{(b)} = Uniform(X_i)
    
    x_{1:n} = x̃_{1:n}^{(b*)}, 其中 b* = argmin_b L(x̃_{1:n}^{(b)})
```

### 多提示多模型攻击

- 同时优化多个提示
- 在多个模型上联合训练
- 增量学习策略

## 实验结果

### 白盒攻击结果

| 模型 | 方法 | Harmful Strings ASR | Harmful Behavior ASR |
|------|------|---------------------|----------------------|
| Vicuna (7B) | GBDA | 0.0% | 4.0% |
| Vicuna (7B) | PEZ | 0.0% | 11.0% |
| Vicuna (7B) | AutoPrompt | 25.0% | 95.0% |
| Vicuna (7B) | **GCG** | **88.0%** | **99.0%** |
| LLaMA-2 (7B) | **GCG** | **57.0%** | **56.0%** |

### 黑盒迁移攻击

| 源模型 | 目标模型 | ASR |
|--------|----------|-----|
| Vicuna-7B+13B | GPT-3.5 | 87.9% |
| Vicuna-7B+13B | GPT-4 | 53.6% |
| Vicuna-7B+13B | PaLM-2 | 66% |
| Vicuna-7B+13B | Claude-2 | 2.1% |

### 消融实验

| 配置 | Vicuna ASR | LLaMA-2 ASR |
|------|------------|-------------|
| 完整GCG | 88.0% | 57.0% |
| 仅单坐标优化 | 25.0% | 3.0% |
| 无多提示训练 | ~70% | ~40% |
| 无多模型训练 | ~60% | ~35% |

## 关键发现

- 全坐标搜索是最重要的创新
- 多提示训练显著提升攻击通用性
- 多模型训练是实现迁移攻击的关键
- Claude-2显示出显著更强的鲁棒性

## 代码资源

- **GitHub**: https://github.com/llm-attacks/llm-attacks
- **演示**: https://llm-attacks.org/
- **衍生实现**: nanoGCG, EasyJailbreak
