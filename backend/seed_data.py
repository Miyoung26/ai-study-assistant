from datetime import date, timedelta
import random
from app.database import get_db
random.seed(42)
db=get_db(); batch=db.batch(); start=date.today()-timedelta(days=119)
for i in range(120):
    d=start+timedelta(days=i); base=35+i*0.25; value=max(0,round(base+random.randint(-20,25)))
    ref=db.collection("data").document(); batch.set(ref,{"date":d.isoformat(),"value":value,"memo":"샘플 학습 기록"})
batch.commit(); print("120개 샘플 데이터 저장 완료")
