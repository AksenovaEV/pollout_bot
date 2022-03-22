import os
from dotenv import load_dotenv

try:
    env_path = '.env'
    load_dotenv(dotenv_path=env_path)
except:
    pass


class Config:
    TOKEN = os.environ.get('TOKEN')