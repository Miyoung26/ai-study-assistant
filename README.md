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
4. Swagger 문서 `/docs`

## 프로젝트 구조
- `backend/app/routers`: HTTP 경로
- `backend/app/services`: 데이터/AI 업무 로직
- `backend/app/models`: Pydantic 검증 모델
- `frontend`: 바닐라 웹 UI

## 로컬 실행
```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # Windows는 복사 후 직접 편집
uvicorn main:app --reload
```
새 터미널에서:
```bash
cd frontend
python -m http.server 5500
```
브라우저에서 `http://localhost:5500`, API 문서는 `http://localhost:8000/docs`를 엽니다.

## 환경 변수
- `OPENAI_API_KEY`: OpenAI API 키
- `OPENAI_MODEL`: 사용할 모델명
- `FIREBASE_SERVICE_ACCOUNT_JSON`: 서비스 계정 JSON 전체를 한 줄 문자열로 저장
- `ALLOWED_ORIGINS`: 허용할 프론트 주소, 쉼표 구분
- `API_BASE_URL`: Vercel 빌드 시 사용할 Render 백엔드 주소

## 샘플 데이터
`.env` 설정 후 `backend` 폴더에서 `python seed_data.py`를 1회 실행합니다. 이 파일은 과제 시연용 합성 데이터 120개를 만듭니다. 실제 제출 설명에 합성 데이터임을 표시하세요.

## Render 배포
- Root Directory: `backend`
- Build Command: `pip install -r requirements.txt`
- Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
- 환경 변수 4개를 등록한 뒤 배포합니다.

## Vercel 배포
- Root Directory: `frontend`
- 환경 변수 `API_BASE_URL=https://내백엔드.onrender.com`
- 배포 후 생성된 Vercel URL을 Render의 `ALLOWED_ORIGINS`에 추가하고 재배포합니다.

## 배포 URL(제출 전 입력)
- 프론트: TODO
- 백엔드: TODO
- Swagger: TODO/docs

## 제출 스크린샷
1. 데이터 요약과 질문/답변이 함께 보이는 채팅 화면
2. 데이터를 추가 또는 삭제한 뒤 목록이 바뀐 화면
3. 이전 대화를 눌러 메시지를 불러온 화면
4. Render의 `/docs` 화면

## 핵심 설명
- 데이터 요약: 날짜순 값의 개수, 합계, 평균, 최대, 최소와 최근 7개/이전 7개 평균 변화율을 계산합니다.
- 컨텍스트 주입: 계산된 요약 JSON을 AI의 `instructions`에 넣어 사용자 데이터에 근거한 답을 생성합니다.
- 구조 분리: router는 입출력, service는 업무 로직, schema는 검증을 담당합니다.
- 보안: 키를 Git에 올리지 않고 환경 변수로만 사용합니다.
