# 추천 논문 목록 (2025년 12월 기준)

본 목록은 2025년 12월 23일 기준으로, 사용자께서 요청하신 4가지 핵심 연구 주제(Structured Rationale Distillation, Test-time Scaling, Model Merging, Math Reasoning)에 맞춰 선별된 최신 논문들입니다.

## 1. Structured Rationale Distillation & Reasoning

- title: "Knowledge Distillation with Structured Chain-of-Thought for Text-to-SQL"
  venue: "arXiv (Dec 2025)"
  link: "https://arxiv.org/abs/2512.17053"
  idea: "비정형 CoT 대신 구조화된(Structured) CoT를 사용하여 LLM의 추론 과정을 SLM에 증류하는 방법론 제안."
  relevance: "연구 주제 1번(Structured Rationale Distillation)과 정확히 일치하며, JSON/Graph 형태의 중간 표현 증류 실험에 직접적인 참고가 됨."
  tips: "구조화된 CoT 포맷 정의 및 Student 모델의 학습 Loss 설계 부분 참고."

- title: "Thinking with DistilQwen: A Tale of Four Distilled Reasoning and Reward Model Series"
  venue: "EMNLP 2025 (Industry Track)"
  link: "https://arxiv.org/abs/2511.01354"
  idea: "Qwen 모델을 기반으로 Reasoning 및 Reward Model을 증류하는 4가지 시리즈 모델에 대한 분석 및 방법론."
  relevance: "최신 SLM(Qwen) 기반의 추론 증류 기법과 Reward Model 학습 노하우를 파악할 수 있음."
  tips: "Distillation 데이터셋 구성 및 Teacher 모델의 Reasoning Trace 필터링 기법."

- title: "Effectiveness of Chain-of-Thought in Distilling Reasoning Capability from Large Language Models"
  venue: "INLG 2025"
  link: "https://arxiv.org/abs/2511.05184"
  idea: "LLM의 CoT가 SLM 증류 시 미치는 영향을 체계적으로 분석하고, 효과적인 CoT 증류 전략 제시."
  relevance: "CoT 증류의 효율성을 높이기 위한 데이터 선별 및 프롬프트 전략 수립에 유용."
  tips: "CoT 유무에 따른 성능 비교 실험 및 실패 케이스 분석 섹션."

## 2. Test-time Scaling & Inference Optimization

- title: "The Art of Scaling Test-Time Compute for Large Language Models"
  venue: "arXiv (Dec 2025)"
  link: "https://arxiv.org/abs/2512.02008"
  idea: "다양한 Test-time scaling 전략(Best-of-N, Verifier 등)을 300억 토큰 규모로 대규모 비교 분석하여 최적의 전략 도출."
  relevance: "연구 질문 RQ2(비용 효율적인 Test-time scaling)에 대한 해답을 줄 수 있는 가장 포괄적인 연구."
  tips: "모델 크기 및 문제 난이도에 따른 최적 Scaling 전략 가이드라인 (Figure/Table)."

- title: "SCALE: Selective Resource Allocation for Overcoming Performance Bottlenecks in Mathematical Test-time Scaling"
  venue: "AAAI 2026 (Accepted)"
  link: "https://arxiv.org/abs/2512.00466"
  idea: "모든 문제에 동일한 리소스를 쓰는 대신, 하위 문제의 난이도를 평가하여 'System 2' 사고가 필요한 곳에만 연산을 집중하는 프레임워크."
  relevance: "SLM의 제한된 리소스를 효율적으로 사용하여 수학 추론 성능을 극대화하는 전략으로 매우 적합."
  tips: "난이도 평가 모듈(Difficulty Assessment) 구현 및 리소스 할당 알고리즘."

- title: "On the Limits of Test-Time Compute: Sequential Reward Filtering for Better Inference"
  venue: "arXiv (Dec 2025)"
  link: "https://arxiv.org/abs/2512.04558"
  idea: "단순 Best-of-N이 아닌, Reward 기반으로 생성된 후보를 순차적으로 필터링하여 문맥에 포함시키는 방식이 더 강력함을 이론/실험적으로 증명."
  relevance: "Verifier/Reward Model을 활용한 고도화된 추론 전략 수립에 기여."
  tips: "Reward-filtered Sequential Inference 알고리즘 및 이론적 증명 부분."

- title: "Zero-Overhead Introspection for Adaptive Test-Time Compute"
  venue: "arXiv (Dec 2025)"
  link: "https://arxiv.org/abs/2512.01457"
  idea: "별도의 Verifier 모델 없이, 생성 모델 자체의 Logit을 활용하여 자신의 성공 가능성과 필요 연산량을 예측(Introspection)하는 ZIP-RC 방법론."
  relevance: "추가 모델 로딩 없이 SLM 단독으로 효율적인 Test-time scaling을 구현할 수 있는 실용적인 방법."
  tips: "ZIP-RC 학습 방법 및 Inference 시점의 종료 조건 설정."

- title: "DeepSeekMath-V2: Towards Self-Verifiable Mathematical Reasoning"
  venue: "arXiv (Nov 2025)"
  link: "https://arxiv.org/abs/2511.22570"
  idea: "수학 증명 과정에서 스스로 검증(Self-verification) 가능한 모델을 학습시키고, 이를 통해 Test-time scaling 효과를 극대화."
  relevance: "수학 도메인 특화 SLM 개발 및 Self-correction 메커니즘 연구에 필수적인 레퍼런스."
  tips: "Proof Generator와 Verifier의 상호작용 학습 파이프라인."

## 3. Model Merging & LoRA Composition

- title: "FlyLoRA: Boosting Task Decoupling and Parameter Efficiency via Implicit Rank-Wise Mixture-of-Experts"
  venue: "NeurIPS 2025"
  link: "https://arxiv.org/abs/2510.08396"
  idea: "초파리 후각 신경망에서 영감을 받아, LoRA의 Rank를 Expert처럼 활용하여 Task 간 간섭을 줄이고 병합 효율을 높이는 방법."
  relevance: "서로 다른 태스크(예: CoT, CG)로 학습된 LoRA를 효과적으로 병합(Merging)하는 새로운 접근법."
  tips: "Implicit Router 구현 및 Rank-wise Expert 할당 방식."

- title: "Unraveling LoRA Interference: Orthogonal Subspaces for Robust Model Merging"
  venue: "ACL 2025"
  link: "https://arxiv.org/abs/2505.22934"
  idea: "LoRA 학습 시 Subspace를 직교(Orthogonal)하게 제약하여, 추후 병합 시 파라미터 간섭을 최소화하는 OSRM 방법론."
  relevance: "연구 질문 RQ3(서로 다른 추론 스타일 병합) 해결을 위한 핵심 기술로, 병합 성능 저하를 막는 방법."
  tips: "Orthogonal Constraint Loss 구현 및 병합 실험 결과."

- title: "Merging LoRAs like Playing LEGO: Pushing the Modularity of LoRA to Extremes Through Rank-Wise Clustering"
  venue: "ICLR 2025"
  link: "https://arxiv.org/abs/2409.16167"
  idea: "LoRA를 더 작은 단위(Minimal Semantic Units)로 쪼개고 재조립(Clustering)하여 새로운 기능을 조합하는 프레임워크."
  relevance: "다양한 능력을 가진 Adapter들을 유연하게 조합하여 SLM의 능력을 확장하는 아이디어."
  tips: "Rank-wise Clustering 알고리즘 및 LoRA-LEGO 프레임워크 구조."

## 4. Math Reasoning & Knowledge Graph

- title: "Efficient Multi-Hop Question Answering over Knowledge Graphs via LLM Planning and Embedding-Guided Search"
  venue: "arXiv (Nov 2025)"
  link: "https://arxiv.org/abs/2511.19648"
  idea: "LLM의 Planning 능력과 KG Embedding 검색을 결합하여 Multi-hop 추론 효율성을 높이는 방법."
  relevance: "KG와 LLM/SLM을 결합하여 복잡한 추론 문제를 해결하는 하이브리드 접근법 참고."
  tips: "LLM Planner와 KG Search 모듈 간의 인터페이스 설계."

- title: "Think Twice: Branch-and-Rethink Reasoning Reward Model"
  venue: "arXiv (Oct 2025)"
  link: "https://arxiv.org/abs/2510.23596"
  idea: "한 번에 점수를 매기는 기존 Reward Model 대신, 중요한 분기점에서 다시 생각(Rethink)하고 평가하는 2-turn Reward Model."
  relevance: "고성능 Verifier 개발을 위한 새로운 아키텍처로, SLM의 자기 검증 능력 향상에 기여."
  tips: "Branch-and-Rethink 프로세스 및 학습 데이터 구성."

---

## 요약 및 제언

1.  **Test-time Scaling의 대중화**: 2025년 하반기 연구들은 단순히 모델 크기를 키우는 것보다, **Inference 시점에 연산을 더 많이(Adaptive Compute)** 하여 성능을 높이는 쪽에 집중하고 있습니다. 특히 **"The Art of Scaling..."** 논문과 **"SCALE"** 논문은 필독을 권장합니다.
2.  **LoRA Merging의 고도화**: 단순 병합(Averaging)을 넘어, 학습 단계에서부터 병합을 고려한 **Orthogonal Training**이나 **Mixture-of-Experts** 방식의 병합이 주류를 이루고 있습니다. **FlyLoRA**와 **OSRM**은 꼭 확인해보시기 바랍니다.
3.  **Structured Distillation**: Text-to-SQL 등 구조화된 출력이 필요한 분야에서 **Structured CoT** 증류가 효과적임이 입증되고 있습니다. 이를 수학 문제의 **Concept Graph** 증류에 적용하면 좋은 성과가 있을 것으로 예상됩니다.
