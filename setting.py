from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    db_connection: str
    ollama_url: str
    qdrant_host: str
    qdrant_port: int

    model_config = SettingsConfigDict(
        env_file=".env"
    )

settings = Settings()