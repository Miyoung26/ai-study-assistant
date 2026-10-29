# 나의 학습시간 AI 비서

시계열 학습시간 데이터를 Firebase Firestore에 저장하고 분석한 뒤, 데이터 요약 정보를 AI 시스템 지시문에 주입하여 사용자별 맞춤 답변을 제공하는 웹 서비스입니다.

120일간의 학습시간 데이터를 기준으로 평균, 최대, 최소, 합계와 최근 학습 추세를 계산합니다. 사용자는 자연어로 학습 기록에 관해 질문할 수 있으며, AI는 저장된 데이터 요약을 바탕으로 답변합니다.

---

## 배포 URL

- 프론트엔드: https://ai-study-assistant-frontend-rho.vercel.app
- 백엔드 API: https://ai-study-assistant-si1b.onrender.com
- Swagger API 문서: https://ai-study-assistant-si1b.onrender.com/docs
- 백엔드 상태 확인: https://ai-study-assistant-si1b.onrender.com/health

> Render 무료 인스턴스는 일정 시간 사용하지 않으면 대기 상태로 전환될 수 있습니다. 첫 접속 시 서버가 시작될 때까지 약간의 시간이 걸릴 수 있습니다.

---

## 서비스 주요 기능

### 1. 학습 데이터 관리

사용자는 날짜, 학습시간, 메모를 입력하여 학습 기록을 저장할 수 있습니다.

지원 기능:

- 학습 기록 추가
- 전체 학습 기록 조회
- 학습 기록 수정
- 학습 기록 삭제
- 데이터 목록 자동 갱신

학습시간은 분 단위로 저장합니다.

### 2. 학습 데이터 요약

Firestore에 저장된 학습 데이터를 분석하여 다음 정보를 제공합니다.

- 데이터 기간
- 전체 데이터 개수
- 총 학습시간
- 평균 학습시간
- 최대 학습시간
- 최소 학습시간
- 최근 7개 기록과 이전 7개 기록의 변화율
- 최근 학습 추세: 증가, 감소 또는 유지

현재 샘플 데이터는 총 120개이며, 과제 시연을 위해 생성한 합성 데이터입니다.

### 3. 데이터 기반 AI 채팅

사용자가 학습 데이터에 관해 질문하면 다음 순서로 처리됩니다.

1. Firestore에서 학습 데이터를 조회합니다.
2. 데이터 요약 API가 평균, 최대, 최소와 최근 추세를 계산합니다.
3. 계산된 요약 정보를 AI 시스템 지시문에 삽입합니다.
4. OpenAI API가 사용자 데이터에 근거한 답변을 생성합니다.
5. 사용자 질문과 AI 답변을 Firestore에 자동 저장합니다.

질문 예시:

- 최근 학습시간 추세를 알려줘.
- 평균 학습시간은 몇 분이야?
- 학습시간이 가장 길었던 기록을 알려줘.
- 최근 학습 기록을 바탕으로 학습계획을 추천해줘.

### 4. 대화 기록 관리

- AI 대화 자동 저장
- 저장된 대화 목록 조회
- 특정 대화 불러오기
- 이전 질문과 답변 재표시
- 대화 기록 삭제

### 5. API 문서

FastAPI가 자동으로 생성하는 Swagger UI에서 전체 API를 확인하고 직접 테스트할 수 있습니다.

- 로컬: http://localhost:8000/docs
- 배포: https://ai-study-assistant-si1b.onrender.com/docs

---

## 기술 스택

### Backend

- Python 3.10 이상
- FastAPI
- Uvicorn
- Pydantic
- Firebase Admin SDK
- OpenAI API
- python-dotenv

### Frontend

- HTML
- CSS
- JavaScript
- 프레임워크를 사용하지 않은 바닐라 JavaScript

### Database

- Firebase Cloud Firestore

### Deployment

- Backend: Render
- Frontend: Vercel
- Source Code: GitHub

---

## 프로젝트 구조

```text
ai-study-assistant
├─ backend
│  ├─ app
│  │  ├─ models
│  │  │  └─ schemas.py
│  │  ├─ routers
│  │  │  ├─ chat.py
│  │  │  ├─ conversations.py
│  │  │  └─ data.py
│  │  ├─ services
│  │  │  ├─ ai_service.py
│  │  │  ├─ conversation_service.py
│  │  │  └─ data_service.py
│  │  ├─ config.py
│  │  └─ database.py
│  ├─ .env.example
│  ├─ .gitignore
│  ├─ main.py
│  ├─ requirements.txt
│  └─ seed_data.py
│
├─ frontend
│  ├─ scripts
│  │  └─ build.js
│  ├─ app.js
│  ├─ config.js
│  ├─ config.template.js
│  ├─ index.html
│  ├─ package.json
│  ├─ style.css
│  └─ vercel.json
│
├─ 01_데이터요약_AI채팅_CRUD.png
├─ 02_대화기록_불러오기.png
├─ 03_Swagger_API문서.png
├─ 04_배포서비스_AI채팅.png
├─ README.md
└─ 초보자_진행가이드.md
```

### 디렉터리 역할

- `backend/app/routers`: API 주소와 요청 및 응답 처리
- `backend/app/services`: 데이터 분석, AI 호출, 대화 저장 업무 로직
- `backend/app/models`: Pydantic 요청 데이터 검증 모델
- `backend/app/config.py`: 환경변수 불러오기
- `backend/app/database.py`: Firebase Firestore 연결
- `frontend`: 사용자 화면과 API 호출 처리

---

## 로컬 실행 방법

### 1. 백엔드 폴더로 이동

```powershell
cd backend
```

### 2. Python 가상환경 생성

```powershell
python -m venv .venv
```

### 3. 가상환경 활성화

Windows PowerShell:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\Activate.ps1
```

Windows 명령 프롬프트:

```cmd
.venv\Scripts\activate.bat
```

macOS 또는 Linux:

```bash
source .venv/bin/activate
```

가상환경이 활성화되면 터미널 앞에 `(.venv)`가 표시됩니다.

### 4. 필수 패키지 설치

```powershell
python -m pip install -r requirements.txt
```

공식 PyPI 연결이 느린 환경에서는 다음과 같이 미러 서버를 사용할 수 있습니다.

```powershell
python -m pip install fastapi uvicorn firebase-admin openai python-dotenv pydantic --index-url https://mirror.kakao.com/pypi/simple/
```

### 5. 환경변수 파일 생성

`backend/.env.example` 파일을 복사하여 `backend/.env` 파일을 만듭니다.

```text
.env.example → .env
```

`.env` 안에 실제 환경변수 값을 입력합니다.

### 6. 샘플 데이터 생성

Firestore가 비어 있을 때 다음 명령을 한 번만 실행합니다.

```powershell
python seed_data.py
```

정상 결과:

```text
120개 샘플 데이터 저장 완료
```

> 이 명령을 여러 번 실행하면 샘플 데이터가 중복될 수 있으므로 한 번만 실행합니다.

### 7. 백엔드 실행

```powershell
uvicorn main:app --reload
```

백엔드 주소:

```text
http://localhost:8000
```

상태 확인:

```text
http://localhost:8000/health
```

Swagger 문서:

```text
http://localhost:8000/docs
```

### 8. 프론트엔드 실행

새 터미널에서 프론트엔드 폴더로 이동합니다.

```powershell
cd frontend
```

프론트엔드 서버를 실행합니다.

```powershell
python -m http.server 5500
```

브라우저에서 다음 주소를 엽니다.

```text
http://localhost:5500
```

로컬 실행 시 `frontend/config.js`는 다음 주소를 사용합니다.

```javascript
window.APP_CONFIG = { API_BASE_URL: "http://localhost:8000" };
```

---

## 환경변수

`backend/.env` 파일에 다음 환경변수를 설정합니다.

```dotenv
OPENAI_API_KEY=실제_OpenAI_API_키
OPENAI_MODEL=gpt-4.1-mini
FIREBASE_SERVICE_ACCOUNT_JSON=Firebase_서비스_계정_JSON_전체
ALLOWED_ORIGINS=http://localhost:5500,https://ai-study-assistant-frontend-rho.vercel.app
```

### 환경변수 설명

- `OPENAI_API_KEY`: OpenAI API 호출에 사용하는 비밀키
- `OPENAI_MODEL`: AI 답변 생성에 사용할 모델
- `FIREBASE_SERVICE_ACCOUNT_JSON`: Firebase 서비스 계정 JSON 전체 내용
- `ALLOWED_ORIGINS`: 백엔드 요청을 허용할 프론트엔드 주소 목록

### 보안 주의사항

다음 정보는 GitHub에 업로드하지 않습니다.

- `.env`
- OpenAI API 키
- Firebase 서비스 계정 JSON 파일
- Firebase 비공개 키

`.gitignore`에서 해당 파일이 제외되는지 확인합니다.

```powershell
git check-ignore -v backend/.env
```

---

## API 목록

### 데이터 API

#### 데이터 추가

```http
POST /api/data
```

요청 예시:

```json
{
  "date": "2026-10-29",
  "value": 90,
  "memo": "AI 응용 학습"
}
```

#### 데이터 목록 조회

```http
GET /api/data
```

#### 데이터 수정

```http
PUT /api/data/{doc_id}
```

#### 데이터 삭제

```http
DELETE /api/data/{doc_id}
```

#### 데이터 요약 조회

```http
GET /api/data/summary
```

응답 예시:

```json
{
  "period": "2026-07-02 ~ 2026-10-29",
  "count": 120,
  "metrics": {
    "total": 6242,
    "average": 52,
    "max": 88,
    "min": 16
  },
  "trend": "증가 (최근 7개 vs 이전 7개: +12.6%)",
  "unit": "분"
}
```

### AI 채팅 API

```http
POST /api/chat
```

요청 예시:

```json
{
  "message": "최근 학습시간 추세를 알려줘",
  "conversation_id": null,
  "messages": []
}
```

AI 채팅 API는 다음 작업을 순서대로 수행합니다.

1. 데이터 요약 조회
2. 요약 정보를 AI 시스템 지시문에 삽입
3. OpenAI API 호출
4. AI 답변 반환
5. 질문과 답변을 Firestore에 자동 저장

### 대화 기록 API

#### 대화 저장

```http
POST /api/conversations
```

#### 대화 목록 조회

```http
GET /api/conversations
```

#### 특정 대화 불러오기

```http
GET /api/conversations/{doc_id}
```

#### 대화 삭제

```http
DELETE /api/conversations/{doc_id}
```

---

## Firestore 컬렉션 구조

### `data`

학습시간 데이터를 저장합니다.

```json
{
  "date": "2026-10-29",
  "value": 90,
  "memo": "AI 응용 학습"
}
```

### `conversations`

사용자 질문과 AI 답변을 저장합니다.

```json
{
  "title": "최근 학습시간 추세를 알려줘",
  "messages": [
    {
      "role": "user",
      "content": "최근 학습시간 추세를 알려줘"
    },
    {
      "role": "assistant",
      "content": "최근 학습시간은 증가하는 추세입니다."
    }
  ],
  "created_at": "저장 시간",
  "updated_at": "수정 시간"
}
```

---

## 데이터 분석 기준

전체 데이터에서 다음 기본 통계를 계산합니다.

- 전체 데이터 개수
- 학습시간 합계
- 평균 학습시간
- 최대 학습시간
- 최소 학습시간

최근 추세는 다음 두 구간의 평균을 비교해 계산합니다.

```text
최근 7개 데이터 평균
        비교
이전 7개 데이터 평균
```

판정 기준:

- 변화율이 `+5%`보다 크면 증가
- 변화율이 `-5%`보다 작으면 감소
- 그 사이는 유지

---

## 컨텍스트 주입 방식

일반적인 AI는 사용자의 Firestore 데이터를 직접 알 수 없습니다.

이 프로젝트에서는 데이터 요약 결과를 다음과 같은 방식으로 AI 시스템 지시문에 삽입합니다.

```text
당신은 사용자의 학습시간 데이터를 분석하는 AI 비서입니다.

[사용자 데이터 요약]
- 데이터 기간
- 데이터 개수
- 평균 학습시간
- 최대 및 최소 학습시간
- 최근 학습 추세

위 데이터에 근거해 답변하세요.
```

따라서 AI는 일반적인 답변이 아니라 저장된 학습 데이터에 근거한 맞춤 답변을 생성할 수 있습니다.

---

## 배포 방법

### Render 백엔드 배포

설정값:

```text
Root Directory: backend
Build Command: pip install -r requirements.txt
Start Command: uvicorn main:app --host 0.0.0.0 --port $PORT
```

Render 환경변수:

```text
OPENAI_API_KEY
OPENAI_MODEL
FIREBASE_SERVICE_ACCOUNT_JSON
ALLOWED_ORIGINS
```

### Vercel 프론트엔드 배포

설정값:

```text
Root Directory