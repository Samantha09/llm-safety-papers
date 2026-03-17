# 论文索引

<p align="center">
  <img src="https://img.shields.io/badge/Total-6%20Papers-blue?style=flat-square" alt="Total Papers">
  <img src="https://img.shields.io/badge/Complete-2%20Notes-success?style=flat-square" alt="Complete">
  <img src="https://img.shields.io/badge/Pending-4%20Notes-orange?style=flat-square" alt="Pending">
</p>

本目录包含 LLM 安全领域的论文阅读笔记，按类别和状态整理。

---

## 📋 快速索引表

| 序号 | 论文标题 | 会议/年份 | 类别 | 阅读日期 | 状态 |
|:----:|----------|:---------:|------|:--------:|:----:|
| 1 | [Harnessing Task Overload: Scalable Jailbreak Attacks](./harnessing-task-overload.md) | arXiv 2024 | 越狱攻击 | 2026-03-11 | ✅ |
| 2 | [MLLM-Protector: Ensuring MLLM's Safety without Hurting Performance](./mllm-protector.md) | arXiv 2024 | 多模态安全 | 2026-03-11 | ✅ |
| 3 | [AutoDAN: Generating Stealthy Jailbreak Prompts](./autodan.md) | NeurIPS 2024 | 越狱攻击 | 2026-03-11 | 📝 |
| 4 | [Nothing in Excess: Mitigating Exaggerated Safety](./nothing-in-excess.md) | ICLR 2025 | 安全对齐 | 2026-03-11 | 📝 |
| 5 | [JailbreakBench: Open Robustness Benchmark](./jailbreakbench.md) | arXiv 2024 | 评估基准 | 2026-03-11 | 📝 |
| 6 | [HarmBench: Standardized Evaluation Framework](./harmbench.md) | ICLR 2024 | 评估基准 | 2026-03-11 | 📝 |

---

## 🏷️ 按标签分类

### 攻击类型

| 标签 | 论文数量 | 论文列表 |
|------|:--------:|----------|
| 🔓 越狱攻击 | 2 | Harnessing Task Overload, AutoDAN |
| 🎯 对抗攻击 | 1 | AutoDAN |
| 🧠 提示注入 | 0 | - |

### 防御类型

| 标签 | 论文数量 | 论文列表 |
|------|:--------:|----------|
| 🛡️ 安全对齐 | 1 | Nothing in Excess |
| 🔍 输出检测 | 1 | MLLM-Protector |
| 🧪 红队测试 | 0 | - |

### 评估基准

| 标签 | 论文数量 | 论文列表 |
|------|:--------:|----------|
| 📊 评估基准 | 2 | JailbreakBench, HarmBench |

### 其他标签

| 标签 | 论文数量 | 论文列表 |
|------|:--------:|----------|
| 🖼️ 多模态 | 1 | MLLM-Protector |
| ⚡ 资源攻击 | 1 | Harnessing Task Overload |
| 🔄 过度拒绝 | 1 | Nothing in Excess |

---

## 📊 按状态分类

### ✅ 完整笔记（2篇）

包含所有标准章节的详细笔记：

1. **[Harnessing Task Overload](./harnessing-task-overload.md)** - 资源饱和攻击
   - 核心思想：通过占用计算资源绕过安全机制
   - 攻击方式：任务过载导致安全机制失效
   - 关键词：`越狱攻击` `资源饱和` `计算开销`

2. **[MLLM-Protector](./mllm-protector.md)** - 多模态模型安全保护
   - 核心思想：输出端检测与解毒
   - 特点：不损害模型性能的安全保护
   - 关键词：`多模态` `输出检测` `轻量级`

### 📝 待补充笔记（4篇）

基础信息已录入，详细分析待完善：

3. **[AutoDAN](./autodan.md)** - 生成隐蔽的越狱提示
   - 会议：NeurIPS 2024
   - 关键词：`对抗生成` `隐蔽攻击` `黑盒`

4. **[Nothing in Excess](./nothing-in-excess.md)** - 缓解过度安全对齐
   - 会议：ICLR 2025
   - 关键词：`过度拒绝` `安全对齐` `平衡`

5. **[JailbreakBench](./jailbreakbench.md)** - 越狱攻击评估基准
   - 会议：arXiv 2024
   - 关键词：`基准测试` `评估框架` `鲁棒性`

6. **[HarmBench](./harmbench.md)** - 标准化安全评估框架
   - 会议：ICLR 2024
   - 关键词：`安全评估` `标准化` `自动化`

---

## 📁 待处理论文（飞书云盘）

以下论文存储在飞书云盘中，格式为快捷方式，需要单独处理：

| 论文标题 | 预计类别 |
|----------|----------|
| Automated Progressive Red Teaming (APRT) | 红队测试 |
| Cold-Attack: Jailbreaking LLMs with Stealth and Controllability | 越狱攻击 |
| Jailbreaking Black Box LLMs in Twenty Queries (PAIR) | 越狱攻击 |
| LLMs know their vulnerabilities | 安全分析 |
| Sleeper Agents: Training Deceptive LLMs | 后门攻击 |
| LLM安全与隐私综述 | 综述 |
| Tree of Attacks: Jailbreaking Black-Box LLMs Automatically | 红队测试 |
| Universal and Transferable Adversarial Attacks (GCG) | 对抗攻击 |
| Under the Influence | 提示注入 |
| Alignment-Weighted DPO | 安全对齐 |
| AuditBench | 评估基准 |

---

## 🔍 使用指南

### 查找论文

- **按攻击类型**：查看「按标签分类」→ 攻击类型
- **按防御方法**：查看「按标签分类」→ 防御类型
- **按完成状态**：查看「按状态分类」
- **按会议等级**：查看快速索引表的「会议/年份」列

### 阅读建议

1. **新手入门**：先读评估基准类论文（JailbreakBench, HarmBench）了解评测方法
2. **攻击研究**：重点看 Harnessing Task Overload 和 AutoDAN
3. **防御研究**：重点看 MLLM-Protector 和 Nothing in Excess

### 笔记格式

完整笔记包含以下章节：
- 基本信息（标题、作者、会议、链接）
- 研究背景与意义
- 所用数据集
- 研究方法
- 实验详细记录
- 结果分析
- 展望
- 代码资源
- 参考文献

---

## 📝 维护说明

- 最后更新：2026-03-17
- 维护者：AI 助手 + 人工审核
- 更新频率：随阅读进度同步更新

---

*返回 [项目主页](../README.md)*
