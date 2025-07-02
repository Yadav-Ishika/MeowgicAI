from sentence_transformers import SentenceTransformer
import numpy as np
import os
import pickle

# Load your cleaned cat data
def load_cat_sentences(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        sentences = f.readlines()
    # Clean and strip
    return [s.strip() for s in sentences if s.strip() != ""]

# Vectorize the sentences
def vectorize_sentences(sentences, model_name='all-MiniLM-L6-v2'):
    print("[INFO] Loading embedding model...")
    model = SentenceTransformer(model_name)
    print("[INFO] Encoding sentences...")
    embeddings = model.encode(sentences)
    return embeddings

# Save embeddings and original text
def save_embeddings(embeddings, sentences, output_dir='vector_data'):
    os.makedirs(output_dir, exist_ok=True)
    np.save(os.path.join(output_dir, 'embeddings.npy'), embeddings)
    with open(os.path.join(output_dir, 'sentences.pkl'), 'wb') as f:
        pickle.dump(sentences, f)
    print(f"[SUCCESS] Saved embeddings and sentences in '{output_dir}'")

if __name__ == "__main__":
    file_path = 'cat_sentences.txt'
    sentences = load_cat_sentences(file_path)
    embeddings = vectorize_sentences(sentences)
    save_embeddings(embeddings, sentences)
