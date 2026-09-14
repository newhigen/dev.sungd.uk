# -*- coding: utf-8 -*-
"""claude-warmup 시각화를 dev.sungd.uk 로 옮긴다.

repo 는 2026-06-14 에 archive 했고 로컬 체크아웃도 없다. GitHub API 로 받아 온다.
quota-windows.html 은 열어 볼 수 있게 그대로 두고, 글에 쓸 그림은 크롬으로 찍는다.
"""
import pathlib
import subprocess

REPO = "newhigen/claude-warmup"
OUT = pathlib.Path(__file__).resolve().parent.parent / "public/p/claude-warmup"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
OUT.mkdir(parents=True, exist_ok=True)

html = subprocess.run(
    ["gh", "api", f"repos/{REPO}/contents/quota-windows.html", "-H", "Accept: application/vnd.github.raw"],
    check=True, capture_output=True).stdout
page = OUT / "quota-windows.html"
page.write_bytes(html)

shot = OUT / "quota-windows.png"
subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=2",
                "--window-size=1240,1100", f"--screenshot={shot}", page.as_uri()],
               check=True, capture_output=True)
# 제목·설치 줄은 글이 대신 말한다 — 문제·해결 두 판만 오린다
subprocess.run(["sips", "-c", "1520", "2400", "--cropOffset", "532", "40", str(shot)],
               check=True, capture_output=True)
print("✓", page.name, len(html), "·", shot.name)

# 링크 공유 표지 — 원본 repo 에 없는 그림이라 tools/ 의 HTML 에서 찍는다
cover = OUT / "cover.png"
subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--virtual-time-budget=4000",
                "--window-size=1200,630", f"--screenshot={cover}",
                (pathlib.Path(__file__).resolve().parent / "cover-claude-warmup.html").as_uri()],
               check=True, capture_output=True)
print("✓", cover.name)
