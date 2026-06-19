# Chain-of-Thought Prompting Elicits Reasoning in Large Language Models review

## 1. Metadata

- Title: Chain-of-Thought Prompting Elicits Reasoning in Large Language Models
- Authors: Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed Chi, Quoc Le, Denny Zhou
- Year: 2022
- Venue / Status: NeurIPS 2022 (arXiv 2201.11903는 2022-01 공개, v6 2023-01)
- Links:
  - Paper: https://arxiv.org/abs/2201.11903
  - GitHub / Model: 공식 official code repository 없음 (prompting 기법; exemplar는 논문 부록 제공)
- Code / Data:
  - 별도 공개 코드/모델 없음. 평가 benchmark는 기존 공개 데이터(GSM8K 등) 사용.
  - primary paper URL만 관리(code URL 없음).
- Paper Type:
  - `inference-time` / `prompting`
  - `canonical reasoning-path baseline`
- Reading Status: `strategically-read`
- Current Priority: `P0`

## 2. One-line Summary

CoT는 few-shot exemplar에 중간 추론 단계(자연어 rationale)를 함께 보여주면 충분히 큰 LLM에서 multi-step arithmetic·commonsense·symbolic reasoning 능력이 emergent하게 발현됨을 보인, reasoning prompting의 canonical 원형 논문이다.

## 3. 핵심 문제 설정

- 이 논문이 푸는 질문은 **추가 학습(finetuning) 없이, prompting만으로 LLM의 multi-step reasoning을 끌어낼 수 있는가**이다.
- 기존 한계로 보는 것:
  - standard few-shot prompting(`question→answer`)은 산술·논리 multi-step 문제에서 scale을 키워도 잘 늘지 않는다(flat scaling).
  - finetuning/verifier 기반 접근은 task별 데이터·학습이 필요하다.
- 해법은 **exemplar에 `question → reasoning steps → answer` 형태의 rationale을 넣어주는 것**뿐이며, 이로써 큰 모델에서 reasoning이 발현(emergent ability at scale)된다.
- 내 연구와의 연결:
  - CoT는 우리 연구의 **가장 강한 baseline path family이자 모든 비교의 기준점(anchor)**이다.
  - 우리의 path family universe(`direct / CoT / prompt-diverse CoT / CG / PAL / PoT / verifier-guided`)에서 CoT는 reference origin이다.
  - 우리 기여는 CoT를 개선하는 것이 아니라, CoT를 포함한 heterogeneous family를 제한 TTC 안에서 언제 더 획득/중단할지 결정하는 상위 orchestration이다.

## 4. 핵심 방법

- reasoning path:
  - 단일 자연어 rationale chain(`step1 → step2 → … → answer`)을 생성하는 prompting.
- sampling:
  - 원 논문은 기본적으로 **greedy decoding** (단일 path). multi-sample/voting은 포함하지 않음(그건 후속 Self-Consistency의 몫).
- self-consistency:
  - 없음(원 논문 범위 밖).
- test-time compute:
  - 명시적 TTC 제어/scaling 개념은 없음. 다만 "rationale 생성 → 더 많은 생성 token"이라는 점에서 우리 token-budget 논의의 하한 기준이 된다.
- verifier / reward / search:
  - 없음. 오히려 "finetuned GPT-3 + verifier"를 prompting만으로 능가한다는 점을 강조.
- selection unit 관점:
  - 통제 단위는 **prompt(exemplar) 설계**이며, path family 간 선택이나 budget allocation, STOP은 다루지 않는다.
- 핵심 관찰:
  - reasoning은 **충분한 model scale에서만** 안정적으로 발현되는 emergent ability다(작은 모델에선 오히려 손해일 수 있음 → SLM 관점에서 중요).

## 5. SLM-Math 관점의 재해석

- CoT는 내 연구의 경쟁자가 아니라 **필수 baseline path family이자 origin reference**다.
- 공통점:
  - 중간 추론(rationale)의 가치를 정면으로 다룬다.
  - 추가 학습 없이 inference-time 행동을 바꾼다.
- 차이점:
  - CoT의 핵심은 **단일 rationale path를 잘 유도하는 prompting**이다.
  - 내 연구의 핵심은 **여러 path family를 state-conditioned하게 구성·선택·검증·중단**하는 것이다.
- SLM 특화 함의:
  - CoT가 "큰 모델에서 emergent"라고 했으므로, **작은 모델에서는 단일 CoT가 항상 유리하지 않을 수 있다**는 점이 우리 연구의 동기를 강화한다(단일 long CoT보다 heterogeneous pool + 적절한 STOP이 필요한 이유).
- 안전한 한 문장 차별화:
  - CoT는 가장 강한 단일 rationale baseline을 제공하고, 내 연구는 **그 baseline 위에서 어떤 path family를 언제 더 추가하고 멈출지**를 다룬다.
- 특히 `CG`는 **CoT의 replacement가 아니라 auxiliary / structured family 중 하나**로 위치시킨다(`CG > CoT` 주장 금지).

## 6. 우리 연구에 대한 novelty risk

- `CoT(중간 추론 단계 유도) 자체`는 이 논문이 원형이므로 절대 우리 novelty가 될 수 없다.
- `prompt에 reasoning을 넣으면 좋아진다`도 CoT가 선점.
- `rationale 생성이 multi-step 문제에 도움된다`도 CoT가 선점.
- 따라서 위험한 framing:
  - `CG/structured rationale가 CoT보다 본질적으로 우월하다` (금지)
  - `우리는 CoT prompting을 개선한다`를 핵심 기여로 쓰기
  - prompt-diversity(CoT_Lv1/2/3) 효과를 우리만의 발견처럼 쓰기
- 주의할 혼동 지점:
  - **prompt-diversity 효과**(여러 CoT 변형)와 **structural effect**(CG 등 구조)를 분리하지 않으면, "다양성 이득"을 "구조 이득"으로 오인할 위험.
- 다만 CoT는 prompting origin이라, RASC/Scaling-TTC 같은 inference-time allocation 직접 baseline과는 위협 성격이 다르다(우리 위험은 주로 wording/baseline 정의 쪽).

## 7. 우리가 빌릴 수 있는 것

- problem framing:
  - reasoning은 emergent하며 model scale/문제 난이도에 의존한다(→ SLM에서는 단일 CoT 한계가 더 큼).
  - inference-time 행동 변화만으로 큰 향상이 가능하다.
- baseline:
  - few-shot **CoT**(greedy)를 모든 path-family 비교의 origin baseline으로 고정.
  - `direct(answer-only) prompting`을 하한 baseline으로, CoT를 그 위 기준으로.
  - prompt-diverse CoT(여러 exemplar/표현)를 우리 pool 다양화의 한 축으로.
- metric:
  - GSM8K(주력), SVAMP, ASDiv, AQuA, MAWPS(arithmetic) — 우리 GSM8K/MATH500 평가와 정렬.
  - exact-match accuracy, generated reasoning-token 길이(budget proxy).
- ablation:
  - `direct vs CoT vs prompt-diverse CoT`의 단일-path 기준선.
  - model scale에 따른 CoT 이득 곡선(SLM에서 단일 CoT의 한계 보이기).
  - prompt-diversity 이득 vs structural(CG) 이득의 **분리 ablation**.
- terminology(차용):
  - `chain-of-thought`, `intermediate reasoning steps`, `rationale`, `emergent ability at scale`, `few-shot exemplar`.

## 8. 우리가 하면 안 되는 주장

- `중간 추론 단계(rationale)를 유도하는 것이 새롭다`고 쓰면 안 된다.
- `CoT prompting을 개선하는 것이 우리 핵심 기여다`라고 쓰면 안 된다.
- `CG/structured rationale가 CoT보다 일반적으로 우월하다`고 쓰면 안 된다.
- `prompt에 reasoning을 넣으면 성능이 오른다`를 새 관찰처럼 쓰면 안 된다.
- CoT 대비 raw GSM8K/MATH SOTA 경쟁 프레임으로 가면 안 된다.

## 9. baseline / ablation 반영 아이디어

- few-shot CoT(greedy)를 모든 실험표의 **origin baseline**으로 고정하고, 그 위에 SC-CoT / Multiple-CoT / heterogeneous pool을 올린다.
- `direct → CoT → prompt-diverse CoT → +CG → +PAL/PoT → +verifier-guided`의 점증 ablation으로 각 family의 한계 기여를 분리.
- **prompt-diversity 통제 실험**: 같은 budget에서 "CoT 표현만 다양화"와 "구조(CG) 추가"를 분리해, 다양성 이득과 구조 이득을 구분.
- SLM scale에서 단일 CoT의 saturation/역효과 지점을 보여, heterogeneous pool + STOP의 필요성을 동기화.
- reasoning-token 길이를 함께 기록해 s1/DeepSeekMath 노트의 token-budget 비교와 정합.

## 10. Related Work에 넣을 문장 초안

Chain-of-Thought prompting(Wei et al., NeurIPS 2022)은 few-shot exemplar에 중간 추론 단계를 함께 제시하면 충분히 큰 언어모델에서 산술·상식·기호 추론 능력이 발현됨을 보인 대표적인 연구로, 별도의 finetuning 없이 prompting만으로 GSM8K 등에서 큰 향상을 이루었다. 이 연구는 이후 거의 모든 reasoning 연구의 기준점이 되었으며, 단일 자연어 rationale path가 multi-step 문제 해결의 강력한 기본 형태임을 확립했다.

그러나 CoT는 단일 reasoning rationale을 유도하는 prompting 기법이며, 제한된 test-time compute 안에서 서로 다른 reasoning path family를 어떻게 구성하고 선택하며 언제 멈출지는 다루지 않는다. 본 연구는 CoT를 가장 강한 baseline path family이자 비교 기준으로 삼되, 주어진 small language model이 현재 reasoning state와 남은 budget을 바탕으로 CoT, prompt-diverse CoT, structured rationale(CG), PAL/PoT, verifier-guided path 등 heterogeneous reasoning path family 중 무엇을 추가로 획득하고 언제 멈출지를 결정하는 **state-conditioned test-time compute allocation** 문제에 위치한다. 특히 본 연구는 CoT를 대체하려는 것이 아니라, CoT가 emergent ability로서 model scale에 의존한다는 점에 착안하여 작은 모델에서의 heterogeneous path-pool 구성과 stopping의 필요성을 다룬다.

## 11. 현재 우선순위와 다음 액션

- 현재 우선순위: `P0`
- 위협도: 낮음 (origin baseline이라 직접 위협이 아니라 **claim 정의·baseline 고정** 측면에서 중요)
- 지금 당장 해야 할 일:
  - few-shot CoT(greedy)를 모든 path-family 비교의 **origin baseline**으로 고정
  - `CG`는 CoT replacement가 아니라 auxiliary/structured family로 명시(`CG > CoT` 금지 wording 가드)
  - prompt-diversity 이득과 structural 이득을 분리하는 ablation 설계
  - SLM scale에서 단일 CoT 한계를 보이는 곡선 확보(heterogeneous pool 동기화)
- 나중으로 미뤄도 되는 일:
  - CoT의 commonsense/symbolic benchmark full sweep(우리 mainline은 math)
  - 대형 모델 emergent-scale 재현
- 한 문장 결론:
  - CoT는 우리가 개선하거나 이기려는 대상이 아니라, **모든 reasoning path family 비교의 origin baseline으로 고정하고, `CG > CoT` 류 주장을 절제하며 prompt-diversity와 structure를 분리하게 만드는 P0 anchor reference**다.
