"""
sync_from_brand_profile.py
=======================================================
把 C:\\claude\\auto-post\\data\\brand_profile.json 的最新內容，
自動同步到 personal-website/index.html 的 <!-- BRAND:xxx --> marker 區段。

特性：
  - 只替換 marker 之間的內容，不會動手寫的金句、文章、聯絡方式
  - JSON-LD 會保留你部署後填入的 "url" 與 "sameAs"
  - 預設自動備份 index.html → index.html.bak
  - --dry-run 只顯示會改什麼、不實際寫檔
  - 可指定不同的 profile 路徑或不同的 index.html

用法：
  python sync_from_brand_profile.py                # 同步 + 備份
  python sync_from_brand_profile.py --dry-run      # 只看會改什麼
  python sync_from_brand_profile.py --no-backup    # 不備份
"""

import argparse
import html
import io
import json
import re
import shutil
import sys
from pathlib import Path

# 讓 Windows cp950 終端機也能印中文 + 符號
try:
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

BASE_DIR = Path(__file__).parent
# 抽離後改指向 exposure-engine 的 brand_profile（auto-post 版已廢棄）
DEFAULT_PROFILE = Path("C:/claude/exposure-engine/data/brand_profile.json")
DEFAULT_INDEX = BASE_DIR / "index.html"


# ═══════════════════════ 轉換邏輯（brand_profile → HTML 片段） ═══════════════════════

def _eyebrow_from_profile(bp: dict) -> str:
    """從 platform_bios.website_about 第一行「｜」之後抓頭銜。"""
    about = (bp.get("platform_bios", {}) or {}).get("website_about", "")
    first_line = about.split("\n", 1)[0].strip()
    if "｜" in first_line:
        return first_line.split("｜", 1)[1].strip()
    return bp.get("tagline", "")


def _tagline_with_br(tagline: str) -> str:
    """中文逗號/句號後換行。若無標點則整句不換。"""
    for sep in ("，", "、", "，", ","):
        if sep in tagline:
            left, right = tagline.split(sep, 1)
            return f"{html.escape(left) + sep}<br>{html.escape(right.strip())}"
    return html.escape(tagline)


def _bold_keywords(paragraph: str, keywords: list) -> str:
    """在段落中把 keywords 包 <strong>（只加到每段第一次出現）。"""
    # 保留已存在的 <strong>；也避免在已 escape 的片段中重複包
    esc = html.escape(paragraph)
    for kw in keywords:
        if not kw:
            continue
        kw_esc = html.escape(kw)
        # 只在段落第一次出現處包，且避免重複巢狀
        if f"<strong>{kw_esc}</strong>" in esc:
            continue
        esc = esc.replace(kw_esc, f"<strong>{kw_esc}</strong>", 1)
    return esc


def _about_prose_html(bio_long: str, keywords: list) -> str:
    """bio_long 切段（\\n\\n）→ 每段 <p>；第一段加粗前 4 個核心關鍵字。"""
    paragraphs = [p.strip() for p in bio_long.split("\n\n") if p.strip()]
    out_lines = []
    core_kws = (keywords or [])[:4]
    for i, p in enumerate(paragraphs):
        if i == 0:
            out_lines.append(f"            <p>{_bold_keywords(p, core_kws)}</p>")
        else:
            out_lines.append(f"            <p>{html.escape(p)}</p>")
    return "\n\n".join(out_lines)


def _build_jsonld_html(bp: dict, existing_jsonld: dict | None) -> str:
    """產出 JSON-LD <script> 區塊。保留現有的 url / sameAs。"""
    keywords = (bp.get("_meta", {}) or {}).get("keywords") or bp.get("keywords", [])
    identity = (bp.get("_meta", {}) or {}).get("source_form", {}).get("identity", "企業顧問")

    # 保留部署後填入的 url / sameAs
    existing_url = (existing_jsonld or {}).get("url", "")
    existing_same_as = (existing_jsonld or {}).get("sameAs", [""])

    jsonld = {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": bp.get("name", ""),
        "alternateName": bp.get("tagline", ""),
        "description": bp.get("bio_medium") or bp.get("positioning_statement", ""),
        "jobTitle": identity,
        "knowsAbout": bp.get("keywords") or keywords,
        "url": existing_url,
        "sameAs": existing_same_as if existing_same_as else [""],
    }
    body = json.dumps(jsonld, ensure_ascii=False, indent=2)
    return f'<script type="application/ld+json">\n{body}\n</script>'


def _extract_existing_jsonld(html_text: str) -> dict | None:
    """從目前的 HTML 擷取 JSON-LD 以保留 url/sameAs。"""
    m = re.search(
        r"<!--\s*BRAND:jsonld\s*-->\s*<script[^>]*>(.*?)</script>\s*<!--\s*/BRAND:jsonld\s*-->",
        html_text,
        re.DOTALL,
    )
    if not m:
        return None
    try:
        return json.loads(m.group(1).strip())
    except json.JSONDecodeError:
        return None


# ═══════════════════════ Marker 定義 ═══════════════════════

def build_replacements(bp: dict, existing_jsonld: dict | None) -> dict:
    name = bp.get("name", "")
    tagline = bp.get("tagline", "")
    positioning = bp.get("positioning_statement", "")
    bio_short = bp.get("bio_short", "")
    bio_long = bp.get("bio_long", "")
    keywords = bp.get("keywords", []) or []
    eyebrow = _eyebrow_from_profile(bp)
    about_lede = f"{name}｜{eyebrow}" if eyebrow else name

    head_title = f"{name}｜{eyebrow}" if eyebrow else name
    og_description = positioning  # 完整定位陳述
    twitter_description = bio_short or positioning

    # Head 區的 marker 要包整個 element（因為 HTML 註解放 <title> 或 <meta content> 內
    # 會被當成純文字，不會被瀏覽器當成 comment）
    ht = html.escape(head_title)
    return {
        # Head — 每個值是完整 element 字串
        "head_title": f"<title>{ht}</title>",
        "meta_description": f'<meta name="description" content="{html.escape(positioning)}">',
        "meta_author": f'<meta name="author" content="{html.escape(name)}">',
        "meta_keywords": f'<meta name="keywords" content="{html.escape(", ".join(keywords))}">',
        "og_title": f'<meta property="og:title" content="{ht}">',
        "og_description": f'<meta property="og:description" content="{html.escape(og_description)}">',
        "og_site_name": f'<meta property="og:site_name" content="{html.escape(name)}">',
        "twitter_title": f'<meta name="twitter:title" content="{ht}">',
        "twitter_description": f'<meta name="twitter:description" content="{html.escape(twitter_description)}">',
        "jsonld": _build_jsonld_html(bp, existing_jsonld),

        # Body
        "nav_brand": html.escape(name),
        "hero_eyebrow": html.escape(eyebrow),
        "hero_title": _tagline_with_br(tagline),
        "hero_cta_about": html.escape(f"認識{name}"),
        "about_h2": html.escape(f"關於{name}"),
        "about_lede": html.escape(about_lede),
        "about_prose": "\n" + _about_prose_html(bio_long, keywords) + "\n            ",
        "footer_bio": html.escape(bio_short),
    }


# ═══════════════════════ Marker 替換 ═══════════════════════

MARKER_PATTERN = re.compile(
    r"<!--\s*BRAND:(?P<key>[a-z0-9_]+)\s*-->(?P<content>.*?)<!--\s*/BRAND:(?P=key)\s*-->",
    re.DOTALL,
)


def apply_replacements(html_text: str, replacements: dict) -> tuple[str, list]:
    """回傳 (new_html, diff_list)。"""
    diffs = []

    def repl(m: re.Match) -> str:
        key = m.group("key")
        old = m.group("content")
        if key not in replacements:
            diffs.append((key, "(no mapping)", "skipped"))
            return m.group(0)
        new = replacements[key]
        if old.strip() == new.strip():
            diffs.append((key, _short(old), "unchanged"))
        else:
            diffs.append((key, _short(old), _short(new)))
        return f"<!-- BRAND:{key} -->{new}<!-- /BRAND:{key} -->"

    new_html = MARKER_PATTERN.sub(repl, html_text)
    return new_html, diffs


def _short(s: str, length: int = 60) -> str:
    one_line = re.sub(r"\s+", " ", s.strip())
    return (one_line[:length] + "…") if len(one_line) > length else one_line


# ═══════════════════════ CLI ═══════════════════════

def main():
    parser = argparse.ArgumentParser(description="Sync brand_profile.json → index.html marker sections")
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE, help="path to brand_profile.json")
    parser.add_argument("--index", type=Path, default=DEFAULT_INDEX, help="path to index.html")
    parser.add_argument("--dry-run", action="store_true", help="show diff only, do not write")
    parser.add_argument("--no-backup", action="store_true", help="skip .bak backup")
    args = parser.parse_args()

    if not args.profile.exists():
        sys.exit(f"[ERR] profile not found: {args.profile}")
    if not args.index.exists():
        sys.exit(f"[ERR] index.html not found: {args.index}")

    print(f"Reading {args.profile} ...")
    bp = json.loads(args.profile.read_text(encoding="utf-8"))
    print(f"  +name: {bp.get('name', '(empty)')}")
    print(f"  +tagline: {bp.get('tagline', '(empty)')}")

    html_text = args.index.read_text(encoding="utf-8")
    existing_jsonld = _extract_existing_jsonld(html_text)
    if existing_jsonld and (existing_jsonld.get("url") or existing_jsonld.get("sameAs") not in ([""], [], None)):
        print(f"  +preserving existing JSON-LD url/sameAs")

    replacements = build_replacements(bp, existing_jsonld)
    new_html, diffs = apply_replacements(html_text, replacements)

    print()
    print(f"Found {len(diffs)} markers:")
    changed = 0
    for key, old, new in diffs:
        if new == "unchanged":
            print(f"  [=] {key:22s} {old}")
        elif new == "skipped":
            print(f"  [!] {key:22s} (no mapping in script)")
        else:
            changed += 1
            print(f"  [~] {key:22s} {old}")
            print(f"      {'':22s} → {new}")
    print()
    print(f"Summary: {changed} changed, {len(diffs) - changed} unchanged/skipped")

    if args.dry_run:
        print("[dry-run] no files written.")
        return

    if changed == 0:
        print("Nothing to write.")
        return

    if not args.no_backup:
        bak = args.index.with_suffix(args.index.suffix + ".bak")
        shutil.copyfile(args.index, bak)
        print(f"Backup: {bak.name}")

    args.index.write_text(new_html, encoding="utf-8")
    print(f"+ Wrote {args.index.name}")


if __name__ == "__main__":
    main()
