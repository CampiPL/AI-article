import openai
import os

# Konfiguracja klucza API OpenAI
openai.api_key = "YOUR_API_KEY"

def load_article(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def generate_html(article_content):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant that formats articles into HTML."},
            {"role": "user", "content": (
                f"Create an HTML body content structure for the following article content. "
                f"Use appropriate tags, insert <img src='image_placeholder.jpg' alt='...'/> for image suggestions, "
                f"and add captions with <figcaption> where relevant.\n\n"
                f"Article content:\n{article_content}"
            )}
        ],
        max_tokens=2000,
        temperature=0.7,
    )
    return response.choices[0].message['content'].strip()

def save_html(content, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def main():
    article_content = load_article("article.txt")  # Wczytaj artykuł z pliku
    html_content = generate_html(article_content)  # Przetwórz artykuł do HTML
    save_html(html_content, "artykul.html")  # Zapisz HTML do pliku

if __name__ == "__main__":
    main()
