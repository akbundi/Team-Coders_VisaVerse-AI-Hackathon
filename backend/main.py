from fastapi import FastAPI
from api import visa, chat

app = FastAPI(title="AI Global Mobility Assistant")

app.include_router(visa.router, prefix="/visa")
app.include_router(chat.router, prefix="/chat")
