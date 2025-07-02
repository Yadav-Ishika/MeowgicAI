import os
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

# 📄 Step 1: Read your combined cat data file
with open("cat_data.txt", "r", encoding="utf-8") as f:
    text = f.read()

# ✂️ Step 2: Break the text into individual sentences
sentences = sent_tokenize(text)

# 🧼 Step 3: Optional - Clean sentences
cleaned_sentences = [s.strip().replace("\n", " ") for s in sentences if len(s.strip()) > 0]

# 💾 Step 4: Save cleaned sentences to a new file (optional)
with open("cat_sentences.txt", "w", encoding="utf-8") as f:
    for s in cleaned_sentences:
        f.write(s + "\n")

print(f"✅ Done! Extracted {len(cleaned_sentences)} sentences.")
