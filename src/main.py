from flask import Flask, request
from libraries.discord import DiscordInterface
from libraries.telegram import TelegramInterface
from libraries.bitrix import BitrixInterface
from libraries.monday import MondayInterface
from libraries.telegram.chats import Chats as TelegramChats
from pathlib import Path
import json
import yaml


app = Flask(__name__)

data_path = Path("data")

with open(data_path / "tokens.json", "rb") as token_file:
    token_dict = json.loads(token_file.read())
telegram_token = token_dict["telegram"]

with open(data_path / "chats.yaml", "rb") as chats_file:
    chats_list = yaml.load(chats_file.read(), yaml.Loader)
chats = TelegramChats(chats_list)

with open(data_path / "webhooks.json", "rb") as webhooks_file:
    webhooks_dict = json.loads(webhooks_file.read())
discord_url = webhooks_dict["discord"]
bitrix_url = webhooks_dict["bitrix"]
discord_interface = DiscordInterface(discord_url)
telegram_interface = TelegramInterface(telegram_token, chats)
bitrix_interface = BitrixInterface(bitrix_url)
monday_interface = MondayInterface()

sources = {
    "telegram": telegram_interface,
    "discord": discord_interface,
    # "bitrix": bitrix_interface,
    # "monday": monday_interface,
}


@app.get("/")
def index():
    return "API is up!"


@app.post("/notify")
def notify_with_webhook():
    body = request.json
    source = None
    if "source" in request.args:
        source = request.args["source"]
        for source_name, obj in sources.items():
            if source_name == source:
                body = obj.receive(body)
                break
    if body is None:
        return "Webhook rejected"
    for source_name, obj in sources.items():
        if source_name != source:
            obj.send(body)
    return "Webhook proceed"


if __name__ == "__main__":
    app.run("0.0.0.0")
