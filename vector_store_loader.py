import numpy as np
import pickle
from sentence_transformers import SentenceTransformer

# Step 1: Load vector embeddings and sentence chunks
def load_vector_store():
    # Load the saved embeddings
    embeddings = np.load("vector_data/embeddings.npy")
    
    # Load the corresponding sentences
    with open("vector_data/sentences.pkl", "rb") as f:
        sentences = pickle.load(f)

    return embeddings, sentences

# Step 2: Load the same sentence transformer model you used earlier
def load_sentence_encoder():
    model = SentenceTransformer('all-MiniLM-L6-v2')
    return model


if __name__ == "__main__":
    embeddings, sentences = load_vector_store()
    print(f"✅ Loaded {len(sentences)} sentences and {embeddings.shape[0]} vectors.")
