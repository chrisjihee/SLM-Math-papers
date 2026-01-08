# 📚 P0 논문 읽기 가이드

> **목표**: 8편의 P0 논문을 체계적으로 읽고, 기존 3편처럼 GPT/Gemini를 활용한 문장별 해석과 보조 설명을 통해 완전히 이해합니다.

---

## 📋 P0 논문 목록 (우선순위순)

| # | 논문 제목 | 학회 | PDF 링크 |
|---|----------|------|----------|
| 04 | Scaling LLM Test-Time Compute Optimally... | ICLR 2025 Oral | [PDF](https://openreview.net/pdf?id=4FWAwZtd2n) |
| 05 | Rewarding Progress: Scaling Automated Process Verifiers... | ICLR 2025 Spotlight | [PDF](https://openreview.net/pdf?id=A6Y7AqlzLW) |
| 06 | Process Reward Models That Think (ThinkPRM) | arXiv 2025 | [PDF](https://arxiv.org/pdf/2504.16828) |
| 07 | Let's Verify Step by Step | ICLR 2024 | [PDF](https://arxiv.org/pdf/2305.20050) |
| 08 | UniCoTT: A Unified Framework for Structural CoT Distillation | ICLR 2025 | [PDF](https://openreview.net/pdf?id=3baOKeI2EU) |
| 09 | MAGDi: Structured Distillation of Multi-Agent Interaction Graphs | ICLR 2025 Spotlight | [PDF](https://arxiv.org/pdf/2402.01620) |
| 10 | Mentor-KD: Making Small Language Models Better Multi-step Reasoners | EMNLP 2024 | [PDF](https://arxiv.org/pdf/2410.09037) |
| 11 | SWITCH: Studying WItH TeaCHer for Knowledge Distillation | EMNLP 2024 | [PDF](https://arxiv.org/pdf/2410.19503) |

---

## 🛠️ 작업 절차

### Step 1: PDF 다운로드 및 텍스트 추출

1. **PDF 다운로드**: 위 표의 PDF 링크에서 각 논문 다운로드
2. **텍스트 추출 방법**:
   - **방법 A**: Adobe Acrobat / PDF 뷰어에서 직접 복사
   - **방법 B**: [pdf.ai](https://pdf.ai/), [ChatPDF](https://chatpdf.com/) 등 온라인 도구 활용
   - **방법 C**: Python `PyPDF2` 또는 `pdfplumber` 사용

### Step 2: 단락별 텍스트화

각 논문에서 다음 섹션의 텍스트를 단락별로 추출합니다:

1. **Abstract** (전체)
2. **1. Introduction** (전체)
3. **2. Related Work** (핵심 부분만)
4. **3. Method / Approach** (전체 - 가장 중요)
5. **4. Experiments** (핵심 결과 부분)
6. **5. Conclusion** (전체)

### Step 3: GPT/Gemini 프롬프트 작성

아래 프롬프트 템플릿을 사용하여 각 단락을 입력합니다.

---

## 📝 프롬프트 템플릿

### 템플릿 A: 기본 해석 프롬프트 (권장)

```markdown
아래는 논문 "[논문 제목]"의 [섹션명] 부분입니다.

다음 형식으로 해석해 주세요:

1. **원문 단락 제시**: 단락 본문을 그대로 보여주고
2. **문장별 해석**: 각 문장마다:
   - ✅ 원문 문장
   - 📖 **단위 해석**: 한국어로 정확히 번역
   - 💡 **보조 설명**: 전문 용어 해설, 배경 지식, 맥락 설명
3. **단락 요약**: 해당 단락의 핵심 메시지 2-3줄 요약

---

[여기에 논문 텍스트 붙여넣기]
```

### 템플릿 B: 심층 분석 프롬프트

```markdown
아래는 논문 "[논문 제목]"의 [섹션명] 부분입니다.

다음 형식으로 **심층 분석**해 주세요:

## 📘 단락 본문 텍스트
[원문을 그대로 출력]

---

## 📝 문장별 해석

### ✅ 문장 1
[원문 문장]

**단위 해석**
[한국어 번역]

**보조 설명**
- [전문 용어 해설]
- [관련 개념 설명]
- [연구 맥락에서의 의미]

---

(모든 문장에 대해 반복)

---

## 🎯 핵심 포인트
1. [이 단락에서 가장 중요한 주장/발견]
2. [우리 연구(한국어 MWP CG 생성)와의 연관성]
3. [실제 구현 시 참고할 점]

---

[여기에 논문 텍스트 붙여넣기]
```

### 템플릿 C: 연구 적용 관점 프롬프트

```markdown
아래는 논문 "[논문 제목]"의 [섹션명] 부분입니다.

**배경**: 저는 한국어 수학 문장제(MWP)에서 Concept Graph(CG)를 생성하고, 이를 활용해 소형 언어모델(sLLM, ≤10B)의 수학 추론 성능을 향상시키는 연구를 진행 중입니다.

다음을 분석해 주세요:

1. **문장별 해석** (기존 형식과 동일)
2. **핵심 기법 추출**: 이 논문에서 제안하는 핵심 방법론
3. **우리 연구 적용**: 한국어 MWP + CG 생성 문제에 어떻게 적용할 수 있는지
4. **구현 아이디어**: 실제 코드로 구현할 때 고려할 점

---

[여기에 논문 텍스트 붙여넣기]
```

---

## 📑 논문별 핵심 질문 리스트

각 논문을 읽으면서 아래 질문에 답을 정리합니다:

### 04. Scaling LLM Test-Time Compute
- [ ] "compute-optimal" 전략이란 정확히 무엇인가?
- [ ] 문제 난이도에 따라 테스트타임 계산을 어떻게 할당하는가?
- [ ] PRM vs ORM 비교에서 어떤 통찰이 있는가?
- [ ] 14× 작은 모델이 큰 모델을 능가하는 조건은?

### 05. Rewarding Progress (PAV)
- [ ] Process Advantage Verifier의 정의와 학습 방법은?
- [ ] "progress"를 Q-value 대신 advantage로 측정하는 이유는?
- [ ] Prover policy의 선택이 왜 중요한가?
- [ ] RL 학습에서 6× sample efficiency 향상의 원인은?

### 06. ThinkPRM
- [ ] Generative PRM vs Discriminative PRM의 차이점은?
- [ ] Verification CoT를 어떻게 생성하는가?
- [ ] 1% 라벨만으로 효과적인 이유는?
- [ ] ProcessBench, MATH-500에서의 성능 비교 결과는?

### 07. Let's Verify Step by Step
- [ ] Process supervision vs Outcome supervision의 핵심 차이는?
- [ ] PRM800K 데이터셋의 구성과 라벨링 방법은?
- [ ] Active learning이 왜 효과적인가?
- [ ] 78% MATH 성능 달성의 핵심 요소는?

### 08. UniCoTT
- [ ] Chain/Tree/Graph CoT를 어떻게 통합하는가?
- [ ] 구조 보존 증류(structural distillation)의 핵심 메커니즘은?
- [ ] SLM에서의 성능 향상 폭은?

### 09. MAGDi
- [ ] Multi-agent 토론을 그래프로 어떻게 변환하는가?
- [ ] 3가지 loss function의 역할은?
- [ ] Graph encoder의 구조와 학습 방법은?

### 10. Mentor-KD
- [ ] 2단계 KD (Teacher→Mentor→Student)의 이점은?
- [ ] Soft label 제공의 효과는?
- [ ] 데이터 품질 문제를 어떻게 해결하는가?

### 11. SWITCH
- [ ] 선택적 교사 개입의 기준은 무엇인가?
- [ ] 긴 시퀀스에서의 오류 누적 문제를 어떻게 해결하는가?
- [ ] Schema 위반 감소 효과는?

---

## 📂 출력 파일 구조

각 논문을 읽은 후 `md/` 폴더에 다음 형식으로 저장합니다:

```
LM-based-KG-papers/
└── md/
    ├── 01. Self-Instruct... .md                    ✅ 완료
    ├── 02. Distilling Step-by-Step... .md          ✅ 완료
    ├── 03. Phased Instruction Fine-Tuning... .md   ✅ 완료
    ├── 04. Scaling LLM Test-Time Compute... .md    ⏳ P0
    ├── 05. Rewarding Progress PAV... .md           ⏳ P0
    ├── 06. ThinkPRM... .md                         ⏳ P0
    ├── 07. Let's Verify Step by Step... .md        ⏳ P0
    ├── 08. UniCoTT... .md                          ⏳ P0
    ├── 09. MAGDi... .md                            ⏳ P0
    ├── 10. Mentor-KD... .md                        ⏳ P0
    └── 11. SWITCH... .md                           ⏳ P0
```

---

## 🚀 바로 시작하기: 첫 번째 논문

### 04. Scaling LLM Test-Time Compute Optimally...

**PDF 링크**: https://openreview.net/pdf?id=4FWAwZtd2n

**주요 정보**:
- 저자: Charlie Victor Snell, Jaehoon Lee, Kelvin Xu, Aviral Kumar (Google DeepMind)
- 학회: ICLR 2025 Oral (최우수 논문급)
- 키워드: test-time compute, LLMs, scaling, language models

**Abstract** (OpenReview에서 확인):
> Enabling LLMs to improve their outputs by using more test-time compute is a critical step towards building self-improving agents that can operate on open-ended natural language. In this paper, we scale up inference-time computation in LLMs, with a focus on answering: if an LLM is allowed to use a fixed but non-trivial amount of inference-time compute, how much can it improve its performance on a challenging prompt? ...

**시작 프롬프트**:
```
아래는 논문 "Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning"의 Abstract 부분입니다.

다음 형식으로 해석해 주세요:
1. 원문 단락 제시
2. 문장별 해석 (원문, 단위 해석, 보조 설명)
3. 단락 요약

---

Enabling LLMs to improve their outputs by using more test-time compute is a critical step towards building self-improving agents that can operate on open-ended natural language. In this paper, we scale up inference-time computation in LLMs, with a focus on answering: if an LLM is allowed to use a fixed but non-trivial amount of inference-time compute, how much can it improve its performance on a challenging prompt? Answering this question has implications not only on performance, but also on the future of LLM pretraining and how to tradeoff inference-time and pre-training compute. Little research has attempted to understand the scaling behaviors of test-time inference methods, with current work largely focusing on proposing new techniques for using inference-time compute and evaluating their effectiveness. Here, we analyze the scaling behaviors of two primary mechanisms to scale test-time compute: (1) searching against dense, process-based verifier reward models; and (2) adaptively updating the model's response distribution based on the prompt. We find that in both cases, the effectiveness of different approaches to scaling test-time compute is strongly problem-dependent. This observation motivates applying a "compute-optimal" scaling strategy, which acts to most effectively allocate test-time compute adaptively per prompt. Using this compute-optimal strategy, we can improve the efficiency of test-time compute scaling for math reasoning problems by more than 4x compared to a best-of-N baseline. Additionally, in a FLOPs-matched evaluation, we find that on problems where a smaller base model attains somewhat non-trivial success rates, test-time compute can be used to outperform a 14x larger model.
```

---

## 💡 팁

1. **한 섹션씩 진행**: Abstract → Introduction → Method 순서로 차근차근
2. **메모 남기기**: 이해가 어려운 부분, 우리 연구와의 연결점 기록
3. **그림/표 참조**: 텍스트와 함께 논문의 그림/표도 함께 보기
4. **질문 리스트 업데이트**: 읽으면서 새로운 질문 추가

---

*마지막 업데이트: 2026-01-08*
