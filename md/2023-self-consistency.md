# Self-Consistency Improves Chain of Thought Reasoning in Language Models review

## 1. Metadata

- Title: Self-Consistency Improves Chain of Thought Reasoning in Language Models
- Authors: Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery, Denny Zhou
- Year: 2023
- Venue / Status: ICLR 2023 (arXiv 2203.11171는 2022-03 공개)
- Links:
  - Paper (OpenReview): https://openreview.net/forum?id=1PL1NIMMrw
  - arXiv: https://arxiv.org/abs/2203.11171
  - GitHub / Model: 공식 official code repository 없음 (decoding/aggregation 기법)
- Code / Data:
  - 별도 공개 코드/모델 없음. 평가 benchmark는 기존 공개 데이터(GSM8K 등) 사용.
  - primary paper URL만 관리(code URL 없음).
- Paper Type:
  - `inference-time` / `prompting`
  - `self-consistency / majority-vote aggregation`
  - `canonical multi-sample baseline`
- Reading Status: `strategically-read`
- Current Priority: `P0`

## 2. One-line Summary

Self-Consistency는 동일 prompt에서 CoT reasoning path를 여러 개(temperature) 샘플링한 뒤 최종 answer를 majority vote로 집계하면, greedy single-path CoT보다 안정적으로 정확도가 오름을 보인 canonical multi-sample / majority-vote baseline이다.

## 3. 핵심 문제 설정

- 이 논문이 푸는 질문은 **하나의 greedy CoT가 종종 틀리는데, 여러 reasoning path를 marginalize하면 더 맞출 수 있는가**이다.
- 기존 한계로 보는 것:
  - greedy single-path CoT는 한 번의 잘못된 step에 취약하다.
  - 정답은 보통 여러 다른 reasoning 경로로 도달 가능하다는 직관을 활용하지 못한다.
- 해법은 **동일 prompt에서 diverse CoT path를 sampling → 각 path의 final answer를 모아 majority vote(answer marginalization)**.
- 내 연구와의 연결:
  - SC는 우리 연구의 **CoT 이후 canonical multi-sample baseline이자 반드시 넘어야 할 fixed homogeneous SC baseline**이다.
  - RASC / CISC / adaptive-TTC 계열은 모두 이 homogeneous SC substrate 위에서 stopping·weighting·confidence를 더한 확장이다.
  - 우리 기여는 SC를 개선하는 것이 아니라, **homogeneous same-prompt sampling 대신 heterogeneous path family pool을 state-conditioned하게 구성·중단**하는 것이다.

## 4. 핵심 방법

- reasoning path:
  - 동일 prompt에서 생성한 여러 자연어 CoT path (temperature sampling).
- sampling:
  - 핵심은 **homogeneous same-prompt multi-sampling** (path family 다양화가 아니라 동일 분포 반복 샘플).
- self-consistency:
  - 각 path의 final answer를 모아 **majority vote(answer marginalization)**. 가장 빈도 높은 answer 선택.
- test-time compute:
  - sample 수 K가 사실상 TTC budget이며, K↑에 따른 accuracy scaling curve를 보고(=sample-scaling curve). 단, **adaptive allocation·stopping은 없음**(고정 K).
- verifier / reward / search:
  - 없음. verifier 없이 순수 answer-frequency 집계. (best-of-N verifier selection과 다름 — 점수가 아니라 빈도.)
- selection unit 관점:
  - 통제 단위는 **sample / answer** (개별 path를 점수화·재배치하지 않고 answer 빈도로 marginalize).
- 핵심 관찰:
  - diverse reasoning path를 marginalize하면 단일 path보다 robust하다.

## 5. SLM-Math 관점의 재해석

- SC는 내 연구의 경쟁자가 아니라 **CoT 다음 단계의 필수 baseline이자 substrate**다.
- 공통점:
  - 여러 reasoning path를 만들어 답을 고르는 multi-path 사고를 정면으로 다룬다.
  - 추가 학습 없이 inference-time 행동을 바꾼다.
- 차이점:
  - SC의 핵심은 **동일 prompt의 homogeneous sampling + 고정 K majority vote**다.
  - 내 연구의 핵심은 **heterogeneous path family(어떤 family를 언제 추가)와 state-conditioned STOP**이다.
- 안전한 한 문장 차별화:
  - SC는 fixed homogeneous same-prompt sampling을 majority-vote하고, 내 연구는 **현재 reasoning state를 보고 서로 다른 path family를 언제 더 획득하고 언제 멈출지**를 다룬다.
- RASC/CISC와의 관계:
  - RASC(reasoning-aware stopping/weighting), CISC(confidence-weighted vote)는 모두 **SC substrate 위의 aggregation/stopping 개선**이며, 우리는 그보다 **upstream의 path-pool 구성(어떤 후보 family를 만들지)**으로 이동한다.

## 6. 우리 연구에 대한 novelty risk

- `self-consistency / majority voting 자체`는 이 논문이 원형이므로 절대 우리 novelty가 될 수 없다.
- `여러 reasoning path를 샘플링하면 좋아진다`도 SC가 선점.
- `sample 수를 늘리면 accuracy가 오른다(sample scaling)`도 SC가 선점.
- `homogeneous multi-sample reasoning`도 SC가 선점.
- 따라서 위험한 framing:
  - `우리는 self-consistency를 도입한다 / 처음 쓴다`
  - `majority voting으로 답을 고르는 것이 우리 기여다`
  - `여러 path 샘플링이 좋다는 것을 보인다`
- 주의할 구분:
  - **fixed homogeneous SC**(동일 prompt 반복 샘플 + 고정 K)와 **heterogeneous path-family allocation**(어떤 family를 언제, STOP 포함)을 명확히 분리하지 않으면 SC와 겹쳐 보인다.

## 7. 우리가 빌릴 수 있는 것

- problem framing:
  - 단일 path는 취약하고, 여러 path의 marginalization이 robust하다.
  - sample 수가 TTC budget의 가장 단순한 형태다.
- baseline:
  - **fixed homogeneous SC@K**(K=1/4/8/16/32/64)를 모든 path-pool 실험표의 필수 비교군으로.
  - greedy single-path CoT(origin) → SC@K → heterogeneous pool의 점증 구조.
- metric:
  - accuracy, `Maj@K`(majority vote accuracy), sample-scaling curve.
  - sample 수 대비 정확도(=budget proxy), token-budget 정규화 비교.
- ablation:
  - `same-prompt SC` vs `prompt-diverse CoT` vs `heterogeneous path-family pool`을 같은 K(또는 token budget)에서 비교.
  - answer-level majority vote vs path-level selection의 경계.
- terminology(차용):
  - `self-consistency`, `majority vote`, `answer marginalization`, `diverse reasoning paths`, `sample scaling`.

## 8. 우리가 하면 안 되는 주장

- `self-consistency를 우리가 처음 쓴다 / 도입한다`고 쓰면 안 된다.
- `majority voting으로 답을 집계하는 것이 우리 novelty다`라고 쓰면 안 된다.
- `여러 reasoning path를 샘플링하면 좋아진다`를 새 관찰처럼 쓰면 안 된다.
- `sample 수를 늘리면 좋아진다(sample scaling)`를 우리 발견처럼 쓰면 안 된다.
- `fixed homogeneous SC`와 `heterogeneous path-family allocation`을 뭉뚱그려 쓰면 안 된다.
- SC 자체를 부정/폄하하는 듯한 wording도 피한다(필수 baseline이므로).

## 9. baseline / ablation 반영 아이디어

- `fixed SC@K`를 K=1/4/8/16/32/64로 모든 실험표의 origin multi-sample baseline으로 고정한다.
- `greedy CoT → SC@K → prompt-diverse CoT → heterogeneous pool(+CG/PAL/PoT) → +verifier-guided`의 점증 비교.
- `same budget에서 homogeneous SC vs heterogeneous pool`을 직접 대비하는 핵심 figure(우리 thesis의 중심 그림).
- `Maj@K`와 `Pass@K`를 분리(DeepSeekMath 노트와 정합)해 exploration vs aggregation을 구분.
- RASC/CISC식 stopping·weighting을 SC 위의 강한 비교군으로 두되, 우리 차별점은 **upstream pool 구성**임을 ablation으로 분리.

## 10. Related Work에 넣을 문장 초안

Self-Consistency(Wang et al., ICLR 2023)는 동일한 prompt에서 여러 chain-of-thought reasoning path를 샘플링한 뒤 최종 answer를 majority vote로 집계(answer marginalization)하면, greedy single-path CoT보다 일관되게 높은 정확도를 얻을 수 있음을 보인 대표적인 sampling-based reasoning baseline이다. 이 방법은 이후 거의 모든 test-time compute / sampling 연구의 기반이 되었으며, Reasoning-Aware Self-Consistency나 Confidence Improves Self-Consistency와 같은 후속 연구는 이 homogeneous self-consistency substrate 위에서 stopping rule, rationale-aware weighting, confidence-weighted voting 등을 더해 sample 효율을 높인다.

그러나 Self-Consistency는 동일 prompt에서 같은 분포의 reasoning path를 반복 샘플링하고 고정된 sample 수로 majority vote하는 homogeneous multi-sample 방법이며, 서로 다른 reasoning path family 중 무엇을 추가로 획득할지나 현재 reasoning state를 보고 언제 멈출지는 다루지 않는다. 본 연구는 Self-Consistency를 반드시 넘어야 할 fixed homogeneous SC baseline으로 삼되, 주어진 small language model이 현재 answer distribution, disagreement, 남은 budget을 바탕으로 CoT, prompt-diverse CoT, structured rationale(CG), PAL/PoT, verifier-guided path 등 heterogeneous reasoning path family 중 무엇을 추가로 획득하고 언제 멈출지를 결정하는 **state-conditioned test-time compute allocation** 문제에 위치한다.

## 11. 현재 우선순위와 다음 액션

- 현재 우선순위: `P0`
- 위협도: 낮음~중간 (origin multi-sample baseline이라 직접 위협이 아니라 **baseline 고정·claim boundary** 측면에서 중요)
- 지금 당장 해야 할 일:
  - `fixed SC@K`(K=1/4/8/16/32/64)를 모든 path-pool 실험표의 필수 baseline으로 고정
  - `homogeneous SC vs heterogeneous pool` budget-matched 대비 figure 설계
  - SC / RASC / CISC를 substrate→aggregation/stopping 확장으로 정리하고, 우리 차별점은 upstream path-pool 구성으로 명시
  - `self-consistency / majority vote 자체`를 novelty로 쓰지 않도록 wording 가드
- 나중으로 미뤄도 되는 일:
  - SC의 commonsense/symbolic benchmark full sweep(우리 mainline은 math)
  - 대규모 K 스케일 재현
- 한 문장 결론:
  - Self-Consistency는 우리가 처음 쓰거나 이기려는 대상이 아니라, **CoT 이후 반드시 넘어야 할 fixed homogeneous SC baseline이자 RASC/CISC의 substrate로 고정하고, 우리 기여를 heterogeneous path-family acquisition과 state-conditioned STOP으로 분리하게 만드는 P0 anchor baseline**이다.
