from typing import Any


class Handler:

    @staticmethod
    def handle(data: Any):
        name = data["name"]
        content = data["content"]
        discord_message_data = {
            "embeds": [
                {
                    "title": name,
                    "description": content,
                    # "color": 0
                }
            ]
        }
        return discord_message_data
