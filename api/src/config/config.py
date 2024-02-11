import os

from dotenv import load_dotenv

HERE = os.path.dirname(__file__)

load_dotenv(dotenv_path=os.path.join(HERE, '.env'))


OPENAI_ORG = os.getenv('OPENAI_ORG')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
