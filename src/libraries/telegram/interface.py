from libraries.abstract_interface import AbstractInterface
from libraries.telegram.sender import Chats
from libraries.telegram.receiver import ReceiverIdentifier, ReceiverFilter, \
    ReceiverPreProcess, ReceiverHandler, ReceiverPostProcess
from telegram import Bot
import asyncio
from typing import Any


class Interface(AbstractInterface):

    def __init__(self, url: str, bot: Bot, chats: Chats):
        self.__url = url
        self.__bot = bot
        self.__chats = chats

    def send(self, data: Any):
        name = data["name"]
        content = data["content"]
        text = f"{name}: {content}"
        for id_, _ in self.__chats:
            asyncio.run(self.__bot.send_message(id_, text))

    def receive(self, data: Any):
        type_ = ReceiverIdentifier.identify(data)
        pass_ = ReceiverFilter.filter(type_)
        if not pass_:
            return None
        data = ReceiverPreProcess.process(data, type_)
        data = ReceiverHandler.handle(data)
        data = ReceiverPostProcess.process(data)
        return data
