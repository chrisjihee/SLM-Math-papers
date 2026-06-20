# TeleResilienceBench: Quantifying Resilience for LLM Reasoning in Telecommunications review

## 1. Metadata

- Title: TeleResilienceBench: Quantifying Resilience for LLM Reasoning in Telecommunications
- Authors: Pranshav Gajjar, Emmanuel Ojo, Vijay K Shah (NextG Wireless Lab, North Carolina State University)
- Year: 2026
- Venue / Status: arXiv 2605.09929 (정식 venue 미표기)
- Links:
  - Paper: https://arxiv.org/abs/2605.09929
  - GitHub / Code (official): https://github.com/prnshv/TeleResilienceBench
- Source PDF (local, source-of-record): `paper/2026-teleresiliencebench.pdf`
- Source Grounding Log:
  - PDF: `paper/2026-teleresiliencebench.pdf` — 13 pages, sha256 `a1528d6348461efe82de4fd90bd9638a040020177b8ca2414f610d3a040ddb5e`, pypdf/pymupdf 본문 추출 정상(약 70k자). title/authors/abstract/method/models/code 직접 확인.
  - **Link-check: 통과** — arXiv 2605.09929가 실제 TeleResilienceBench임을 PDF 제목으로 확정(이전 `link-check-needed` 해소).
  - 그룹: NC State NextG Wireless Lab (netop/Huawei와 무관).
  - arXiv TeX/ar5iv: 미사용.
- Paper Type: `benchmark` / `reasoning resilience / recovery (telecom)` — NFM extension reference
- Reading Status: `strategically-read`
- Current Priority: `P2` (NFM extension / long-term)

## 2. One-line Summary

TeleResilienceBench는 모델이 prior step·upstream agent·자기 이전 생성으로부터 **결함 있는 reasoning trace를 이어받아 계속·교정**하는 "reasoning resilience"를, 7개 telecom sub-domain(GSMA Open-Telco)에서 weak generator의 실패 trace를 중간 절단해 target model이 복구하게 하는 방식으로 정량화한 benchmark다.

## 3. 핵심 문제 설정

- 문제: telecom 워크플로에서 LLM은 task accuracy만으로 부족하다. 실제로는 이미 잘못 진행 중인 reasoning(이전 step/상류 agent/자기 생성)을 **이어받아 회복**해야 한다.
- 해법: **reasoning resilience** 정의·정량화 — weak generator의 실패를 모아 flawed reasoning trace를 **midpoint에서 truncate**, target model이 **continue+correct**하게 하고 recovery를 측정. 7 telecom sub-domain(GSMA Open-Telco), 8 model 평가.
- 내 연구와의 연결: 이 benchmark는 **현재(부분·결함) reasoning state를 이어받아 회복**하는 설정이라, 우리 "current reasoning state-conditioned path acquisition/STOP" framing과 **개념적으로 가장 가깝다**. 다만 여전히 NFM extension/long-term bridge로 둔다(thesis core 아님).

## 4. 핵심 방법(벤치마크 구성)

- 인스턴스 구성: weak generator model의 실패 사례 수집 → flawed reasoning trace를 **중간(midpoint)에서 절단** → target model에게 **이어서 풀고 교정**하도록 요청.
- 도메인: GSMA Open-Telco LLM suite 기반 **7 telecom sub-domains** (+ auxiliary TeleMath numerical eval).
- 평가 모델: **8개**(Qwen3.5, Gemma4, Nemotron-3 families).
- metric: **CR%(correction/recovery rate)** 등(예: TeleMath auxiliary 23.4% CR%).
- selection unit(우리 관점): **continuation/correction of a partial trace**. benchmark, method 제안 아님.

## 5. SLM-Math 관점의 재해석

- TeleResilienceBench는 method 경쟁자라기보다 **NFM extension 평가 자원이자 reasoning-recovery reference**다.
- 공통점: **현재 reasoning state(부분 trace)를 조건으로** 다음 행동을 결정 → 우리 state-conditioned framing과 직접 닿음.
- 차이점: 입력이 telecom 도메인 + "given a broken trace, recover"라 우리 main setup(빈 상태에서 path-pool 구성)과 다르다. recovery/continuation이 핵심.
- 연결: 우리 STOP/재시도/path switch 결정을 "현재 trace가 틀렸을 때 어떤 path family로 갈아탈지"로 확장하는 reference. recovery setting을 우리 macro-action(`restart`, `switch-family`, `verify-then-continue`) 설계의 개념적 참고로 사용 가능. 단 bridge/extension로만.

## 6. 우리 연구에 대한 novelty risk

- 낮음(benchmark). 다만 경계:
  - `reasoning resilience/recovery 자체가 우리 novelty다`로 쓰면 안 됨(이 benchmark가 정의·정량화 선점).
  - `우리가 reasoning recovery를 처음 제안한다`고 쓰면 안 됨.
  - `thesis를 telecom resilience로 전환`하면 안 됨.
  - `TeleResilienceBench로 NFM 전체를 대표한다`고 과장 금지.
- 특히 우리 state-conditioned framing과 가까우므로 **"recovery를 우리가 발명"한 것처럼 읽히지 않게** 인용 주의.

## 7. 우리가 빌릴 수 있는 것

- framing: reasoning resilience, 부분 trace로부터의 continuation/correction, recovery rate metric.
- baseline/metric: CR%(recovery rate) — 우리 STOP/switch 후 정답 회복률 측정에 참고.
- analysis: midpoint-truncated trace에서 path switch vs continue 비교 → 우리 macro-action 설계.
- terminology: `reasoning resilience`, `trace continuation/correction`, `correction rate(CR%)`, `inherited reasoning`.

## 8. 우리가 하면 안 되는 주장

- `reasoning resilience/recovery를 우리가 처음 제안/정의한다`.
- `telecom resilience를 main thesis로 전환한다`.
- `TeleResilienceBench로 NFM 전체를 대표한다`.
- `우리 state-conditioned framing이 이 benchmark를 일반적으로 해결한다`.
- `NFM foundation model/telecom benchmark 구축이 우리 contribution이다`.

## 9. baseline / ablation 반영 아이디어

- 우리 macro-action에 `verify-then-continue` / `switch-family-on-low-confidence` / `restart`를 두고, "broken trace recovery" 시 어떤 action이 유리한지(개념적으로 TeleResilienceBench 설정과 정렬) 분석.
- CR%(recovery rate)를 우리 STOP/재시도 정책 평가 보조 지표로 참고.
- 단, telecom-specific이므로 mainline(math) 우선, 이 benchmark는 long-term extension.

## 10. Related Work에 넣을 문장 초안

TeleResilienceBench(Gajjar et al., 2026)는 LLM이 telecom 워크플로에서 이미 잘못 진행 중인 부분 reasoning trace를 이어받아 계속·교정하는 능력(reasoning resilience)을, weak generator의 실패 trace를 중간에서 절단하고 target model이 복구하게 하는 방식으로 7개 telecom sub-domain에 걸쳐 정량화한 벤치마크다.

본 연구는 reasoning resilience나 telecom recovery 자체를 새 기여로 두지 않으며, thesis를 telecom으로 전환하지 않는다. 다만 이 benchmark가 다루는 "현재(부분·결함) reasoning state를 조건으로 다음 행동을 결정한다"는 설정은 우리의 state-conditioned reasoning path acquisition·STOP framing과 개념적으로 닿으므로, 우리는 이를 macro-action(예: verify-then-continue, switch-family, restart) 설계와 recovery 측면을 검증하는 long-term NFM extension reference로만 사용한다.

## 11. 현재 우선순위와 다음 액션

- 현재 우선순위: `P2` (NFM extension / long-term)
- 위협도: 낮음 (benchmark; state-conditioned framing과 가까워 인용 wording 주의)
- NFM bridge role: extension/long-term (reasoning recovery). thesis core 아님.
- 지금 할 일:
  - TeleResilienceBench를 NFM extension reference로 고정(link-check 통과 기록).
  - `reasoning resilience/recovery를 우리가 처음 제안`·`thesis를 telecom으로 전환` 금지 wording 유지.
  - recovery 설정을 우리 macro-action(switch/restart/verify-then-continue) 설계의 개념적 참고로만.
- 나중으로 미뤄도 되는 일: TeleResilienceBench 재현·평가, GSMA Open-Telco suite 확장.
- 한 줄 결론: TeleResilienceBench는 우리 state-conditioned reasoning framing과 가장 가까운 NFM extension benchmark이며, reasoning recovery를 우리가 발명한 것처럼 쓰지 않고 long-term application reference로만 둔다.
