# -*- coding: utf-8 -*-
"""한달(wallcal) 산출물을 dev.sungd.uk 로 옮긴다 — pull-pillbox.py 와 같은 꼴.

원본은 wallcal repo 의 docs/. 글에서 가리킬 것만 골라 public/p/wallcal/ 로 복사한다.
시안 페이지는 통째로 옮기고 썸네일을 따로 찍는다 — 개발기에서 격자로 걸고, 누르면 그 페이지로 간다.

⚠ 위젯 캡처는 **에뮬레이터의 데모 달력**으로 찍는다. 폰 홈 화면을 찍으면 실제 일정이
   그대로 공개 저장소에 남는다. 다시 만드는 절차는 wallcal 의 docs/img/README.md 에.

체크아웃 말고 다른 곳(워크트리 등)에서 가져오려면 `WALLCAL=<경로> python3 tools/pull-wallcal.py`.
"""
import os
import pathlib
import shutil
import subprocess

SRC = pathlib.Path(os.environ.get("WALLCAL", pathlib.Path.home() / "dev/wallcal"))
DOCS = SRC / "docs"
OUT = pathlib.Path(__file__).resolve().parent.parent / "public/p/wallcal"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# 시안 페이지 — 갈림길마다 안을 그려 놓고 고른 화면들. 고른 차례대로.
PAGES = [
    ("ideas", "달력 위젯 아이디어", "8월 30일 — 무엇을 만들지부터"),
    ("style", "색과 글꼴", "8월 30일 — 파스텔·조용한 주말색"),
    ("next", "다음 일정 줄", "9월 1일 — 디데이로 갈아탄 자리"),
    ("day", "오른쪽 그날 칸", "9월 2일 — 시간축으로"),
    ("holiday", "공휴일 그리는 법", "9월 3일 — 이어지는 선"),
    ("shape", "위젯 바탕 모양", "9월 3일 — 두 장"),
    ("chip", "일정 막대 스타일", "9월 4일 — 안 바꾸기로"),
    ("allday", "종일과 시각 가르기", "9월 4일 — 점"),
    ("deadline", "마감 그리기", "9월 4일 — 별 단 것을 선으로"),
]
EVO = 6

need = ([DOCS / "img/widget-light.png", DOCS / "img/widget-dark.png",
         DOCS / "img/app.png", DOCS / "img/day.png", DOCS / "img/icon.png",
         DOCS / "legend.html"]
        + [DOCS / f"{n}.html" for n, _, _ in PAGES]
        + [DOCS / f"img/evo-{i}.png" for i in range(1, EVO + 1)])
missing = [str(p) for p in need if not p.exists()]
if missing:
    raise SystemExit("wallcal 체크아웃이 최신이 아니다 — git pull 부터.\n  없음: "
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


# ── 위젯 — 밝을 때·어두울 때. 소개 맨 위 그림은 밝은 판을 쓴다
shrink(DOCS / "img/widget-light.png", OUT / "widget-light.png", 1200)
shrink(DOCS / "img/widget-dark.png", OUT / "widget-dark.png", 1200)
shutil.copy2(OUT / "widget-light.png", OUT / "widget.png")

# ── 화면 — 앱 목록과 그날 시간 축
shrink(DOCS / "img/app.png", OUT / "app.png", 900)
shrink(DOCS / "img/day.png", OUT / "day.png", 300)

# ── 아이콘 — tools/icon.svg 를 규칙대로 그린 것(wallcal 쪽에서 뜬다)
shutil.copy2(DOCS / "img/icon.png", OUT / "icon.png")

# ── 변천사 — tools/gen_evo.py 가 그때 배치로 다시 그린 것
for i in range(1, EVO + 1):
    shrink(DOCS / f"img/evo-{i}.png", OUT / f"evo-{i}.png", 600)

# ── 시안 페이지 — 통째로 옮기고 맨 윗 화면을 썸네일로
for name, _, _ in PAGES:
    dst = OUT / "pages" / f"{name}.html"
    shutil.copy2(DOCS / f"{name}.html", dst)
    shot(dst, OUT / f"shot-{name}.png")
    subprocess.run(["sips", "--resampleWidth", "520", str(OUT / f"shot-{name}.png")],
                   check=True, capture_output=True)

# ── 일정 도감 — 종류별로 어떻게 보이는지 한 장
shutil.copy2(DOCS / "legend.html", OUT / "legend.html")

print("wallcal →", OUT)
print("  그림", len(list(OUT.glob("*.png"))), "장 · 시안", len(PAGES), "쪽")
