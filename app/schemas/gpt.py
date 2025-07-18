from pydantic import BaseModel

class GptMessage(BaseModel):
    content: str
    reasoning: str