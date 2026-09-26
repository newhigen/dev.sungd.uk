# dev.sungd.uk

직접 만든 앱, 도구, 대시보드와 개발 노트. Astro.

## 실행

```sh
npm install
npm run dev        # localhost:4321
npm run build      # dist/
```

## 어디를 고치나

```
src/content/projects/   프로젝트 한 편 = 파일 하나 (.md, 그림을 직접 배치하면 .mdx)
src/pages/index.astro   목록 — 대표 한 편 + 갈래별
src/pages/[slug].astro  소개 한 편. why.astro, making.astro 가 「왜 만들었나」, 「개발기」
src/content/why/        「왜 만들었나」 본문
src/content/making/     「개발기」 본문
src/content/notes/      개발 노트 (/notes)
src/styles/site.css     토큰과 화면 전부. sungd.uk 랜딩과 같은 계열
public/p/<슬러그>/       그 프로젝트의 그림과, 열어볼 수 있게 옮겨 둔 페이지
```

프로젝트 머리말:

| 키 | 무엇 |
|---|---|
| `title` `tagline` `period` | 목록과 글머리에 그대로 뜬다 |
| `status` | 사용 중, 보류, 완료, 종료. 카드와 글머리에 배지로 선다 |
| `purpose` | 갈래 — 생활, 돈, 일·커리어, 개발 도구, 공부·관심사. 목록 위 칩으로 거른다 |
| `ended` | 보류하거나 종료한 까닭 한 줄 |
| `draft` | 페이지를 안 연 편. 목록에 카드만 흐리게 선다 |
| `tags` `github` `link` `linkLabel` | 글머리 메타 줄 |
| `cover` `coverLight` | 밤과 낮 판. 목록 대표 그림과 og 이미지 |
| `headCover` | 글머리에 그림을 자동으로 세울지. 본문에서 직접 놓으면 `false` |
| `use` | 이럴 때 쓴다 — 서너 줄 |
| `shots` | 그전 모습 (`src` `label` `note`) |
| `feature` | 목록 맨 위에 크게. 하나만 |

## 배포

main 에 머지하면 `.github/workflows/deploy.yml` 이 GitHub Pages 로 올린다. 도메인은 Cloudflare 에서 `dev` → `CNAME newhigen.github.io` (회색 구름).

## ⚠ 경고

- 프로젝트 페이지를 새로 쓰거나 고칠 땐 `personal-project-page` 스킬을 따른다.
- 옛 주소 `resume.sungd.uk/projects/*` 에서 넘기는 장치는 없다. 필요하면 Cloudflare 에서 건다.
