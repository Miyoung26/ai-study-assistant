from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import ALLOWED_ORIGINS
from app.routers import data, conversations, chat
app=FastAPI(title="나의 학습시간 AI 비서",version="1.0.0")
app.add_middleware(CORSMiddleware,allow_origins=ALLOWED_ORIGINS,allow_credentials=True,allow_methods=["*"],allow_headers=["*"])
app.include_router(data.router); app.include_router(conversations.router); app.include_router(chat.router)
@app.get("/")
def root(): return {"message":"API is running","docs":"/docs"}
@app.get("/health")
def health(): return {"status":"ok"}
