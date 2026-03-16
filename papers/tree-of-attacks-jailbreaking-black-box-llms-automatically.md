# Tree of Attacks: Jailbreaking Black-Box LLMs Automatically

> **论文笔记**: Tree-of-Attacks
> **来源**: 飞书文档
> **上传时间**: 2026-03-17 00:59:38

---

## 基本信息

- **论文标题**: Tree of Attacks: Jailbreaking Black-Box LLMs Automatically
- **简称**: TAP (Tree of Attacks with Pruning)
- **作者**: Anay Mehrotra, Manolis Zampetakis, Paul Kassianik, Blaine Nelson, Hyrum Anderson, Yaron Singer, Amin Karbasi
- **机构**: 哈佛大学、耶鲁大学、Robust Intelligence、微软
- **会议**: NeurIPS 2024
- **arXiv**: https://arxiv.org/abs/2312.02119
- **代码**: https://github.com/RICommunity/TAP

## 核心贡献

1. **TAP算法**: 树形攻击与剪枝机制，查询次数减少约50%
2. **两阶段剪枝**: 预查询剪枝 + 后查询剪枝
3. **高效率**: 平均仅需20-30次查询（PAIR需50-60次）
4. **高成功率**: GPT-4上84%攻击成功率

## 研究方法

### 三模型架构

| 角色 | 功能 | 典型模型 |
|------|------|----------|
| 攻击者 (Attacker) | 生成改进的攻击提示 | Vicuna-13B, GPT-3.5 |
| 评估者 (Evaluator) | 评估提示质量和响应 | GPT-4 |
| 目标 (Target) | 被攻击的LLM | GPT-4, GPT-4o, Llama-2 |

### 核心算法流程

```
初始化：以空提示作为根节点
迭代执行（直到成功或达到最大深度）：
  1. 分支（Branch）：攻击者生成多个改进提示
  2. 剪枝阶段1：评估者过滤偏离主题的提示
  3. 攻击与评估：向目标模型发送剩余提示
  4. 剪枝阶段2：保留得分最高的提示进入下一轮
返回：成功越狱的提示
```

## 实验结果

### 与基线方法对比

| 方法 | GPT-4 ASR | GPT-4-Turbo ASR | 平均查询次数 |
|------|-----------|-----------------|--------------|
| 手工越狱 (AIM) | 15% | 10% | 1 |
| GCG (迁移) | 47% | 42% | 500 |
| PAIR | 62% | 58% | 52 |
| **TAP** | **84%** | **82%** | **28** |

### 剪枝机制消融实验

| 配置 | 成功率 | 平均查询 | 效率提升 |
|------|--------|----------|----------|
| 完整TAP | 84% | 28 | 基准 |
| 无预查询剪枝 | 83% | 42 | -50% |
| 无后查询剪枝 | 81% | 38 | -36% |
| 无剪枝 | 80% | 51 | -82% |

### 不同目标模型攻击结果

| 模型 | ASR | 查询次数 | 模型类型 |
|------|-----|----------|----------|
| Vicuna-13B | 98% | 12 | 开源 |
| Llama-2-7B | 86% | 22 | 开源 |
| GPT-3.5 | 91% | 18 | 封闭源 |
| GPT-4 | 84% | 28 | 封闭源 |
| GPT-4o | 81% | 32 | 封闭源 |

## 关键发现

- 树形搜索显著提升探索效率
- 剪枝是提高效率的关键（减少40-60%查询）
- 评估者质量影响攻击效果
- 攻击具有一定迁移性

## 代码资源

- **GitHub**: https://github.com/RICommunity/TAP
- **集成**: 已被集成到JailbreakBench和Giskard Hub
