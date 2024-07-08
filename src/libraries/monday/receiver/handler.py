from datetime import datetime, timezone, timedelta
from typing import Any


class Handler:

    @staticmethod
    def handle(data: Any):
        if data["event"]["type"] == "update_column_value":
            event = data["event"]
            column = event["columnTitle"]
            task_name = event["pulseName"]
            status_name = event["value"]["label"]["text"]
            change_time = datetime.strptime(event["triggerTime"], "%Y-%m-%dT%H:%M:%S.%f%z")
            utc3 = timezone(timedelta(hours=3))
            formatted_change_time = change_time.astimezone(utc3).strftime("%d.%m.%Y %H:%M:%S")
            central_data = {
                "name": "Статус задачи изменен",
                "content": f"{column} задачи {task_name} изменен на {status_name} в {formatted_change_time}"
            }
            return central_data
