from math import sqrt


def function(update, context):
    try:
        state = context.user_data['state']
    except:
        state = 1
    if state == 1:
        update.message.reply_text('Введите число у которого нужно взять квадртный корень')
        context.user_data['state'] = 2
        return 0
    elif state == 2:
        try:
            text = update.message.text
            n = int(text)
            update.message.reply_text(sqrt(n))
            return -1
        except:
            update.message.reply_text('Ошибка, попробуйте снова')
            return 0
