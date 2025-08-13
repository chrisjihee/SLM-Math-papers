### 목표 맥락
- **목표**: 10B 이하 sLLM이 한국어 MWP에서 LLM 수준의 개념 그래프(JSON triples) 생성 및 추론 성능을 재현
- **핵심 과제**: (1) 그래프 중심 지식/근거의 구조화, (2) LLM→sLLM 증류(형식 일치·추론 보존), (3) 커리큘럼/지시문 튜닝으로 안정 학습

### 전체 전략
- **3축 프레임**으로 읽습니다:  
  - **A. IFT·커리큘럼·합성 데이터**: 안정적으로 “형식 준수 + 도메인 적합”을 만드는 기반  
  - **B. 그래프 중심 정렬/증류**: 개념·관계·근거를 구조화해서 직접 감독  
  - **C. 효율적 KD**: LLM 신호를 sLLM에 손실 없이 이식(멘토/선택적 교사介入/증거-그래프 동시 증류)

---

### 0단계(오리엔테이션, 2시간)
- 모든 논문 초록/그림/방법 개요만 훑고, 당장 쓸 “핵심 산출물 체크리스트”를 정합니다:
  - 산출물: 손실식(특히 그래프·형식·선호도), 데이터 생성 파이프라인(자연어↔트리플), 커리큘럼 규칙, 평가 지표(스키마 준수율, triple F1, 근거 일치, 최종 MR 정확도 Δ)

---

### 1단계(기반 IFT·커리큘럼) — Day 1–2
1) [Self-Instruct: Aligning Language Models with Self-Generated Instructions](https://arxiv.org/abs/2212.10560) — ACL 2023  
   - **왜 먼저**: 합성 지시문 파이프라인의 표준. CG JSON 스키마 기반 필터링 설계에 직결  
   - **초점**: Appx B 필터링 규칙 → relation_snake_case·중복 제거·스키마 검증으로 치환  
2) [Distilling Step-by-Step! Outperforming Larger LMs…](https://arxiv.org/abs/2305.02301) — NeurIPS 2023  
   - **왜**: CoT/구조화 근거를 다중-태스크로 증류하는 전범. CG의 facts/disambiguation 병렬 감독 설계에 적합  
   - **초점**: §5.3 Rationale Ablation, 다중-태스크 손실 설계  
3) [Phased Instruction Fine-Tuning for LLMs](https://arxiv.org/abs/2406.04371) — ACL 2024 (Findings)  
   - **왜**: 쉬운→어려운 **두 단계 커리큘럼**으로 JSON 형식 오류↓ 수렴 안정  
   - **초점**: 난도 기준을 “triple 수(≤3 vs >3)”로 단순화해 2-phase 적용

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
