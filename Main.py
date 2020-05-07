from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler
import time


def start(update, context):
    update.message.reply_text(
        "temp message")


def help(update, context):
    update.message.reply_text(
        "this is help")


def _time(update, context):
    update.message.reply_text(str('Текущее время: ' + time.asctime().split()[3]))


def date(update, context):
    temp = time.asctime().split()
    update.message.reply_text(str(' '.join(["Текущая дата:",
                                           temp[1],
                                           temp[2],
                                           temp[4]])))


def text(update, context):
    update.message.reply_text('Я получил сообщение ' + update.message.text)


def main():
    #request_kwargs = {
    #    'proxy_url': 'https://200.195.162.242:3128'
    #}
    updater = Updater(token='1279678359:AAHt3EhVe3daGWBgyyChxyMgtH1-FgWyQWI', use_context=True)#, request_kwargs=request_kwargs)  # нужен токен бота
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler('time', _time))
    dp.add_handler(CommandHandler('date', date))
    dp.add_handler(MessageHandler(Filters.text, text))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
