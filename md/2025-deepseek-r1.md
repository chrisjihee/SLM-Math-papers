# DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning review

## 1. Metadata

- Title: DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning
- Authors: DeepSeek-AI (collective authorship; 대규모 공동저자)
- Year: 2025
- Venue / Status: arXiv:2501.12948, 2025-01 공개 (arXiv 2025 기준)
- Links:
  - Paper: https://arxiv.org/abs/2501.12948
  - GitHub / Model: https://github.com/deepseek-ai/DeepSeek-R1
- Code / Data:
  - DeepSeek-R1 / DeepSeek-R1-Zero weights 및 distilled checkpoints(Qwen·Llama 기반 1.5B~70B) 공개
  - primary paper URL과 code/model URL은 분리 유지
- Paper Type:
  - `training-heavy`
  - `reasoning RL (GRPO)`
  - `distillation to small models`
  - `inference-time behavior 분석 (long CoT / self-verification)`
  - `contrastive frontier reference`
- Reading Status: `strategically-read`
- Current Priority: `P0`

## 2. One-line Summary

DeepSeek-R1은 human-labeled reasoning trajectory 없이 순수 RL(GRPO)만으로 long CoT·self-verification·dynamic strategy adaptation 같은 reasoning 행동이 창발함을 보이고(R1-Zero), 이를 cold-start + multi-stage RL로 안정화한 뒤 1.5B~70B 소형 모델로 distill해 강한 reasoning을 이식한 training-heavy frontier reasoner 논문이다.

## 3. 핵심 문제 설정

- 이 논문이 푸는 질문은 **명시적 reasoning supervision(human CoT annotation, SFT) 없이도 LLM의 reasoning 능력을 incentivize할 수 있는가**이다.
- 기존 한계로 보는 것:
  - reasoning 능력 향상이 대체로 대규모 human-labeled reasoning data나 강한 teacher distillation에 의존한다.
  - 그 의존성이 확장성과 재현성을 제약한다.
- 핵심 주장은 **reward signal(정답 여부, format 등)만 주면 RL 과정에서 reasoning이 스스로 길어지고 self-verification·reflection 행동이 emergent하게 나타난다**는 것이다.
- 내 연구와의 연결:
  - 직접적으로는 inference-time에 여러 path family를 선택·중단하는 논문이 아니다.
  - 그러나 long CoT, self-verification, strategy adaptation, distilled small reasoner라는 **claim 경계를 강하게 점유**하므로, 우리 mainline의 wording을 직접 제약한다.
  - 즉 직접 baseline 경쟁축이 아니라 **claim boundary를 긋는 contrastive frontier reference**다.

## 4. 핵심 방법

- DeepSeek-R1-Zero (pure RL):
  - SFT 없이 base model에 곧바로 GRPO(Group Relative Policy Optimization) 기반 RL을 적용한다.
  - value model을 두지 않고 같은 question의 sampled outputs group으로 baseline을 잡는 RL design(GRPO는 DeepSeekMath 계열과 연속).
  - rule-based reward(answer correctness, format)를 주로 사용한다.
  - 학습이 진행되며 response length(=thinking length)가 자발적으로 증가하고, 중간 검증/재고 같은 "aha moment" 행동이 창발한다.
- DeepSeek-R1 (cold-start + multi-stage):
  - R1-Zero의 readability 저하·language mixing 문제를 완화하기 위해 소량의 고품질 long-CoT cold-start data로 SFT한 뒤,
  - reasoning-oriented RL → rejection sampling 기반 SFT data 재생성 → 전 영역 RL의 multi-stage 파이프라인을 거친다.
- Distillation:
  - R1이 생성한 reasoning data로 Qwen·Llama 계열 1.5B~70B 모델을 SFT distillation한다.
  - 같은 규모에서 RL을 직접 도는 것보다 강한 reasoner로부터 distill하는 편이 효과적이라고 보고한다.
- selection unit 관점:
  - 이 논문의 통제 단위는 **model weights(training)** 와 **single long reasoning trace**다.
  - 외부에서 path family나 macro strategy를 명시적으로 선택·중단하는 구조가 아니다. self-verification/전략 전환은 trace 내부에서 학습된 implicit behavior다.

## 5. SLM-Math 관점의 재해석

- DeepSeek-R1은 내 연구의 직접 경쟁자라기보다, **"작은 모델 + 강한 reasoning" claim을 선점한 상위 contrastive reference**다.
- 공통점:
  - 작은 모델의 reasoning을 중시한다.
  - reasoning 과정에서 길이·검증·전략 적응이 중요하다는 점을 인정한다.
- 차이점:
  - R1의 핵심은 RL로 **model parameter 자체를 reasoner로 학습**하는 것이다.
  - 내 연구의 핵심은 주어진(고정된) backbone 위에서 제한된 TTC 안의 **heterogeneous reasoning path pool 구성·선택·검증·중단**이다.
  - R1의 reasoning behavior는 trace 내부의 implicit emergent 행동이고, 내 연구의 path family·macro strategy·STOP은 **외부에서 제어 가능한 명시적 decision unit**이다.
  - R1-distilled 소형 모델은 우리에게 경쟁 대상이 아니라 **strong backbone / strong baseline substrate**다.
- 안전한 한 문장 차별화:
  - DeepSeek-R1은 RL과 distillation으로 reasoning을 model 안에 학습시키고, 내 연구는 **그렇게 얻은 backbone 위에서 서로 다른 path family에 budget을 어떻게 나누고 언제 멈출지**를 다룬다.

## 6. 우리 연구에 대한 novelty risk

- `작은 모델도 강한 reasoning을 할 수 있다`는 넓은 claim은 distilled 1.5B~70B로 이미 강하게 선점되었다.
- `long CoT를 유도한다`, `self-verification/reflection 행동을 다룬다`도 이미 emergent behavior로 보고되었다.
- `RL로 reasoning capability를 incentivize한다`도 새롭지 않다.
- `distilled small reasoner` 자체도 강한 선행축이다.
- `dynamic strategy adaptation(전략 전환)`도 R1이 창발 행동으로 이미 언급하므로, 우리가 처음 다룬다고 하면 위험하다.
- 따라서 위험한 framing:
  - `SLM이 test-time에 깊게 reasoning할 수 있음을 보였다`
  - `self-verification / long thinking을 도입한다`
  - `reasoning을 유도/강화하는 것이 기여다`
- 다만 위협의 성격이 RASC / Learning How Hard to Think / Scaling TTC 같은 **inference-time 직접 baseline**과는 다르다. R1은 **training-time 기여**라 우리 inference-time mainline과 직교하며, 위험은 주로 **wording/claim boundary** 쪽에 있다.

## 7. 우리가 빌릴 수 있는 것

- problem framing:
  - reasoning은 단일 capability가 아니라 길이·검증·전략 적응이 결합된 행동이다.
  - training-time reasoning gain과 inference-time reasoning gain을 분리해야 한다.
  - distillation으로 얻은 reasoner는 backbone일 뿐, 그 위의 test-time 사용 방식은 별개 문제다.
- baseline:
  - DeepSeek-R1-Distill-Qwen-1.5B / 7B 등을 **strong distilled-reasoner backbone baseline**으로 사용.
  - "RL/distill로 학습된 long-CoT reasoner" vs "고정 backbone + 우리 orchestration" 대비군.
- metric:
  - AIME(pass@1), MATH-500, (가능 시) GPQA Diamond — 기존 우리 GSM8K/MATH500 평가와 정렬.
  - long-CoT의 thinking-token / length budget을 함께 보고해 budget-matched 비교 가능하게.
- ablation:
  - `long single-CoT (R1-style)` vs `heterogeneous path pool (ours)`를 **budget-matched**로 비교.
  - distilled reasoner backbone에 우리 orchestration을 얹었을 때 budget 절감·정확도 변화.
  - same backbone에서 implicit self-verification에 의존할 때 vs 외부 verifier/STOP을 둘 때.
- terminology(차용, 단 배경/대비로만):
  - `cold-start`, `reasoning trajectory`, `self-verification`, `dynamic strategy adaptation`, `long chain-of-thought`, `aha moment`, `distilled reasoner`, `System 2 reasoning`, `GRPO`.

## 8. 우리가 하면 안 되는 주장

- `RL로 reasoning capability를 유도하는 것이 새롭다`고 쓰면 안 된다.
- `small distilled reasoner 자체가 우리 novelty다`라고 쓰면 안 된다.
- `long CoT / self-verification / reflection behavior를 우리가 처음 다룬다`고 쓰면 안 된다.
- `작은 모델이 test-time compute로 깊은 수학 reasoning을 할 수 있음을 우리가 처음 보였다`고 쓰면 안 된다.
- `dynamic strategy adaptation(전략 전환)을 우리가 처음 제안한다`고 쓰면 안 된다.
- `우리 backbone이 R1-distill보다 raw하게 강하다` 같은 raw math SOTA 경쟁 프레임으로 가면 안 된다.

## 9. baseline / ablation 반영 아이디어

- `DeepSeek-R1-Distill-Qwen-1.5B/7B`를 strong reasoner backbone baseline 후보로 등록한다.
- `single long-CoT (budget forcing 포함) vs SC CoT vs heterogeneous path pool`을 동일 token budget 곡선에서 비교한다(s1 노트의 budget-matched 비교와 연동).
- distilled reasoner 위에서 implicit self-verification에만 의존할 때와, 외부 STOP / lightweight verifier를 붙일 때의 budget-accuracy 차이를 측정한다.
- AIME / MATH-500의 pass@1과 thinking-token을 함께 기록해 "더 길게 생각 = 더 좋음"이 아니라 path 다양화가 언제 유리한지 본다.
- `heavy RL + distillation`은 direct reproduction target이 아니라 **upper/reference backbone**으로만 둔다.

## 10. Related Work에 넣을 문장 초안

DeepSeek-R1은 human-labeled reasoning trajectory 없이 순수 reinforcement learning(GRPO)만으로 긴 chain-of-thought, self-verification, 동적 전략 적응 같은 reasoning 행동이 창발할 수 있음을 보이고, 이를 cold-start와 multi-stage RL로 안정화한 뒤 1.5B에서 70B 규모의 소형 모델로 distillation하여 강한 수학·코딩·STEM reasoning을 이식한 대표적인 reasoning RL 연구다. 이 논문은 작은 모델이 강한 reasoner로 distill될 수 있음을 보여주며, long-CoT와 self-verification을 모델 가중치 내부의 emergent behavior로 자리매김한다.

그러나 DeepSeek-R1의 핵심은 reinforcement learning과 distillation으로 model 자체를 reasoner로 학습시키는 training-time 접근이며, 고정된 backbone 위에서 제한된 test-time compute를 어떻게 배분할지는 직접 다루지 않는다. 본 연구는 이러한 training-heavy reasoner를 강한 backbone이자 비교 대상으로 삼되, 주어진 small language model이 현재 reasoning state, answer distribution, disagreement, 남은 budget을 바탕으로 CoT, prompt-diverse CoT, PoT/PAL, structured rationale, verifier-guided path 등 heterogeneous reasoning path family 중 무엇을 추가로 획득하고 언제 멈출지를 결정하는 **state-conditioned test-time compute allocation** 문제에 위치한다.

## 11. 현재 우선순위와 다음 액션

- 현재 우선순위: `P0`
- 위협도: 중간~높음 (raw 성능 경쟁축은 직교하지만, long-CoT·self-verification·distilled small reasoner claim boundary를 강하게 제약)
- 지금 당장 해야 할 일:
  - DeepSeek-R1을 `training-heavy / reasoning RL` 축의 P0 contrastive reference로 고정 (rStar-Math·DeepSeekMath와 같은 cluster)
  - claim에서 `long CoT / self-verification / RL reasoning / distilled small reasoner`를 우리 novelty로 쓰지 않도록 wording 가드 설정
  - `R1-Distill` 계열을 strong reasoner backbone baseline 후보로 등록
  - `single long-CoT vs heterogeneous path pool`의 budget-matched 비교를 평가 프로토콜에 포함
- 나중으로 미뤄도 되는 일:
  - GRPO / multi-stage RL 파이프라인 직접 재현
  - R1-Zero pure-RL 재현
  - distillation data 재생성 및 full distillation reproduction
- 한 문장 결론:
  - DeepSeek-R1은 우리가 따라가야 할 implementation target이 아니라, **training-heavy reasoner와 구분되는 lightweight test-time path-pool orchestration으로 우리 연구를 위치시키고, long-CoT·self-verification·distilled reasoner claim을 절제하게 만드는 P0 contrastive reference**다.
