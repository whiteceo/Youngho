# AI 업무 플랫폼 · Phase 1 사업 타당성 검토

AI 교육·정책·관리를 하나로 묶은 통합 AI 거버넌스 솔루션에 대한 사업 타당성 검토 자료입니다.

| 경로 | 내용 |
|---|---|
| [docs/saas-feasibility.md](docs/saas-feasibility.md) | 검토서 본문 |
| [deck/index.html](deck/index.html) | 발표 자료 (44장, 1920×1080) |
| [deck/calc.html](deck/calc.html) | 손익 계산기 (발표 자료 안에도 들어 있음) |
| [model/](model/) | 손익 모델 `model_v6.py`, 실행 스크립트 `run_v6.py`·`gen_ch5.py`, 계산기 명세 `calculator-spec.md` |
| [research/](research/) | 근거 조사: 시장(`research-market.md`), 조직·인력(`research-org.md`), 결정 기준(`research-criteria.md`) |

## 발표 자료 보기

`deck/index.html`을 브라우저로 엽니다. GitHub Pages가 켜져 있으면 저장소 사이트 주소 뒤에 `elcampus-ai-work-platform/phase1-feasibility/deck/`를 붙여 엽니다. `deck/` 안의 `index.html`, `calc.html`, `fonts/`는 상대 경로로 서로 연결되어 있으니 함께 옮겨야 합니다.

발표 중에는 →, 클릭, 스페이스로 넘깁니다. 일부 장은 단계별로 나타나며, 주소 끝에 `?all`을 붙이면 모든 단계가 한 번에 보입니다.

글꼴(Spoqa Han Sans Neo, Noto Serif KR 부분 집합)은 `deck/fonts/`에 들어 있습니다(OFL 라이선스).

## 손익 모델 실행

```
cd model
python3 run_v6.py     # 시나리오별 손익 출력
python3 gen_ch5.py    # 검토서 5장 표를 ch5_tables.md로 생성
```
