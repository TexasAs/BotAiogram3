from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.environ.get('HOST')
DB_USER = os.environ.get('USER')
DB_PASS = os.environ.get('PASSWORD')
DB_NAME = os.environ.get('DB_NAME')
DB_PORT = os.environ.get('PORT')