from pydantic_settings import BaseSettings , SettingsConfigDict
from pathlib import Path

# Get the path to src/.env
SRC_DIR = Path(__file__).resolve().parent.parent  # Points to 'src' directory
ENV_FILE = SRC_DIR / ".env"

class Settings(BaseSettings):
    APP_NAME : str
    APP_VERSION: str 
    # OPENAI_API_KEY :str
    FILE_MAX_SIZE: int
    FILE_ALLOWED_TYPES : list
    FILE_DEFAULT_CHUNK_SIZE: int
    model_config = SettingsConfigDict(
        env_file=str(ENV_FILE),  # ← Explicit path to src/.env
        env_file_encoding="utf-8"
    )
        
def get_settings():
    return Settings()
        
    