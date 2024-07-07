from libraries.telegram.receiver.identifier import Identifier
from copy import deepcopy
from typing import Any


class PreProcess:

    @staticmethod
    def process(data: Any, type_: str):
        mod_data = deepcopy(data)
        mod_data["type"] = type_
        return mod_data
