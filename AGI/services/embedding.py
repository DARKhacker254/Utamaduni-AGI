from sentence_transformers import SentenceTransformer
from AGI.core.config import EMBEDDING_MODEL

_model = SentenceTransformer(EMBEDDING_MODEL)

def get_embedding(text: str):
    return _model.encode(text)
