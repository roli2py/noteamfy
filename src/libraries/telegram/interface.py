from libraries.abstract_interface import AbstractInterface
from libraries.telegram.chats import Chats
from libraries.telegram.receiver import ReceiverIdentifier, ReceiverFilter, \
    ReceiverPreProcess, ReceiverHandler
from libraries.telegram.sender import ReceiverHandler
from telegram import Bot
from telegram.constants import ParseMode
import asyncio
from typing import Any


class Interface(AbstractInterface):

    def __init__(self, token: str, chats: Chats):
        self.__token = token
        self.__bot = Bot(self.__token)
        self.__chats = chats

    def send(self, data: Any):
        data = ReceiverHandler.handle(data)
        coroutines = []
        for chat in self.__chats.list:
            id_ = chat["id"]
            coroutine = self.__bot.send_message(
                id_, data, parse_mode=ParseMode.MARKDOWN_V2)
            coroutines.append(coroutine)

        async def send_messages():
            await asyncio.gather(*coroutines)

        asyncio.run(send_messages())

    def receive(self, data: Any):
        type_ = ReceiverIdentifier.identify(data)
        pass_ = ReceiverFilter.filter(type_)
        if not pass_:
            return None
        data = ReceiverPreProcess.process(data, type_)
        data = ReceiverHandler.handle(data)
        data = ReceiverPostProcess.process(data)
        return data
