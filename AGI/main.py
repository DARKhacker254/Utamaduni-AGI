from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from AGI.routes.api_v1 import router as api_router
from AGI.core.logger import logger
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI(title="Utamaduni Cultural AGI")
os.makedirs("data/tts", exist_ok=True)
app.mount("/static/tts", StaticFiles(directory="data/tts"), name="tts")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def root():
    logger.info("Root endpoint hit")
    return {"message": "Utamaduni AGI running!"}
