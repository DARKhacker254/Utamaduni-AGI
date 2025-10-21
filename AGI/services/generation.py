import asyncio

async def generate_with_context(user_text, lang, reasoning, related):
    # Simple rule-based generation for Phase 2 (LLM later)
    base = f"({lang.upper()}) Reasoning: {reasoning}"
    example = related[0]["text_original"] if related else "No cultural data found"
    await asyncio.sleep(0.1)
    return f"{base}. Example proverb: '{example}'."
