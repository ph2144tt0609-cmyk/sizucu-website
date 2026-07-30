# -*- coding: utf-8 -*-
"""中日ドラゴンズ だいすきクイズ100もん — A4 PDF 用 HTML ジェネレーター"""

MC, OX, MATH = "mc", "ox", "math"

# セクション定義: (key, 見出し, 絵文字, 色, 薄い色)
SECTIONS = {
    "s1": ("ドラゴンズの クイズ", "🐉", "#0a3ea0", "#e3ecfb"),
    "s2": ("やきゅうの きほん クイズ", "⚾", "#0077c8", "#e0f1fb"),
    "s3": ("まるばつ クイズ", "⭕", "#e88a00", "#fdf0da"),
    "s4": ("ドラゴンズ さんすう", "✏️", "#159a4a", "#e2f5e9"),
}

Q = []  # (sec, type, text, choices, ans)

def mc(sec, text, choices, ans):
    Q.append((sec, MC, text, choices, ans))

def ox(sec, text, ans):
    Q.append((sec, OX, text, None, ans))

def ma(sec, text, ans):
    Q.append((sec, MATH, text, None, ans))

# ---------- だい1しょう ドラゴンズの クイズ (1-25) ----------
mc("s1", "ドラゴンズの 「ドラゴン」は どんな いきもの?", ["りゅう", "とら", "うさぎ"], 1)
mc("s1", "ドラゴンズの チームカラーは なにいろ?", ["あか", "あお", "きいろ"], 2)
mc("s1", "ドラゴンズの ホームタウンは どこ?", ["とうきょう", "おおさか", "なごや"], 3)
mc("s1", "なごやが ある けんは どこ?", ["あいちけん", "ほっかいどう", "おきなわけん"], 1)
mc("s1", "ドラゴンズの ホームきゅうじょうは どれ?", ["とうきょうドーム", "バンテリンドーム", "こうしえん"], 2)
mc("s1", "マスコットの ドアラは どんな どうぶつ?", ["パンダ", "ゴリラ", "コアラ"], 3)
mc("s1", "ドアラが とくいな わざは どれ?", ["けんだま", "バクてん", "さかあがり"], 2)
mc("s1", "マスコットの シャオロンは なんの いきもの?", ["ねこ", "きょうりゅう", "りゅう"], 3)
mc("s1", "ドラゴンズの マスコットは なんにん いる?", ["1にん", "2にん", "3にん"], 3)
mc("s1", "ドアラ・シャオロンと あと 1にんは だれ?", ["メロロン", "パオロン", "バナロン"], 2)
mc("s1", "ドラゴンズが はいって いる リーグは?", ["セ・リーグ", "パ・リーグ", "Jリーグ"], 1)
mc("s1", "おなじ セ・リーグの チームは どれ?", ["ホークス", "ファイターズ", "ジャイアンツ"], 3)
mc("s1", "ゆうめいな おうえんかは どれ?", ["チューリップ", "もえよドラゴンズ!", "うみ"], 2)
mc("s1", "しんぶんで ドラゴンズを あらわす かんじは?", ["竜(りゅう)", "虎(とら)", "鷹(たか)"], 1)
mc("s1", "あめの ひ、ドームの しあいは どうなる?", ["ちゅうしに なる", "プールに なる", "そのまま できる"], 3)
mc("s1", "おうえんの とき ファンが てに もつ ものは?", ["メガホン", "フライパン", "かさ"], 1)
mc("s1", "なごやの ゆうめいな たべものは どれ?", ["たこやき", "みそカツ", "ジンギスカン"], 2)
mc("s1", "はるの キャンプ(れんしゅう)は どこで やる?", ["ほっかいどう", "うちゅう", "おきなわ"], 3)
mc("s1", "コアラが たくさん すんで いる くには?", ["オーストラリア", "エジプト", "フランス"], 1)
mc("s1", "おはなしの りゅうが くちから はく ものは?", ["みず", "ひ", "シャボンだま"], 2)
mc("s1", "コアラが たべる はっぱは どれ?", ["ユーカリのは", "ささのは", "バナナのは"], 1)
mc("s1", "ユニフォームの せなかに かいて あるのは?", ["せばんごう", "でんわばんごう", "おなまえシール"], 1)
mc("s1", "ドラゴンズを おうえんする ひとを なんと いう?", ["フォーク", "フライ", "ファン"], 3)
mc("s1", "しあいの まえに せんしゅが する ことは?", ["ひるね", "れんしゅう", "かいもの"], 2)
mc("s1", "ドームの グラウンドは こうていより?", ["ずっと ひろい", "おなじくらい", "せまい"], 1)

# ---------- だい2しょう やきゅうの きほん (26-50) ----------
mc("s2", "やきゅうは 1チーム なんにんで まもる?", ["7にん", "9にん", "11にん"], 2)
mc("s2", "ストライクが 3つに なると?", ["アウト", "ホームラン", "タイム"], 1)
mc("s2", "アウトが 3つに なると どうなる?", ["しあい おわり", "おやつ", "せめと まもり こうたい"], 3)
mc("s2", "ボールを なげる せんしゅは だれ?", ["ピッチャー", "キャッチャー", "バッター"], 1)
mc("s2", "ピッチャーの たまを うける せんしゅは?", ["ランナー", "コーチ", "キャッチャー"], 3)
mc("s2", "ボールを うつ どうぐは どれ?", ["ラケット", "バット", "つりざお"], 2)
mc("s2", "ボールを とる とき てに つける ものは?", ["ながぐつ", "ヘルメット", "グローブ"], 3)
mc("s2", "スタンドまで たまを とばす うちかたは?", ["タッチダウン", "ホームラン", "シュート"], 2)
mc("s2", "しあいは ふつう なんかいまで やる?", ["3かい", "6かい", "9かい"], 3)
mc("s2", "ベースは ホームも いれて ぜんぶで いくつ?", ["3つ", "4つ", "5つ"], 2)
mc("s2", "ランナーが ホームベースまで かえると?", ["1てん はいる", "アウトに なる", "やりなおし"], 1)
mc("s2", "しあいに かつのは どんな チーム?", ["こえが おおきい", "てんが おおい", "せが たかい"], 2)
mc("s2", "ボールが 4つに なると バッターは?", ["アウトに なる", "おうちに かえる", "1るいへ すすめる"], 3)
mc("s2", "うった たまが おちる まえに とられたら?", ["セーフ", "アウト", "ホームラン"], 2)
mc("s2", "1るいの つぎに はしって いく ベースは?", ["2るい", "3るい", "ホームベース"], 1)
mc("s2", "にほんの プロやきゅうチームは いくつ?", ["8チーム", "12チーム", "20チーム"], 2)
mc("s2", "セ・リーグと もう ひとつの リーグは?", ["ピ・リーグ", "プ・リーグ", "パ・リーグ"], 3)
mc("s2", "やきゅうの ボールは なにいろ?", ["しろ", "くろ", "みどり"], 1)
mc("s2", "ボールの ぬいめ(いと)は なにいろ?", ["あお", "きんいろ", "あか"], 3)
mc("s2", "かんとくの おしごとは どれ?", ["きっぷを うる", "さくせんを きめる", "そうじを する"], 2)
mc("s2", "しあいの はじまりに いう ことばは?", ["プレイボール!", "いただきます!", "おやすみなさい!"], 1)
mc("s2", "そとの ほうを まもる せんしゅは?", ["ないやしゅ", "うんてんしゅ", "がいやしゅ"], 3)
mc("s2", "ホームランを うったら どう する?", ["ベースを 1しゅう", "すぐ すわる", "かくれる"], 1)
mc("s2", "バッターが あたまに かぶる ものは?", ["むぎわらぼうし", "ヘルメット", "ニットぼう"], 2)
mc("s2", "しんぱんが りょうてを よこに ひろげたら?", ["アウト", "ストライク", "セーフ"], 3)

# ---------- だい3しょう まるばつクイズ (51-75) ----------
ox("s3", "ドアラは パンダで ある。", "×")
ox("s3", "ドラゴンズの ホームは とうきょうに ある。", "×")
ox("s3", "バンテリンドームには やねが ある。", "○")
ox("s3", "やきゅうは ボールを あしで ける スポーツだ。", "×")
ox("s3", "ホームランを うつと てんが はいる。", "○")
ox("s3", "ストライク 2つで アウトに なる。", "×")
ox("s3", "しあいは ふつう 5かいで おわる。", "×")
ox("s3", "キャッチャーは かおに マスクを つける。", "○")
ox("s3", "ドアラは バクてんで ゆうめいだ。", "○")
ox("s3", "シャオロンと パオロンは ねこの なかまだ。", "×")
ox("s3", "ドラゴンズは 50ねん いじょう まえから ある。", "○")
ox("s3", "セ・リーグには ぜんぶで 6チーム ある。", "○")
ox("s3", "やきゅうの ボールは しかくい。", "×")
ox("s3", "グローブは あたまに かぶる どうぐだ。", "×")
ox("s3", "ドームの なかは ライトで あかるい。", "○")
ox("s3", "ファウルボールが きたら よく みて きを つける。", "○")
ox("s3", "せんしゅは しあいちゅう みずを のめない。", "×")
ox("s3", "おうえんグッズには タオルも ある。", "○")
ox("s3", "おうえんは おおきな こえで しても いい。", "○")
ox("s3", "やきゅうの しあいに しんぱんは いない。", "×")
ox("s3", "かんとくも ユニフォームを きて いる。", "○")
ox("s3", "ドアラは そらを とべる。", "×")
ox("s3", "ほんものの りゅうが ドームに すんで いる。", "×")
ox("s3", "ドームには いすが たくさん ある。", "○")
ox("s3", "まけても つぎ がんばれば だいじょうぶ。", "○")

# ---------- だい4しょう ドラゴンズさんすう (76-100) ----------
ma("s4", "3てんと 2てんを とったよ。あわせて なんてん?", "5てん")
ma("s4", "ドラゴンズ 4てん、あいて 1てん。なんてんがち?", "3てん")
ma("s4", "ボールが 10こ。3こ とんで いった。のこりは?", "7こ")
ma("s4", "せんしゅ 9にんと かんとく 1にん。あわせて?", "10にん")
ma("s4", "メガホン 6ぽんの うち 2ほん かした。のこりは?", "4ほん")
ma("s4", "ドアラが ホームラン 3ぼん、パオロンが 4ほん。あわせて なんぼん?", "7ほん")
ma("s4", "スタンドに 20にん。あとから 10にん きたよ。ぜんぶで なんにん?", "30にん")
ma("s4", "しあいは 9かいまで。6かい おわったよ。のこりは なんかい?", "3かい")
ma("s4", "ジュースは 1ぱい 100えん。2はい かうと なんえん?", "200えん")
ma("s4", "バクてんに 7かい ちょうせんして 5かい せいこう。しっぱいは なんかい?", "2かい")
ma("s4", "ベースは 1しゅうで 4つ ふむよ。2しゅうでは いくつ ふむ?", "8つ")
ma("s4", "1チームは 9にん。2チームでは ぜんぶで なんにん?", "18にん")
ma("s4", "ボールが 1はこに 5こ。3はこでは なんこ?", "15こ")
ma("s4", "よる 6じに しあいが はじまり、3じかんで おわった。おわったのは なんじ?", "よる9じ")
ma("s4", "タオルを 4にんに 2まいずつ くばるよ。ぜんぶで なんまい?", "8まい")
ma("s4", "7たい7の どうてん! あと 1てん とったら なんてん?", "8てん")
ma("s4", "カードを 3にんに 4まいずつ あげるよ。ぜんぶで なんまい?", "12まい")
ma("s4", "ホームランが きょう 2ほん、きのう 1ぽん、おととい 1ぽん。ぜんぶで?", "4ほん")
ma("s4", "50えんの カードと 30えんの シールを かうよ。あわせて なんえん?", "80えん")
ma("s4", "いすが 1れつに 8こ。2れつでは なんこ?", "16こ")
ma("s4", "ドアラは まいにち バクてんを 2かい。1しゅうかん(7にち)では なんかい?", "14かい")
ma("s4", "しあいは 2じから。その 30ぷん まえに つくには なんじ なんぷん?", "1じ30ぷん")
ma("s4", "こんしゅう 3しょう、らいしゅう 2しょうすると、あわせて なんしょう?", "5しょう")
ma("s4", "ファン 100にんの うち 60にんが タオルを もって いる。もって いないのは?", "40にん")
ma("s4", "クイズは ぜんぶで 100もん。99もん おわった。のこりは なんもん?", "1もん")

assert len(Q) == 100, f"問題数が {len(Q)} 問です"

CIRCLED = {1: "①", 2: "②", 3: "③"}

BASEBALL_SVG = """<svg class="bb" viewBox="0 0 100 100">
<circle cx="50" cy="50" r="46" fill="#ffffff" stroke="#d8dee9" stroke-width="3"/>
<path d="M22 9 Q 50 50 22 91" fill="none" stroke="#e04747" stroke-width="4" stroke-linecap="round" stroke-dasharray="0.1 9"/>
<path d="M78 9 Q 50 50 78 91" fill="none" stroke="#e04747" stroke-width="4" stroke-linecap="round" stroke-dasharray="0.1 9"/>
<path d="M22 9 Q 50 50 22 91" fill="none" stroke="#e04747" stroke-width="2"/>
<path d="M78 9 Q 50 50 78 91" fill="none" stroke="#e04747" stroke-width="2"/>
</svg>"""


def q_card(i, sec, typ, text, choices, ans):
    color, light = SECTIONS[sec][2], SECTIONS[sec][3]
    body = f'<div class="qt">{text}</div>'
    if typ == MC:
        ch = "".join(
            f'<span class="c"><b style="color:{color}">{CIRCLED[k+1]}</b>{c}</span>'
            for k, c in enumerate(choices)
        )
        body += f'<div class="ch">{ch}</div>'
        return (
            f'<div class="q" style="--c:{color};--l:{light}">'
            f'<div class="num">{i}</div><div class="qb">{body}</div></div>'
        )
    if typ == OX:
        return (
            f'<div class="q" style="--c:{color};--l:{light}">'
            f'<div class="num">{i}</div><div class="qb">{body}</div>'
            f'<div class="oxpick"><span>○</span><span>×</span></div></div>'
        )
    return (
        f'<div class="q" style="--c:{color};--l:{light}">'
        f'<div class="num">{i}</div><div class="qb">{body}</div>'
        f'<div class="ansbox"><span class="al">こたえ</span></div></div>'
    )


def ribbon(sec, cont=False):
    title, emoji, color, _light = SECTIONS[sec]
    suffix = '<span class="cont">つづき</span>' if cont else ""
    return f'<div class="sec" style="--c:{color}"><span class="em">{emoji}</span>{title}{suffix}</div>'


def render_range(a, b):
    """問題番号 a..b (1はじまり) のカードとセクションリボンを出力"""
    out = []
    prev_sec = Q[a - 2][0] if a > 1 else None
    for idx in range(a, b + 1):
        sec, typ, text, choices, ans = Q[idx - 1]
        if sec != prev_sec:
            out.append(ribbon(sec))
            prev_sec = sec
        elif idx == a:
            out.append(ribbon(sec, cont=True))
        out.append(q_card(idx, sec, typ, text, choices, ans))
    return "\n".join(out)


def answer_columns():
    """こたえページよう: セクションごとに 1れつ (4れつ × 25こ)"""
    cols = []
    idx = 0
    for sec in ["s1", "s2", "s3", "s4"]:
        title, emoji, color, light = SECTIONS[sec]
        rows = []
        first = idx + 1
        for _ in range(25):
            idx += 1
            _sec, typ, text, choices, ans = Q[idx - 1]
            if typ == MC:
                val = (f'<b style="color:{color}">{CIRCLED[ans]}</b> '
                       f'{choices[ans - 1]}')
            elif typ == OX:
                val = f'<b style="color:{color};font-size:9.5pt">{ans}</b>'
            else:
                val = f'<b>{ans}</b>'
            rows.append(
                f'<div class="ar"><span class="arn">{idx}</span>'
                f'<span class="arv">{val}</span></div>'
            )
        cols.append(
            f'<div class="acol" style="--c:{color};--l:{light}">'
            f'<div class="acol-h">{emoji} {title} <span class="rng">{first}〜{idx}</span></div>'
            + "".join(rows) + "</div>"
        )
    return "\n".join(cols)


def footer(page, total=4):
    return (
        f'<div class="foot"><span class="fl">📣 がんばれ! ドラゴンズ!</span>'
        f'<span class="fp">{page} / {total}</span>'
        f'<span class="fr">⚾ たのしく やきゅうを おぼえよう!</span></div>'
    )


HERO = f"""
<div class="hero">
  <div class="hero-deco d1"></div><div class="hero-deco d2"></div>
  <div class="hero-left">{BASEBALL_SVG}</div>
  <div class="hero-mid">
    <div class="hero-top">⭐ しょうがく 2ねんせいから チャレンジ できるよ! ⭐</div>
    <h1><ruby>中日<rt>ちゅうにち</rt></ruby>ドラゴンズ<br><span class="t2">だいすき クイズ <span class="hundred">100</span>もん!</span></h1>
    <div class="hero-sub">🐨 ぜんぶ とけたら きみも ドラゴンズはかせ! 🔥</div>
  </div>
  <div class="hero-right"><div class="dragon">🐉</div></div>
</div>
<div class="namebar">
  <div class="nb"><span class="nl">なまえ</span><span class="nline"></span></div>
  <div class="nb"><span class="nl">できた かず</span><span class="nline short"></span><span class="nl2">もん / 100もん</span></div>
  <div class="nb star">⭐⭐⭐ めざせ まんてん! ⭐⭐⭐</div>
</div>
"""

MINIHEAD = """
<div class="minihead">
  <span class="mh-ball">⚾</span>
  <span class="mh-title"><ruby>中日<rt>ちゅうにち</rt></ruby>ドラゴンズ だいすき クイズ 100もん!</span>
  <span class="mh-drag">{emoji}</span>
</div>
"""

html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<title>中日ドラゴンズ だいすきクイズ100もん</title>
<style>
  @page {{ size: A4; margin: 0; }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  html, body {{
    -webkit-print-color-adjust: exact; print-color-adjust: exact;
    font-family: 'Rounded Mplus 1c', 'IPAPGothic', sans-serif;
    color: #1b2a4a;
  }}
  .page {{
    width: 210mm; height: 296.6mm; overflow: hidden; position: relative;
    padding: 6mm 8mm 10mm;
    background:
      radial-gradient(circle at 4mm 4mm, #dce9fb 0, #dce9fb 1.1mm, transparent 1.2mm),
      linear-gradient(180deg, #f2f7ff 0%, #eaf2fe 100%);
    background-size: 12mm 12mm, 100% 100%;
    page-break-after: always;
  }}
  .page:last-child {{ page-break-after: auto; }}

  /* ===== ヒーローヘッダー ===== */
  .hero {{
    position: relative; overflow: hidden;
    display: flex; align-items: center; gap: 4mm;
    background: linear-gradient(120deg, #041f66 0%, #0a3ea0 55%, #0d5ad2 100%);
    border-radius: 4mm; padding: 2.8mm 5.5mm;
    border: 0.8mm solid #041f66;
    box-shadow: 0 1mm 0 #b9cdf0;
  }}
  .hero-deco {{ position: absolute; border-radius: 50%; opacity: .14; background: #fff; }}
  .d1 {{ width: 34mm; height: 34mm; right: 24mm; top: -14mm; }}
  .d2 {{ width: 22mm; height: 22mm; left: 30mm; bottom: -12mm; }}
  .bb {{ width: 14.5mm; height: 14.5mm; filter: drop-shadow(0 0.6mm 0 rgba(0,0,0,.25)); }}
  .hero-mid {{ flex: 1; text-align: center; color: #fff; }}
  .hero-top {{ font-size: 7.5pt; font-weight: 700; color: #cfe0ff; letter-spacing: .04em; }}
  h1 {{
    font-family: 'Rounded Mplus 1c Black', 'Rounded Mplus 1c', 'IPAPGothic', sans-serif;
    font-size: 17pt; line-height: 1.26; margin: .8mm 0 .4mm;
    text-shadow: 0 .8mm 0 rgba(0,0,0,.3);
  }}
  h1 ruby rt {{ font-size: 6pt; font-weight: 700; color: #ffd94d; }}
  .t2 {{ font-size: 14pt; }}
  .hundred {{
    display: inline-block; color: #ffd94d; font-size: 19pt;
    transform: rotate(-3deg); text-shadow: 0 .8mm 0 rgba(0,0,0,.35);
  }}
  .hero-sub {{ font-size: 8pt; font-weight: 700; color: #e8f0ff; }}
  .hero-right .dragon {{ font-size: 31pt; filter: drop-shadow(0 .8mm 0 rgba(0,0,0,.25)); }}

  /* ===== なまえ・てんすう ===== */
  .namebar {{ display: flex; gap: 3mm; margin: 1.8mm 0 1.6mm; }}
  .nb {{
    flex: 1; display: flex; align-items: center; gap: 2mm;
    background: #fff; border: 0.45mm solid #0a3ea0; border-radius: 2.5mm;
    padding: 1.1mm 3mm; font-size: 8.5pt; box-shadow: 0 .5mm 0 #c6d6f2;
  }}
  .nl {{
    background: #0a3ea0; color: #fff; font-weight: 800;
    border-radius: 5mm; padding: .3mm 2.6mm; font-size: 7.5pt; white-space: nowrap;
  }}
  .nl2 {{ font-size: 7.5pt; font-weight: 700; color: #55617e; white-space: nowrap; }}
  .nline {{ flex: 1; border-bottom: 0.4mm solid #9db4dd; height: 4.5mm; }}
  .nline.short {{ flex: 0 0 12mm; }}
  .nb.star {{ justify-content: center; color: #b57e00; font-weight: 800; font-size: 8pt;
              background: #fff8e2; border-color: #e8b400; box-shadow: 0 .5mm 0 #ecd9a0; }}

  /* ===== 2ページ目いこうの ミニヘッダー ===== */
  .minihead {{
    display: flex; align-items: center; justify-content: center; gap: 4mm;
    background: linear-gradient(120deg, #041f66, #0d5ad2);
    color: #fff; border-radius: 3mm; padding: 1.8mm 4mm; margin-bottom: 2.2mm;
    border: 0.6mm solid #041f66; box-shadow: 0 .8mm 0 #b9cdf0;
  }}
  .mh-title {{ font-family:'Rounded Mplus 1c ExtraBold','Rounded Mplus 1c',sans-serif; font-size: 12pt; }}
  .mh-title ruby rt {{ font-size: 5pt; color: #ffd94d; }}
  .mh-ball, .mh-drag {{ font-size: 13pt; }}

  /* ===== セクションリボン ===== */
  .sec {{
    break-inside: avoid;
    display: flex; align-items: center; gap: 2mm;
    background: linear-gradient(100deg, var(--c), color-mix(in srgb, var(--c) 72%, #fff));
    color: #fff; font-family: 'Rounded Mplus 1c ExtraBold','Rounded Mplus 1c',sans-serif;
    font-size: 9.5pt; border-radius: 5mm 5mm 5mm 1mm;
    padding: .7mm 3.6mm; margin: 0 0 1.3mm;
    box-shadow: 0 .6mm 0 rgba(10,62,160,.18);
  }}
  .sec .em {{ font-size: 10pt; }}
  .sec .cont {{
    margin-left: auto; font-size: 7pt; background: rgba(255,255,255,.25);
    border-radius: 4mm; padding: .2mm 2.4mm;
  }}

  /* ===== もんだいカード ===== */
  .cols {{ column-count: 2; column-gap: 5mm; column-fill: auto; }}
  .p1 .cols {{ height: 237.5mm; }}
  .p2 .cols {{ height: 267mm; }}
  .p3 .cols {{ height: 129mm; }}
  .q {{
    break-inside: avoid;
    display: flex; align-items: flex-start; gap: 1.5mm;
    background: #fff; border: 0.3mm solid #ccd9ef; border-left: 1.3mm solid var(--c);
    border-radius: 2mm; padding: .75mm 1.5mm .8mm 1.1mm; margin-bottom: 1mm;
    box-shadow: 0 .45mm 0 rgba(10,62,160,.07);
  }}
  .num {{
    flex: 0 0 5.5mm; height: 5.5mm; border-radius: 50%;
    background: var(--c); color: #fff;
    font-family: 'Rounded Mplus 1c ExtraBold','Rounded Mplus 1c',sans-serif;
    font-size: 8.2pt; display: flex; align-items: center; justify-content: center;
    margin-top: .2mm;
  }}
  .qb {{ flex: 1; min-width: 0; }}
  .qt {{ font-size: 8.6pt; font-weight: 700; line-height: 1.2; }}
  .ch {{ font-size: 8pt; line-height: 1.22; margin-top: .4mm; color: #2c3c5e; }}
  .ch .c {{ margin-right: 2.4mm; white-space: nowrap; }}
  .ch .c b {{ margin-right: .4mm; font-size: 8.8pt; }}
  .oxpick {{
    flex: 0 0 auto; align-self: center; display: flex; gap: 1.2mm;
    font-weight: 800; color: #8a97b5; font-size: 10pt;
  }}
  .oxpick span {{
    width: 6mm; height: 6mm; border: 0.35mm dashed #aab8d6; border-radius: 1.6mm;
    display: flex; align-items: center; justify-content: center; background: var(--l);
  }}
  .ansbox {{
    flex: 0 0 auto; align-self: center; display: flex; align-items: center;
    min-width: 16mm; height: 6.2mm;
    border: 0.35mm dashed #7fae92; border-radius: 1.6mm; background: var(--l);
    padding-left: 1.2mm;
  }}
  .al {{ font-size: 5.8pt; font-weight: 800; color: #159a4a; writing-mode: horizontal-tb; }}

  /* ===== まめちしき・おえかき ===== */
  .funbox {{
    break-inside: avoid;
    background: #fff; border: 0.45mm dashed #7fa3e0; border-radius: 2.5mm;
    padding: 1.6mm 2.4mm; margin-bottom: 1.4mm;
  }}
  .fb-title {{
    display: inline-block; background: #ffd94d; color: #6b4c00;
    font-family: 'Rounded Mplus 1c ExtraBold','Rounded Mplus 1c',sans-serif;
    font-size: 7.5pt; border-radius: 4mm; padding: .2mm 2.6mm; margin-bottom: .8mm;
  }}
  .fb-text {{ font-size: 8pt; font-weight: 700; line-height: 1.35; color: #2c3c5e; }}
  .drawbox {{
    break-inside: avoid; position: relative; overflow: hidden;
    background: #fff; border: 0.45mm dashed #7fa3e0; border-radius: 2.5mm;
    padding: 1.6mm 2.4mm; height: 88mm;
  }}
  .db-inner {{
    position: absolute; left: 2.4mm; right: 2.4mm; top: 9mm; bottom: 2.4mm;
    border-radius: 2mm;
    background:
      radial-gradient(circle at 1mm 1mm, #dbe7fa 0, #dbe7fa .7mm, transparent .8mm);
    background-size: 6mm 6mm;
  }}
  .db-emoji {{ position: absolute; right: 4mm; bottom: 3mm; font-size: 17pt; opacity: .55; }}
  .db-emoji2 {{ position: absolute; left: 4mm; bottom: 3mm; font-size: 13pt; opacity: .4; }}

  /* ===== にんていしょう ===== */
  .cert {{
    margin-top: 2.5mm; height: 131mm; position: relative;
    background:
      radial-gradient(circle at 3mm 3mm, #f6e6b8 0, #f6e6b8 1mm, transparent 1.1mm),
      linear-gradient(180deg, #fffdf4, #fdf6df);
    background-size: 11mm 11mm, 100% 100%;
    border: 1mm solid #d9a400; border-radius: 4mm;
    box-shadow: inset 0 0 0 1.2mm #fffdf4, inset 0 0 0 1.6mm #e8c25c;
    padding: 7mm 12mm 5mm; text-align: center;
  }}
  .cert-deco {{ position: absolute; font-size: 15pt; }}
  .cert-deco.tl {{ left: 5mm; top: 4mm; }}
  .cert-deco.tr {{ right: 5mm; top: 4mm; }}
  .cert-deco.bl {{ left: 5mm; bottom: 4mm; }}
  .cert-deco.br {{ right: 5mm; bottom: 4mm; }}
  .cert-stars {{ font-size: 10pt; letter-spacing: .6em; margin-bottom: 1mm; }}
  .cert-title {{
    font-family: 'Rounded Mplus 1c Black','Rounded Mplus 1c',sans-serif;
    font-size: 19pt; color: #b57e00; letter-spacing: .35em; text-indent: .35em;
  }}
  .cert-name {{ margin-top: 4mm; font-size: 12pt; font-weight: 800; }}
  .cert-name .cline {{
    display: inline-block; width: 62mm; border-bottom: 0.5mm solid #b57e00;
    height: 8mm; vertical-align: bottom; margin-right: 2.5mm;
  }}
  .cert-text {{ margin-top: 3.5mm; font-size: 10.5pt; font-weight: 700; line-height: 1.65; color: #2c3c5e; }}
  .cert-text ruby rt {{ font-size: 5.5pt; color: #b57e00; }}
  .cert-score {{ margin-top: 2.5mm; font-size: 11pt; font-weight: 800; color: #2c3c5e; }}
  .cert-score .cbox {{
    display: inline-block; width: 17mm; height: 8.5mm; vertical-align: middle;
    border: 0.5mm dashed #d9a400; border-radius: 2mm; background: #fff; margin: 0 1.5mm;
  }}
  .cert-grant {{ margin-top: 2.5mm; font-size: 9.5pt; font-weight: 700; line-height: 1.6; color: #2c3c5e; }}
  .cert-grant b {{ color: #0a3ea0; font-size: 11.5pt; }}
  .cert-date {{ margin-top: 3mm; font-size: 9pt; font-weight: 700; color: #55617e; }}
  .cert-date .dline {{
    display: inline-block; width: 12mm; border-bottom: 0.4mm solid #9db4dd; height: 5mm;
    vertical-align: bottom;
  }}
  .cert-date .cert-from {{ margin-left: 6mm; font-size: 8pt; color: #8a6d1a; }}

  /* ===== こたえページ ===== */
  .notebar {{
    display: flex; align-items: center; gap: 3mm;
    background: #fff; border: 0.45mm solid #0a3ea0; border-radius: 2.5mm;
    padding: 1.6mm 3.5mm; margin-bottom: 2.4mm; font-size: 8.5pt; font-weight: 700;
    color: #2c3c5e; box-shadow: 0 .5mm 0 #c6d6f2;
  }}
  .notebar .nl {{ flex-shrink: 0; }}
  .agrid {{ display: flex; gap: 2.6mm; }}
  .acol {{
    flex: 1; min-width: 0; background: #fff;
    border: 0.35mm solid #ccd9ef; border-top: 1.7mm solid var(--c);
    border-radius: 2.5mm; padding: 1.7mm 1.5mm;
    box-shadow: 0 .5mm 0 rgba(10,62,160,.08);
  }}
  .acol-h {{
    text-align: center; font-family: 'Rounded Mplus 1c ExtraBold','Rounded Mplus 1c',sans-serif;
    font-size: 8.3pt; color: var(--c); margin-bottom: 1.3mm; white-space: nowrap;
  }}
  .acol-h .rng {{ font-size: 6.5pt; color: #93a1bd; }}
  .ar {{
    display: flex; align-items: center; gap: 1.3mm;
    padding: .5mm 1mm; border-radius: 1.3mm; min-height: 5.9mm;
  }}
  .ar:nth-child(odd) {{ background: var(--l); }}
  .arn {{
    flex: 0 0 5.4mm; text-align: center; background: var(--c); color: #fff;
    font-family: 'Rounded Mplus 1c ExtraBold','Rounded Mplus 1c',sans-serif;
    font-size: 6.8pt; border-radius: 2mm; padding: .15mm 0;
  }}
  .arv {{ font-size: 8.3pt; font-weight: 700; color: #1b2a4a; white-space: nowrap; letter-spacing: -.01em; }}
  .kaisetsu {{
    margin-top: 2.6mm; background: #fff; border: 0.45mm dashed #7fa3e0;
    border-radius: 2.5mm; padding: 1.8mm 3mm;
  }}
  .kai-title {{
    display: inline-block; background: #0a3ea0; color: #fff;
    font-family: 'Rounded Mplus 1c ExtraBold','Rounded Mplus 1c',sans-serif;
    font-size: 8pt; border-radius: 4mm; padding: .25mm 3mm; margin-bottom: 1.2mm;
  }}
  .kai-items {{ display: flex; flex-wrap: wrap; }}
  .kai-items div {{ flex: 0 0 50%; font-size: 7.8pt; font-weight: 700; color: #2c3c5e;
                    line-height: 1.5; padding-right: 3mm; box-sizing: border-box; }}
  .kai-items b {{ color: #0a3ea0; }}
  .rankrow {{ display: flex; gap: 2.6mm; margin-top: 2.6mm; }}
  .rank {{
    flex: 1; text-align: center; background: #fff; border: 0.4mm solid #e8c25c;
    border-radius: 2.5mm; padding: 1.6mm 1mm 1.8mm; box-shadow: 0 .5mm 0 #ecd9a0;
  }}
  .rank .rr {{
    font-family: 'Rounded Mplus 1c ExtraBold','Rounded Mplus 1c',sans-serif;
    font-size: 9.5pt; color: #b57e00;
  }}
  .rank .rs {{ font-size: 8pt; margin: .4mm 0; }}
  .rank .rl {{ font-size: 7.6pt; font-weight: 800; color: #2c3c5e; }}

  /* ===== 100てんバナー ===== */
  .goal {{
    margin-top: 2.2mm; display: flex; align-items: center; justify-content: center; gap: 4mm;
    background: linear-gradient(100deg, #0a3ea0, #0d5ad2 45%, #159a4a);
    color: #fff; border-radius: 3mm; padding: 2mm 4mm;
    font-family: 'Rounded Mplus 1c ExtraBold','Rounded Mplus 1c',sans-serif; font-size: 11pt;
    box-shadow: 0 .8mm 0 #b9cdf0;
  }}
  .goal .small {{ font-size: 7.5pt; font-family: 'Rounded Mplus 1c'; font-weight: 700; color: #dce8ff; }}

  /* ===== フッター ===== */
  .foot {{
    position: absolute; left: 8mm; right: 8mm; bottom: 3.4mm;
    display: flex; align-items: center; justify-content: space-between;
    font-size: 6.8pt; font-weight: 700; color: #6f7fa3;
  }}
  .fp {{
    background: #0a3ea0; color: #fff; border-radius: 4mm; padding: .3mm 3mm;
    font-weight: 800;
  }}
</style>
</head>
<body>

<!-- ============ 1ページめ (Q1-40) ============ -->
<div class="page p1">
  {HERO}
  <div class="cols">
{render_range(1, 40)}
    <div class="funbox">
      <div class="fb-title">🐨 まめちしき</div>
      <div class="fb-text">バンテリンドームには 3まんにん いじょうの ファンが はいれるんだ! すごい ひろさだね!</div>
    </div>
  </div>
  {footer(1)}
</div>

<!-- ============ 2ページめ (Q41-80) ============ -->
<div class="page p2">
  {MINIHEAD.format(emoji="🐉")}
  <div class="cols">
{render_range(41, 80)}
    <div class="funbox">
      <div class="fb-title">🐉 まめちしき</div>
      <div class="fb-text">りゅう(ドラゴン)は つよさと ゆうきの シンボル! だから なごやの チームは 「ドラゴンズ」って いうんだよ。</div>
    </div>
    <div class="drawbox">
      <div class="fb-title">✏️ おえかきコーナー</div>
      <span style="font-size:7.5pt;font-weight:700;color:#55617e;"> じぶんだけの ドアラや りゅうを かいて みよう!</span>
      <div class="db-inner"></div>
      <div class="db-emoji">🐉</div>
      <div class="db-emoji2">⚾</div>
    </div>
  </div>
  {footer(2)}
</div>

<!-- ============ 3ページめ (Q81-100 + にんていしょう) ============ -->
<div class="page p3">
  {MINIHEAD.format(emoji="🐨")}
  <div class="cols">
{render_range(81, 100)}
  </div>
  <div class="cert">
    <div class="cert-deco tl">🐉</div><div class="cert-deco tr">⚾</div>
    <div class="cert-deco bl">📣</div><div class="cert-deco br">🐨</div>
    <div class="cert-stars">⭐⭐⭐⭐⭐</div>
    <div class="cert-title">にんていしょう</div>
    <div class="cert-name"><span class="cline"></span>さん</div>
    <div class="cert-text">あなたは 「<ruby>中日<rt>ちゅうにち</rt></ruby>ドラゴンズ だいすきクイズ」<br>100もんに チャレンジ しました!</div>
    <div class="cert-score">せいかい <span class="cbox"></span> もん</div>
    <div class="cert-grant">これからも ドラゴンズと やきゅうを たのしんでね。<br><b>きみを 『ドラゴンズはかせ』に にんてい します!</b></div>
    <div class="cert-date"><span class="dline"></span> がつ <span class="dline"></span> にち<span class="cert-from">「だいすきクイズ 100もん」より</span></div>
  </div>
  {footer(3)}
</div>

<!-- ============ 4ページめ (こたえの ページ) ============ -->
<div class="page p4">
  {MINIHEAD.format(emoji="🏆")}
  <div class="notebar">
    <span class="nl">🏆 こたえの ページ</span>
    <span>✏️ もんだいを といて から みてね! おうちの ひとと いっしょに まるつけを して、できた かずを 1ページめに かこう!</span>
  </div>
  <div class="agrid">
{answer_columns()}
  </div>
  <div class="kaisetsu">
    <div class="kai-title">💡 ワンポイント</div>
    <div class="kai-items">
      <div><b>14ばん:</b> しんぶんは かんじで チームを かくよ。ドラゴンズは 竜(りゅう)!</div>
      <div><b>18ばん:</b> はるは あたたかい おきなわで れんしゅうを して、シーズンに そなえるんだ。</div>
      <div><b>56ばん:</b> ストライクは 3つで アウト! ボールは 4つで フォアボールだよ。</div>
      <div><b>61ばん:</b> ドラゴンズが できたのは 1936ねん。90ねんくらい まえだよ!</div>
      <div><b>89ばん:</b> 6じの 3じかん あとは 9じ。とけいを みて たしかめて みよう。</div>
      <div><b>97ばん:</b> 2じの 30ぷん まえは 1じ30ぷん。はやめに つくと あんしんだね。</div>
    </div>
  </div>
  <div class="rankrow">
    <div class="rank"><div class="rr">100もん</div><div class="rs">⭐⭐⭐</div><div class="rl">パーフェクト! ドラゴンズはかせ!</div></div>
    <div class="rank"><div class="rr">80〜99もん</div><div class="rs">⭐⭐</div><div class="rl">すごい! はかせまで あとすこし!</div></div>
    <div class="rank"><div class="rr">50〜79もん</div><div class="rs">⭐</div><div class="rl">いいちょうし! そのちょうし!</div></div>
    <div class="rank"><div class="rr">0〜49もん</div><div class="rs">🌱</div><div class="rl">なんども チャレンジ して みよう!</div></div>
  </div>
  <div class="goal">
    <span>⭐ 100もん クリアで きみも ドラゴンズはかせ! ⭐</span>
    <span class="small">まちがえた もんだいは もういちど チャレンジ してみてね 🐉⚾</span>
  </div>
  {footer(4)}
</div>

</body>
</html>
"""

import pathlib
base = pathlib.Path(__file__).parent
out = base / "dragons_quiz.html"
out.write_text(html, encoding="utf-8")
print(f"wrote {out} ({len(Q)} questions)")
