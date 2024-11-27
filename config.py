import os

from dotenv import load_dotenv
load_dotenv()


ADMIN_ID = os.environ.get('ADMIN_ID')
TOKEN = os.environ.get('TOKEN')
URL = os.environ.get('URL')