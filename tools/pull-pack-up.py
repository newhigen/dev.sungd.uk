# -*- coding: utf-8 -*-
"""준비물(pack-up) 산출물을 dev.sungd.uk 로 옮긴다 — pull-wallcal.py 와 같은 꼴.

원본은 pack-up repo 의 docs/. 글에서 가리킬 것만 골라 public/p/pack-up/ 으로 복사한다.
시안 페이지는 통째로 옮기고 썸네일을 따로 찍는다 — 개발기에서 격자로 걸고, 누르면 그 페이지로 간다.

⚠ 위젯 캡처는 **위젯만 잘라** 온다. 홈 화면을 통째로 찍으면 옆에 붙은 달력 위젯의 실제
   일정(이름·약속)이 그대로 공개 저장소에 남는다. 자르는 자리는 pack-up 의 dev-crop.py 로 잡는다.

체크아웃 말고 다른 곳(워크트리 등)에서 가져오려면 `PACKUP=<경로> python3 tools/pull-pack-up.py`.
"""
import os
import pathlib
import shutil
import subprocess
import sys

SRC = pathlib.Path(os.environ.get("PACKUP", pathlib.Path.home() / "dev/pack-up"))
DOCS = SRC / "docs"
OUT = pathlib.Path(__file__).resolve().parent.parent / "public/p/pack-up"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# 시안 페이지 — 갈림길마다 안을 그려 놓고 고른 화면들. 고른 차례대로.
PAGES = [
    ("widget-ideas", "위젯 한 판 그리기", "9월 1일 — 네 안 중 겹쳐 세우기"),
    ("widget-1row", "한 줄 위젯 배치", "9월 1일 — 왼쪽·오른쪽에서 위·아래로"),
    ("widget-polish", "한 줄 위젯 다듬기", "9월 2일 — 눈금과 이름표"),
    ("widget-dust", "위젯에 미세먼지", "9월 2일 — 그림 «안» 에 조각으로"),
    ("guide-bands", "기준 화면", "9월 3일 — 구간 띠에 준비물을 얹어"),
]

need = ([DOCS / f"{n}.png" for n in ("main", "week", "guide", "widget")]
        + [DOCS / f"{n}.html" for n, _, _ in PAGES]
        + [SRC / "tools/icon.svg"])
missing = [str(p) for p in need if not p.exists()]
if missing:
    raise SystemExit("pack-up 체크아웃이 최신이 아니다 — git pull 부터.\n  없음: "
                     + "\n  없음: ".join(missing))
OUT.mkdir(parents=True, exist_ok=True)
(OUT / "pages").mkdir(exist_ok=True)


def shrink(src, dst, width):
    shutil.copy2(src, dst)
    subprocess.run(["sips", "--resampleWidth", str(width), str(dst)],
                   check=True, capture_output=True)


def shot(html, dst, size="1200,900"):
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                    f"--window-size={size}", f"--screenshot={dst}",
                    pathlib.Path(html).as_uri()], check=True, capture_output=True)


# ── 아이콘 — 규칙대로 그린 것을 176px 로 찍는다
sys.path.insert(0, str(pathlib.Path.home() / ".claude/skills/personal-android-app"))
import xml.etree.ElementTree as ET
import icon as ic

svg = ic.icon_svg(ET.parse(SRC / "tools/icon.svg").getroot(), 54, 176, ic.PLATE, ic.INK, ic.INK2)
html = OUT / "_icon.html"
html.write_text(f'<html><body style="margin:0;background:transparent">{svg}</body></html>',
                encoding="utf-8")
shot(html, OUT / "icon.png", "176,176")
html.unlink()

# ── 폰 화면 — 목록과 하루 차트 / 이번 주 / 기준
shrink(DOCS / "main.png", OUT / "main.png", 900)
shrink(DOCS / "week.png", OUT / "week.png", 900)
shrink(DOCS / "guide.png", OUT / "guide.png", 900)

# ── 위젯 — 홈 화면에서 위젯만 잘라 온 것
shrink(DOCS / "widget.png", OUT / "widget.png", 1100)

# ── 시안 페이지 — 통째로 옮기고 맨 윗 화면을 썸네일로
for name, _, _ in PAGES:
    dst = OUT / "pages" / f"{name}.html"
    shutil.copy2(DOCS / f"{name}.html", dst)
    shot(dst, OUT / f"shot-{name}.png")
    subprocess.run(["sips", "--resampleWidth", "520", str(OUT / f"shot-{name}.png")],
                   check=True, capture_output=True)

print("pack-up →", OUT)
print("  그림", len(list(OUT.glob("*.png"))), "장 · 시안", len(PAGES), "쪽")
