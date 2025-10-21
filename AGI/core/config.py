import os
from dotenv import load_dotenv
load_dotenv()

DB_URL = os.getenv("DATABASE_URL", "sqlite:///./utamaduni.db")
EMBEDDING_MODEL = "paraphrase-multilingual-MiniLM-L12-v2"
