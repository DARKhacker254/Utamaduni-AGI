from langdetect import detect
import re

def detect_language(text: str) -> str:
    try:
        lang = detect(text)
        if lang in ["sw", "en"]:
            return lang
    except Exception:
        pass
    if re.search(r"\bomundu\b", text.lower()):
        return "luhya"
    return "en"

def classify_intent(text: str) -> str:
    lower = text.lower()
    if "methali" in lower or "proverb" in lower:
        return "proverb"
    if "hadithi" in lower or "story" in lower:
        return "story"
    return "general"
