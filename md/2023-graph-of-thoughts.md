# Graph of Thoughts: Solving Elaborate Problems with Large Language Models review

## 1. Metadata

- Title: Graph of Thoughts: Solving Elaborate Problems with Large Language Models
- Authors: Maciej Besta, Nils Blach, Ales Kubicek, Robert Gerstenberger, Michał Podstawski, Lukas Gianinazzi, Joanna Gajda, Tomasz Lehmann, Hubert Niewiadomski, Piotr Nyczyk, Torsten Hoefler (ETH Zurich / Warsaw University of Technology / Cledar)
- Year: 2024 (citation 기준; arXiv 2308.09687 v1 2023-08, v4 2024-02)
- Venue / Status: AAAI 2024 (DOI 10.1609/aaai.v38i16.29720)
- Links:
  - Paper: https://arxiv.org/abs/2308.09687
  - GitHub / Code (official): https://github.com/spcl/graph-of-thoughts
- Source PDF (local, source-of-record): `paper/2023-graph-of-thoughts.pdf`
- Source Grounding Log:
  - PDF: `paper/2023-graph-of-thoughts.pdf` — 63 pages, sha256 `73caa3c05813105e5db38edfbb58e1b660771a00dfdb74768c8845e15263c5da`, pypdf/pymupdf 본문 추출 정상(약 172k자). title/authors/abstract/method/benchmark/result/code URL 직접 확인.
  - TeX source: `/tmp/got_tex` (arXiv e-print, 임시·비-commit), main `aaai-got.tex`, 템플릿 `aaai24.sty`(→ AAAI 2024 확정). abstract/introduction/background/scheme/arch/eval/conc/appendix 구조와 `eval.tex` 결과를 직접 확인. repo에 commit하지 않음.
  - ar5iv HTML: https://ar5iv.labs.arxiv.org/html/2308.09687 — section 구조·개념 독해 보조(“The Latency-Volume Tradeoff” 장, GoO/GRS, volume metric 확인). PDF/TeX와 불일치 없음. 비-commit.
  - arXiv abstract: https://arxiv.org/abs/2308.09687 — 11인 저자, venue AAAI 2024, DOI, subjects(cs.CL/cs.AI/cs.LG) 확인.
  - code URL: https://github.com/spcl/graph-of-thoughts (PDF “Website & code”).
- Correction(중요):
  - GoT 실험 모델은 **ChatGPT-3.5 / GPT-3.5** 이다(TeX `eval.tex` 확인). ToT의 GPT-4 실험과 혼동하지 말 것.
- Paper Type:
  - `inference-time` / `prompting`
  - `graph-structured reasoning (thought transformations)`
  - search-heavy / graph-reasoning contrastive boundary reference
- Reading Status: `strategically-read`
- Current Priority: `P1`

## 2. One-line Summary

GoT는 LLM의 reasoning을 thought를 정점(vertex), 의존성을 간선(edge)으로 갖는 **임의의 방향 그래프**로 모델링하고, generate/aggregate(merge)/refine 같은 thought transformation과 thought scoring으로 thought를 합치고 다듬어, CoT·ToT(트리)를 넘어 sorting 등 elaborate 과제에서 품질↑·비용↓을 보인 graph-structured prompting framework이다.

## 3. 핵심 문제 설정

- 문제: CoT(선형)·ToT(트리)는 thought 간 **합치기(merge)·되먹임(feedback loop)** 같은 비선형 의존성을 표현하지 못해, 분해-후-병합이 필요한 elaborate 과제에 비효율적이다.
- 해법: reasoning을 **arbitrary graph `G=(V,E)`** 로 일반화 — thought=vertex, dependency=edge. 여러 thought를 **aggregate**(synergy), 네트워크 전체를 **distill**, thought를 **refine loop**로 개선.
- 내 연구와의 연결: GoT는 우리 `CG(Concept Graph)` 이름과 가장 가까워 **reviewer가 가장 먼저 연상할 graph-boundary reference**다. 단 GoT의 통제 단위는 **thought/vertex(미시)** 이고 graph 내부 transformation/실행이며, 우리 CG는 graph-preserving traversal이 아니라 linearized structured rationale이다.

## 4. 핵심 방법 (PDF+TeX grounding)

- 표현: directed graph `G=(V,E)`, V=LLM thoughts, E=dependencies.
- thought transformations: **Generate**(기존 thought에서 k개 새 thought), **Aggregate**(여러 thought를 하나로 merge), **Refine**(한 thought를 self-loop로 개선). + **Scoring & Ranking thoughts**.
- 시스템 아키텍처: **Prompter / Parser / Scoring & Validation / Controller**, 그리고 **GoO(Graph of Operations = 실행 계획)** 와 **GRS(Graph Reasoning State = 동적 상태)**.
- 분석 지표: **volume of a thought**(어떤 thought v에 도달 가능한 선행 thought 수) — latency–volume tradeoff에서 GoT가 low latency + high volume을 동시에 달성.
- selection/통제 단위: **thought / vertex / graph state(GRS)** 및 graph operation. heterogeneous path-family 선택이나 STOP 정책은 아님.
- 실험 설정(TeX `eval.tex` 직접 확인):
  - 모델 **ChatGPT-3.5 / GPT-3.5**, 100 samples/task, temperature 1.0, 4k context(document merging은 16k).
  - baseline: **IO, CoT, CoT-SC, ToT, ToT2** (cost-matched 구성).
  - tasks: **sorting, set intersection, keyword counting, document merging**.
- 핵심 결과:
  - GoT vs ToT — sorting(P=128) median error 약 **62%↓** + 비용 **>31%↓**.
  - GoT vs CoT/IO — sorting(P=64) error 약 **65%/83%↓**.
  - **문제 크기 P가 커질수록 GoT 우위 확대**(decompose→solve→merge).

## 5. SLM-Math 관점의 재해석

- GoT는 직접 baseline 경쟁자라기보다, **graph-structured reasoning의 naming/claim boundary reference**다.
- 공통점: 여러 thought를 만들어 평가·결합하는 multi-thought 사고, 추가 학습 없이 inference-time 행동 변경.
- 차이점:
  - **granularity**: GoT는 thought/vertex 단위 graph transformation(미시). 우리는 path family / route / macro strategy / STOP(거시).
  - **graph vs heterogeneous pool**: GoT는 동질 thought의 graph. 우리는 `direct / CoT / prompt-diverse CoT / CG / PAL / PoT / verifier-guided` 이질 family pool.
  - **graph-controller(GoO/GRS) vs lightweight orchestration**: GoT는 graph 실행 제어. 우리는 route/strategy-card 추정 + macro action routing + STOP을 budget allocation으로.
  - **large API model(GPT-3.5) vs small LM**: GoT는 GPT-3.5 puzzle 과제. 우리는 small LM + fixed sample bank / offline simulator.
- 안전한 한 문장 차별화:
  - GoT는 하나의 reasoning을 thought graph로 변환·실행하고, 우리 CG는 그 graph search가 아니라 linearized structured rationale이며, 본 연구는 제한 TTC 안의 heterogeneous path-family acquisition·STOP에 집중한다.

## 6. 우리 연구에 대한 novelty risk

- **graph-structured reasoning / arbitrary thought graph / transformation-based LLM reasoning**을 강하게 선점 → "graph로 reasoning" 류 주장 불가.
- **aggregation/merging, refinement loop, thought scoring/ranking**도 선점.
- 우리 **CG가 graph reasoning**이라는 인상을 주면 GoT와 정면충돌(우리 CG는 graph-preserving traversal이 아니라 linearized structured rationale).
- 단, 위협은 thought/vertex 단위 graph transformation(미시)이고 GPT-3.5 puzzle 과제 — RASC/Scaling-TTC 같은 inference-time allocation 직접 baseline과는 결이 다름.

## 7. 우리가 빌릴 수 있는 것

- framing: thought 간 **의존성·병합·되먹임**의 중요성 / **latency–volume(또는 cost–quality) tradeoff** / decompose→solve→merge.
- baseline: `IO / CoT / CoT-SC / ToT` 까지 직접 baseline, **GoT는 graph boundary reference로만**(cost-matched GoT-inspired lightweight comparison은 선택).
- metric: error/quality + **cost(LM call) 동시 보고**, 문제 크기 scaling, cost-matched comparison.
- terminology(차용): `thought transformation`, `aggregation/merging`, `refine`, `Graph of Operations(GoO)`, `Graph Reasoning State(GRS)`, `volume of a thought`.

## 8. 우리가 하면 안 되는 주장

- `graph로 reasoning을 구조화하는 것이 새롭다`(GoT/ToT 선점).
- `우리 CG가 GoT식 graph search/traversal과 같다`(과장 금지 — 우리 CG는 linearized structured rationale).
- `thought aggregation/merging/refinement loop를 우리가 처음 도입한다`.
- `transformation-based / graph-of-thought reasoning이 우리 기여다`.
- GoT 대비 raw 성능 SOTA 경쟁, graph 내부 실행 비용(generation+aggregation+refinement+scoring) 무시.
- GoT를 GPT-4 실험으로 잘못 기록하지 말 것(실제 GPT-3.5).

## 9. baseline / ablation 반영 아이디어

- GoT는 **full reproduction 비대상** — graph-reasoning / search-heavy **boundary reference**. 필요 시에만 cost-matched **GoT-inspired lightweight comparison**(merge/refine 일부) 1개.
- 우리 path-family pool 비교에는 `IO/CoT/CoT-SC/ToT`까지 직접 baseline, GoT는 graph 경계 대비로.
- "structure 이득(graph/merge)"과 "우리 heterogeneous path-family 다양화 이득"을 분리하는 ablation(ToT 노트의 prompt-diversity vs structural 분리와 연동).
- cost(LM call/graph operation) 계상 원칙을 GoT 사례로 강화(분해-병합도 budget에 산입).

## 10. Related Work에 넣을 문장 초안

Graph of Thoughts(Besta et al., AAAI 2024)는 LLM이 생성하는 thought를 정점으로, thought 간 의존성을 간선으로 갖는 임의의 그래프로 reasoning을 모델링하고, generate·aggregate(merge)·refine 같은 thought transformation과 thought scoring을 통해 CoT·ToT를 넘는 비선형 추론을 가능하게 한 graph-structured prompting framework다. 이들은 ChatGPT-3.5 기반으로 sorting·set intersection·keyword counting·document merging에서 ToT 대비 품질을 높이면서(예: sorting에서 median error 약 62% 감소, 비용 31% 이상 절감) 문제 크기가 커질수록 이점이 커짐을 보였다.

그러나 GoT의 초점은 단일 reasoning을 thought 그래프 내부에서 변환·실행하는 graph-structured prompting이며, 제한된 test-time compute 안에서 서로 다른 reasoning path family를 어떤 순서·budget으로 획득하고 언제 멈출지는 다루지 않는다. 본 연구의 Concept Graph는 graph-preserving traversal이 아니라 linearized structured rationale로서 heterogeneous reasoning path family 중 하나이며, 본 연구는 GoT류 thought-graph 변환·탐색이 아니라 현재 reasoning state와 남은 budget을 바탕으로 한 **state-conditioned heterogeneous path-family acquisition·macro strategy allocation·STOP under limited TTC**라는 lightweight orchestration에 위치한다.

## 11. 현재 우선순위와 다음 액션

- 현재 우선순위: `P1`
- 위협도: 중간 (CG↔graph reasoning 혼동 위험이 특히 큼; 직접 baseline 경쟁은 아님)
- 구현 결정: **full reproduction 비대상**; graph-reasoning / search-heavy boundary reference. 필요 시 cost-matched GoT-inspired lightweight comparison만.
- 지금 할 일:
  - GoT를 ToT·MCTS류(rStar-Math)와 함께 search/graph cluster의 P1 reference로 고정.
  - `graph reasoning · thought graph · aggregation/merging · refinement loop · transformation reasoning`을 novelty로 쓰지 않도록 wording 가드.
  - **"CG는 linearized structured rationale이며 GoT식 graph-of-thought search가 아니다"** 를 positioning에 명문화.
  - cost(LM call/graph operation) 계상 원칙 강화. GoT 실험 모델은 GPT-3.5로 정확히 기록.
- 나중으로 미뤄도 되는 일: GoT graph-controller(GoO/GRS) 재현, puzzle benchmark 평가.
- 한 줄 결론: GoT는 우리가 재현·경쟁할 대상이 아니라, "reasoning을 그래프로 변환·실행"하는 graph-structured boundary reference로 두고, 우리 CG를 graph search와 분리하며 우리를 path-family acquisition·STOP under limited TTC로 위치시키게 하는 P1 reference다.
