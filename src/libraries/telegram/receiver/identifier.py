from typing import Any


class Identifier:

    @staticmethod
    def identify(data: Any):
        if "message" in data:
            message = data["message"]
            if "entities" in message:
                entities = message["entities"]
                first_entity = entities[0]
                if (first_entity["type"] == "bot_command"
                        and first_entity["offset"] == 0):
                    return "command"
                return "entities"
            if "text" in message:
                return "text"
            return "message"
        return "unknown"
