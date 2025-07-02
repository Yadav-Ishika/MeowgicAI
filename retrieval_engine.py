import numpy as np
from numpy.linalg import norm
from vector_store_loader import load_vector_store, load_sentence_encoder

# --- Find best matching paragraph ---
def find_best_match(question, model, embeddings, sentences, top_k=1):
    question_vec = model.encode([question])[0]
    similarities = np.dot(embeddings, question_vec) / (norm(embeddings, axis=1) * norm(question_vec))
    top_k_indices = similarities.argsort()[-top_k:][::-1]
    top_matches = [sentences[i] for i in top_k_indices]
    return top_matches

# --- Test block ---
if __name__ == "__main__":
    embeddings, sentences = load_vector_store()
    model = load_sentence_encoder()

    question = "How high can cats jump?"
    top_paragraphs = find_best_match(question, model, embeddings, sentences, top_k=1)

    print("\n🔍 Best Matching Paragraph:\n")
    print(top_paragraphs[0])
