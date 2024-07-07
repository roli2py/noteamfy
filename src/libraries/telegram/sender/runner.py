from telegram.ext import ApplicationBuilder
from libraries.telegram.sender import ChatManager, Chats


class Runner:

    def __init__(self, token: str, chats: Chats):
        self.__token = token
        self.__app = ApplicationBuilder().token(self.__token).build()
        self.__chats = chats
        self.__chat_manager = ChatManager(self.__chats)

    @property
    def app(self):
        return self.__app

    def __add_handlers(self):
        chat_manager_handlers = self.__chat_manager.get_handlers()
        # notifier_handlers = self.__notifier.get_handlers()
        self.__app.add_handlers(chat_manager_handlers)
        # self.__app.add_handlers(notifier_handlers)

    def start(self):
        self.__add_handlers()
        self.__app.run_polling()
