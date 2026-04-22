from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "ItemAdvisor Foundation"
    env: str = "development"
    mongodb_uri: str = "mongodb://localhost:27017"
    mongodb_db: str = "itemadvisor"
    session_secret: str = "change-me-for-production"
    session_cookie_name: str = "itemadvisor_session"
    session_secure: bool = False
    manager_email: str = "manager@example.com"
    manager_password: str = "manager123"
    user_email: str = "user@example.com"
    user_password: str = "user123"

    model_config = SettingsConfigDict(
        env_prefix="ITEMADVISOR_",
        env_file=".env",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()

