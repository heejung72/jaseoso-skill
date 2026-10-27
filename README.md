# jasoseo-skill

채용공고/JD, 자소서 문항, 글자수 제한, 초안을 붙여넣으면 **기업 제출용 자기소개서**로 다듬는 Claude Code 스킬입니다.

## 특징

- **보존형 첨삭 기본** — 사용자의 핵심 경험과 어필 포인트를 먼저 잠그고 문장/구조를 개선
- **문항 중심** — 멋진 문장보다 문항에 정확히 답하는 구조 우선
- **사실 보존** — 없는 경험, 수치, 기술을 만들지 않음
- **JD 과적합 방지** — 키워드 나열이 아닌 실제 경험과의 연결

## 설치

```bash
git clone https://github.com/YOUR_USERNAME/jasoseo-skill.git
```

### Claude Code에서 사용

프로젝트 디렉토리에서 Claude Code를 열면 자동으로 스킬을 인식합니다.

또는 전역 설치:
```bash
cp -r skills/jasoseo ~/.claude/commands/
```

## 사용법

Claude Code에서 아래처럼 붙여넣으면 됩니다:

```text
자소서 수정해줘.

채용공고/JD:
[채용공고 복붙]

자소서 문항:
[문항 복붙]

글자수:
700자 이내, 공백 포함

초안:
[내 초안]
```

## 출력 예시

```text
[최종 제출본]

글자수: 684/700자 (기준: 공백 포함)

살린 핵심:
- 팀 프로젝트에서 일정 지연을 줄인 경험
- 역할별 체크리스트를 만든 본인의 행동

수정 요약:
- 문항을 직무역량형으로 판단해 경험 중심으로 재구성
- "성장하겠습니다" 같은 클리셰 제거
```

## 3가지 모드

| 모드 | 사용법 | 동작 |
|---|---|---|
| 진단만 | "분석만 해줘" | 문제점과 개선 방향 제시 |
| 보존형 첨삭 (기본) | "수정해줘", "다듬어줘" | 핵심 유지하며 개선 |
| 재작성 | "아예 새로 써줘" | 구조부터 재구성 |

## 프로젝트 구조

```
jasoseo-skill/
├── plugin.json
├── skills/jasoseo/
│   ├── SKILL.md                    ← 스킬 본체
│   └── references/
│       ├── intake-schema.md        ← 입력 파싱
│       ├── jd-parser-rules.md      ← JD 추출
│       ├── question-taxonomy.md    ← 문항 분류
│       ├── writing-rules.md        ← 작성 원칙
│       ├── diagnosis-taxonomy.md   ← 진단 체계
│       ├── naturalness-rules.md    ← 자연화 규칙
│       ├── rewrite-playbook.md     ← 재작성 전략
│       └── audit-checklist.md      ← 검증 체크리스트
└── scripts/
    └── count_korean_length.py      ← 글자수 측정
```

## 라이선스

MIT
