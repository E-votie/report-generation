from langchain_openai import OpenAIEmbeddings
from config import get_settings

settings = get_settings()

def get_embedding():
    return OpenAIEmbeddings(
        openai_api_key = settings.openai_api_key
    )