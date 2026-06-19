# Self-Refine: Iterative Refinement with Self-Feedback review

## 1. Metadata

- Title: Self-Refine: Iterative Refinement with Self-Feedback
- Authors: Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, Shashank Gupta, Bodhisattwa Prasad Majumder, Katherine Hermann, Sean Welleck, Amir Yazdanbakhsh, Peter Clark (CMU / Allen Institute for AI / UW / NVIDIA / UC San Diego / Google Research)
- Year: 2023
- Venue / Status: NeurIPS 2023 (arXiv 2303.17651, v1 2023-03, v2 2023-05)
- Links:
  - Paper: https://arxiv.org/abs/2303.17651
  - Project / Code (official): https://selfrefine.info/
- Source PDF (local, source-of-record): `paper/2023-self-refine.pdf`
- Source Grounding Log:
  - PDF: `paper/2023-self-refine.pdf` — 54 pages, sha256 `81e44592314d80218ad108d3490cd0b84ba5962fefd5c84819987afd77a57087`, pypdf/pymupdf 본문 추출 정상(약 124k자). title/authors/abstract/method/tasks/code 직접 확인.
  - arXiv abstract: 저자·arXiv id·subjects(cs.CL/cs.AI/cs.LG)·official link(selfrefine.info) 확인.
  - official code/project: https://selfrefine.info/.
  - TeX source/ar5iv: 미사용(PDF로 충분).
  - 주의: venue(NeurIPS 2023)는 외부 확정 사실로 기록(PDF/arXiv comment에 직접 미표기).
- Paper Type: `inference-time` / `prompting` / `iterative self-refinement (reflection)` baseline reference
- Reading Status: `strategically-read`
- Current Priority: `P1`

## 2. One-line Summary

Self-Refine는 추가 학습·RL·supervised data 없이 **하나의 LLM이 generator·feedback provider·refiner 역할을 모두 맡아** 초기 출력을 생성→자기 피드백→개선을 반복하는 iterative self-refinement 기법으로, GPT-3.5/GPT-4에서 7개 과제 평균 품질을 끌어올린 대표 reflection 논문이다.

## 3. 핵심 문제 설정

- 문제: LLM은 첫 시도에서 최선의 출력을 내지 않는다. 사람이 글을 고치듯 **inference-time에 스스로 피드백을 주고 고치면** 더 나은 출력을 낼 수 있는가?
- 해법: `generate → self-feedback(같은 LLM) → refine` 루프를 few-shot prompting만으로 반복. 별도 학습/보상모델 불필요.
- 내 연구와의 연결: Self-Refine는 **reflection / self-feedback / iterative refinement를 선점**한 논문이다. 우리 연구에서 reflection은 새 기여가 아니라 **macro strategy 후보 중 하나**이며, 핵심은 제한된 TTC 안에서 어떤 path family를 추가 획득·언제 STOP·어떤 verification을 쓸지다.

## 4. 핵심 방법

- 구성: 단일 LLM `M`이 (1) 초기 출력 생성, (2) 자기 출력에 대한 구체적 자연어 feedback 생성, (3) feedback를 반영한 refine을 **반복**(정지 조건 또는 최대 iteration까지).
- 학습: **없음**(no supervised data, no additional training, no RL). few-shot exemplar로 feedback/refine을 유도.
- selection unit: 동일 path(단일 출력)의 **iterative 개선**. heterogeneous path-family 선택이나 budget allocation/STOP 정책은 아님.
- 실험(PDF 본문):
  - model: **GPT-3.5, GPT-4**(ChatGPT 포함).
  - tasks(7): dialog response, code optimization, code readability, **Math Reasoning(GSM8K)**, sentiment reversal, acronym generation, constrained generation.
  - 결과: single-pass 대비 평균 약 20% 절대 향상. **단, Math Reasoning(GSM8K)에서는 향상이 작음** — 과제 의존성이 큼.

## 5. SLM-Math 관점의 재해석

- Self-Refine는 직접 baseline 경쟁자라기보다 **reflection macro-strategy의 대표 reference**다.
- 공통점: 추가 학습 없이 inference-time 행동으로 품질 개선, "한 번에 끝내지 않는다"는 점.
- 차이점:
  - Self-Refine는 **동일 path를 반복 개선**(sequential refinement). 우리는 **heterogeneous path family 사이의 획득·배분·STOP**(거시).
  - Self-Refine는 large model(GPT-3.5/4) 중심. 우리는 small LM + budget 제약.
- 연결: reflection을 우리 macro strategy card 중 하나(`refine-then-retry`)로 포함하고, **parallel SC vs iterative refinement를 budget-matched로 비교**할 수 있다.
- caveat: Self-Refine의 수학에서의 작은 향상을 근거로 **"reflection은 효과 없다"고 일반화하면 안 된다**(과제·모델·budget 의존).

## 6. 우리 연구에 대한 novelty risk

- **reflection / self-feedback / iterative refinement**를 이미 선점 → 이 자체를 우리 novelty로 쓰면 충돌.
- "같은 모델이 스스로 평가·개선" 아이디어도 선점.
- 위험 framing: `self-refinement가 우리 기여`, `reflection loop를 도입`.
- 단, Self-Refine는 단일 path 개선(미시)이라 inference-time allocation 직접 baseline과는 결이 다름.

## 7. 우리가 빌릴 수 있는 것

- framing: 첫 출력이 최선이 아니다 / inference-time 개선 / 과제별로 reflection 이득이 다르다.
- baseline: `single-pass`, `Self-Refine(k iterations)`를 reflection macro-strategy baseline으로. parallel SC와 budget-matched 비교.
- metric: 품질 + **iteration 수/생성 token(cost)** 동시 보고.
- ablation: reflection iteration 수 sweep, 과제별 reflection 이득(특히 math vs 비-math), parallel(SC) vs sequential(refine) 비교.
- terminology: `self-feedback`, `iterative refinement`, `generator/feedback/refiner`, `stop condition`.

## 8. 우리가 하면 안 되는 주장

- `iterative self-refinement / reflection을 우리가 처음 제안한다`.
- `self-feedback 기반 개선이 우리 기여다`.
- `reflection은 (일반적으로) 효과 없다`(Self-Refine의 math 약세를 일반화 금지).
- reflection을 raw 성능 SOTA 경쟁으로 프레이밍.

## 9. baseline / ablation 반영 아이디어

- macro strategy card에 `self_refine_k`(reflection) 추가, parallel SC/Multiple-CoT와 같은 budget 곡선에서 비교.
- 과제·문제 난이도별로 reflection이 언제 이득인지(특히 GSM8K/MATH)와 STOP 시점 분석.
- "reflection 1회 더"의 한계 효용과 token budget tradeoff를 측정.
- reflection을 path-pool에 넣을 때 generation+feedback+refine cost를 TTC budget에 계상.

## 10. Related Work에 넣을 문장 초안

Self-Refine(Madaan et al., NeurIPS 2023)은 추가 학습이나 강화학습 없이 하나의 LLM이 생성자·피드백 제공자·정제자 역할을 모두 맡아 초기 출력을 생성하고 자기 피드백으로 반복 개선하는 iterative self-refinement 기법으로, GPT-3.5/GPT-4에서 대화·코드·수학 추론 등 7개 과제의 출력 품질을 평균적으로 향상시켰다. 다만 수학 추론(GSM8K)에서는 향상 폭이 제한적이어서, 자기 정제의 이득이 과제에 따라 달라짐을 보여준다.

본 연구는 self-refinement 자체를 새 기여로 두지 않는다. 우리는 reflection/iterative refinement를 macro strategy 후보 중 하나로 포함하되, 제한된 test-time compute 안에서 어떤 heterogeneous reasoning path family를 추가로 획득하고 언제 STOP하며 어떤 voting/verification으로 최종 답을 결정할지를 다루는 **state-conditioned path-pool acquisition과 budget allocation** 문제에 위치한다. 또한 Self-Refine의 수학 과제 약세를 일반화하지 않고, reflection을 budget-matched로 parallel sampling과 공정 비교한다.

## 11. 현재 우선순위와 다음 액션

- 현재 우선순위: `P1`
- 위협도: 중간 (reflection claim boundary; 직접 baseline 경쟁은 아님)
- 구현 결정: full reproduction 비대상. reflection을 macro strategy card(`self_refine_k`)로 도입해 budget-matched 비교에만 활용.
- 지금 할 일:
  - Self-Refine를 Reflexion과 함께 reflection/self-feedback cluster의 P1 reference로 고정.
  - `reflection/self-refinement 자체를 novelty로 쓰지 않기`, `reflection 무효 일반화 금지` wording 가드.
  - reflection cost를 TTC budget에 계상.
- 나중으로 미뤄도 되는 일: Self-Refine full 재현, 7개 과제 평가.
- 한 줄 결론: Self-Refine는 reflection을 선점한 macro-strategy reference이며, 우리 기여는 reflection loop 자체가 아니라 heterogeneous path-pool acquisition·STOP·budget allocation임을 분명히 하는 데 쓴다.
