"""The LLM used by both the RAG chain and the agents.

Gemini is called through the Gemini API with an API key (GOOGLE_API_KEY) in BOTH modes:
  * local - the key comes from your .env
Embeddings (rag/embeddings.py) switch between the Gemini API and Vertex AI with APP_MODE.
"""

from langchain_google_genai import ChatGoogleGenerativeAI

from config.settings import settings
from exceptions import ConfigurationError


def get_llm() -> ChatGoogleGenerativeAI:
    """Create the chat model on first use (not at import time) and reuse it afterwards."""
    if not settings.GOOGLE_API_KEY:
        raise ConfigurationError("GOOGLE_API_KEY is empty. Add it to .env (https://aistudio.google.com/apikey).")
    return ChatGoogleGenerativeAI(
        model=settings.llm_model_name,
        google_api_key=settings.GOOGLE_API_KEY,
        temperature=settings.llm_temperature,
    )
