from fastapi import APIRouter, HTTPException
from app.models.schemas import ConversationCreate
from app.services import conversation_service as s
router=APIRouter(prefix="/api/conversations",tags=["conversations"])
@router.post("")
def create(payload:ConversationCreate): return s.save_conversation(payload.title,[m.model_dump() for m in payload.messages])
@router.get("")
def list_all(): return s.list_conversations()
@router.get("/{doc_id}")
def get_one(doc_id:str):
    result=s.get_conversation(doc_id)
    if not result: raise HTTPException(404,"대화를 찾을 수 없습니다.")
    return result
@router.delete("/{doc_id}")
def delete(doc_id:str):
    if not s.delete_conversation(doc_id): raise HTTPException(404,"대화를 찾을 수 없습니다.")
    return {"ok":True}
