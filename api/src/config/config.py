import os

from dotenv import load_dotenv

from src.utils import get_project_root

ROOT = get_project_root()

load_dotenv(dotenv_path=os.path.join(ROOT, '.env'))


OPENAI_ORG = os.getenv('OPENAI_ORG')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


print(OPENAI_ORG, OPENAI_API_KEY)
