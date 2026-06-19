# TeleMath: A Benchmark for Large Language Models in Telecom Mathematical Problem Solving review

## 1. Metadata

- Title: TeleMath: A Benchmark for Large Language Models in Telecom Mathematical Problem Solving
- Authors: Vincenzo Colle, Mohamed Sana, Nicola Piovesan, Antonio De Domenico, Fadhel Ayed, Merouane Debbah (Huawei Paris Research Center / Università degli Studi di Cassino / Khalifa University)
- Year: 2025
- Venue / Status: arXiv 2506.10674 (정식 venue 미확인 — arXiv 기준)
- Links:
  - Paper: https://arxiv.org/abs/2506.10674
  - Dataset (official): https://huggingface.co/datasets/netop/TeleMath
- Source PDF (local, source-of-record): `paper/2025-telemath.pdf`
- Source Grounding Log:
  - PDF: `paper/2025-telemath.pdf` — 6 pages, sha256 `f11f106f3b21413e8831af70f28e8c227b7258e157d10086ca1077a2c1d1e690`, pypdf/pymupdf 본문 추출 정상(약 29k자). title/authors/abstract/benchmark 구성/metric 직접 확인.
  - arXiv abstract / HF dataset(netop/TeleMath) 확인.
  - TeX source/ar5iv: 미사용.
  - 주의: 정식 venue는 PDF로 미확인 → arXiv로 기록.
- Paper Type: `benchmark` / `domain application (telecom math)` — NFM bridge reference
- Reading Status: `strategically-read`
- Current Priority: `P0` (NFM bridge immediate candidate)

## 2. One-line Summary

TeleMath는 신호처리·네트워크 최적화·성능분석 등 telecom 도메인의 수학적 문제 500 QnA로 구성된 첫 benchmark로, reasoning/non-reasoning LLM을 pass@1과 cons@16(consensus@16, SC majority vote)으로 평가하여 우리 math reasoning mainline을 NFM 도메인으로 잇는 가장 자연스러운 bridge다.

## 3. 핵심 문제 설정

- 문제: 일반 수학 reasoning은 좋아졌지만, **telecom 같은 특화 도메인의 mathematically-intensive task**에서 LLM 능력은 거의 탐구되지 않았다.
- 해법: 10명의 SME가 설계한(초기 50문제 → 확장) **500 QnA** benchmark TeleMath를 구축, signal processing·network optimization·performance analysis 영역을 포괄. reference solution은 Qwen2.5-72B-Instruct로 생성.
- 내 연구와의 연결: TeleMath는 우리 thesis core가 아니라 **domain-aware reasoning strategy selection의 application benchmark**다. 특히 **cons@16(=Self-Consistency majority vote@16)** 을 metric으로 쓰는 점이 우리 TTC/path-pool framing과 직접 닿는다.

## 4. 핵심 방법(벤치마크 구성)

- 데이터: **500 QnA pairs**, telecom math 3대 영역(signal processing / network optimization / performance analysis). 10 SME 설계.
- reference solution 생성: **Qwen2.5-72B-Instruct**.
- 평가 metric: **pass@1** 및 **cons@16**(consensus over 16 samples = majority vote). reasoning vs non-reasoning model 비교(예: DeepSeek-R1-Distill-Llama-70B pass@1 53.21% / cons@16 60.80%).
- selection unit(우리 관점): benchmark 자체는 method가 아님 — `answer / strategy` 평가 대상.

## 5. SLM-Math 관점의 재해석

- TeleMath는 method 경쟁자가 아니라 **NFM bridge application benchmark / evaluation 자원**이다.
- 공통점: 수학 reasoning 평가, **majority-vote(cons@16) 사용** → 우리 SC/TTC framing과 직접 정렬.
- 차이점: domain(telecom)·문제 성격이 GSM8K/MATH word problem과 다름(수식·도메인 지식 결합).
- 연결: math mainline에서 검증한 heterogeneous path-pool/STOP/allocation을 **TeleMath로 domain transfer**하는 bridge stage 1. cons@16이 baseline이므로 우리 path-pool이 같은 budget에서 cons@16을 넘는지 보이기 좋다.

## 6. 우리 연구에 대한 novelty risk

- 낮음(benchmark). 다만 다음을 경계:
  - `TeleMath 결과만으로 NFM 전체 reasoning을 대표한다`고 과장 금지.
  - 첫 top-tier main paper를 **TeleMath 중심으로 이동**하면 안 됨(domain bridge로 한정).
  - cons@16은 이미 SC majority vote이므로 `majority vote/SC를 우리가 도입`처럼 쓰면 안 됨.

## 7. 우리가 빌릴 수 있는 것

- framing: 일반 math reasoning ↔ 도메인 특화 math의 gap, domain reasoning benchmark.
- baseline/metric: **pass@1, cons@16(=SC@16)** — 우리 fixed SC@K·budget-matched 비교와 직접 정렬.
- analysis: reasoning vs non-reasoning model, telecom-specific failure mode, solution token length(=cost proxy).
- terminology: `consensus@k(cons@16)`, `domain-specific mathematical reasoning`.

## 8. 우리가 하면 안 되는 주장

- `TeleMath로 NFM 전체를 대표한다`.
- `domain math benchmark를 우리가 처음 만든다`(TeleMath가 first).
- `cons@16/majority vote가 우리 기여다`.
- main thesis를 telecom benchmark 중심으로 재정의.

## 9. baseline / ablation 반영 아이디어

- bridge stage 1에서 `direct/CoT/PoT/RAG` 최소 path family로 시작, **same budget에서 path-pool vs cons@16** 비교.
- pass@1 vs cons@16(SC) 곡선을 우리 fixed SC@K·heterogeneous pool 곡선과 동일 축에 정렬.
- telecom math failure mode(수식/단위/도메인지식)별로 어떤 path family(특히 PoT/tool)가 유리한지 분석.
- domain transfer 시 strategy-card를 telecom-aware로 확장할지 검토.

## 10. Related Work에 넣을 문장 초안

TeleMath(Colle et al., 2025)는 신호처리·네트워크 최적화·성능분석 등 telecom 도메인의 수학적 문제 500개로 구성된 첫 benchmark로, 도메인 전문가가 설계하고 reasoning/non-reasoning LLM을 pass@1과 cons@16(consensus over 16 samples)로 평가한다. 이는 일반 수학 reasoning에서 특화 도메인으로의 일반화 격차를 드러낸다.

본 연구는 TeleMath를 main thesis의 대상이 아니라 domain-aware reasoning strategy selection의 application benchmark(NFM bridge)로 사용한다. 특히 TeleMath가 채택한 cons@16은 Self-Consistency majority vote와 동일하므로, 우리는 제한된 test-time compute 안에서 heterogeneous reasoning path family를 구성·선택·중단하는 방법이 동일 budget에서 fixed Self-Consistency(cons@k)를 능가하는지를 telecom 도메인에서 검증하는 bridge 실험으로 위치시킨다.

## 11. 현재 우선순위와 다음 액션

- 현재 우선순위: `P0` (NFM bridge immediate candidate)
- 위협도: 낮음 (benchmark; 과장 framing만 경계)
- 구현 결정: NFM bridge stage 1 평가 자원으로 사용. method 재현 대상 아님.
- 지금 할 일:
  - TeleMath를 NFM bridge stage 1로 고정, `direct/CoT/PoT/RAG` 최소 path family + cons@16 baseline 정렬.
  - `TeleMath = NFM 전체 대표`·`main thesis 이동` 금지 wording 유지.
  - cons@16(SC@16)을 우리 fixed SC@K 비교축으로 활용.
- 나중으로 미뤄도 되는 일: TeleTables/TeleLogs(stage 2/3) 확장.
- 한 줄 결론: TeleMath는 우리 math mainline을 telecom으로 잇는 첫 bridge benchmark이며, cons@16 baseline 위에서 heterogeneous path-pool/STOP의 domain transfer를 검증하는 데 쓴다(thesis core 이동은 금지).
