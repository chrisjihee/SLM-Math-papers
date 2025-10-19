KoGSM: 한국어 초등학교 수학추론 벤치마크

허정O, 임수종O, 장지현1, 이숙의1, 권오욱O

O한국전자통신연구원 언어지능연구실, 1㈜마인즈솔루션

{jeonghur, isj}@etri.re.kr, jidoli8@naver.com, jayou3830@gmail.com, ohwoog@etri.re.kr

KoGSM: Math Reasoning Benchmark for Korean Grade School Math Jeong HeoO, Soo-Jong LimO, Ji-Hyun Jang1, Suk-Eui Lee1, Oh-Woog KwonO OElectronics and Telecommunications Research Institute, 1Minds Solution

요  약

본 논문에서는 한국의 교육수준과 환경에 맞는 수학문제추론 벤치마크인 KoGSM에 대해서 소개 한다. 자동번역 후 번역검수한 한국어 GSM8k 데이터와 비교 실험을 수행하였고, KoGSM 벤치마 크가 문제의 다양성과 난이도가 높은 것을 확인하였다. 그리고, Mistral-7B와 Llama3-8B 모델에 기반하여 한국어 MetaMathQA 데이터와 KoGSM 데이터의 다양한 조합에 따른 학습 모델군을 비 교평가 하였고, Llama3-8B에 기반한 모델군이 성능이 우수함을 확인하였다.

서  론

초거대 언어모델의 발전으로 인공지능에 대한 기대와 함께 초거대 언어모델이 논리적 추론이 가능하지, 아니면 단지 패턴에 따른 결과 생성인지에 대한 논란이 있다[1]. 이와 같은 의문을 해소하기 위해, 언어이해 능력과 수리적 논리추론이 요구되는 수학문제추론(math word problem) 태스크에 대한 관심이 늘어나면서, 다양한 수학문제추론 벤치마크가 구축되어 초거대 언어모델의 능력을 평가하고 있다. 그러나, 한국어로 된 수학문제추론 벤치마크는 아직 존재하지 않고, 단지 영어로 구성된 GSM8k[2], MATH[3] 벤치마크 등을 자동 번역하여 벤치마크로 사용하고 있다. 이렇게 자동 번역된 데이터는 번역오류와 함께 문화적 차이(수치단위, 문화적 상식 등)가 존재하여 한국어 초거대 언어모델에 대한 수학문제추론 평가에 한계가 있다. 본 논문에서는 언급된 문제를 해결하기 위해 국내 초등학교 5학년~6학년 학습수준의 수학문제추론 벤치마크인 KoGSM(Korean Grade School Math) 벤치마크를 소개한다. KoGSM 벤치마크는 상용 초거대 언어모델로부터 지식증류한 합성데이터이다. 그리고, KoGSM과 MetaMathQA 데이터를 이용하여 Mistral-7B와 Llama3-8B 모델을 학습하고 평가한 결과, GSM8k 보다 KoGSM 데이터의 문제  난이도가 높은 것을  확인하였다.  또한  전반적인

성능이 낮아서 초거대언어모델과 달리 소형언어모델은 아직 수학문제추론에 한계가 있고, 많은 연구가 진행되어야 함을 확인하는 결과이다.

관련연구

GSM8k[2]는 초등학교 수준의 수학문제 벤치마크이다. 작업자가 기본산술연산 (덧셈, 뺄셈, 곱셈, 나눗셈)을 사용하여 최종적인 답에 도달할 수 있는 문제와 단계별 추론 솔루션을 구축한 벤치마크로 8.5개 train데이터와 1k의 test데이터로 구성되어 있다. 최근 GSM8k 데이터들이 초거대 언어모델의 사전학습 데이터에 포함되어 데이터오염 문제가 있다는 의구심으로 인해 평가에 대한 신뢰도 문제가 있다.

MATH[3]는 도전적인 수학경시대회 문제(competition mathematics problems) 12.5k로 구성된 벤치마크이다. MATH는 각 문제에 대해서 모델이 정답을 도출하기 위해 필요한 풀이과정의 설명을 가르치도록 단계별 솔루션을 제공하고 있다.

MetaMathQA[4] 데이터셋은 질문을 세가지 방식의 부트스트래핑 방법으로 확장하고, 정답 솔루션을 증강하는 방식으로 GSM8k와 MATH 데이터를 증강하여 395k로 구성한 수학문제추론 데이터 셋이다.

앞서 언급된 데이터들은 영어로 된 수학문제 데이터로

영어권의 수치단위나 상식이 포함된 경우가 많아 한국어 언어모델의 평가에는 부적절하다.

KoGSM 벤치마크

KoGSM 벤치마크는 다음의 프로세스를 통해 구축된다.

위의 프로세스와 같이 N차 반복 프롬프팅을 통해 초거대언어모델로부터 KoGSM 벤치마크를 구축하였다. 벤치마크 구축에 사용된 초거대언어모델은 ChatGPT4o, Claude3.5 sonnet, Gemini, Gemini_adv이다. 구축된 데이터는 총 50,156개로 Train 데이터와 Test 데이터를 9:1의 비율로 구성하였다. KoGSM 벤치마크의 통계정보는 표 1과 표 2와 같다.

표 1. Grade(학년-학기) 별 train과 text 데이터 구성비

표 2. 생성 LLM 별 train과 text 데이터 구성비

수학문제추론모델 학습과 평가 방법

본 논문에서는 KoGSM 벤치마크의 수학문제를 해결하기 위해서 베이스모델로 Mistral-7B와 Llama3-8B 모델에 기반한 6개의 모델을 학습하였다. 모델학습을 위한 학습데이터는 KoGSM 데이터와 한국어 MetaMathQA 데이터를 이용하였다. 한국어 MetaMathQA

데이터는 DeepL 자동번역 도구를 이용한 데이터로 번역오류를 포함하고 있다. 모델은 아래와 같이 학습에 사용된 데이터의 조합에 따라 구분하였다.

Mistral_MetaMath:	Mistral-7B에	한국어

MetaMathQA 데이터로 미세조정한 모델

Mistral_KoGSM: Mistral-7B에 KoGSM 데이터로 미세조정한 모델

Mistral_AllMath: Mistral-7B에 한국어 KoGSM와 MetaMathQA 데이터로 미제조정한 모델

Llama_MetaMath:	Llama3-8B에	한국어

MetaMathQA 데이터로 미세조정한 모델

Llama_KoGSM: Llama3-8B에 KoGSM 데이터로 미세조정한 모델

Llama_AllMath: Llama3-8B에 한국어 KoGSM와 MetaMathQA 데이터로 미제조정한 모델

학습은 LoRA 어댑터를 이용 1 하였다. 평가는 lm- evaluation-harness를 이용하였고, 평가데이터는 한국어 GSM8k 데이터와 KoGSM test 데이터 2 를 이용하였다. 한국어 GSM8k 데이터는 DeepL을 통해 자동번역된 데이터에 대해서 번역검수를 통해 오류를 수정하였다. 특히, 수치단위와 문화적 상식에 따른 차이는 한국의 수치단위와 문화적 상식으로 수정하였다.

실험결과 및 분석

추론평가는 5-shot과 8-shot CoT에 대해서 수행하였다. 표 3은 전체 실험결과이다. 정답만을 생성하는 5-shot 실험에서는 GSM8k와 KoGSM의 성능이 매우 낮았다. 이는	단순히	소형언어모델에서는	5개의 예제(examples)만을 제시하는 ICL(In-Context Learning)로 논리적인 추론이 필요한 수학문제 추론에는 한계가 있음을 확인할 수 있다. 반면, 생각의 사슬(chain- of-thought)을 생성하면서 수학적 논리추론을 할 수 있도록 CoT 프롬프트를 적용하였을 때, 성능이 크게 개선되었다. GSM8k에서는 LlamaAllMath 모델이 0.5221의 성능을 보여, MistralAllMath 모델의 0.4511보다 0.0710만큼 높고, KoGSM에서는 LlamaAllMath 모델이 0.3120이고, MistralAllMath 모델의  0.2680보다  0.0440만큼  높다.  Base모델로

1 학습 파라미터: epoch 5, lr 2e-4, weight-decay 0.01, warmup_ratio 0.03, lr-scheduler linear, peft-lora-r 256, peft-lora-alpha 128, target_module [q_proj, k_proj, v_proj, o_proj, gate_proj]

2 본 논문의 평가에서는 5,014개 중, 랜덤으로 1,000를 선정하여 평가하였음.

Mistral-7B모델보다는	Llama3-8B	모델	성능이 전반적으로 우수하였다.

표 3. 수학문제추론 모델들에 대한 성능 실험

(평가 Metric은 flexible em이고, CoT는 8-shot CoT임)

45k 데이터를 학습한 KoGSM 모델이 395k 데이터를 학습한 MetaMath 모델과 비교하여 데이터 크기에 비해

표 4. KoGSM 평가데이터의 정답유형별 성능

표 5. KoGSM 평가데이터의 Grade 별 성능

결론

본 논문에서는 한국어 교육환경에 맞는 수학문제추론 벤치마크인 KoGSM에 대해서 소개하였다. 그리고, 한국어 GSM8k 데이터와 비교 실험을 수행하였고, KoGSM 벤치마크가 문제의 난이도가 높은 것을 확인하였다. 그리고,  Mistral-7B와  Llama3-8B  모델에  기반하여

일정한 성능수준을 보였다. 또한 CoT의 경우, KoGSM 데이터와 MetaMath 데이터를 함께 학습한 경우, GSM8k와 KoGSM 평가 대부분에서 성능이 개선됨을 확인하였다. 단, LlamaMetaMath 모델이 LlamaAllMath모델보다 0.012 만큼 성능이 우수하였다.

GSM8k CoT 평가의 경우, 최고성능이 0.5221 (LlamaAllMath 모델)이고, KoGSM의 경우, 최고성능이 0.3240(LlamaMetaMath 모델)로 성능차이가 크다. 이는 GSM8k 데이터의 경우, 정답유형으로 정수가 대부분이지만, KoGSM 데이터는 분수, 소수, 비율도 포함되어 있다. 그림 1과 표 4는 KoGSM 정답유형의 분포와 정답유형별 성능을 분석한 결과이다. 정답유형별 성능을 보면, 분수와 비율에 대한 문제의 경우 성능이 낮다. 그리고, 표 5의 Grade 별 성능분석에서는 고학년 문제일수록 학습된 모델의 성능이 낮아지는 것을 확인할 수 있다. 보다 고차원적인 논리적 추론을 요구하는 질문일수록 추론에 어려움을 겪는 것이다.

그림 1. KoGSM 평가데이터의 정답유형 분포

한국어 MetaMathQA 데이터와 KoGSM 데이터의 다양한

조합에 따른 학습 모델을 비교평가 하였고, Llama3-8B에 기반한 모델군이 성능이 우수함을 확인하였다. 앞으로 KoGSM 데이터를 중학교 저학년 수학문제까지 포함할 수 있도록 확장하여 구축할 것이고, 그림과 함께 제시되는 수학문제를 위한 멀티모달 수학문제추론 벤치마크로 확장할 것이다.

감사의 글

이 논문은 2024년도 정부(과학기술정보통신부)의 재원으로 정보통신기획평가원의 지원을 받아 수행된 연구임 (RS-2023-00216011, 사람처럼 개념적으로 이해/추론이 가능한 복합인공 지능 원천기술 연구)

참고문헌

Iman Mirzadeh, et, al. “GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models”, arXiv preprint arXiv:2410.05229v1, 2024.

K. Cobbe, et, al. “Training verifiers to solve math word problems”, arXiv preprint arXiv:2110.14168, 2021

Dan Hendrycks, et, al. “Measuring mathematical problem solving with the math dataset.”, arXiv preprint arXiv:2103.03874, 2021.

Longhui Yu, et, al. “MetaMath: Bootstrap your own mathematical questions for large language models.” ,arXiv preprint arXiv:2309.12284, 2023.
