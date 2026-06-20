# Phased Instruction Fine-Tuning for Large Language Models review

## 1. Metadata

- Title: Phased Instruction Fine-Tuning for Large Language Models
- Authors: Wei Pang, Chuan Zhou, Xiao-Hua Zhou, Xiaojie Wang (Beijing University of Posts and Telecommunications / Peking University)
- Year: 2024
- Venue / Status: ACL 2024 Findings (pp. 5735–5748; arXiv 2406.04371)
- Links:
  - Paper: https://aclanthology.org/2024.findings-acl.341/ / https://arxiv.org/abs/2406.04371
  - GitHub / Code (official): https://github.com/xubuvd/PhasedSFT
- Source PDF (local, source-of-record): `paper/2024-phased-instruction-ft.pdf`
- Source Grounding Log:
  - PDF: `paper/2024-phased-instruction-ft.pdf` — 14 pages, sha256 `fa8c89918d11454aad6db577eac98ef580cd40ec50e46b360a48b2e533a86b9d`(legacy `paper/03. ….pdf`의 canonical 복사본, 동일 sha256, legacy 보존), pypdf/pymupdf 본문 추출 정상(약 50k자). venue("Findings of ACL 2024")·title·authors·abstract·method·models·code 직접 확인.
  - legacy 자료: `reading/03`, `contents/03` 존재(보조). source-of-record는 PDF 재추출.
  - TeX source/ar5iv: 미사용.
- Paper Type: `training` / `instruction tuning (phased/staged easy-to-hard curriculum)` — instruction-tuning curriculum boundary reference
- Reading Status: `strategically-read`
- Current Priority: `P1`

## 2. One-line Summary

Phased IFT는 instruction following 학습이 점진적 과정이라는 가정 아래, GPT-4로 instruction 난이도를 평가해 데이터를 난이도 증가 subset으로 나눈 뒤 easy-to-hard로 단계적으로 fine-tune하여, 한 번에 모든 난이도를 섞어 학습하는 One-off IFT보다 instruction-following을 개선한 staged instruction-tuning 논문이다.

## 3. 핵심 문제 설정

- 문제: 기존 **One-off IFT**는 다양한 난이도의 instruction을 동시에 학습해, instruction 준수 능력을 효과적으로 끌어올리지 못할 수 있다.
- 해법: **Phased IFT** — GPT-4로 instruction 난이도를 평가 → 난이도 증가 subset 분할 → **단계적(easy-to-hard) fine-tuning**(curriculum).
- 내 연구와의 연결: Phased IFT는 **phased/staged instruction tuning / training curriculum을 선점**했다. 우리 연구는 **training phase 설계가 아니라 inference-time path-pool control**임을 명확히 해야 한다. (특히 "난이도 기반"이라는 점에서 우리 difficulty/state-conditioned **test-time** allocation과 혼동되지 않게 분리.)

## 4. 핵심 방법

- 난이도 평가: GPT-4로 각 instruction의 난이도 점수화.
- subset 분할: 난이도 증가 순으로 데이터 분할.
- staged fine-tuning: easy→hard 순으로 phase별 fine-tune(점진적 curriculum).
- 학습: training-heavy(instruction tuning curriculum). test-time 제어/search/verifier 없음.
- selection unit: **instruction subset / training phase(학습 supervision)**. heterogeneous path-family 선택/budget allocation/STOP은 아님.
- 실험: Llama-2 7B/13B/70B, Llama3 8/70B, Mistral-7B; Alpaca data. One-off IFT 대비 향상.

## 5. SLM-Math 관점의 재해석

- Phased IFT는 직접 baseline 경쟁자라기보다 **instruction-tuning curriculum의 대표 reference이자 boundary**다.
- 공통점: **난이도(difficulty)** 를 활용(우리 difficulty/state-conditioned 관심과 표면적으로 닿음).
- 차이점(핵심):
  - Phased IFT는 **training-time easy-to-hard curriculum(난이도 기반 학습 순서)**. 우리는 **inference-time difficulty/state-conditioned path-pool allocation(난이도 기반 추론 시점 배분)**.
  - Phased IFT의 단위는 training phase/subset. 우리는 path family / macro strategy / STOP.
- 연결: "난이도 기반 학습 curriculum"(Phased IFT)과 "난이도/state 기반 test-time allocation"(우리)을 명확히 분리. 둘 다 difficulty를 쓰지만 적용 시점(training vs inference)이 다름.

## 6. 우리 연구에 대한 novelty risk

- **phased/staged instruction tuning / training curriculum / 난이도 기반 학습 순서**를 이미 선점 → 이 자체를 우리 novelty로 쓰면 충돌.
- "난이도에 따라 학습/처리를 단계화하면 좋아진다"는 관찰도(training 측에서) 선점.
- 위험 framing: `phased training curriculum이 우리 기여`, `난이도 기반 단계화를 우리가 한다`(training과 inference 혼동).
- 단, Phased IFT는 training-time curriculum이라 우리 inference-time allocation과 결이 다름 — **이 분리를 명문화하지 않으면 difficulty 기반 아이디어가 겹쳐 보임**.

## 7. 우리가 빌릴 수 있는 것

- framing: instruction-following 학습의 점진성, 난이도 평가(GPT-4 scoring), easy-to-hard.
- baseline: Phased IFT로 학습한 backbone을 우리 orchestration의 fixed backbone 후보로(경쟁 아님).
- metric: instruction-following win rate — training-time gain과 inference-time gain 분해.
- ablation: 난이도 평가 방식, phase 수, easy-to-hard vs random — 우리 test-time difficulty 분석과 대비(시점 분리).
- terminology: `phased/staged fine-tuning`, `instruction difficulty`, `easy-to-hard curriculum`, `One-off IFT`.

## 8. 우리가 하면 안 되는 주장

- `phased/staged instruction tuning / training curriculum을 우리가 처음 제안한다`.
- `난이도 기반 단계화가 우리 기여다`(특히 training vs inference 시점 혼동).
- `instruction tuning을 개선하는 것이 우리 핵심 기여다`.
- difficulty 기반 test-time allocation을 Phased IFT의 training curriculum과 동일시.

## 9. baseline / ablation 반영 아이디어

- "난이도 기반 training curriculum"(Phased IFT)과 "난이도/state 기반 test-time allocation"(우리)을 명시적으로 분리하는 framing/ablation.
- instruction tuning(curriculum 포함)은 backbone 확보 수단으로만, 비교 중심은 fixed backbone 위 test-time path-pool.
- 난이도 추정(우리 state-conditioned policy)의 시점이 inference임을 명문화(Learning-How-Hard·Scaling-TTC 노트와 연동).

## 10. Related Work에 넣을 문장 초안

Phased Instruction Fine-Tuning(Pang et al., Findings of ACL 2024)은 instruction following 학습이 점진적 과정이라는 가정 아래, GPT-4로 instruction 난이도를 평가해 데이터를 난이도 증가 subset으로 나누고 easy-to-hard로 단계적으로 fine-tune하는 phased instruction tuning을 제안하여, 모든 난이도를 한 번에 학습하는 One-off IFT보다 instruction-following을 개선했다.

본 연구는 phased/staged instruction tuning이나 난이도 기반 training curriculum 자체를 새 기여로 두지 않는다. Phased IFT가 training 시점에 난이도 기반 학습 순서를 설계하는 반면, 우리는 fixed/given backbone 위에서 추론 시점에 문제별 reasoning state와 난이도를 보고 어떤 heterogeneous path family를 추가로 획득하고 언제 멈출지를 결정하는 **state-conditioned test-time path-pool allocation**에 위치한다. 즉 둘 다 난이도를 활용하지만 적용 시점(training vs inference)이 본질적으로 다르다.

## 11. 현재 우선순위와 다음 액션

- 현재 우선순위: `P1`
- 위협도: 낮음~중간 (instruction-tuning curriculum claim boundary; difficulty 시점 혼동 방지가 핵심; 직접 baseline 경쟁은 아님)
- 구현 결정: full reproduction 비대상. instruction tuning은 backbone 확보 수단으로만.
- 지금 할 일:
  - Phased IFT를 Self-Instruct와 함께 instruction-tuning boundary로 P1 reference 고정.
  - `phased training curriculum / 난이도 기반 단계화 자체를 novelty로 쓰지 않기`, `training-time curriculum과 test-time allocation을 분리` wording 가드.
  - 우리 difficulty 추정의 시점이 inference임을 명문화.
- 나중으로 미뤄도 되는 일: Phased IFT 재현, instruction-following 평가.
- 한 줄 결론: Phased IFT는 난이도 기반 training curriculum을 선점한 reference이며, 우리 기여를 training-time phase 설계가 아니라 inference-time state-conditioned path-pool allocation으로 분리(difficulty 시점 분리)하게 만드는 P1 reference다.
