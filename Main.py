from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler, ConversationHandler
from fp.fp import FreeProxy
from telegram import ReplyKeyboardMarkup
import os


def start(update, context):
    context.user_data['dir'] = 'files'
    return 1


def help(update, context):
    update.message.reply_text(
        "this is help")


def stop(update, context):
    update.message.reply_text('Stop')


def make_answer():
    pass


def options(dir, action):
    if action == 'Back':
        tdir = '/'.join(dir.split('/')[:-1])
    else:
        tdir = dir + '/' + action
    if os.path.isfile(tdir):
        return dir, True, os.listdir(dir)
    else:
        return tdir, False, os.listdir(tdir)


def text(update, context):
    if update.message.text == '/stop':
        return ConversationHandler.END
    elif update.message.text == 'update 228qwertychelik':
        # make_answer(update=True)
        update.message.reply_text('Update... done')
        return 1
    else:
        text = update.message.text
        print(text)
        try:
            context.user_data['dir'], need_open, dirs = options(context.user_data['dir'], text)
            if need_open:
                pass
            else:
                print([[i] for i in dirs], [[i] for i in dirs].append(['Back']), context.user_data['dir'])
                temp = [[i] for i in dirs]
                temp.append(['Back'])
                update.message.reply_text('Select dir',
                                          reply_markup=ReplyKeyboardMarkup(temp, one_time_keyboard=False))

        except Exception as ex:
            print(ex, ex.with_traceback())
            update.message.reply_text('Error. Please, try again')
        return 1


def main():
    while 1:
        try:
            print('start find proxy...')

            request_kwargs = {
                'proxy_url': FreeProxy(country_id=['US', 'UK']).get()
            }
            print('set proxy', request_kwargs['proxy_url'])
            updater = Updater(token='1279678359:AAHt3EhVe3daGWBgyyChxyMgtH1-FgWyQWI', use_context=True,
                              request_kwargs=request_kwargs)  # нужен токен бота
            dp = updater.dispatcher
            main_handler = ConversationHandler(
                entry_points=[CommandHandler('start', start)],
                states={
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
