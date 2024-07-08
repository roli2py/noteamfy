from libraries.abstract_interface import AbstractInterface
from libraries.monday.receiver import ReceiverHandler
from typing import Any


class Interface(AbstractInterface):

    def send(self, data: Any):
        pass

    def receive(self, data: Any):
        data = ReceiverHandler.handle(data)
        return data
