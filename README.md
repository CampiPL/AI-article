# Article to HTML Generator

This project is a Python-based tool that connects to the OpenAI API to convert an article into HTML format. The generated HTML content can then be embedded into a predefined template and saved as an output file for preview purposes. This project uses a custom template for article presentation and automatically adds image placeholders and captions where necessary.

## Features

- Loads an article from a text file.
- Uses OpenAI's GPT-3.5 model to generate HTML from article content.
- Embeds the generated HTML content into a predefined template.
- Saves the final HTML output into a file for previewing.
- Supports API key configuration via a `.env` file to ensure security.

## Prerequisites

Before you begin, ensure that you have the following installed:

- Python 3.7 or higher
- [pip](https://pip.pypa.io/en/stable/) (Python package manager)

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/article-to-html-generator.git

2. Navigate to the project directory:

cd article-to-html-generator

3. Create a virtual environment:

python -m venv env

4. Activate the virtual environment:

On Windows:

.\env\Scripts\activate

On macOS/Linux:

source env/bin/activate

5. Install the required dependencies:

pip install -r requirements.txt

6. Create a .env file in the root directory with your OpenAI API key:

API_KEY=your-api-key-here

## Usage

1. Prepare an article text file (article.txt) containing the article content you want to convert.

2. Run the program.py script to process the article and generate the HTML:

python program.py

3. The script will generate:

 - artykul.html: The raw HTML content of the article.
 - podglad.html: A final HTML preview with a template applied.

4. Open the podglad.html file in your browser to view the formatted article.

## Files

 - program.py: Main Python script for generating the HTML from article content.
 - szablon.html: Template file for the final HTML output.
 - article.txt: Sample article content file (you can replace this with your own content).
 - requirements.txt: List of required Python libraries.
 - .gitignore: To ignore sensitive files such as the .env file.

## Dependencies

 - openai: For interacting with the OpenAI API.
 - python-dotenv: To load environment variables from the .env file.
 - Other dependencies listed in requirements.txt.

## License

This project is licensed under the MIT License - see the LICENSE file for details.