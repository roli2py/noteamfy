from typing import Any


class Handler:

    @staticmethod
    def describe(data: Any):
        type_ = data["type"]
        match type_:
            case "command":
                full_command = data["message"]["text"]
                parted_command = full_command.split(" ")
                command = parted_command[0]
                args = parted_command[1:]
                if command.startswith("/notify"):
                    if 1 <= len(args):
                        notification_type = args[0]
                        match notification_type:
                            case "task":
                                name = "Task"
                                content = "Created a task"
                            case _:
                                name = "Another type of the notification"
                                content = f"Created a {notification_type} notification"
                    else:
                        name = "Notification"
                        content = "Created a notification"
                else:
                    name = "Command"
                    content = f"Written a {command} command"
            case "entities" | "text":
                name = "Text"
                content = data["message"]["text"]
            # case "message":
            #     pass
            case _:
                name = "Unknown"
                content = "Unknown type of the update"
        return name, content

    @classmethod
    def handle(cls, data: Any):
        name, content = cls.describe(data)
        central_data = {
            "name": name,
            "content": content
        }
        return central_data
