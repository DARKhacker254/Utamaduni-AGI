from AGI.services.nlp import detect_language, classify_intent
from AGI.services.vectorstore import search_similar
from AGI.services.metta_client import run_rule
from AGI.services.generation import generate_with_context
from AGI.services.tts import text_to_speech


async def cultural_reasoner(user_text: str):
    # (1) Detect language — simple heuristic
    lang = "sw" if any(w in user_text.lower() for w in ["nipe", "methali", "habari"]) else "en"

    # (2) Placeholder intent and reasoning logic
    intent = "proverb_request" if "methali" in user_text.lower() else "general_chat"
    symbolic_result = f"({lang}) Reasoning: lesson 'Patience leads to blessing'. Example proverb: 'Haraka haraka haina baraka'."

    # (3) Placeholder related data (could come from FAISS or MeTTa)
    related = [{"text_original": "Haraka haraka haina baraka"}]

    # (4) Generate text reply
    reply = symbolic_result

    # (5) Generate audio
    audio_path = text_to_speech(reply, lang)

    # ✅ (6) Return final structured response
    return {
        "lang": lang,
        "intent": intent,
        "reasoning": symbolic_result,
        "sources": [r["text_original"] for r in related],
        "reply": reply,
        "audio_url": f"/static/tts/{audio_path.split('/')[-1]}"
    }
