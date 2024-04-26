Here's a generated README.md for your project:

# README Writer Assistant

README Writer Assistant is a Python project that generates README.md files for a given project structure. It uses language models like GPT-4, GPT-3.5 Turbo, and Claude3 Opus to generate the content of the README based on the project's file structure and file contents.

## Project Structure

The project has the following file structure:

```
├── .env
├── .env_example
├── poetry.lock
├── pyproject.toml
└── src
    ├── app.py
    └── readmewriterassistant
        ├── __init__.py
        ├── files_manager.py
        └── llms.py
```

## Dependencies

The project uses the following main dependencies:

- streamlit: For building the web application interface
- python-dotenv: For loading environment variables from .env file
- langchain: For integrating with language models
- langchain-community: For additional LangChain integrations
- langchain-anthropic: For integrating with Anthropic's language models
- langchain-openai: For integrating with OpenAI's language models

The full list of dependencies can be found in the `pyproject.toml` file.

## Configuration

The project uses environment variables for configuration. The `.env` file contains the API keys for OpenAI and Anthropic. An example `.env` file is provided as `.env_example`. Make sure to create a `.env` file with your own API keys before running the application.

## Usage

To run the application, navigate to the `src` directory and run the following command:

```
streamlit run app.py
```

This will start the Streamlit application. In the web interface, you can:

1. Select the language model to use for generating the README
2. Enter the names of folders or files to exclude (comma-separated)
3. Enter the base folder path for generating the README
4. Click the "Generate ReadMe.md" button to generate the README content

The generated README content will be displayed in the web interface.

## Code Overview

The main components of the project are:

- `app.py`: The main Streamlit application file that sets up the user interface and handles user interactions.
- `readmewriterassistant/files_manager.py`: Contains the `FilesManager` class responsible for listing files, formatting the file tree, and reading file contents.
- `readmewriterassistant/llms.py`: Contains the `LLMs` class that manages the available language models and their initialization based on the environment (local or not).

The `App` class in `app.py` uses the `FilesManager` and `LLMs` classes to generate the README content based on the selected language model, excluded files/folders, and the project's file structure and contents.

## License

This project is open-source and available under the [MIT License](LICENSE).
