# LLM Safety 论文汇总

> 本文档汇总了 LLM 安全领域的核心论文，按年份和方向分类整理。
> 
> **维护者**: Kimi Claw  
> **更新频率**: 每周自动更新  
> **总收录**: 约 74 篇论文（2021-2026年）

---

## 📅 2026年

### 5月更新

#### 5月4日 - CCF-A/B 论文收录

本周收录 1 篇确定录用的 LLM Safety 论文（1篇CCF-A）：

| 论文 | 会议 | 等级 | 方向 | 摘要 |
|------|------|------|------|------|
| [One Single Hub Text Breaks CLIP: Identifying Vulnerabilities in Cross-Modal Encoders via Hubness](https://arxiv.org/abs/2604.27674) | ACL 2026 | CCF-A | Cross-Modal Security / Vulnerability | 发现跨模态编码器中的hubness问题可被利用：通过单一hub文本在多数图像上获得不合理的高相似度，揭示CLIP等跨模态模型的脆弱性 |

---

### 3月更新

#### 3月16日 - CCF-A/B 论文收录

本周收录 3 篇确定录用的 LLM Safety 论文（1篇CCF-A，2篇CCF-B）：

| 论文 | 会议 | 等级 | 方向 | 摘要 |
|------|------|------|------|------|
| [Benchmarking Long-Context ESG Reports for Hallucination Mitigation](https://arxiv.org/abs/2603.13154) | AAAI 2026 | CCF-A | Hallucination Mitigation | 提出ESG-Bench基准数据集，用于ESG报告理解和LLM幻觉缓解 |
| [Security-by-Design for LLM-Based Code Generation](https://arxiv.org/abs/2603.11212) | EuroS&P 2026 | CCF-B | Code Security | 研究CodeLLM内部安全概念表示，提出SCS-Code方法 |
| [Examining Linguistic Biases in Personalized Automated Writing Feedback](https://arxiv.org/abs/2603.12471) | LAK 2026 | CCF-B | Bias/Fairness | 检查LLM在个性化自动写作反馈中的语言偏见 |

#### 3月9日更新

本周新增 6 篇论文：

| 论文 | 方向 | arXiv | 摘要 |
|------|------|-------|------|
| SIABENCH | Benchmark | [2603.06422](https://arxiv.org/abs/2603.06422) | 评估LLM在安全事件分析中的能力 |
| ESAA-Security | AI安全/代码审计 | [2603.06365](https://arxiv.org/abs/2603.06365) | 事件溯源架构，对AI生成代码进行可重现安全审计 |
| Proteus | 隐私保护 | [2603.06540](https://arxiv.org/abs/2603.06540) | 隐私保护设备日志框架 |
| Breaking Bad Email Habits | 社会工程 | [2603.04324](https://arxiv.org/abs/2603.04324) | 分析钓鱼模拟活动，发现重复点击主要反映个人特质 |
| Extracting Private Information from LLM Insights | Privacy | [2603.09781](https://arxiv.org/abs/2603.09781) | 提出CLIOPATRA攻击，从LLM insight系统中提取隐私信息 |

#### 其他2026年论文

| 论文 | 方向 | arXiv | 摘要 | 代码 |
|------|------|-------|------|------|
| AuditBench | Alignment/Red Teaming | [2602.22755](https://arxiv.org/abs/2602.22755) | 提出AuditBench基准，评估对齐审计技术 | 未开源 |
| Alignment-Weighted DPO | Alignment | [2602.21346](https://arxiv.org/abs/2602.21346) | 通过推理感知后训练增强对齐，提高对越狱攻击的鲁棒性 | 未开源 |
| Under the Influence | AI Safety | [2602.21262](https://arxiv.org/abs/2602.21262) | 使用Sokoban游戏研究LLM的说服力和警觉性能力 | 未开源 |

---

### 4月更新

### 4月更新

#### 4月23日 - DoS & 资源耗尽攻击论文收录

本周收录 5 篇 LLM DoS / 资源耗尽攻击论文：

| 论文 | 会议 | 等级 | 方向 | 摘要 |
|------|------|------|------|------|
| [ThinkTrap: DoS Attacks against Black-box LLM Services via Infinite Thinking](https://arxiv.org/abs/2512.07086) | NDSS 2026 | CCF-A | DoS Attack / Infinite Loop | 通过对抗prompt使LLM进入无限生成循环，10 RPM即可将服务吞吐压至1%；提出输入空间优化框架，在低维子空间中进行黑盒优化 |
| [Crabs: Consuming Resource via Auto-generation for LLM-DoS Attack under Black-box Settings](https://arxiv.org/abs/2412.13879) | ACL 2025 Findings | CCF-B | DoS Attack / Auto Generation | 提出AutoDoS自动生成黑盒DoS攻击prompt；发明DoS Attack Tree结构化方法；效果显著且可自动化 |
| [Rethinking Latency DoS: Attacking the LLM Serving Framework](https://arxiv.org/abs/2602.07878) | arXiv | — | DoS Attack / System Layer | Fill攻击耗尽KV cache造成线头阻塞，Squeeze攻击迫使调度器反复抢占；比现有算法延迟攻击效率高30-40% |
| [Beyond Max Tokens: Stealthy Resource Amplification via Tool Calling Chains in LLM Agents](https://arxiv.org/abs/2601.10955) | arXiv | — | DoS Attack / Agent/MCP | 针对MCP协议的多轮工具调用链经济DoS攻击；通过Monte Carlo Tree Search优化文本字段，最大化成本且保证任务成功率 |
| [Resource Consumption Threats in LLMs (Survey)](https://arxiv.org/abs/2603.16068) | arXiv | — | Survey / Resource Security | 系统性综述LLM资源消耗威胁全流程：威胁诱导→机制理解→缓解策略；建立统一框架 |

#### 4月20日 - CCF-A/B 论文收录

本周收录 3 篇确定录用的 LLM Safety 论文（2篇CCF-A，1篇CCF-B）：

| 论文 | 会议 | 等级 | 方向 | 摘要 |
|------|------|------|------|------|
| [PIArena: A Platform for Prompt Injection Evaluation](https://arxiv.org/abs/2604.08499) | ACL 2026 | CCF-A | Prompt Injection | 提出 PIArena 统一评测平台，支持 SOTA 攻击/防御集成评估；设计动态策略攻击自适应优化注入提示；揭示多个 SOTA 防御的局限性（任务泛化不足、易受自适应攻击、目标任务对齐时根本脆弱） |
| [Directing LLM Routers to Expensive Models via Adversarial Suffix Optimization](https://arxiv.org/abs/2604.15022) | ACL 2026 | CCF-A | Router Attack | 提出R²A方法，通过对抗后缀优化误导黑盒LLM路由器选择昂贵模型；部署混合集成代理路由器模拟黑盒路由器；商业和开源路由系统上均显著提升昂贵模型路由率 |
| [Continual Unlearning in Real Time with Ensured Preservation of LLM Knowledge](https://arxiv.org/abs/2604.14644) | ACL Findings 2026 | CCF-A | Unlearning/Evaluation | 提出CURaTE方法，实现实时持续遗忘并保证LLM知识保留；基于句子嵌入模型判断输入是否对应存储的遗忘请求 |

---

#### 4月27日 - CCF-A/B 论文收录

本周收录 9 篇确定录用的 LLM Safety CCF-A/B 论文（9篇CCF-A）：

| 论文 | 会议 | 等级 | 方向 | 摘要 |
|------|------|------|------|------|
| [Hidden Secrets in the arXiv: Discovering, Analyzing, and Preventing Unintentional Information Disclosure in Source Files](https://arxiv.org/abs/2604.20927) | IEEE S&P 2026 | CCF-A | Privacy/Information Disclosure | 系统性分析arXiv 270万份LaTeX源码中的信息泄露问题：发现近100%提交都包含"隐藏"信息（API密钥、Git历史、内部链接等）；提出ALC-NG工具进行彻底清理 |
| [Adaptive Instruction Composition for Automated LLM Red-Teaming](https://arxiv.org/abs/2604.21159) | ACL 2026 | CCF-A | Red Teaming / Jailbreak | 提出自适应指令组合框架，通过强化学习平衡探索与利用，在组合空间中引导攻击者生成多样化越狱提示；在Harmbench上超越多种自适应方法 |
| [Benchmarking Contextual Integrity in Enterprise LLM Agents](https://arxiv.org/abs/2604.21308) | ACL 2026 Industry | CCF-A | Privacy / Agent | 提出CI-Work基准，模拟企业信息流五方向评估LLM Agent隐私泄露；揭示隐私违规率15.8%-50.9%的严峻现实；发现任务效用与隐私泄露存在反向权衡 |
| [Structured Memory for Long-Horizon Behavior in LLMs](https://arxiv.org/abs/2604.21748) | ACL 2026 | CCF-A | Memory / Agent | 提出StructMem结构化层次记忆框架，保留事件级绑定并诱导跨事件连接；在LoCoMo上提升时序推理和多跳问答性能，同时大幅降低token使用和API调用 |
| [Revisiting Non-Verbatim Memorization in Large Language Models](https://arxiv.org/abs/2604.21882) | ACL 2026 | CCF-A | Memorization / Privacy | 提出RedirectQA数据集，利用Wikipedia重定向关联Wikidata事实三元组与多样化表面形式；揭示13个LLM的事实记忆既非完全表面特定也非完全表面不变，表面多样性对评估非逐字记忆至关重要 |
| [Machine Behavior in Relational Moral Dilemmas: Moral Rightness, Predicted Human Behavior, and Model Decisions](https://arxiv.org/abs/2604.21871) | ACL Findings 2026 | CCF-A | Ethics / Alignment | 研究LLM在关系道德困境中的决策，发现模型决策与道德正确性对齐而非与预测人类行为对齐；揭示LLM决策优先考虑刚性规范性规则而非社交敏感性，可能导致现实部署中的严重偏差 |
| [From If-Statements to ML Pipelines: Revisiting Bias in Code-Generation](https://arxiv.org/abs/2604.21716) | ACL Findings 2026 | CCF-A | Bias / Code Generation | 揭示现有代码生成偏见评估严重低估实际偏见：87.7%的ML流水线包含敏感属性（vs条件语句的59.2%）；即使模型证明排除了无关特征仍保留敏感属性；传统基准低估部署风险 |
| [Real-time Risk Event Discovery from Noisy Customer Incidents at Enterprise Scale](https://arxiv.org/abs/2604.21889) | ACL 2026 Industry | CCF-A | LLM Agent / Incident Detection | 提出TingIS企业级事件发现系统，峰值吞吐量2000条/分钟、P90延迟3.5分钟；在真实数据上显著优于基线方法 |
| [Turning the Adversary's Poison against Itself: Cluster Segregation Concealment for Backdoor Defense](https://arxiv.org/abs/2604.21416) | Computers & Security Journal | CCF-B | Backdoor Defense | 提出CSC后门防御方法，利用投毒样本在潜伏空间早期形成孤立簇的特性，通过DBSCAN聚类识别异常簇并重新标记为虚拟类；在12种投毒攻击上SOTA，将平均攻击成功率降至近零 |


## 📅 2024年

### Benchmarks

| 论文 | 会议 | arXiv | 摘要 | 代码 |
|------|------|-------|------|------|
| **TrustLLM** - Liu et al. | - | [2401.05561](https://arxiv.org/abs/2401.05561) | LLM可信度综合评估 | 未开源 |
| **AgentDojo** - Debenedetti et al. | NeurIPS 2024 | - | 动态提示注入攻击评估环境 | [GitHub](https://github.com/ethz-spylab/agentdojo) |
| **HELM Safety** - CRFM/Stanford | - | - | 语言模型标准化安全评估 | 未开源 |
| **JailbreakBench** - Chao et al. | NeurIPS 2024 | - | 越狱攻击开放鲁棒性基准 | [GitHub](https://github.com/JailbreakBench/jailbreakbench) |
| **R-Judge** - Yuan et al. | EMNLP 2024 | - | LLM Agent安全风险意识基准 | 未开源 |
| **HallusionBench** - Guan et al. | CVPR 2024 | - | 语言幻觉与视觉错觉诊断套件 | 未开源 |
| **DiaHalu** - Chen et al. | - | [2403.00896](https://arxiv.org/abs/2403.00896) | 对话级幻觉评估基准 | 未开源 |
| **Cybench** | - | [2405.16382](https://arxiv.org/abs/2405.16382) | LLM网络安全能力评估框架 | 未开源 |

### Jailbreak Attacks

| 论文 | 会议 | arXiv | 摘要 | 代码 |
|------|------|-------|------|------|
| **Cold-Attack** - Guo et al. | - | [2402.06679](https://arxiv.org/abs/2402.06679) | 隐蔽可控的越狱攻击 | 未开源 |
| **Jailbreaking Black Box LLMs in Twenty Queries (PAIR)** - Chao et al. | - | [2310.08419](https://arxiv.org/abs/2310.08419) | 20次查询内黑盒越狱 | 未开源 |
| **ActorBreaker** - Ren et al. | ACL 2025 | [2410.10700](https://arxiv.org/abs/2410.10700) | 基于行动者网络的多轮越狱攻击，通过自然分布偏移发现安全漏洞 | [GitHub](https://github.com/AI45Lab/ActorAttack) |
| **Tree of Attacks** - Mehrotra et al. | NeurIPS 2024 | - | 树形攻击自动越狱黑盒LLM | [GitHub](https://github.com/RICommunity/TAP) |
| **AutoDAN** - Liu et al. | ICLR 2024 | - | 生成隐蔽越狱提示 | [GitHub](https://github.com/SheltonLiu-N/AutoDAN) |
| **Crescendo Multi-Turn Jailbreak** - Russinovich et al. | - | - | 多轮递增式越狱攻击 | 未开源 |
| **Harnessing Task Overload** - Dong et al. | - | [2410.04190](https://arxiv.org/abs/2410.04190) | 利用任务过载实现可扩展越狱 | 未开源 |
| **AutoDAN-Turbo** - Liu et al. | - | [2410.05295](https://arxiv.org/abs/2410.05295) | 终身学习策略自探索代理 | [GitHub](https://github.com/SaFoLab-WISC/AutoDAN-Turbo) |
| **HarmBench** - Mazeika et al. | - | [2402.04249](https://arxiv.org/abs/2402.04249) | 自动红队测试标准化评估框架 | [GitHub](https://github.com/centerforaisafety/HarmBench) |
| **Jailbroken** - Wei et al. | NeurIPS 2023 | - | 分析安全训练失败原因 | 未开源 |

### Defense & Safety

| 论文 | 会议 | arXiv | 摘要 | 代码 |
|------|------|-------|------|------|
| **MLLM-Protector** - Pi et al. | - | [2401.02906](https://arxiv.org/abs/2401.02906) | 保护多模态LLM安全而不损失性能 | 未开源 |
| **NeMo Guardrails** - Rebedea et al. | EMNLP 2023 Demo | - | 可控制和安全的LLM应用工具包 | [GitHub](https://github.com/NVIDIA/NeMo-Guardrails) |
| **Defending with Spotlighting** - Hines et al. | - | - | 利用spotlighting防御间接提示注入 | 未开源 |

### Red Teaming

| 论文 | 会议 | arXiv | 摘要 | 代码 |
|------|------|-------|------|------|
| **Automated Progressive Red Teaming (APRT)** - Jiang et al. | - | [2407.03876](https://arxiv.org/abs/2407.03876) | 自动化渐进式红队测试 | 未开源 |
| **Holistic Automated Red Teaming** - Zhang et al. | - | [2409.16783](https://arxiv.org/abs/2409.16783) | 自上而下测试用例生成的整体自动化红队测试 | 未开源 |
| **Curiosity-Driven Red-Teaming** - Hong et al. | - | [2402.19464](https://arxiv.org/abs/2402.19464) | 好奇心驱动的红队测试 | 未开源 |

### Hallucination

| 论文 | 会议 | arXiv | 摘要 | 代码 |
|------|------|-------|------|------|
| **Siren's Song** - Zhang et al. | - | [2309.01219](https://arxiv.org/abs/2309.01219) | LLM幻觉综述 | 未开源 |
| **HaloScope** - Du et al. | - | [2409.17504](https://arxiv.org/abs/2409.17504) | 利用无标签生成进行幻觉检测 | 未开源 |
| **Semantic Entropy Probes** - Kossen et al. | - | [2406.15927](https://arxiv.org/abs/2406.15927) | 鲁棒低成本幻觉检测 | 未开源 |

### Alignment & Safety Training

| 论文 | 会议 | arXiv | 摘要 | 代码 |
|------|------|-------|------|------|
| **Sleeper Agents** - Hubinger et al. | - | [2401.05566](https://arxiv.org/abs/2401.05566) | 训练持久存在的欺骗性LLM | 未开源 |
| **Are Aligned Neural Networks Adversarially Aligned** - Carlini et al. | NeurIPS 2024 | - | 对齐神经网络是否对抗性对齐 | 未开源 |
| **Safety Layers in Aligned LLMs** - Li et al. | - | [2408.17003](https://arxiv.org/abs/2408.17003) | 对齐LLM中的安全层 | 未开源 |
| **Nothing in Excess** - Cao et al. | - | [2408.11491](https://arxiv.org/abs/2408.11491) | 缓解过度安全问题 | 未开源 |
| **Instruction Hierarchy** - Wallace et al. | - | [2404.13208](https://arxiv.org/abs/2404.13208) | 指令层次结构训练 | 未开源 |
| **Emulated Disalignment** - Zhou et al. | - | [2402.12343](https://arxiv.org/abs/2402.12343) | 模拟非对齐：安全对齐可能适得其反 | 未开源 |
| **Speak Out of Turn** - Zhou et al. | - | [2402.17262](https://arxiv.org/abs/2402.17262) | 多轮对话中的安全漏洞 | 未开源 |
| **BeaverTails** - Ji et al. | NeurIPS 2024 | - | 通过人类偏好数据集改进安全对齐 | 未开源 |

### Prompt Injection & Security

| 论文 | 会议 | arXiv | 摘要 | 代码 |
|------|------|-------|------|------|
| **Formalizing Prompt Injection Attacks** - Liu et al. | USENIX Security 2024 | - | 提示注入攻击形式化与基准测试 | 未开源 |
| **Benchmarking Indirect Prompt Injection** - Yi et al. | - | [2312.14197](https://arxiv.org/abs/2312.14197) | 间接提示注入攻击基准测试 | 未开源 |

### Surveys

| 论文 | arXiv | 内容 |
|------|-------|------|
| **AI Alignment Survey** - Ji et al. | [2310.19852](https://arxiv.org/abs/2310.19852) | AI对齐全面综述 |
| **Jailbreak Attacks and Defenses Against LLMs: A Survey** | [2407.04295](https://arxiv.org/abs/2407.04295) | 越狱攻击与防御综述 |
| **A Survey on LLM Security and Privacy** - Yao et al. | - | LLM安全与隐私全面综述 |
| **Against the Achilles' Heel** - Lin et al. | [2404.00629](https://arxiv.org/abs/2404.00629) | 生成式AI红队测试综述 |

---

## 📅 2023年

| 论文 | 会议 | arXiv | 摘要 | 代码 |
|------|------|-------|------|------|
| **Universal and Transferable Adversarial Attacks (GCG)** - Zou et al. | ICLR 2024 | [2307.15043](https://arxiv.org/abs/2307.15043) | 通用可迁移对抗攻击 | [GitHub](https://github.com/llm-attacks/llm-attacks) |
| **Towards Mitigating LLM Hallucination** - Ji et al. | EMNLP 2023 Findings | - | 通过自我反思缓解LLM幻觉 | 未开源 |
| **GPTFuzzer** - Yu et al. | - | [2309.10253](https://arxiv.org/abs/2309.10253) | 自动生成越狱提示的红队测试 | 未开源 |
| **Llama Guard** - Inan et al. | - | [2312.06674](https://arxiv.org/abs/2312.06674) | 基于LLM的输入输出安全保障 | [GitHub](https://github.com/meta-llama/PurpleLlama) |
| **Not What You've Signed Up For** - Greshake et al. | AISec 2023 | - | 间接提示注入攻击 | 未开源 |
| **A Holistic Approach to Undesired Content Detection** - Markov et al. | AAAI 2023 | - | 不良内容检测的整体方法 | 未开源 |
| **Trustworthy LLMs Survey** - Liu et al. | - | [2308.05374](https://arxiv.org/abs/2308.05374) | 可信LLM评估综述 | 未开源 |
| **Do Anything Now** - Shen et al. | CCS 2024 | - | 野外越狱提示特征分析 | 未开源 |
| **Don't Listen to Me** - Yu et al. | USENIX Security 2024 | - | 理解越狱提示的本质 | 未开源 |
| **Survey of Hallucination in NLG** - Ji et al. | ACM Computing Surveys | - | 自然语言生成中的幻觉综述 | 未开源 |
| **Prompt Injection Attack** - Liu et al. | - | [2306.05499](https://arxiv.org/abs/2306.05499) | 针对LLM集成应用的提示注入攻击 | 未开源 |

---

## 📅 2021-2022年（早期重要工作）

| 论文 | 会议 | 年份 | 摘要 | 代码 |
|------|------|------|------|------|
| **Red Teaming Language Models with Language Models** - Perez et al. | - | 2022 | 用LLM对LLM进行红队测试 | 未开源 |
| **TruthfulQA** - Lin et al. | - | 2022 | 测量模型模仿人类谬误的程度 | 未开源 |
| **Asleep at the Keyboard** - Pearce et al. | IEEE S&P | 2022 | GitHub Copilot代码安全分析 | 未开源 |
| **You Autocomplete Me** - Schuster et al. | USENIX Security | 2021 | 神经代码补全中的投毒攻击 | 未开源 |
| **Extracting Training Data from LLMs** - Carlini et al. | USENIX Security | 2021 | 从大型语言模型中提取训练数据 | 未开源 |

---

## 📊 方向统计

| 方向 | 论文数量 | 占比 |
|------|:--------:|:----:|
| Jailbreak Attacks | ~20 | 25% |
| Benchmarks | ~15 | 19% |
| Alignment & Safety | ~15 | 19% |
| Hallucination | ~10 | 12% |
| Red Teaming | ~8 | 10% |
| Prompt Injection | ~6 | 8% |
| Privacy & Security | ~6 | 8% |
| DoS & Resource Exhaustion | ~5 | 6% |

---

## 📝 更新记录

| 日期 | 更新内容 |
|------|----------|
| 2026-04-23 | 新增5篇DoS/资源耗尽攻击论文（ThinkTrap-NDSS 2026, Crabs-ACL 2025, Latency DoS, Tool Chain DoS, Survey） |
| 2026-04-13 | 收录2篇CCF-A论文（PIArena - ACL 2026, TrajGuard - ACL Findings 2026） |
| 2026-04-10 | 阅读完成第47篇论文：HARM - Holistic Automated Red Teaming (EMNLP 2024) |
| 2026-03-21 | 修正论文：ActorBreaker (v2最新版本) - 更新标题、方法名、代码链接 |
| 2026-03-16 | 收录3篇CCF-A/B论文（AAAI 2026, EuroS&P 2026, LAK 2026） |
| 2026-03-09 | 新增6篇论文（SIABENCH, ESAA-Security, Proteus等） |
| 2026-03-04 | 首次整理，收录2021-2026年约80篇论文 |
| 后续 | 每周一自动更新上周新论文 |

---

*本文档由 Kimi Claw 自动整理维护*  
*最后更新: 2026-04-23*
