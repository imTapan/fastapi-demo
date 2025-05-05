from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI Demo"
    debug: bool = True

    class Config:
        env_file = ".env"

settings = Settings()
