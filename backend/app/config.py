from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "AI Resume API"
    VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"

    DATABASE_URL: str = "postgresql+asyncpg://postgres:123456789@localhost:5432/resume_analyzer"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
