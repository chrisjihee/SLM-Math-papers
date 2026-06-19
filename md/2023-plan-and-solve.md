# Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models review

## 1. Metadata

- Title: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models
- Authors: Lei Wang, Wanyu Xu, Yihuai Lan, Zhiqiang Hu, Yunshi Lan, Roy Ka-Wei Lee, Ee-Peng Lim (Singapore Management Univ / Southwest Jiaotong Univ / SUTD / East China Normal Univ)
- Year: 2023
- Venue / Status: ACL 2023 (arXiv 2305.04091)
- Links:
  - Paper: https://arxiv.org/abs/2305.04091
  - GitHub / Code (official): https://github.com/AGI-Edgerunners/Plan-and-Solve-Prompting
- Source PDF (local, source-of-record): `paper/2023-plan-and-solve.pdf`
- Source Grounding Log:
  - PDF: `paper/2023-plan-and-solve.pdf` — 24 pages, sha256 `cc65b7ad233da4f46a673c0045ee2c0ab332948d86b3f401ba97345d650abf04`, pypdf/pymupdf 본문 추출 정상(약 69k자). title/authors/abstract/method/code 직접 확인.
  - arXiv abstract: 저자·arXiv id·official code 확인.
  - TeX source/ar5iv: 미사용(PDF로 충분).
  - 주의: venue(ACL 2023)는 외부 확정 사실로 기록(PDF 텍스트 직접 미노출).
- Paper Type: `inference-time` / `prompting` / `zero-shot plan-first structured prompting` baseline reference
- Reading Status: `strategically-read`
- Current Priority: `P1`

## 2. One-line Summary

Plan-and-Solve(PS/PS+)는 Zero-shot-CoT("Let's think step by step")의 누락·계산 오류를 줄이기 위해 **먼저 계획을 세우고(plan) 그 계획을 단계별로 수행(solve)** 하도록 지시하는 zero-shot plan-first prompting으로, exemplar 없이 GPT-3에서 Zero-shot-CoT를 능가하고 일부 데이터셋에서 few-shot CoT에 근접했다.

## 3. 핵심 문제 설정

- 문제: Zero-shot-CoT는 manual exemplar를 없앴지만 **계산 오류·단계 누락·의미 오해**가 잦다.
- 해법: prompt를 **plan-first**로 바꿈 — "먼저 문제를 이해하고 계획을 세운 뒤, 계획을 단계별로 수행하라"(PS). PS+는 "변수/숫자 추출, 중간 결과 계산" 등 상세 지시를 더해 계산 오류를 줄임. 모두 zero-shot.
- 내 연구와의 연결: Plan-and-Solve는 **plan-first / zero-shot reasoning prompt를 선점**했다. 우리 연구에서 plan-first는 새 기여가 아니라 **CoT family 내부의 prompt-diversity 또는 macro strategy card 후보**이며, 핵심은 budget 하 strategy 선택·중단이다.

## 4. 핵심 방법

- PS: zero-shot trigger를 "Let's first understand the problem and devise a plan … Then carry out the plan and solve step by step"로 교체.
- PS+: 추가 지시(관련 변수·숫자 추출, 중간 계산 명시)로 계산 오류 완화.
- 학습: 없음(zero-shot, exemplar 없음).
- selection unit: **단일 prompt(plan-first) 적용**. heterogeneous path-family 선택/budget allocation/STOP은 아님.
- 실험(PDF 본문):
  - model: **GPT-3 text-davinci-003**.
  - baseline: **Zero-shot-CoT**; 데이터셋: arithmetic(GSM8K 등)·commonsense·symbolic.
  - 결과: PS/PS+가 Zero-shot-CoT를 능가, PS+는 일부 math에서 few-shot CoT에 근접.

## 5. SLM-Math 관점의 재해석

- Plan-and-Solve는 직접 baseline 경쟁자라기보다 **plan-first prompt family / macro-strategy의 대표 reference**다.
- 공통점: 추가 학습 없이 prompt로 reasoning 구조 변경.
- 차이점:
  - PS는 **단일 plan-first prompt 고정**. 우리는 `direct / CoT / prompt-diverse CoT / plan-first / decompose-first / PAL/PoT / CG / verifier-guided` 중 **무엇을 언제 쓸지**(거시).
  - 단일 큰 모델(GPT-3) zero-shot. 우리는 small LM + budget.
- 연결: plan-first를 우리 prompt family/strategy card(`plan_first`)로 포함하고, Least-to-Most(decompose-first)·Self-Discover와 함께 structured prompting cluster로 묶어 budget-matched 비교.

## 6. 우리 연구에 대한 novelty risk

- **plan-first / zero-shot reasoning prompt / planning 기반 prompting**을 이미 선점 → 이 자체를 우리 novelty로 쓰면 충돌.
- "계획을 먼저 세우면 zero-shot reasoning이 좋아진다"는 관찰도 선점.
- 위험 framing: `plan-first prompt가 우리 기여`, `prompt로 reasoning을 개선`.
- 단, PS는 단일 prompt strategy(미시)라 inference-time allocation 직접 baseline과는 결이 다름.

## 7. 우리가 빌릴 수 있는 것

- framing: zero-shot CoT의 오류 유형(계산/누락/의미) 분석 / plan-first의 효용.
- baseline: `Zero-shot-CoT`, `PS`, `PS+`, `few-shot CoT`를 prompt family로 같은 budget 곡선에서 비교.
- metric: accuracy + 오류 유형 분해 + 생성 token(cost).
- ablation: plan-first on/off, PS vs PS+(상세 지시) 효과, prompt-diverse vs plan-first vs decompose-first.
- terminology: `plan-first`, `devise a plan`, `zero-shot CoT`, `calculation/missing-step/semantic error`.

## 8. 우리가 하면 안 되는 주장

- `plan-first / planning prompting을 우리가 처음 제안한다`.
- `zero-shot reasoning prompt 개선이 우리 핵심 기여다`.
- `계획 수립 prompt가 reasoning을 개선함을 우리가 처음 보였다`.
- PS 대비 raw 성능 SOTA 경쟁, strategy card를 단순 prompt engineering으로 정당화.

## 9. baseline / ablation 반영 아이디어

- macro strategy card에 `plan_first`(PS/PS+) 추가, prompt-diverse CoT·`decompose_first`와 같은 budget 곡선 비교.
- zero-shot-CoT 오류 유형 분해를 우리 STOP/verification 설계의 진단 도구로 활용.
- plan-first의 추가 generation cost를 TTC budget에 계상.
- prompt-diversity 이득과 strategy(plan/decompose) 이득을 분리하는 ablation(CoT/Least-to-Most 노트와 연동).

## 10. Related Work에 넣을 문장 초안

Plan-and-Solve Prompting(Wang et al., ACL 2023)은 Zero-shot-CoT의 계산·누락·의미 오류를 줄이기 위해, 모델이 먼저 계획을 세우고 그 계획을 단계별로 수행하도록 지시하는 zero-shot plan-first prompting(PS/PS+)을 제안하여, exemplar 없이 GPT-3에서 Zero-shot-CoT를 능가하고 일부 수학 데이터셋에서 few-shot CoT에 근접했다. 이 연구는 plan-first·planning 기반 zero-shot structured prompting의 대표적 baseline이다.

본 연구는 plan-first나 planning prompting 자체를 새 기여로 두지 않는다. 우리는 plan-first를 CoT family 내부의 prompt-diversity 혹은 macro strategy 후보(strategy card)로만 포함하고, 제한된 test-time compute 안에서 현재 reasoning state·budget을 보고 어떤 strategy/path family를 추가로 획득하고 언제 STOP하며 어떤 voting/verification으로 답을 정할지를 다루는 **state-conditioned macro strategy allocation**에 위치한다. strategy card는 단순 prompt engineering이 아니라 budget 하 선택·중단 의사결정 단위로 다룬다.

## 11. 현재 우선순위와 다음 액션

- 현재 우선순위: `P1`
- 위협도: 중간 (plan-first/planning prompting claim boundary; 직접 baseline 경쟁은 아님)
- 구현 결정: full reproduction 비대상. plan-first(PS/PS+)를 strategy card로 도입해 budget-matched 비교에 활용.
- 지금 할 일:
  - Plan-and-Solve를 Least-to-Most·Self-Discover와 함께 structured prompting / planning cluster의 P1 reference로 고정(positioning은 decomposition·planning 공통 항목으로 처리).
  - `plan-first/planning prompting 자체를 novelty로 쓰지 않기` wording 가드, strategy card를 의사결정 문제로 프레이밍.
  - plan-first cost를 TTC budget에 계상.
- 나중으로 미뤄도 되는 일: PS/PS+ full 재현, 10개 데이터셋 평가.
- 한 줄 결론: Plan-and-Solve는 plan-first zero-shot prompting을 선점한 reference이며, 우리 기여는 계획/프롬프트 자체가 아니라 budget 하 macro strategy allocation·STOP임을 분명히 하는 데 쓴다.
