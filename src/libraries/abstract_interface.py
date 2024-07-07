from typing import Any


class AbstractInterface:

    def send(self, data: Any):
        raise NotImplementedError()

    def receive(self, data: Any):
        raise NotImplementedError()
