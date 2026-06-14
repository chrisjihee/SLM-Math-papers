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

## 4. 현재 safe claim

- `CG`는 여러 reasoning path family 중 하나다.
- 현재 strongest student result는 multiple-CoT 축에 있다.
- 다음 병목은 route generation보다 route/budget selection과 answer/path verification이다.
- adaptive TTC는 여전히 중요하지만, novelty는 단순 budget allocation보다 path-family / strategy-level allocation 쪽에 있어야 한다.

## 5. 현재 forbidden claim

- "CG가 CoT보다 우수하다"
- "graph reasoning superiority"
- "sequential routing is solved"
- "reflection is ineffective in general"
- "NFM에서 곧바로 SOTA를 낼 수 있다"
- "이 연구의 main novelty는 CG 자체다"

## 제출 전략상 가장 위험한 선행연구

### rStar-Math

- risk:
  full MCTS + PPM + self-evolution이 현재 우리 line보다 훨씬 강한 math frontier다.
- response:
  우리는 raw frontier performance 경쟁이 아니라, 제한된 TTC 안에서 lightweight path/strategy selection을 다룬다.

### Learning How Hard to Think

- risk:
  adaptive TTC 자체는 새롭지 않다.
- response:
  우리의 contribution은 단순 budget allocation이 아니라 path-family / strategy-level allocation이어야 한다.

### Reasoning-Aware Self-Consistency / Confidence Improves Self-Consistency

- risk:
  SC efficiency, early stopping, confidence-weighted voting은 이미 연구되어 있다.
- response:
  우리는 homogeneous SC가 아니라 heterogeneous path pool construction과 state-conditioned strategy selection을 강조해야 한다.

### Self-Discover / Automatic Model Selection

- risk:
  reasoning strategy selection 자체도 새롭지 않다.
- response:
  우리는 dynamic budgeted path acquisition, stopping, verifier/reranker를 결합한 방향으로 차별화해야 한다.

### Verifier / PRM papers

- risk:
  answer/path selection은 verifier/PRM literature에서 강하게 다뤄졌다.
- response:
  우리의 route/strategy reranker는 step-level PRM과 다르게 path acquisition 전/중간의 lightweight policy/value estimator로 위치시킨다.

## 정보과학회 S/A 우수학술대회 기준 제출 전략

- 현재 연구의 1차 target은 `ACL / EMNLP / NAACL / AAAI`다.
- `ICLR / ICML / NeurIPS`는 stretch target이다.
- `ACL Findings / EMNLP Findings / NAACL Findings / COLING / EACL / IJCAI`는 realistic fallback이다.
- `SIGIR / KDD / WSDM / CIKM / WWW`는 ranking, retrieval, evidence-grounding이 중심이 될 때만 고려한다.
- NFM bridge는 처음부터 `SIGCOMM / NSDI / INFOCOM`을 노리지 말고, `TeleMath` 중심의 domain reasoning application을 NLP/AI venue에 붙이는 것이 우선이다.
- network venue는 실제 network-system contribution이 생겼을 때만 고려한다.

## 8. graph / structured reasoning papers와의 포지셔닝

- 공통점:
  structured intermediate representation에 관심이 있다.

- 차이점:
  현재 우리 `CG`는 graph-preserving traversal보다 **linearized structured rationale**에 가깝다.

- 안전한 문장:
  "CG-style rationale은 structured path family 중 하나로 평가된다."

- 금지 문장:
  "우리는 graph reasoning을 했다."

## 9. NFM를 어떻게 붙일 것인가

- NFM는 메인 thesis topic이 아니라 application/bridge다.
- 가장 좋은 immediate bridge는 `TeleMath`다.
- `TeleTables`, `TeleLogs`는 second-phase candidate다.
- `TeleQnA`는 retrieval/knowledge anchor로는 유용하지만 thesis core novelty로는 약하다.

## 10. paper title 방향

- State-Conditioned Test-Time Compute Allocation for Small Language Model Reasoning
- Budget-Aware Reasoning Path Pool Construction for Small Language Models
- Heterogeneous Reasoning Path Selection for Efficient Self-Consistency
- Macro-Action Routing for Budget-Efficient Mathematical Reasoning
- Strategy-Card Reranking for Small Language Model Reasoning
- Domain-Aware Reasoning Strategy Selection for Telecom Mathematical Reasoning

## 11. blunt recommendation

첫 논문은 **math reasoning mainline**으로 가야 한다.

- 주제:
  path pool + TTC allocation + reranking/verification
- 벤치마크:
  `GSM8K-kor`, `GSM8K`, 가능하면 `MATH500`
- CG:
  auxiliary structured family
- NFM:
  후속 bridge paper
