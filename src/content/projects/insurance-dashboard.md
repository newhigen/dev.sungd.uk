---
draft: true
title: "보험 상품 비교 분석"
tagline: "두 보험 상품을 한 기준으로 비교하고 30년 손익을 시뮬레이션."
period: "2026.05.25"
purpose: 돈
status: 완료
tags: ["Insurance", "Dashboard"]
link: "https://sungd.uk/dashboards/insurance.html"
linkLabel: 대시보드
cover: "/p/insurance-dashboard/insurance-dashboard.png"
use:
  - "성별·나이를 같게 맞춰 두 상품을 비교한다"
  - "같이 들 때 더 받는 시너지 항목을 짚는다"
  - "30년 누적 보험료·환급을 시뮬레이션한다"
---
## 문제

두꺼운 보험 제안서는 용어도 낯설고 내용도 많아 막막하다. 두 상품의 공통 혜택이 뭔지, 결정적으로 어디가 다른지가 한눈에 안 보인다. 병원비를 중복으로 받을 수 있는지도 헷갈린다.

## 접근

보장 항목 수나 금액보다, 공통으로 겹치는 것·결정적으로 다른 것·같이 들 때 더 받는 것을 봤다. 화려한 특약보다 실질 가치를 기준에 뒀다.

## 만든 법

복잡한 건 걷어내고 핵심만 나란히 비교한다.

<div class="dg"><div class="dg-node"><b>보험 구조 파악</b></div><div class="dg-arr">→</div><div class="dg-node"><b>내 보험 정리</b></div><div class="dg-arr">→</div><div class="dg-node"><b>A vs B 비교</b></div><div class="dg-arr">→</div><div class="dg-node"><b>30년 시뮬</b></div><div class="dg-arr">→</div><div class="dg-node key"><b>판단</b></div></div>

낯선 용어는 가이드 페이지에 따로 정리해뒀다.

## 기능

### 핵심만 비교
- **공통 베이스** — 성별·나이를 똑같이 맞춰 상품 자체의 실력을 본다
- **시너지 분석** — 두 보험을 같이 들 때 더 받는 항목을 짚는다
- **장기 시뮬레이션** — 30년 보험료와 환급금을 미리 계산

### 한국 보험 구조 반영
- 실손 세대(1~4세대) 차이와 전환 기준
- 갱신형 vs 비갱신형 보험료 추이

## 성과

- 두꺼운 제안서를 한 장 비교 리포트로 압축
- 30년 누적 보험료·환급을 미리 시뮬 — 전엔 감으로 골랐다
- 예시 데이터 기반이라, 실제 결정은 약관·설계사 확인 후가 맞다
