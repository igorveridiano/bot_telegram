from telegram.ext import Updater, Filters
from telegram.ext import CommandHandler, MessageHandler

updater = Updater(token="851095270:AAGYsUcw3zQ-iOmhPBE5A4EogpAXeBciZPA")
dispatcher = updater.dispatcher

def start(bot, update):

    msg = "Welcome to Filmes Bot"

    bot.send_message(
        chat_id=update.message.chat_id,
        text=msg
    )

def echo(bot, update):

    msg = update.message.text

    if msg.lower().__eq__("bom dia"):
        bot.send_message(
            chat_id=update.message.chat_id,
            text="Bom dia!")

    elif msg.lower().__eq__("boa noite"):
        bot.send_message(
            chat_id=update.message.chat_id,
            text="Boa noite!")

    elif msg.lower().__eq__("boa tarde"):
        bot.send_message(
            chat_id=update.message.chat_id,
            text="Boa tarde!")

    elif msg.lower().__eq__("oi") or msg.lower().__eq__("ola") or msg.lower().__eq__("olá") or msg.lower().__eq__("hi"):
        bot.send_message(
            chat_id=update.message.chat_id,
            text="Olá, precisa de ajuda!")

start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text, echo)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)

updater.start_polling()
updater.idle()