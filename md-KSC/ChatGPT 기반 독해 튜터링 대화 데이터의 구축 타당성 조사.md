# ChatGPT 기반 독해 튜터링 대화 데이터의 구축 타당성 조사

---

ChatGPT 기반 독해 튜터링 대화 데이터의 구축 타당성 조사

최승권 O1, 전예림 2, 황금하 1 권오욱 1

1 한국전자통신연구원, 2 순천향대학교 AI 빅데이터학과 학부생

choisk@etri.re.kr, 9261190@sch.ac.kr, hgh@etri.re.kr, ohwoog@etri.re.kr

## Feasibility Study on Constructing Reading Comprehension Tutoring Dialogue Data based on ChatGPT

Sung-Kwon ChoiO1, Ye-Lim Jeon2, Jin-Xia Huang1, Oh-Woog Kwon1

1Language Intelligent Research Section, ETRI, 2Dept. of AI Big Data, Soon Chun Hyang University

# 요  약

본 논문에서는 ChatGPT를 이용하여 독해 튜터링 대화 데이터를 구축하고 학습용 데이터로 활용하는 것이 타당한 지에 대한 타당성 조사를 목표로 한다. 이를 위해 수동으로 구축한 독해 튜터링 대화 데이 터 5,708개 지문 중 임의로 50개 지문을 추출한 후, zero-shot과 few-shot prompting, chatgpt-3.5- turbo와 chatgpt-4.0 엔진의 조합으로 대화 데이터를 자동 구축하고 수동 구축 대화 데이터와 비교 평가 하였다. 자동 평가는 코사인 유사도(cosine similarity), TF-IDF, Sentence Transformer를 이용하였다. 코 사인 유사도는 문장 간의 유사도를 고려한 것이며 TF-IDF는 문단(Paragraph) 간의 유사도를 고려한 것 이며 Sentence Transformer는 대화 간의 의미적 유사도를 고려한 것이다. 그 결과 문단 간의 유사도를 위한 TF-IDF와 대화 간의 의미적 유사도를 위한 Sentence Transformer 비교에 따르면 few-shot prompting과 gpt-4.0 엔진의 조합이 수동 구축과 가장 유사한 것으로 측정되었다. 따라서 독해 지문과 연습문제가 주어졌을 때, gpt-4.0 엔진에서 few-shot prompting을 이용하여 독해 튜터링 대화 코퍼스를 자동으로 구축하여 학습용으로 활용하는 것이 유의미하다는 것을 알 수 있다.

# 서  론

인공지능 기술의 발전과 더불어 학습자가 영어 지문(passage)을 얼마나 정확하게 독해하는 지를 평가하는 딥러닝 기반 독해 시스템이 개발되고 있다. 그 중에서도 읽기/말하기를 동시에 교육하려는 대화기반 영어 독해 튜터링 시스템이 최근에 개발되었다.[1] 대화기반 영어 독해 튜터링 시스템에서 대화 학습은 Tutor 질문, Student 대답으로 구성된 대화 데이터인 ‘DIRECT 데이터셋’으로 학습되었다. 이 DIRECT 데이터셋은 수동으로만 구축되었기 때문에 학습 데이터로써 높은 품질을 가지지만 비싼 구축 비용, 적은 데이터양, 긴 구축기간이 해결해🅓 할 문제였다.

본 논문에서는 ChatGPT를 이용하여 독해 튜터링 대화 데이터를 자동으로 구축하여 학습 데이터로 활용하고자 할 때, 수동으로 구축한 DIRECT 데이터셋 과 비교하여 얼마나 유사한 지, 어떤 Prompting 방식이 적절한 지에 대한 타당성 검증을 목표로 한다.1

1 이 논문은 2019년도 정부(과학기술정보통신부)의 재원으로 정보통신기획평가원의 지원을 받아 수행된 연구임 (2019-0-00004, 준지도학습형 언어지능 원천기술 및 이에 기반한 외국인 지원용 한국어 튜터링

# 수동 구축된 독해 튜터링 대화 데이터

독해 튜터링 시스템을 위해 사용되는 독해 교육 데이터셋으로 RACE[2], DREAM[3], OpenBookQA[4] 등이 있다. 이 독해 교육 데이터셋은 사지선다형 연습문제의 읽기 중심의 데이터이며 대화 데이터는 아니다.

기존의 독해 교육 데이터와 달리 독해 튜터링 대화 데이터인 DIRECT 데이터셋은 독해 읽기/말하기 교육을 위한 대화 중심의 데이터이다. DIRECT 데이터셋은 학습자의 영어 지문 이해와 영어 대화 능력 향상을 목표로 RACE[2]의 중학교 버전을 토대로 구축되었다. 이	DIRECT	데이터셋은 텍스트로 된 읽기 지문과 연습문제가 주어지면, 대화 형 식으로 질문하고 사용자 응답을 입력 받아 의미적으로 정확한지 평가하며 정확하면 다음 연습문제에 대하여 질문하고 오답이면 한 번 더 응답할 수 있도록 피드백 을 출력하거나 정답을 알려주는		방식으로 구축되었다[1].

서비스 개발)

그림1. 수동 구축된 DIRECT 데이터셋의 구성

수동 구축된 DIRECT 데이터셋의 통계는 다음과 같다[1].

표1. 수동 구축된 DIRECT 데이터셋의 통계


| 분류 | Train | Dev | Test | Total |
| --- | --- | --- | --- | --- |
| 대화셋수 | 5,099 | 302 | 307 | 5,708 |
| Question턴 | 21,463 | 1,239 | 1,280 | 23,982 |
| Feedback턴 | 9,431 | 475 | 524 | 10,430 |
| Chat턴 | 10,481 | 582 | 625 | 11,688 |
| 전체 턴수 | 41,377 | 2,296 | 2,429 | 46,102 |
| 평균 턴수 | 8.11 | 7.60 | 7.91 | 8.08 |


DIRECT 데이터셋은 5,708개 지문을 대상으로 4명의 구축자가 3.5개월에 걸쳐 수동으로 구축하였다. 4명의 구축자는 오프라인 영어 교육 경험이 있는 인력으로 2명이 Tutor와 Student 역할을 하였으며 1개 지문은 평균 8.08개의 턴으로 이루어졌었다.

ChatGPT 기반 독해 튜터링 대화 데이터 구축 방법 기존의	수동으로	구축하는	방법과	ChatGPT를

활용하여 자동으로 구축하는 방법을 비교하면 다음의

프로세스와 같다.

그림2. ChatGPT 기반 독해 튜터링 대화 데이터 구축 프로세스

그림 2에서 중앙을 중심으로 왼쪽은 기존의 독해 튜터링 대화 데이터의 수동 구축 방식이며 오른쪽은 ChatGPT에 의한 자동 구축 방식이다. 기존의 방식은 3단계인 1) RACE 데이터와 같은 독해 교육용 데이터로부터 지문 및 문제 수집, 2) 영어 전문가에 의한 수동 대화 구축, 3) 영어 전문가에 의한 수동 검증 및 평가로 이루어졌는데 반해, ChatGPT를 이용한 방식은 4단계로 구성된다. 1) RACE 데이터와 같은 독해 교육용 데이터로부터 지문 및 문제 수집, 2) Prompt 구축, 3) ChatGPT에 의한 대화 데이터의 자동 구축, 4) 코사인 유사도(cosine similarity)와 같은 자동 평가이다.

# ChatGPT 기반 독해 튜터링 대화 데이터 구축 타당성 분석

Zero-Shot Prompt vs. Few-Shot Prompt 구축 ChatGPT를  이용하여  독해  튜터링  대화  데이터를

생성하기  위해  독해지문,  연습문제,  정답을  토대로

ChatGPT에 프롬프트를 입력하고 대화 생성 성능을 확인하며 최적의 prompt를 찾고자 하였다[5]. 그 결과 zero-shot prompting은 일관성 있는 대화 생성의 장점이 있었으며 few-shot prompting은 정확도가 높다는 장점이 있었다. few-shot prompt에는 zero-shot prompt에 tutor와 student 대화 예제를 추가하였다.

# 자동 대화 데이터 구축

zero-shot prompt와 few-shot prompt를 이용하여 독해 튜터링 대화 데이터를 자동으로 구축하였다. 사용한 API는 gpt-3.5-turbo와 gpt-4였다. 생성된 결과를 수동 구축 대화 데이터와 비교 분석하기 위해 50개의 수동 대화 데이터를 임의로 추출하였다.

표2. 수동 구축 대화 데이터 vs. ChatGPT에 의해 자동 구축된 50개의 대화 데이터 비교

표 2로부터 알 수 있는

것은 수동 구축된

전체턴

shot prompting과 gpt-4.0 엔진의 조합, few-shot prompting과 gpt-3.5 엔진의 조합의 순서로 품질이 좋았다. 또한 few-shot prompting과 gpt-4.0 엔진의 조합에 의해 생성된 대화턴은 독해지문, 연습문제, 정답을 모두 포함하고 있어서 교육적으로도 활용가치가

수(821개)와 ChatGPT에 의해 자동으로 구축된 전체턴 수는 prompting 방식이나 API의 종류에 따라 차이가 크게 나지 않았지만 전체 토큰수는 ChatGPT에 의해 자동으로 구축된 토큰수가 거의 2배에 달했다. 즉, ChatGPT가 더 많은 단어를 사용하여 대화를 생성하였다.

# 자동 평가

수동 구축 대화턴과 ChatGPT에 의해 자동 구축된 대화턴을 자동 평가하여 비교하였다. 자동 평가는 코사인 유사도(cosine similarity), TF-IDF, Sentence Transformer로 측정되었다. 코사인 유사도는 문장 간의 유사도를 고려한 것이며 TF-IDF는 문단(Paragraph) 간의 유사도를 고려한 것이며 Sentence Transformer는 대화 간의 의미적 유사도를 고려한 것이다.

표3. 수동 구축 대화 데이터 vs. ChatGPT에 의해 자동 구축된 50개의 대화 데이터의 유사도 비교


| 분류 | 측정식 | 수동구축 vs.
Zero-shot prompting | 수동구축 vs.
Zero-shot prompting | 수동구축	vs.
Few-shot prompting | 수동구축	vs.
Few-shot prompting |
| --- | --- | --- | --- | --- | --- |
| 분류 | 측정식 | gpt- 3.5 | gpt- 4.0 | gpt- 3.5 | gpt- 4.0 |
| #전체 턴평 균값 | Cosine similarity | 0.48 | 0.40 | 0.60 | 0.56 |
| #전체 턴평 균값 | TF-IDF | 0.43 | 0.47 | 0.44 | 0.49 |
| #전체 턴평 균값 | Sentence Transformer | 0.80 | 0.81 | 0.80 | 0.83 |
| #전체 턴최 대값 | Cosine similarity | 1.00 | 1.00 | 1.00 | 1.00 |
| #전체 턴최 대값 | TF-IDF | 0.66 | 0.71 | 0.67 | 0.76 |
| #전체 턴최 대값 | Sentence Transformer | 0.91 | 0.91 | 0.91 | 0.93 |
| #전체 턴최 소값 | Cosine similarity | -1.00 | -1.00 | -1.00 | -1.00 |
| #전체 턴최 소값 | TF-IDF | 0.26 | 0.24 | 0.27 | 0.25 |
| #전체 턴최 소값 | Sentence Transformer | 0.57 | 0.66 | 0.58 | 0.72 |


문단 간의 유사도를 위한 TF-IDF와 대화 간의 의미적 유사도를 위한 Sentence Transformer 비교에 따르면 few-shot prompting과 gpt-4.0 엔진의 조합이 수동 구축과 가장 유사한 것으로 측정되었으며, zero-

높았다.

# 결  론

대화기반 영어 독해 튜터링 시스템을 위한 학습용 데이터로 수동으로 구축된 대화 데이터를 사용하였으나 비싼 구축 비용, 적은 데이터양, 긴 구축기간이 해결해🅓 할 문제였다. 이런 점에서 본 논문에서는 ChatGPT를 이용하여 독해 튜터링 대화 데이터를 자동으로 구축하기 위해 ChatGPT 기반 독해 튜터링 대화 데이터 구축 프로세스를 수립하고 prompting 방식을 검증하고자 하였다. 자동 평가 결과 현재 시점에서는 few-shot prompting과 gpt-4.0 엔진의 조합으로 독해 튜터링 대화 데이터를 자동으로 구축하고 인간의 감수에 의한 학습 데이터 구축이 바람직하다는 것을 확인하였다.

# 참 고 문 헌

Huang, Jin-Xia, Yohan Lee, Oh-Woog Kwon, “DIRECT: Toward Dialogue-Based Reading Comprehension Tutoring”, in IEEE Access, Vol.11, 2023, pp.8978-8987. 2023.

Lai, G., Q. Xie, H. Liu, Y. Yang, and E. Hovy, “RACE: Large-scale ReAding comprehension dataset from examinations”, in Proc. Conf. Empirical Methods Natural Lang. Process, pp. 785-794. 2017.

Sun, K, D. Yu, J. Chen, D. Yu, Y. Choi, and C. Cardie, “DREAM: A challenge data set and models for dialogue-based reading comprehension”, in Trans. Assoc. Comput. Linguistics, vol. 7, pp.

217-231. 2019.

Todor Mihaylov, Peter Clark, Tushar Khot, and Ashish Sabharwal, “Can a suit of armor conduct electricity? a new dataset for open book question answering”. In Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing, pages 2381–2391, 2018.

전혜림, 황금하, 최승권, 조민수, “인공지능 튜터링 시스템을 위한 대화 기반 교육 데이터 구축 및 품질 평가”, 한국정보처리학회 ACK2023, 430-431, 2023.
