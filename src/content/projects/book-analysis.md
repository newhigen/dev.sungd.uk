---
draft: true
title: "독서 성향 분석"
tagline: "읽은 책 데이터로 분야·저자 분포와 시기별 흐름을 정리하는 리포트."
period: "2026.05.30"
purpose: 공부·관심사
status: 끝남
tags: ["Data Analysis", "Python"]
link: "https://resume.sungd.uk/dashboards/book-analysis.html"
linkLabel: 대시보드
cover: "/p/book-analysis/book-analysis.png"
use:
  - "책 목록(제목·분야·연도)을 넣는다"
  - "분야 분포·시기별 흐름으로 취향을 살핀다"
  - "성향 요약을 하나의 관점으로 참고한다"
shots:
  - src: "/p/book-analysis/book-before.png"
    label: "토스 스타일"
    note: "친근체였지만 내 색이 아니었다 — polished로"
---
읽은 책 목록(제목·분야·연월)으로 분야 분포와 시기별 흐름을 집계한다.

**뭐가 보이나**
- 분야가 어디로 쏠리는지 · 관심이 해마다 어디로 옮겨갔는지
- 저자·Mood·Pace로 본 취향의 결 · 독서 가속 곡선
- 연도별 회고(Year in Review) · 다음에 읽을 책 추천

<div class="dg"><div class="dg-node"><b>책 목록</b><span>제목·연월</span></div><div class="dg-arr">→</div><div class="dg-node"><b>메타 보강</b><span>분야·Mood·Pace</span></div><div class="dg-arr">→</div><div class="dg-node"><b>집계·시각화</b><span>Python</span></div><div class="dg-arr">→</div><div class="dg-node key"><b>리포트</b><span>4탭</span></div></div>

전엔 "많이 읽었다" 정도만 알았다. 데이터만 갱신하면 리포트는 다시 그려진다.

<details>
<summary>왜 이렇게 봤나 — 배경·관점</summary>

목록은 제목의 나열일 뿐, 분야 쏠림·관심 이동·취향의 실제는 거기서 안 드러난다.

권수보다 어떤 분야로 옮겨갔는지가 취향을 더 잘 보여준다고 봤다. 해석엔 주관이 섞이니 결론이 아니라 참고로 본다.

입력은 제목·연월만으로 시작해 분야·Mood·Pace 같은 메타를 읽는 대로 채우고(입력 진행률로 추적), 집계는 결정적 스크립트라 데이터만 갱신하면 리포트가 그대로 다시 그려진다.
</details>
