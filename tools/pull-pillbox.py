# -*- coding: utf-8 -*-
"""약수첩(pillbox) 산출물을 dev.sungd.uk 로 옮긴다 — pull-sleep-now.py 와 같은 꼴.

원본은 pillbox repo 의 docs/. 글에서 가리킬 것만 골라 public/p/pillbox/ 로 복사하고
주소를 ASCII 로 바꾼다. 그림은 화면에 맞게 줄인다.
"""
import pathlib, shutil, subprocess, sys

SRC = pathlib.Path.home() / "dev/pillbox"
DOCS = SRC / "docs"
OUT = pathlib.Path(__file__).resolve().parent.parent / "public/p/pillbox"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

need = [DOCS / "manual.html", DOCS / "explore/10-아이콘-가족/4-먹-판에-밀림.html", DOCS / "explore/9-2칸으로/1-2x1로-줄이기.html"]
missing = [str(p) for p in need if not p.exists()]
if missing: raise SystemExit("pillbox 체크아웃이 최신이 아니다 — git pull 부터.\n  없음: " + "\n  없음: ".join(missing))
OUT.mkdir(parents=True, exist_ok=True); (OUT / "pages").mkdir(exist_ok=True); (OUT / "img").mkdir(exist_ok=True)

def shrink(src, dst, width):
    dst.parent.mkdir(parents=True, exist_ok=True); shutil.copy2(src, dst)
    subprocess.run(["sips", "--resampleWidth", str(width), str(dst)], check=True, capture_output=True)

def shot(html, dst, size="1200,1500"):
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--window-size={size}",
                    f"--screenshot={dst}", pathlib.Path(html).as_uri()], check=True, capture_output=True)

# ── 1. 아이콘 — 규칙대로 그린 것을 마스크 씌워 176px 로 찍는다
sys.path.insert(0, str(pathlib.Path.home() / ".claude/skills/personal-android-app"))
import xml.etree.ElementTree as ET
import icon as ic
root = ET.parse(SRC / "tools/icon.svg").getroot()
svg = ic.icon_svg(root, 54, 176, ic.PLATE, ic.INK, ic.INK2)
html = OUT / "_icon.html"
html.write_text(f'<html><body style="margin:0;background:transparent">{svg}</body></html>', encoding="utf-8")
shot(html, OUT / "icon.png", "176,176"); html.unlink()

# ── 2. 위젯 — 에뮬레이터로는 좁은 배치가 안 걸려 위젯이 그리는 것과 같은 그림(시안 4번)을 두 배로 찍는다
sys.path.insert(0, str(SRC / "tools"))
import gen_2x1 as g
from draw import theme
dark, _ = g.now_big(theme(True)); light, _ = g.now_big(theme(False))
# 시안은 앱 버튼이 옛 파랑이다 — 지금 규칙(먹 판 · 미색 캡슐)으로 바꿔 찍는다
fix = lambda s: s.replace("#2E6BC4", "#2B2926").replace('rx="4.4" fill="#FFFFFF"', 'rx="4.4" fill="#E6DFD3"')
dark, light = fix(dark), fix(light)
for name, body, bg in (("widget-dark", dark, "#1D1F2E"), ("widget-light", light, "#DDD9E8")):
    h = OUT / f"_{name}.html"
    h.write_text(f'<html><body style="margin:0;background:{bg};display:flex;align-items:center;justify-content:center;width:420px;height:320px">'
                 f'<div style="transform:scale(2.0);transform-origin:center">{body}</div></body></html>', encoding="utf-8")
    shot(h, OUT / f"{name}.png", "420,320"); h.unlink()

# ── 3. 앱 화면 — 설명서용으로 찍은 것을 그대로. 위젯은 폰에서 찍은 것
shutil.copy2(DOCS / "img" / "widget.png", OUT / "widget.png")
for n in ("main_top", "main_tail", "history", "settings_top", "meds", "edit"):
    shrink(DOCS / "img" / f"{n}.png", OUT / f"{n}.png", 620)
# 변천사 — 옛 치수 그대로 다시 그린 위젯. 실제 크기감이 살게 배율은 그대로 둔다
for evo in sorted((DOCS / "img").glob("evo-*.png")):
    shutil.copy2(evo, OUT / evo.name)
# 인공눈물 띠 세 상태 — 「왜 만들었나」
for st in sorted((DOCS / "img").glob("tears-*.png")):
    shutil.copy2(st, OUT / st.name)

# ── 4. 시안 미리보기와 열어볼 페이지
pages = {
    "tiles": "explore/1-위젯-타일/1-타일-무엇으로.html",
    "forms": "explore/2-제형-그림/3-연고-비율과-알약-길이.html",
    "compact": "explore/6-작게-줄이기/1-4x1로-줄이기.html",
    "two-cells": "explore/9-2칸으로/1-2x1로-줄이기.html",
    "icon-family": "explore/10-아이콘-가족/1-네-앱을-한-결로.html",
    "icon-muted": "explore/10-아이콘-가족/3-원색-빼고.html",
    "icon-final": "explore/10-아이콘-가족/4-먹-판에-밀림.html",
}
for slug, rel in pages.items():
    src = DOCS / rel
    if not src.exists(): print("⚠ 없음", rel); continue
    shutil.copy2(src, OUT / "pages" / f"{slug}.html")
    tmp = OUT / f"shot-{slug}.png"; shot(src, tmp)
    subprocess.run(["sips", "--resampleWidth", "700", str(tmp)], check=True, capture_output=True)

# ── 5. 설명서와 그 화면
shutil.copy2(DOCS / "manual.html", OUT / "manual.html")
for png in sorted((DOCS / "img").glob("*.png")): shrink(png, OUT / "img" / png.name, 620)

total = sum(f.stat().st_size for f in OUT.rglob("*") if f.is_file())
print(f"파일 {sum(1 for f in OUT.rglob('*') if f.is_file())}개 · {total/1024/1024:.1f}MB")
