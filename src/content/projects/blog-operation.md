---
draft: true
title: "블로그 운영"
tagline: "옵시디언으로 쓰고 아스트로로 배포하는 개인 지식 관리 시스템."
period: "2025.07.01"
purpose: 공부·관심사
tags: ["Astro"]
cover: "/p/blog-operation/blog-operation.png"
coverLight: "/p/blog-operation/blog-operation-light.png"
use:
  - "옵시디언에 글을 쓰고 push한다"
  - "자동 빌드·배포로 생각·기술 두 채널에 나뉜다"
  - "히트맵·목차·대시보드 카드를 필요할 때 붙인다"
---
## 문제

외부 플랫폼에 글을 쓰면 서비스가 닫히거나 디자인을 마음대로 못 바꿔 답답할 때가 있다. 플랫폼에 갇히지 않고 글을 온전히 소유하고 싶었다. 생각 기록과 기술 메모의 성격도 분명히 나누고 싶었다.

## 접근

기록을 외부 플랫폼이 아니라 내 저장소에 두고, 필요한 기능은 직접 짠다.

## 만든 법

나에게 맞는 워크플로우를 만들었다.

<div class="dg"><div class="dg-node"><b>옵시디언</b></div><div class="dg-arr">→</div><div class="dg-node"><b>깃 push</b></div><div class="dg-arr">→</div><div class="dg-node"><b>자동 빌드</b></div><div class="dg-arr">→</div><div class="dg-node key"><b>배포</b></div></div>

옵시디언에서 쓰고 푸시만 하면, 아스트로가 빌드해 배포한다.

## 기능

### 두 갈래 채널
- **생각 기록장** — 읽은 책과 떠오른 생각을 짧은 호흡으로
- **기술 블로그** — 개발 도구와 AI 인사이트를 간결하게

### 직접 짠 도구
- **독서 히트맵** — 언제 얼마나 읽었는지
- **목차 자동 생성** — 긴 글도 길 잃지 않게
- **대시보드 카드** — 분석 대시보드를 블로그에 바로 띄우는 시스템

## 성과

- 옵시디언에서 push만 하면 자동 빌드·배포 — 전엔 수동이었다
- 플랫폼이 닫혀도 글이 남는다. 기록을 온전히 소유
- 히트맵·목차·대시보드 카드를 필요할 때 직접 붙인다
