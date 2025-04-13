from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    LLM_MODEL: str = Field(description="The LLM model to use", default="gpt-4o-mini")
    OPENAI_API_KEY: str = Field(description="OpenAI API key")

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
