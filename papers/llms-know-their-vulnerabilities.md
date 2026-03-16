# LLMs know their vulnerabilities

> **论文笔记**: LLMs-know-vulnerabilities
> **来源**: 飞书文档
> **上传时间**: 2026-03-17 00:58:25

---

## 基本信息

- **论文标题**: LLMs know their vulnerabilities: Uncover Safety Gaps through Natural Distribution Shifts
- **作者**: Qibing Ren, Hao Li, Dongrui Liu, Zhanxu Xie, Xiaoya Lu, Yu Qiao, Lei Sha, Junchi Yan, Lizhuang Ma, Jing Shao
- **机构**: 上海交通大学人工智能教育部重点实验室, 北京航空航天大学, 上海人工智能实验室
- **会议**: ACL 2025 Main Conference
- **arXiv**: https://arxiv.org/abs/2410.10700
- **代码**: https://github.com/AI45Lab/ActorAttack

## 核心贡献

1. **新漏洞类型**: 首次系统性揭示自然分布偏移漏洞
2. **ActorBreaker方法**: 基于行动者网络理论的攻击方法
3. **跨学科理论**: 将社会学行动者网络理论引入AI安全研究
4. **SOTA性能**: 平均ASR 77.7%，远超Crescendo (49.3%)

## 研究方法

### 行动者网络理论

基于布鲁诺·拉图尔的理论，将有害内容相关的实体分为六类：

| 类型 | 英文 | 定义 | 示例 |
|------|------|------|------|
| 创作 | Creation | 有害思想的起源 | 恐怖主义理论家 |
| 执行 | Execution | 实施者 | 犯罪分子 |
| 传播 | Distribution | 传播媒介 | 极端网站 |
| 接受 | Reception | 受众 | 追随者 |
| 促进 | Facilitation | 便利因素 | 工具、技术 |
| 规制 | Regulation | 规制实体 | 执法机构 |

### 两阶段攻击框架

1. **预攻击阶段**: 构建围绕种子有毒提示的网络
2. **攻击阶段**: 基于攻击线索生成多轮查询

## 实验结果

### 攻击成功率对比 (HarmBench)

| 方法 | GPT-3.5 | GPT-4o | GPT-o1 | Claude-3.5 | Llama-3-8B | Llama-3-70B | 平均 |
|------|---------|--------|--------|------------|------------|-------------|------|
| GCG | 55.8 | 12.5 | 0.0 | 3.0 | 34.5 | 17.0 | 20.5 |
| PAIR | 41.0 | 39.0 | 0.0 | 3.0 | 18.7 | 36.0 | 23.0 |
| Crescendo | 60.0 | 62.0 | 14.0 | 38.0 | 60.0 | 62.0 | 49.3 |
| **ActorBreaker** | **78.5** | **84.5** | **60.0** | **78.5** | **79.0** | **85.5** | **77.7** |

### 防御效果

| 防御方法 | Llama-3-8B ASR |
|----------|----------------|
| 无防御 | 78.0% |
| Circuit Breaker + 单轮数据 | 28.0% |
| Circuit Breaker + 多轮数据 | 16.5% |

## 关键发现

- SOTA性能：平均ASR 77.7%
- 跨模型有效：在GPT-o1上仍达60% ASR
- 高效率：平均仅需8.7次交互
- 高多样性：BERT相似度0.32-0.36

## 代码资源

- **代码**: https://github.com/AI45Lab/ActorAttack
- **论文**: https://arxiv.org/abs/2410.10700
