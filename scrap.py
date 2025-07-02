# import wikipediaapi

# # Add a proper user-agent string
# wiki = wikipediaapi.Wikipedia(
#     language='en',
#     user_agent='MeowgicAI-NLP-Project/1.0 (ishika11112@gmail.com)'
# )

# page = wiki.page("Cat")

# if page.exists():
#     with open("cat_wikipedia.txt", "w", encoding="utf-8") as f:
#         f.write(page.text)
#     print("Text saved successfully.")
# else:
#     print("Page not found.")
# ------------------------------------------------------------------
def count_words_in_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return 0

# Path to your file
file_path = "cat_data.txt"
word_count = count_words_in_file(file_path)

print(f"Total number of words in '{file_path}': {word_count}")
# -------------------------------------------------------------------
# import requests
# from bs4 import BeautifulSoup

# url = "https://www.britannica.com/animal/cat"

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
# }

# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.content, "html.parser")

# # Find article container
# article = soup.find("article")

# # Extract text from paragraphs inside the article
# paragraphs = article.find_all("p")
# text = "\n\n".join([p.get_text(strip=True) for p in paragraphs])

# # Save to a .txt file
# with open("cat_fun_facts.txt", "w", encoding="utf-8") as f:
#     f.write(text)

# print("Cat facts scraped and saved to 'cat_fun_facts.txt'")