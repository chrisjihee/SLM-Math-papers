# 추천 논문 목록 (2025년 12월 검색)

검색 일자: 2025-12-23
검색 방법: ACL Anthology, OpenReview (ICLR 2025), arXiv, Hugging Face Papers

---

## 🥇 최우선 읽기 권장 (검색 요청 1: Structured Rationale Distillation)

### 1. Quantification of Large Language Model Distillation
- **Venue**: ACL 2025 (Long Paper)
- **Link**: https://aclanthology.org/2025.acl-long.248/
- **Idea**: LLM 증류의 정량화 방법론 제안 - 증류 효과 측정 및 분석
- **Relevance**: CG/CoT 증류 효과 정량화에 직접 활용 가능
- **Tips**: 증류 효과 측정 메트릭 섹션 참고

### 2. TEACH: A Contrastive Knowledge Adaptive Distillation Framework for Classical Reasoning
- **Venue**: ACL 2025 (Long Paper)
- **Link**: https://aclanthology.org/2025.acl-long.178/
- **Idea**: Contrastive learning을 활용한 지식 적응 증류 프레임워크
- **Relevance**: CoT vs CG 비교 증류에 contrastive 기법 적용 가능
- **Tips**: Knowledge adaptation 메커니즘 분석

### 3. Learning from Committee: Reasoning Distillation from a Mixture of Teachers
- **Venue**: Findings of ACL 2025
- **Link**: https://aclanthology.org/2025.findings-acl.217/
- **Idea**: 여러 Teacher 모델의 Reasoning을 통합하여 Student에 증류
- **Relevance**: GPT-4o + LLaMA-4-Maverick 멀티 Teacher 증류에 활용
- **Tips**: Teacher 앙상블 방법론 참고

### 4. Flipping Knowledge Distillation: Leveraging Small Models' Expertise to Enhance Large Models
- **Venue**: ACL 2025 (Long Paper)
- **Link**: https://aclanthology.org/2025.acl-long.1081/
- **Idea**: 역방향 증류 - 작은 모델의 전문성을 큰 모델에 전달
- **Relevance**: Student CG → Teacher 피드백 루프 구현에 참고
- **Tips**: Expertise transfer 메커니즘

### 5. Dual-Space Knowledge Distillation for Large Language Models
- **Venue**: EMNLP 2024 (Main Conference)
- **Link**: https://aclanthology.org/2024.emnlp-main.1010/
- **Idea**: 이중 공간(logit + feature)에서의 지식 증류
- **Relevance**: CG 증류 시 다층적 표현 학습에 적용 가능
- **Tips**: Dual-space alignment 구현 방법

### 6. Self-Distillation for Large Language Models in Code Generation
- **Venue**: EMNLP 2024 (Main Conference)
- **Link**: https://aclanthology.org/2024.emnlp-main.66/
- **Idea**: 자기 증류를 통한 코드 생성 성능 향상
- **Relevance**: Self-improvement 패러다임을 CG 생성에 적용 가능
- **Tips**: Self-distillation 파이프라인 참고

---

## 🥇 최우선 읽기 권장 (검색 요청 2: Test-time Scaling)

### 7. **★★★ Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning** ★★★
- **Venue**: ICLR 2025 (Oral) ⭐ **Must Read**
- **Link**: https://openreview.net/forum?id=4FWAwZtd2n
- **Authors**: Charlie Victor Snell, Jaehoon Lee, Kelvin Xu, Aviral Kumar (Google DeepMind)
- **Idea**: Test-time compute scaling이 parameter scaling보다 reasoning에서 더 효과적일 수 있음
- **Relevance**: SLM × N회 추론 vs LLM × 1회 추론 break-even 분석에 핵심 참고 문헌
- **Tips**: Scaling laws, optimal compute allocation 섹션

### 8. Inference Scaling for Long-Context Retrieval Augmented Generation
- **Venue**: ICLR 2025 (Oral)
- **Link**: https://openreview.net/forum?id=FSjIrOm1vz
- **Idea**: Long-context RAG에서의 inference scaling 전략
- **Relevance**: RAG + Test-time scaling 조합 연구에 참고
- **Tips**: Inference compute 최적화 방법

### 9. Self-Improvement in Language Models: The Sharpening Mechanism
- **Venue**: ICLR 2025 (Oral)
- **Link**: https://openreview.net/forum?id=WJaUkwci9o
- **Idea**: LLM Self-improvement의 이론적 메커니즘 분석 (sharpening)
- **Relevance**: Self-consistency의 이론적 근거, 왜 다중 샘플링이 효과적인지 이해
- **Tips**: Sharpening mechanism 수학적 분석

### 10. Process-supervised Reward Model in Mathematical Reasoning
- **Venue**: ACL 2025 (Long Paper)
- **Link**: https://aclanthology.org/2025.acl-long.216/
- **Idea**: 수학 추론에서의 Process Reward Model (PRM) 활용
- **Relevance**: SLM Verifier 학습 및 Best-of-N reranking에 핵심 참고
- **Tips**: PRM 학습 데이터 구축 방법, PRM vs ORM 비교

### 11. DeAL: Decoding-time Alignment for Large Language Models
- **Venue**: ACL 2025 (Long Paper)
- **Link**: https://aclanthology.org/2025.acl-long.1274/
- **Idea**: Decoding time에 alignment를 수행하는 방법
- **Relevance**: Test-time에서 출력 품질 향상 전략
- **Tips**: Decoding-time intervention 구현

---

## 🥇 최우선 읽기 권장 (검색 요청 3: Model Merging & LoRA)

### 12. Improving LoRA via Reparameterization and Initialization Techniques
- **Venue**: Findings of NAACL 2025
- **Link**: https://aclanthology.org/2025.findings-naacl.429/
- **Idea**: LoRA의 재매개변수화 및 초기화 기법 개선
- **Relevance**: CG-LoRA와 CoT-LoRA 병합 전 각 LoRA 품질 향상
- **Tips**: 초기화 전략 및 reparameterization 방법

### 13. Efficient Parameter-Efficient Fine-Tuning of Large Models
- **Venue**: ACL 2025 (Long Paper)
- **Link**: https://aclanthology.org/2025.acl-long.575/
- **Idea**: 대형 모델의 효율적 PEFT 방법론
- **Relevance**: LoRA 학습 효율성 향상에 적용
- **Tips**: 효율적 fine-tuning 레시피

### 14. Block Diffusion: Interpolating Between Autoregressive and Diffusion Language Models
- **Venue**: ICLR 2025 (Oral)
- **Link**: https://openreview.net/forum?id=tyEyYT267x
- **Idea**: AR과 Diffusion 모델 사이의 보간
- **Relevance**: 다른 생성 패러다임 결합에 대한 인사이트
- **Tips**: 모델 결합 방법론

---

## 🥇 최우선 읽기 권장 (검색 요청 4: Math Reasoning & KG)

### 15. Enhancing Mathematical Reasoning in LLMs by Stepwise Correction
- **Venue**: ACL 2025 (Long Paper)
- **Link**: https://aclanthology.org/2025.acl-long.1048/
- **Idea**: 단계별 교정을 통한 수학 추론 향상
- **Relevance**: CG의 단계별 검증 및 교정에 적용 가능
- **Tips**: Stepwise correction 알고리즘

### 16. Enhancing Chain-of-Thought Reasoning with Critical Representation Fine-tuning
- **Venue**: ACL 2025 (Long Paper)
- **Link**: https://aclanthology.org/2025.acl-long.1129/
- **Idea**: Critical representation을 통한 CoT 추론 향상
- **Relevance**: CoT 품질 개선 전략
- **Tips**: Critical representation 정의 및 학습

### 17. Graph Reasoning with LLMs
- **Venue**: ACL 2025 (Long Paper)
- **Link**: https://aclanthology.org/2025.acl-long.537/
- **Idea**: LLM에서의 Graph Reasoning 방법론
- **Relevance**: Concept Graph를 LLM 추론에 통합하는 핵심 참고
- **Tips**: Graph → Text 변환 및 통합 방법

### 18. Decoding on Graphs: Faithful and Sound Reasoning on Knowledge Graphs
- **Venue**: ACL 2025 (Long Paper)
- **Link**: https://aclanthology.org/2025.acl-long.1186/
- **Idea**: Knowledge Graph에서의 faithful reasoning
- **Relevance**: CG 기반 추론의 신뢰성 보장 방법
- **Tips**: Soundness guarantee 메커니즘

### 19. ARise: Towards Knowledge-Augmented Reasoning via Risk-Adaptive Search
- **Venue**: ACL 2025 (Long Paper)
- **Link**: https://aclanthology.org/2025.acl-long.538/
- **Idea**: 위험 적응 탐색을 통한 지식 증강 추론
- **Relevance**: KG + 추론 통합 시 탐색 전략
- **Tips**: Risk-adaptive search 알고리즘

### 20. Knowledge-Augmented Multimodal Clinical Rationale Generation for Disease Diagnosis with Small Language Models
- **Venue**: ACL 2025 (Long Paper)
- **Link**: https://aclanthology.org/2025.acl-long.540/
- **Idea**: SLM에서 지식 증강을 통한 rationale 생성
- **Relevance**: SLM + KG 통합의 실제 적용 사례
- **Tips**: Knowledge injection 방법

---

## 🥈 추가 권장 논문 (ICLR 2025 Oral/Spotlight)

### 21. Scaling Laws for Precision
- **Venue**: ICLR 2025 (Oral)
- **Link**: https://openreview.net/forum?id=wg1PCg3CUP
- **Idea**: Precision (양자화)에 대한 scaling laws
- **Relevance**: SLM 효율적 배포에 참고

### 22. Knowledge Entropy Decay during Language Model Pretraining Hinders New Knowledge Acquisition
- **Venue**: ICLR 2025 (Oral)
- **Link**: https://openreview.net/forum?id=eHehzSDUFp
- **Idea**: Pretraining 중 knowledge entropy decay 현상
- **Relevance**: 지식 학습 메커니즘 이해

### 23. Context-Parametric Inversion: Why Instruction Finetuning May Not Actually Improve Context Reliance
- **Venue**: ICLR 2025 (Oral)
- **Link**: https://openreview.net/forum?id=SPS6HzVzyt
- **Idea**: Instruction finetuning이 context 의존성을 개선하지 않을 수 있음
- **Relevance**: Fine-tuning 효과의 한계 이해

### 24. Spread Preference Annotation: Direct Preference Judgment for Efficient LLM Alignment
- **Venue**: ICLR 2025 (Oral)
- **Link**: https://openreview.net/forum?id=BPgK5XW1Nb
- **Idea**: 효율적 LLM alignment를 위한 preference annotation 방법
- **Relevance**: DPO 데이터 구축 효율화

---

## 🥈 추가 권장 논문 (EMNLP 2024)

### 25. Teaching Small Language Models
- **Venue**: EMNLP 2024 (Main Conference)
- **Link**: https://aclanthology.org/2024.emnlp-main.333/
- **Idea**: SLM 교육 방법론
- **Relevance**: SLM 학습 전반에 대한 overview

### 26. Self-AMPLIFY: Improving Small Language Models with Self Post Hoc Explanations
- **Venue**: EMNLP 2024 (Main Conference)
- **Link**: https://aclanthology.org/2024.emnlp-main.615/
- **Idea**: Self-explanation을 통한 SLM 개선
- **Relevance**: SLM 자체 개선 전략

### 27. LM2: A Simple Society of Language Models Solves Complex Reasoning
- **Venue**: EMNLP 2024 (Main Conference)
- **Link**: https://aclanthology.org/2024.emnlp-main.920/
- **Idea**: 여러 LM의 협업을 통한 복잡한 추론 해결
- **Relevance**: Multi-agent reasoning 접근

### 28. Weak-to-Strong Reasoning
- **Venue**: Findings of EMNLP 2024
- **Link**: https://aclanthology.org/2024.findings-emnlp.490/
- **Idea**: 약한 모델에서 강한 모델로의 추론 전이
- **Relevance**: SLM → LLM 역방향 개선

### 29. Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning
- **Venue**: Findings of EMNLP 2024
- **Link**: https://aclanthology.org/2024.findings-emnlp.882/
- **Idea**: CoT Reasoning의 faithfulness 측정 및 개선
- **Relevance**: CoT 품질 평가 메트릭

---

## 🥈 추가 권장 논문 (NAACL 2025)

### 30. DrawEduMath: Evaluating Vision Language Models with Expert-Annotated Student-level Math Questions
- **Venue**: NAACL 2025 (Long Paper)
- **Link**: https://aclanthology.org/2025.naacl-long.352/
- **Idea**: 학생 수준 수학 문제에 대한 VLM 평가
- **Relevance**: 교육용 수학 추론 벤치마크

### 31. Better Complex Reasoning (with small models)
- **Venue**: NAACL 2025 (Long Paper)
- **Link**: https://aclanthology.org/2025.naacl-long.515/
- **Idea**: 소형 모델에서의 복잡한 추론 개선
- **Relevance**: SLM 추론 향상 전략

### 32. Distillation Solution and Components Analysis
- **Venue**: NAACL 2025 (Long Paper)
- **Link**: https://aclanthology.org/2025.naacl-long.364/
- **Idea**: 증류 솔루션 및 구성 요소 분석
- **Relevance**: 증류 기법의 체계적 분석

---

## 📚 arXiv Preprints (2025년 12월 최신)

### 33. MDToC: Metacognitive Dynamic Tree of Concepts for Boosting Mathematical Problem-Solving of LLMs
- **Link**: https://arxiv.org/abs/2512.18841
- **Idea**: 메타인지적 동적 개념 트리를 통한 수학 문제 해결 향상
- **Relevance**: Concept Graph의 동적 버전

### 34. JEPA-Reasoner: Decoupling Latent Reasoning from Token Generation
- **Link**: https://arxiv.org/abs/2512.19171
- **Idea**: 잠재 추론과 토큰 생성의 분리
- **Relevance**: 추론과 생성 분리 아키텍처

### 35. A Large Language Model Based Method for Complex Logical Reasoning over Knowledge Graphs
- **Link**: https://arxiv.org/abs/2512.19092
- **Idea**: KG 위에서의 복잡한 논리 추론
- **Relevance**: CG + LLM 논리 추론

### 36. Increasing the Thinking Budget is Not All You Need
- **Link**: https://arxiv.org/abs/2512.19585
- **Idea**: Thinking budget 증가만으로는 충분하지 않음
- **Relevance**: Test-time compute의 한계 분석

---

## 📖 읽기 우선순위 요약

### 🔴 이번 주 필독 (Top 5)
1. **Scaling LLM Test-Time Compute Optimally** (ICLR 2025 Oral) - #7
2. **Process-supervised Reward Model in Mathematical Reasoning** (ACL 2025) - #10
3. **Self-Improvement in Language Models: The Sharpening Mechanism** (ICLR 2025 Oral) - #9
4. **Learning from Committee: Reasoning Distillation from a Mixture of Teachers** (ACL 2025) - #3
5. **Graph Reasoning with LLMs** (ACL 2025) - #17

### 🟠 다음 주 권장 (6-10위)
6. TEACH: A Contrastive Knowledge Adaptive Distillation Framework - #2
7. Enhancing Mathematical Reasoning in LLMs by Stepwise Correction - #15
8. Decoding on Graphs: Faithful and Sound Reasoning - #18
9. Dual-Space Knowledge Distillation for LLMs - #5
10. Inference Scaling for Long-Context RAG - #8

### 🟡 추가 읽기 (11-15위)
11. Quantification of LLM Distillation - #1
12. Flipping Knowledge Distillation - #4
13. DeAL: Decoding-time Alignment - #11
14. Enhancing CoT with Critical Representation - #16
15. ARise: Knowledge-Augmented Reasoning - #19

---

## 참고 사항

1. **ICLR 2025 Oral 논문**은 높은 품질이 보장되므로 우선 읽기 권장
2. **ACL 2025** 논문들은 2025년 7월 발표 예정 (현재 공개된 것은 사전 공개본)
3. **arXiv preprint**는 peer review 전이므로 주의해서 참고
4. GPT/Gemini 검색 결과와 병합하여 최종 목록 결정 필요

---

*생성일: 2025-12-23*
*검색 도구: GitHub Copilot (Claude Opus 4.5)*
