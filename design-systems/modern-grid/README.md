# Modern Grid

**한 줄:** 다크 차콜(#242424) 바탕에 라임 그린(#84BD26) 하나만 강조로 쓰고, 직각 카드와 45° 해치로 위계를 만드는 컨설팅 보고서형 슬라이드 시스템(1280×720).

**이럴 때:** 투자·외부 발표, 핵심 수치 몇 개로 끌고 가는 짧은 덱. 표가 많고 숫자를 꼼꼼히 읽혀야 하는 검토 보고에는 report-light가 낫습니다.

**출처:** white가 다른 세션에서 만든 Design System artifact(https://claude.ai/artifact/TqPfh68Pp2TNH7djDWV8Hy, 2026-10-25 14:46 버전). Etsy "Consulting Presentation Template — modern grid series" 다크 모드 미리보기 10장을 보고 정리한 첫 버전입니다. 색은 이미지에서 뽑은 근사치입니다.

## 특징
- 색: 바탕 `bg` #242424, 면 `surface` #303030 / `surface-2` #3A3A3A, 글자 #FFFFFF / #C8C8C8 / #A3A3A3, 강조 `green-500` #84BD26, 결론 패널 `green-panel` #3A4A1C, 섹션 점·차트용 노랑 #F0AE24, 차트 전용 파랑 #1EA8D8
- 글꼴: 한글 Pretendard(없으면 Noto Sans KR), 숫자 Inter Tight. 위계는 크기보다 굵기 대비(디바이더 제목 700 / 부제 300을 같은 36px)
- 모서리 직각, 그림자 없음. 깊이는 바탕 → 면 명도 단계로만
- 해치는 전망치·현재 단계·검토 대상처럼 "확정과 다른 것" 표시에만
- 기본 흐름: 왼쪽 근거 카드 → 가운데 차트 → 오른쪽 그린 결론 패널
- 대비 주의: 그린 면 위 흰 글자는 2.3:1이라 24px 이상 굵은 숫자에만. 작은 글자는 #1C1C1C

## 파일
- `tokens.json`: 원본 토큰 그대로
- `base.css`: 토큰 CSS 변수 + 원본 `components/bundle.css`
- `source/`: 원본 전체(README, design-system.json, 컴포넌트 13종 README·preview: SlideFrame, SectionDivider, KpiHero, StatList, InsightCard, Callout, BarChart, DataTable, Matrix, ProcessSteps, Progress, Eyebrow, Cover)
- `samples/01-slide-frame.png`, `02-section-divider.png`: 원본 preview를 1280×720으로 렌더(이 환경에서는 Pretendard·Inter Tight 대신 대체 글꼴)

## 이번 덱과의 관계
AI 업무 플랫폼 검토 덱에는 적용하지 않습니다. 작업 마지막 단계에 주요 3장(02 요약, 21 손익, 34 판정)만 별도 샘플로 적용해 비교합니다.

## 쓸 때 확인할 것
- artifact 슬라이드 엔진에 올릴 경우 report-light README의 "artifact 엔진 제약"을 똑같이 지켜야 합니다(grid minmax, span 배경·글꼴, var() 미지원 등). `base.css`는 일반 브라우저용입니다.
- 1280×720 기준이라 1920×1080으로 쓸 때는 크기를 1.5배로 환산합니다.
