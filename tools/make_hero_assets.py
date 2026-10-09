"""トップページ（2026-10 親しみリニューアル）の写真と映像を作る。

元画像は ChatGPT（Codex の画像生成）で作った PNG。引数でそのフォルダを渡す。
  py -X utf8 tools/make_hero_assets.py <PNGのフォルダ> [--movie-only]
出力: images/f-*.jpg / .webp（ヒーローは映像の中にだけ入るので静止画はポスター1枚）と images/hero-movie.mp4（約15秒・無音ループ）
"""
import sys
from pathlib import Path

import imageio_ffmpeg
import numpy as np
from PIL import Image

SRC = Path(sys.argv[1])
OUT = Path(__file__).resolve().parent.parent / "images"

# 元ファイル名 → サイトでの名前・最大幅
ASSETS = {
    "hero-a": ("f-hero-counter", 1672),   # 映像のポスター（読み込み前・止めたときに見える1枚目）
    "about": ("f-about-handover", 900),
    "team": ("f-team-band", 1916),
    "svc-consult": ("f-svc-consult", 1200),
    "svc-otc": ("f-svc-otc", 1200),
    "svc-zaitaku": ("f-svc-homecare", 1200),
}


def save_photos():
    for src, (name, maxw) in ASSETS.items():
        im = Image.open(SRC / f"{src}.png").convert("RGB")
        if im.width > maxw:
            im = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)
        im.save(OUT / f"{name}.jpg", quality=82, optimize=True, progressive=True)
        if name != "f-hero-counter":  # ポスターは <video poster> で使うので JPEG だけ
            im.save(OUT / f"{name}.webp", quality=78, method=6)
        print(name, im.size)


def make_movie(w=1600, h=896, fps=24, hold=5.0, fade=1.0):
    """3枚を「ゆっくり寄る＋1秒のクロスフェード」でつなぐ。最後は1枚目に戻るので継ぎ目なくループする。"""
    slides = [Image.open(SRC / f"{s}.png").convert("RGB") for s in ("hero-a", "hero-b", "hero-c")]
    n = len(slides)
    total = hold * n
    span = hold + fade

    def frame_of(i, u):
        im = slides[i]
        zoom = 1.0 + 0.07 * (u / span)
        # 元画像を出力比率に合わせて切り出し、ズーム分だけ小さい範囲を取る
        cw, ch = im.width / zoom, im.width / zoom * h / w
        if ch > im.height / zoom:
            ch = im.height / zoom
            cw = ch * w / h
        # 偶数枚目は右へ、奇数枚目は左へ少しずつ流す
        drift = (u / span - 0.5) * (im.width - cw) * 0.5 * (1 if i % 2 == 0 else -1)
        cx = im.width / 2 + drift
        cy = im.height / 2
        box = (cx - cw / 2, cy - ch / 2, cx + cw / 2, cy + ch / 2)
        return np.asarray(im.resize((w, h), Image.BICUBIC, box=box), dtype=np.float32)

    out = OUT / "hero-movie.mp4"
    writer = imageio_ffmpeg.write_frames(
        str(out), (w, h), fps=fps, codec="libx264", quality=None, pix_fmt_out="yuv420p",
        output_params=["-crf", "27", "-preset", "slow", "-movflags", "+faststart", "-an"],
    )
    writer.send(None)
    for k in range(round(total * fps)):
        t = k / fps
        canvas = None
        # 表示中の枚を「後から始まったものが上」に重ねる
        layers = []
        for i in range(n):
            u = (t - hold * i) % total
            if u < span:
                layers.append((u, i))
        layers.sort(key=lambda x: -x[0])  # 古いほうから描く
        for u, i in layers:
            f = frame_of(i, u)
            a = min(1.0, u / fade)
            canvas = f if canvas is None else canvas * (1 - a) + f * a
        writer.send(np.clip(canvas, 0, 255).astype(np.uint8).tobytes())
    writer.close()
    print(out.name, round(out.stat().st_size / 1024), "KB")


if __name__ == "__main__":
    if "--movie-only" not in sys.argv:
        save_photos()
    make_movie()
