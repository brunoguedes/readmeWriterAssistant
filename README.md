# Readme Writer Assistant

Readme Writer Assistant is a Python-based tool designed to help developers create high-quality README files for their projects. It provides a simple and intuitive interface for generating README files in Markdown format, ensuring that all essential information is included.

## Features

- Generates README files in Markdown format
- Includes a summary of the project and its features
- Provides a high-level overview of the code and project structure
- Offers installation instructions and dependency information
- Includes instructions on how to configure and use the tool
- Acknowledges third-party code and provides contribution guidelines
- Includes license information
- Supports multiple language models, including Claude3 Opus, GPT-3.5 Turbo, GPT-4, llama3, llama3 Groq, openhermes, mistral, and mixtral

## Project Structure

```
├── .env
├── .env_example
├── LICENSE
├── pyproject.toml
└── src
    ├── app.py
    └── readmewriterassistant
        ├── __init__.py
        ├── files_manager.py
        └── llms.py
```

The `src/readmewriterassistant/__init__.py` file is an empty file that marks the `readmewriterassistant` directory as a Python package. It allows the modules within the package to be imported and used in other parts of the project.

The `src/readmewriterassistant/files_manager.py` file contains the `FilesManager` class, which provides methods for listing files, formatting the file tree, and reading file contents.

The `src/readmewriterassistant/llms.py` file contains the `LLMs` class, which manages the available language models and their configurations. It provides the following methods:

- `__init__(self, temperature=0.1)`: Initializes the `LLMs` class with a specified temperature and loads the environment variables from the `.env` file.
- `get_llm(self, llm_name)`: Returns the language model instance based on the provided `llm_name`.
- `get_max_context_length(self, llm_name)`: Returns the maximum context length for the specified `llm_name`.
- `get_available_llms(self)`: Returns a list of available language models.

## Installation

1. Clone the repository:

```
git clone https://github.com/brunoguedes/readmewriterassistant.git
```

2. Navigate to the project directory:

```
cd readmewriterassistant
```

3. Install the required dependencies using Poetry:

```
poetry install
```

## Dependencies

- Python 3.12
- Streamlit 1.33.0
- python-dotenv 1.0.1
- langchain 0.1.16
- langchain-community 0.0.34
- langchain-anthropic 0.1.11
- langchain-openai 0.1.3
- langchain-groq 0.1.3

## Configuration and Usage

1. Create a copy of the `.env_example` file and rename it to `.env`.

2. Open the `.env` file and fill in the required configuration variables:

```
OPENAI_API_KEY='your_openai_api_key'
ANTHROPIC_API_KEY='your_anthropic_api_key'
IS_LOCAL='true'
```

3. Run the application:

```
streamlit run ./src/app.py
```

4. The application will launch in your default web browser. You will see the following options:
   - Select the language model you'd like to use from the dropdown menu.
   - Enter the names of folders or files you'd like to exclude (comma-separated).
   - Enter the folder you want to generate the README.md from.
   - The folder structure will be displayed below.
   - Click the "Generate ReadMe.md" button to generate the README file.

5. The generated README.md will be displayed in sections, updating as the application processes each file in the project structure.

## Acknowledgements

- OpenAI for providing the language model API
- Anthropic for providing the language model API
- Streamlit for the web application framework
- Poetry for dependency management and packaging

## Contributing

We welcome contributions from the community! If you'd like to contribute to Readme Writer Assistant, please follow these steps:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Make your changes and commit them with descriptive messages
4. Push your changes to your forked repository
5. Submit a pull request to the main repository

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
