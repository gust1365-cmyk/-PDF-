# INTOPS 발주서 생성기 — EXE 빌더

## EXE 다운로드

1. 저장소 → **Actions 탭** 클릭
2. 가장 최근 **Build EXE** 클릭
3. 하단 **Artifacts** → `INTOPS_발주서생성기_Windows` 다운로드
4. 압축 해제 후 `INTOPS_발주서생성기.exe` 더블클릭 실행

## 파일 구조

```
intops-exe-builder/
├── .github/
│   └── workflows/
│       └── build.yml          ← Actions 자동빌드 (절대 위치 변경 금지)
├── app/
│   ├── main.py                ← PyWebView 래퍼
│   └── INTOPS_발주서생성기.html ← 앱 본체
├── requirements.txt
└── README.md
```

## GitHub에 올리는 방법

```bash
git init
git add .
git commit -m "init"
git remote add origin https://github.com/아이디/저장소명.git
git push -u origin main
```

push 즉시 Actions 자동 실행 → 약 3~5분 후 EXE 생성
