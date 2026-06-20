# TeleTables: A Benchmark for Large Language Models in Telecom Table Interpretation review

## 1. Metadata

- Title: TeleTables: A Benchmark for Large Language Models in Telecom Table Interpretation
- Authors: Anas Ezzakri, Nicola Piovesan, Mohamed Sana, Antonio De Domenico, Fadhel Ayed, Haozhe Zhang (Paris Research Center, Huawei Technologies / Shanghai Research Center, Huawei)
- Year: 2026
- Venue / Status: arXiv 2601.04202 (정식 venue 미표기)
- Links:
  - Paper: https://arxiv.org/abs/2601.04202
  - Dataset (official): https://huggingface.co/datasets/netop/TeleTables (MIT)
  - GitHub / Code (official): 미확인
- Source PDF (local, source-of-record): `paper/2026-teletables.pdf`
- Source Grounding Log:
  - PDF: `paper/2026-teletables.pdf` — 9 pages, sha256 `93602841a039e9cf3334d9edfae66f55381205d06ed2864500c4617d15838c6f`, pypdf/pymupdf 본문 추출 정상(약 42k자). title/authors/abstract/benchmark 구성/metric 직접 확인.
  - HF dataset card(netop/TeleTables): size/schema/metric/license 교차확인.
  - arXiv TeX/ar5iv: 미사용. official code URL 미확인.
- Paper Type: `benchmark` / `domain application (telecom table interpretation)` — NFM bridge stage 2 reference
- Reading Status: `strategically-read`
- Current Priority: `P1` (NFM bridge stage 2)

## 2. One-line Summary

TeleTables는 3GPP 표준 문서의 technical table을 retrieval·interpretation·multi-step reasoning하는 LLM 능력을 500개 human-verified MCQ로 평가하는 telecom table interpretation benchmark로, pass@1·cons@16로 측정하며 우리 path-pool/verifier 아이디어를 structured-table 도메인으로 옮겨보는 NFM bridge stage 2다.

## 3. 핵심 문제 설정

- 문제: telecom 엔지니어링은 3GPP 등 표준 문서의 **표(table)에 담긴 기술 정보 해석**이 핵심인데, LLM이 이 table interpretation/reasoning을 얼마나 하는지 평가가 부족하다.
- 해법: 3GPP spec에서 추출한 real table 위에 **500 human-verified MCQ**(5 choices, 정답 index + explanation + difficulty)를 구축. table retrieval·interpretation·multi-step numeric/structured reasoning 평가.
- 내 연구와의 연결: TeleTables는 thesis core가 아니라 **structured/table reasoning bridge(stage 2)**. 우리 연결은 "structured evidence + reasoning path selection + verifier-aware answer selection" 정도로 제한한다.

## 4. 핵심 방법(벤치마크 구성)

- 데이터: **500 QA pairs**(HF: 371 real tables / 13 3GPP specs), schema = question / choices(5) / answer(index) / explanation / difficulty / table_id·title / document_id·title·url.
- 생성: Qwen3-32B generator + human validation(difficult MCQ 포함).
- 평가 metric: **pass@1**, **cons@16**(consensus@16 = majority voting = Self-Consistency). 예: Qwen3-32B 91.18% pass@1 / 92.60% cons@16, difficult 83.60% pass@1.
- selection unit(우리 관점): MCQ **answer**(+ table evidence). benchmark 자체는 method 아님.

## 5. SLM-Math 관점의 재해석

- TeleTables는 method 경쟁자가 아니라 **NFM bridge stage 2 평가 자원**이다.
- 공통점: 수학/숫자 reasoning + **cons@16(=SC majority vote)** metric → 우리 TTC/SC framing과 직접 정렬.
- 차이점: 입력이 **table(structured evidence) + retrieval**이라 task form이 GSM8K word problem과 다름. table 해석·schema 이해가 추가됨.
- 연결: math mainline에서 검증한 heterogeneous path-pool/STOP/allocation을 **table 도메인으로 transfer**. path family 후보: `direct reasoning`, `CoT`, `table-aware decomposition`, `retrieval/evidence-first`, `verifier-guided selection`. STOP/budget allocation은 **evidence sufficiency + answer agreement** 기준으로 검토 가능.

## 6. 우리 연구에 대한 novelty risk

- 낮음(benchmark). 다만 경계:
  - `table reasoning 자체가 우리 novelty다`로 쓰면 안 됨(TeleTables가 benchmark로 선점).
  - `telecom tables가 NFM 전체를 대표한다`고 과장 금지.
  - `우리 방법이 table reasoning을 일반적으로 해결한다`고 단정 금지.
  - cons@16은 이미 SC majority vote이므로 `SC/majority vote를 우리가 도입`처럼 쓰면 안 됨.

## 7. 우리가 빌릴 수 있는 것

- framing: 일반 reasoning ↔ structured-table 도메인 gap, table retrieval+interpretation+reasoning 3단계.
- baseline/metric: **pass@1, cons@16(=SC@16)** — 우리 fixed SC@K·budget-matched 비교와 직접 정렬.
- analysis: difficulty별 정확도, table 유형별 failure mode, table retrieval vs interpretation 분해.
- terminology: `table interpretation`, `consensus@k(cons@16)`, `evidence(table) grounding`, `difficulty flag`.

## 8. 우리가 하면 안 되는 주장

- `telecom table reasoning을 우리가 처음/일반적으로 해결한다`.
- `TeleTables로 NFM 전체를 대표한다`.
- `domain table benchmark 구축이 우리 main contribution이다`.
- `cons@16/majority vote가 우리 기여다`.
- main thesis를 table reasoning 중심으로 재정의.

## 9. baseline / ablation 반영 아이디어

- bridge stage 2에서 `direct/CoT/table-aware decomposition/retrieval-first/verifier-guided` path family를 **same budget에서 cons@16 대비** 비교.
- evidence-first(table 먼저 찾기) vs direct의 STOP/agreement 분석 → evidence sufficiency 기반 STOP 검토.
- difficulty별로 어떤 path family가 유리한지 분석(우리 state-conditioned allocation의 domain transfer 증거).
- table-specific strategy-card(table prompt / retrieval-table selection)로 strategy-card 확장 검토.

## 10. Related Work에 넣을 문장 초안

TeleTables(Ezzakri et al., 2026)는 3GPP 표준 문서의 기술 표를 retrieval·interpretation·multi-step reasoning하는 LLM 능력을 500개의 human-verified 객관식 문항으로 평가하는 telecom table interpretation benchmark로, pass@1과 cons@16(16-sample consensus)로 측정한다.

본 연구는 telecom table reasoning이나 도메인 benchmark 구축 자체를 새 기여로 두지 않는다. 우리는 TeleTables를 math mainline에서 정립한 state-conditioned reasoning path-pool allocation을 structured-table 도메인으로 확장해 검증하는 bridge benchmark(stage 2)로 사용하며, 특히 cons@16이 Self-Consistency majority vote와 동일하므로 동일 budget에서 heterogeneous path family 구성·선택·중단이 fixed SC를 능가하는지를 telecom table 도메인에서 확인하는 application 실험으로 위치시킨다.

## 11. 현재 우선순위와 다음 액션

- 현재 우선순위: `P1` (NFM bridge stage 2)
- 위협도: 낮음 (benchmark; 과장 framing만 경계)
- NFM bridge role: stage 2 (table/structured-evidence reasoning). thesis core 아님.
- 지금 할 일:
  - TeleTables를 NFM bridge stage 2로 고정, `direct/CoT/table-aware decomposition/retrieval-first/verifier-guided` path family + cons@16 baseline 정렬.
  - `table reasoning/도메인 benchmark 구축이 우리 novelty`·`NFM 전체 대표`·`main thesis 이동` 금지 wording 유지.
  - evidence sufficiency + answer agreement 기반 STOP을 table 도메인에서 검토.
- 나중으로 미뤄도 되는 일: TeleLogs(stage 3) 확장, table retrieval pipeline 재현.
- 한 줄 결론: TeleTables는 우리 path-pool/STOP/verifier 아이디어를 telecom table 도메인으로 옮겨보는 NFM bridge stage 2 benchmark이며, thesis core(math reasoning/TTC allocation)를 table reasoning으로 대체하지 않는다.
