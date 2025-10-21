from fastapi import APIRouter
from pydantic import BaseModel
from AGI.services.reasoner import cultural_reasoner

router = APIRouter()

class Query(BaseModel):
    user_text: str

@router.post("/chat")
async def chat(q: Query):
    response = await cultural_reasoner(q.user_text)
    return response

