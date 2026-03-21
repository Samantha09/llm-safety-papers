# ESAA-Security: An Event-Sourced, Verifiable Architecture for Agent-Assisted Security Audits of AI-Generated Code

## 基本信息

- **论文标题**: ESAA-Security: An Event-Sourced, Verifiable Architecture for Agent-Assisted Security Audits of AI-Generated Code
- **作者**: Elzo Brito Dos Santos Filho 等
- **发表时间**: 2026年3月 (arXiv:2603.06365)
- **论文链接**: https://arxiv.org/abs/2603.06365
- **开源代码**: https://github.com/elzobrito/ESAA-Security
- **研究方向**: AI代码安全审计 / 智能体软件工程 / 可验证审计
- **会议/期刊**: arXiv预印本 (cs.CR)

---

## 研究背景

### AI代码生成的安全问题

AI辅助软件生成极大提升了开发效率，但一个持久工程问题也随之放大：系统可能在功能上正确，却在结构上存在安全隐患。在"vibe coding"环境下，开发速度加快，但系统在身份验证、授权机制、输入验证、密钥处理、会话控制、依赖管理、基础设施加固和AI特定风险处理等方面普遍薄弱。

### 现有LLM安全审计的局限

当前基于prompt的安全审查存在以下核心问题：

1. **覆盖不均**: 开放式LLM对话容易遗漏关键安全检查点，审计范围模糊
2. **弱可重复性**: 同一代码库多次审计结果可能不一致，缺乏确定性
3. **发现无据可查**: 漏洞发现以叙述性文本呈现，难以追溯依据
4. **缺乏不可变审计轨迹**: 无从验证"LLM声称发现该漏洞"的中间过程

### 核心洞察

> "安全审查不应被建模为与LLM的自由对话，而应是一个由契约和事件治理的证据导向审计过程。"

---

## 核心贡献

### 1. ESAA事件溯源治理内核

继承ESAA架构的核心思想，将**事件日志**而非可变仓库快照作为真实来源（Source of Truth）：

- **分离关注点**: 将启发式智能体认知与确定性状态变更分离
- **只追加事件日志**: 所有状态变更通过append-only事件记录
- **约束输出**: 智能体在受限协议下发出结构化意图
- **重放验证**: 通过重放和哈希验证一致性

### 2. ESAA-Security安全审计专用框架

领域专用 specialization，在四个阶段governed execution pipeline：

| 阶段 | 说明 | 关键活动 |
|------|------|----------|
| **Reconnaissance** | 侦察阶段 | 信息收集、代码库结构分析 |
| **Domain Audit Execution** | 领域审计执行 | 16个安全领域、95项可执行检查 |
| **Risk Classification** | 风险分类 | 漏洞清单、严重程度分类、风险矩阵 |
| **Final Reporting** | 最终报告 | Markdown/JSON审计报告、修复指导 |

### 3. 结构化输出产品

框架产生的可交付物：
- 结构化检查结果 (Structured Check Results)
- 漏洞清单 (Vulnerability Inventories)
- 严重程度分类 (Severity Classifications)
- 风险矩阵 (Risk Matrices)
- 修复指导 (Remediation Guidance)
- 执行摘要 (Executive Summaries)
- 最终审计报告 (Markdown/JSON)

---

## 技术架构

### 治理内核（Governance Kernel）

```
智能体发出结构化意图 → 编排器验证 → 只追加日志 → 重投影派生视图 → 重放验证完整性
```

1. **智能体（Agent）**: 在约束协议下发出结构化意图（不能自由生成文本）
2. **编排器（Orchestrator）**: 验证意图，持久化已接受输出
3. **只追加日志（Append-only Log）**: 不可变事件记录
4. **重投影（Reprojection）**: 从事件日志确定性重建派生视图
5. **重放验证（Replay Verification）**: 通过哈希验证一致性

### 26项任务 × 16个安全领域 × 95项可执行检查

| 类别 | 示例领域 |
|------|----------|
| 传统安全 | 注入防护、认证与会话管理、加密、错误处理 |
| Web安全 | XSS、CSRF、SQL注入、API安全 |
| AI特定风险 | Prompt注入、数据泄露、对抗输入 |

---

## 关键设计原则

### 证据导向（Evidence-Oriented）

漏洞发现必须满足以下条件才能成为审计结论的一部分：
1. ✅ 以结构化形式发出
2. ✅ 经契约验证
3. ✅ 追加到事件日志
4. ✅ 纳入派生视图
5. ✅ 保持在重放可验证完整性下

### 契约治理（Contract Governance）

智能体输出被约束为结构化模板，而非自由文本。这从根本上消除了"LLM生成流畅但无根据的叙述"的风险。

### 可审计性（Auditability by Construction）

最终报告天然可审计——每个结论都能从事件日志中重放得到验证。

---

## 评估框架

ESAA-Security的评估不止于"漏洞枚举"，还包括：

| 评估维度 | 说明 |
|----------|------|
| **Traceability** | 可追溯性 — 从检查项到结论的完整链路 |
| **Reproducibility** | 可重复性 — 相同代码库的多次审计结果一致 |
| **Coverage Explicitness** | 覆盖显式性 — 审计范围明确定义 |
| **Artifact Completeness** |  artifact完整性 — 所有交付物齐全 |
| **Remediation Usefulness** | 修复实用性 — 漏洞描述可操作 |

---

## 局限性

1. **检查项覆盖仍有限**: 95项检查无法覆盖所有安全领域，需持续扩展
2. **LLM能力依赖**: 审计质量仍受限于底层LLM的代码理解能力
3. **领域专用性**: 针对AI生成代码优化，对传统代码库的泛化性待验证
4. **性能开销**: 事件溯源架构可能带来额外的时间和存储开销

---

## 伦理声明

- 仅使用公开可用的AI生成代码和合成测试用例
- 未涉及真实敏感系统
- 开源实现可供社区审查和改进

---

## 核心要点

> **治理问题而非提示问题**: Agentic AI安全审计的核心挑战不是改进prompt，而是建立可保持问责性、可逆性和跨长时间自主操作状态一致性的治理内核。

> **证据优先于叙述**: 在ESAA-Security中，发现的漏洞不是因为LLM写了有说服力的文本而成为审计结论，而是因为它通过了结构化契约验证、事件持久化和重放验证。

---

*笔记由 AI 助手辅助整理，基于 arXiv 公开信息生成。*
*最后更新: 2026-03-21*
