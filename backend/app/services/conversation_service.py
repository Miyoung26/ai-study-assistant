from datetime import datetime
from app.database import get_db

def _doc(doc):
    d=doc.to_dict(); d["id"]=doc.id
    for k,v in list(d.items()):
        if hasattr(v,"isoformat"): d[k]=v.isoformat()
    return d

def save_conversation(title, messages, conversation_id=None):
    db=get_db(); body={"title":title,"messages":messages,"updated_at":datetime.utcnow()}
    if conversation_id:
        ref=db.collection("conversations").document(conversation_id); ref.set(body, merge=True)
    else:
        body["created_at"]=datetime.utcnow(); ref=db.collection("conversations").document(); ref.set(body)
    return {"id":ref.id, **body}

def list_conversations():
    docs=get_db().collection("conversations").order_by("updated_at", direction="DESCENDING").stream()
    return [_doc(d) for d in docs]

def get_conversation(doc_id):
    doc=get_db().collection("conversations").document(doc_id).get()
    return _doc(doc) if doc.exists else None

def delete_conversation(doc_id):
    ref=get_db().collection("conversations").document(doc_id)
    if not ref.get().exists:return False
    ref.delete();return True
