from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "FastAPI Project Template"
    app_version: str = "0.1.0"
    debug: bool = True
    host: str = "127.0.0.1"
    port: int = 8000

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()