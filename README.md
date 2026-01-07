# LM-based-KG 논문 자료 디렉토리

**Last updated:** 2026-01-07

## 📁 디렉토리 구조

```
LM-based-KG-papers/
├── MUST-READ-PLAN.md      # 정본 must-read shortlist + 4주 실행 계획
├── UNIFIED-PAPER-LIST.md  # 테마별 전체 후보 풀 (55편)
├── README.md              # 이 파일
├── papars.yaml            # 초기 후보 풀 (12편, 구조화된 원본)
└── ...                    # 기타 참고 자료
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
- 연구 방향과 거리가 먼 30편 제외됨 (코드 생성, 역방향 증류, Diffusion, RAG 등)
- 핵심 논문 13편 ⭐ 표시

### 3. [papars.yaml](papars.yaml) — 초기 후보
- 구조화된 YAML 형태의 원본 후보 풀

## ✅ 이미 읽은 논문 (3편)

| # | 논문 | 학회 | 상태 |
|---|------|------|------|
| 1 | Self-Instruct | ACL 2023 | ✅ 완료 |
| 2 | Distilling Step-by-Step | ACL 2023 (Findings) | ✅ 완료 |
| 3 | Phased Instruction Fine-Tuning | ACL 2024 (Findings) | ✅ 완료 |

## 📊 논문 통계

| 테마 | 논문 수 | 핵심(⭐) |
|------|---------|----------|
| Structured Rationale Distillation | 19 | 5 |
| Test-time Scaling & Inference | 19 | 4 |
| Model Merging & LoRA | 7 | 2 |
| Math Reasoning & KG Integration | 10 | 2 |
| **총계** | **55** | **13** |

## 🔗 관련 문서

- [../PLAN.md](../PLAN.md) — 연구 마스터 플랜 (3축 정의)
- [../README.md](../README.md) — 프로젝트 전체 개요
