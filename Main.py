from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler, ConversationHandler
from fp.fp import FreeProxy
import time


def start(update, context):
    update.message.reply_text(
        "temp message")
    return 1

def help(update, context):
    update.message.reply_text(
        "this is help")


def stop(update, context):
    update.message.reply_text('Stop')

def text(update, context):
    if update.message.text == '/stop':
        return ConversationHandler.END
    else:
        update.message.reply_text('Я получил сообщение ' + update.message.text)
        return 1



def main():
    while 1:
        try:
            print('start find proxy...')
            request_kwargs = {
                'proxy_url': FreeProxy(country_id=['US', 'UK']).get()
            }
            print('set proxy', request_kwargs['proxy_url'])
            updater = Updater(token='1279678359:AAHt3EhVe3daGWBgyyChxyMgtH1-FgWyQWI', use_context=True, request_kwargs=request_kwargs)  # нужен токен бота
            dp = updater.dispatcher
            main_handler = ConversationHandler(
                entry_points=[CommandHandler('start', start)],
                states = {
                    1: [MessageHandler(Filters.text, text)]
                },
                fallbacks=[CommandHandler('stop', stop)]
            )
            dp.add_handler(main_handler)
            updater.start_polling()
            updater.idle()
        except Exception as ex:
            print('error', ex)


if __name__ == '__main__':
    main()
