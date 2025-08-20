# 사용자 질문
이제 두번째 논문(Distilling Step-by-Step! Outperforming Larger Language Models with Less Training Data and Smaller Model Sizes)에 이어서 읽어볼 다음 논문을 다시 신중하게 정해보고자 합니다.

두번째 논문을 읽는데도 3일 정도 소모되었으므로, 효과적으로 다음 논문을 정해보려고 합니다.
이제는 점진적으로 단계적으로 구현해보다가 실험이 진행될 때 다시 시간 내서 논문을 읽어볼 수 있다고 생각합니다.

두번째 논문에 이어서 연구과제에서 달성하려는 목표를 위해 다음으로 읽어야할 논문은 무엇인지 다시 한번 신중하게 생각해보고 추천해주세요.
각 논문의 abstract와 각 논문 내용까지도 참고하여서 다시 한번 정말 신중하게 추천해주세요.


# 모델: GPT-5
### 다음 읽을 1순위: Phased Instruction Fine-Tuning (ACL 2024, Findings)
- 이유: 지금 파이프라인(7K LLM-CG + 멀티태스크 학습)의 가장 큰 리스크는 JSON/트리플 형식 오류와 수렴 불안정입니다. Phased IFT는 “쉬운→어려운” 커리큘럼으로 형식 준수·안정 수렴을 실질적으로 개선합니다. 구현 난이도도 낮아 즉시 적용 가능합니다.
- 핵심 읽기 포인트
  - §3 Method: IDC/IDS/Uptraining 구조(난도별 분할→순차 업트레이닝)
  - §4.3 Full permutation: 단계 순서가 성능에 미치는 영향(쉬운→어려운이 최적)
  - 난도 정의 대체 규칙: 트리플 수(≤3 vs >3), 관계 타입 다양도(낮음→높음)
- 바로 적용안
  - 데이터 분할: Phase-1=트리플 ≤3(단문·단순 관계), Phase-2=>3(복합 관계·긴 JSON)
  - 스케줄: Phase-1 짧고 안정화 중심(예: 에폭 1), Phase-2에서 본 학습(에폭 1–2), λ(라쇼날 가중) Phase-2에서만 상향
  - 산출물: 커리큘럼 분할 스크립트, 학습 스케줄/하이퍼파라미터 템플릿

### 2순위(학습 중 병행 참고): SWITCH (EMNLP 2024)
- 이유: 긴 JSON 출력에서 스키마 위반/형식 오류를 유발하는 “오류 토큰”만 선택적으로 교사 분포를 주입해 정정하는 방법. 멀티태스크 학습과 궁합이 좋고, 형식 안정성에 직접 기여.
- 핵심 읽기 포인트
  - Algorithm 2: 학생-교사 확률 괴리 토큰 검출→교사介入
  - 임계값/윈도우 길이 튜닝, JSON 키/구조 토큰 우선 적용
- 적용안: Phase-2 또는 파인튜닝 말기에만 SWITCH 켜기(오버헤드 최소화), 스키마 토큰 집합에 한정 적용

### 3순위(후속 품질 보완): InstructGraph (ACL 2024, Findings)
- 이유: 그래프-중심 인스트럭션 + 선호 정렬로 중복/순서 오류·환각을 줄여 CG 품질을 끌어올림. 기본 성능이 오른 뒤 품질 다듬기에 적합.
- 핵심 읽기 포인트
  - §2.3/2.4: 구조화 포맷과 선호도(pair) 설계(부정 샘플: unfactual/conflict/missing)
- 적용안: 교사 점수로 자동 선호 pair 생성→DPO/선호 정렬을 소규모(예: 10–20k 샘플)로 추가

### 4순위(보조 데이터 증강): Contextualization Distillation (Findings of EACL 2024)
- 이유: 트리플→자연어 문맥 생성으로 CG의 background knowledge 섹션을 강화. Distilling Step-by-Step의 데이터 효율성을 더 끌어올릴 수 있음.
- 적용안: 듀얼 태스크(재구성+컨텍추얼라이제이션)로 소규모 증강(예: 1–2k) 후 ablation

### 나중에(옵션)
- Mentor-KD: 교사 신호·데이터가 부족할 때(현재 7K면 보류)
- GraphGPT: 구조 변경 비용 큼(안정화 이후)
- MAGDi/DRAG/Recall-Extraction: 현재 MWP-CG 목표와 거리(필요 시 특정 모듈 전이)

### 실행 제안(최소 부담)
- Day 0.5: Phased IFT 핵심 섹션만 정독→데이터 분할/스케줄 즉시 반영
- 학습 진행 중 병행: SWITCH 알고리즘 파트만 발췌→형식 오류가 눈에 띄면 적용
- 1차 성능 확정 후: InstructGraph 최소 페이퍼-투-코드(선호 pair 생성)로 품질 보정

요약
- 바로 읽을 논문: Phased IFT(1순위) → SWITCH(병행 참고) → InstructGraph(후속 품질) → Contextualization(보조 증강).
- 목적 적합성·즉시성·구현 용이성을 기준으로 선정했으며, 현재 파이프라인에 가장 큰 가치(수렴·형식 안정)를 주는 순서입니다.


# 모델: Claude-4
두 번째 논문 "Distilling Step-by-Step"을 읽으신 후, 다음 단계를 위한 논문 추천을 위해 현재 상황을 먼저 분석해보겠습니다.
Ran tool
Ran tool
이제 HTML 폴더 내 논문들의 초록을 확인하여 현재 상황에 가장 적합한 다음 논문을 추천하겠습니다.
Ran tool
Ran tool
Ran tool
Ran tool
현재 상황을 종합적으로 분석한 후, 다음 단계에서 읽어야 할 논문을 추천하겠습니다.
Ran tool
## 현재 상황 분석

**진행 상황:**
- Self-Instruct: 4단계 부트스트래핑 파이프라인 완료 (✅)
- Distilling Step-by-Step: 멀티태스크 손실 (L_label + λ*L_rationale) 기법 이해 완료 (✅)

**구현 준비 상황:**
- 데이터 전략: 7K 학습셋 LLM-CG 생성 + Self-Instruct 1-2K 보조
- 학습 방법: 멀티태스크 (정답 + CG) 동시 학습
- 평가 지표: MR 정확도, CG 스키마 준수율, triple F1

## 추천 논문: **Phased Instruction Fine-Tuning (3번)**

**이유:**

1. **실험 안정성 확보가 핵심**: 현재 멀티태스크 학습 (정답+CG 동시 생성)을 계획하고 있는데, 이는 복잡도가 높고 학습 불안정성 위험이 있습니다. Phased IFT는 "쉬운→어려운" 2단계 커리큘럼으로 JSON 형식 오류를 줄이고 수렴을 안정화합니다.

2. **즉시 적용 가능한 방법론**: 
   - Phase 1: triple ≤3 (단순 CG)
   - Phase 2: triple >3 (복합 CG)
   이 기준으로 7K 데이터를 분할하여 점진적 학습이 가능합니다.

3. **구현 복잡도 대비 효과 극대화**: GraphGPT나 MAGDi 같은 복잡한 그래프 인코더보다 단순하면서도, 현재 설계한 멀티태스크 학습에 직접 적용 가능합니다.

4. **단기 성과 확보**: 3일 내 읽고 즉시 실험 설계에 반영할 수 있어, 빠른 프로토타입 구현이 가능합니다.

## 대안들과 비교

**DRAG (9번)**: 증거+그래프 기반 증류는 매우 관련성 높지만, RAG 시스템 구축이 선행되어야 하고 복잡도가 높습니다.

**GraphGPT (4번)**: 그래프-LLM 정렬은 중요하지만, 현재 CG→rationale 매핑이 이미 설계되어 있어 추가 복잡성만 가중됩니다.

**MAGDi (6번)**: 멀티에이전트 증류는 흥미롭지만, 단일 교사 모델(Llama-4-Maveric) 기반 현재 설계와 맞지 않습니다.

## 실행 계획
Ran tool
## 최종 추천: **3번 - Phased Instruction Fine-Tuning for Large Language Models**

**핵심 이유:**
1. **현재 상황에 최적화**: Self-Instruct + Distilling Step-by-Step 기반 설계에 안정성을 더하는 완벽한 보완재
2. **즉시 적용 가능**: triple 수(≤3 vs >3) 기준으로 7K 데이터 분할하여 2단계 커리큘럼 구현
3. **학습 안정성 확보**: JSON 형식 오류 감소, 멀티태스크 학습 수렴 안정화
4. **구현 복잡도 적정**: 3일 내 이해하고 실험에 반영 가능

이 논문을 읽으신 후, 바로 프로토타입 구현에 들어가면서 나머지 논문들은 실험 진행 중 필요에 따라 참조하시는 것이 효율적일 것 같습니다.


# 모델: Gemini-2.5
안녕하세요. `Self-Instruct`와 `Distilling Step-by-Step!` 논문을 성공적으로 읽고 연구 계획을 구체화하신 것을 확인했습니다. 이제 구현 단계로 넘어가면서 가장 효율적으로 다음 논문을 선택해야 할 시점입니다.

`weekly-report.txt`와 `README.md`의 현재 계획, 그리고 `html` 폴더의 논문 내용까지 모두 다시 한번 깊이 있게 분석하여, 지금 시점에서 가장 전략적인 다음 논문을 신중하게 추천해 드립니다.

### 최종 결론 요약

1.  **1순위 (즉시 실행 및 병행)**: **`Phased Instruction Fine-Tuning for Large Language Models` (03)**
    *   **핵심**: `Distilling Step-by-Step`의 학습 과정을 **안정화**하고, sLLM의 고질적인 문제인 **JSON 형식 오류를 줄이는** 가장 간단하고 효과적인 방법입니다.
2.  **2순위 (1순위 적용 후 문제 발생 시)**: **`SWITCH` (08)**
    *   **핵심**: `Phased IFT`로도 해결되지 않는 **긴 CG의 형식 오류**를 잡기 위한 강력한 토큰 레벨 교정 기법입니다.
3.  **3순위 (품질 고도화 단계)**: **`InstructGraph` (05)**
    *   **핵심**: 형식과 추론 성능이 안정된 후, CG 내용의 **품질(중복, 순서, 환각)**을 개선하기 위한 선호도 학습 방법입니다.

---

### 상세 추천 근거 및 실행 계획

#### 🎯 **1순위: `Phased Instruction Fine-Tuning for Large Language Models` (ACL 2024 Findings)**

`Distilling Step-by-Step`이 **"무엇을, 어떻게"** 가르칠지에 대한 핵심 프레임워크라면, `Phased IFT`는 그 학습 과정이 **"실패하지 않도록"** 만드는 가장 중요한 안전장치입니다.

*   **왜 지금 이 논문인가?**
    1.  **가장 시급한 문제 해결**: 현재 계획의 가장 큰 기술적 난관은 **sLLM이 복잡하고 긴 JSON 형식의 CG를 안정적으로 생성하도록 만드는 것**입니다. `Phased IFT`는 "쉬운 것부터 어려운 것 순서로" 학습시키는 간단한 커리큘럼을 통해 이 문제를 직접적으로 해결합니다. (`html/03...html` 분석 결과, 이 방법은 모델의 수렴을 돕고 Alpaca 데이터셋에서 Llama 계열 모델의 성능을 크게 향상시켰습니다.)
    2.  **즉시 적용 가능 및 낮은 구현 비용**: 이 논문의 아이디어는 모델 구조나 손실 함수를 변경할 필요가 없습니다. 단순히 7K 학습 데이터를 **난이도(예: CG 내 트리플 수)**에 따라 두 그룹으로 나누고 순서대로 학습시키기만 하면 됩니다. 이는 현재 계획된 `(4순위) 커리큘럼 적용`을 구체화하는 가장 확실한 방법입니다.
    3.  **점진적 발전 철학과 일치**: 먼저 간단한 형식(Phase-1)을 마스터하게 한 뒤, 복잡한 형식(Phase-2)을 학습시키는 방식은 연구를 안정적으로 진행시키려는 현재의 목표와 완벽하게 부합합니다.

*   **읽고 바로 적용할 핵심 (`html/03...html` 기반)**:
    *   **핵심 이론 (Section 3)**: 데이터셋을 난이도에 따라 분할하여 순차적으로 학습(Uptraining)하는 방법론을 이해합니다.
    *   **구현 방식**: 논문에서는 GPT-4로 난이도를 평가했지만, 우리는 이미 계획한 대로 CG의 **"트리플 수 (예: 3개 이하 vs. 3개 초과)"** 라는 단순한 규칙으로 7K 데이터를 Phase-1, Phase-2로 나눕니다.

#### 🔄 **2순위 (보완 카드): `SWITCH: Studying WItH TeaCHer for Knowledge Distillation` (EMNLP 2024)**

*   **왜 후순위인가?**: `Phased IFT`가 충분히 효과적일 수 있으므로, 더 복잡한 `SWITCH`는 일단 시도해 본 뒤 필요할 때 읽는 것이 효율적입니다. `SWITCH`는 학생 모델의 생성 과정에 교사 모델이 개입하여 토큰 확률을 직접 교정하는 방식으로, 구현과 디버깅에 시간이 더 소요됩니다.
*   **언제 읽어야 하는가?**: 1순위 방법을 적용했음에도 불구하고, 특히 길이가 긴 CG(예: 500 토큰 이상)에서 JSON의 괄호가 맞지 않거나 스키마를 위반하는 문제가 계속 발생할 때, 이 논문이 결정적인 해결책이 될 수 있습니다.

#### 🛠️ **3순위 (고도화 카드): `InstructGraph` (ACL 2024 Findings)**

*   **왜 후순위인가?**: 이 논문은 CG의 **내용적 품질**을 다룹니다. 예를 들어, 같은 의미의 트리플이 중복되거나, 비논리적인 순서로 생성되는 문제를 해결합니다. 이는 모델이 일단 유효한 형식의 CG를 꾸준히 생성하는 것이 확인된 *후에* 다룰 문제입니다.
*   **언제 읽어야 하는가?**: sLLM이 형식적으로는 완벽한 CG를 생성하지만, 그 내용이 LLM 교사의 품질에 미치지 못할 때, 선호도 정렬(Preference Alignment)을 통해 생성 품질을 한 단계 더 끌어올리기 위해 읽으면 좋습니다.

---

#### 📋 **점진적 실행 로드맵**

1.  **금주 ~ 차주**:
    *   **구현**: `Distilling Step-by-Step`의 멀티태스크 학습 파이프라인 프로토타입을 구현합니다.
    *   **데이터 생성**: (계획대로) 한국어 GSM8k 학습셋 7K에 대한 CG 생성을 시작합니다.
    *   **논문 읽기**: 데이터 생성이 진행되는 동안 **`Phased Instruction Fine-Tuning` (03) 논문을 정독**하여 커리큘럼 적용 방식을 최종 확정합니다.

2.  **3주차**:
    *   **실험**: 생성된 7K 데이터를 `Phased IFT` 커리큘럼에 따라 Phase-1, Phase-2로 분할하고, **첫 번째 학습 및 평가를 실행**합니다.
    *   **분석**: 결과 분석 후, JSON 형식 오류율이 여전히 높다면 **`SWITCH` (08) 논문**을 읽으며 다음 개선 단계를 준비합니다.

**결론적으로, 지금은 `Distilling Step-by-Step`이라는 엔진에 `Phased IFT`라는 안정화 장치를 더하는 것이 가장 중요합니다.** 이 두 가지를 결합하여 첫 실험을 성공적으로 마치는 것이 연구를 가장 순탄하게 진행하는 길입니다.


# 모델: Grok-4
### 사용자 질문 요약 및 추천 근거
사용자님의 쿼리를 바탕으로, "Distilling Step-by-Step" 논문(멀티태스크 rationale 증류로 데이터·모델 효율성 향상) 후 연구 목표(sLLM의 한국어 MWP CG 생성/추론 재현)에 가장 적합한 다음 논문을 신중히 선정했습니다. `papars.yaml`의 abstract와 `html/` 폴더 논문 내용(예: Phased IFT의 §3 Method, GraphGPT의 §3.2 Alignment Projector 등)을 철저히 분석했습니다. 이전 "Self-Instruct"(데이터 생성)와 "Distilling Step-by-Step"(멀티태스크 증류)의 연장선상에서, 이제 학습 안정성(형식 오류↓, 수렴 향상)을 보강하는 논문을 우선 추천합니다. 이는 점진적 구현(멀티태스크 학습 후 커리큘럼 적용)에 적합하며, 복잡도 낮아 2–3일 내 적용 가능합니다.

#### 🎯 **1순위 추천: Phased Instruction Fine-Tuning for Large Language Models (ACL 2024, Findings)**
##### 선택 이유 (abstract와 내용 기반 분석)
1. **현재 과제 연계성**: "Distilling Step-by-Step"의 멀티태스크 학습(CG=rationale 매핑)이 복잡한 JSON 형식에서 불안정할 수 있음. 이 논문은 "쉬운→어려운" **2단계 커리큘럼**(abstract: progressive alignment hypothesis)으로 형식 오류↓·수렴 안정성을 제공. 한국어 MWP 목표에서 CG(JSON triples) 난도를 트리플 수로 분할하면(§3 Method), 7K 데이터 학습 시 안정적 재현 가능. 기존 실험(+21.6% 향상)을 바탕으로 멀티태스크 불안정을 보완.
2. **시간·구현 효율**: 1–2일 소요. §4.3(순서 실험) 결과처럼 데이터 분할만으로 적용 가능. "Distilling Step-by-Step" 후 즉시 병합: Phase-1(단순 CG)에서 멀티태스크 기본 학습 → Phase-2(복합 CG)로 확장.
3. **검증 효과**: Alpaca 데이터 실험에서 One-off IFT 대비 안정적(§4.1). 우리 7K CG + Self-Instruct 합성(1–2k) 데이터에 적용 시, sLLM(8B)에서 LLM 수준 재현 기대. unlabeled 설정에서도 유효(§4.2 ablation).

##### 읽기 & 적용 가이드 (html 전문 기반)
- **필독 섹션**: §3 (난도 평가·분할·업트레이닝), §4.3 (순서 비교, 1-2-3 최적).
- **즉시 실험 아이디어**:
  - Phase-1: 트리플 수 ≤3 (쉬운 CG 데이터)로 멀티태스크 기본 학습.
  - Phase-2: >3 (어려운 CG)로 확장, λ 튜닝 병행.
  - 적용: 7K LLM-CG 데이터 난도 분할 후 순차 학습; 형식 오류율 20%↓ 기대.

#### 🔄 **2순위: GraphGPT: Graph Instruction Tuning for Large Language Models (SIGIR 2024)**
##### 선택 이유
- **그래프 중심 보완**: "Distilling Step-by-Step" 후 CG 구조화 강화. abstract에서 text↔graph grounding + projector로 그래프 생성·추론↑. MWP CG(JSON triples)를 graph로 매핑해 경량 업데이트(§3.2).
- **효율성**: LoRA projector로 head 0.5%만 학습 → 비용↓. 7K 데이터 학습 시 그래프 IT로 triple 품질 향상.
- **검증**: Zero-shot 그래프 학습에서 우수(§4), 우리 unlabeled CG 증류에 적합.

##### 읽기 & 적용 가이드
- **필독 섹션**: §3.2 (Alignment Projector), §4 (zero-shot 평가).
- **즉시 실험 아이디어**: YAML-triple을 graph embedding으로 변환, LoRA로 head 업데이트; MWP triples 생성 정확도↑.

#### 📋 **즉시 실행 로드맵**
- **Week 1**: Phased IFT 읽기 + "Distilling Step-by-Step" 멀티태스크에 Phase 적용 프로토타입.
- **Week 2**: 7K CG 데이터 분할·학습 실행, 형식 오류 분석.

#### 🚫 **다른 논문 후순위 이유**
- **InstructGraph/MAGDi**: 그래프 IT/KD지만, Phased IFT로 기반 안정 후 추가.
- **Mentor-KD/SWITCH**: KD 세부 기법, 증류 안정화 후 검토.
- **DRAG/Contextualization**: RAG/KGC, 현재 MWP CG 중심과 거리.

**최종 근거**: "Distilling Step-by-Step" 후 학습 안정(Phased IFT)이 급선무. html/03...html 내용(§3)에서 난도 기반 분할이 CG 형식 오류에 최적. 점진 구현에 맞춤.

