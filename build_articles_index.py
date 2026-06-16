"""
build_articles_index.py
========================
掃 articles/*.html → 抽 title/date/description → 產 articles/index.html
（全部文章歸檔頁，按年月分組）

執行：
    py build_articles_index.py
    py build_articles_index.py --dry-run
"""

import argparse
import html
import io
import re
import sys
from collections import defaultdict
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

BASE_DIR = Path(__file__).parent
ARTICLES_DIR = BASE_DIR / "articles"
OUTPUT = ARTICLES_DIR / "index.html"

FILENAME_DATE = re.compile(r"^(\d{4}-\d{2}-\d{2})-")
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.DOTALL)
DESC_RE = re.compile(r'<meta\s+name="description"\s+content="(.*?)"', re.DOTALL)


def extract_meta(path: Path) -> dict | None:
    m = FILENAME_DATE.match(path.name)
    if not m:
        return None
    date = m.group(1)

    text = path.read_text(encoding="utf-8", errors="replace")

    title_m = TITLE_RE.search(text)
    title = title_m.group(1).strip() if title_m else path.stem
    # 去掉「｜昆廷老師」尾巴
    if "｜" in title:
        title = title.rsplit("｜", 1)[0].strip()

    desc_m = DESC_RE.search(text)
    desc = desc_m.group(1).strip() if desc_m else ""
    # HTML entity unescape（meta content 裡可能有 &quot; 等）
    desc = html.unescape(desc)
    title = html.unescape(title)

    return {
        "filename": path.name,
        "date": date,
        "title": title,
        "description": desc,
    }


def collect_articles() -> list[dict]:
    out = []
    for f in sorted(ARTICLES_DIR.glob("*.html"), reverse=True):
        if f.name in ("_template.html", "index.html"):
            continue
        meta = extract_meta(f)
        if meta:
            out.append(meta)
    out.sort(key=lambda a: a["date"], reverse=True)
    return out


def render(articles: list[dict]) -> str:
    # 按 YYYY-MM 分組
    groups: dict[str, list[dict]] = defaultdict(list)
    for a in articles:
        ym = a["date"][:7]
        groups[ym].append(a)
    ordered_months = sorted(groups.keys(), reverse=True)

    sections = []
    for ym in ordered_months:
        year, month = ym.split("-")
        sections.append(f'<section class="archive-month">')
        sections.append(f'<h2 class="archive-month-title">{year} 年 {int(month)} 月</h2>')
        sections.append('<ul class="archive-list">')
        for a in groups[ym]:
            t = html.escape(a["title"])
            d = html.escape(a["description"])
            sections.append(
                f'  <li class="archive-item">'
                f'<a href="{a["filename"]}" class="archive-link">'
                f'<span class="archive-date">{a["date"]}</span>'
                f'<span class="archive-title">{t}</span>'
                f'<span class="archive-desc">{d}</span>'
                f'</a></li>'
            )
        sections.append("</ul>")
        sections.append("</section>")

    body = "\n".join(sections)
    total = len(articles)

    return f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>全部文章｜昆廷老師</title>
<meta name="description" content="昆廷老師的全部文章歸檔，按時間排序。涵蓋企業 AI 導入、Claude Code 教學、中小企業數位轉型、易經決策。">
<meta name="author" content="昆廷老師">
<link rel="canonical" href="https://etimmyqq-lab.github.io/articles/">

<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-3KEGWS9929"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', 'G-3KEGWS9929');
</script>

<meta property="og:type" content="website">
<meta property="og:locale" content="zh_TW">
<meta property="og:title" content="全部文章｜昆廷老師">
<meta property="og:description" content="昆廷老師的全部文章歸檔，按時間排序。">
<meta property="og:url" content="https://etimmyqq-lab.github.io/articles/">
<meta property="og:image" content="https://etimmyqq-lab.github.io/assets/og-default.jpg">

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "name": "全部文章",
  "url": "https://etimmyqq-lab.github.io/articles/",
  "isPartOf": {{
    "@type": "WebSite",
    "name": "昆廷老師",
    "url": "https://etimmyqq-lab.github.io/"
  }},
  "about": {{
    "@type": "Person",
    "name": "昆廷老師",
    "url": "https://etimmyqq-lab.github.io/"
  }}
}}
</script>

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{"@type": "ListItem", "position": 1, "name": "首頁", "item": "https://etimmyqq-lab.github.io/"}},
    {{"@type": "ListItem", "position": 2, "name": "全部文章", "item": "https://etimmyqq-lab.github.io/articles/"}}
  ]
}}
</script>

<link rel="stylesheet" href="../assets/style.css">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700&family=Noto+Serif+TC:wght@700&display=swap" rel="stylesheet">

<style>
.archive-hero {{
    padding: 80px 0 40px;
    background: linear-gradient(135deg, #f8fafd 0%, #eef3f9 100%);
}}
.archive-hero h1 {{
    font-family: 'Noto Serif TC', serif;
    font-size: clamp(2rem, 4vw, 2.8rem);
    color: #15395a;
    margin: 0 0 12px;
}}
.archive-hero p {{
    color: #4a5568;
    margin: 0;
    font-size: 1.05rem;
}}
.archive-count {{
    color: #C9A96E;
    font-size: 0.9rem;
    letter-spacing: 0.12em;
    margin-bottom: 12px;
}}
.archive-body {{
    max-width: 860px;
    margin: 0 auto;
    padding: 60px 24px 80px;
}}
.archive-month {{ margin-bottom: 48px; }}
.archive-month-title {{
    font-family: 'Noto Serif TC', serif;
    font-size: 1.3rem;
    color: #1F4E79;
    padding: 0 0 10px 14px;
    margin: 0 0 20px;
    border-left: 4px solid #C9A96E;
    border-bottom: 1px solid #e4e8ef;
}}
.archive-list {{
    list-style: none;
    padding: 0;
    margin: 0;
}}
.archive-item {{ margin-bottom: 12px; }}
.archive-link {{
    display: grid;
    grid-template-columns: 110px 1fr;
    grid-template-areas:
        "date title"
        "date desc";
    column-gap: 18px;
    row-gap: 4px;
    padding: 14px 18px;
    background: #fff;
    border: 1px solid #e4e8ef;
    border-radius: 10px;
    text-decoration: none;
    color: #1a2233;
    transition: all .2s;
}}
.archive-link:hover {{
    border-color: #1F4E79;
    box-shadow: 0 4px 16px rgba(31, 78, 121, 0.08);
    transform: translateX(2px);
}}
.archive-date {{
    grid-area: date;
    color: #C9A96E;
    font-size: 0.9rem;
    letter-spacing: 0.06em;
    align-self: start;
    padding-top: 2px;
}}
.archive-title {{
    grid-area: title;
    font-family: 'Noto Serif TC', serif;
    font-weight: 700;
    color: #15395a;
    font-size: 1.05rem;
    line-height: 1.5;
}}
.archive-desc {{
    grid-area: desc;
    color: #4a5568;
    font-size: 0.92rem;
    line-height: 1.7;
    overflow: hidden;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
}}
@media (max-width: 600px) {{
    .archive-link {{
        grid-template-columns: 1fr;
        grid-template-areas:
            "date"
            "title"
            "desc";
    }}
    .archive-date {{ padding-top: 0; }}
}}
.back-link {{
    display: inline-block;
    margin-top: 40px;
    color: #1F4E79;
    text-decoration: none;
    font-size: 0.95rem;
}}
.back-link:hover {{ text-decoration: underline; }}
</style>
</head>
<body>

<header class="nav">
    <div class="container nav-inner">
        <a href="../" class="brand">昆廷老師</a>
        <nav class="nav-links">
            <a href="../about.html">作者</a>
            <a href="../cooperation.html">合作</a>
            <a href="../#services">服務</a>
            <a href="../learn-claude.html">Claude 教學</a>
            <a href="../#about">關於</a>
            <a href="../#topics">核心主題</a>
            <a href="./">文章</a>
            <a href="../#contact">聯絡</a>
        </nav>
    </div>
</header>

<section class="archive-hero">
    <div class="container">
        <div class="archive-count">ARCHIVE · 共 {total} 篇</div>
        <h1>全部文章</h1>
        <p>從企業 AI 導入、易經決策到中小企業數位轉型的實戰觀點，按時間排序。</p>
    </div>
</section>

<main class="archive-body">
{body}
<a href="../" class="back-link">← 回首頁</a>
</main>

<footer class="footer">
    <div class="container">
        <p class="footer-bio">企業 AI 導入顧問，提供 Claude Code 教學、數位轉型實作與易經決策對話。昆廷老師陪中小企業主與社會人士先想清楚問題，再把 AI 工具真正接進工作流程。</p>
        <p class="footer-copy">© 2026 昆廷老師. All rights reserved.</p>
    </div>
</footer>

</body>
</html>
"""


def main():
    parser = argparse.ArgumentParser(description="Build articles/index.html from articles/*.html")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if not ARTICLES_DIR.exists():
        sys.exit(f"[ERR] {ARTICLES_DIR} not found")

    articles = collect_articles()
    print(f"Found {len(articles)} articles")
    for a in articles[:5]:
        print(f"  {a['date']}  {a['title']}")
    if len(articles) > 5:
        print(f"  ... ({len(articles) - 5} more)")

    html_text = render(articles)
    if args.dry_run:
        print(f"\n[dry-run] would write {OUTPUT} ({len(html_text)} bytes)")
        return

    OUTPUT.write_text(html_text, encoding="utf-8")
    print(f"\n+ Wrote {OUTPUT.relative_to(BASE_DIR)} ({len(html_text)} bytes)")


if __name__ == "__main__":
    main()
