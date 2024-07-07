from src.libraries.abstract_interface import AbstractInterface
from src.libraries.discord.sender.pre_process import PreProcess
from src.libraries.discord.sender.handler import Handler
from src.libraries.discord.sender.post_process import PostProcess
import httpx
from typing import Any


class Interface(AbstractInterface):

    def __init__(self, url: str):
        self.__url = url

    def send(self, data: Any):
        data = PreProcess.process(data)
        data = Handler.handle(data)
        data = PostProcess.process(data)

        httpx.post(self.__url, json=data)

    def receive(self, data: Any):
        pass

