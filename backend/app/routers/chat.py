from fastapi import APIRouter, HTTPException
from app.models.schemas import ChatRequest
from app.services.ai_service import chat
router=APIRouter(prefix="/api/chat",tags=["chat"])
@router.post("")
def create(payload:ChatRequest):
    try: return chat(payload.message,[m.model_dump() for m in payload.messages],payload.conversation_id)
    except Exception as e: raise HTTPException(500,f"AI 처리 중 오류: {str(e)}")
