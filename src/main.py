from flask import Flask, request
from libraries.discord import DiscordInterface
from libraries.telegram import TelegramInterface
from libraries.bitrix import BitrixInterface
from libraries.telegram.sender.runner import Runner as TelegramBotRunner
from libraries.telegram.sender.chats import Chats as TelegramChats
from pathlib import Path
from threading import Thread
from asyncio import set_event_loop, new_event_loop
import json
import yaml


app = Flask(__name__)

data_path = Path("data")

with open(data_path / "token.json", "rb") as token_file:
    token_dict = json.loads(token_file.read())
telegram_token = token_dict["telegram"]

with open(data_path / "chats.yaml", "rb") as chats_file:
    chats_list = yaml.load(chats_file.read(), yaml.Loader)
chats = TelegramChats(chats_list)


def start_telegram_bot(runner):
    event_loop = new_event_loop()
    set_event_loop(event_loop)
    runner.start()


telegram_bot_runner = TelegramBotRunner(telegram_token, chats)
telegram_bot = telegram_bot_runner.app.bot

Thread(target=start_telegram_bot, args=(telegram_bot_runner,)).start()

with open(data_path / "webhooks.json", "rb") as webhooks_file:
    webhooks_dict = json.loads(webhooks_file.read())
discord_url = webhooks_dict["discord"]
telegram_url = webhooks_dict["telegram"]
bitrix_url = webhooks_dict["bitrix"]
discord_interface = DiscordInterface(discord_url)
telegram_interface = TelegramInterface(telegram_url, telegram_bot, chats)
bitrix_interface = BitrixInterface(bitrix_url)


@app.post("/")
def index():
    return "API is up!"


@app.post("/notify")
def notify_with_webhook():
    body = request.json
    if "type" in request.args:
        type_ = request.args["type"]
        match type_:
            case "telegram":
                body = telegram_interface.receive(body)
            case _:
                pass
    if body is None:
        return "Webhook rejected"
    discord_interface.send(body)
    telegram_interface.send(request.json)
    # bitrix_interface.send(body)
    # if request.json["event"]["type"] == "update_column_value":
    #     event = request.json["event"]
    #     column = event["columnTitle"]
    #     task_name = event["pulseName"]
    #     status_name = event["value"]["label"]["text"]
    #     change_time = datetime.strptime(event["triggerTime"], "%Y-%m-%dT%H:%M:%S.%f%z")
    #     utc3 = timezone(timedelta(hours=3))
    #     formatted_change_time = change_time.astimezone(utc3).strftime("%d.%m.%Y %H:%M:%S")
    #     embed = {
    #         "title": "Статус задачи изменен",
    #         "description": f"{column} задачи {task_name} изменен на {status_name} в {formatted_change_time}"
    #     }
    return "Webhook proceed"

if __name__ == "__main__":
    app.run("0.0.0.0")
