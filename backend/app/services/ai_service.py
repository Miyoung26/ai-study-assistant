import json
from openai import OpenAI
from app.config import OPENAI_API_KEY, OPENAI_MODEL
from app.services.data_service import get_summary
from app.services.conversation_service import save_conversation


def chat(message, prior_messages, conversation_id=None):
    if not OPENAI_API_KEY:
        raise RuntimeError("OPENAI_API_KEY 환경 변수가 없습니다.")
    summary = get_summary()
    instructions = (
        "당신은 사용자의 학습시간 데이터를 분석하는 친절한 AI 비서입니다. "
        "아래 요약에 근거해 답하고, 데이터로 확인할 수 없는 내용은 추측하지 마세요. "
        "값의 단위는 분입니다. 초보자가 이해하기 쉽게 한국어로 답하세요.\n\n"
        f"[사용자 데이터 요약]\n{json.dumps(summary, ensure_ascii=False)}"
    )
    history = [{"role": m["role"], "content": m["content"]} for m in prior_messages[-10:]]
    input_items = history + [{"role": "user", "content": message}]
    response = OpenAI(api_key=OPENAI_API_KEY).responses.create(
        model=OPENAI_MODEL,
        instructions=instructions,
        input=input_items,
        max_output_tokens=500,
    )
    answer = response.output_text
    messages = history + [
        {"role": "user", "content": message},
        {"role": "assistant", "content": answer},
    ]
    title = message[:30] + ("..." if len(message) > 30 else "")
    saved = save_conversation(title, messages, conversation_id)
    return {"answer": answer, "conversation_id": saved["id"], "summary": summary}
