# 추천 논문 통합 목록 (Unified Paper List)

**Last updated:** 2026-01-06
**총 논문 수:** 85편 (중복 제거 후)

이 문서는 저장소 내 모든 추천 논문 자료(`papars.yaml`, `2nd/3rd-recommendation.md`, `recommended-papers-2025-by-*.md`)를 **테마별로 통합**한 정본입니다.

---

## 📌 정본 Must-read (정리 완료)

> 아래 항목은 [MUST-READ-PLAN.md](MUST-READ-PLAN.md)에서 우선순위가 확정된 논문들입니다.

### ✅ 이미 읽음 (완료)
| # | 논문 | 학회 | 링크 |
|---|------|------|------|
| 1 | Self-Instruct: Aligning Language Models with Self-Generated Instructions | ACL 2023 | https://arxiv.org/abs/2212.10560 |
| 2 | Distilling Step-by-Step! Outperforming Larger Language Models with Less Training Data and Smaller Model Sizes | ACL 2023 (Findings) | https://arxiv.org/abs/2305.02301 |
| 3 | Phased Instruction Fine-Tuning for Large Language Models | ACL 2024 (Findings) | https://arxiv.org/abs/2406.04371 |

---

## 🔥 테마 1: Structured Rationale Distillation (구조화된 증류)

SLM에게 CoT/그래프 구조를 효율적으로 증류하는 연구들입니다.

| # | 논문 | 학회 | 링크 | 핵심 아이디어 |
|---|------|------|------|--------------|
| 1 | **UniCoTT: A Unified Framework for Structural Chain-of-Thought Distillation** | ICLR 2025 | https://openreview.net/forum?id=3baOKeI2EU | Chain/Tree/Graph 형태의 구조적 CoT를 통합 포맷으로 SLM에 증류 |
| 2 | **MAGDi: Structured Distillation of Multi-Agent Interaction Graphs** | ICLR 2025 (Spotlight) | https://arxiv.org/abs/2402.01620 | GPT-4 다중 에이전트 토론을 논증 그래프로 변환 후 증류 |
| 3 | **Mentor-KD: Making Small Language Models Better Multi-step Reasoners** | EMNLP 2024 | https://arxiv.org/abs/2410.09037 | 70B→13B Mentor→7B 학생의 2단계 KD + soft label |
| 4 | **SWITCH: Studying WItH TeaCHer for Knowledge Distillation of LLMs** | EMNLP 2024 | https://arxiv.org/abs/2410.19503 | 긴 시퀀스에서 오류 토큰만 선택적 교사介入 KD |
| 5 | **InstructGraph: Boosting LLMs via Graph-centric Instruction Tuning and Preference Alignment** | ACL 2024 (Findings) | https://arxiv.org/abs/2402.08785 | 그래프 중심 IT + preference alignment로 환각 감소 |
| 6 | **QCRD: Quality-guided Contrastive Rationale Distillation** | arXiv 2024 | https://arxiv.org/abs/2405.13014 | 고품질/저품질 rationale을 대비 학습으로 증류 |
| 7 | **Distilling Reasoning Ability from LLMs with Adaptive Thinking** | arXiv 2024 | https://arxiv.org/abs/2404.09170 | 난이도에 따라 생각 길이를 적응적으로 조절 |
| 8 | **Symbolic Chain-of-Thought Distillation (SCoTD)** | ACL 2023 | https://arxiv.org/abs/2306.14050 | 교사 LLM의 다양한 CoT 샘플링으로 소형 모델 증류 |
| 9 | **Beyond Answers: Multi-Teacher Knowledge Distillation (TinyLLM)** | WSDM 2025 | https://arxiv.org/abs/2402.04616 | 여러 교사 LLM의 답+추론을 통합 증류 |
| 10 | **Distilling Structured Rationale from LLMs to SLMs for Abstractive Summarization** | AAAI 2025 | https://doi.org/10.1609/aaai.v39i24.34727 | 구조화 rationale 다단계 평가 + 게이팅 fusion |
| 11 | **Keypoint-based Progressive Chain-of-Thought Distillation** | ICML 2024 | https://proceedings.mlr.press/v202/feng24a.html | 중요 토큰 가중치 + 역순 커리큘럼 학습 |
| 12 | **MoDE-CoTD: CoT Distillation with Mixture of Decoupled LoRA-Experts** | LREC-COLING 2024 | https://aclanthology.org/2024.lrec-main.1003 | 여러 태스크별 LoRA 전문가를 병합 증류 |
| 13 | **Unveiling the Key Factors for Distilling CoT Reasoning** | ACL 2025 (Findings) | https://aclanthology.org/2025.findings-acl.782 | CoT 세분화/포맷/교사 규모의 체계적 분석 |
| 14 | **Learning to Maximize Mutual Information for CoT Distillation** | ACL 2024 (Findings) | https://aclanthology.org/2024.findings-acl.577/ | 정답+CoT 간 상호정보량(MI) 최대화 |
| 15 | **Teaching SLMs Reasoning through Counterfactual Distillation** | EMNLP 2024 | https://aclanthology.org/2024.emnlp-main.333/ | Counterfactual 데이터 + multi-view CoT |
| 16 | **Distilling Mathematical Reasoning Capabilities into SLMs (EoTD/ETD)** | arXiv 2024 | https://arxiv.org/abs/2401.11864 | 수식 형태 중간표현(EoT) + Ensemble Thoughts |
| 17 | **Skip-Thinking: Chunk-wise CoT Distillation** | EMNLP 2025 | https://aclanthology.org/2025.emnlp-main.610/ | 청크 단위 분할로 불필요한 서술 건너뛰기 |
| 18 | **Towards Efficient CoT Distillation: Self-Guided Rationale Selector (MoRSD)** | EMNLP 2025 (Findings) | https://aclanthology.org/2025.findings-emnlp.413/ | 학생 모델이 자체 평가로 rationale 선별 |
| 19 | **Distilling LLM Agent into Small Models with Retrieval and Code Tools** | NeurIPS 2025 (Spotlight) | https://arxiv.org/abs/2505.17612 | 에이전트 행동(CoT+Tool)을 SLM에 이식 |
| 20 | **DRAG: Distilling RAG for SLMs via Evidence and Graph-based Distillation** | ACL 2025 | https://arxiv.org/abs/2506.01954 | 증거 순위 + KG를 다중 loss로 증류 |
| 21 | **Contextualization Distillation from LLM for KG Completion** | EACL 2024 (Findings) | https://arxiv.org/abs/2402.01729 | Triple→자연어 문맥으로 재작성 후 증류 |
| 22 | **KARD: Knowledge-Augmented Reasoning Distillation for SLMs** | NeurIPS 2023 | https://arxiv.org/abs/2305.18395 | 외부 지식(검색/KB) 기반 reasoning chain 증류 |
| 23 | **Reasoning Scaffolding: Distilling the Flow of Thought from LLMs** | arXiv 2025 | https://arxiv.org/abs/2509.23619 | Flow-of-thought를 이산 신호 시퀀스로 구조화 |
| 24 | **Improving Mathematical Reasoning via Feedback-Driven Distillation** | arXiv 2024 | https://arxiv.org/abs/2411.14698 | 실패 케이스 기반 문제 변형 + 피드백 루프 |
| 25 | **TEACH: A Contrastive Knowledge Adaptive Distillation Framework** | ACL 2025 | https://aclanthology.org/2025.acl-long.178/ | Contrastive learning 기반 지식 적응 증류 |
| 26 | **Learning from Committee: Reasoning Distillation from a Mixture of Teachers** | ACL 2025 (Findings) | https://aclanthology.org/2025.findings-acl.217/ | 여러 Teacher 모델의 Reasoning 통합 증류 |
| 27 | **Flipping Knowledge Distillation: Leveraging Small Models' Expertise** | ACL 2025 | https://aclanthology.org/2025.acl-long.1081/ | 역방향 증류 - 작은 모델 전문성을 큰 모델에 전달 |
| 28 | **Dual-Space Knowledge Distillation for LLMs** | EMNLP 2024 | https://aclanthology.org/2024.emnlp-main.1010/ | 이중 공간(logit + feature)에서 지식 증류 |
| 29 | **Self-Distillation for LLMs in Code Generation** | EMNLP 2024 | https://aclanthology.org/2024.emnlp-main.66/ | 자기 증류를 통한 코드 생성 성능 향상 |
| 30 | **Quantification of Large Language Model Distillation** | ACL 2025 | https://aclanthology.org/2025.acl-long.248/ | LLM 증류 효과 정량화 방법론 |

---

## 🚀 테마 2: Test-time Scaling & Inference Optimization

SLM이 추론 시점에 더 많이/효율적으로 생각하여 성능을 높이는 방법론입니다.

| # | 논문 | 학회 | 링크 | 핵심 아이디어 |
|---|------|------|------|--------------|
| 1 | **Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters** ⭐ | ICLR 2025 (Oral) | https://openreview.net/forum?id=4FWAwZtd2n | Test-time compute가 parameter scaling보다 효과적일 수 있음 |
| 2 | **Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning** | ICLR 2025 (Spotlight) | https://openreview.net/forum?id=A6Y7AqlzLW | Progress 기반 prover policy + PRM 스케일링 |
| 3 | **Process Reward Models That Think (ThinkPRM)** | arXiv 2025 | https://arxiv.org/abs/2504.16828 | 생성적 PRM으로 데이터 효율/서치 성능 향상 |
| 4 | **Let's Verify Step by Step** | ICLR 2024 | https://arxiv.org/abs/2305.20050 | PRM800K + Process vs Outcome supervision |
| 5 | **GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning** | arXiv 2025 | https://arxiv.org/abs/2504.00891 | PRM을 생성적으로 사용하여 TTS 스케일링 |
| 6 | **Kinetics: Rethinking Test-Time Scaling Laws** | arXiv 2025 | https://arxiv.org/abs/2506.05333 | 모델 크기별 TTS 비용-효율 분석 |
| 7 | **Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling** | arXiv 2025 | https://arxiv.org/abs/2502.06703 | 소형 모델이 유리한 컴퓨트 구간 분석 |
| 8 | **Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference** | arXiv 2024 | https://arxiv.org/abs/2408.00724 | Best-of-N, voting, tree-search 비용 효율 분석 |
| 9 | **s1: Simple test-time scaling** | arXiv 2025 | https://arxiv.org/abs/2501.19393 | s1K 데이터 구성 + budget forcing 기법 |
| 10 | **Small Language Models Need Strong Verifiers to Self-Correct Reasoning** | ACL 2024 (Findings) | https://aclanthology.org/2024.findings-acl.924 | 강력한 LLM 피드백으로 SLM 자기정정 학습 |
| 11 | **Reasoning-Aware Self-Consistency (RASC)** | NAACL 2025 | https://aclanthology.org/2025.naacl-main.184 | 추론 경로 품질 평가로 SC 효율화 (70-90% 샘플 절약) |
| 12 | **rStar: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking** | arXiv 2025 | https://arxiv.org/abs/2501.04519 | MCTS + PPM 자기진화로 7B가 O1 수준 달성 |
| 13 | **Soft Self-Consistency Improves Language Models Agents** | ACL 2024 (Short) | https://aclanthology.org/2024.acl-short.28/ | 확률값 가중 투표로 SC 효율화 |
| 14 | **Boosting the Power of SLMs with Self-Consistency Training (MC-CoT)** | ECCV 2024 | https://arxiv.org/abs/2311.14109 | Train-time에 SC 아이디어 도입 |
| 15 | **General Purpose Verification for CoT Prompting** | arXiv 2024 | https://arxiv.org/abs/2405.00204 | 관련성/정확성/일관성 3원칙 검증 |
| 16 | **Beyond the First Error: Process Reward Models for Reflective Mathematical Reasoning** | EMNLP 2025 (Findings) | https://aclanthology.org/2025.findings-emnlp.253/ | Error Propagation/Cessation 규칙으로 PRM 학습 |
| 17 | **Process Reward Model with Q-value Rankings** | ICLR 2025 (Poster) | https://openreview.net/forum?id=wQEdh2cgEk | Q-value 기반 랭킹으로 PRM 학습 |
| 18 | **Stop Summation: Min-Form Credit Assignment (PURE)** | NeurIPS 2025 (Poster) | https://openreview.net/forum?id=3Sxby0hH1q | Min-form 신용할당으로 reward hacking 방지 |
| 19 | **Efficient PRM Training via Active Learning (ActPRM)** | COLM 2025 | https://openreview.net/forum?id=CJ2FmPmoDE | 불확실한 step만 선별 라벨링 |
| 20 | **Retrieval-Augmented PRM for Generalizable Mathematical Reasoning** | ACL 2025 (Findings) | https://openreview.net/forum?id=zkoeIWbTYy | 유사 문제/단계 검색으로 PRM 판단 보강 |
| 21 | **Provable Scaling Laws for Test-Time Compute of LLMs** | NeurIPS 2025 (Poster) | https://openreview.net/forum?id=GBMzJLhsRj | 이론적 스케일링 법칙 (리그/토너먼트식 비교) |
| 22 | **Optimizing Test-Time Compute via Meta Reinforcement Finetuning** | ICML 2025 (Poster) | https://openreview.net/forum?id=TqODUDsU4u | 메타-RL로 compute 할당 정책 학습 |
| 23 | **V-STaR: Training Verifiers for Self-Taught Reasoners** | ICLR 2024 | https://arxiv.org/abs/2402.06457 | 정답/오답 데이터로 Verifier 학습 + DPO 결합 |
| 24 | **Quiet-STaR: Language Models Can Teach Themselves to Think Before Speaking** | arXiv 2024 | https://arxiv.org/abs/2403.09629 | 모든 토큰에 내적 독백(Rationale) 생성 |
| 25 | **Are More LLM Calls All You Need? Scaling Laws of Compound Inference Systems** | arXiv 2024 | https://arxiv.org/abs/2403.02419 | Vote/Filter/Chain 복합 추론 Scaling Law 분석 |
| 26 | **Inference Scaling for Long-Context RAG** | ICLR 2025 (Oral) | https://openreview.net/forum?id=FSjIrOm1vz | Long-context RAG inference scaling 전략 |
| 27 | **Self-Improvement in Language Models: The Sharpening Mechanism** | ICLR 2025 (Oral) | https://openreview.net/forum?id=WJaUkwci9o | Self-improvement의 이론적 메커니즘 분석 |
| 28 | **Process-supervised Reward Model in Mathematical Reasoning** | ACL 2025 | https://aclanthology.org/2025.acl-long.216/ | 수학 추론에서의 PRM 활용 |
| 29 | **DeAL: Decoding-time Alignment for LLMs** | ACL 2025 | https://aclanthology.org/2025.acl-long.1274/ | Decoding time에 alignment 수행 |

---

## 🧩 테마 3: Model Merging & LoRA Composition

서로 다른 능력(CoT vs Graph)을 가진 모델/어댑터를 합치는 최신 기법입니다.

| # | 논문 | 학회 | 링크 | 핵심 아이디어 |
|---|------|------|------|--------------|
| 1 | **LoRA Soups: Merging LoRAs for Practical Skill Composition Tasks** | COLING 2025 (Industry) | https://aclanthology.org/2025.coling-industry.55/ | CAT 방식으로 LoRA 가중치 최적 조합 학습 |
| 2 | **LoRAHub: Efficient Cross-Task Generalization via Dynamic LoRA Composition** | NeurIPS 2023 / COLM 2024 | https://arxiv.org/abs/2307.13269 | Gradient-free 최적화(CMA-ES)로 LoRA 계수 조정 |
| 3 | **Merging LoRAs like Playing LEGO (LoRA-LEGO)** | arXiv 2024 | https://arxiv.org/abs/2409.16167 | Rank-wise clustering으로 LoRA 재조립 |
| 4 | **Model merging with SVD to tie the Knots (KnOTS)** | arXiv 2024 | https://arxiv.org/abs/2410.19735 | SVD 기반 변환으로 LoRA 서브스페이스 정렬 |
| 5 | **Unraveling LoRA Interference: Orthogonal Subspaces (OSRM)** | ACL 2025 | https://arxiv.org/abs/2505.22934 | 업데이트 서브스페이스 직교화로 간섭 완화 |
| 6 | **Evolutionary Optimization of Model Merging Recipes** | arXiv 2024 (Sakana AI) | https://arxiv.org/abs/2403.13187 | 유전 알고리즘으로 최적 병합 비율 탐색 |
| 7 | **WARM: On the Benefits of Weight Averaged Reward Models** | ICLR 2024 | https://arxiv.org/abs/2401.12187 | 체크포인트 병합으로 Reward Hacking 방지 |
| 8 | **Improving LoRA via Reparameterization and Initialization Techniques** | NAACL 2025 (Findings) | https://aclanthology.org/2025.findings-naacl.429/ | LoRA 재매개변수화 및 초기화 개선 |
| 9 | **Efficient Parameter-Efficient Fine-Tuning of Large Models** | ACL 2025 | https://aclanthology.org/2025.acl-long.575/ | 효율적 PEFT 방법론 |
| 10 | **Block Diffusion: Interpolating Between AR and Diffusion Language Models** | ICLR 2025 (Oral) | https://openreview.net/forum?id=tyEyYT267x | AR과 Diffusion 모델 보간 |

---

## 📐 테마 4: Math Reasoning & Knowledge Graph Integration

그래프 구조와 수학적 추론을 결합하는 연구입니다.

| # | 논문 | 학회 | 링크 | 핵심 아이디어 |
|---|------|------|------|--------------|
| 1 | **Graph of Thoughts: Solving Elaborate Problems with LLMs** | AAAI 2024 | https://arxiv.org/abs/2308.09687 | LLM 정보를 그래프 구조로 표현, 병합/피드백 루프 |
| 2 | **Self-attention-based Graph-of-Thought for Math (SaGoT)** | ACL 2025 (Findings) | https://aclanthology.org/2025.findings-acl.317/ | Self-attention 변형으로 그래프식 추론 |
| 3 | **Think-on-Graph: Deep and Responsible Reasoning with KGs** | ICLR 2024 | https://arxiv.org/abs/2307.07697 | KG 위에서 Beam Search하며 추론 |
| 4 | **Graph-constrained Reasoning: Faithful Reasoning on KGs** | ICML 2025 | https://openreview.net/forum?id=GCR_KGT | KG-Trie + constrained decoding으로 환각 감소 |
| 5 | **Graph Reasoning with LLMs** | ACL 2025 | https://aclanthology.org/2025.acl-long.537/ | Graph→Text 변환 및 통합 방법 |
| 6 | **Decoding on Graphs: Faithful and Sound Reasoning on KGs** | ACL 2025 | https://aclanthology.org/2025.acl-long.1186/ | KG에서의 faithful reasoning |
| 7 | **ARise: Towards Knowledge-Augmented Reasoning via Risk-Adaptive Search** | ACL 2025 | https://aclanthology.org/2025.acl-long.538/ | 위험 적응 탐색을 통한 지식 증강 추론 |
| 8 | **Knowledge-Augmented Multimodal Clinical Rationale Generation with SLMs** | ACL 2025 | https://aclanthology.org/2025.acl-long.540/ | SLM + KG 통합 실제 적용 사례 |
| 9 | **Understand, Solve and Translate: Bridging Multilingual Math Reasoning Gap (HRM8K/UST)** | MRL Workshop 2025 | https://arxiv.org/abs/2502.18878 | 한국어 포함 다국어 수학 벤치마크 |
| 10 | **Buffer of Thoughts: Thought-Augmented Reasoning with LLMs** | NeurIPS 2024 | https://arxiv.org/abs/2406.04271 | Thought Template + Meta-Buffer 검색 |
| 11 | **Orca-Math: Unlocking the Potential of SLMs in Grade School Math** | arXiv 2024 (Microsoft) | https://arxiv.org/abs/2402.14830 | Agent-Instruct로 7B가 100B급 성능 달성 |
| 12 | **Self-Discover: Large Language Models Self-Compose Reasoning Structures** | NeurIPS 2024 | https://arxiv.org/abs/2402.03620 | JSON 형태 추론 모듈 자동 생성 |
| 13 | **AlphaMath / DeepSeek-Math: Process Supervision for Mathematics** | arXiv 2024 | https://arxiv.org/abs/2401.07405 | MCTS로 트리 탐색 + 단계별 Process Reward |
| 14 | **Enhancing Mathematical Reasoning in LLMs by Stepwise Correction** | ACL 2025 | https://aclanthology.org/2025.acl-long.1048/ | 단계별 교정을 통한 수학 추론 향상 |
| 15 | **Enhancing CoT Reasoning with Critical Representation Fine-tuning** | ACL 2025 | https://aclanthology.org/2025.acl-long.1129/ | Critical representation으로 CoT 품질 개선 |
| 16 | **GraphGPT: Graph Instruction Tuning for LLMs** | SIGIR 2024 | https://arxiv.org/abs/2310.13023 | 텍스트↔그래프 정렬 + dual-stage projector |
| 17 | **Improving Recall of LLMs: Model Collaboration for Relational Triple Extraction** | LREC-COLING 2024 | https://arxiv.org/abs/2404.09593 | 65B 평가 + 7B 추출 협업으로 recall 향상 |

---

## 📚 기타/배경 논문

| # | 논문 | 학회 | 링크 | 비고 |
|---|------|------|------|------|
| 1 | Distillation with Explanations from Large Language Models | LREC-COLING 2024 | https://aclanthology.org/2024.lrec-main.449/ | 설명 데이터 생성/정제 파이프라인 |
| 2 | Scaling Laws for Precision | ICLR 2025 (Oral) | https://openreview.net/forum?id=wg1PCg3CUP | 양자화 scaling laws |

---

## 🔍 검증 필요 (Placeholder/TBD)

아래 항목은 공식 URL 확인이 필요한 논문입니다.

| # | 논문명 | 출처 | 상태 |
|---|--------|------|------|
| 1 | CoT-Decoding: Chain-of-Thought Decoding with Logic Constraints | Gemini-pro 추천 | TBD (placeholder 링크, 실제 논문 확인 필요) |

---

## 📊 통계 요약

| 테마 | 논문 수 |
|------|---------|
| Structured Rationale Distillation | 30 |
| Test-time Scaling & Inference | 29 |
| Model Merging & LoRA | 10 |
| Math Reasoning & KG Integration | 17 |
| 기타/배경 | 2 |
| **총계 (중복 제거)** | **~85** |

---

## 📎 출처 파일 목록

- `papars.yaml` — 12편 (기본 후보)
- `2nd-recommendation.md` — 순차 추천 기록
- `3rd-recommendation.md` — 순차 추천 기록
- `recommended-papers-2025-by-GPT-5.2.md` — 15편
- `recommended-papers-2025-by-GPT-5.2-pro.md` — 15편
- `recommended-papers-2025-by-GPT-5.2-research.md` — 9편
- `recommended-papers-2025-by-GPT-5.2-think.md` — 15편
- `recommended-papers-2025-by-GPT-5.2-agent.md` — 11편
- `recommended-papers-2025-by-Gemini-pro.md` — 12편
- `recommended-papers-2025-by-Opus.md` — 21편

---

## 🔗 관련 문서

- [MUST-READ-PLAN.md](MUST-READ-PLAN.md) — 정본 must-read + 4주 실행 계획
- [../PLAN.md](../PLAN.md) — 연구 3축(Axis) 정의
