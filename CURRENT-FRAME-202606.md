# CURRENT FRAME 2026-06

## 1. 배경

이 연구는 원래 **Concept Graph(CG) distillation**에서 출발했다. 2025년 결과는 "teacher가 만든 structured rationale을 student가 학습하면 일부 소형 모델의 수학 추론이 개선될 수 있다"는 가능성을 보여줬다. 그러나 2026년 Axis 1/2와 4월 15일, 6월 11일, 6월 13일 미팅을 거치며 프레임은 바뀌었다.

현재 evidence는 다음을 보여 준다.

- Axis 1 공식 `val-selected best on test`에서 `LLaMA-8B` 기준 `CoT_Lv1 61.37% > CoT_Lv2 57.86% > CoT_Lv3 56.72% > CG 53.13%`.
- Axis 2 `budget12` student strongest system은 `CG+CoT`가 아니라 `CoT_Lv1+CoT_Lv2+CoT_Lv3`이며, test에서 `70.3053%`.
- `student+none` practical oracle은 `test-1310`에서 `90.9924%`로, 현재 best fixed system `72.9008%`보다 headroom이 매우 크다.
- warm-start sequential router oracle은 `test-1310`에서 `67.33% -> 88.70%`까지 올라간다.

즉, 현재 연구는 더 이상 "CG superiority"를 증명하는 프로젝트가 아니다. 더 정확한 문장은 다음과 같다.

> CG는 여러 reasoning path family 중 하나이며, 현재 핵심 병목은 path pool construction, path selection, answer selection / verification, budget-aware stopping이다.

## 2. 현재 중심 질문

현재 canonical question은 아래 한 문장으로 정리한다.

> 제한된 테스트타임 계산량 안에서 소형 언어모델이 heterogeneous reasoning path를 어떻게 구성, 선택, 검증, 중단해야 하는가?

조금 더 풀면 네 개의 하위 질문이다.

1. 어떤 reasoning path family를 pool에 넣어야 하는가?
2. 어떤 문제에서 어떤 path family와 budget이 유리한가?
3. 언제 더 샘플링하고, 언제 멈춰야 하는가?
4. path 간 충돌이 있을 때 어떤 verifier / reranker / combiner가 필요한가?

## 3. 왜 Axis 1 / Axis 2가 이 프레임으로 이어졌는가

### Axis 1이 보여 준 것

- CoT는 현재 더 강한 baseline이다.
- CG는 0이 아니지만 predefined winner가 아니다.
- `plan-first` 같은 단일 포맷 교체는 오히려 성능을 떨어뜨렸다.
- 따라서 질문은 "CG를 살릴 것인가"보다 "어떤 표현이 어떤 조건에서 보완 신호를 주는가"로 이동했다.

### Axis 2가 보여 준 것

- 병렬 sampling 자체가 강력하다.
- multiple-CoT diversity가 매우 강하다.
- adaptive policy의 핵심 가치는 accuracy 자체보다 **budget allocation efficiency**에 있다.
- generation quantity보다 **problem-conditioned allocation**과 **selection/verification**이 더 큰 병목일 가능성이 높다.

### Sequential router line이 보여 준 것

- offline oracle upper bound는 충분히 크다.
- structured heuristic도 의미 있지만 learned policy는 아직 약하다.
- 현재 가장 자연스러운 formulation은 token-level reasoning이 아니라 **sample-level / strategy-level TTC allocation**이다.

## 4. reasoning path family를 어떻게 정의할 것인가

현재 연구에서 `reasoning path family`는 단순 prompt variant보다 넓은 개념이다. 아래처럼 본다.

- `direct / none`
  외부 rationale 없이 바로 답을 내는 경로.

- `CoT variants`
  자연어 CoT, sectioned CoT, structured CoT 등.

- `prompt-diverse CoT`
  같은 CoT 계열이지만 서로 다른 style / decomposition / perspective를 갖는 경로 묶음.

- `PoT / PAL / tool-assisted reasoning`
  계산이나 symbolic execution을 외부 도구로 넘기는 경로.

- `structured rationale`
  sectioned JSON, statement list, schema-constrained intermediate rationale.

- `concept graph`
  triple/graph-style intermediate representation을 쓰는 structured path family.

- `verifier-guided path`
  sample 생성 후 verifier / PRM / reranker로 고르거나 수정하는 경로.

- `search / reflection path`
  Tree search, MCTS, reflection, revision, long-thought 등 iterative search를 포함하는 경로.

- `RAG-grounded path`
  외부 문서, table, spec, KG, log context를 끌어와 reasoning하는 경로.

핵심은 **CG도 이 taxonomy 안의 한 path family**라는 점이다.

## 5. 현재 허용되는 주장

- CG는 일부 조건에서 유효한 structured rationale family일 수 있다.
- CoT diversity와 route composition이 현재 매우 강한 신호다.
- adaptive TTC allocation은 budget efficiency 관점에서 유망하다.
- 현재 병목은 route generation만이 아니라 route selection / answer selection / verification이다.
- sequential TTC router는 sample-level compute allocation problem으로 보는 편이 정확하다.
- 현재 CG 구현은 graph-preserving reasoning보다 **linearized structured rationale**에 가깝다.
- NFM는 selective application domain으로 연결할 수 있다.

## 6. 아직 허용되지 않는 주장

- "CG가 CoT보다 우월하다"
- "graph reasoning을 이미 달성했다"
- "sequential routing 문제가 해결됐다"
- "listwise line은 실패했으니 버려도 된다"
- "reflection은 원리적으로 무의미하다"
- "NFM에서 곧바로 SOTA를 낼 수 있다"
- "이 연구의 main novelty는 CG 자체다"

특히 아래 표현은 피한다.

- "CG를 rescue해야 한다"
- "CG가 메인 contribution이다"
- "graph reasoning superiority"

## 7. 현재 메인라인의 안전한 논문화 프레임

가장 안전한 umbrella는 다음과 같다.

> Efficient and Reliable Reasoning Path Selection for Small Language Models

메인 contribution 후보는 아래 조합이다.

- heterogeneous reasoning path pool construction
- budget-aware test-time compute allocation
- state-conditioned path / strategy reranking
- verifier-aware answer/path selection

여기서 `CG`는 main axis가 아니라 **한 구조화 path family**로 포함한다.

## 8. 현재 scope 안 / 밖

### 현재 scope 안

- 메인 벤치마크: `GSM8K-kor`, `GSM8K`, 가능하면 `MATH` 또는 `MATH500`
- 비교축: direct, CoT variants, prompt-diverse CoT, structured rationale, CG, verifier-guided selection
- 메트릭: accuracy + average budget + token/latency proxy + case study
- research question: path pool, selection, stopping, verification

### 현재 scope 밖

- rStar-Math 수준의 대규모 self-evolution 재현
- 대형 teacher 의존 test-time inference
- 너무 많은 benchmark 동시 확장
- telecom-only thesis 전환
- CG를 graph reasoning으로 과장하는 서술

## 9. NFM는 어디에 들어오는가

NFM는 메인 주제가 아니라 **application/bridge domain**이다.

가장 자연스러운 연결은 아래 세 가지다.

- `TeleMath`
  math reasoning mainline과 직접 연결된다.

- `TeleTables`
  structured input / table reasoning / retrieval-selection으로 이어진다.

- `TeleLogs`
  RCA와 verifier/diagnostic path selection 문제로 이어진다.

`TeleQnA`와 `3GPP TSG`는 더 쉬운 retrieval/knowledge anchor로 활용할 수 있지만, thesis core로 두지는 않는다.

## 10. 현재 한 줄 결론

2026-06 이후 SLM-Math의 중심은 **CG 우월성 입증**이 아니라, **수학 추론에서 heterogeneous reasoning path pool을 만들고, 제한된 TTC 안에서 어떤 path를 어떻게 선택·검증·중단할지 연구하는 것**이다.
