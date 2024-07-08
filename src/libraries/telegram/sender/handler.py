from typing import Any


class Handler:

    @staticmethod
    def handle(data: Any):
        name = data["name"]
        content = data["content"]
        telegram_message_data = (f"*{name}*\n"
                                 "\n"
                                 f"{content}")
        return telegram_message_data
