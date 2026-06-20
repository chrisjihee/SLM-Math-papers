# Reasoning Language Models for Root Cause Analysis in 5G Wireless Networks (TeleLogs) review

## 1. Metadata

- Title: Reasoning Language Models for Root Cause Analysis in 5G Wireless Networks (dataset: TeleLogs)
- Authors: Mohamed Sana, Nicola Piovesan, Antonio De Domenico, Yibin Kang, Haozhe Zhang, Merouane Debbah, Fadhel Ayed (Paris Research Center, Huawei / Huawei China / Khalifa University)
- Year: 2025
- Venue / Status: arXiv 2507.21974 (정식 venue 미표기)
- Links:
  - Paper: https://arxiv.org/abs/2507.21974
  - Dataset (official): https://huggingface.co/datasets/netop/TeleLogs (MIT; 접근 시 contact-sharing 동의 필요)
  - GitHub / Code (official): 미확인
- Source PDF (local, source-of-record): `paper/2025-telelogs.pdf`
- Source Grounding Log:
  - PDF: `paper/2025-telelogs.pdf` — 10 pages, sha256 `cd4083b0749035f545c63b493130e10324236b0e780466b91916a1aecd45300b`, pypdf/pymupdf 본문 추출 정상(약 43k자). title/authors/abstract/dataset/metric 직접 확인.
  - HF dataset card(netop/TeleLogs): fields/root-cause/metric/license 교차확인.
  - arXiv TeX/ar5iv: 미사용. official code URL 미확인.
- Paper Type: `benchmark` + `domain LLM framework (RCA)` — NFM bridge stage 3 reference
- Reading Status: `strategically-read`
- Current Priority: `P1` (NFM bridge stage 3)

## 2. One-line Summary

이 논문은 5G 네트워크의 throughput 저하를 진단하는 Root Cause Analysis를 위해 annotated troubleshooting 문제로 구성된 TeleLogs 벤치마크를 제시하고 lightweight LLM RCA framework·domain adaptation을 평가한 연구로, RCA/log reasoning을 우리 verifier·evidence-selection·STOP 아이디어로 옮겨보는 NFM bridge stage 3다(단, thesis core는 RCA가 아님).

## 3. 핵심 문제 설정

- 문제: 모바일 네트워크의 RCA는 해석가능성·도메인 전문성·인과추론이 필요해 어렵고, open-source reasoning LLM도 잘 못한다.
- 해법: **TeleLogs** 데이터셋(annotated troubleshooting, 5G throughput<임계 진단, 8 predefined root causes)으로 RCA 능력을 benchmark하고, lightweight LLM RCA framework + domain-specific adaptation을 제안·평가.
- 내 연구와의 연결: TeleLogs는 thesis core가 아니라 **log/RCA reasoning bridge(stage 3)**. verifier/evidence-first reasoning/STOP과 연결하되, **thesis core를 RCA로 이동하지 않는다**.

## 4. 핵심 방법(벤치마크 + framework)

- 데이터(TeleLogs): network engineering params(gNodeB/antenna/beamforming) + user-plane data(speed/downlink throughput/RSRP/SINR/neighbor/RB) + symptom(throughput < 임계) + **8 predefined root causes**.
- task: 주어진 로그/지표에서 root cause를 진단(분류/추론).
- framework: lightweight LLM RCA + domain-specific adaptation(open-source reasoning LLM이 어려워 adaptation 필요).
- 평가 metric: **pass@1**, **maj@4**(majority voting@4 = Self-Consistency).
- selection unit(우리 관점): **root-cause answer + evidence**. benchmark가 핵심, framework는 domain adaptation 포함.

## 5. SLM-Math 관점의 재해석

- TeleLogs는 method 경쟁자라기보다 **NFM bridge stage 3 평가 자원이자 RCA reference**다.
- 공통점: 여러 후보(root cause) 중 evidence 기반 선택 + **maj@4(=SC)** → 우리 voting/STOP framing과 닿음.
- 차이점: 입력이 시계열/구조화 로그 + 도메인 지식이라 GSM8K word problem과 task form이 크게 다름. RCA는 인과추론·evidence sufficiency가 핵심.
- 연결: path family 후보 = `direct diagnosis`, `evidence-first reasoning`, `hypothesis generation`, `verifier/checker route`, `retrieval route`. STOP은 **evidence sufficiency / hypothesis confidence / disagreement resolution**으로 연결 가능. 단 bridge/validation 후보로만.

## 6. 우리 연구에 대한 novelty risk

- 낮음(benchmark/domain framework). 다만 경계(가장 중요):
  - `RCA 자체가 우리 novelty다`로 쓰면 안 됨.
  - `log analysis를 main thesis로 전환`하면 안 됨.
  - `TeleLogs만으로 NFM reasoning을 대표한다`고 과장 금지.
  - maj@4는 이미 SC majority vote이므로 `SC/voting을 우리가 도입`처럼 쓰면 안 됨.

## 7. 우리가 빌릴 수 있는 것

- framing: RCA의 evidence sufficiency·causal reasoning·hypothesis confidence, domain adaptation 필요성.
- baseline/metric: **pass@1, maj@4(=SC@4)** — 우리 fixed SC@K·budget-matched 비교와 정렬.
- analysis: root cause별 난이도, evidence-first vs direct, disagreement resolution.
- terminology: `root cause analysis`, `evidence sufficiency`, `hypothesis confidence`, `maj@k`, `troubleshooting`.

## 8. 우리가 하면 안 되는 주장

- `RCA / log reasoning을 우리가 처음/일반적으로 해결한다`.
- `main thesis를 RCA/log analysis로 전환한다`.
- `TeleLogs로 NFM 전체를 대표한다`.
- `maj@4/majority vote가 우리 기여다`.
- `NFM foundation model을 우리가 제안한다`.

## 9. baseline / ablation 반영 아이디어

- bridge stage 3에서 `direct diagnosis/evidence-first/hypothesis-gen/verifier-route/retrieval` path family를 **same budget에서 maj@4 대비** 비교.
- evidence sufficiency 기반 STOP(충분한 증거 모이면 멈춤) vs fixed sampling 비교.
- root-cause disagreement resolution(여러 가설 충돌 시 verifier/voting) 분석 — 우리 voting/verifier framing의 domain transfer.
- 단, telecom-specific adaptation 부담이 크므로 mainline 우선, TeleLogs는 후속.

## 10. Related Work에 넣을 문장 초안

Sana et al.(2025)은 5G 네트워크의 throughput 저하 Root Cause Analysis를 위해 annotated troubleshooting 문제로 구성된 TeleLogs 벤치마크를 제시하고, lightweight LLM 기반 RCA framework와 domain-specific adaptation을 pass@1·maj@4로 평가하여 open-source reasoning LLM이 이 문제에 어려움을 겪음을 보였다.

본 연구는 RCA나 log reasoning 자체를 새 기여로 두지 않으며, main thesis를 RCA로 전환하지 않는다. 우리는 TeleLogs를 math mainline에서 정립한 state-conditioned reasoning path-pool allocation과 verifier/voting 아이디어를 log/RCA 도메인으로 확장해 검증하는 bridge benchmark(stage 3)로만 사용하며, 특히 maj@4가 Self-Consistency majority vote와 동일하므로 evidence-first 같은 heterogeneous path family와 evidence-sufficiency 기반 STOP이 fixed SC를 능가하는지를 RCA 도메인에서 확인하는 application 실험으로 위치시킨다.

## 11. 현재 우선순위와 다음 액션

- 현재 우선순위: `P1` (NFM bridge stage 3)
- 위협도: 낮음 (benchmark; thesis-core가 RCA로 이동하지 않게 wording 주의)
- NFM bridge role: stage 3 (log/RCA reasoning). thesis core 아님.
- 지금 할 일:
  - TeleLogs를 NFM bridge stage 3로 고정, `direct/evidence-first/hypothesis-gen/verifier-route/retrieval` path family + maj@4 baseline 정렬.
  - `RCA/log reasoning이 우리 novelty`·`thesis를 RCA로 전환`·`TeleLogs로 NFM 대표` 금지 wording 유지.
  - evidence sufficiency / hypothesis confidence / disagreement 기반 STOP을 RCA 도메인에서 검토.
- 나중으로 미뤄도 되는 일: TeleLogs domain adaptation 재현, RCA framework 재현(telecom adaptation 부담 큼).
- 한 줄 결론: TeleLogs는 우리 verifier/voting/STOP 아이디어를 5G RCA 도메인으로 옮겨보는 NFM bridge stage 3 benchmark이며, thesis core(math reasoning/TTC allocation)를 RCA/log analysis로 대체하지 않는다.
