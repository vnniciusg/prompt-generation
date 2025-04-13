from typing import Optional

from langchain_openai import ChatOpenAI


class LLMService:
    _instance: Optional["LLMService"] = None
    _llm: Optional[ChatOpenAI] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LLMService, cls).__new__(cls)
        return cls._instance

    def initialize(self, temperature: float = 0, **kwargs) -> None:
        if self._llm is None:
            from src.config.settings import Settings

            settings = Settings()
            self._llm = ChatOpenAI(
                model=settings.LLM_MODEL,
                api_key=settings.OPENAI_API_KEY,
                temperature=temperature,
                **kwargs,
            )

    def get_llm(self) -> ChatOpenAI:
        if self._llm is None:
            self.initialize()
        return self._llm

    def bind_tools(self, tools: list) -> ChatOpenAI:
        return self.get_llm().bind_tools(tools)
