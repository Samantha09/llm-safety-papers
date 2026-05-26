# Toward Securing AI Agents Like Operating Systems

## 1. 基本信息

| 项目 | 内容 |
|------|------|
| **论文标题** | Toward Securing AI Agents Like Operating Systems |
| **作者** | Lukas Pirch, Micha Horlboge, Patrick Großmann, Syeda Mahnur Asif, Klim Kireev, Thorsten Holz, Konrad Rieck |
| **arXiv链接** | https://arxiv.org/abs/2605.14932 |
| **PDF链接** | https://arxiv.org/pdf/2605.14932 |
| **研究方向** | LLM Agent安全 / OS安全类比 |
| **会议/期刊** | arXiv (2026, under submission) |
| **arXiv编号** | 2605.14932v1 |
| **领域** | Cryptography and Security (cs.CR) |

---

## 2. 英文摘要原文 (arXiv Abstract)

> Autonomous agents based on large language models (LLMs) are rapidly emerging as a general-purpose technology, with recent systems such as OpenClaw extending their capabilities through broad tool use, third-party skills, and deeper integration into user environments. At the same time, these agentic systems introduce substantial security risks by combining unconstrained capabilities with access to sensitive user data. In this work, we investigate the security of LLM-based agents through the lens of operating systems. We argue that both face strikingly similar challenges in isolating resources, separating privileges, and mediating communication.

> Guided by this perspective, we survey the current landscape of open-source agents, derive a unified agent architecture, and systematically analyze potential attack vectors. To validate this analysis, we conduct a case study evaluating four widely used OpenClaw-like agents. Even under modest attacker capabilities, we find that several protection mechanisms fail in practice and that secure operation requires detailed system knowledge and careful configuration. However, we also observe that while some agentic capabilities remain insecure by design, many vulnerabilities can be mitigated using well-established techniques from operating system security. We conclude with a set of recommendations for the secure design of agentic systems.

---

## 3. 核心贡献

1. **OS视角的安全分析**: 首次将LLM Agent安全问题类比为操作系统安全问题
2. **统一Agent架构**: 推导出一个统一的Agent架构模型
3. **系统性攻击面分析**: 系统分析潜在攻击向量
4. **OpenClaw案例研究**: 对四个广泛使用的OpenClaw类Agent进行评估
5. **缓解建议**: 提出基于OS安全经典技术的缓解方案

---

## 4. 研究背景

### 4.1 LLM Agent的崛起

LLM驱动的自主Agent正在成为通用技术，以OpenClaw为代表的系统通过广泛的工具使用、第三方技能和深入的用户环境集成来扩展能力。

### 4.2 安全风险

这些Agent系统通过将不受限制的能力与对敏感用户数据的访问相结合，引入了重大的安全风险。

### 4.3 OS类比的核心观点

操作系统和LLM Agent面临着惊人相似的挑战：
- **资源隔离** (Isolating resources)
- **特权分离** (Separating privileges)
- **通信中介** (Mediating communication)

---

## 5. 论文亮点

- 直接以OpenClaw作为研究对象
- 发现即便在中等攻击能力下，多个保护机制也会失效
- 安全操作需要详细的系统知识和仔细的配置
- 许多漏洞可以通过操作系统安全中的经典技术来缓解

---

*本文档由 LLM Safety 论文阅读助手自动生成*
*论文来源：arXiv:2605.14932*
*添加日期：2026-05-25*
