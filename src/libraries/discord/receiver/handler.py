from typing import Any


class Handler:

    def handle(self, data: Any):
        name = data["title"]
        content = data["content"]
        central_data = {
            "name": name,
            "content": content
        }
        return central_data
