import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'


class Settings:
    PROJECT_NAME: str = 'WT info'
    PROJECT_VERSION: str = "1.0.0"

    PG_USER: str = os.getenv('POSTGRES_USER')
    PG_PWD: str = os.getenv('POSTGRES_PASSWORD')
    PG_SERVER: str = os.getenv('POSTGRES_SERVER', 'localhost')
    PG_PORT: str = os.getenv('POSTGRES_PORT', 5342)
    PG_DB: str = os.getenv('POSTGRES_DB')
    DATABASE_URL = (f"")
