# Automated Progressive Red Teaming

> **论文笔记**: APRT
> **来源**: 飞书文档
> **上传时间": 2026-03-17 00:56:11

---

## 基本信息

- **论文标题**: Automated Progressive Red Teaming
- **作者**: Bojian Jiang, Yi Jing, Tianhao Shen, Tong Wu, Qing Yang, Deyi Xiong
- **机构**: 天津大学智能与计算学部, 度小满金融
- **会议**: COLING 2025 (已接收)
- **arXiv**: https://arxiv.org/abs/2407.03876
- **代码**: https://github.com/tjunlp-lab/APRT

## 核心贡献

1. **APRT框架**: 首个将红队测试框架化为可有效学习任务的自动化渐进式红队测试框架
2. **三模块架构**: 意图扩展LLM + 意图隐藏LLM + 邪恶制造者(Evil Maker)
3. **AER评估指标**: 提出Attack Effectiveness Rate，解决ASR指标的局限性
4. **强攻击效果**: Llama-3-8B上54%成功率，GPT-4o达50%，Claude-3.5达39%

## 研究方法

### 三模块架构

```
意图扩展LLM → Evil Maker → 意图隐藏LLM → 目标LLM
                ↑                           ↓
                └────── Reward LLMs ←───────┘
```

### 渐进式训练流程

1. 意图扩展: 生成多样化攻击提示
2. 样本过滤: Evil Maker过滤无效提示
3. 意图隐藏: 将有害意图转化为欺骗性提示
4. 训练数据选择: 主动学习策略选择有价值样本
5. 模型更新: 基于反馈更新意图隐藏LLM

## 实验结果

| 方法 | Llama-3-8B | GPT-4o | Claude-3.5 |
|------|------------|--------|------------|
| GCG | ~30% | ~15% | ~10% |
| PAIR | ~35% | ~20% | ~15% |
| TAP | ~40% | ~25% | ~20% |
| AutoDAN | ~45% | ~30% | ~25% |
| MART | ~48% | ~35% | ~28% |
| **APRT** | **54%** | **50%** | **39%** |

## 关键发现

- 渐进训练显著提升攻击效果（单轮38% → 4轮54%）
- 在开源模型训练后可迁移到闭源商业模型
- AER指标与人类评估高度一致（95%+一致性）

## 术语表

| 术语 | 定义 |
|------|------|
| Red Teaming | 通过模拟攻击发现系统安全漏洞的方法 |
| AER | Attack Effectiveness Rate，攻击有效率 |
| Intention Hiding | 将有害意图隐藏在看似无害的表述中 |
| Active Learning | 优先选择难样本进行训练的策略 |
