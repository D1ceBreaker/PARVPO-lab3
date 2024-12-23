import os

from pydantic_settings import BaseSettings


class Setting(BaseSettings):
    db_url = os.environ.get("DATABASE_URL")
    db_echo: bool = False
    #db_echo: bool = True


settings = Setting()