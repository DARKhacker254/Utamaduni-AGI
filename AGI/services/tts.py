from gtts import gTTS
import os, uuid

def text_to_speech(text: str, lang: str = "sw"):
    """Convert text to speech and return audio file paths."""
    tts = gTTS(text=text, lang=lang)
    fname = f"speech_{uuid.uuid4().hex[:8]}.mp3"
    path = os.path.join("data", "tts", fname)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tts.save(path)
    return path
