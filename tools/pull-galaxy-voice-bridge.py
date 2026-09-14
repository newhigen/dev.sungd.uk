# -*- coding: utf-8 -*-
"""갤럭시 음성 브리지(galaxy-voice-bridge) 시안을 dev.sungd.uk 로 옮긴다 — pull-pack-up.py 와 같은 꼴.

원본 repo 는 private 이고 스크린샷이 없다. design/ 의 시안 HTML 여섯 쪽을 통째로 옮기고,
크롬으로 찍어 개발기 격자 썸네일을 만든다. 소개의 캡슐 상태 넷은 캡처가 아니라
src/components/gvb/Capsules.astro 가 main.swift 값으로 다시 그린다.

⚠ recordings/ 는 절대 가져오지 않는다 — 실제 목소리다. 글에 쓰는 건 개수와 길이뿐.

체크아웃 말고 다른 곳에서 가져오려면 `GVB=<경로> python3 tools/pull-galaxy-voice-bridge.py`.
"""
import os
import pathlib
import shutil
import subprocess

SRC = pathlib.Path(os.environ.get("GVB", pathlib.Path.home() / "dev/galaxy-voice-bridge"))
DESIGN = SRC / "design"
OUT = pathlib.Path(__file__).resolve().parent.parent / "public/p/galaxy-voice-bridge"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# 시안 페이지 — 고른 차례대로
PAGES = ["ui-candidates", "bright-capsule-variants", "capsule-current-comparison",
         "special-capsule-showcase", "radical-voice", "subtle-capsules"]

missing = [str(DESIGN / f"{n}.html") for n in PAGES if not (DESIGN / f"{n}.html").exists()]
if missing:
    raise SystemExit("galaxy-voice-bridge 체크아웃이 최신이 아니다 — git pull 부터.\n  없음: "
                     + "\n  없음: ".join(missing))
(OUT / "pages").mkdir(parents=True, exist_ok=True)


def shot(html, dst, size, scale=1):
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                    "--virtual-time-budget=3000", f"--force-device-scale-factor={scale}",
                    f"--window-size={size}", f"--screenshot={dst}", pathlib.Path(html).as_uri()],
                   check=True, capture_output=True)


for name in PAGES:
    dst = OUT / "pages" / f"{name}.html"
    shutil.copy2(DESIGN / f"{name}.html", dst)
    thumb = OUT / f"shot-{name}.png"
    shot(dst, thumb, "1200,900")
    subprocess.run(["sips", "--resampleWidth", "520", str(thumb)], check=True, capture_output=True)

print("galaxy-voice-bridge →", OUT)
print("  썸네일", len(PAGES), "장")
