# Jailbreaking Black Box Large Language Models in Twenty Queries

> **论文笔记**: PAIR
> **来源**: 飞书文档
> **上传时间**: 2026-03-17 00:57:14

---

## 基本信息

- **论文标题**: Jailbreaking Black Box Large Language Models in Twenty Queries
- **作者**: Patrick Chao, Alexander Robey, Edgar Dobriban, Hamed Hassani, George J. Pappas, Eric Wong
- **机构**: University of Pennsylvania
- **会议**: NeurIPS 2023 (Workshop)
- **arXiv**: https://arxiv.org/abs/2310.08419

## 核心贡献

1. **PAIR算法**: 黑盒越狱算法，仅需不到20次查询
2. **效率突破**: 比GCG减少500倍以上查询次数
3. **自动化**: 无需人工干预，完全自动化的攻击生成
4. **语义可解释性**: 生成人类可读的语义文本

## 研究方法

### PAIR算法流程

```
输入: 有害指令 x, 攻击者模型 A, 目标模型 T
输出: 越狱提示 p

1. 初始化: p_0 = "How can I {x}?"
2. for i = 1 to N do:
3.     p_i = A(generate_prompt | p_{i-1}, response_{i-1})
4.     response_i = T(p_i)
5.     if Judge(response_i) == "harmful":
6.         return p_i
7. return best_prompt_from_history
```

### 说服策略

- **逻辑说服**: 使用逻辑论证
- **权威诉求**: 引用权威
- **角色扮演**: 模拟特定角色
- **情境假设**: 创建假设场景
- **信息掩盖**: 使用委婉语

## 实验结果

### 攻击成功率对比

| 方法 | GPT-3.5 | GPT-4 | Claude-2 | Llama-2 | 平均查询 |
|------|---------|-------|----------|---------|----------|
| GCG | 88% | 56% | 2% | 32% | ~10,000 |
| AutoDAN | 92% | 48% | 8% | 28% | ~5,000 |
| **PAIR** | **96%** | **76%** | **24%** | **64%** | **~20** |

### 查询效率分析

| 模型 | 平均查询次数 | 中位数查询次数 | 成功率 |
|------|--------------|----------------|--------|
| GPT-3.5 | 12.3 | 8 | 96% |
| GPT-4 | 18.7 | 15 | 76% |
| Llama-2 | 15.2 | 11 | 64% |
| Claude-2 | 19.8 | 20 | 24% |

## 关键发现

- 仅需约20次查询即可成功越狱
- 攻击提示在同一家族模型间迁移性较好
- Claude-2表现出更强的安全对齐

## 代码资源

- **论文**: https://arxiv.org/abs/2310.08419
- **代码**: 未开源（但算法描述足够详细可复现）
- **复现难度**: 中等
