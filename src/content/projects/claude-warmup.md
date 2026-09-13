---
draft: true
title: "Claude 워밍업"
tagline: "출근 전 Claude quota 윈도우를 미리 깨워 하루 토큰을 고르게 분산."
period: "2026.05.29"
purpose: 개발 도구
status: 폐기
ended: "공식 Claude Code 루틴(/schedule)이 같은 일을 하게 돼 접었다 (2026.06)"
tags: ["Claude Code", "CLI"]
github: "https://github.com/newhigen/claude-warmup"
link: "https://resume.sungd.uk/dashboards/claude-warmup.html"
linkLabel: 대시보드
cover: "/p/claude-warmup/claude-warmup.png"
use:
  - "워밍업 시각을 예약해둔다"
  - "출근 전 자동으로 quota 윈도우가 시작된다"
  - "윈도우 시각화로 몰림·분산을 확인한다"
---
> 출근 전 quota 윈도우를 미리 깨우려고 만든 CLI. 한 달 만에 공식 기능으로 대체돼 은퇴했다.

## 왜 만들었나

Claude의 5시간 quota 윈도우는 첫 메시지 시각에 고정된다. 출근 후 처음 쓰는 순간 윈도우가 묶여서 오후엔 토큰이 부족했다. 출근 전에 미리 한 번 깨우면 하루에 나눠 받는다. launchd로 새벽 호출을 예약했다. cron은 절전 중 잡을 건너뛰지만 launchd는 깨어나면 실행한다 — 새벽 예약엔 launchd가 맞다.

## 어디서 막혔나

새벽 워밍업이 자주 실패했다. 원인은 macOS DarkWake. 화면이 꺼진 채 깨어난 절전 상태에선 네트워크가 비활성이라 호출이 실패한다. wake-bridge로 우회를 시도했지만 효과 없었다. 우회를 접고 "맥이 깨어 있어야 함"을 한계로 문서화했다.

## 어떻게 끝났나

이후 Claude Code에 Routine 기능이 생겼다. 정해진 시각 실행을 공식 지원한다. launchd로 하던 일과 같다. 직접 만든 스케줄러는 공식 기능으로 대체됐다. 워밍업 잡 제거, 저장소 archive 처리.

## 남는 것

만들면서 문제를 정의하고 직접 해결해봤다. 더 단순하고 나은 해결책(공식 Routine)이 나오자 복잡한 기존 방식은 과감히 버렸다. 빈틈을 메우는 도구는 공식 기능이 그 빈틈을 채우면 사라진다.
