# POSITIONING NOTES

## 1. 한 문장 thesis candidate

소형 언어모델의 수학 추론에서 핵심은 특정 rationale 포맷의 우월성보다, **heterogeneous reasoning path pool을 제한된 테스트타임 계산량 안에서 어떻게 선택·검증·중단하느냐**에 있다.

## 2. 메인 contribution 후보

- problem-conditioned test-time compute allocation
- heterogeneous reasoning path family selection
- route-card / strategy-card 기반 lightweight reranking
- answer selection / verification을 포함한 budget-aware inference orchestration

## 3. 우리의 contribution이 아닌 것

- 새로운 대규모 math pretraining corpus
- rStar-Math 급 MCTS self-evolution 재현
- PRM 자체의 SOTA 학습법
- graph reasoning 자체의 근본적 돌파
- telecom foundation model 전체를 새로 만드는 것

## 4. rStar-Math / strong math SLM papers와의 포지셔닝

- 경쟁점:
  같은 "math reasoning" 축에 있다.

- 차이점:
  rStar-Math는 `MCTS + PPM + self-evolution + massive synthesized trajectories`에 가깝다.
  우리는 **lighter-weight inference orchestration / path selection / budget allocation** 문제를 다룬다.

- 안전한 문장:
  "본 연구는 rStar-Math류의 대규모 search/self-evolution을 재현하려는 것이 아니라, 더 가벼운 compute budget 아래에서 heterogeneous reasoning path를 선택하는 문제를 다룬다."

- 피해야 할 문장:
  "우리 방법이 rStar-Math보다 더 강하다."

## 5. self-consistency papers와의 포지셔닝

- baseline:
  `Self-Consistency`는 반드시 baseline이다.

- 차이점:
  우리는 단순 `same-prompt repeated sampling`이 아니라 **path family 자체가 이질적인 후보 풀**을 다룬다.

- 메시지:
  "Self-consistency를 부정하는 것이 아니라, self-consistency의 후보 풀을 더 잘 구성하고, 문제별로 샘플 수와 path family를 다르게 배정하는 문제로 확장한다."

## 6. verifier / PRM papers와의 포지셔닝

- baseline:
  `Training Verifiers`, `Let's Verify Step by Step`, `Math-Shepherd`, `ThinkPRM`은 verifier 축의 정석이다.

- 차이점:
  우리는 full step-level verifier를 새로 만드는 것보다, **path-level / strategy-level selection과 lightweight reranking**에 더 가깝다.

- 메시지:
  "정답 후보나 step을 직접 검증하는 PRM과 달리, 본 연구는 어떤 reasoning path family를 더 샘플링할지 결정하는 policy/value estimator에 가깝다."

## 7. Self-Discover / strategy selection papers와의 포지셔닝

- 공통점:
  reasoning strategy를 고정하지 않고 선택한다.

- 차이점:
  Self-Discover는 주로 **reasoning structure composition**이고, 우리는 **budgeted path acquisition and stopping**을 본다.

- 메시지:
  "전략을 한 번 정하고 끝내는 것이 아니라, 현재까지의 상태를 보고 다음 샘플/다음 전략을 고르는 sequential allocation에 가깝다."

## 8. graph / structured reasoning papers와의 포지셔닝

- 공통점:
  structured intermediate representation에 관심이 있다.

- 차이점:
  현재 우리 CG는 graph-preserving traversal보다 **linearized structured rationale**에 가깝다.

- 안전한 문장:
  "CG-style rationale은 structured path family 중 하나로 평가된다."

- 금지 문장:
  "우리는 graph reasoning을 했다."

## 9. NFM를 어떻게 붙일 것인가

- NFM는 메인 thesis topic이 아니라 application/bridge다.
- 가장 좋은 연결은 `TeleMath -> TeleTables -> TeleLogs` 순이다.
- `TeleQnA`는 retrieval/knowledge anchor로는 좋지만 thesis core novelty로는 약하다.
- NFM paper는 메인 math paper 이후의 확장 또는 parallel bridge paper로 두는 편이 안전하다.

## 10. Forbidden claims

- "CG가 CoT보다 우수하다"
- "graph reasoning superiority"
- "sequential routing is solved"
- "reflection is ineffective in general"
- "listwise failed, so ranking은 끝났다"
- "NFM에서 SOTA를 달성할 수 있다"
- "teacher-level search 없이도 rStar류와 직접 경쟁 가능하다"

## 11. Safer claims

- "CG는 여러 path family 중 하나이며 utility는 조건부다."
- "현재 strongest student result는 multiple-CoT이지만, structured path family는 auxiliary diversity source로 남아 있다."
- "문제별 route/budget allocation이 다음 핵심 병목이다."
- "path-level reranking과 stopping policy는 lightweight but meaningful contribution이 될 수 있다."
- "NFM는 math mainline을 해치지 않는 범위에서 selective bridge domain으로 유효하다."

## 12. paper title 방향

- State-Conditioned Test-Time Compute Allocation for Small Language Model Reasoning
- Budget-Aware Reasoning Path Pool Construction for Small Language Models
- Heterogeneous Reasoning Path Selection for Efficient Self-Consistency
- Macro-Action Routing for Budget-Efficient Mathematical Reasoning
- Strategy-Card Reranking for Small Language Model Reasoning
- Domain-Aware Reasoning Strategy Selection for Telecom Mathematical Reasoning

## 13. blunt recommendation

첫 논문은 **math reasoning mainline**으로 가야 한다.

- 주제: path pool + TTC allocation + reranking/verification
- 벤치마크: `GSM8K-kor`, `GSM8K`, 가능하면 `MATH500`
- CG: auxiliary structured family
- NFM: 후속 bridge paper
