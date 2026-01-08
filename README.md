# LM-based-KG 논문 자료 디렉토리

**Last updated:** 2026-01-08

## 📁 디렉토리 구조

```
LM-based-KG-papers/
├── MUST-READ-PLAN.md      # 정본 must-read shortlist + 4주 실행 계획
├── UNIFIED-PAPER-LIST.md  # 테마별 전체 후보 풀 (55편)
├── README.md              # 이 파일 (디렉토리 가이드 + 완료된 논문 리뷰)
├── papars.yaml            # 구조화된 논문 데이터 (읽은 논문 상세 + 읽을 논문 목록)
└── md/                    # 개별 논문 심층 리뷰 노트 (Markdown)
```

## 🎯 연구 목표

**목표**: 10B 이하 sLLM이 한국어 MWP에서 LLM 수준의 개념 그래프(JSON triples) 생성 및 추론 성능을 재현

**연구 3축 (PLAN.md)**:
- **Axis 1**: CoT vs CG — 구조화된 Rationale의 데이터 효율성
- **Axis 2**: Test-time Inference Scaling — SLM에서의 비용 효율적 추론
- **Axis 3**: Model Merging + DPO — 서로 다른 추론 스타일 병합

## 📚 문서 가이드

### 1. [MUST-READ-PLAN.md](MUST-READ-PLAN.md) — 정본 (가장 먼저 참조)
- **P0/P1 우선순위** shortlist (14편)
- **4주 실행 계획** (읽기 → 구현 → 측정)
- PLAN.md 3축과의 매핑

### 2. [UNIFIED-PAPER-LIST.md](UNIFIED-PAPER-LIST.md) — 테마별 전체 후보
- **55편** 논문을 4개 테마로 분류
- 연구 방향과 거리가 먼 30편 제외됨
- 핵심 논문 13편 ⭐ 표시

### 3. [papars.yaml](papars.yaml) — 구조화된 데이터
- 논문들의 메타데이터, 핵심 아이디어, 프로젝트 관련성, 구현 팁 등을 YAML 형태로 관리

---

## ✅ 완료된 논문 리뷰 (Completed Papers)

이미 읽고 분석이 완료된 논문들의 핵심 요약입니다.

### 1. Self-Instruct: Aligning Language Models with Self-Generated Instructions (ACL 2023)
- **핵심 아이디어**: 175개 seed instruction에서 시작하여 LM이 스스로 52k instructions를 생성-필터링하는 파이프라인. Output-first 방식으로 다양성 확보.
- **프로젝트 관련성**: 한국어 MWP CG 데이터가 부족한 상황에서, 교사 LLM을 활용해 도메인 특화 데이터를 증강하는 프레임워크로 채택.
- **구현 포인트**: ROUGE-L 필터링, Classification 태스크 구분, Seed 설계.

### 2. Distilling Step-by-Step! (ACL 2023 Findings)
- **핵심 아이디어**: `Target`만 학습하는 것이 아니라, `Rationale`(추론 과정)을 멀티태스크로 함께 학습하여 적은 데이터로 성능 극대화.
- **프로젝트 관련성**: CG(Concept Graph) 자체가 Rationale 역할을 하므로, `L_label + λ L_graph` 형태의 손실 함수 설계에 직접 적용.
- **구현 포인트**: `[label]` / `[rationale]` 프리픽스 분리 학습, λ 튜닝.

### 3. Phased Instruction Fine-Tuning (ACL 2024 Findings)
- **핵심 아이디어**: "Progressive Alignment Hypothesis" — 쉬운 것부터 어려운 순서로 단계적 학습(Curriculum Learning)이 효과적임.
- **프로젝트 관련성**: 복잡한 CG 구조를 한 번에 학습하기보다, Triple 수가 적거나 관계가 단순한 것(Phase 1)부터 복합 추론(Phase 2)으로 확장.
- **구현 포인트**: GPT-4 기반 난이도 평가(1-5점), 데이터셋 분할 및 순차적 Up-training.

---

## 📊 진행 상황 요약

| 상태 | 논문 수 | 비고 |
|------|---------|------|
| ✅ 완료 | 3 | 핵심 방법론 (데이터 생성, 증류, 커리큘럼) 파악 완료 |
| 📅 예정 | 14 | P0 (8편) + P1 (6편) — [MUST-READ-PLAN.md](MUST-READ-PLAN.md) 참조 |
| 🗃️ 후보 | 38 | [UNIFIED-PAPER-LIST.md](UNIFIED-PAPER-LIST.md) 참조 |
