---
draft: true
title: "커리어 레이더"
tagline: "한국 IT 채용 공고(JD)를 직군별 회사×스택 매트릭스 + 통합 직무기술서 + 학습 로드맵으로 정리하는 도구. 회사명은 익명화한 예시."
period: "2026.05"
purpose: 일·커리어
tags: ["Data Analysis", "Career"]
link: "https://resume.sungd.uk/dashboards/career-radar.html"
linkLabel: 대시보드
cover: "/p/career-radar/career-radar.png"
use:
  - "관심 직군의 채용 공고를 수집·구조화한다"
  - "회사×스택 매트릭스로 공통·차별 기술을 본다"
  - "통합 직무기술서와 학습 로드맵을 받는다"
---
## 문제

직군 하나를 준비하려 해도 회사마다 요구가 제각각이다. 공고는 채용 사이트마다 흩어져 있고, 공통으로 요구하는 게 뭔지·이 회사만의 차별점이 뭔지는 결국 손으로 비교한다. 그러다 우선순위가 흐려진다.

## 접근

개별 회사 공고를 하나씩 좇기보다, 한 직군을 여러 회사가 어떻게 요구하는지 겹쳐 봤다. 그러면 늘 공통으로 나오는 기술이 준비 우선순위로 떠오른다. 우대사항보다 공통분모가 더 실질적인 신호라고 봤다. 다만 공고는 수집 시점·표본에 따라 달라지니 절대 기준은 아니다.

## 만든 법

<div class="dg"><div class="dg-node"><b>채용 공고</b></div><div class="dg-arr">→</div><div class="dg-node"><b>본문 추출</b><span>Haiku</span></div><div class="dg-arr">→</div><div class="dg-node"><b>구조화</b><span>Sonnet/Opus</span></div><div class="dg-arr">→</div><div class="dg-node"><b>집계</b><span>deterministic</span></div><div class="dg-arr">→</div><div class="dg-node key"><b>매트릭스·JD·로드맵</b></div></div>

수집은 가벼운 모델로, 구조화는 큰 모델로, 집계는 결정적 스크립트로 나눠 비용과 신뢰도를 맞췄다.

## 기능

- **회사 × 스택 매트릭스** — 공고에 직접 등장한 기술만, 빈칸은 '미명시'로 구분
- **공통 스택** — 수집된 회사 절반 이상이 요구하는 기술 (우선 학습 후보)
- **회사별 차별점** — 그 회사 JD에만 등장한 기술
- **통합 직무기술서 · 로드맵** — 직군별로 묶은 JD와 학습 경로

## 성과

- 흩어진 채용 공고를 직군별 매트릭스 한 장으로 — 전엔 사이트마다 열어 손으로 비교했다
- 공통·차별 기술이 드러나 준비 우선순위가 잡힌다
- 추정 없이 공고 원문 기반 — 다만 수집 시점·범위에 따라 달라지고, 공개용이라 회사명은 익명화했다
