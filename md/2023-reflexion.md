# Reflexion: Language Agents with Verbal Reinforcement Learning review

## 1. Metadata

- Title: Reflexion: Language Agents with Verbal Reinforcement Learning
- Authors: Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao (Northeastern University / MIT / Princeton University)
- Year: 2023
- Venue / Status: NeurIPS 2023 (arXiv 2303.11366)
- Links:
  - Paper: https://arxiv.org/abs/2303.11366
  - GitHub / Code (official): https://github.com/noahshinn024/reflexion
- Source PDF (local, source-of-record): `paper/2023-reflexion.pdf`
- Source Grounding Log:
  - PDF: `paper/2023-reflexion.pdf` — 19 pages, sha256 `6059b6f89fea9959bd3dab553fbb97756a3dfb1b15e3cbab2fbf3ab6664333bd`, pypdf/pymupdf 본문 추출 정상(약 59k자). title/authors/abstract/method/tasks/code 직접 확인.
  - arXiv abstract: 저자·arXiv id·official code(github.com/noahshinn024/reflexion) 확인.
  - TeX source/ar5iv: 미사용(PDF로 충분).
  - 주의: venue(NeurIPS 2023)는 외부 확정 사실로 기록.
- Paper Type: `inference-time` / `agentic` / `verbal RL (reflection + episodic memory)` baseline reference
- Reading Status: `strategically-read`
- Current Priority: `P1`

## 2. One-line Summary

Reflexion은 모델 weight를 업데이트하지 않고, language agent가 task feedback에 대해 **자연어로 self-reflect한 텍스트를 episodic memory에 저장**해 다음 trial의 의사결정을 개선하는 verbal reinforcement learning framework으로, ALFWorld·HotPotQA·HumanEval에서 강한 agent baseline을 넘었다.

## 3. 핵심 문제 설정

- 문제: language agent가 trial-and-error로 빠르게 학습하려면 보통 많은 샘플과 비싼 fine-tuning이 필요하다. **weight 업데이트 없이** inference-time 언어 피드백만으로 개선할 수 있는가?
- 해법: agent가 (Actor가 행동→Evaluator가 피드백→Self-Reflection이 자연어 반성 생성)을 거쳐 **reflective text를 episodic memory buffer에 누적**, 이후 trial에서 그 memory를 context로 활용.
- 내 연구와의 연결: Reflexion은 **reflection을 단순 prompt baseline이 아니라 feedback·memory 기반 reasoning strategy로 선점**했다. 우리 연구에서 reflection은 macro strategy 후보일 뿐, 핵심은 제한된 TTC 안의 path-family 획득·STOP·verification이다.

## 4. 핵심 방법

- 구성요소: **Actor**(행동/출력 생성), **Evaluator**(task feedback/보상 신호), **Self-Reflection model**(자연어 반성 생성), **episodic memory**(반성 누적).
- 학습: **weight update 없음**(verbal/linguistic reinforcement). 외부 환경 feedback(게임·컴파일러·정답 등)을 신호로 사용.
- selection unit: **trial 단위 반복 + memory 축적**(agentic). heterogeneous path-family 선택이나 budget allocation은 아님.
- 실험(PDF 본문):
  - model: **GPT-3.5, GPT-4**.
  - tasks: ALFWorld(decision-making), **HotPotQA(reasoning, +20%)**, **HumanEval(coding, 91% pass@1, GPT-4 80% 상회)**.
  - 의존: Evaluator/feedback 신호 품질에 성능이 크게 의존(외부 환경/정답 필요).

## 5. SLM-Math 관점의 재해석

- Reflexion은 직접 baseline 경쟁자라기보다 **reflection+memory 기반 verbal-RL의 대표 reference**다.
- 공통점: weight 학습 없이 inference-time 행동 변경, "여러 trial로 개선".
- 차이점:
  - Reflexion은 **외부 환경 feedback + episodic memory + 다회 trial**(agentic). 우리는 **단일 budget 안의 path-pool 구성·STOP**(non-agentic, 제한 TTC).
  - Reflexion의 reasoning 평가는 HotPotQA(QA)·게임·코딩 중심. 우리 mainline은 GSM8K/MATH word problem.
  - math에서는 외부 환경 보상이 없어 Evaluator를 answer-checking/self-eval로 대체해야 함 → reflection 신호 비용·신뢰도가 별도 이슈.
- 연결: reflection을 macro strategy card(`reflexion_like_retry`)로 포함하되, **memory/다회 trial cost를 TTC budget에 계상**하고 single-budget parallel sampling과 공정 비교.

## 6. 우리 연구에 대한 novelty risk

- **verbal feedback / self-reflection / episodic memory / trial-and-error 개선**을 이미 선점 → 이 자체를 우리 novelty로 쓰면 충돌.
- "RL 없이 언어 피드백으로 강화" 아이디어도 선점.
- 위험 framing: `reflection/verbal-RL이 우리 기여`, `memory 기반 self-improvement를 도입`.
- 단, Reflexion은 agentic multi-trial(미시·환경의존)이라 우리 inference-time path-allocation과 결이 다름.

## 7. 우리가 빌릴 수 있는 것

- framing: weight update 없는 inference-time 개선 / feedback 신호 품질이 성능을 좌우 / reflection을 메모리 기반 strategy로 형식화.
- baseline: reflection macro-strategy(`reflexion-like`)를 parallel SC/Multiple-CoT와 budget-matched 비교.
- metric: success/accuracy + **trial 수·memory token·총 LM call(cost)** 동시 보고.
- ablation: trial 수 sweep, feedback 신호 종류(정답/self-eval), reflection on/off, parallel vs sequential.
- terminology: `verbal reinforcement`, `self-reflection`, `episodic memory`, `Actor/Evaluator/Self-Reflection`, `trial-and-error`.

## 8. 우리가 하면 안 되는 주장

- `verbal feedback / memory-based reflection을 우리가 처음 제안한다`.
- `reflection/self-improvement가 우리 핵심 기여다`.
- `reflection은 (일반적으로) 효과 없다`(과제·feedback 의존, 일반화 금지).
- Reflexion 대비 raw 성능 SOTA 경쟁.

## 9. baseline / ablation 반영 아이디어

- macro strategy card에 `reflexion_like_retry`(feedback+memory) 추가, single-budget parallel과 budget-matched 비교.
- math에서 Evaluator를 answer-checking/self-eval로 둘 때 reflection 신호의 비용·신뢰도 분석.
- reflection 다회 trial의 한계 효용과 token/LM-call budget tradeoff 측정.
- reflection(memory) cost를 TTC budget에 계상.

## 10. Related Work에 넣을 문장 초안

Reflexion(Shinn et al., NeurIPS 2023)은 모델 가중치를 갱신하지 않고 language agent가 task feedback에 대해 자연어로 self-reflect한 내용을 episodic memory에 저장하여 다음 trial의 의사결정을 개선하는 verbal reinforcement learning framework로, ALFWorld·HotPotQA·HumanEval에서 강한 agent baseline을 넘었다(예: HumanEval 91% pass@1). 이 연구는 reflection을 단순 prompt 기법이 아니라 feedback·memory 기반의 반복 학습 전략으로 자리매김했다.

본 연구는 verbal reinforcement나 memory 기반 self-reflection 자체를 새 기여로 두지 않는다. 우리는 reflection을 macro strategy 후보 중 하나로만 포함하고, 제한된 test-time compute 안에서 어떤 heterogeneous reasoning path family를 추가로 획득하고 언제 STOP하며 어떤 voting/verification으로 답을 정할지를 다루는 **state-conditioned path-pool acquisition과 budget allocation**에 위치한다. 또한 Reflexion이 외부 환경 feedback과 다회 trial에 의존하는 agentic 설정인 반면, 우리는 단일 budget 안의 비-agentic path 구성으로 구분되며, reflection의 memory/trial 비용을 TTC budget에 명시적으로 계상한다.

## 11. 현재 우선순위와 다음 액션

- 현재 우선순위: `P1`
- 위협도: 중간 (reflection/verbal-RL claim boundary; 직접 baseline 경쟁은 아님)
- 구현 결정: full reproduction 비대상. reflection을 macro strategy card로 도입해 budget-matched 비교에만 활용.
- 지금 할 일:
  - Reflexion을 Self-Refine과 함께 reflection/self-feedback cluster의 P1 reference로 고정.
  - `verbal feedback/memory-based reflection을 novelty로 쓰지 않기`, `reflection 무효 일반화 금지` wording 가드.
  - math 설정에서 feedback 신호(정답/self-eval) 대체와 그 비용을 명시, reflection cost를 TTC budget에 계상.
- 나중으로 미뤄도 되는 일: Reflexion full agentic 재현, ALFWorld/HotPotQA/HumanEval 평가.
- 한 줄 결론: Reflexion은 reflection+memory 기반 verbal-RL을 선점한 reference이며, 우리 기여는 reflection 자체가 아니라 heterogeneous path-pool acquisition·STOP·budget allocation임을 분명히 하는 데 쓴다.
