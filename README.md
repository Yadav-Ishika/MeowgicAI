# 🐾 MeowgicAI – Your Cat Companion AI

**MeowgicAI** is an NLP-based Question Answering system that intelligently answers any query related to cats using text abstraction (not simple text retrieval). It leverages sentence embeddings, vector similarity search, and a fine-tuned language model (FLAN-T5 or BART) to generate concise, rephrased factual answers.

---

## 🚀 Features

- 🧠 **Text Abstraction** (not extraction!)
- 🔍 Semantic search using vector embeddings
- 🎙️ AI-generated voice response (with mute and replay)
- 🌙 Clean Dark-Themed Streamlit UI
- ⚡ FastAPI-powered backend for question-answering
- 🐱 Cat-specific knowledge base from raw text

---

## 🛠️ Tech Stack

| Layer       | Tools/Libs                               |
|-------------|------------------------------------------|
| UI          | Streamlit + HTML/CSS                     |
| Backend     | FastAPI                                  |
| NLP Model   | `google/flan-t5-base` / `facebook/bart-large-cnn` |
| Embedding   | `sentence-transformers/all-MiniLM-L6-v2` |
| TTS         | `gTTS`                                   |
| Vector Store| Cosine similarity with NumPy             |

---

## 📡 API Test: Successful Response from `/ask` Endpoint

![Landing Page](MeowgicAI/Screenshot 2025-07-02 174144.png)

## 🗂️ Project Structure

MeowgicAI/<br>
├── app.py # (Optional script version)<br>
├── meowgic_ui.py # Streamlit frontend<br>
├── meowgic_api.py # FastAPI backend<br>
├── retrieval_engine.py # Vector search logic<br>
├── vectorize_cat_sentences.py # Embedding generator<br>
├── prepare_sentences.py # Sentence cleaner/tokenizer<br>
├── vector_data/ # Stored embeddings & sentences<br>
├── data/<br>
│ └── cat_data.txt # Raw cat info<br>
│ └── cat_sentences.txt # Tokenized cat facts<br>
├── requirements.txt # Dependencies<br>
└── README.md<br>


---

## 💡 How It Works

1. **Data Preparation**
   - Store raw cat facts in `cat_data.txt`
   - Clean and split into sentences → `cat_sentences.txt`
   - Vectorize using Sentence Transformers → `vector_data/`

2. **Query Flow**
   - User types a question on UI
   - Backend finds top-matching sentences via cosine similarity
   - Model generates abstracted answer from context
   - Voice is generated via gTTS and played automatically

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/MeowgicAI.git
cd MeowgicAI
```
### 2. Install Dependencies
```
pip install -r requirements.txt
```
### 3.Prepare Data
```
python prepare_sentences.py
python vectorize_cat_sentences.py
```
### 4.Run Backend
```
uvicorn meowgic_api:app --reload
```
### 5.Launch UI
```
python meowgic_ui.py
```

# Conclusion
This program is currently executing with zero error, so you are good to go with it, **Thank You**

# License
Apache-2.0 license

# Contact me at
LinkedIn Account : www.linkedin.com/in/rayyan-ashraf-71117b249<br />
Instagram Account : @etsrayy<br />
Email At : ryshashraf@gmail.com

