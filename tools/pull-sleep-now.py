# -*- coding: utf-8 -*-
"""sleep-now 산출물을 dev.sungd.uk 로 옮긴다.

원본은 sleep-now repo 의 docs/ 다. 그대로 두면 비공개라 아무도 못 여니, 글에서 가리킬
페이지만 골라 사이트 public/ 안으로 복사하고 주소를 ASCII 로 바꾼다. 그림은 화면에 맞게
줄인다 — 원본은 폰 해상도 그대로라 그냥 올리면 무겁다.
"""
import pathlib
import shutil
import subprocess

SRC = pathlib.Path.home() / "dev/sleep-now/docs"
OUT = pathlib.Path(__file__).resolve().parent.parent / "public/p/sleep-now"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# 체크아웃이 뒤처져 있으면 옛 파일을 도로 얹게 된다. 먼저 확인하고 멈춘다.
need = [SRC / "manual.html", SRC / "phases.html", SRC / "explore/1-이름"]
missing = [str(p) for p in need if not p.exists()]
if missing:
    raise SystemExit("sleep-now 체크아웃이 최신이 아니다 — git pull 부터.\n  없음: "
                     + "\n  없음: ".join(missing))

OUT.mkdir(parents=True, exist_ok=True)
(OUT / "pages").mkdir(exist_ok=True)


def shrink(src: pathlib.Path, dst: pathlib.Path, width: int):
    """가로 폭을 맞춰 줄인다. 원본이 이미 작으면 그대로 복사."""
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    subprocess.run(["sips", "--resampleWidth", str(width), str(dst)],
                   check=True, capture_output=True)


def shot(html: pathlib.Path, dst: pathlib.Path, size="1200,1500"):
    """페이지를 열어 첫 화면을 찍는다 — 렌더가 없는 시안의 미리보기."""
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                    f"--window-size={size}", f"--screenshot={dst}", html.as_uri()],
                   check=True, capture_output=True)


# ── 1. 글에 쓰는 화면 ────────────────────────────────────────────
# 앱 화면은 폰에서 직접 찍은 것(app-light/app-dark)을 쓴다. 여기서는 잠금화면만.
# Now Bar — 원본 캡처에는 배터리 알림까지 들어 있다. 알약 둘레만 오려 쓴다
_nb = OUT / "_nowbar.png"
subprocess.run(["sips", "-c", "277", "857", "--cropOffset", "298", "283",
                str(SRC / "img" / "nowbar.png"), "--out", str(_nb)], check=True, capture_output=True)
shrink(_nb, OUT / "nowbar.png", 900); _nb.unlink()
shutil.copy2(SRC / "img" / "demo.mp4", OUT / "demo.mp4")

# 변천사 — 그때 화면을 그대로 (docs/explore 에 남아 있는 그림)
for slug, src in {
    "hero": SRC / "explore/6-홈-화면/히어로-남은-시간.png",
    "buttons": SRC / "explore/6-홈-화면/버튼-둘.png",
    "timeline": SRC / "explore/6-홈-화면/사이-시간-목표-전.png",
}.items():
    shrink(src, OUT / f"evo-{slug}.png", 320)

# ── 2. 시안 미리보기 ─────────────────────────────────────────────
# 렌더가 남아 있는 것은 그것을 줄이고, 없는 것은 지금 찍는다.
have = {
    "name": SRC / "explore/1-이름/5-오늘-더-쓰면.png",
    "icon-moon": SRC / "explore/2-런처-아이콘/2-열둘.png",
    "icon-final": SRC / "explore/2-런처-아이콘/17-살짝-내림.png",
}
for slug, png in have.items():
    shrink(png, OUT / f"shot-{slug}.png", 700)

make = {
    "statusbar": SRC / "explore/3-상단-바와-나우바/3-스물여덟-개.html",
    "palette": SRC / "explore/4-글꼴과-색/2-어둠과-밝음.html",
    "timeline": SRC / "explore/6-홈-화면/5-타임라인에-다-싣기.html",
    "lower": SRC / "explore/6-홈-화면/4-가로선-넉-줄.html",
}
for slug, html in make.items():
    tmp = OUT / f"shot-{slug}.png"
    shot(html, tmp)
    subprocess.run(["sips", "--resampleWidth", "700", str(tmp)], check=True, capture_output=True)

# ── 3. 열어볼 수 있게 옮기는 페이지 ──────────────────────────────
copy = {
    "pages/name.html": SRC / "explore/1-이름/5-오늘-더-쓰면.html",
    "pages/icon-moon.html": SRC / "explore/2-런처-아이콘/2-열둘.html",
    "pages/icon-final.html": SRC / "explore/2-런처-아이콘/17-살짝-내림.html",
    "pages/statusbar.html": SRC / "explore/3-상단-바와-나우바/3-스물여덟-개.html",
    "pages/palette.html": SRC / "explore/4-글꼴과-색/2-어둠과-밝음.html",
    "pages/lower.html": SRC / "explore/6-홈-화면/4-가로선-넉-줄.html",
    "pages/timeline.html": SRC / "explore/6-홈-화면/5-타임라인에-다-싣기.html",
    "pages/phases.html": SRC / "phases.html",
}
for dst, src in copy.items():
    shutil.copy2(src, OUT / dst)

# 구간 대조판이 쓰는 그림 — 폰 화면이라 절반으로 줄여도 읽힌다
for png in sorted((SRC / "phases").glob("*.png")):
    shrink(png, OUT / "pages/phases" / png.name, 460)

# 설명서와 그 화면
shutil.copy2(SRC / "manual.html", OUT / "manual.html")
for png in sorted((SRC / "img").glob("*.png")):
    shrink(png, OUT / "img" / png.name, 620)
shutil.copy2(SRC / "img" / "demo.mp4", OUT / "img" / "demo.mp4")

total = sum(f.stat().st_size for f in OUT.rglob("*") if f.is_file())
print(f"파일 {sum(1 for f in OUT.rglob('*') if f.is_file())}개 · {total/1024/1024:.1f}MB")
