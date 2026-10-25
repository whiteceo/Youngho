# biz-plan

신사업 기획 자료 저장소입니다. 회사·사업별 폴더 아래에 단계(phase)별 폴더를 둡니다.

```
biz-plan/
├── index.html                          GitHub Pages 첫 화면 (사업·단계별 발표 자료 링크)
├── design-systems/                     발표 자료 디자인 시스템 2종 (report-light, modern-grid)
└── <회사>-<사업>/
    └── phase<번호>-<단계>/
        ├── README.md
        ├── docs/       문서
        ├── deck/       발표 자료 (index.html이 Pages로 바로 열림)
        ├── model/      계산 모델과 실행 스크립트
        └── research/   근거 조사
```

## 사업 목록

| 회사-사업 | 단계 | 발표 자료 | 자료 |
|---|---|---|---|
| 엘캠퍼스 · AI 업무 플랫폼 | Phase 1 사업 타당성 검토 | [deck](elcampus-ai-work-platform/phase1-feasibility/deck/index.html) | [폴더](elcampus-ai-work-platform/phase1-feasibility/) |

새 사업이나 단계를 추가하면 이 표와 루트 `index.html`의 링크도 함께 추가합니다.

## 디자인 시스템

발표 자료를 만들 때 [design-systems/](design-systems/README.md)의 두 시스템 중 하나를 고릅니다. 흰 바탕 보고서형 `report-light`(AI 업무 플랫폼 검토 덱), 어두운 바탕 컨설팅형 `modern-grid`.
