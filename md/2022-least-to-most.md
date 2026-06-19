# Least-to-Most Prompting Enables Complex Reasoning in Large Language Models review

## 1. Metadata

- Title: Least-to-Most Prompting Enables Complex Reasoning in Large Language Models
- Authors: Denny Zhou, Nathanael Schärli, Le Hou, Jason Wei, Nathan Scales, Xuezhi Wang, Dale Schuurmans, Claire Cui, Olivier Bousquet, Quoc Le, Ed Chi (Google Research, Brain Team)
- Year: 2022 (citation 기준 arXiv 공개; venue ICLR 2023)
- Venue / Status: ICLR 2023 (arXiv 2205.10625, v1 2022-05)
- Links:
  - Paper: https://arxiv.org/abs/2205.10625
  - GitHub / Code (official): 없음 (prompting 기법)
- Source PDF (local, source-of-record): `paper/2022-least-to-most.pdf`
- Source Grounding Log:
  - PDF: `paper/2022-least-to-most.pdf` — 61 pages, sha256 `ab71759f86119d1c368cef0ffabc5499562b605188a5dd6a00ed7ca0fa995c71`, pypdf/pymupdf 본문 추출 정상(약 203k자). venue("Published as a conference paper at ICLR 2023")·title·authors·abstract·method·benchmarks 직접 확인.
  - arXiv abstract: arXiv id·subjects 확인.
  - TeX source/ar5iv: 미사용(PDF로 충분).
  - official code: 없음(code_url 빈 값).
- Paper Type: `inference-time` / `prompting` / `decomposition (decompose-first) structured prompting` baseline reference
- Reading Status: `strategically-read`
- Current Priority: `P1`

## 2. One-line Summary

Least-to-Most Prompting은 복잡한 문제를 더 쉬운 subproblem들의 sequence로 분해하고 이전 답을 활용해 순차적으로 푸는 decompose-first prompting으로, exemplar보다 어려운 문제(easy-to-hard generalization)에서 CoT보다 강함을 GSM8K·DROP·SCAN에서 보였다.

## 3. 핵심 문제 설정

- 문제: CoT는 prompt exemplar보다 **어려운 문제(harder than exemplars)** 에서 성능이 빠르게 떨어진다(easy-to-hard generalization 한계).
- 해법: **decompose-first** — 문제를 simpler subproblem 시퀀스로 분해(1단계)한 뒤, 각 subproblem을 이전 답을 이용해 순차적으로 해결(2단계). 둘 다 few-shot prompting.
- 내 연구와의 연결: Least-to-Most는 **decomposition / planning 기반 structured prompting을 선점**했다. 우리 연구에서 decompose-first는 새 기여가 아니라 **macro strategy card 후보 중 하나**이며, 핵심은 제한된 TTC 안에서 어떤 path family/strategy를 언제 쓸지다.

## 4. 핵심 방법

- 2단계: (1) **decomposition** prompt로 subproblem 리스트 생성, (2) **sequential solving** — 각 subproblem을 이전 subproblem의 답을 컨텍스트에 넣어 차례로 해결.
- 학습: 없음(few-shot prompting only).
- selection unit: **subproblem 분해 + 순차 해결**(단일 strategy). heterogeneous path-family 선택/budget allocation/STOP은 아님.
- 실험(PDF 본문):
  - model: **GPT-3 code-davinci-002** 중심.
  - benchmarks: **GSM8K(math), DROP(reading/arithmetic), SCAN(compositional generalization, length split에서 99%+)**.
  - 결과: 어려운 문제로 갈수록 CoT 대비 우위 확대(easy-to-hard generalization).

## 5. SLM-Math 관점의 재해석

- Least-to-Most는 직접 baseline 경쟁자라기보다 **decompose-first macro-strategy의 대표 reference**다.
- 공통점: 추가 학습 없이 prompting으로 reasoning 구조 변경, "한 방에 풀지 않고 단계화".
- 차이점:
  - Least-to-Most는 **단일 decompose-first strategy를 고정 적용**. 우리는 `direct / CoT / prompt-diverse CoT / decompose-first / plan-first / PAL/PoT / CG / verifier-guided` 중 **무엇을 언제 추가 획득할지**(거시).
  - 단일 큰 모델(GPT-3) 중심. 우리는 small LM + budget.
- 연결: decompose-first를 우리 macro strategy card(`decompose_first`)로 포함하고, prompt-diverse CoT family와 함께 budget-matched로 비교.
- 주의: 우리 CoT_Lv1/Lv2/Lv3·strategy card가 **단순 prompt engineering으로 보일 위험** → 차별점은 "어떤 prompt family를 현재 state·budget에서 선택·중단할지"라는 의사결정 문제임을 강조.

## 6. 우리 연구에 대한 novelty risk

- **decomposition / 문제 분해 / planning 기반 structured prompting**을 이미 선점 → 이 자체를 우리 novelty로 쓰면 충돌.
- "어려운 문제를 쉬운 subproblem으로 나눠 푼다"는 관찰도 선점.
- 위험 framing: `decompose-first/planning prompt가 우리 기여`, `structured prompting을 도입`.
- 단, Least-to-Most는 단일 prompt strategy(미시)라 inference-time allocation 직접 baseline과는 결이 다름.

## 7. 우리가 빌릴 수 있는 것

- framing: easy-to-hard generalization / exemplar보다 어려운 문제에서의 취약성 / 분해의 효용.
- baseline: `CoT`, `decompose-first(Least-to-Most)`, `plan-first`를 prompt/strategy family로 같은 budget 곡선에서 비교.
- metric: accuracy + 난이도(문제 크기)별 성능 곡선 + 생성 token(cost).
- ablation: decompose-first on/off, 문제 난이도별 strategy별 이득(prompt-diverse vs decompose vs plan).
- terminology: `decompose-first`, `subproblem decomposition`, `sequential solving`, `easy-to-hard generalization`.

## 8. 우리가 하면 안 되는 주장

- `decomposition / planning prompting을 우리가 처음 제안한다`.
- `decompose-first / structured prompting이 우리 핵심 기여다`.
- `문제 분해가 어려운 문제에 좋다는 것을 우리가 처음 보였다`.
- Least-to-Most 대비 raw 성능 SOTA 경쟁, strategy card를 단순 prompt engineering으로 정당화.

## 9. baseline / ablation 반영 아이디어

- macro strategy card에 `decompose_first` 추가, prompt-diverse CoT/`plan_first`와 같은 budget 곡선 비교.
- 문제 난이도별로 어떤 strategy card가 유리한지(easy-to-hard) 분석 → state-conditioned 선택 동기화.
- decompose-first의 추가 generation cost(분해+순차 해결)를 TTC budget에 계상.
- prompt-diversity 이득과 strategy(decompose) 이득을 분리하는 ablation(CoT 노트와 연동).

## 10. Related Work에 넣을 문장 초안

Least-to-Most Prompting(Zhou et al., ICLR 2023)은 복잡한 문제를 더 쉬운 subproblem들의 시퀀스로 분해한 뒤 이전 답을 활용해 순차적으로 푸는 decompose-first prompting으로, exemplar보다 어려운 문제에서 chain-of-thought보다 강한 easy-to-hard generalization을 GSM8K·DROP·SCAN에서 보였다. 이 연구는 decomposition·planning 기반 structured prompting의 대표적 baseline이다.

본 연구는 decomposition이나 planning prompting 자체를 새 기여로 두지 않는다. 우리는 decompose-first를 macro strategy 후보(strategy card) 중 하나로만 포함하고, 제한된 test-time compute 안에서 현재 reasoning state와 남은 budget을 바탕으로 어떤 heterogeneous reasoning path family/strategy를 추가로 획득하고 언제 STOP하며 어떤 voting/verification으로 답을 정할지를 다루는 **state-conditioned macro strategy allocation**에 위치한다. 즉 prompt family/strategy card는 단순 prompt engineering이 아니라 budget 하의 선택·중단 의사결정 단위로 다룬다.

## 11. 현재 우선순위와 다음 액션

- 현재 우선순위: `P1`
- 위협도: 중간 (decomposition/planning claim boundary; 직접 baseline 경쟁은 아님)
- 구현 결정: full reproduction 비대상. decompose-first를 strategy card로 도입해 budget-matched 비교에 활용.
- 지금 할 일:
  - Least-to-Most를 Plan-and-Solve·Self-Discover와 함께 structured prompting / decomposition cluster의 P1 reference로 고정.
  - `decomposition/planning prompt 자체를 novelty로 쓰지 않기` wording 가드, strategy card를 단순 prompt engineering으로 보이지 않게 의사결정 문제로 프레이밍.
  - decompose-first cost를 TTC budget에 계상.
- 나중으로 미뤄도 되는 일: Least-to-Most full 재현, SCAN/DROP 평가.
- 한 줄 결론: Least-to-Most는 decompose-first structured prompting을 선점한 reference이며, 우리 기여는 분해/계획 prompt 자체가 아니라 budget 하 macro strategy allocation·STOP임을 분명히 하는 데 쓴다.
