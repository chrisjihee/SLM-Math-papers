# MAGDi: Structured Distillation of Multi-Agent Interaction Graphs Improves Reasoning in Smaller Language Models review

## 1. Metadata

- Title: MAGDi: Structured Distillation of Multi-Agent Interaction Graphs Improves Reasoning in Smaller Language Models
- Authors: Justin Chih-Yao Chen, Swarnadeep Saha, Elias Stengel-Eskin, Mohit Bansal (UNC Chapel Hill)
- Year: 2025
- Venue / Status: ICLR 2025 Spotlight (OpenReview ffLblkoCw8)
- Links:
  - Paper: https://openreview.net/forum?id=ffLblkoCw8
  - GitHub / Code (official): https://github.com/dinobby/MAGDi
- Source PDF (local, source-of-record): `paper/2025-magdi.pdf`
- Source Grounding Log:
  - PDF: `paper/2025-magdi.pdf` — 16 pages, sha256 `1f3f4492d356ad7eb728ed6819829faef7410834c89d41fd8af2e52e0dfc5a97`(legacy `paper/09. ….pdf`의 canonical 복사본, 동일 sha256, legacy 보존), pypdf/pymupdf 본문 추출 정상(약 77k자). title/authors/abstract/method/code 직접 확인.
  - TeX source/ar5iv: 미사용.
  - 주의: venue(ICLR 2025 Spotlight)·arXiv id(2402.01620으로 알려짐)는 외부/legacy 확정(PDF 텍스트 직접 미표기). benchmark 세부 추가 확인 권장.
- Paper Type: `training` / `structured distillation of multi-agent interaction graphs (GNN-augmented student)` — graph-distillation boundary reference
- Reading Status: `strategically-read`
- Current Priority: `P1`

## 2. One-line Summary

MAGDi는 여러 LLM agent가 여러 라운드 상호작용(debate)한 내용을 **graph로 표현**하고, base student에 GNN(graph encoder)을 augment해 그 구조적 상호작용을 작은 LM에 **structured distillation**함으로써, 비싼 multi-agent multi-round inference 없이 단일 효율 모델로 reasoning을 끌어올린 multi-agent interaction graph distillation 논문이다.

## 3. 핵심 문제 설정

- 문제: multi-agent LLM 상호작용은 reasoning을 개선하지만, 여러 모델·여러 라운드의 긴 생성으로 **비싸고**, 추론에 쓸 **단일 효율 모델을 제공하지 못한다**.
- 해법: **MAGDi** — multi-agent 상호작용을 노드(개별 agent 응답)·엣지(상호작용)로 된 **graph**로 구성하고, base student를 GNN으로 보강해 구조 정보를 학습, 다중 목적(next-token + correct/incorrect contrastive + graph structure)으로 distill → 단일 student.
- 내 연구와의 연결: MAGDi는 **multi-agent interaction graph distillation / graph-structured distillation을 선점**했다. 우리 CG route는 **graph reasoning이 아니라 structured rationale/path family**로 제한해야 하며, 우리 기여는 graph를 학습시키는 것이 아니라 TTC 안의 path-family 선택이다.

## 4. 핵심 방법

- interaction graph: 여러 LLM(teacher)들이 debate한 round별 응답을 노드로, 상호작용(동의/반박/수정)을 엣지로 표현.
- student augmentation: base student LM에 **Graph Neural Network**를 붙여 graph 구조 표현을 학습.
- structured distillation 목적: (1) next-token(정답 추론 모방), (2) correct vs incorrect **contrastive**(margin), (3) **graph-level structure** 보존.
- 학습: training-heavy distillation. test-time 제어/search/verifier 없음(오히려 multi-agent 비용을 제거).
- selection unit: **(multi-agent) structured rationale / graph(학습 supervision)**. heterogeneous path-family 선택/budget allocation/STOP은 아님.
- benchmark: commonsense + math reasoning(다수; 추가 확인 권장).

## 5. SLM-Math 관점의 재해석

- MAGDi는 직접 baseline 경쟁자라기보다 **graph distillation의 "진짜 graph target" reference**(우리 CG가 graph가 아님을 분명히 하는 boundary)다.
- 공통점: multi-agent/구조적 reasoning을 작은 모델로 효율화(우리 lightweight 지향과 동기 유사).
- 차이점:
  - MAGDi는 **training-time multi-agent interaction graph distillation(+GNN)**. 우리는 **fixed backbone 위 test-time path-pool 구성·STOP**.
  - MAGDi의 graph는 agent 상호작용 graph(진짜 graph 구조 + GNN). 우리 CG는 graph-preserving traversal이 아니라 linearized structured rationale.
- 연결: MAGDi는 "graph distillation이 무엇을 의미하는지"의 기준점. 우리 CG를 graph reasoning으로 과장하지 않도록 절제하고, 현재 기여를 path-family allocation으로 명시.

## 6. 우리 연구에 대한 novelty risk

- **multi-agent interaction graph / graph-structured distillation / GNN-augmented student**를 이미 선점 → 이 자체를 우리 novelty로 쓰면 충돌.
- 특히 우리 **CG를 graph reasoning/graph distillation**으로 전면화하면 MAGDi(및 GoT)와 정면충돌.
- 위험 framing: `graph distillation이 우리 기여`, `interaction graph로 SLM reasoning 향상`, `CG가 graph reasoning이다`.
- 단, MAGDi는 training-time distillation이라 우리 inference-time allocation과 결이 다름.

## 7. 우리가 빌릴 수 있는 것

- framing: multi-agent multi-round inference의 비용 문제 / 단일 효율 모델 필요(우리 lightweight orchestration 동기와 공명).
- baseline: MAGDi로 distill된 student를 우리 orchestration의 fixed backbone 후보로(경쟁 아님).
- metric: reasoning accuracy + inference 효율(multi-agent 대비) — training-time gain과 inference-time gain 분해.
- ablation: contrastive(correct/incorrect) 목적, graph structure 목적 on/off, GNN 유무.
- terminology: `multi-agent interaction graph`, `structured distillation`, `graph encoder/GNN`, `single efficient student`.

## 8. 우리가 하면 안 되는 주장

- `graph distillation / multi-agent interaction graph distillation을 우리가 처음 제안한다`.
- `interaction graph 또는 GNN-augmented student가 우리 기여다`.
- `우리 CG가 graph reasoning/graph-preserving distillation이다`.
- 이 논문 대비 distillation 성능 SOTA 경쟁, training-time gain을 inference-time 기여로 혼동.

## 9. baseline / ablation 반영 아이디어

- CG를 structured rationale/path family로 제한 명시, **graph reasoning claim 절제**(GoT 노트와 연동).
- distillation은 backbone 확보 수단으로만, 비교 중심은 fixed backbone 위 test-time path-pool.
- multi-agent 비용 vs 단일 모델 효율 대비를 우리 "lightweight orchestration vs heavy multi-agent/search" 포지셔닝에 활용.

## 10. Related Work에 넣을 문장 초안

MAGDi(Chen et al., ICLR 2025 Spotlight)는 여러 LLM agent가 여러 라운드 상호작용한 내용을 그래프로 표현하고, base student 모델에 graph neural network를 augment하여 그 구조적 상호작용을 작은 언어모델에 structured distillation함으로써, 비싼 multi-agent multi-round 추론 없이 단일 효율 모델로 commonsense·math reasoning을 향상시켰다. 이는 graph-structured distillation과 multi-agent interaction의 효율화를 대표하는 연구다.

본 연구는 multi-agent interaction graph distillation이나 graph-structured distillation 자체를 새 기여로 두지 않는다. 우리의 Concept Graph는 graph-preserving traversal이 아니라 linearized structured rationale로서 여러 reasoning path family 중 하나로 보존되며, 현재 기여는 graph를 학습으로 주입하는 것이 아니라 fixed/given backbone 위에서 제한된 test-time compute 안의 heterogeneous reasoning path family를 문제별로 구성·선택·중단하는 **state-conditioned test-time path-pool allocation**에 있다. 다만 MAGDi가 지적한 multi-agent 추론의 비용 문제는 우리의 lightweight orchestration 동기와 공명한다.

## 11. 현재 우선순위와 다음 액션

- 현재 우선순위: `P1`
- 위협도: 중간 (graph distillation/CG graph claim을 직접 제약; 직접 baseline 경쟁은 아님)
- 구현 결정: full reproduction 비대상. distillation은 backbone 확보 수단으로만, 비교 중심은 test-time orchestration.
- 지금 할 일:
  - MAGDi를 Distilling Step-by-Step·UniCoTT·STaR와 함께 distillation boundary cluster의 P1 reference로 고정. GoT와 함께 graph-claim 절제 reference로도 연결.
  - `graph distillation/interaction graph/GNN-augmented student를 novelty로 쓰지 않기`, `CG를 graph reasoning으로 과장하지 않기` wording 가드.
  - multi-agent 비용 대비 lightweight orchestration 동기를 positioning에 활용.
- 나중으로 미뤄도 되는 일: MAGDi 재현, GNN distillation 평가.
- 한 줄 결론: MAGDi는 "진짜 graph distillation"의 기준점이며, 우리 CG를 graph reasoning과 분리하고 현재 기여를 fixed backbone 위 test-time path-pool allocation으로 분리하게 만드는 P1 reference다.
