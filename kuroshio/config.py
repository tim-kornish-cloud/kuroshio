"""
Author: Timothy Kornish
CreatedDate: October 8 -2026
Description: set up config login credentials and token values
"""

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    database_url: str

    secret_key: SecretStr
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    reset_token_expire_minutes: int = 60

    # forgotten password email values
    mail_server: str = "localhost"
    mail_port: int = 587
    mail_username: str = ""
    mail_password: SecretStr = SecretStr("")
    mail_from: str = "noreply@example.com"
    mail_use_tls: bool = True

    frontend_url: str = "http://localhost:8000"

    # Salesforce values
    Username: str
    Password: str
    Token: str
    URL: str
    SOAP_API: str

settings = Settings()  # type: ignore[call-arg] # Loaded from .env file
