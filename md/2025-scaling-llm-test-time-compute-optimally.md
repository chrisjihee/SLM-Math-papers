# Scaling LLM Test-Time Compute Optimally Can Be More Effective Than Scaling Parameters for Reasoning review

## 1. Metadata

- Title: Scaling LLM Test-Time Compute Optimally Can Be More Effective Than Scaling Parameters for Reasoning
- Authors: Charlie Snell, Jaehoon Lee, Kelvin Xu, Aviral Kumar
- Year: 2025
- Venue / Status: ICLR 2025 published conference paper
- Link: https://openreview.net/forum?id=4FWAwZtd2n
- Code / Data:
  - Code: PDF 기준 명시적 official repository는 확인되지 않음
  - Data / Benchmark: `MATH`
  - Model family: `PaLM 2-S*`, appendix 일부 `PaLM 2-S`, `PaLM 2-M`
- Reading Status: `strategically-read`
- Current Priority: `P0`

## 2. One-line Summary

이 논문은 수학 추론에서 test-time compute를 무작정 늘리는 대신, 문제 난이도에 따라 `parallel sampling`, `sequential revision`, `PRM-based search` 중 compute-optimal strategy를 고르면 더 적은 계산량으로 더 높은 효율을 얻을 수 있음을 보인다.

## 3. 핵심 문제 설정

- 고정된 inference budget이 있을 때, 그 계산량을 어떤 test-time strategy에 써야 reasoning 성능이 가장 잘 오르는지가 핵심 문제다.
- 기존 TTC 연구는 어떤 논문은 self-correction이나 iterative prompting이 잘 된다고 하고, 어떤 논문은 잘 안 된다고 하며 결과가 엇갈렸다.
- 이 논문은 그 불일치를 `방법이 원래 좋은가/나쁜가`가 아니라, **문제 난이도와 base model의 solvability에 따라 좋은 TTC 사용 방식이 다르다**는 문제로 재해석한다.
- 따라서 질문은 단순히 `sample을 더 뽑을까 말까`가 아니라 다음으로 바뀐다.
  - `parallel sampling`이 좋은가
  - `sequential revision`이 좋은가
  - `PRM beam search`나 `lookahead search`가 좋은가
  - 같은 budget에서 어떤 전략 조합이 compute-optimal한가
- 현재 SLM-Math와 매우 직접적으로 연결되지만, 이 논문은 주로 **difficulty-conditioned strategy selection**이고, 우리는 **current reasoning state를 보는 heterogeneous path-family allocation**으로 차별화해야 한다.

## 4. 핵심 방법

- 이 논문은 TTC 사용 방식을 크게 두 축으로 나눈다.
  - verifier / PRM 기반 output-space search
  - proposal distribution refinement로서의 sequential revision
- verifier / PRM 기반 축:
  - `best-of-N weighted`
  - `beam search`
  - `lookahead search`
  - step-level PRM score를 이용해 intermediate candidate를 필터링하거나 rerank한다.
- revision 축:
  - 이전 attempt를 보고 다음 attempt를 수정하는 sequential revision model을 fine-tuning한다.
  - parallel sampling이 global exploration에 가깝다면, revision은 local refinement에 가깝다.
- 핵심 formulation은 prompt `q`, compute budget `N`, test-time hyperparameter `θ`에 대해 어떤 output distribution이 유도되는지 보고, 문제별로 accuracy를 최대화하는 `θ`를 선택하는 것이다.
- 결과적으로 이 논문은 `무조건 더 많이 샘플링`이 아니라 **어떤 문제에 어떤 TTC strategy를 쓰는가**가 중요하다고 주장한다.

## 5. SLM-Math 관점의 재해석

- 이 논문은 현재 연구의 framing과 매우 가깝다.
- 공통점:
  - 제한된 TTC 안에서 무엇을 더 할지 결정한다.
  - `parallel vs sequential`, `search vs revision`, `small model + TTC vs larger model` 구도를 모두 다룬다.
  - verifier / reranking / budget allocation을 같은 큰 그림에서 본다.
- 차이점:
  - 이 논문은 주로 `difficulty bin -> strategy / hyperparameter 선택` 문제다.
  - 선택 단위도 `best-of-N`, `beam`, `lookahead`, `revision ratio` 같은 search/revision mechanism 쪽이다.
  - 내 연구는 `direct`, `CoT`, `prompt-diverse CoT`, `structured rationale`, `PoT`, `CG`, `verifier-guided path` 등 **heterogeneous reasoning path family** 중 무엇을 추가로 획득할지, 그리고 언제 멈출지를 다뤄야 한다.
- 안전한 한 문장 차별화:
  - 이 논문이 problem difficulty를 바탕으로 TTC strategy를 고른다면, 내 연구는 **current reasoning state를 보고 next path family 또는 STOP을 고르는 문제**를 다룬다.

## 6. 우리 연구에 대한 novelty risk

- `adaptive TTC` 자체는 이미 새롭지 않다.
- `문제별로 compute를 다르게 배분한다`는 claim도 이미 약하다.
- `strategy selection` 자체도 이미 상당 부분 선점되어 있다.
- `verifier / PRM search`는 강한 baseline이다.
- `sequential vs parallel TTC trade-off`도 이미 분석되어 있다.
- `작은 모델 + TTC가 큰 모델보다 나을 수 있다`는 claim도 이미 강하게 제시되었다.
- 특히 위험한 claim:
  - `우리는 문제별 adaptive TTC allocation을 제안한다`
  - `우리는 strategy-level test-time compute selection을 처음 다룬다`
  - `best-of-N보다 효율적인 compute allocation이 새롭다`
- 안전한 방향:
  - `difficulty-conditioned strategy selection`이 아니라
  - `state-conditioned heterogeneous reasoning path pool construction and stopping`

## 7. 우리가 빌릴 수 있는 것

- 문제 framing:
  - fixed test-time budget 아래에서 어떤 compute strategy가 좋은가
  - TTC effectiveness는 problem difficulty에 strongly dependent하다
  - search / revision / sampling은 같은 축에서 비교되어야 한다
- baseline:
  - Majority voting
  - Parallel best-of-N
  - Best-of-N weighted
  - PRM best-of-N weighted
  - Beam search
  - Lookahead search
  - Sequential revision
  - Difficulty-conditioned oracle / predicted policy
- metric:
  - Accuracy vs generation budget
  - Difficulty-bin accuracy
  - Compute-normalized accuracy
  - verifier overhead 포함 cost accounting
  - budget-efficiency curve
- ablation:
  - oracle difficulty vs predicted difficulty
  - easy / medium / hard bin
  - sequential / parallel ratio
  - verifier quality degradation
  - majority voting vs verifier selection
- 표현/도식:
  - `Accuracy vs Budget` curve
  - difficulty/state bin별 selected strategy heatmap
  - oracle upper bound vs learned policy 비교
  - over-optimization / Goodharting risk 진단

## 8. 우리가 하면 안 되는 주장

- `adaptive TTC allocation`이 본 연구의 핵심 novelty라고 쓰면 안 된다.
- `문제 난이도에 따라 strategy를 고르는 것`을 새 contribution처럼 쓰면 안 된다.
- `verifier search는 항상 좋다`고 쓰면 안 된다.
- `sequential refinement가 parallel sampling보다 항상 좋다`고 쓰면 안 된다.
- `작은 모델 + TTC가 항상 큰 모델을 대체한다`고 쓰면 안 된다.
- `difficulty estimation은 간단히 붙이면 된다`고 쓰면 안 된다.
- `TTC와 pretraining compute는 1:1 교환 가능하다`고 쓰면 안 된다.

## 9. baseline / ablation 반영 아이디어

- `difficulty-only compute-optimal baseline`을 문서와 실험 설계에서 명시적 baseline으로 둔다.
- `best-of-N`, `majority`, `SC CoT`, `Multiple-CoT`, `Static MoR`, `Adaptive MoR`를 같은 budget 곡선에 올린다.
- `difficulty-only selector`와 `state-conditioned selector`를 직접 비교한다.
- verifier 호출 비용과 token / sample budget을 따로 기록한다.
- easy / medium / hard 문제에서 어떤 path family가 실제로 유리한지 분석한다.
- `oracle upper bound vs learned policy vs heuristic` 구조를 유지한다.
- verifier / reranker를 붙일 때는 high-budget에서 over-optimization이 생기는지도 본다.

## 10. Related Work에 넣을 문장 초안

Snell et al.의 **Scaling LLM Test-Time Compute Optimally Can Be More Effective Than Scaling Parameters for Reasoning**은 수학 추론에서 test-time compute를 어떻게 효율적으로 사용할지 체계적으로 분석한 대표적인 연구다. 이들은 test-time compute 사용 방식을 verifier 기반 search와 proposal distribution refinement로 나누고, `MATH` benchmark에서 `best-of-N`, `PRM-based beam search`, `lookahead search`, `sequential revisions`를 비교하였다. 특히 문제 난이도에 따라 최적의 compute strategy가 달라지며, difficulty-conditioned compute-optimal scaling이 `best-of-N`보다 훨씬 적은 compute로 유사하거나 더 높은 성능을 낼 수 있음을 보였다.

그러나 이 연구의 compute-optimal policy는 주로 문제 난이도에 기반해 search / revision strategy 또는 sequential-parallel ratio를 선택하는 방식이다. 반면 본 연구는 작은 언어모델의 수학 추론에서, 현재까지 생성된 reasoning paths의 answer distribution, route usage, disagreement, remaining budget 등 **intermediate reasoning state**를 관찰하고, `CoT`, `prompt-diverse CoT`, `structured rationale`, `PoT`, `direct solving`, `verifier-guided path` 등 heterogeneous reasoning path family 중 어떤 후보를 추가로 획득할지 또는 언제 멈출지를 결정하는 문제를 다룬다. 따라서 본 연구는 기존 compute-optimal TTC scaling 연구를 출발점으로 삼되, difficulty-conditioned strategy selection을 넘어 **state-conditioned reasoning path pool construction and stopping under limited test-time compute**로 확장한다.

## 11. 현재 우선순위와 다음 액션

- 현재 우선순위: `P0`
- 위협도: 높음
- 지금 당장 해야 할 일:
  - 이 논문을 `adaptive TTC / compute-optimal inference` 축의 핵심 anchor로 고정
  - 논문 framing에서 `adaptive TTC`만 전면에 두지 않도록 수정
  - `difficulty-only baseline`과 `state-conditioned baseline`을 분리해 설계
  - `best-of-N / majority / static MoR / adaptive MoR` budget-matched 표를 의무 baseline으로 포함
- 나중으로 미뤄도 되는 일:
  - full PRM training 재현
  - lookahead / online MCTS full reproduction
  - FLOPs-matched large-scale reproduction
- 한 문장 결론:
  - 내 연구는 `difficulty-conditioned compute allocation`의 반복이 아니라, **current reasoning state를 보고 heterogeneous path family를 획득·중단하는 TTC orchestration 문제**로 가야 한다.
