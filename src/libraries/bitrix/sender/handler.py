from typing import Any


class Handler:

    @staticmethod
    def handle(data: Any):
        name = data["name"]
        content = data["content"]
        bitrix_lead_data = {
            "fields": {
                "TITLE": name,
                "COMMENTS": content
            }
        }
        return bitrix_lead_data
