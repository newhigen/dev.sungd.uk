# projects.sungd.uk

프로젝트 — 앱 · 도구 · 대시보드 · 분석. [projects.sungd.uk](https://projects.sungd.uk)

전에는 `resume.sungd.uk/projects` 에 있었다. 주소는 이력서인데 라우트로 보면 프로젝트가
더 컸고, 갈래도 화면도 다시 짜야 해서 제 주소로 뗐다.

## 구조

```
src/content/projects/   프로젝트 한 편 = 파일 하나 (.md · 그림을 직접 배치하면 .mdx)
src/pages/index.astro   목록 — 대표 한 편 + 갈래별
src/pages/[slug].astro  글 한 편
src/styles/site.css     토큰과 화면 전부. sungd.uk 랜딩과 같은 계열
public/p/<슬러그>/       그 프로젝트의 그림과, 열어볼 수 있게 옮겨 둔 페이지
```

## 머리말

| 키 | 무엇 |
|---|---|
| `title` `tagline` `period` | 목록과 글머리에 그대로 뜬다 |
| `status` | 사용 중 · 멈춤 · 끝남 · 폐기. 목록이 이 순서로 절을 나눈다 |
| `purpose` | 갈래 — 생활 · 돈 · 일·커리어 · 개발 도구 · 공부·관심사. 목록 위 칩으로 거른다 |
| `ended` | 멈추거나 접은 까닭 한 줄. 카드와 글머리에 선다 |
| `draft` | 페이지를 안 연 편. 목록에 카드만 흐리게 선다 |
| `tags` `github` `link` `linkLabel` | 글머리 메타 줄 |
| `cover` `coverLight` | 밤·낮 판. 목록 대표 그림과 og 이미지 |
| `headCover` | 글머리에 그림을 자동으로 세울지. 본문에서 직접 놓으면 `false` |
| `use` | 이럴 때 쓴다 — 서너 줄 |
| `shots` | 그전 모습 (`src` · `label` · `note`) |
| `feature` | 목록 맨 위에 크게. 하나만 |

## 만들기

```bash
npm install
npm run dev        # localhost:4321
npm run build      # dist/
```

`main` 에 올리면 Actions 가 GitHub Pages 로 올린다. 도메인은 Cloudflare 에서
`projects` → `CNAME newhigen.github.io` (회색 구름).

## 남은 것

- 대시보드 링크는 아직 `resume.sungd.uk/dashboards/…` 를 가리킨다. 옮길지는 나중에
- `resume.sungd.uk/projects/*` 에서 이쪽으로 넘기는 안내가 아직 없다
