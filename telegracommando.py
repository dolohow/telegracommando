import configparser
import logging
import os

from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters

CONFIG = configparser.ConfigParser()
CONFIG.read("telegracommando.ini")

args = parser.parse_args()

logging.basicConfig(
    filename="telegracommando.log",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO)

logger = logging.getLogger(__name__)


def cmd(update, context):
    path = f"commands.d{update.message.text}"
    if not os.path.exists(path):
        update.message.reply_text("No such command", quote=False)
        return
    reply = os.popen(path).read()
    update.message.reply_text(f"`{reply}`", quote=False, parse_mode="Markdown")


def main():
    updater = Updater(CONFIG["Telegram"]["bot_token"], use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(
        MessageHandler(
            Filters.chat(CONFIG.getint("Telegram", "chat_id")) & Filters.text
            & Filters.command, cmd))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
