import os
from dotenv import load_dotenv

load_dotenv('.env')


class Settings:
    def __init__(self):
        self.SECRET = os.getenv('SECRET')
        self.DB_NAME = os.getenv('DB_NAME')
        self.DB_HOST = os.getenv('DB_HOST')
        self.DB_PORT = os.getenv('DB_PORT')
        self.DB_USER = os.getenv('DB_USER')
        self.DB_PASSWORD = os.getenv('DB_PASSWORD')

        self.DB_URL = \
            f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/'
            # f'{self.DB_NAME}'


settings = Settings()
