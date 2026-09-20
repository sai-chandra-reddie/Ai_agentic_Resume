from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "AI Resume API"
    VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"

    DATABASE_URL: str = "postgresql+asyncpg://postgres:123456789@localhost:5432/resume_analyzer"

    SECRET_KEY: str = "default_insecure_secret_key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

        # SMTP Settings
    SMTP_HOST: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_USER: str = ""         # your email
    SMTP_PASSWORD: str = ""     # your app password
    EMAILS_FROM_EMAIL: str = "" # same as SMTP_USER usually
    EMAILS_FROM_NAME: str = "AI Resume Builder"


    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
