# -*- coding: utf-8 -*-
"""peon-ping 목소리 팩을 dev.sungd.uk 로 옮긴다.

팩은 2026-09-02 에 기계에서 지웠고 claude-config git 이력에만 남아 있다(커밋 cdf92fe).
체크아웃 없이 GitHub API 로 그 커밋의 파일을 받아 온다.
"""
import pathlib
import subprocess

REPO = "newhigen-labs/claude-config"
REF = "cdf92fe"
PACK = "common/peon-ping/packs/matilda-excited/sounds"
OUT = pathlib.Path(__file__).resolve().parent.parent / "public/p/peon-ping"
OUT.mkdir(parents=True, exist_ok=True)

for name in ["task_complete_01.mp3", "input_required_01.mp3", "resource_limit_01.mp3"]:
    data = subprocess.run(
        ["gh", "api", f"repos/{REPO}/contents/{PACK}/{name}?ref={REF}",
         "-H", "Accept: application/vnd.github.raw"],
        check=True, capture_output=True).stdout
    (OUT / name.replace("_01", "").replace("_", "-")).write_bytes(data)
    print("✓", name, len(data))
