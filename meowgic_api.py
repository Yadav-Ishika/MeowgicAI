from fastapi import FastAPI
from pydantic import BaseModel
from retrieval_engine import load_vector_store, load_sentence_encoder, find_best_match
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

app = FastAPI()

# --- Load model and encoders once ---
print("[INFO] Loading vector store...")
embeddings, sentences = load_vector_store()

print("[INFO] Loading sentence encoder...")
encoder = load_sentence_encoder()

print("[INFO] Loading model...")
model_name = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)


# --- Request schema ---
class QuestionRequest(BaseModel):
    question: str


# --- Generate abstracted answer ---
def generate_answer(context, question, tokenizer, model, max_length=150):
    prompt = f"""You are a cat expert.

Based only on the context below, answer the question in 1–2 clear and rephrased factual sentences.

Context: {context}

Question: {question}

Answer:"""

    # Tokenize with truncation to avoid exceeding model limit
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)

    output = model.generate(
        **inputs,
        max_length=max_length,
        do_sample=True,
        top_p=0.9,
        temperature=0.7,
        num_return_sequences=1,
        repetition_penalty=1.2
    )

    answer = tokenizer.decode(output[0], skip_special_tokens=True).strip()

    # Keep only first 2 sentences
    sentences = answer.split(". ")
    answer = ". ".join(sentences[:2]).strip()
    if not answer.endswith("."):
        answer += "."

    return answer


# --- API route ---
@app.post("/ask")
def ask_question(request: QuestionRequest):
    question = request.question.strip()

    print(f"[INFO] Received question: {question}")

    # 🔼 Increased top_k for richer context
    top_paragraphs = find_best_match(question, encoder, embeddings, sentences, top_k=8)
    context = " ".join([para.strip() for para in top_paragraphs])

    print("[INFO] Generating answer...")

    answer = generate_answer(context, question, tokenizer, model)

    return {
        "question": question,
        "answer": answer,
        "top_paragraphs": top_paragraphs
    }
