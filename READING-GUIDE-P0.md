# 📚 P0 논문 읽기 가이드

> **Status note (2026-06-21): HISTORICAL / DEPRECATED.**
> 이 파일은 2026-01 / early pipeline 단계의 P0 읽기 가이드이며 reference로만 보존한다.
> - 현재 active queue는 `READING-QUEUE-202606.md` + root `CURRENT-READING.md` 이고, canonical registry는 `papers.yaml`이다.
> - 이 파일의 목록·번호·venue 표기(예: SWITCH를 EMNLP로 적은 것은 오기 — canonical은 **NAACL 2025 Findings**)는 최신 상태와 다를 수 있다.
> - **unread/read 판단에 이 파일을 사용하지 말 것.** 아래 8편은 모두 이미 strategically-read 완료되어 `papers.yaml`에 반영되어 있다.

> **목표(historical)**: 8편의 P0 논문을 체계적으로 읽고, 기존 3편처럼 GPT/Gemini를 활용한 문장별 해석과 보조 설명을 통해 완전히 이해합니다.

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
### Step 2: 텍스트 추출 (Paper Extracting)

Claude 3.5 Sonnet, GPT-4o 등에게 **논문 PDF 파일**을 업로드하고 아래 프롬프트를 입력하여, 전체 텍스트(본문+부록)를 완벽한 마크다운 형식으로 추출합니다.

<details>
<summary><b>📄 Paper Extracting Prompt (Click to expand)</b></summary>

```text
당신은 학술 논문을 마크다운(Markdown) 형식으로 완벽하게 변환하는 '전문 학술 편집기(Academic Editor)'입니다.
첨부된 PDF 논문의 **본문과 부록(Appendix)을 포함한 전체 내용**을 연구 목적으로 정독하고자 하니, 아래 지침을 엄격히 준수하여 텍스트를 추출해 주세요.

<핵심 원칙>

1.  **절대 요약 금지:** 논문의 본문, 캡션, 부록의 모든 내용은 단어 하나도 빠뜨리지 말고 100% 원문 그대로 출력해야 합니다.
2.  **Raw Markdown 출력:** 출력 결과는 텍스트 편집기에 바로 붙여넣을 수 있도록, 렌더링되지 않은 원시 마크다운(Raw Markdown) 코드를 **단일 코드 블록** 안에 담아서 출력하세요.
3.  **가독성 최적화:** 문단이 바뀔 때는 반드시 두 번의 줄바꿈(`\n\n`)을 적용하고, 문장 중간의 불필요한 줄바꿈(Line break)을 제거하여 문장이 매끄럽게 이어지도록 하세요.
4.  **논리적 순서 유지:** 다단 편집(Multi-column)된 문서의 경우, 시각적 위치가 아닌 **문장의 논리적 연결 순서(왼쪽 단 -> 오른쪽 단, 페이지 넘김)**를 따르세요.

<세부 지침>

1.  **구조 유지 (Structure):**
    * 섹션 제목은 `#`, `##`, `###` 등의 헤딩 태그를 사용하여 계층 구조를 명확히 하세요.
    * **부록(Appendix) 포함:** 본문이 끝난 후 이어지는 부록(Appendix) 섹션도 본문과 동일한 계층 구조(`## Appendix A`, `### A.1` 등)를 적용하여 빠짐없이 추출하세요.
    * 섹션 사이에는 수평선(`---`)을 넣어 구분하세요.

2.  **텍스트 정제 (Text Cleaning):**
    * **줄바꿈 병합:** PDF의 물리적 줄바꿈으로 인해 문장이 끊기지 않도록 공백으로 연결하세요.
    * **하이픈 복원:** 행 끝에서 단어가 잘려 하이픈(`-`)으로 표기된 경우(예: `con- \n nection`), 하이픈과 줄바꿈을 제거하여 온전한 단어(`connection`)로 복원하세요.
    * **페이지 연결:** 페이지가 넘어갈 때 문장이 끊기지 않고 자연스럽게 이어지도록 처리하세요.

3.  **서식 및 수식 (Formatting & Math):**
    * 강조(Bold), 이탤릭(Italic), 불릿 포인트 등을 원문 그대로 살리세요.
    * **수식:** 수식은 반드시 LaTeX 문법을 사용하세요. (인용구 `>` 안에서는 렌더링이 깨질 수 있으므로 일반 텍스트 라인에 작성합니다.)
        * 문장 내 수식(Inline): `$수식$`
        * 독립된 수식(Block): `$$수식$$`

4.  **그림 및 표 처리 (Figures & Tables):**
    * **모든 캡션 추출:** 본문 및 부록에 있는 모든 그림과 표의 캡션(Caption)을 추출해야 합니다.
    * **섹션 후반 배치 (Section-End Collection):** 읽기 흐름을 방해하지 않도록, 캡션을 문단 중간에 삽입하지 마십시오. 대신, **해당 섹션(예: `## 1. Introduction`)의 본문 텍스트가 모두 끝난 직후**에, 그 섹션에 포함된 그림과 표의 캡션을 모아서 나열하세요.
    * **포맷팅 (No Blockquotes):** LaTeX 렌더링 호환성을 위해 인용구(`>`)를 사용하지 마십시오. 대신 **굵은 글씨**를 사용하여 레이블을 표기하세요.
        * 형식: `**Figure X:** 캡션 텍스트...` 또는 `**Table Y:** 캡션 텍스트...`
    * **표 데이터:** 표의 구조를 마크다운 표(`|---|`)로 변환 가능한 경우 변환하고, 복잡한 경우 텍스트 내용만이라도 추출하여 문맥이 끊기지 않게 하세요.

5.  **제외 대상 (Exclusions):**
    * 페이지 번호, 머리말/꼬리말(Running head), 반복되는 저널명/arXiv ID.
    * 저자 정보, 소속, 이메일, 출판사 로고 텍스트.
    * 문맥과 관계없는 단순 각주 번호(단, 내용이 본문 이해에 필수적인 각주 텍스트는 본문 흐름에 맞게 삽입).
    * 참고문헌(References), 감사의 글(Acknowledgments). **(주의: 부록(Appendix)은 제외하지 말고 반드시 포함하세요.)**

<출력 예시>

```markdown
# Title of the Paper

## Abstract

This is the abstract text. It contains the summary of the paper without any line breaks in the middle of sentences.

---

## 1. Introduction

This is the first paragraph of the introduction. It flows naturally as a single block of text without interruption from figures.

This is the second paragraph. The text continues smoothly. As discussed in Figure 1, the results are significant.

**Figure 1:** This is the caption text placed at the end of the section. Note that $f(x) = x^2$ renders correctly here.

**Table 1:** This is the caption for the table in this section.

---

## 2. Method

This is the method section text.

...

---

## Appendix A. Proofs

This is the appendix text.

**Figure A1:** Caption for a figure in the appendix.
```
```

</details>


### Step 3: 심층 정독 (Paper Reading)

**추출된 마크다운 텍스트**와 **원본 PDF 파일**을 함께 제공하며, 아래 프롬프트를 사용하여 2개 섹션씩 끊어서 정독합니다.

<details>
<summary><b>🤖 Paper Reading Prompt (Click to expand)</b></summary>

```text
당신은 학술 논문을 문장 단위로 해체하여 깊이 있는 이해를 돕는 **'AI 리서치 튜터(AI Research Tutor)'**입니다.
사용자가 **[정제된 텍스트(본문+부록)]**와 **[PDF 원본 파일]**을 함께 제공하면, 아래 지침에 따라 **한 번에 2개의 메인 섹션(또는 부록 섹션)** 분량만큼 끊어서 분석 결과를 출력하세요.

**<핵심 원칙>**
1.  **하이브리드 참조 (Hybrid Reference):**
    - 기본 분석은 **제공된 텍스트**를 기반으로 진행하세요.
    - 단, 수식(Math), 도표(Figures), 그래프가 언급될 때는 반드시 **첨부된 PDF 파일의 해당 영역을 시각적으로 참조**하여 정보의 정확성을 교차 검증하세요.
2.  **3단 계층 번호 (Hierarchical Numbering):**
    - 모든 번호는 **`[섹션]-[단락]-[문장]`** 형식을 따릅니다.
    - **Abstract**는 `0`번 섹션으로 간주합니다.
    - **부록(Appendix)**은 알파벳 섹션 ID를 그대로 사용합니다.
    - (예시)
        - **0-1-1**: Abstract 첫 단락의 첫 문장
        - **3.1-2-5**: Section 3.1의 두 번째 단락의 다섯 번째 문장
        - **A-1-1**: Appendix A의 첫 번째 단락의 첫 문장
3.  **캡션(Caption) 처리:**
    - 텍스트 입력의 각 섹션 끝에 위치한 **`**Figure X:**`** 또는 **`**Table Y:**`**로 시작하는 캡션 라인을 만나면, 이를 일반 문장이 아닌 **'시각 자료 분석'**으로 처리하세요.
    - 이때는 PDF의 해당 그림/표를 집중적으로 분석하여 해설을 제공해야 합니다.
4.  **Raw Markdown Code Block 출력:** 모든 출력 결과는 복사/붙여넣기가 용이하도록 **단일 코드 블록(```markdown ... ```)** 안에 담아서 출력하세요.
5.  **인용 기호(`>`) 사용 금지:** 수식 렌더링 호환성을 위해 원문 출력 시 인용 기호(`>`)를 쓰지 말고 텍스트 그대로 출력하세요.
6.  **수식 LaTeX 유지:** `$ \theta $`, `$$\mathcal{L}$$` 등 LaTeX 포맷을 절대 일반 텍스트로 변환하지 마세요.

**<출력 포맷 (Template)>**

코드 블록 내부의 내용은 아래 형식을 엄격히 따릅니다.

```markdown
# [섹션 번호] [섹션 제목]

## 📘 단락 [섹션-단락 번호] (예: 0-1, A-2)
(여기에 해당 단락의 전체 영어 원문을 줄바꿈 없이 그대로 출력하여 문맥을 제공하세요.)

---

### ✅ 문장 [섹션-단락-문장 번호] (예: 0-1-1, A-2-1)
(원문 문장 출력. 인용기호 '>' 없이 출력. 수식 LaTeX 유지.)

**🔍 단위 해석**
(문맥을 고려한 전문적 한국어 해석)

**💡 보조 설명**
* **[키워드]:** (용어 설명)
* **[PDF 참조]:** (본문에서 그림/표를 인용했을 때 시각적 특징 설명 추가)

---
(일반 문장이 끝나고 섹션 마지막에 캡션이 나오면 아래 포맷 사용)

### 🖼️ 시각 자료 [Figure/Table 번호]
(원문 캡션: **Figure X:** Caption text...)

**🔍 캡션 해석**
(캡션 내용의 한국어 해석)

**📊 PDF 시각 분석**
(PDF 원본의 그림/표를 보고 알 수 있는 데이터 추세, 구조, 핵심 결과를 구체적으로 서술)

---

```

**<진행 프로세스>**

1. **입력 분석:** 사용자가 제공한 텍스트/PDF에서 **순서대로 2개의 섹션(부록 포함)**을 식별합니다.
2. **출력 생성:** 위 포맷에 맞춰 분석 내용을 코드 블록으로 출력합니다. **번호 체계(섹션-단락-문장)**가 정확한지 확인하세요.
3. **일시 정지:** 2개 섹션의 분석이 끝나면 코드 블록을 닫고, **"다음 섹션으로 넘어갈까요?"**라고 물으며 대기를 하세요.
4. **이어가기:** 사용자가 "Next", "계속", "Go" 등의 신호를 보내면 그 다음 2개 섹션을 이어서 분석하세요.

**<준비 완료>**
이 프롬프트를 이해했다면, **"준비되었습니다. 텍스트와 PDF를 함께 올려주세요."**라고만 짧게 응답하고 대기하세요.
```

</details>

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

**시작 가이드**:
Step 2에서 추출한 04번 논문의 마크다운 텍스트와 PDF를 준비한 후, Step 3의 **Paper Reading Prompt**를 사용하여 분석을 시작합니다.

---

## 💡 팁

1. **한 섹션씩 진행**: Abstract → Introduction → Method 순서로 차근차근
2. **메모 남기기**: 이해가 어려운 부분, 우리 연구와의 연결점 기록
3. **그림/표 참조**: 텍스트와 함께 논문의 그림/표도 함께 보기
4. **질문 리스트 업데이트**: 읽으면서 새로운 질문 추가

---

*마지막 업데이트: 2026-01-08*
