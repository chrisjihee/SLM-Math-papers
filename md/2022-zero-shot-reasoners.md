# Large Language Models are Zero-Shot Reasoners review

## 1. Metadata

- Title: Large Language Models are Zero-Shot Reasoners
- Authors: Takeshi Kojima, Shixiang Shane Gu, Machel Reid, Yutaka Matsuo, Yusuke Iwasawa (The University of Tokyo / Google Research, Brain Team)
- Year: 2022
- Venue / Status: NeurIPS 2022 (arXiv 2205.11916)
- Links:
  - Paper: https://arxiv.org/abs/2205.11916
  - GitHub / Code (official): https://github.com/kojima-takeshi188/zero_shot_cot
- Source PDF (local, source-of-record): `paper/2022-zero-shot-reasoners.pdf`
- Source Grounding Log:
  - PDF: `paper/2022-zero-shot-reasoners.pdf` — 42 pages, sha256 `43a3d73c77c7f3e115bb85522a4d94aaa54cdb55a0d9e17eb6af3117f39111c7`, pypdf/pymupdf 본문 추출 정상(약 129k자). venue("36th Conference on Neural Information Processing Systems")·title·authors·abstract·method·benchmarks·code 직접 확인.
  - arXiv abstract: arXiv id·subjects 확인.
  - TeX source/ar5iv: 미사용(PDF로 충분).
- Paper Type: `inference-time` / `prompting` / `zero-shot CoT (minimal reasoning prompt)` origin baseline reference
- Reading Status: `strategically-read`
- Current Priority: `P1`

## 2. One-line Summary

이 논문은 답 앞에 "Let's think step by step" 한 줄을 붙이는 것만으로 LLM이 exemplar 없이 multi-step reasoning을 수행함을 보인 Zero-shot-CoT의 원형으로, 단일 task-agnostic prompt로 MultiArith·GSM8K 등에서 standard zero-shot 대비 큰 향상을 달성했다.

## 3. 핵심 문제 설정

- 문제: few-shot CoT는 과제별 manual exemplar가 필요하다. **exemplar 없이도** LLM의 multi-step reasoning을 끌어낼 수 있는가?
- 해법: **Zero-shot-CoT** — answer 앞에 "Let's think step by step"를 붙이는 2단계 prompting(① reasoning 생성, ② answer 추출). 단일 prompt가 모든 과제에 task-agnostic하게 적용.
- 내 연구와의 연결: 이 논문은 **zero-shot reasoning prompt("Let's think step by step")의 원형**이다. 우리 연구에서 zero-shot-CoT는 새 기여가 아니라 **가장 기본적인 CoT family / prompt-diversity anchor**이며, 핵심은 budget 하 path-family 선택·중단이다.

## 4. 핵심 방법

- Zero-shot-CoT: ① "Q: … A: Let's think step by step." 로 reasoning을 생성, ② 생성된 reasoning에 answer-extraction prompt를 붙여 최종 답 추출.
- 학습: 없음(zero-shot, exemplar 없음, single task-agnostic template).
- selection unit: **단일 minimal prompt 적용**. heterogeneous path-family 선택/budget allocation/STOP은 아님.
- 실험(PDF 본문):
  - model: **InstructGPT text-davinci-002**(주), GPT-3, PaLM 540B.
  - benchmarks: arithmetic(MultiArith, **GSM8K**, AQUA-RAT, SVAMP), symbolic(Last Letter, Coin Flip), commonsense 등.
  - 결과: standard zero-shot 대비 큰 향상(예: MultiArith·GSM8K). reasoning은 model scale에서 emergent.

## 5. SLM-Math 관점의 재해석

- 이 논문은 직접 baseline 경쟁자라기보다 **zero-shot-CoT origin / prompt-diversity anchor reference**다.
- 공통점: 추가 학습 없이 prompt로 reasoning 유도, "단계적으로 생각".
- 차이점:
  - Zero-shot-CoT는 **단일 minimal prompt 고정**. 우리는 `direct / zero-shot-CoT / few-shot CoT / prompt-diverse CoT / plan-first / decompose-first / PAL/PoT / CG / verifier-guided` 중 **무엇을 언제 쓸지**(거시).
  - 큰 모델(InstructGPT/PaLM) zero-shot. 우리는 small LM + budget(작은 모델에선 zero-shot-CoT 이득이 약할 수 있음).
- 연결: zero-shot-CoT를 우리 path family의 **하한/anchor baseline**으로 두고, few-shot CoT·prompt-diverse CoT와 함께 prompt-diversity 축을 구성.

## 6. 우리 연구에 대한 novelty risk

- **zero-shot reasoning prompt / "Let's think step by step" / exemplar 없는 reasoning 유도**를 이미 선점 → 이 자체를 우리 novelty로 쓰면 충돌.
- "minimal prompt로 reasoning이 emergent하다"는 관찰도 선점.
- 위험 framing: `zero-shot-CoT/step-by-step prompting이 우리 기여`, `prompt로 reasoning을 유도`.
- 단, Zero-shot-CoT는 단일 prompt(미시)라 inference-time allocation 직접 baseline과는 결이 다름.

## 7. 우리가 빌릴 수 있는 것

- framing: exemplar 없이 reasoning 유도 / minimal prompt anchor / reasoning의 scale-dependence.
- baseline: `direct`, `Zero-shot-CoT`, `few-shot CoT`, `prompt-diverse CoT`를 prompt family로 같은 budget 곡선에서 비교.
- metric: accuracy + 생성 token(cost) + model scale별 곡선(특히 small LM에서 zero-shot-CoT 이득 약화).
- ablation: zero-shot vs few-shot CoT, prompt template 변형(다양성), answer-extraction 방식.
- terminology: `zero-shot-CoT`, `Let's think step by step`, `task-agnostic prompt`, `reasoning/answer extraction`.

## 8. 우리가 하면 안 되는 주장

- `zero-shot step-by-step prompting을 우리가 새롭게 제안한다`.
- `"Let's think step by step" / zero-shot reasoning prompt가 우리 기여다`.
- `minimal prompt로 reasoning이 유도됨을 우리가 처음 보였다`.
- Zero-shot-CoT 대비 raw 성능 SOTA 경쟁, prompt family를 단순 prompt engineering으로 정당화.

## 9. baseline / ablation 반영 아이디어

- `Zero-shot-CoT`를 path family의 minimal/anchor baseline으로 고정하고, few-shot CoT·prompt-diverse CoT와 prompt-diversity 축에서 비교.
- small LM scale에서 zero-shot-CoT 이득이 약화되는 지점을 보여, heterogeneous pool·strategy 선택의 필요성을 동기화.
- prompt-diversity 이득과 구조(structure) 이득을 분리하는 ablation(CoT 노트와 연동).
- zero-shot-CoT cost(2단계 generation)를 TTC budget에 계상.

## 10. Related Work에 넣을 문장 초안

Kojima et al.(NeurIPS 2022)의 Large Language Models are Zero-Shot Reasoners는 답 앞에 "Let's think step by step"라는 단일 task-agnostic prompt를 추가하는 것만으로 LLM이 exemplar 없이 multi-step reasoning을 수행함을 보여, Zero-shot-CoT의 원형을 제시했다. 이 방법은 InstructGPT·PaLM에서 MultiArith·GSM8K 등 arithmetic·symbolic 과제의 zero-shot 성능을 크게 향상시켰다.

본 연구는 zero-shot-CoT나 step-by-step prompting 자체를 새 기여로 두지 않는다. 우리는 zero-shot-CoT를 reasoning path family의 가장 기본적인 anchor/prompt-diversity baseline으로 삼고, 제한된 test-time compute 안에서 현재 reasoning state·budget을 바탕으로 어떤 heterogeneous reasoning path family/strategy를 추가로 획득하고 언제 STOP하며 어떤 voting/verification으로 답을 정할지를 다루는 **state-conditioned path-pool acquisition과 budget allocation**에 위치한다. 특히 작은 모델에서는 zero-shot-CoT의 이득이 약화될 수 있으므로 path-pool 구성의 필요성이 커진다.

## 11. 현재 우선순위와 다음 액션

- 현재 우선순위: `P1`
- 위협도: 낮음~중간 (origin/anchor baseline; claim 정의 측면에서 중요)
- 구현 결정: full reproduction 비대상. zero-shot-CoT를 path family anchor baseline으로 고정.
- 지금 할 일:
  - 이 논문을 CoT/Least-to-Most/Plan-and-Solve와 함께 prompt-family/structured prompting cluster의 P1 anchor reference로 고정(positioning은 decomposition·planning 공통 항목으로 처리).
  - `zero-shot step-by-step prompting 자체를 novelty로 쓰지 않기` wording 가드.
  - small LM에서 zero-shot-CoT 이득 약화 곡선 확보(heterogeneous pool 동기화).
- 나중으로 미뤄도 되는 일: 전체 benchmark sweep, PaLM/InstructGPT scale 재현.
- 한 줄 결론: Zero-shot-CoT origin은 우리가 새로 제안할 대상이 아니라 prompt-family anchor baseline으로 고정하고, 우리 기여를 budget 하 heterogeneous path-family acquisition·STOP으로 분리하는 데 쓴다.
