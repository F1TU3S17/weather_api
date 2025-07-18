from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    OPENWEATHER_API_KEY: str
    OPEN_ROUTER_API_KEY: str
    LOCAL_REDIS_URL: str
    class Config:
        env_file = ".env"
        
settings = Settings()