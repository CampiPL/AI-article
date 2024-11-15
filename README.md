# Article to HTML Generator

This project is a Python-based application that connects to the OpenAI API to generate HTML content from a given article. The app processes the article, generates HTML body content with appropriate structure and tags, and then saves the output to a file. Additionally, it can generate an overview HTML page by embedding the generated article HTML into a template.

## Features

 - Article Processing: Load a text file containing an article and generate structured HTML content using OpenAI's API.
 - Template Integration: Combine the generated article HTML with a predefined template to produce a complete overview HTML page.
 - CLI Interface: Command-line interface for generating article HTML, overview HTML, or both, with simple arguments.
 - Supports API key configuration via a `.env` file to ensure security.

## Requirements

### Before you begin, ensure that you have the following installed:

 - Python 3.7 or higher
 - [pip](https://pip.pypa.io/en/stable/) (Python package manager)

## Setup

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/article-to-html-generator.git

2. Navigate to the project directory:

	```bash
	cd article-to-html-generator

3. Create a virtual environment:

	```bash
	python -m venv env

4. Activate the virtual environment:

 - On Windows:

	```bash
	.\env\Scripts\activate

 - On macOS/Linux:

	```bash
	source env/bin/activate

5. Install the required dependencies:

	```bash
	pip install -r requirements.txt

6. Create a .env file in the root directory with your OpenAI API key:

	```makefile
	API_KEY = "your-openai-api-key-here"

## Files

 - program.py: Main Python script for generating the HTML from article content.
 - szablon.html: Template file for the final HTML output.
 - article.txt: Sample article content file (you can replace this with your own content).
 - requirements.txt: List of required Python libraries.
 - .gitignore: To ignore sensitive files such as the .env file.

## Usage

### You have three options to run this program depending on arguments you pass

1. Generate HTML from article


	```bash
	python program.py
	```

	This will:

	- Read the article from article.txt.
	- Generate HTML and save it to artykul.html.

2. Generate HTML from article with its overview HTML

	```bash
	python program.py --overview
	```

	This will:

	- Generate HTML from article.txt (if not already generated).
	- Create podglad.html by inserting the article HTML into the szablon.html template.

3. Generate Only Overview HTML
	If you already have the artykul.html file and only want to generate the overview HTML:

	```bash
	python program.py --only-overview
	```

	This will:

	- Read the existing artykul.html and szablon.html.
	- Generate podglad.html without regenerating the article HTML.

## Dependencies

 - OpenAI API key (ensure you have registered and received an API key from OpenAI)
 - Other dependencies listed in requirements.txt.

## Troubleshooting

Ensure the .env file contains a valid API key.
If any files (e.g., article.txt, szablon.html) are missing or corrupted, the program will raise appropriate errors.