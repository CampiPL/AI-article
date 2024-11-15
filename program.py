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
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    except Exception as e:
        raise Exception(f"An error occurred while reading the file {file_path}: {e}")

def generate_html(article_content):
    """
    Generate HTML content for the article using OpenAI's API.
    """
    try:
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
            temperature=0.7,
        )
        return response.choices[0].message['content'].strip()
    except openai.error.OpenAIError as e:
        raise Exception(f"An error occurred while communicating with OpenAI API: {e}")

def save_html(content, file_path):
    """
    Save the generated HTML content to a specified file.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
    except Exception as e:
        raise Exception(f"An error occurred while saving the file {file_path}: {e}")

def generate_overview(artykul_path, template_path, output_path):
    """
    Generate overview HTML by combining content and a template.
    """
    try:
        
        with open(artykul_path, 'r', encoding='utf-8') as artykul_file:
            artykul_content = artykul_file.read()
            
        with open(template_path, 'r', encoding='utf-8') as template_file:
            template = template_file.read()
        
        if not template.strip():
            raise ValueError("The template file is empty.")
        
        final_html = template.replace("<!-- Paste the generated article HTML code here -->", artykul_content)
        
        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write(final_html)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found: {e}")
    except ValueError as e:
        raise ValueError(f"Invalid template file: {e}")
    except Exception as e:
        raise Exception(f"An error occurred during overview generation: {e}")


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Generate only article HTML, only overview HTML or both.")
    parser.add_argument("--overview", action="store_true", help="Generate article HTML and on its basis overview HTML using the template.")
    parser.add_argument("--only-overview", action="store_true", help="Only generate the overview HTML using the template.")
    args = parser.parse_args()

    try:

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
                
    except ValueError as e:
        print(f"Argument Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
