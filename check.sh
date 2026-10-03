#!/usr/bin/env bash
# 깨졌으면 알려 준다. PR 전에 돌린다(전역 훅 pr_check.py 가 `gh pr create` 앞에서 부른다).
#
#   ./check.sh
#
# 1) astro check — 타입과 템플릿. 지금 있는 기존 오류는 실패로 치지 않고 개수만 보여 준다
#    (오류가 0개가 되면 이 스크립트도 자동으로 필수로 바뀐다).
# 2) astro build — 임시 폴더로 빌드해 깨지지 않는지 본다. 기존 dist/ 는 안 건드린다.
#
# ⚠ repo 를 `.claude/worktrees/` 밑 worktree 에서 체크아웃하면, vite(rolldown)가 워크스페이스
#   루트를 메인 체크아웃으로 잘못 잡아 `astro/tsconfigs/strict` 를 못 찾고 깨진다(astro 7.3.5 +
#   vite 8.3.x, 2026-10-03 확인). node_modules 를 심링크로 두면 또 다른 버그(가상 모듈 경로가
#   겹쳐 build 가 깨짐)가 난다. 그래서 소스와 node_modules 를 repo 밖 임시 폴더로 통째로
#   복사해 거기서 돌린다.
set -uo pipefail
cd "$(dirname "$0")"

if [ ! -d node_modules ]; then
  echo "✗ node_modules 가 없다 — npm install 먼저"
  exit 1
fi

work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT
if ! cp -Rc . "$work/" 2>/dev/null && ! cp -R . "$work/"; then
  echo "✗ 임시 폴더로 복사하지 못했다"
  exit 1
fi
rm -rf "$work/.git" "$work/dist" "$work/.astro"

fail=0

check_out=$(cd "$work" && npx astro check 2>&1)
n=$(printf '%s\n' "$check_out" | grep -Eo '^- [0-9]+ error' | grep -Eo '[0-9]+' | head -1)
n=${n:-0}
if [ "$n" = "0" ]; then
  if printf '%s\n' "$check_out" | grep -q "Result ("; then
    echo "✓ astro check"
  else
    echo "✗ astro check (실행 실패)"; printf '%s\n' "$check_out" | tail -10 | sed 's/^/   /'; fail=1
  fi
else
  echo "⚠ astro check (기존 오류 ${n}개 — 고치기 전까진 실패로 안 침)"
fi

if out=$(cd "$work" && npx astro build --outDir "$(mktemp -d)" 2>&1); then
  echo "✓ astro build"
else
  echo "✗ astro build"; printf '%s\n' "$out" | tail -15 | sed 's/^/   /'; fail=1
fi

[ "$fail" = 0 ] && echo "— 멀쩡하다" || echo "— 깨진 게 있다"
exit "$fail"
