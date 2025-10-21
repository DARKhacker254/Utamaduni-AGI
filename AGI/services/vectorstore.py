import faiss, numpy as np, json, os

def build_index(json_path="data/seed_proverbs.json"):
    with open(json_path) as f:
        data = json.load(f)
    from AGI.services.embedding import get_embedding
    vectors = [get_embedding(d["text_original"]) for d in data]
    dim = len(vectors[0])
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(vectors))
    return index, data

INDEX, DATA = build_index()

def search_similar(text, k=3):
    from AGI.services.embedding import get_embedding
    emb = get_embedding(text)
    D, I = INDEX.search(np.array([emb]), k)
    return [DATA[i] for i in I[0]]
