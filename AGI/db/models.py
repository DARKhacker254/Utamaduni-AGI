# models/proverb_model.py
from pydantic import BaseModel

class Proverb(BaseModel):
    id: str
    category: str
    culture: str
    language: str
    text: str
    meaning: str
    tags: list[str]
