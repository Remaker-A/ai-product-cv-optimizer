# Design Options

Use this file when the user asks for layout, visual polish, typography, or PDF design. Always ask for preference when it matters, but recommend a default if the user wants speed.

## Color Intake

Ask:

```text
你更喜欢哪类色系：蓝灰科技、黑灰极简、青绿色 AI 工具感、暖中性、还是更个性化一点？
```

Recommended palettes:

- **Blue-gray tech, default**: `#121A2A`, `#2F6FE4`, `#EEF5FF`, `#D7E0ED`, `#6B7280`.
- **Black-gray minimal**: `#111827`, `#374151`, `#F3F4F6`, `#D1D5DB`, `#6B7280`.
- **Teal AI tool**: `#0F766E`, `#14B8A6`, `#ECFDF5`, `#CCFBF1`, `#334155`.
- **Warm neutral with restraint**: `#1F2937`, `#B45309`, `#FFFBEB`, `#E5E7EB`, `#4B5563`.
- **Dark premium**: use only if the user explicitly wants a non-traditional resume; ensure ATS/export readability.

Rules:

- Use one unified color family. Do not assign a different saturated color to every project card.
- Use accent color for section bars, labels, and key numbers only.
- Keep backgrounds very light; body text should stay high-contrast.
- Avoid rainbow cards, heavy gradients, bokeh blobs, and corporate stock-style decoration.

## Font Recommendations

Ask:

```text
字体你想偏现代科技、稳重商务、还是更轻快个性？我可以给你 2-3 套组合。
```

Recommended combinations:

- **Modern AI product**: MiSans for body, HarmonyOS Sans SC Bold for headings, Inter/Segoe UI for English and numbers.
- **Clean and safe**: Noto Sans SC for body and headings, Inter for English and numbers.
- **Windows-compatible**: Microsoft YaHei UI for body, Microsoft YaHei Bold for headings, Segoe UI for English and numbers.
- **Polished Chinese PDF**: Source Han Sans SC for body, Source Han Sans SC Heavy/Bold for headings.

Avoid:

- SimSun, KaiTi, FangSong, default serif fonts for modern AI product resumes.
- Too many font families in one page.
- Tiny body text below readable PDF size.

## Layout Rules

- Use modular sections: top summary/skills, work experience, projects, education.
- Use cards only for repeated project/work modules; do not nest cards inside cards.
- Avoid long full-width paragraphs. Split into "职责" and "亮点" blocks when content is dense.
- Make the strongest work/project visually larger or full-width; use two-column modules for secondary projects.
- Keep labels short: "职责", "亮点", "结果", "规模", "技术".
- Use consistent date placement and alignment.
- Preserve enough white space, but do not leave a visibly empty bottom third.
- Keep section headings slightly larger and clearer than body text.

Suggested one-page Chinese resume sizing:

- Name: 22-28 pt.
- Target title / summary: 9.5-11 pt.
- Section heading: 11-13 pt.
- Body: 8.8-10.2 pt.
- Small labels/date: 7.5-8.8 pt.
- Line height: 1.15-1.35 depending on density.

## Illustration Guidance

Use illustrations only if they support personality and do not compete with content.

- Prefer small, memorable, simple manga/editorial-style accents if the user wants personality.
- Keep opacity/size restrained; avoid generic office workflow illustration.
- Do not place illustration behind important text.
- Do not let decoration create multiple color systems.

## PDF Visual QA Checklist

Render the PDF and inspect:

- One page unless the user requested otherwise.
- No text overlap, clipping, or compressed line height.
- No bottom whitespace large enough to suggest unfinished layout.
- Top third communicates target fit within 10 seconds.
- Work experience and top projects are visually prioritized.
- Colors are unified and not noisy.
- Dates, labels, and cards align consistently.
- Fonts render correctly in PDF, including Chinese punctuation and mixed English.
- Printed grayscale still preserves hierarchy.
