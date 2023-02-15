# coding: utf8
from pydantic import BaseSettings, SecretStr
import json


class Settings(BaseSettings):
    bot_token: SecretStr

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


config = Settings()