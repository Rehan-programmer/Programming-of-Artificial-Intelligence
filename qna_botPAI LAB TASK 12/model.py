from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def create_index(texts):
    embeddings = model.encode(texts)
    d = embeddings.shape[1]
    index = faiss.IndexFlatL2(d)
    index.add(np.array(embeddings))
    faiss.write_index(index, 'index.faiss')
    return index

def search(query, df, index, k=3):
    query_vec = model.encode([query])
    distances, indices = index.search(np.array(query_vec), k)
    results = []
    for i in range(k):
        results.append(df.iloc[indices[0][i]]['text'])
    return results
