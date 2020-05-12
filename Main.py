from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler, ConversationHandler
from fp.fp import FreeProxy
from telegram import ReplyKeyboardMarkup
import os
import importlib


def start(update, context):
    context.user_data['dir'] = 'files'
    context.user_data['func_work'] = False
    dirs = os.listdir('files')
    temp = [[i] for i in dirs]
    update.message.reply_text('Select dir. /help to help',
                              reply_markup=ReplyKeyboardMarkup(temp, one_time_keyboard=True))
    return 1


def help(update, context):
    update.message.reply_text(
        "Select the desired function. Click on it. "
        "The function is executed once. "
        "After that use the keyboard. /stop to stop, /help to help(this messange)"
        "/start to restart (if you have problems)")


def stop(update, context):
    update.message.reply_text('Stop')


def make_answer(way):
    with open(way, mode='rt') as file:
        temp = file.read()
    module = importlib.import_module(temp)
    func = module.function
    return func


def options(dir, action):
    print(dir, action)
    if action == 'Back':
        if dir != 'files':
            tdir = '/'.join(dir.split('/')[:-1])
        else:
            tdir = dir
    else:
        tdir = dir + '/' + action
    if os.path.isfile(tdir):
        return dir, True, os.listdir(dir), tdir
    else:
        return tdir, False, os.listdir(tdir), ''


def text(update, context, skip=False):
    if update.message.text == '/stop':
        return ConversationHandler.END
    if update.message.text == '/help':
        help(update, context)
        return 1
    elif context.user_data['func_work'] == True:
        answ = context.user_data['func'](update, context)
        if answ == -1:
            context.user_data['func_work'] = False
            context.user_data['func'] = 0
            context.user_data['state'] = 1
            print('skip 1')
            text(update, context, skip=True)
        else:
            return 1
    if skip == True:
        print('skip 2')
        dirs = os.listdir(context.user_data['dirs'])
        temp = [[i] for i in dirs]
        update.message.reply_text('Select dir',
                                  reply_markup=ReplyKeyboardMarkup(temp, one_time_keyboard=True))
        return 1
    else:
        text_t = update.message.text
        try:
            context.user_data['dir'], need_open, dirs, open_dir = options(context.user_data['dir'], text_t)
            print(1)
            if need_open:
                print(2)
                context.user_data['func'] = make_answer(open_dir)
                context.user_data['func_work'] = True
                context.user_data['state'] = 1
                text(update, context)
            else:
                temp = [[i] for i in dirs]
                temp.append(['Back'])
                update.message.reply_text('Select dir',
                                          reply_markup=ReplyKeyboardMarkup(temp, one_time_keyboard=True))

        except Exception as ex:
            print(ex, type(ex))
            update.message.reply_text('Error. Please, try again')
        return 1


def main():
    while 1:
        try:
            print('start find proxy...')

            #request_kwargs = {
            #    'proxy_url': FreeProxy().get()
            #}
            #print('set proxy', request_kwargs['proxy_url'])
            updater = Updater(token='', use_context=True)#,
                              #request_kwargs=request_kwargs)  # нужен токен бота
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
