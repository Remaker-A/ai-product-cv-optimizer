#!/usr/bin/env python3
"""Render a PDF resume page for visual QA and report page count.

Usage:
    python render_pdf_check.py resume.pdf --out-dir render_check --scale 2
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Render a PDF page for resume visual QA.")
    parser.add_argument("pdf", type=Path, help="Path to the PDF resume.")
    parser.add_argument("--out-dir", type=Path, default=Path("render_check"), help="Directory for rendered PNG output.")
    parser.add_argument("--scale", type=float, default=2.0, help="Render scale. Use 2-3 for layout QA.")
    parser.add_argument("--page", type=int, default=0, help="Zero-based page index to render.")
    args = parser.parse_args()

    pdf_path = args.pdf.expanduser().resolve()
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    try:
        from pypdf import PdfReader
    except ImportError as exc:
        raise SystemExit("Missing dependency: pypdf. Install it in the active Python environment.") from exc

    try:
        import pypdfium2 as pdfium
    except ImportError as exc:
        raise SystemExit("Missing dependency: pypdfium2. Install it in the active Python environment.") from exc

    reader = PdfReader(str(pdf_path))
    page_count = len(reader.pages)
    if args.page < 0 or args.page >= page_count:
        raise ValueError(f"Page index {args.page} out of range for {page_count} page(s).")

    out_dir = args.out_dir.expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    doc = pdfium.PdfDocument(str(pdf_path))
    image = doc[args.page].render(scale=args.scale).to_pil()
    out_path = out_dir / f"{pdf_path.stem}_page_{args.page + 1}.png"
    image.save(out_path)

    result = {
        "pdf": str(pdf_path),
        "pages": page_count,
        "rendered_page": args.page + 1,
        "scale": args.scale,
        "image_size": image.size,
        "png": str(out_path),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
