import datetime
import asyncio

import discord

from src.model.config import UserObject
from src.utils.singleton import Singleton

SIGNAL_HOUR = 20


class TimeSignal(Singleton):
    """
    時報を操作するClass
    """
    def __init__(self, channel: discord.TextChannel, user_object: UserObject, timezone=9):
        """
        時報に使用する変数の初期化
        """
        self.channel = channel
        self.user_object = user_object
        self.timezone = datetime.timezone(datetime.timedelta(hours=timezone))

    async def base(self):
        """
        時報のループ処理を行う関数
        """
        while True:
            time = datetime.datetime.now(tz=self.timezone)

            if time.hour == SIGNAL_HOUR and time.minute == 0:
                await self.time_signal()

            await asyncio.sleep(50)

    async def time_signal(self):
        """
        時報を実行する関数
        """
        await self.channel.send(self.user_object.generate_url())

        await asyncio.sleep(15)
