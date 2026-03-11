from fastapi import FastAPI
from pydantic import BaseModel
from agent import ask_agent

app = FastAPI()


class ChatRequest(BaseModel):
    message: str
class ChatResponse(BaseModel):
    response: str


@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    reply = await ask_agent(req.message)
    return {"response": reply}