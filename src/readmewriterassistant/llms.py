import os
from dotenv import load_dotenv

from langchain_community.llms import Ollama
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_groq import ChatGroq

class LLMs:
    def __init__(self, temperature=0.1):
        load_dotenv()  # Load environment variables from .env file
        is_local = os.getenv("IS_LOCAL", "false").lower() == "true"
        if is_local:
            self.llm_map = {
                "Claude3 Opus": {
                    "llm": lambda: ChatAnthropic(model_name="claude-3-opus-20240229", temperature=temperature),
                    "max_context_length": 100000
                },
                "GPT-3.5 Turbo": {
                    "llm": lambda: ChatOpenAI(model_name="gpt-3.5-turbo", temperature=temperature),
                    "max_context_length": 4096
                },
                "GPT-4": {
                    "llm": lambda: ChatOpenAI(model_name="gpt-4", temperature=temperature),
                    "max_context_length": 8192
                },
                "llama3": {
                    "llm": lambda: Ollama(model="llama3", temperature=temperature),
                    "max_context_length": 8192
                },
                "llama3 Groq": {
                    "llm": lambda: ChatGroq(model="llama3-70b-8192", temperature=temperature),
                    "max_context_length": 8192
                },
                "openhermes": {
                    "llm": lambda: Ollama(model="openhermes", temperature=temperature),
                    "max_context_length": 2048
                },
                "mistral": {
                    "llm": lambda: Ollama(model="mistral", temperature=temperature),
                    "max_context_length": 2048
                },
                "mixtral": {
                    "llm": lambda: Ollama(model="mixtral", temperature=temperature),
                    "max_context_length": 2048
                }
            }
        else:
            self.llm_map = {
                "Claude3 Opus": {
                    "llm": lambda: ChatAnthropic(model_name="claude-3-opus-20240229", temperature=temperature),
                    "max_context_length": 100000
                },
                "GPT-3.5 Turbo": {
                    "llm": lambda: ChatOpenAI(model_name="gpt-3.5-turbo", temperature=temperature),
                    "max_context_length": 4096
                },
                "GPT-4": {
                    "llm": lambda: ChatOpenAI(model_name="gpt-4", temperature=temperature),
                    "max_context_length": 8192
                },
                "llama3 Groq": {
                    "llm": lambda: ChatGroq(model="llama3-70b-8192", temperature=temperature),
                    "max_context_length": 8192
                }
            }

    def get_llm(self, llm_name):
        return self.llm_map.get(llm_name)["llm"]()

    def get_max_context_length(self, llm_name):
        return self.llm_map.get(llm_name)["max_context_length"]

    def get_available_llms(self):
        return list(self.llm_map.keys())
    