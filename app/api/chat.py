from fastapi.routing import APIRouter, HTTPException
from starlette.status import HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_400_BAD_REQUEST
from llm.agent import agent_executor
from models.chat import ChatRequest

router = APIRouter()

@router.post("/chat", name="bot:post-data", status_code=HTTP_200_OK)
def bot_response(chat_request: ChatRequest):
    try:
        message = agent_executor.invoke({"input": chat_request.message})
        return message
    except Exception as e:
        raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))