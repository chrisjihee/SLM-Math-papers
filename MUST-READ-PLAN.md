# Must-read(우선순위) + 읽기/구현 계획 (정본)

Last updated: 2025-12-24

목표: 10B 이하 sLLM이 한국어 MWP에서 **개념 그래프(CG; JSON triples)**를 안정적으로 생성하고, **최소 테스트타임 비용**으로 추론 성능을 끌어올리는 것.

선정/운영 원칙:
- 링크는 **공식 페이지**만 사용합니다 (ACL Anthology / OpenReview / arXiv / 학회 프로시딩/퍼블리셔).
- 이 문서는 저장소 내 “추천 논문” 자료들의 **정본(canonical) shortlist + 실행 계획**입니다.
- 후보 풀/초안은 `papars.yaml`, `recommended-papers-2025-by-*.md`에 남아 있을 수 있으나, 이 문서의 링크/메타가 최종입니다.

## 상태: 이미 읽음(완료)
- Self-Instruct: Aligning Language Models with Self-Generated Instructions — ACL 2023 — https://arxiv.org/abs/2212.10560
- Distilling Step-by-Step! Outperforming Larger Language Models with Less Training Data and Smaller Model Sizes — ACL 2023 (Findings) — https://arxiv.org/abs/2305.02301
- Phased Instruction Fine-Tuning for Large Language Models — ACL 2024 (Findings) — https://arxiv.org/abs/2406.04371

## Must-read shortlist (우선순위)

### P0 (먼저 읽기: 바로 실험/구현에 연결)
1) Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning — ICLR 2025 (Oral) — https://openreview.net/forum?id=4FWAwZtd2n
- 왜: best-of-$N$/self-consistency/rerank를 “감(heuristic)”이 아니라 **compute-optimal** 문제로 정의해 줍니다. [PLAN.md](../PLAN.md)의 Axis 2에 직결.
- 뽑을 것: $N$ 증가에 따른 효용/비용 곡선, break-even(“SLM×$N$ vs LLM×1”) 사고틀.

2) Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning — ICLR 2025 (Spotlight) — https://openreview.net/forum?id=A6Y7AqlzLW
- 왜: 베이스 생성기를 크게 바꾸지 않고도 **테스트타임 선택(Selection)**만으로 성능을 올리는 가장 직접적인 루트.
- 뽑을 것: PRM(프로세스 검증기) 학습 데이터 레시피/스케일링, 실패 모드, rerank 적용 방식.

3) Process Reward Models That Think — arXiv — https://arxiv.org/abs/2504.16828
- 왜: “현대 PRM 레시피” 관점에서, CG 생성 과정/부분 그래프를 점수화하는 verifier 설계에 힌트가 많습니다.

4) Let’s Verify Step by Step — arXiv — https://arxiv.org/abs/2305.20050
- 왜: verifier + search/rerank의 고전적 기준선(blueprint). 빠르게 MVP를 만들 때 레퍼런스로 좋습니다.

5) UniCoTT: A Unified Framework for Structural Chain-of-Thought Distillation — ICLR 2025 (Poster) — https://openreview.net/forum?id=3baOKeI2EU
- 왜: “구조를 보존하는 증류”의 대표 사례. CG가 이미 구조화된 중간표현이므로 Axis 1(표현 비교)과 Axis 1/2의 브릿지로 유용.

6) MAGDi: Structured Distillation of Multi-Agent Interaction Graphs Improves Reasoning in Smaller Language Models — https://arxiv.org/abs/2402.01620
- 왜: 그래프 자체를 증류 타겟으로 두는 설계가 CG 증류 방향성과 강하게 맞닿습니다.

7) Mentor-KD: Making Small Language Models Better Multi-step Reasoners — https://arxiv.org/abs/2410.09037
- 왜: teacher 데이터가 제한적/노이즈가 있을 때의 “멘토-학생” 2단계 KD 템플릿을 제공합니다.

8) SWITCH: Studying WItH TeaCHer for Knowledge Distillation of Large Language Models — https://arxiv.org/abs/2410.19503
- 왜: 선택적 교사介入으로 **긴 출력의 노이즈/스키마 위반(JSON 깨짐)**을 줄이는 데 직접적입니다.

### P1 (두 번째 물결: 평가/정렬 강화 + 모델 병합/LoRA 조합)
9) LoRA Soups: Merging LoRAs for Practical Skill Composition Tasks — COLING 2025 (Industry Track) — https://aclanthology.org/2025.coling-industry.55/
- 왜: CG/MR/QA/RP처럼 태스크별 LoRA를 운용할 때 **조합(composition)**을 현실적으로 다룹니다. [PLAN.md](../PLAN.md)의 Axis 3에 직결.

10) Unraveling LoRA Interference: Orthogonal Subspaces for Robust Model Merging — https://arxiv.org/abs/2505.22934
- 왜: 왜 naive merge가 깨지는지(간섭/서브스페이스)와 완화 방향을 제공합니다.

11) InstructGraph: Boosting Large Language Models via Graph-centric Instruction Tuning and Preference Alignment — https://arxiv.org/abs/2402.08785
- 왜: 그래프 포맷을 중심으로 한 instruction + preference alignment를 같이 봅니다. CG 출력의 “좋은/나쁜” 페어를 만드는 관점에서 도움.

12) DRAG: Distilling RAG for SLMs from LLMs to Transfer Knowledge and Mitigate Hallucination via Evidence and Graph-based Distillation — https://arxiv.org/abs/2506.01954
- 왜: KG/증거 기반으로 hallucination을 줄이려는 경우(선택 사항) 참고할 만한 증류 설계.

13) Quantification of Large Language Model Distillation — ACL 2025 (Long) — https://aclanthology.org/2025.acl-long.248/
- 왜: KD 성능을 “정답률”만이 아니라 무엇이 좋아졌는지(지표/분해) 더 단단하게 보고하는 데 도움.

14) Learning from Committee: Reasoning Distillation from a Mixture of Teachers — ACL 2025 (Findings) — https://aclanthology.org/2025.findings-acl.217/
- 왜: 여러 teacher/API/체크포인트를 쓸 때의 aggregation 레퍼런스.

## 4주 계획(읽기 → 구현 → 측정)

### Week 1 — Test-time scaling 기준선
읽기: (P0) #1 + #4
- 구현: best-of-$N$ / self-consistency + 기존 출력에 대한 단순 rerank.
- 측정: $N$ 대비 정확도, 토큰/시간 비용 대비 정확도(비용-성능 곡선).

### Week 2 — PRM(프로세스 검증기) MVP
읽기: (P0) #2 + #3
- 구현: (1) 중간 단계(또는 부분 CG)의 유효성/진행(progress)을 점수화하는 PRM, (2) rerank 적용.
- 측정: Week 1 대비 gain, 긴 출력에서의 안정성, JSON 스키마 위반률 감소.

### Week 3 — 구조/그래프 증류 업그레이드
읽기: (P0) #5 + #6 + #7
- 구현: “정답만”이 아니라 **구조화 중간표현(CG)**를 직접 맞추는 증류(제약/손실) 추가.
- 측정: CG 스키마 준수율, triple-F1(가능하면), end-task MR 성능.

### Week 4 — 안정성 + 모듈화(LoRA 조합/병합)
읽기: (P1) #9 + #10 (+ #11: preference pair를 쓰면)
- 구현: 태스크별 LoRA 학습 후 병합/조합 실험 + 간섭 진단(merge 후 단일 태스크 회귀).
- 측정: 단일 태스크 보존(per-task retention) + 조합 태스크 이득.

## PLAN.md 3축(Axis)와의 매핑
- Axis 1 (CoT vs CG: 구조화 표현의 데이터 효율): 이미 읽은 3편(Self-Instruct / Distilling Step-by-Step / Phased IFT) + (P0) #5 UniCoTT + (P1) #11 InstructGraph
- Axis 2 (Test-time Inference Scaling): (P0) #1 Scaling test-time compute + #2 Rewarding Progress + #3 PRM That Think + #4 Let’s Verify
- Axis 3 (Model Merging + DPO): (P1) #9 LoRA Soups + #10 LoRA Interference (그리고 내부적으로는 TIES/DARE/DPO를 결합)

## 링크 검증 메모(중요)
- Rewarding Progress(OpenReview): 유효 링크는 https://openreview.net/forum?id=A6Y7AqlzLW 입니다. (이전 후보 중 일부 ID는 “Note not found”)
- UniCoTT(OpenReview): 유효 링크는 https://openreview.net/forum?id=3baOKeI2EU 입니다. (이전 후보 중 일부 ID는 “Note not found”)
- LoRA Soups(ACL Anthology): 유효 링크는 https://aclanthology.org/2025.coling-industry.55/ 입니다. (이전 후보 중 하나인 2025.coling-industry.39 는 다른 논문)

## 비추천(현 프로젝트 기준, 지금은 우선순위 낮음)
- 구현 레시피가 거의 없는 “일반론/서베이” 중심 논문
- 10B 이하 제약으로 전이/증류 프로토콜이 불분명한 “대형 모델 전용” 학습 논문
- 공식 랜딩 페이지(OpenReview/arXiv/Anthology 등) 정체성이 불명확한 자료
