# 나의 학습시간 AI 비서

시계열 학습시간 데이터를 Firestore에 저장하고 요약한 뒤, 그 요약을 AI 시스템 지시문에 주입하여 맞춤 답변을 제공하는 웹 서비스입니다.

## 기술 스택

- Backend: Python, FastAPI, Pydantic, Firebase Admin SDK, OpenAI API
- Frontend: HTML, CSS, JavaScript
- DB: Firebase Firestore
- Deploy: Render(백엔드), Vercel(프론트)

## 주요 기능

1. 데이터 CRUD 및 요약 API
2. 요약 컨텍스트 기반 AI 채팅과 로딩 표시
3. 대화 자동 저장, 목록, 불러오기, 삭제
4. Swagger 문서 /docs

## 프로젝트 구조

- backend/app/routers: HTTP 경로
- backend/app/services: 데이터/AI 업무 로직
- backend/app/models: Pydantic 검증 모델
- frontend: 바닐라 웹 UI

## 로컬 실행

1. 백엔드 폴더로 이동: cd backend
2. 가상환경 생성: python -m venv .venv
3. 가상환경 활성화
   - Windows: .venv\Scripts\activate
   - macOS/Linux: source .venv/bin/activate
4. 패키지 설치: pip install -r requirements.txt
5. 환경변수 파일 준비: .env.example을 복사해 .env 생성 후 값 입력
6. 서버 실행: uvicorn main:app --reload
7. 프론트엔드는 frontend 폴더를 라이브 서버(5500포트 등)로 실행

## 환경변수 (.env)

- OPENAI_API_KEY: OpenAI API 키
- FIREBASE_CREDENTIALS: Firebase 서비스 계정 키 경로
- 그 외 프로젝트에 설정한 항목

## API 요약

- GET /records: 학습 기록 목록 조회
- POST /records: 학습 기록 생성
- PUT /records/{id}: 학습 기록 수정
- DELETE /records/{id}: 학습 기록 삭제
- GET /summary: 학습 데이터 요약
- POST /chat: 요약 컨텍스트 기반 AI 채팅
- GET /conversations: 대화 목록 조회
- DELETE /conversations/{id}: 대화 삭제

## 라이선스

학습용 프로젝트입니다.

