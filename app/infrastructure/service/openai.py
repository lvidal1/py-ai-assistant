import os
import openai


class OpenAI:
    def __init__(self) -> None:
        openai.organization = os.environ.get("OPENAI_ORG_ID")
        openai.api_key = os.environ.get("OPENAI_API_KEY")

    def client(self):
        return openai
