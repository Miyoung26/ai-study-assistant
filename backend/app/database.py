import json
import firebase_admin
from firebase_admin import credentials, firestore
from app.config import FIREBASE_SERVICE_ACCOUNT_JSON

_db = None

def get_db():
    global _db
    if _db is not None:
        return _db
    if not FIREBASE_SERVICE_ACCOUNT_JSON:
        raise RuntimeError("FIREBASE_SERVICE_ACCOUNT_JSON 환경 변수가 없습니다.")
    if not firebase_admin._apps:
        info = json.loads(FIREBASE_SERVICE_ACCOUNT_JSON)
        firebase_admin.initialize_app(credentials.Certificate(info))
    _db = firestore.client()
    return _db
