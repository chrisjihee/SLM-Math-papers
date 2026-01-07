# 추천 논문 통합 목록 (Unified Paper List)

**Last updated:** 2026-01-07
**총 논문 수:** 55편 (정리 후)

이 문서는 저장소 내 추천 논문 자료를 **연구 방향(PLAN.md 3축)에 맞게 정선**한 정본입니다.

> **연구 3축 (PLAN.md)**:
> - **Axis 1**: CoT vs CG — 구조화된 Rationale의 데이터 효율성
> - **Axis 2**: Test-time Inference Scaling — SLM에서의 비용 효율적 추론
> - **Axis 3**: Model Merging + DPO — 서로 다른 추론 스타일 병합

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

SLM에게 CoT/그래프 구조를 효율적으로 증류하는 연구들입니다. (**Axis 1 핵심**)

| # | 논문 | 학회 | 링크 | 핵심 아이디어 |
|---|------|------|------|--------------|
| 1 | **UniCoTT: A Unified Framework for Structural Chain-of-Thought Distillation** ⭐ | ICLR 2025 | https://openreview.net/forum?id=3baOKeI2EU | Chain/Tree/Graph 형태의 구조적 CoT를 통합 포맷으로 SLM에 증류 |
| 2 | **MAGDi: Structured Distillation of Multi-Agent Interaction Graphs** ⭐ | ICLR 2025 (Spotlight) | https://arxiv.org/abs/2402.01620 | GPT-4 다중 에이전트 토론을 논증 그래프로 변환 후 증류 |
| 3 | **Mentor-KD: Making Small Language Models Better Multi-step Reasoners** ⭐ | EMNLP 2024 | https://arxiv.org/abs/2410.09037 | 70B→13B Mentor→7B 학생의 2단계 KD + soft label |
| 4 | **SWITCH: Studying WItH TeaCHer for Knowledge Distillation of LLMs** ⭐ | EMNLP 2024 | https://arxiv.org/abs/2410.19503 | 긴 시퀀스에서 오류 토큰만 선택적 교사介入 KD |
| 5 | **InstructGraph: Boosting LLMs via Graph-centric Instruction Tuning** ⭐ | ACL 2024 (Findings) | https://arxiv.org/abs/2402.08785 | 그래프 중심 IT + preference alignment로 환각 감소 |
| 6 | **QCRD: Quality-guided Contrastive Rationale Distillation** | arXiv 2024 | https://arxiv.org/abs/2405.13014 | 고품질/저품질 rationale을 대비 학습으로 증류 |
| 7 | **Distilling Reasoning Ability from LLMs with Adaptive Thinking** | arXiv 2024 | https://arxiv.org/abs/2404.09170 | 난이도에 따라 생각 길이를 적응적으로 조절 |
| 8 | **Symbolic Chain-of-Thought Distillation (SCoTD)** | ACL 2023 | https://arxiv.org/abs/2306.14050 | 교사 LLM의 다양한 CoT 샘플링으로 소형 모델 증류 |
| 9 | **Beyond Answers: Multi-Teacher Knowledge Distillation (TinyLLM)** | WSDM 2025 | https://arxiv.org/abs/2402.04616 | 여러 교사 LLM의 답+추론을 통합 증류 |
| 10 | **Keypoint-based Progressive Chain-of-Thought Distillation** | ICML 2024 | https://proceedings.mlr.press/v202/feng24a.html | 중요 토큰 가중치 + 역순 커리큘럼 학습 |
| 11 | **MoDE-CoTD: CoT Distillation with Mixture of Decoupled LoRA-Experts** | LREC-COLING 2024 | https://aclanthology.org/2024.lrec-main.1003 | 여러 태스크별 LoRA 전문가를 병합 증류 |
| 12 | **Unveiling the Key Factors for Distilling CoT Reasoning** | ACL 2025 (Findings) | https://aclanthology.org/2025.findings-acl.782 | CoT 세분화/포맷/교사 규모의 체계적 분석 |
| 13 | **Learning to Maximize Mutual Information for CoT Distillation** | ACL 2024 (Findings) | https://aclanthology.org/2024.findings-acl.577/ | 정답+CoT 간 상호정보량(MI) 최대화 |
| 14 | **Teaching SLMs Reasoning through Counterfactual Distillation** | EMNLP 2024 | https://aclanthology.org/2024.emnlp-main.333/ | Counterfactual 데이터 + multi-view CoT |
| 15 | **Distilling Mathematical Reasoning Capabilities (EoTD/ETD)** | arXiv 2024 | https://arxiv.org/abs/2401.11864 | 수식 형태 중간표현(EoT) + Ensemble Thoughts |
| 16 | **DRAG: Distilling RAG for SLMs via Evidence and Graph-based Distillation** | ACL 2025 | https://arxiv.org/abs/2506.01954 | 증거 순위 + KG를 다중 loss로 증류 |
| 17 | **Contextualization Distillation from LLM for KG Completion** | EACL 2024 (Findings) | https://arxiv.org/abs/2402.01729 | Triple→자연어 문맥으로 재작성 후 증류 |
| 18 | **Learning from Committee: Reasoning Distillation from a Mixture of Teachers** | ACL 2025 (Findings) | https://aclanthology.org/2025.findings-acl.217/ | 여러 Teacher 모델의 Reasoning 통합 증류 |
| 19 | **Quantification of Large Language Model Distillation** | ACL 2025 | https://aclanthology.org/2025.acl-long.248/ | LLM 증류 효과 정량화 방법론 |

---

## 🚀 테마 2: Test-time Scaling & Inference Optimization

SLM이 추론 시점에 더 많이/효율적으로 생각하여 성능을 높이는 방법론입니다. (**Axis 2 핵심**)

| # | 논문 | 학회 | 링크 | 핵심 아이디어 |
|---|------|------|------|--------------|
| 1 | **Scaling LLM Test-Time Compute Optimally** ⭐⭐ | ICLR 2025 (Oral) | https://openreview.net/forum?id=4FWAwZtd2n | Test-time compute가 parameter scaling보다 효과적일 수 있음 |
| 2 | **Rewarding Progress: Scaling Automated Process Verifiers** ⭐ | ICLR 2025 (Spotlight) | https://openreview.net/forum?id=A6Y7AqlzLW | Progress 기반 prover policy + PRM 스케일링 |
| 3 | **Process Reward Models That Think (ThinkPRM)** ⭐ | arXiv 2025 | https://arxiv.org/abs/2504.16828 | 생성적 PRM으로 데이터 효율/서치 성능 향상 |
| 4 | **Let's Verify Step by Step** ⭐ | ICLR 2024 | https://arxiv.org/abs/2305.20050 | PRM800K + Process vs Outcome supervision |
| 5 | **Kinetics: Rethinking Test-Time Scaling Laws** | arXiv 2025 | https://arxiv.org/abs/2506.05333 | 모델 크기별 TTS 비용-효율 분석 |
| 6 | **Can 1B LLM Surpass 405B LLM? Compute-Optimal Test-Time Scaling** | arXiv 2025 | https://arxiv.org/abs/2502.06703 | 소형 모델이 유리한 컴퓨트 구간 분석 |
| 7 | **Inference Scaling Laws: Compute-Optimal Inference** | arXiv 2024 | https://arxiv.org/abs/2408.00724 | Best-of-N, voting, tree-search 비용 효율 분석 |
| 8 | **s1: Simple test-time scaling** | arXiv 2025 | https://arxiv.org/abs/2501.19393 | s1K 데이터 구성 + budget forcing 기법 |
| 9 | **Small Language Models Need Strong Verifiers to Self-Correct** | ACL 2024 (Findings) | https://aclanthology.org/2024.findings-acl.924 | 강력한 LLM 피드백으로 SLM 자기정정 학습 |
| 10 | **Reasoning-Aware Self-Consistency (RASC)** | NAACL 2025 | https://aclanthology.org/2025.naacl-main.184 | 추론 경로 품질 평가로 SC 효율화 (70-90% 샘플 절약) |
| 11 | **rStar: Small LLMs Can Master Math Reasoning** | arXiv 2025 | https://arxiv.org/abs/2501.04519 | MCTS + PPM 자기진화로 7B가 O1 수준 달성 |
| 12 | **Soft Self-Consistency Improves Language Models Agents** | ACL 2024 (Short) | https://aclanthology.org/2024.acl-short.28/ | 확률값 가중 투표로 SC 효율화 |
| 13 | **Boosting SLMs with Self-Consistency Training (MC-CoT)** | ECCV 2024 | https://arxiv.org/abs/2311.14109 | Train-time에 SC 아이디어 도입 |
| 14 | **Beyond the First Error: PRM for Reflective Reasoning** | EMNLP 2025 (Findings) | https://aclanthology.org/2025.findings-emnlp.253/ | Error Propagation/Cessation 규칙으로 PRM 학습 |
| 15 | **Process Reward Model with Q-value Rankings** | ICLR 2025 (Poster) | https://openreview.net/forum?id=wQEdh2cgEk | Q-value 기반 랭킹으로 PRM 학습 |
| 16 | **V-STaR: Training Verifiers for Self-Taught Reasoners** | ICLR 2024 | https://arxiv.org/abs/2402.06457 | 정답/오답 데이터로 Verifier 학습 + DPO 결합 |
| 17 | **Quiet-STaR: LMs Can Teach Themselves to Think Before Speaking** | arXiv 2024 | https://arxiv.org/abs/2403.09629 | 모든 토큰에 내적 독백(Rationale) 생성 |
| 18 | **Are More LLM Calls All You Need? Compound Inference Scaling** | arXiv 2024 | https://arxiv.org/abs/2403.02419 | Vote/Filter/Chain 복합 추론 Scaling Law 분석 |
| 19 | **Process-supervised Reward Model in Mathematical Reasoning** | ACL 2025 | https://aclanthology.org/2025.acl-long.216/ | 수학 추론에서의 PRM 활용 |

---

## 🧩 테마 3: Model Merging & LoRA Composition

서로 다른 능력(CoT vs CG)을 가진 모델/어댑터를 합치는 최신 기법입니다. (**Axis 3 핵심**)

| # | 논문 | 학회 | 링크 | 핵심 아이디어 |
|---|------|------|------|--------------|
| 1 | **LoRA Soups: Merging LoRAs for Practical Skill Composition** ⭐ | COLING 2025 (Industry) | https://aclanthology.org/2025.coling-industry.55/ | CAT 방식으로 LoRA 가중치 최적 조합 학습 |
| 2 | **Unraveling LoRA Interference: Orthogonal Subspaces (OSRM)** ⭐ | ACL 2025 | https://arxiv.org/abs/2505.22934 | 업데이트 서브스페이스 직교화로 간섭 완화 |
| 3 | **LoRAHub: Efficient Cross-Task Generalization via Dynamic LoRA Composition** | NeurIPS 2023 / COLM 2024 | https://arxiv.org/abs/2307.13269 | Gradient-free 최적화(CMA-ES)로 LoRA 계수 조정 |
| 4 | **Merging LoRAs like Playing LEGO (LoRA-LEGO)** | arXiv 2024 | https://arxiv.org/abs/2409.16167 | Rank-wise clustering으로 LoRA 재조립 |
| 5 | **Model merging with SVD to tie the Knots (KnOTS)** | arXiv 2024 | https://arxiv.org/abs/2410.19735 | SVD 기반 변환으로 LoRA 서브스페이스 정렬 |
| 6 | **Evolutionary Optimization of Model Merging Recipes** | arXiv 2024 (Sakana AI) | https://arxiv.org/abs/2403.13187 | 유전 알고리즘으로 최적 병합 비율 탐색 |
| 7 | **WARM: On the Benefits of Weight Averaged Reward Models** | ICLR 2024 | https://arxiv.org/abs/2401.12187 | 체크포인트 병합으로 Reward Hacking 방지 |

---

## 📐 테마 4: Math Reasoning & Knowledge Graph Integration

그래프 구조와 수학적 추론을 결합하는 연구입니다. (Axis 1, 2와 결합 활용)

| # | 논문 | 학회 | 링크 | 핵심 아이디어 |
|---|------|------|------|--------------|
| 1 | **Graph of Thoughts: Solving Elaborate Problems with LLMs** | AAAI 2024 | https://arxiv.org/abs/2308.09687 | LLM 정보를 그래프 구조로 표현, 병합/피드백 루프 |
| 2 | **Think-on-Graph: Deep and Responsible Reasoning with KGs** ⭐ | ICLR 2024 | https://arxiv.org/abs/2307.07697 | KG 위에서 Beam Search하며 추론 |
| 3 | **Graph-constrained Reasoning: Faithful Reasoning on KGs** | ICML 2025 | https://openreview.net/forum?id=GCR_KGT | KG-Trie + constrained decoding으로 환각 감소 |
| 4 | **Buffer of Thoughts: Thought-Augmented Reasoning** | NeurIPS 2024 | https://arxiv.org/abs/2406.04271 | Thought Template + Meta-Buffer 검색 |
| 5 | **Orca-Math: Unlocking the Potential of SLMs in Grade School Math** ⭐ | arXiv 2024 (Microsoft) | https://arxiv.org/abs/2402.14830 | Agent-Instruct로 7B가 100B급 성능 달성 |
| 6 | **Self-Discover: LLMs Self-Compose Reasoning Structures** | NeurIPS 2024 | https://arxiv.org/abs/2402.03620 | JSON 형태 추론 모듈 자동 생성 |
| 7 | **AlphaMath / DeepSeek-Math: Process Supervision for Mathematics** | arXiv 2024 | https://arxiv.org/abs/2401.07405 | MCTS로 트리 탐색 + 단계별 Process Reward |
| 8 | **Enhancing Mathematical Reasoning by Stepwise Correction** | ACL 2025 | https://aclanthology.org/2025.acl-long.1048/ | 단계별 교정을 통한 수학 추론 향상 |
| 9 | **GraphGPT: Graph Instruction Tuning for LLMs** | SIGIR 2024 | https://arxiv.org/abs/2310.13023 | 텍스트↔그래프 정렬 + dual-stage projector |
| 10 | **Understand, Solve and Translate (HRM8K/UST)** | MRL Workshop 2025 | https://arxiv.org/abs/2502.18878 | 한국어 포함 다국어 수학 벤치마크 |

---

## 📚 참고 자료 (Optional)

| # | 논문 | 학회 | 링크 | 비고 |
|---|------|------|------|------|
| 1 | Distillation with Explanations from LLMs | LREC-COLING 2024 | https://aclanthology.org/2024.lrec-main.449/ | 설명 데이터 생성/정제 파이프라인 |

---

## 📊 통계 요약

| 테마 | 논문 수 | 핵심(⭐) |
|------|---------|----------|
| Structured Rationale Distillation | 19 | 5 |
| Test-time Scaling & Inference | 19 | 4 |
| Model Merging & LoRA | 7 | 2 |
| Math Reasoning & KG Integration | 10 | 2 |
| **총계** | **55** | **13** |

> **정리 기준**: PLAN.md의 3축(CoT vs CG, Test-time Scaling, Model Merging)과 직결되는 논문 위주로 정선. 코드 생성, 역방향 증류, Diffusion 모델, Long-context RAG 등 연구 방향과 거리가 먼 30편 제외.

---

## 🔗 관련 문서

- [MUST-READ-PLAN.md](MUST-READ-PLAN.md) — 정본 must-read + 4주 실행 계획
- [../PLAN.md](../PLAN.md) — 연구 3축(Axis) 정의
- `papars.yaml` — 초기 후보 풀 (12편)
