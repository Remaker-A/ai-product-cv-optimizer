# AI Product CV Optimizer

一个可复用的 Skill，用于优化 AI 产品、AI 产品工程师、AI Agent PM、多模态 / AIGC 产品等方向的简历。它覆盖目标岗位澄清、HR/PM 视角评审、内容深挖、项目取舍、文案改写、版式设计与 PDF 渲染检查。

## 适用场景

这个 Skill 适合用于以下方向的简历优化：

- AI 产品经理
- AI 产品工程师
- AI Agent PM
- 多模态 / AIGC 产品
- 消费级 AI 应用
- 开发者工具与 AI 平台
- 企业 AI / SaaS AI
- 智能硬件 / 机器人
- AI 评测、数据与安全产品

它不只是做语言润色，而是帮助 Codex 从目标公司和岗位出发，重新判断简历的重点、结构、项目排序、指标表达和最终视觉呈现。

## 核心能力

1. 明确用户的目标 PM 方向和目标公司。
2. 将目标岗位映射到 HR、PM Hiring Manager、垂直方向 PM Lead、技术 Reviewer 等不同评审视角。
3. 先读取用户材料，再围绕关键经历进行深挖提问。
4. 挖掘个人贡献、项目指标、上线状态、评测方法、产品判断和业务结果。
5. 按照“问题 / 场景 -> 个人动作 -> 产品或技术方法 -> 可验证结果”的结构改写简历内容。
6. 根据目标岗位相关性，对工作经历和项目经历进行取舍，不把所有项目平均展开。
7. 帮助用户选择统一的色系、字体、模块化排版和信息层级。
8. 对最终 PDF 做渲染检查，重点检查页数、重叠、截断、留白、信息密度和字体观感。

## 目录结构

```text
ai-product-cv-optimizer/
|-- SKILL.md
|-- agents/
|   `-- openai.yaml
|-- references/
|   |-- target-and-reviewers.md
|   |-- content-discovery.md
|   |-- content-playbook.md
|   `-- design-options.md
`-- scripts/
    `-- render_pdf_check.py
```

## 参考文件说明

- `target-and-reviewers.md`：目标岗位分类、公司类型和 Reviewer 视角映射。
- `content-discovery.md`：用于深挖工作经历和项目经历的问题库。
- `content-playbook.md`：简历结构、文案模板、项目取舍规则和 AI 产品表达方式。
- `design-options.md`：色系、字体、模块化排版和 PDF 视觉检查标准。

## PDF 检查脚本

使用以下命令渲染 PDF 页面并输出页数信息：

```bash
python scripts/render_pdf_check.py path/to/resume.pdf --out-dir render_check --scale 2
```

脚本依赖：

- `pypdf`
- `pypdfium2`

脚本会输出 JSON 摘要，并生成一张 PNG 图片，方便人工检查简历是否存在文字重叠、内容截断、底部留白过多、字号过小或字体渲染异常等问题。

## 示例 Prompt

```text
Use $ai-product-cv-optimizer to optimize my resume for an AI Agent PM internship at foundation model startups and consumer AI companies.
```

也可以这样使用：

```text
请使用 ai-product-cv-optimizer 帮我优化一份面向 AI 产品工程师岗位的中文简历，目标公司是大模型创业公司和 AI 应用团队。
```

## 设计原则

- 让目标岗位和候选人定位在 10 秒内被看懂。
- 把最强的工作经历和项目经历放在更显眼的位置。
- 优先使用具体指标，而不是空泛的“显著提升”。
- 使用统一色系，不为每个项目使用不同颜色。
- 将密集内容拆成模块，例如“职责”“亮点”“结果”。
- 对较大的内容和排版调整，先给用户文字版确认，再修改文件。

## 隐私说明

本仓库只包含可复用的方法、模板和匿名化示例，不应包含任何候选人的完整私人简历内容。
