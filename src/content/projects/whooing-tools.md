---
draft: true
title: "가계부 자동 기입"
tagline: "은행 명세서를 후잉 가계부 형식으로 자동 변환하는 스크립트."
period: "2026.05.18"
purpose: 돈
tags: ["Python", "Finance", "MCP"]
cover: "/p/whooing-tools/whooing-tools.png"
coverLight: "/p/whooing-tools/whooing-tools-light.png"
use:
  - "매핑 규칙(정기·단골·이름)을 한 번 정해둔다"
  - "은행 엑셀을 넣으면 후잉 CSV로 변환된다"
  - "차변·대변까지 맞춰 바로 기입한다"
---
## 문제

복식부기 가계부는 좋지만, 은행 내역을 매번 옮겨 적는 게 일이다. 은행마다 엑셀 형식이 다르고, 같은 카페라도 상황 따라 계정과목을 다르게 두고 싶을 때가 있다. 매달 한 시간 가까이 수작업에 든다.

## 접근

거래처를 그때그때 분류하면 기준이 흔들린다. 매핑 규칙을 한 번 정해두고 변환은 자동에 맡기면, 늘 같은 기준으로 쌓인다.

## 만든 법

데이터를 정제해 후잉 가계부 형식으로 바꾼다.

<div class="dg"><div class="dg-stack"><div class="dg-node">A은행</div><div class="dg-node">B은행</div><div class="dg-node">C카드</div><div class="dg-node">D카드</div></div><div class="dg-arr">→</div><div class="dg-node"><b>파서</b></div><div class="dg-arr">→</div><div class="dg-node"><b>분석</b></div><div class="dg-arr">→</div><div class="dg-node"><b>매핑</b></div><div class="dg-arr">→</div><div class="dg-node key"><b>후잉 CSV</b></div></div>

글자만 바꾸는 게 아니다. 매핑 규칙을 따로 두어, 거래처를 일일이 코드로 짤 필요가 없다. 정규식과 키워드로 분류 체계를 만든다.

## 기능

### 똑똑한 매핑
우선순위에 따라 겹치지 않게 분류한다.
- **정기 지출** — 보험료·구독료·관리비처럼 매달 나가는 것부터
- **자주 가는 곳** — 단골 가맹점은 정해둔 계정으로 바로
- **이름 매칭** — 가맹점 이름 일부만 봐도 찾아낸다

### 후잉 지원
- 계정·항목 관리 (자산~지출)
- 차변·대변 양변 동시 기록

## 성과

- 매달 한 시간 가까이 걸리던 정산이 10분 안쪽으로 — 내 경험상
- 매핑 규칙으로 매번 같은 기준으로 분류된다. 전엔 거래처마다 손봤다
- 은행별로 다른 형식을 한 파서로 흡수
