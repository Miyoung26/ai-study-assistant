from fastapi import APIRouter, HTTPException
from app.models.schemas import DataCreate, DataUpdate
from app.services import data_service as s
router=APIRouter(prefix="/api/data",tags=["data"])
@router.get("/summary")
def summary(): return s.get_summary()
@router.post("")
def create(payload:DataCreate): return s.create_data(payload)
@router.get("")
def list_all(): return s.list_data()
@router.put("/{doc_id}")
def update(doc_id:str,payload:DataUpdate):
    result=s.update_data(doc_id,payload)
    if not result: raise HTTPException(404,"데이터를 찾을 수 없습니다.")
    return result
@router.delete("/{doc_id}")
def delete(doc_id:str):
    if not s.delete_data(doc_id): raise HTTPException(404,"데이터를 찾을 수 없습니다.")
    return {"ok":True}
