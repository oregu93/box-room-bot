import os
from dotenv import load_dotenv

# читать переменные среды прямо из файлов и даже из командной строки
load_dotenv()

# берем значения из файла env
TOKEN = os.getenv('BOT_TOKEN')
api_secret = os.getenv('API_SECRET')
api_key = os.getenv('API_KEY')
FAUNA_KEY = os.getenv('FAUNA_KEY')