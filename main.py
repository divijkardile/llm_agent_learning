from fastapi import FastAPI

from api.chat import router as chat_router
from api.document import router as document_router

app = FastAPI()

app.include_router(chat_router)
app.include_router(document_router)