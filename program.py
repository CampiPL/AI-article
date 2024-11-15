import openai
import os
import argparse
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve the API key from environment variables
openai.api_key = os.getenv("API_KEY")

def load_article(file_path):
    """
    Load the article content from a specified file path.
    
    Parameters:
        file_path (str): The path to the file containing the article content.
        
    Returns:
        str: The content of the article as a string.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def generate_html(article_content):
    """
    Generate HTML content for the article using OpenAI's API.
    The function sends a prompt to OpenAI's ChatCompletion API to format
    the article with HTML tags, add image placeholders, and captions where appropriate.

    Parameters:
        article_content (str): The text content of the article to be formatted in HTML.
        
    Returns:
        str: The generated HTML content as a string.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant that formats articles into HTML."},
            {"role": "user", "content": (
                f"Create an HTML body content structure for the following article content (without <html>, <head>, and <body> tags, plain body content). "
                f"Use appropriate tags, insert <img src='image_placeholder.jpg' alt='...'/> for image suggestions (at least one per heading) and put them "
                f"in the appropriate place in the text (but not in the beginning), also those images should be in figure. "
                f"Add descriptive captions with <figcaption> to each image.\n\n"
                f"Article content:\n{article_content}"
            )}
        ],
        max_tokens=2000,
        temperature=0.7,
    )
    return response.choices[0].message['content'].strip()

def save_html(content, file_path):
    """
    Save the generated HTML content to a specified file.
    
    Parameters:
        content (str): The HTML content to be saved.
        file_path (str): The path to the file where the content will be saved.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
        
def generate_overview(artykul_path, template_path, output_path):
    """
    Save the generated HTML content from the article file by inserting it into a template.
    
    Parameters:
        artykul_path (str): The path to the article HTML file.
        template_path (str): The path to the template file.
        output_path (str): The path to save the final HTML.
    """
    # Odczytaj treść artykułu z pliku artykul.html
    with open(artykul_path, 'r', encoding='utf-8') as artykul_file:
        artykul_content = artykul_file.read()
        
    # Odczytaj szablon z pliku
    with open(template_path, 'r', encoding='utf-8') as template_file:
        template = template_file.read()
    
    # Wstaw treść artykułu w odpowiednie miejsce w szablonie
    final_html = template.replace("<!-- Paste the generated article HTML code here -->", artykul_content)
    
    # Zapisz ostateczny plik HTML
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(final_html)


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Generate HTML content and optionally create an overview.")
    parser.add_argument("--overview", action="store_true", help="Generate overview HTML using the template.")
    parser.add_argument("--only-overview", action="store_true", help="Only generate the overview HTML using the template.")
    args = parser.parse_args()

    if args.only_overview:
        # Generate overview HTML directly from existing 'artykul.html'
        generate_overview('artykul.html', 'szablon.html', 'podglad.html')
    else:
        # Load the article content from the 'article.txt' file
        article_content = load_article("article.txt")
        
        # Generate HTML content using the loaded article
        html_content = generate_html(article_content)
        
        # Save the generated HTML content to 'artykul.html'
        save_html(html_content, "artykul.html")
        
        # Generate overview if the --overview flag is provided
        if args.overview:
            generate_overview('artykul.html', 'szablon.html', 'podglad.html')

if __name__ == "__main__":
    main()
