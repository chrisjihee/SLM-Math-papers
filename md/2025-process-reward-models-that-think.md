# Process Reward Models That Think review

## 1. Metadata

- Title: Process Reward Models That Think
- Authors: Muhammad Khalifa, Rishabh Agarwal, Lajanugen Logeswaran, Jaekyeom Kim, Hao Peng, Moontae Lee, Honglak Lee, Lu Wang
- Year: 2025
- Venue / Status: PDF 기준 preprint, GitHub metadata 기준 `TMLR / unverified`
- Link: https://arxiv.org/abs/2504.16828
- Code / Data:
  - GitHub: https://github.com/mukhal/thinkprm
  - 코드, 데이터, 모델 공개
- Benchmarks: `PRM800K`, `ProcessBench`, `MATH-500`, `AIME '24`, `GPQA-Diamond`, `LiveCodeBench`
- Reading Status: `strategically-read`
- Current Priority: `P1`

## 2. One-line Summary

THINKPRM은 long verification CoT를 생성하는 **generative PRM**을 학습해, step-level supervision을 많이 쓰지 않고도 best-of-N, verifier-guided search, compute-matched self-consistency에서 강한 test-time scaling 성능을 보인 논문이다.

## 3. 핵심 문제 설정

- 수학 추론에서 좋은 verifier, 특히 PRM이 중요하지만 discriminative PRM은 step-level process label을 대량으로 요구한다.
- LLM-as-a-Judge는 prompt sensitivity, invalid label, looping, overthinking 문제가 있다.
- THINKPRM은 `step-level label을 많이 모으지 않고도 verifier를 만들 수 있는가`를 묻는다.
- 핵심적으로 이 논문은 generator compute가 아니라 **verifier compute**까지 TTC에 포함해서 봐야 한다는 점을 보여준다.
- 내 연구와의 연결은 매우 직접적이다.
  - 내 연구는 reasoning path를 고르는 문제이지만
  - THINKPRM은 그 뒤에 붙는 verifier가 “생각하는” 방법을 보여준다.

## 4. 핵심 방법

- THINKPRM은 discriminative PRM이 아니라 **generative PRM**이다.
- verification reasoning path는 solution path가 아니라 **verification path**다.
- 학습 데이터는 QwQ-32B-Preview가 생성한 verification CoT를 rejection filtering해서 구성한다.
- PRM800K의 step labels와 맞는 verification chain만 남기고, malformed 또는 overthinking chain은 제거한다.
- test-time에는 다음을 사용한다.
  - `best-of-N`
  - verifier-guided beam search
  - parallel verifier scaling
  - sequential verifier scaling
- PRM score는 long verification CoT의 마지막 판단 또는 step-level 판단으로 사용된다.
- `LLM-as-a-Judge` 대비 invalid output과 looping 문제가 적다는 점을 강조한다.

## 5. SLM-Math 관점의 재해석

- 이 논문은 verifier 자체를 test-time compute allocation의 대상으로 확장한다.
- 공통점:
  - 여러 candidate solution을 검증하고 고른다.
  - majority voting보다 verifier selection이 강할 수 있음을 보인다.
  - compute-matched 비교를 중요하게 본다.
- 차이점:
  - 이 논문은 verifier가 이미 주어진 candidate를 얼마나 잘 판단할지에 초점이 있다.
  - 내 연구는 candidate를 만들기 전에 어떤 path family를 샘플링할지, 그리고 generation과 verification 중 어디에 budget을 쓸지 정해야 한다.
- 안전한 한 문장 차별화:
  - THINKPRM은 verifier compute scaling의 대표 사례이고, 내 연구는 **generation compute와 verification compute를 함께 고려한 path-family / strategy-level allocation**을 다뤄야 한다.

## 6. 우리 연구에 대한 novelty risk

- `verifier 기반 candidate selection`은 이미 강한 선행축이다.
- `best-of-N + verifier`도 새롭지 않다.
- `TTC를 generation뿐 아니라 verification에도 쓴다`는 claim도 이미 있다.
- `small verifier + strong scaling`도 이미 확인되었다.
- `LLM-as-a-Judge보다 prompt-aware verifier가 낫다`는 방향도 새롭지 않다.
- 특히 위험한 claim:
  - `verifier로 candidate reasoning path를 고르는 것이 새롭다`
  - `SC보다 검증 기반 선택이 낫다는 것을 우리가 처음 보인다`
  - `verifier compute allocation이 본 논문의 novelty다`
- 안전한 방향:
  - verifier 자체가 아니라 **candidate pool construction / path-family diversity / stopping policy**

## 7. 우리가 빌릴 수 있는 것

- problem framing:
  - verifier도 reasoning process가 될 수 있다
  - TTC는 generation budget + verification budget으로 나뉜다
  - 검증이 강해질수록 generation-only scaling의 한계가 드러난다
- baseline:
  - Majority voting / Self-Consistency
  - Best-of-N + verifier scoring
  - Weighted majority voting
  - LLM-as-a-Judge
  - DiscPRM
  - Math-Shepherd-PRM
  - Guided beam search with PRM
- metric:
  - Accuracy vs number of samples
  - Compute-matched accuracy vs FLOPs
  - Verification F1
  - Invalid judgment ratio
  - Average budget used
  - Parallel vs sequential verifier scaling
- ablation:
  - long verification CoT vs short verification CoT
  - process-based filtering vs outcome-based filtering
  - verifier prompt sensitivity
  - generator-only vs verifier-added compute
  - easy vs hard problem bins
- figure/table idea:
  - budget-accuracy curve
  - compute-matched curve
  - generation vs verification budget allocation plot
  - invalid output / parsing error table

## 8. 우리가 하면 안 되는 주장

- `verifier를 붙여 candidate를 고르는 것이 새롭다`고 쓰면 안 된다.
- `Self-Consistency보다 검증 기반 선택이 낫다`를 본 연구의 main novelty로 쓰면 안 된다.
- `TTC는 주로 solution generation의 문제`라고 좁게 쓰면 안 된다.
- `LLM-as-a-Judge면 충분하다`고 쓰면 안 된다.
- `step-level supervision이 없으면 verifier를 만들 수 없다`고 쓰면 안 된다.
- `우리 reranker가 solution verifier와 같은 종류다`라고 쓰면 안 된다.
- `verifier compute scaling 자체가 우리 contribution`이라고 쓰면 안 된다.

## 9. baseline / ablation 반영 아이디어

- SC, Best-of-N, verifier selection, hybrid를 모두 비교한다.
- verifier compute를 allocation variable로 넣는다.
- generator-only vs verifier-added compute를 같은 FLOPs로 맞춘다.
- `@4`, `@8`, `@K` verifier scaling을 별도로 본다.
- verifier prompt sensitivity와 invalid output ratio를 로그로 남긴다.
- route-card / strategy-card는 solution verifier가 아니라 acquisition policy로 유지한다.
- `generation budget`과 `verification budget`을 분리해서 보고한다.

## 10. Related Work에 넣을 문장 초안

**Process Reward Models That Think**는 discriminative PRM이 요구하는 대량의 step-level supervision을 줄이기 위해, long verification CoT를 생성하는 **generative PRM**인 THINKPRM을 제안하였다. THINKPRM은 소량의 process labels만으로도 ProcessBench, MATH-500, AIME ’24에서 강한 verification 성능을 보였고, best-of-N selection과 verifier-guided search에서 verifier compute를 parallel 또는 sequential하게 확장할 수 있음을 보였다. 특히 LLM-as-a-Judge보다 invalid label과 looping 문제가 적고, compute-matched 비교에서 verifier가 reasoning 성능을 실질적으로 끌어올릴 수 있음을 보여 준다.

그러나 이 연구는 주어진 candidate solution을 검증하는 verifier 중심이다. 반면 본 연구는 제한된 test-time compute 안에서 어떤 reasoning path family를 생성할지, generation compute와 verification compute를 어떻게 나눌지, 언제 stop할지까지 포함하는 **state-conditioned reasoning path pool construction** 문제를 다룬다. 따라서 THINKPRM은 강력한 verifier baseline이자, generation-only self-consistency를 넘어 verification-aware TTC allocation을 고려해야 한다는 근거로 배치된다.

## 11. 현재 우선순위와 다음 액션

- 현재 우선순위: `P1`
- 위협도: 높음
- 지금 당장 해야 할 일:
  - generative verifier와 discriminative PRM의 차이를 문서에서 분명히 할 것
  - TTC를 generation budget과 verification budget으로 나눠 표현할 것
  - Best-of-N + verifier selection을 baseline universe에 포함할 것
  - LLM-as-a-Judge를 verifier baseline으로만 쓰지 말고 invalid output / looping diagnostics를 같이 볼 것
- 나중으로 미뤄도 되는 일:
  - full verifier-guided beam search 재현
  - long verification CoT 재학습
  - OOD code / science benchmark full replication
- 한 문장 결론:
  - THINKPRM은 verifier 자체가 생각할 수 있음을 보여 주는 강한 baseline이며, 내 연구는 그보다 앞단의 **어떤 reasoning path를 생성하고, generation과 verification에 budget을 어떻게 배분할지**를 다뤄야 한다.
