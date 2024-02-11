from openai import OpenAI

from src.config import OPENAI_ORG, OPENAI_API_KEY


openai_client = OpenAI(
    organization=OPENAI_ORG,
    api_key=OPENAI_API_KEY,
)
