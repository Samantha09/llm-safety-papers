# practical-notes

> 大模型安全论文的**复现笔记**、代码实践与 Jupyter 实验记录

---

## 🎯 模块定位

本目录用于保存论文的**实战复现**内容，与 [`papers/`](../papers/) 中的论文笔记形成互补：

| 目录 | 内容 |
|------|------|
| `papers/` | 论文精读笔记（结构化解析、核心观点） |
| **`practical-notes/`** | **复现代码、Jupyter Notebook、实验记录** |

简单说：`papers/` 告诉你论文**讲了什么**，`practical-notes/` 帮你实际**跑通、验证和改进**。

---

## 📁 目录结构

```
practical-notes/
├── <paper-name-slug>/          # 按论文简称命名，与 papers/ 中的文件名对应
│   ├── README.md               # 必选：实验说明、环境配置、运行指南
│   ├── notebooks/              # Jupyter Notebook 实验
│   │   └── *.ipynb
│   ├── src/                    # 核心复现代码
│   │   └── *.py
│   ├── assets/                # 实验结果图片、数据图表
│   └── results/               # 输出结果、生成的对抗样本等
```

> **命名规范**：论文简称全部用小写，单词间用连字符 `-` 连接，与 `papers/` 中的 Markdown 文件名保持一致。  
> 例如：论文 `AutoDAN-Turbo.md` → 复现目录 `practical-notes/auto-dan-turbo/`

---

## 📝 README 模板

每个复现笔记根目录下 **必须包含** `README.md`，参考格式：

```markdown
# {论文简称} - 复现笔记

## 📖 论文信息
- **标题**: {论文全名}
- **来源**: {会议/期刊，年份}
- **论文笔记**: ../papers/{year}/{论文简称}.md
- **开源代码**: {原始仓库链接}

## 🧪 复现环境
- **模型**: {使用的模型，如 GPT-4、Claude-3、LLaMA-3}
- **依赖**: requirements.txt 或 environment.yml
- **硬件**: GPU 型号 / CPU-only

## ⚡ 快速开始
{运行步骤}

## 🔬 实验结果
{复现效果对比、原论文结果对比}

## 💡 关键发现
{复现过程中的重要发现或注意事项}
```

---

## 📋 内容规范

### ✅ 推荐包含
- 环境配置步骤（依赖版本）
- 核心代码片段及注释
- 原始论文结果 vs 复现结果对比
- 运行脚本或命令
- 复现过程中遇到的坑及解决方案

### ❌ 避免包含
- 大型模型权重文件（使用 `.gitignore` 过滤）
- 敏感 API Key（使用环境变量）
- 大量原始数据（超过 10MB 的文件考虑外部存储）
- 与论文无关的探索性代码

---

## 🚀 快速开始

### 1. 克隆仓库
```bash
git clone git@gitee.com:zhangshirui1/llm-safety-papers.git
cd llm-safety-papers/practical-notes
```

### 2. 查看已有复现
```bash
ls -la */
```

### 3. 运行某个复现
```bash
cd <paper-slug>/src
pip install -r requirements.txt
python run.py
```

---

## 🔗 相关链接

- 📚 [论文笔记总览](../papers/) — papers/ 目录
- 📊 [论文阅读进度](../README.md#-项目概况) — 实时进度
- 🗂️ [完整目录结构](../README.md#-仓库结构)

---

_本模块由 LLM Safety 论文阅读计划自动维护。_
