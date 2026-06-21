# LEGACY CG-CENTRIC PAPERS

> **historical only — active source of truth가 아니다.** (2026-06-21 `archive/legacy-cg-phase/` 로 이동)
> 현재 운영은 top-level canonical 문서(`../../papers.yaml`, `../../READING-QUEUE-202606.md`, `../../RELATED-WORK-MATRIX.md`, `../../POSITIONING-NOTES.md`)만 본다.

이 문서는 **2026-01 전후 CG-centric phase의 historical record**를 보존하기 위한 문서다.

- 현재 canonical frame은 [CURRENT-FRAME-202606.md](../../CURRENT-FRAME-202606.md)다.
- legacy 자료는 현재 연구의 출발점과 배경을 보여 주는 기록으로 보존한다.
- 현재 연구에서는 `CG`를 predefined winner가 아니라 **여러 reasoning path family 중 하나**로 재위치시킨다.
- 아래 세 논문은 모두 canonical 11섹션 노트(`../../md/`)로 재작성되었고 원문 PDF는 `../../paper/`에 있다. 이 문서는 그 historical 배경 설명만 남긴다.

## 왜 따로 보존하는가

2025년~2026년 초반의 related-work 정리는 `CG distillation`, `structured rationale`, `instruction tuning` 쪽에 더 큰 비중을 두고 있었다. 이후 Axis 1/2와 2026-06 미팅을 거치며 메인 질문이 **heterogeneous reasoning path selection + test-time compute allocation + verifier/reranker** 쪽으로 이동했다.

그렇다고 해서 초기 문헌 정리를 지우면 안 된다. 초기 자료는 아래 역할을 한다.

- 왜 연구가 `CG`에서 출발했는지 설명한다.
- teacher rationale / distillation / curriculum에 대한 출발점을 복원해 준다.
- 현재 프레임에서 어떤 아이디어를 background로 내렸는지 보여 준다.

## 현재도 보존되어 있는 legacy 장문 자료

아래 파일들은 단순 메타데이터 압축본이 아니라, 비교적 긴 요약과 해설을 유지하고 있다.

> 링크는 canonical 산출물(`../../paper/`, `../../md/`)을 가리킨다. 옛 추출 텍스트(`contents/`)와 중간 요약(`summary/`)은 2026-06-21 단순화에서 삭제되었고, 문장단위 reading 노트는 `../legacy-reading-pipeline-2026-01/reading/` 에 historical-only로 남아 있다.

### Self-Instruct

- canonical PDF: [../../paper/2023-self-instruct.pdf](../../paper/2023-self-instruct.pdf)
- canonical note: [../../md/2023-self-instruct.md](../../md/2023-self-instruct.md)
- legacy reading 노트(historical): `../legacy-reading-pipeline-2026-01/reading/01. (ACL23) Self-Instruct; ....md`
- 당시 의미: self-generated instruction, synthetic data bootstrapping, instruction diversity를 보는 출발점이었다.
- 현재 위치: 메인 novelty 문헌이 아니라 **training/data background**다.

### Distilling Step-by-Step!

- canonical PDF: [../../paper/2023-distilling-step-by-step.pdf](../../paper/2023-distilling-step-by-step.pdf) (published Findings-ACL 버전은 `../legacy-paper-filenames/02. ....pdf` 에 보존)
- canonical note: [../../md/2023-distilling-step-by-step.md](../../md/2023-distilling-step-by-step.md)
- legacy reading 노트(historical): `../legacy-reading-pipeline-2026-01/reading/02. (ACL23) Distilling Step-by-Step! ....md`
- 당시 의미: rationale distillation이 SLM reasoning을 밀어 올릴 수 있다는 가장 직접적인 근거였다.
- 현재 위치: path selection보다 **distillation background**에 가깝다.

### Phased Instruction Fine-Tuning

- canonical PDF: [../../paper/2024-phased-instruction-ft.pdf](../../paper/2024-phased-instruction-ft.pdf)
- canonical note: [../../md/2024-phased-instruction-ft.md](../../md/2024-phased-instruction-ft.md)
- legacy reading 노트(historical): `../legacy-reading-pipeline-2026-01/reading/03. (ACL24) Phased Instruction Fine-Tuning ....md`
- 당시 의미: difficulty-aware curriculum, staged uptraining, progressive alignment를 정당화하는 문헌이었다.
- 현재 위치: 메인 math TTC 논문이라기보다 **curriculum-style training background**다.

## 현재 프레임에서 이 세 논문을 어떻게 읽어야 하는가

- `Self-Instruct`:
  synthetic instruction generation의 역사적 배경으로 읽는다.
- `Distilling Step-by-Step!`:
  structured rationale supervision의 대표적 선행연구로 읽는다.
- `Phased Instruction Fine-Tuning`:
  curriculum / staged uptraining의 참고문헌으로 읽는다.

즉, 세 논문 모두 **지워야 할 옛 자료**가 아니라, 현재 프레임에서 `training-side background`로 재분류해야 할 자료다.

## 현재 canonical reading order와의 관계

현재 우선순위는 legacy 문헌이 아니라 아래 순서다.

1. `Self-Consistency / TTC / adaptive compute`
2. `math frontier`
3. `strategy selection / routing`
4. `verifier / PRM`
5. `selective NFM bridge`

legacy CG-centric 자료는 이 주축을 보조하는 historical layer로 유지한다.
