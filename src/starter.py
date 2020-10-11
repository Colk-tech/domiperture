import os

from src.discord.main_client import MainClient
from src.model.config import UserObject
from src.utils.environ_getter import environ_getter


def start():
    discord_token: str = environ_getter("DISCORD_TOKEN", "DISCORD_TOKENが設定されていません。")

    url_template = environ_getter("URL_TEMPLATE", "URL_TEMPLATEが設定されていません。")
    building = environ_getter("USER_BUILDING", "USER_BUILDINGが設定されていません。")
    room_number = environ_getter("USER_ROOM_NUMBER", "USER_ROOM_NUMBERが設定されていません。")
    name = environ_getter("USER_NAME", "USER_NAMEが設定されていません。")
    base_id = int(environ_getter("DISCORD_BASE_CHANNEL", "DISCORD_BASE_CHANNELが設定されていません。"))

    user_config = UserObject(url_template, building, room_number, name)

    discord_client = MainClient(discord_token, base_id, user_config)
    discord_client.run()
