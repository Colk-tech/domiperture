import asyncio

import discord

from src.model.config import UserObject


class MainClient(discord.Client):
    def __init__(self, token: str, config: UserObject):
        super().__init__()
        self.token: str = token
        self.user_object = config

    def run(self):
        super().run(self.token)

    async def on_ready(self):
        pass

    async def on_message(self, message: discord.Message):
        if not (message.content.startswith("!url")):
            return

        await message.channel.send(self.user_object.generate_url())
