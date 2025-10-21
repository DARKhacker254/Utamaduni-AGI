import json

def get_random_fact(lang: str, path="data/seed_proverbs.json"):
    with open(path) as f:
        data = json.load(f)
    filtered = [d for d in data if d["language"] == lang]
    import random
    return random.choice(filtered if filtered else data)
