---
draft: true
title: "건강검진 결과지 분석"
tagline: "건강검진 수치의 연도별 추세를 추적하는 대시보드."
period: "2026.05.20"
purpose: 생활
tags: ["Health", "Dashboard"]
link: "https://sungd.uk/dashboards/health.html"
linkLabel: 대시보드
cover: "/p/health-dashboard/health-dashboard.png"
coverLight: "/p/health-dashboard/health-dashboard-light.png"
use:
  - "검진 결과 수치를 연도별로 모은다"
  - "추세 인사이트로 오르내림의 방향을 본다"
  - "정상 범위 대비 내 위치를 가늠한다 (참고용)"
---
## 문제

건강검진 결과표는 보통 그해 것만 보고 서랍에 넣는다. 그런데 진짜 상태는 수치 하나가 아니라 변화하는 흐름에 있다. 혈당이 정상이어도 3년째 오르고 있다면 얘기가 다르다.

## 접근

수치가 정상 범위 안이라도 방향이 더 중요하다고 봤다. 3년째 오르는 혈당은 지금 정상이어도 신호다. 한 시점이 아니라 추세선으로 읽는다.

## 만든 법

검진 PDF에서 수치를 추출해 연도별 추세로 정리한다.

<div class="dg"><div class="dg-node"><b>검진 PDF</b></div><div class="dg-arr">→</div><div class="dg-node"><b>수치 추출</b></div><div class="dg-arr">→</div><div class="dg-node"><b>정상범위 비교</b></div><div class="dg-arr">→</div><div class="dg-node"><b>추세 분석</b></div><div class="dg-arr">→</div><div class="dg-node key"><b>인사이트</b></div></div>

빌드 한 번으로 5년 치 기록과 추세 차트가 최신으로 갱신된다.

## 기능

### 변화를 문장으로
- **추세 인사이트** — "혈당이 점진적으로 오르는 편"처럼 흐름을 짚는다
- **상태 표시** — 좋아지면 초록, 주의가 필요하면 강조 색
- **생활 습관 연결** — 식단·영양제 시점과 수치 변화를 함께 본다

### 대시보드
- 개선 중인지 주의인지 상단 카드에서 바로
- 차트에 정상 범위를 표시해 내 위치를 가늠

## 성과

- 흩어진 검진 PDF를 빌드 한 번으로 5년 추세로 묶는다
- 수치 하나가 아니라 흐름·방향이 보인다 — 전엔 그해 결과만 봤다
- 다만 의학 판단을 대신하진 않는다. 참고용이다
