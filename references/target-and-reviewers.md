# Target And Reviewer Mapping

Use this file after reading the user's target role and target companies. The goal is to convert a vague resume request into concrete reviewer expectations.

## Target Direction Taxonomy

- **AI Agent PM / Agentic Product**: values workflow design, tool use, memory, evaluation, human-in-the-loop, latency/cost, bad-case handling, and productized agent loops.
- **AI Product Engineer**: values demo-to-product execution, frontend/backend integration, model/API orchestration, rapid prototyping, system thinking, and measurable product outcomes.
- **Multimodal / AIGC Product**: values generation workflow, image/video/audio understanding, creative control, consistency, user experience, model selection, and evaluation.
- **Consumer AI Product**: values user insight, interaction design, activation/retention, content or creation loops, polish, and fast iteration.
- **Enterprise AI / SaaS AI**: values workflow ROI, reliability, permission/security, customer scenarios, deployment constraints, and business metrics.
- **Developer Tools / AI Coding / Platform**: values developer workflow empathy, API/product abstraction, documentation, ecosystem thinking, reliability, and technical depth.
- **AI Platform / Model Operations**: values evaluation, data pipeline, model governance, prompt/version management, observability, and scalable internal tools.
- **Intelligent Hardware / Robotics**: values real-world demo reliability, perception-control chains, hardware/software integration, latency, safety, and onsite robustness.
- **AI Data / Evaluation / Safety**: values benchmark design, quality control, judge/evaluator design, red teaming, policy boundaries, and measurable accuracy or coverage.

## Company Archetypes

- **Foundation model lab / AI-native startup**: emphasize model understanding, agent/product architecture, evaluation loops, speed of execution, and product taste.
- **Consumer content or social platform**: emphasize creation workflows, user scenarios, interaction polish, content quality, and distribution context. Do not force community/growth if the user says they are out of scope.
- **Enterprise SaaS or vertical AI company**: emphasize pain-point clarity, workflow embedding, measurable efficiency, customer adoption, permission/security, and implementation feasibility.
- **Developer productivity or cloud platform**: emphasize developer experience, API abstraction, integration reliability, docs, technical judgment, and ecosystem leverage.
- **Hardware / robotics / embodied AI company**: emphasize end-to-end chain, real-world task success, response time, sensor/control choices, and demo repeatability.
- **Large tech AI division**: emphasize cross-functional collaboration, scale, business alignment, rigorous metrics, and ability to work within complex systems.

## Reviewer Perspectives

### HR Screener

Checks in 10 seconds:

- Target role is obvious from title/summary.
- Skills match JD keywords without keyword stuffing.
- Work/projects have recognisable company, role, dates, results.
- Strongest signals are above the fold.
- Layout is readable and not crowded.

### PM Hiring Manager

Checks:

- Did the candidate own product decisions, not only assist execution?
- Are problems, users, tradeoffs, and results clear?
- Can the candidate turn fuzzy AI capability into a usable product?
- Are metrics credible and relevant?
- Is there evidence of launch, iteration, or evaluation?

### Domain PM Lead

Adjust by target direction:

- Agent: workflow design, memory/tooling/eval, bad cases, automation rate, latency/cost.
- Multimodal/AIGC: creative control, consistency, model evaluation, asset pipeline, user workflow.
- Enterprise: ROI, reliability, permissions, customer adoption, process embedding.
- Platform/devtools: API abstractions, developer workflow, reliability, integration, docs.
- Hardware/robotics: perception/control chain, onsite demo success, latency, task completion, safety.

### Technical Reviewer

Checks whether technical claims are plausible:

- Model/API choices, architecture boundaries, data flow, and system constraints.
- Candidate's own contribution versus team contribution.
- Evaluation method, sample size, failure handling, and reproducibility.

### Design/Product Taste Reviewer

Checks:

- Information hierarchy and interaction thinking.
- Whether the resume itself demonstrates product taste.
- Whether examples show user-centric decisions instead of pure feature accumulation.

## Multi-Reviewer Prompt Template

When the user asks for HR/PM scoring, instantiate 3-5 reviewers:

```text
你是 {company_or_archetype} 的 {reviewer_role}，正在评估候选人是否适合 {target_role}。
请从 1-10 分评价：目标匹配度、10 秒可读性、产品判断、AI/技术理解、结果可信度、风险点。
先给结论，再列出优点、扣分点、最值得修改的 3 件事。
不要泛泛而谈，必须引用简历中的具体内容。
```

Use distinct reviewer biases. For example: strict HR, AI Agent PM Lead, consumer AI PM, enterprise AI PM, technical product lead.
