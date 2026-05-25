---
name: ai-product-cv-optimizer
description: Use this skill when optimizing, rewriting, reviewing, or redesigning resumes/CVs for AI product roles, AI product engineer roles, AI Agent PM, multimodal/AIGC products, AI applications, developer tools, AI platforms, enterprise AI, intelligent hardware, or Demo-to-Product work. It supports target-role and company intake, HR/PM reviewer mapping, deep content discovery, resume copywriting, project prioritization, design system selection, one-page PDF layout QA, and iteration after user confirmation.
---

# AI Product CV Optimizer

## Core Goal

Turn AI product or AI product engineer materials into a target-positioned resume that can pass a 10-second HR scan and still stand up to PM/Hiring Manager scrutiny.

Prioritize: target fit, evidence, metrics, ownership, product judgment, model/application understanding, and clean one-page readability.

## Required Workflow

1. **Clarify target first.** Ask for the user's PM direction and target companies before making positioning decisions. If the user already gave them, restate the assumption.
2. **Map reviewers.** Convert the target role/company into concrete reviewer perspectives: HR screener, PM Hiring Manager, domain PM lead, and when relevant technical/product-design reviewers. Use `references/target-and-reviewers.md`.
3. **Read the materials.** Extract current sections, projects, metrics, dates, design constraints, and weak/strong signals from uploaded PDFs, images, docs, or text.
4. **Ask deep questions after reading.** Do not ask generic questions before understanding the base material. Use `references/content-discovery.md` to ask concise, high-yield questions, usually one experience or project at a time.
5. **Separate strategy from edits.** For substantial changes, first provide a text-only rewrite/structure preview and get user confirmation before editing files.
6. **Prioritize, do not equalize.** Expand role-relevant work and high-signal projects; compress, merge, or remove weakly related projects. Work experience and shipped products usually outrank hackathons unless the hackathon is exceptionally relevant.
7. **Design with one system.** Ask the user for preferred color family and font taste, recommend options, then apply a unified palette and typography system. Use `references/design-options.md`.
8. **Render-check final output.** For PDFs, run `scripts/render_pdf_check.py` or an equivalent render workflow and inspect for page count, overlap, truncation, bottom whitespace, density, and font quality.

## Intake Questions

Ask only what is missing, and keep it short:

- Target PM direction: AI Agent PM, AI product engineer, multimodal/AIGC, consumer AI, enterprise AI, developer tools, AI platform, intelligent hardware, data/evaluation/safety, or another direction?
- Target companies or company types?
- Role level and constraint: internship/full-time, location, availability, earliest start date, on-site days, language?
- What should be emphasized or avoided: growth, community, operations, research, engineering depth, design, hardware, etc.?
- Design preference: color family, visual style, font preference, one-page vs two-page?

## Content Output Standard

Write resume bullets as:

`Scope / problem -> personal action -> product or technical method -> measurable result`

Prefer concrete metrics. If exact metrics are unavailable, ask for them. If still unavailable, use honest proxies such as launch status, demo success rate, user/group scale, team size, time-to-demo, case coverage, latency, adoption frequency, or award/result.

Avoid:

- Long unbroken lines that span the full page.
- Feature lists without problem/result.
- Buzzwords without evidence.
- Treating every project as equally important.
- Forcing growth/community positioning when the target is AI product, product engineering, or innovation product.

## File Editing Rules

- Preserve the user's existing final assets unless explicitly asked to replace them.
- Do not embed a candidate's full private resume content into this skill. Keep examples anonymized.
- When modifying DOCX/PDF/PPT-derived resumes, produce a renderable artifact and visually inspect the result.
- When the user asks for only a content draft, do not edit files.

## Bundled References

- `references/target-and-reviewers.md`: target direction taxonomy, company archetypes, and reviewer prompts.
- `references/content-discovery.md`: question bank for mining deeper project/work details.
- `references/content-playbook.md`: rewrite templates, section strategy, and project prioritization rules.
- `references/design-options.md`: color palettes, font choices, modular layout rules, and visual QA checklist.

## Bundled Script

Use:

```bash
python scripts/render_pdf_check.py path/to/resume.pdf --out-dir render_check --scale 2
```

The script reports PDF page count and renders a page PNG for manual layout QA.
