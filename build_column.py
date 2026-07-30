#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_column.py — コラム記事台帳から一覧・トップ・sitemapを同期する

正本: column/articles.json（新しい記事は配列の先頭に追加）
同期先:
  1. column/index.html  … 記事一覧（新しい順・全記事）
  2. index.html         … トップ「お薬と薬局のコラム」の最新3本
  3. sitemap.xml        … コラム部分のURL・lastmod（トップページのlastmodも追随）

対象範囲は各ファイルの BUILD マーカーコメントの内側だけ。
記事本体 (column/<slug>.html) と挿絵 (images/column/*.svg) はこのスクリプトでは作らない。

使い方:  py -X utf8 build_column.py
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = "https://www.sizucu.co.jp"

REQUIRED = [
    "slug", "title", "description", "category", "categoryJp", "color",
    "date", "thumb", "thumbAlt", "thumbWidth", "thumbHeight",
    "teaserTitle", "teaserText",
]
COLORS = {"green", "orange", "blue"}
DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}$")


def fail(msg):
    print(msg)
    sys.exit(1)


def load_articles():
    path = ROOT / "column" / "articles.json"
    if not path.exists():
        fail(f"[エラー] {path} がありません")
    data = json.loads(path.read_text(encoding="utf-8"))
    articles = data.get("articles", [])
    if not articles:
        fail("[エラー] articles.json に記事がありません")

    errors = []
    slugs = set()
    for a in articles:
        slug = a.get("slug", "?")
        for key in REQUIRED:
            if not str(a.get(key, "")).strip():
                errors.append(f"{slug}: {key} が空です")
        if a.get("color") not in COLORS:
            errors.append(f"{slug}: color は green / orange / blue のいずれかにしてください")
        if not DATE_RE.match(a.get("date", "")):
            errors.append(f"{slug}: date は YYYY-MM-DD 形式にしてください")
        if a.get("updated") and not DATE_RE.match(a["updated"]):
            errors.append(f"{slug}: updated は YYYY-MM-DD 形式にしてください")
        if slug in slugs:
            errors.append(f"{slug}: slug が重複しています")
        slugs.add(slug)
        if not (ROOT / "column" / f"{slug}.html").exists():
            errors.append(f"{slug}: column/{slug}.html がありません（記事本体を先に作成してください）")
        if not (ROOT / "images" / "column" / a.get("thumb", "")).exists():
            errors.append(f"{slug}: images/column/{a.get('thumb')} がありません（挿絵を先に作成してください）")
    if errors:
        print("[エラー] articles.json の検証に失敗しました:")
        for e in errors:
            print("  -", e)
        sys.exit(1)

    # 新しい順。同日の記事は配列で先にあるものが先（安定ソート）
    return sorted(articles, key=lambda a: a["date"], reverse=True)


def jdate(iso):
    y, m, d = iso.split("-")
    return f"{int(y)}年{int(m)}月{int(d)}日"


def lastmod(a):
    return a.get("updated") or a["date"]


def post_card(a):
    """column/index.html の一覧カード"""
    return f'''      <li>
        <a class="post-card post-card--{a["color"]}" href="{a["slug"]}.html">
          <div class="post-thumb"><img src="../images/column/{a["thumb"]}" alt="{a["thumbAlt"]}" width="{a["thumbWidth"]}" height="{a["thumbHeight"]}" loading="lazy"></div>
          <div class="post-body">
            <span class="cat">{a["category"]}<span class="jp">{a["categoryJp"]}</span></span>
            <h2>{a["title"]}</h2>
            <p>{a["description"]}</p>
            <span class="meta">{jdate(a["date"])}</span>
          </div>
        </a>
      </li>'''


def teaser_card(a):
    """トップページの最新3本カード"""
    return f'''        <a class="column-card column-card--{a["color"]}" href="column/{a["slug"]}.html">
          <div class="column-card-thumb"><img src="images/column/{a["thumb"]}" alt="{a["thumbAlt"]}" width="{a["thumbWidth"]}" height="{a["thumbHeight"]}" loading="lazy"></div>
          <div class="column-card-body">
            <span class="column-card-cat">{a["category"]}</span>
            <h3 class="column-card-title">{a["teaserTitle"]}</h3>
            <p class="column-card-text">{a["teaserText"]}</p>
            <span class="column-card-more">記事を読む →</span>
          </div>
        </a>'''


def sitemap_url(loc, mod, freq):
    return f'''  <url>
    <loc>{loc}</loc>
    <lastmod>{mod}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>0.6</priority>
  </url>'''


def sitemap_block(articles):
    col_lastmod = max(lastmod(a) for a in articles)
    parts = [sitemap_url(f"{SITE}/column/", col_lastmod, "monthly")]
    for a in articles:
        parts.append(sitemap_url(f"{SITE}/column/{a['slug']}.html", lastmod(a), "yearly"))
    return "\n".join(parts)


def replace_between(path, start_marker, end_marker, body):
    """マーカーの内側だけを差し替える。改行コード(CRLF/LF)は元ファイルに合わせる。"""
    raw = path.read_bytes().decode("utf-8")
    crlf = "\r\n" in raw
    text = raw.replace("\r\n", "\n")

    i = text.find(start_marker)
    j = text.find(end_marker)
    if i == -1 or j == -1 or j <= i:
        fail(f"[エラー] {path.name}: マーカーが見つかりません\n"
             f"  必要: {start_marker} … {end_marker}")

    # STARTマーカーはコメントの閉じ -->（説明文込み）までを保持して、その直後から差し替える
    close = text.find("-->", i)
    if close == -1 or close > j:
        fail(f"[エラー] {path.name}: STARTマーカーのコメントが --> で閉じられていません")
    head_end = close + len("-->")
    line_start = text.rfind("\n", 0, j) + 1  # ENDマーカー行の行頭（インデント保持）
    new_text = text[:head_end] + "\n" + body + "\n" + text[line_start:]

    changed = new_text != text
    if changed:
        out = new_text.replace("\n", "\r\n") if crlf else new_text
        path.write_bytes(out.encode("utf-8"))
    return changed


def bump_top_lastmod(articles):
    """sitemap.xml のトップページ lastmod を、コラム最終更新日まで進める（巻き戻しはしない）"""
    path = ROOT / "sitemap.xml"
    raw = path.read_bytes().decode("utf-8")
    crlf = "\r\n" in raw
    text = raw.replace("\r\n", "\n")
    col_lastmod = max(lastmod(a) for a in articles)

    pat = re.compile(r"(<loc>" + re.escape(SITE) + r"/</loc>\s*<lastmod>)(\d{4}-\d{2}-\d{2})(</lastmod>)")
    m = pat.search(text)
    if not m:
        print("[注意] sitemap.xml にトップページの lastmod が見つからず、更新をスキップしました")
        return False
    if m.group(2) >= col_lastmod:
        return False
    new_text = pat.sub(lambda mm: mm.group(1) + col_lastmod + mm.group(3), text, count=1)
    out = new_text.replace("\n", "\r\n") if crlf else new_text
    path.write_bytes(out.encode("utf-8"))
    return True


def verify(articles):
    """生成後の完全性チェック。HTMLタグバランス・XML妥当性・リンク実在を毎回確認する。"""
    from html.parser import HTMLParser
    import xml.etree.ElementTree as ET

    void_tags = {"meta", "link", "img", "br", "input", "hr", "source", "path", "circle",
                 "rect", "use", "area", "base", "col", "embed", "track", "wbr"}

    class Checker(HTMLParser):
        def __init__(self):
            super().__init__(convert_charrefs=True)
            self.stack, self.errors = [], []

        def handle_starttag(self, tag, attrs):
            if tag not in void_tags:
                self.stack.append(tag)

        def handle_endtag(self, tag):
            if tag in void_tags:
                return
            if not self.stack:
                self.errors.append(f"余分な閉じタグ </{tag}> (行{self.getpos()[0]})")
            elif self.stack[-1] != tag:
                self.errors.append(f"タグ不一致 <{self.stack[-1]}> vs </{tag}> (行{self.getpos()[0]})")
            else:
                self.stack.pop()

    problems = []
    targets = [ROOT / "index.html", ROOT / "column" / "index.html"]
    targets += [ROOT / "column" / f"{a['slug']}.html" for a in articles]
    for f in targets:
        content = f.read_text(encoding="utf-8")
        c = Checker()
        c.feed(content)
        leftover = [t for t in c.stack if t != "html"]
        if c.errors or leftover:
            problems.append(f"{f.relative_to(ROOT)}: {c.errors[:3]} 未閉じ={leftover[:5]}")
        if "{{" in content:
            problems.append(f"{f.relative_to(ROOT)}: テンプレートの置換漏れ {{{{…}}}} が残っています")

    try:
        ET.parse(ROOT / "sitemap.xml")
    except ET.ParseError as e:
        problems.append(f"sitemap.xml: XMLとして不正 ({e})")

    if problems:
        print("[エラー] 生成後チェックに失敗しました:")
        for p in problems:
            print("  -", p)
        sys.exit(1)
    print(f"[OK] 検証: HTML {len(targets)} ファイルのタグ対応・sitemap.xml の妥当性に問題なし")


def main():
    articles = load_articles()
    latest3 = articles[:3]

    changed = []
    if replace_between(ROOT / "column" / "index.html",
                       "<!-- BUILD:POST-LIST START", "<!-- BUILD:POST-LIST END -->",
                       "\n".join(post_card(a) for a in articles)):
        changed.append("column/index.html")
    if replace_between(ROOT / "index.html",
                       "<!-- BUILD:COLUMN-TEASER START", "<!-- BUILD:COLUMN-TEASER END -->",
                       "\n\n".join(teaser_card(a) for a in latest3)):
        changed.append("index.html")
    if replace_between(ROOT / "sitemap.xml",
                       "<!-- BUILD:COLUMN START", "<!-- BUILD:COLUMN END -->",
                       sitemap_block(articles)):
        changed.append("sitemap.xml")
    if bump_top_lastmod(articles):
        changed.append("sitemap.xml (トップlastmod)")

    verify(articles)

    print(f"[OK] 記事 {len(articles)} 本を同期しました")
    print(f"  更新ファイル: {', '.join(changed) if changed else '（変更なし）'}")
    print("  掲載順（新しい順）:")
    for a in articles:
        mark = "  ★トップ掲載" if a in latest3 else ""
        print(f"    {a['date']}  {a['slug']:24s} ({a['color']}){mark}")


if __name__ == "__main__":
    main()
