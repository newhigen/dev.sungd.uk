# -*- coding: utf-8 -*-
"""쿠폰함(coupons) 산출물을 dev.sungd.uk 로 옮긴다 — pull-wallcal.py 와 같은 꼴.

원본은 coupons repo 의 docs/. 글에서 가리킬 것만 골라 public/p/coupons/ 로 복사한다.
시안 페이지는 통째로 옮기고 썸네일을 따로 찍는다 — 개발기에서 격자로 걸고, 누르면 그 페이지로 간다.

⚠ 화면은 **에뮬레이터의 견본 쿠폰**으로 찍는다(coupons 쪽 tools/shots.py). 폰으로 찍으면
   진짜 바코드 번호가 공개 저장소에 그대로 남는다.

체크아웃 말고 다른 곳에서 가져오려면 `COUPONS=<경로> python3 tools/pull-coupons.py`.
"""
import os
import pathlib
import shutil
import subprocess

SRC = pathlib.Path(os.environ.get("COUPONS", pathlib.Path.home() / "dev/coupons"))
DOCS = SRC / "docs"
OUT = pathlib.Path(__file__).resolve().parent.parent / "public/p/coupons"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# 시안 페이지 — 카드를 실제 크기(360dp)로 늘어놓고 고른 화면들. 고른 차례대로.
# (원본 파일, 옮길 이름) — 주소는 아스키로 바꾼다
PAGES = [
    ("1-목록-카드", "cards"),
    ("2-브랜드-색", "brand-color"),
    ("3-공식-로고", "logo"),
]
SHOTS = ["icon", "list", "list-dark", "register", "nearby", "add"]

need = ([DOCS / f"img/{n}.png" for n in SHOTS]
        + [DOCS / f"explore/{n}.html" for n, _ in PAGES])
missing = [str(p) for p in need if not p.exists()]
if missing:
    raise SystemExit("coupons 체크아웃이 최신이 아니다 — 화면부터 다시 찍는다"
                     "(python3 tools/shots.py).\n  없음: " + "\n  없음: ".join(missing))
OUT.mkdir(parents=True, exist_ok=True)
(OUT / "pages").mkdir(exist_ok=True)


def shrink(src, dst, width):
    shutil.copy2(src, dst)
    subprocess.run(["sips", "--resampleWidth", str(width), str(dst)],
                   check=True, capture_output=True)


def shot(html, dst, size="1400,900"):
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                    f"--window-size={size}", f"--screenshot={dst}",
                    pathlib.Path(html).as_uri()], check=True, capture_output=True)


# ── 화면 — 목록은 밤낮 두 판(글머리 그림), 나머지는 한 판씩
shrink(DOCS / "img/list.png", OUT / "list.png", 900)
shrink(DOCS / "img/list-dark.png", OUT / "list-dark.png", 900)
for name in ("register", "nearby", "add"):
    shrink(DOCS / f"img/{name}.png", OUT / f"{name}.png", 600)

# ── 아이콘 — tools/icon.svg 를 규칙대로 그린 것(coupons 쪽에서 뜬다)
shutil.copy2(DOCS / "img/icon.png", OUT / "icon.png")

# ── 시안 페이지 — 통째로 옮기고 맨 윗 화면을 썸네일로.
#    3-공식-로고 는 로고 그림을 함께 쓴다.
shutil.rmtree(OUT / "pages/logo", ignore_errors=True)
shutil.copytree(DOCS / "explore/logo", OUT / "pages/logo")
for name, slug in PAGES:
    dst = OUT / "pages" / f"{slug}.html"
    shutil.copy2(DOCS / f"explore/{name}.html", dst)
    shot(dst, OUT / f"shot-{slug}.png")
    subprocess.run(["sips", "--resampleWidth", "520", str(OUT / f"shot-{slug}.png")],
                   check=True, capture_output=True)

print("coupons →", OUT)
print("  그림", len(list(OUT.glob("*.png"))), "장 · 시안", len(PAGES), "쪽")
