# Recommended papers (2023–2025) — 2025-12

아래는 요청하신 4개 테마(우선순위: **Structured distillation > Test-time scaling/PRM > Model merging/LoRA > Math/KG 배경**)에 맞춰, **중복(이미 알고 있는 고전/대표작)**을 피하면서 2023–2025 위주로 정리한 **15편**입니다.

- 원칙: venue는 OpenReview의 “Published/Decision” 또는 arXiv “Comments: accepted …”가 있는 경우에만 확정 표기, 그 외는 `arXiv`로 표기
- 포맷: 각 논문당 YAML 항목 1개

---

total: 15
papers:
  - title: "Reasoning Scaffolding: Distilling the Flow of Thought from LLMs"
    year: 2025
    venue: "arXiv"
    link: "https://arxiv.org/abs/2509.23619"
    themes:
      - structured_distillation
      - reasoning
    idea: "Flow-of-thought를 '의미 연산/담화 기능' 같은 이산 신호(예: Contrast, Addition) 시퀀스로 구조화해, (1) 다음 신호 예측 + (2) 해당 단계 생성 멀티태스크로 소형 모델에 이식."
    relevance: "CoT를 그대로 베끼기보다 '구조(계획/연산 흐름)'를 증류하는 접근이라 3B–8B에서 데이터 효율과 제어성을 함께 노리기 좋음."
    tips: "현재 파이프라인에서 rationale 텍스트를 그대로 학습시키는 대신, 중간에 'signal head'를 추가(분류/seq2seq)하거나, 단계별 태그를 pseudo-label로 생성해 보세요."

  - title: "Towards Efficient CoT Distillation: Self-Guided Rationale Selector for Small Language Models"
    year: 2025
    venue: "arXiv"
    link: "https://arxiv.org/abs/2509.23574"
    themes:
      - structured_distillation
      - data_curation
    idea: "교사 CoT 후보들 중에서 정확도/다양성/난이도 등을 고려해 '학습에 유리한 rationale'만 선택해 증류(자기유도 선택)."
    relevance: "현재 생성된 체인/풀이가 많을수록 좋은 게 아니라, 오히려 노이즈·편향이 커지는 경우가 많아 '선별 증류'가 실전에서 효율적."
    tips: "CG/MR/QA 데이터 생성 후, (a) 정답률, (b) step 길이/중복, (c) heuristic consistency로 스코어링해 상위 K만 distill하는 ablation을 권장."

  - title: "Skip-Thinking: Chunk-wise Chain-of-Thought Distillation Enables Smaller Language Models to Reason Better and Faster"
    year: 2025
    venue: "arXiv"
    link: "https://arxiv.org/abs/2505.18642"
    themes:
      - structured_distillation
      - efficiency
    idea: "CoT를 chunk 단위로 분리해 '추론에 기여하는 chunk'만 학습/생성하도록 하여, 불필요한 서술을 건너뛰는(distill+inference) 방식으로 속도와 성능을 같이 개선."
    relevance: "추론 토큰을 줄이면서도 정답률을 유지/개선하려는 목표(테스트타임 비용 절감)와 직결."
    tips: "학습 시 chunk 라벨(keep/skip)을 만들기 위해, step-wise PRM 또는 간단한 verifier로 chunk 중요도를 추정하는 조합이 유효할 가능성이 큼."

  - title: "Improving Mathematical Reasoning Capabilities of Small Language Models via Feedback-Driven Distillation"
    year: 2024
    venue: "arXiv"
    link: "https://arxiv.org/abs/2411.14698"
    themes:
      - structured_distillation
      - math_reasoning
    idea: "학생 모델의 실패 케이스를 기반으로 문제 변형/유사문제/단계 피드백을 생성해 데이터 자체를 다회전으로 증강하고 다시 증류(피드백 루프)."
    relevance: "GSM8k-kor 류에서 '데이터를 더 많이'가 아니라 '실패 모드 중심'으로 증류 신호를 강화하는 패턴이라 재현 가치가 높음."
    tips: "현재 repo의 MR/CG 생성 결과를 이용해, 오답 유형(계산/조건 누락/단위 등)별로 augmentation을 분리한 뒤 커리큘럼(쉬운→어려운)으로 재증류해 보세요."

  - title: "Beyond Answers: ... Multi-Teacher Knowledge Distillation" 
    year: 2025
    venue: "WSDM 2025"
    link: "https://arxiv.org/abs/2402.04616"
    themes:
      - structured_distillation
      - multi_teacher
    idea: "여러 교사 LLM의 답+추론(전략 포함)을 모아 'TinyLLM'식 지식증류를 수행. 단일 교사 대비 편향을 줄이고 범용성을 높이는 방향."
    relevance: "OpenRouter/Together 등 여러 API/체크포인트를 교사로 쓰는 실전 세팅과 잘 맞음(teacher ensemble)."
    tips: "교사별 스타일이 달라 conflict가 생길 수 있으니, (a) teacher agreement 필터, (b) best-of-N 선택, (c) teacher-id 조건부 학습을 비교해보면 좋음."

  - title: "Knowledge-Augmented Reasoning Distillation for Small Language Models in Knowledge-Intensive Tasks (KARD)"
    year: 2023
    venue: "NeurIPS 2023"
    link: "https://arxiv.org/abs/2305.18395"
    themes:
      - structured_distillation
      - retrieval
      - knowledge_intensive
    idea: "외부 지식(검색/KB)을 근거로 한 reasoning chain을 distill해서, 지식집약 QA에서 소형 모델의 추론과 근거 사용을 함께 강화."
    relevance: "KG/위키데이터 기반 파이프라인과 결합하기 좋은 'retrieval-grounded distillation' 레퍼런스."
    tips: "현재 프로젝트의 KG/문서 검색 결과를 rationale에 항상 포함시키지 말고, (1) retrieval-only, (2) retrieval+reason, (3) reason-only 세 가지로 분리해 어떤 신호가 실제로 도움이 되는지 확인 권장."

  - title: "Process Reward Model with Q-value Rankings"
    year: 2025
    venue: "ICLR 2025 (Poster)"
    link: "https://openreview.net/forum?id=wQEdh2cgEk"
    themes:
      - prm
      - test_time_scaling
    idea: "PRM 학습을 step-wise BCE 대신 Q-value 기반 '랭킹'으로 훈련해, 단계 간 상대적 우열을 더 직접적으로 학습(순서/중요도 반영)."
    relevance: "step-level supervision을 만드는 비용이 큰 상황에서, pairwise/ ranking 신호는 더 견고하게 동작할 여지가 큼."
    tips: "현재 생성된 풀이들에 대해 verifier로 step pairwise 비교를 만들고(승/패), 그걸로 PRM을 랭킹 로스로 학습하는 실험이 구현 난이도 대비 임팩트가 큼."

  - title: "Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning"
    year: 2025
    venue: "NeurIPS 2025 (Poster)"
    link: "https://openreview.net/forum?id=3Sxby0hH1q"
    themes:
      - prm
      - robustness
    idea: "step reward를 합(sum)으로 누적하는 방식이 reward hacking/스푸리어스 단계를 키울 수 있음을 지적하고, min-form credit assignment(PURE)로 더 안정적인 신용할당을 제안."
    relevance: "PRM 기반 rerank/rollout에서 '길고 그럴듯한' 체인이 과대평가되는 문제를 줄이는 데 직접적."
    tips: "테스트타임에서 chain score를 단순 합/평균으로 두지 말고, min/quantile/trimmed aggregation을 비교해보면 재현 포인트를 빠르게 잡을 수 있음."

  - title: "Efficient Process Reward Model Training via Active Learning"
    year: 2025
    venue: "COLM 2025"
    link: "https://openreview.net/forum?id=CJ2FmPmoDE"
    themes:
      - prm
      - data_efficiency
    idea: "PRM 라벨(또는 비교) 획득 비용을 줄이기 위해 불확실/정보가 큰 step만 선별해서 라벨링하는 active learning 기반 PRM 학습(ActPRM)."
    relevance: "대규모 step 라벨을 만들기 어려운 프로젝트에 '라벨 예산' 관점의 실전적 해법."
    tips: "우선은 heuristic uncertainty(모델 엔트로피, 듀얼 모델 disagreement)로 샘플링해도 유사한 효과를 볼 수 있으니, 라벨링 파이프라인부터 쪼개서 도입 추천."

  - title: "Retrieval-Augmented Process Reward Model for Generalizable Mathematical Reasoning"
    year: 2025
    venue: "ACL 2025 (Findings)"
    link: "https://openreview.net/forum?id=zkoeIWbTYy"
    themes:
      - prm
      - retrieval
      - math_reasoning
    idea: "PRM이 OOD에서 무너지는 문제를 완화하기 위해, 유사 문제/단계를 retrieval로 가져와 PRM 판단을 보강(일종의 'retrieval-augmented verifier')."
    relevance: "GSM8k-kor처럼 분포가 바뀌면 step 평가가 흔들리는 환경에서, 검색 기반 보정은 특히 유효할 수 있음."
    tips: "retrieval corpus를 (a) 문제 텍스트, (b) 정답식/중간식, (c) step 텍스트로 나눠 인덱싱하고, 어떤 키가 PRM 일반화에 가장 기여하는지 ablation 권장."

  - title: "Provable Scaling Laws for the Test-Time Compute of Large Language Models"
    year: 2025
    venue: "NeurIPS 2025 (Poster)"
    link: "https://openreview.net/forum?id=GBMzJLhsRj"
    themes:
      - test_time_scaling
      - theory
    idea: "테스트타임 compute를 늘릴 때(샘플링/비교/리랭크) 어떤 집계 규칙이 이득을 보장하는지에 대한 이론적 스케일링 법칙을 제시(리그/토너먼트식 비교 등)."
    relevance: "best-of-N, self-consistency류를 넘어, '어떤 aggregation이 안전한가'를 설계할 때 가이드가 됨."
    tips: "실험에서는 단순 best-of-N 외에, pairwise tournament + PRM/ORM judge 조합을 한 번이라도 넣어두면 이론-실전 연결이 쉬워짐."

  - title: "Optimizing Test-Time Compute via Meta Reinforcement Finetuning"
    year: 2025
    venue: "ICML 2025 (Poster)"
    link: "https://openreview.net/forum?id=TqODUDsU4u"
    themes:
      - test_time_scaling
      - optimization
    idea: "테스트타임 compute 할당/탐색을 메타-RL로 학습해, 언제 더 샘플링/검색/검증을 할지 정책적으로 최적화."
    relevance: "SLM에서 '항상 많이 샘플'은 비싸므로, 문제별로 compute를 적응적으로 쓰는 방향이 중요."
    tips: "먼저는 RL까지 가지 않고도, difficulty predictor(예: entropy/length/PRM score variance)로 adaptive N을 조절하는 베이스라인부터 구축하면 안정적으로 확장 가능."

  - title: "LoRA Soups: Merging LoRAs for Practical Skill Composition Tasks"
    year: 2025
    venue: "COLING 2025 (Industry track)"
    link: "https://arxiv.org/abs/2410.13025"
    themes:
      - lora_merging
      - skill_composition
    idea: "서로 다른 스킬로 학습된 LoRA들을 재학습 없이 합쳐(composition), 타겟 복합 과제를 풀게 하는 실용적 병합 전략(CAT 등)을 제시."
    relevance: "CG/MR/QA/RP 등 태스크별 LoRA를 만든 뒤 '조합'으로 복합 추론을 만들려는 니즈에 직접 부합."
    tips: "repo에서 태스크별로 LoRA를 따로 학습한다면, 데이터 믹싱 대비 LoRA merge가 언제 이득인지(특히 데이터가 부족한 타겟 과제) 체크포인트별로 비교 추천."

  - title: "Merging LoRAs like Playing LEGO: Pushing the Modularity of LoRA to Extremes Through Rank-Wise Clustering"
    year: 2024
    venue: "arXiv"
    link: "https://arxiv.org/abs/2409.16167"
    themes:
      - lora_merging
      - modularity
    idea: "LoRA를 rank 단위의 최소 의미 단위(MSU)로 보고, rank-wise clustering으로 LoRA를 재조립/병합(LoRA-LEGO)해 간섭을 줄이고 성능을 확보."
    relevance: "단순 가중합/merge가 깨질 때(간섭) rank 단위 분해는 새로운 해결책."
    tips: "실전 적용 시에는 먼저 (a) rank 재가중, (b) rank pruning, (c) rank clustering을 순서대로 ablation해서 복잡도를 통제하는 게 좋음."

  - title: "Model merging with SVD to tie the Knots"
    year: 2024
    venue: "arXiv"
    link: "https://arxiv.org/abs/2410.19735"
    themes:
      - model_merging
      - lora_merging
    idea: "LoRA 병합이 어려운 핵심 원인을 '서브스페이스 정렬 부족'으로 보고, SVD 기반 변환으로 여러 LoRA를 정렬된 공간에 매핑한 뒤 기존 merge 기법을 적용(KnOTS)."
    relevance: "LoRA merge가 불안정한 프로젝트에서, 정렬(alignment) 관점의 디버깅/개선 방향을 제공."
    tips: "병합 전후로 layer별/모듈별 cosine similarity나 principal angle을 측정해 '정렬 문제'를 계량화하면, 다른 merge 기법과의 비교가 쉬워짐."

  - title: "Unraveling LoRA Interference: Orthogonal Subspaces for Robust Model Merging"
    year: 2025
    venue: "ACL 2025"
    link: "https://arxiv.org/abs/2505.22934"
    themes:
      - lora_merging
      - robustness
    idea: "LoRA 병합 성능 저하를 데이터-파라미터 상호작용(간섭)으로 설명하고, LoRA 업데이트 서브스페이스를 사전에 직교화/제약해 간섭을 완화(OSRM)."
    relevance: "여러 태스크/도메인 LoRA를 함께 굴릴 때 생기는 '간섭'을 구조적으로 줄이는 접근이라 유지보수성이 좋음."
    tips: "병합 이후 성능만 보지 말고, 단일태스크 성능 보존(회귀)과 merge 하이퍼파라미터 민감도까지 함께 평가하면 논문 주장과 정확히 맞춰 검증 가능."
