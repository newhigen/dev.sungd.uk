---
draft: true
title: "Claude 대시보드 패치"
tagline: "claude-dashboard status line을 개인 취향으로 커스터마이즈하는 패치."
period: "2026.05.25"
purpose: 개발 도구
tags: ["Claude Code", "Customize"]
github: "https://github.com/newhigen/claude-dashboard-patches"
use:
  - "status line 표시 항목·포맷을 개인화한다"
  - "업데이트 후 스크립트로 패치를 복원한다"
---
## 문제

claude-dashboard의 status line을 취향대로 손봐도, 플러그인이 업데이트되면 캐시가 덮어쓴다. 매번 다시 손보긴 번거롭다.

## 화면

정상 페이스 — 모든 윈도우 여유:

```
~/dev/api-server (main* ↑3)   +1 -1 │ Context: ███░░░ 43%
Opus(High) │ 5h 0.7x ░░░░░░ 5% → 2:30 AM ✓   7d 1.0x █░░░░░ 15% → 5/22 FRI ✓
```

5h 고갈 경고 — reset 전 100% 도달 예상:

```
~/dev/api-server (main* ↑3)   +1 -1 │ Context: ███████ 87%
Opus(High) │ 5h 1.4x ███████ 87% → 2:30 PM ⚠ (reset 5:00 PM)   7d 1.0x █░░░░░ 15% → 5/22 FRI ✓
```

## 만든 법

변경을 별도 디렉토리에 보관하고, 업데이트 후 재적용 스크립트로 다시 입힌다. 업데이트와 개인화를 양립시키는 방법이다.

## 기능

- **status line 커스터마이즈** — 표시 항목·포맷 개인화
- **재적용 스크립트** — 플러그인 업데이트 후 패치 자동 복원

## 배경

자주 업데이트되는 플러그인을 커스터마이즈하면 매번 덮어쓰인다. 패치를 분리해두면 업데이트와 개인화를 양립시킬 수 있다.

## 성과

- 플러그인 업데이트 후 패치가 자동 복원된다 — 전엔 매번 다시 손봤다
- 잦은 업데이트와 개인화를 양립시킨다
