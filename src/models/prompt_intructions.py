from pydantic import BaseModel


class PromptInstructions(BaseModel):
    """Instructions on how to prompt the LLM."""

    objective: str
    variables: list[str]
    constraints: list[str]
    requirements: list[str]
