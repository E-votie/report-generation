from functools import lru_cache
#from pydantic_settings import BaseSettings
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from pathlib import Path

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
BOT_DATA_DIR = Path(BASE_DIR).parent / 'bot_data'

load_dotenv()

class Settings(BaseModel):
    openai_api_key: str = os.getenv("openai_api_key")
    min_summary_token_limit: int = 400

@lru_cache()
def get_settings():
    return Settings()