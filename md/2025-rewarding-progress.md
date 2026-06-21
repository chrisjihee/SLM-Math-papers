# Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning review

## 1. Metadata

- Title: Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning
- Authors: Amrith Setlur, Chirag Nagpal, Adam Fisch, Xinyang Geng, Jacob Eisenstein, Rishabh Agarwal, Alekh Agarwal, Jonathan Berant, Aviral Kumar (Google Research / Google DeepMind / Carnegie Mellon University)
- Year: 2024 (arXiv 2410.08146, 2024-10)
- Venue / Status: ICLR 2025 (legacy 분류 기준; arXiv comment 미표기 — 외부/legacy 확정)
- Links:
  - Paper: https://arxiv.org/abs/2410.08146
  - GitHub / Code (official): 미확인
- Source PDF (local, source-of-record): `paper/2025-rewarding-progress.pdf`
- Source Grounding Log:
  - PDF: `paper/2025-rewarding-progress.pdf` — 31 pages, sha256 `b6d4572d38985f10bfa418d8db857877a6800a5e85984642a525d60565364864`, pypdf/pymupdf 본문 추출 정상(약 99k자). title/authors/method/models 직접 확인.
  - arXiv abstract: PAV/progress/prover policy·8% gain·1.5–5× compute efficiency 확인.
  - legacy 자료: 문장단위 reading 노트는 `archive/legacy-reading-pipeline-2026-01/reading/05.…`에 historical-only 보존(`contents/05`은 삭제). published ICLR2025 버전 PDF는 `archive/legacy-paper-filenames/05.…pdf`에 보존(canonical preprint PDF와 sha256 다름). source-of-record는 canonical PDF 재추출.
  - TeX source/ar5iv: 미사용. venue(ICLR 2025)는 외부/legacy 확정.
- Paper Type: `verifier (process reward / PRM)` / `training + inference-time` — verifier/PRM boundary reference
- Reading Status: `strategically-read`
- Current Priority: `P1`

## 2. One-line Summary

Rewarding Progress는 process reward를 "progress"(정답 도달 likelihood의 변화 = advantage)로 정의하고, base policy와 구별되는 **prover policy** 하에서 이를 자동으로 측정하는 **Process Advantage Verifiers(PAV)** 를 제안해, outcome reward 대비 test-time search·RL에서 정확도(약 8%↑)와 compute 효율(1.5–5×)을 높인 automated process verifier 논문이다.

## 3. 핵심 문제 설정

- 문제: outcome reward model(ORM)은 최종 정답만 보상해 multi-step reasoning의 credit assignment가 약하다. PRM은 step별 feedback을 주지만 보통 비싼 human step annotation이 필요하고 무엇을 보상할지 정의가 모호하다.
- 해법: step별 보상을 **"progress" = prover policy 하에서 정답 확률의 advantage(변화)** 로 정의하고 자동으로 측정(PAV). 이 progress 신호로 test-time search(beam)와 RL credit assignment를 개선.
- 내 연구와의 연결: 이 논문은 **automated process verifier / progress reward / process verification scaling을 선점**했다. 우리 연구에서 verifier는 final decision·STOP 후보일 뿐, **main novelty는 upstream heterogeneous path-pool construction**이다.

## 4. 핵심 방법

- progress 정의: 각 step의 reward = **advantage**(그 step 이후 정답에 도달할 likelihood의 변화), **prover policy**(base와 구별) 기준.
- 자동화: human step label 없이 prover로부터 progress 신호를 추정(PAV 학습).
- 사용처: (1) **test-time search**(beam/best-of-N 가이드), (2) **RL**의 dense credit assignment.
- selection unit: **step / path**(verifier-guided). heterogeneous path-family 획득은 아님.
- 실험(PDF/abstract):
  - model: **Gemma2 2B/9B/27B**, GSM8K/MATH.
  - baseline: ORM; 결과: 정확도 약 **8%↑**, compute 효율 **1.5–5×↑**.

## 5. SLM-Math 관점의 재해석

- 이 논문은 직접 baseline 경쟁자라기보다 **process verifier/PRM cluster의 최신 reference**(Let's Verify·Math-Shepherd·ThinkPRM과 묶음)다.
- 공통점: verifier로 step/candidate를 평가해 test-time search·선택을 개선.
- 차이점:
  - 이 논문은 **verifier(progress reward) 자체를 설계·scaling**. 우리는 verifier가 평가할 **candidate pool을 어떻게 state-conditioned하게 구성·중단**할지(upstream).
  - step-level dense reward vs 우리 route/family-level lightweight estimator.
- 연결: PAV류 progress 신호를 우리 **STOP criterion / final decision** 후보로 차용 가능하되, generation–verification budget split을 명시하고 verifier compute를 TTC budget에 계상.

## 6. 우리 연구에 대한 novelty risk

- **process reward / automated process verifier / verifier-guided selection / progress(advantage) reward**를 이미 선점 → 이 자체를 우리 novelty로 쓰면 충돌.
- "verifier로 step을 평가해 search를 개선" 아이디어도 선점.
- 위험 framing: `verifier/PRM 도입이 우리 기여`, `process reward로 candidate selection을 개선`.
- 단, 이 논문은 verifier 설계(다운스트림)라 우리 upstream path-pool construction과 결이 다름.

## 7. 우리가 빌릴 수 있는 것

- framing: outcome vs process reward, credit assignment, progress(advantage) 정의, prover policy.
- baseline: ORM vs PRM/PAV-guided selection을 우리 final-decision/STOP 비교군으로.
- metric: accuracy + **compute efficiency(verifier overhead 포함)** — generation–verification budget split 설계에 직접 활용.
- ablation: verifier on/off, step-level vs route-level 신호, verifier budget sweep.
- terminology: `process advantage verifier(PAV)`, `progress reward`, `prover policy`, `credit assignment`, `compute-efficient verification`.

## 8. 우리가 하면 안 되는 주장

- `process verifier / process reward / progress reward를 우리가 처음 제안한다`.
- `verifier-guided selection / PRM 도입이 우리 기여다`.
- `automated process verification을 우리가 처음 한다`.
- 이 논문 대비 verifier 성능 SOTA 경쟁, verifier compute를 무시한 정확도만 비교.

## 9. baseline / ablation 반영 아이디어

- verifier는 우리 pipeline의 **final decision / STOP** 후보로만 두고, 중심 비교는 **path-pool construction(upstream)**.
- **generation–verification budget split**을 명시적 ablation으로(같은 총 budget에서 더 생성 vs 더 검증).
- PAV류 progress 신호를 route/family-level lightweight estimator와 비교(step-level 대비 cost·효과).
- verifier overhead를 TTC budget에 계상한 compute-efficiency 곡선.

## 10. Related Work에 넣을 문장 초안

Rewarding Progress(Setlur et al., ICLR 2025)는 process reward를 prover policy 하에서의 "progress"(정답 도달 확률의 advantage)로 정의하고 이를 자동으로 측정하는 Process Advantage Verifiers(PAV)를 제안하여, outcome reward 대비 test-time search와 RL credit assignment에서 정확도와 compute 효율을 크게 높였다. 이는 automated process verification과 process-reward scaling의 최신 대표 연구다.

본 연구는 process verifier나 progress reward 자체를 새 기여로 두지 않는다. 우리는 verifier(PAV·PRM 류)를 final decision 또는 STOP criterion 후보로만 활용하고, 핵심 novelty는 제한된 test-time compute 안에서 verifier가 평가할 candidate pool을 현재 reasoning state에 따라 어떻게 구성·중단할지를 다루는 **upstream heterogeneous path-pool construction**과 generation–verification budget split에 둔다. verifier compute는 TTC budget에 명시적으로 계상한다.

## 11. 현재 우선순위와 다음 액션

- 현재 우선순위: `P1`
- 위협도: 중간 (verifier/process-reward claim boundary; 직접 baseline 경쟁은 아님)
- 구현 결정: full reproduction 비대상. verifier는 final-decision/STOP 후보로만, 비교 중심은 upstream path-pool.
- 지금 할 일:
  - Rewarding Progress를 Let's Verify·Math-Shepherd·ThinkPRM과 함께 verifier/PRM cluster의 P1 reference로 고정.
  - `process verifier/process reward/verifier-guided selection 자체를 novelty로 쓰지 않기` wording 가드.
  - generation–verification budget split·verifier overhead 계상을 평가 설계에 명시.
- 나중으로 미뤄도 되는 일: PAV 재현, Gemma2 search/RL 평가.
- 한 줄 결론: Rewarding Progress는 automated process verifier(progress reward)를 선점한 reference이며, 우리 기여는 verifier 자체가 아니라 verifier가 평가할 path-pool의 upstream 구성·STOP·budget split임을 분명히 하는 데 쓴다.
