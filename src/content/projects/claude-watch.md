---
draft: true
title: "Claude 워치"
tagline: "여러 Claude Code 창 중 답을 기다리는 창을 한눈에 보여주는 모니터."
period: "2026.05.23"
purpose: 개발 도구
tags: ["Claude Code", "CLI"]
github: "https://github.com/newhigen/claude-watch"
use:
  - "여러 세션 상태를 한 줄 요약으로 본다"
  - "입력 필요·Context 풀·작동·완료로 묶여 표시된다"
  - "대기 중인 창부터 골라 손본다"
---
## 문제

Claude Code를 여러 개 띄워 병렬로 굴리다 보면, 어느 창이 내 입력을 기다리는지 일일이 들춰봐야 한다. 알트탭 노가다다. 답을 기다리는 창을 놓치면 그만큼 시간이 빈다.

## 화면

```
claude-watch
4 입력 필요 · 1 Context 풀 · 2 작동 · 2 완료

  입력 필요 · 4
* api-server     타입 에러 2건 더 손볼까요?               Opus 85% 12m
* mobile-app     이 버튼 색상 이대로 갈까요?               Opus 72% 8m
* docs-site      이 두 문단 합칠까요?                      Opus 97% 6m
* infra          마이그레이션 지금 적용할까요?             Opus 64% 3m

  Context 풀 · 1
! data-pipeline  컨텍스트 거의 참 · 압축 후 계속할까요?   Opus 99% 24m

  작동 중 · 2
~ web-crawler    사이트맵 크롤링 중                       Opus 41% 15m
~ ml-training    에폭 7/20 학습 중                      Sonnet 38% 47m

  완료 · 2
· auth-service   토큰 갱신 로직 리팩터링 완료             Opus 88% 18m
· landing-page   히어로 카피 3안 제안 완료                 Opus 76% 9m
```

## 만든 법

모든 세션을 상태로 묶었다. 입력 필요 → Context 풀 → 작동 중 → 완료 순으로, 급한 것이 위로 온다. 모델·context 사용률·경과 시간도 한 줄에 같이 보여준다.

## 기능

- **상태 요약** — 입력 필요·Context 풀·작동 중·완료 세션 수를 한 줄로
- **섹션 그룹핑** — 상태별로 묶어 대기 중인 것부터
- **세션별 정보** — 작업 설명·모델·context 사용률·경과 시간

## 배경

병렬로 여러 에이전트를 돌릴수록 "다음에 손볼 창"을 빠르게 찾는 게 생산성을 좌우한다 — 적어도 내 작업 방식에선 그랬다.

## 성과

- 답을 기다리는 창을 알트탭 없이 한눈에 — 놓쳐서 노는 시간이 준다
- 여러 세션 상태를 한 화면에 모아 다음에 손볼 것을 빠르게 고른다
