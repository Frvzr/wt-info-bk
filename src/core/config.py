import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


class Settings(BaseSettings):
    DRIVER: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    SECRET_KEY: str = "secret"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DEBUG: bool = False
    TESTING: bool = False

    # model_config = SettingsConfigDict(
    #     env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
    # )
    model_config = SettingsConfigDict(env_file=Path(__file__).resolve().parent.parent.parent / ".env")

    def get_db_url(self):
        return (f"{self.DRIVER}://{self.DB_USER}:{self.DB_PASSWORD}@"
                f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}")


settings = Settings()
