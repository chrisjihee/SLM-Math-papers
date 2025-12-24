### 목표 맥락
- Canonical shortlist + plan: [MUST-READ-PLAN.md](MUST-READ-PLAN.md)
- **목표**: 10B 이하 sLLM이 한국어 MWP에서 LLM 수준의 개념 그래프(JSON triples) 생성 및 추론 성능을 재현
- **핵심 과제**: (1) 그래프 중심 지식/근거의 구조화, (2) LLM→sLLM 증류(형식 일치·추론 보존), (3) 커리큘럼/지시문 튜닝으로 안정 학습

### 전체 전략
-- **3축 프레임**으로 읽습니다:  
  - **A. IFT·커리큘럼(curriculum)·합성 데이터(synthetic)**: 안정적으로 “형식 준수 + 도메인 적합”을 만드는 기반  
  - **B. 그래프 중심 정렬/증류**: 개념·관계·근거를 구조화해서 직접 감독  
  - **C. 효율적 KD**: LLM 신호를 sLLM에 손실 없이 이식(멘토/선택적 교사介入/증거-그래프 동시 증류)

---

### 0단계(오리엔테이션, 2시간)
- 모든 논문 초록/그림/방법 개요만 훑고, 당장 쓸 “핵심 산출물 체크리스트”를 정합니다:
  - 산출물: 손실식(특히 그래프·형식·선호도), 데이터 생성 파이프라인(자연어↔triple), curriculum 규칙, 평가 지표(스키마 준수율, triple F1, 근거 일치, 최종 MR 정확도 Δ)

---

### 1단계(기반 IFT·커리큘럼) — Day 1–2
1) [Self-Instruct: Aligning Language Models with Self-Generated Instructions](https://arxiv.org/abs/2212.10560) — ACL 2023  
   - **왜**: 소형 LM이 한국어 MWP의 CG 생성·추론을 대형 수준으로 재현하려면 도메인 특화 instruction 데이터가 필요하지만, 수작업 annotation은 비용이 크고 창의성이 제한적이다. Self-Instruct는 175 seed에서 시작해 LM이 스스로 52k instruction을 생성하는 4단계 pipeline(지시문 생성→분류 판별→instance 생성→filtering)을 제시하며, 16k 이후 성능 plateau 발견으로 우리 도메인에서는 소규모 고품질 데이터로도 충분한 성능 달성 가능성을 보여준다. 특히 교사 LLM(Llama-4-Maveric)의 데이터 생성 비용을 절감하면서도 CG 생성 과제에 특화된 instruction 다양성을 확보할 수 있다.  
   - **초점**: (1) 도메인 특화 pipeline: MWP-CG 생성 패턴 30-50개 seed 설계 → template 확장(문체/슬롯/난이도) → CG 생성/추론/검증 태스크 분류 → output-first로 label bias 완화. (2) 품질 filtering 강화: ROUGE-L < 0.7, JSON format 검증, 한국어 개념/관계 표기 표준화, 중복·충돌 제거. (3) 데이터 규모 최적화: 16k plateau 근거로 1k→2k→3k 점진적 확장하며 성능 saturation 지점 탐지. (4) 품질 검증: 생성된 instruction의 CG triple 정확성을 교사 LLM으로 재검증하여 Self-Instruct + Distilling Step-by-Step 연계 파이프라인 구축.  
2) [Distilling Step-by-Step! Outperforming Larger LMs…](https://arxiv.org/abs/2305.02301) — ACL 2023 (Findings)  
   - **왜**: 표준 finetuning과 distillation은 LLM과 비교 가능한 성능을 위해 대량의 학습 데이터가 필요한 반면, LLM이 생성한 rationale(추론 과정)을 추가 감독으로 활용한 멀티태스크 학습은 데이터 사용량과 모델 크기를 동시에 줄이면서 더 나은 성능을 달성한다. 770M T5가 540B PaLM Few-shot CoT를 초과하는 결과는 우리 목표인 'sLLM(≤10B)로 LLM 수준 재현'에 직접 부합한다. 한국어 MWP에서 CG(JSON triples) 생성 과정 자체가 수학적 추론의 구조화된 중간 단계이므로 rationale 역할을 하며, 교사 LLM(Llama-4-Maveric)이 생성한 7K 학습셋에 "정답 + CG" 동시 감독을 적용하여 추론 내재화가 가능하다.  
   - **초점**: (1) 멀티태스크 손실 설계: L = L_label + λ L_rationale 구조에서 λ∈{0.3,0.5,0.7} 스윕으로 CG 품질과 정답 정확도 균형점 탐지, [label]/[rationale] 프리픽스로 작업 분리하여 동일 모델에서 두 태스크 수행. (2) 데이터 구성 전략: 교사 LLM 생성 7K CG를 주력으로, Self-Instruct 합성 1-2k로 경계 사례·다양성 보강, 입력=한국어 MWP, 출력1=최종 정답, 출력2=CG facts+disambiguation JSON. (3) 커리큘럼 연계: Phased IFT와 결합하여 Phase-1(단순 CG, triple≤3)→Phase-2(복합 CG, >3) 순차 학습으로 rationale 품질 단계적 향상. (4) 평가 체계: MR 정확도, 스키마 준수율, triple F1, 형식 오류율, 추론 일관성, 데이터/모델 효율성 종합 분석. (5) 어블레이션 실험: no-rationale vs single-task vs multi-task, 교사 LLM별(GPT-4, Llama-4-Maveric) rationale 품질 비교, 프리픽스 유무, CG 길이 제한 효과.  
3) [Phased Instruction Fine-Tuning for LLMs](https://arxiv.org/abs/2406.04371) — ACL 2024 (Findings)  
   - **왜**: 기존 One-off IFT는 다양한 난이도의 instruction을 동시에 학습시켜 복잡성 차이를 간과하므로, 모델의 instruction 수행 능력 향상이 비효율적이다. Progressive Alignment Hypothesis에 기반한 Phased IFT는 인간 학습과 유사하게 쉬운 것부터 어려운 것으로 점진적 정렬이 더 효과적임을 실증한다. GPT-4 난이도 평가와 3단계(쉬움→중간→어려움) 순차 uptraining으로 Llama2/3, Mistral 등 다양한 모델에서 일관된 성능 향상을 보이며, 6가지 permutation 실험을 통해 '1→2→3' 순서가 최적임을 증명했다. 한국어 MWP CG 생성에서 JSON 형식 준수와 안정적 수렴을 달성하는 핵심 방법론으로, Distilling Step-by-Step과 결합 시 rationale 품질이 단계적으로 향상된다.  
   - **초점**: (1) 다차원적 난이도 평가 체계: 단순한 triple 수가 아닌 ① 추론 깊이(1-step 직접 연산 → 4+step 복합 추론), ② 개념 복잡성(기본 사칙연산 → 다변수 연립/추상적 관계), ③ 혼동 요소 민감성(단순 정보 추출 → 복잡한 distractor 패턴)을 종합 평가하여 MWP의 실제 인지적 부하 반영. (2) GPT-4 기반 종합 평가: "이 문제를 풀기 위해 필요한 추론 단계, 수학적 개념 복잡도, 혼동 가능성을 각각 1-5점으로 평가"하는 다차원 프롬프트 설계, 가중 평균(α*추론깊이 + β*개념복잡성 + γ*혼동민감성)으로 최종 난이도 산출. (3) 데이터 분할 최적화: 1.5/3.5 임계값으로 3단계 분할, 각 stage 내 난이도 분산 최소화 및 stage 간 명확한 구분성 확보. (4) 학습 순서 검증: 반드시 쉬운→어려운 순서 준수, permutation 실험으로 최적 순서 확인, 각 stage별 동일한 hyperparameter 사용. (5) 성능 모니터링 고도화: stage별 CG 스키마 준수율, 형식 오류율, triple F1뿐만 아니라 추론 일관성, 개념 이해도, 혼동 저항성까지 추적. (6) 검증 메커니즘: 인간 전문가 샘플 검증으로 자동 평가 체계의 타당성 확보, ablation study로 각 난이도 차원의 기여도 분석.

---

### 2단계(그래프 중심 정렬/증류) — Day 3–4
4) [GraphGPT: Graph Instruction Tuning for LLMs](https://arxiv.org/abs/2310.13023) — SIGIR 2024  
   - **왜**: 텍스트↔그래프 정렬, projector/어댑터로 경량 업데이트. CG 생성 직접 강화  
   - **초점**: §3.2 Alignment Projector, LoRA로 head 일부만 업데이트  
5) [InstructGraph](https://aclanthology.org/2024.findings-acl.801/) — ACL 2024 (Findings)  
   - **왜**: 그래프 중심 IT + preference alignment. triple 순서·중복 선호 감독  
   - **초점**: §4 Alignment Loss, 선호도 pair 자동 생성(교사 스코어로 대체 가능)  
6) [MAGDi](https://arxiv.org/abs/2402.01620) — ICLR 2025 (Spotlight)  
   - **왜**: 다중 에이전트 “논증 그래프”를 구조화 증류 → 수학/상식 Reasoning↑  
   - **초점**: Fig.2 파이프라인(토론 로그→그래프), 노드/엣지 라벨을 CG 스키마로 매핑

---

### 3단계(효율적 KD로 형식·추론 보존) — Day 5
7) [Mentor-KD](https://aclanthology.org/2024.emnlp-main.977/) — EMNLP 2024  
   - **왜**: 70B→13B 멘토→8B 학생 2단계 KD가 데이터 적을 때 강력  
   - **초점**: §4 Mentor Generation, 중간 모델로 CG·정답 풀이 동시 교정 후 압축  
8) [SWITCH](https://arxiv.org/abs/2410.19503) — EMNLP 2024  
   - **왜**: **오류 토큰만 선택적 교사介入** → JSON 포맷 위반·긴 출력의 형식 오류 대폭 감소  
   - **초점**: Algorithm 2, 스키마 위반 지점 탐지→teacher prob 주입

---

### 4단계(증거·지식그래프 동시 증류) — Day 6
9) [DRAG](https://aclanthology.org/2025.acl-long.358/) — ACL 2025  
   - **왜**: RAG의 증거 순위 + 지식 그래프를 KL/대조 손실로 동시 증류 → 환각↓ 사실 일관성↑  
   - **초점**: §3 Method, Table 3 Ablation. CG triple과 supporting sentence를 함께 저장/감독

---

### 5단계(인접 KGC·리콜 향상 아이디어 전이) — Day 7
10) [Contextualization Distillation… for KGC](https://aclanthology.org/2024.findings-eacl.32/) — Findings of EACL 2024  
   - **왜**: triple↔자연어 문맥 듀얼 태스크로 구조·언어 양면 감독  
   - **초점**: Algorithm 1 문맥 생성·필터 규칙 → BG/설명 문장 생성에 전이  
11) [Improving Recall… Relational Triple Extraction](https://aclanthology.org/2024.lrec-main.778/) — LREC-COLING 2024  
   - **왜**: 평가-교사와 학생 협업/재랭크로 triple 리콜↑. 추론 전 단계에서 후보 재정렬  
   - **초점**: inference-time 협업, 점수 임계값·top-k 튜닝

---

### 논문별 읽기 포인트(공통 체크리스트)
- **문제-데이터**: MWP→triple 스키마 매핑 규칙, 중복·동의어 처리  
- **손실 설계**: 형식 준수(스키마·토큰 레벨), 구조 일치(트리플/그래프), 선호도, 근거 정렬(KL/contrastive)  
- **생성 파이프라인**: teacher 생성→필터→멘토 교정→학생 학습, 커리큘럼 경계  
- **추론 결합**: CG를 넣었을 때 MR 정확도 Δ, ablation 필수  
- **효율성**: LoRA/프로젝터/선택적 KD로 비용 제어

---

### 1주(7일) 실행형 읽기·적용 계획
- **Day 1**: Self-Instruct, Distilling Step-by-Step  
  - 산출물: CG 합성·필터 스크립트 초안, 다중-태스크 손실 틀  
- **Day 2**: Phased IFT  
  - 산출물: Phase-1/2 데이터 분할(트리플 수 기준), 학습 스케줄  
- **Day 3**: GraphGPT  
  - 산출물: projector/LoRA 설계안, 텍스트↔트리플 임베딩 정렬 방식  
- **Day 4**: InstructGraph, MAGDi  
  - 산출물: 그래프 정렬/선호도 손실, 논증 그래프→CG 스키마 매핑 규칙  
- **Day 5**: Mentor-KD, SWITCH  
  - 산출물: 멘토 생성 파이프라인, 스키마 위반 토큰 탐지+교사介入 로직  
- **Day 6**: DRAG  
  - 산출물: triple+근거 저장 포맷, 대조 손실 추가  
- **Day 7**: KGC·리콜  
  - 산출물: triple↔문맥 듀얼 태스크, 평가-교사 재랭크 실험안

---

### 즉시 적용 팁
- **스키마-우선**: 형식 위반 토큰에만 교사介入(SWITCH) → 학습 안정성 극대화  
- **커리큘럼**: “triple 수”·“관계 타입 다양도”로 난도 정의 → 두 단계 IFT  
- **구조 증류**: triple과 supporting sentence를 나란히 저장 → KL+대조 손실 동시 적용(DRAG)  
- **선호도**: 중복 제거·관계 라벨 정확도에 대한 선호 pair를 교사 점수로 자동 생성(InstructGraph)  
- **경량 업데이트**: projector/LoRA로 헤드 일부만 학습(GraphGPT) → 비용 절감

---

- 요약
  - 읽기 순서: 기반 IFT(1–3) → 그래프 중심(4–6) → 효율 KD(7–8) → 증거·그래프 동시 증류(9) → KGC 전이(10–11).
  - 각 단계는 sLLM의 CG(JSON) 품질을 안정화(형식), 구조화(그래프/선호), 보존(KD) 순으로 누적 개선.
  - 7일 로드맵과 논문별 “왜/초점”을 제공해 곧바로 파이프라인 설계와 실험으로 연결 가능.
