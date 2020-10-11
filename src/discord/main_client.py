import asyncio
from typing import Optional

import discord

from src.model.config import UserObject
from src.discord.time_signal import TimeSignal


class MainClient(discord.Client):
    def __init__(self, token: str, base_id: int, config: UserObject):
        super().__init__()
        self.token: str = token
        self.base_id: int = base_id
        self.user_object = config

        self.base_channel: Optional[discord.TextChannel] = None

    def run(self):
        super().run(self.token)

    async def on_ready(self):
        guild: discord.Guild = self.guilds[0]
        self.base_channel = guild.get_channel(self.base_id)

        time_signal = TimeSignal(self.base_channel, self.user_object)
        asyncio.ensure_future(time_signal.base())

    async def on_message(self, message: discord.Message):
        if not (message.content.startswith("!url")):
            return

        await message.channel.send(self.user_object.generate_url())
