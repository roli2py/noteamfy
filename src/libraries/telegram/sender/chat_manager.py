from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from libraries.telegram.sender.chats import Chats


class ChatManager:

    def __init__(self, chats: Chats):
        self.__chats = chats

    async def __set_chat(self, update: Update, ctx: ContextTypes.DEFAULT_TYPE):
        chat = update.effective_chat
        self.__chats.list.append({"id": chat.id, "name": chat.title})

    async def __remove_chat(
            self,
            update: Update,
            ctx: ContextTypes.DEFAULT_TYPE
    ):
        chat = update.effective_chat
        self.__chats.list = [
            chat_item for chat_item in self.__chats.list if chat_item["id"] != chat.id
        ]

    def get_handlers(self):
        handlers = (
            CommandHandler("set_chat", self.__set_chat),
            CommandHandler("remove_chat", self.__remove_chat),
        )
        return handlers
