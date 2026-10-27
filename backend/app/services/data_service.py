from datetime import datetime
from app.database import get_db

def _serialize(doc):
    d = doc.to_dict(); d["id"] = doc.id
    for k, v in list(d.items()):
        if hasattr(v, "isoformat"): d[k] = v.isoformat()
    return d

def create_data(payload):
    db=get_db(); body=payload.model_dump(mode="json")
    body["created_at"] = datetime.utcnow()
    ref=db.collection("data").document(); ref.set(body)
    return {"id":ref.id, **payload.model_dump(mode="json")}

def list_data():
    docs=get_db().collection("data").order_by("date").stream()
    return [_serialize(d) for d in docs]

def update_data(doc_id, payload):
    ref=get_db().collection("data").document(doc_id)
    if not ref.get().exists: return None
    body=payload.model_dump(mode="json"); body["updated_at"]=datetime.utcnow(); ref.update(body)
    return {"id":doc_id, **payload.model_dump(mode="json")}

def delete_data(doc_id):
    ref=get_db().collection("data").document(doc_id)
    if not ref.get().exists: return False
    ref.delete(); return True

def get_summary():
    rows=list_data()
    if not rows:
        return {"period":"데이터 없음","count":0,"metrics":{},"trend":"판단 불가"}
    values=[float(r["value"]) for r in rows]
    recent=values[-7:]; previous=values[-14:-7]
    trend="유지"
    change=0.0
    if previous:
        a=sum(recent)/len(recent); b=sum(previous)/len(previous)
        change=((a-b)/b*100) if b else 0
        trend="증가" if change>5 else "감소" if change<-5 else "유지"
    return {"period":f'{rows[0]["date"]} ~ {rows[-1]["date"]}',"count":len(rows),
      "metrics":{"total":round(sum(values),1),"average":round(sum(values)/len(values),1),"max":max(values),"min":min(values)},
      "trend":f"{trend} (최근 7개 vs 이전 7개: {change:+.1f}%)","unit":"분"}
