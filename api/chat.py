from fastapi import FastAPI, Depends, APIRouter
from models.chat_response import ChatResponse
from models.chat_request import ChatRequest
from dependencies import get_bot_service
from service.bot import Bot

router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest, bot: Bot = Depends(get_bot_service)):
    response = bot.ask(request.message)
    return ChatResponse(response=response)