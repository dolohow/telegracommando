import argparse
import configparser
import logging
import os
import pathlib
import re

from telegram.ext import Updater, MessageHandler, Filters

PARSER = argparse.ArgumentParser(
    description='Torrent downloading progress on Telegram')
PARSER.add_argument(
    '--config',
    action='store',
    default='telegracommando.ini',
    help='Path to configuration file',
    metavar='PATH',
    type=pathlib.Path,
)
ARGS = PARSER.parse_args()

CONFIG = configparser.ConfigParser()
CONFIG.read(ARGS.config)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO)

logger = logging.getLogger(__name__)

VALID_ARGUMENT = re.compile("^[a-zA-Z0-9]+$")


def cmd(update, context):
    msg = update.message.text.split(' ')
    msg[0] = msg[0].split('@')[0]
    msg[0] = msg[0][1:]
    for m in msg:
        if not bool(VALID_ARGUMENT.match(m)):
            update.message.reply_text(
                "Command may only consist of letters and numbers", quote=False)
            return
    path = f"commands.d/{msg[0]}"
    if not os.path.exists(path):
        update.message.reply_text("No such command", quote=False)
        return

    reply = os.popen(f"{path} {' '.join(msg[1:])}").read()
    if reply:
        update.message.reply_text(f"`{reply}`",
                                  quote=False,
                                  parse_mode="Markdown")
    else:
        update.message.reply_text("Command returned nothing", quote=False)


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
