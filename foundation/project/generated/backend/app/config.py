from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


ROOT_ENV_FILE = Path(__file__).resolve().parents[4] / ".env"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=str(ROOT_ENV_FILE), env_file_encoding="utf-8")

    itemadvisor_env: str = Field(alias="ITEMADVISOR_ENV")
    itemadvisor_app_name: str = Field(alias="ITEMADVISOR_APP_NAME")
    itemadvisor_mongodb_uri: str = Field(alias="ITEMADVISOR_MONGODB_URI")
    itemadvisor_mongodb_db: str = Field(alias="ITEMADVISOR_MONGODB_DB")
    itemadvisor_session_secret: str = Field(alias="ITEMADVISOR_SESSION_SECRET")
    itemadvisor_session_cookie_name: str = Field(alias="ITEMADVISOR_SESSION_COOKIE_NAME")
    itemadvisor_session_secure: bool = Field(alias="ITEMADVISOR_SESSION_SECURE")
    itemadvisor_manager_email: str = Field(alias="ITEMADVISOR_MANAGER_EMAIL")
    itemadvisor_manager_password: str = Field(alias="ITEMADVISOR_MANAGER_PASSWORD")
    itemadvisor_user_email: str = Field(alias="ITEMADVISOR_USER_EMAIL")
    itemadvisor_user_password: str = Field(alias="ITEMADVISOR_USER_PASSWORD")


settings = Settings()
