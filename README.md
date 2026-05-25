# AI Product CV Optimizer

[中文说明](README.zh-CN.md)

A reusable Codex skill for optimizing AI product and AI product engineer resumes with HR/PM review, content discovery, design guidance, and PDF QA.

## What This Skill Does

This skill helps Codex turn raw resume materials into a targeted, readable, and evidence-backed resume for AI product roles, including:

- AI Product Manager
- AI Product Engineer
- AI Agent PM
- Multimodal / AIGC Product
- Developer Tools and AI Platform
- Enterprise AI / SaaS AI
- Intelligent Hardware / Robotics
- AI Evaluation, Data, and Safety Products

It is designed for resume workflows that require more than surface-level polishing: target-company positioning, reviewer simulation, project prioritization, content mining, layout decisions, and final PDF rendering checks.

## Core Workflow

1. Clarify the user's target PM direction and target companies.
2. Map the target to reviewer perspectives such as HR, PM Hiring Manager, domain PM lead, and technical reviewer.
3. Read the user's resume materials before asking deep follow-up questions.
4. Mine concrete ownership, metrics, launch evidence, evaluation methods, and product decisions.
5. Rewrite content around problem, action, method, and measurable result.
6. Prioritize high-signal work and projects instead of giving every item equal space.
7. Choose a unified design system: color family, typography, modular layout, and visual hierarchy.
8. Render-check the final PDF for page count, overlap, clipping, whitespace, density, and font quality.

## Skill Structure

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

## References

- `target-and-reviewers.md`: target role taxonomy, company archetypes, and reviewer prompts.
- `content-discovery.md`: focused question bank for digging into projects and work experience.
- `content-playbook.md`: resume structure, bullet templates, prioritization rules, and AI product wording patterns.
- `design-options.md`: color palettes, typography recommendations, modular layout rules, and PDF QA checklist.

## PDF QA Script

Use the bundled script to render a PDF page and report page count:

```bash
python scripts/render_pdf_check.py path/to/resume.pdf --out-dir render_check --scale 2
```

The script requires:

- `pypdf`
- `pypdfium2`

It outputs a JSON summary and a rendered PNG for manual layout inspection.

## Example Prompt

```text
Use $ai-product-cv-optimizer to optimize my resume for an AI Agent PM internship at foundation model startups and consumer AI companies.
```

## Design Principles

- Make the target role obvious within 10 seconds.
- Put the strongest work and project signals above or near the top.
- Prefer concrete metrics over vague impact language.
- Use one unified color system rather than multi-color project cards.
- Split dense content into modular blocks such as "responsibility" and "highlight".
- Ask for user confirmation before making substantial file edits.

## Privacy

This repository contains reusable workflow instructions and anonymized templates only. It should not include any candidate's full private resume content.
