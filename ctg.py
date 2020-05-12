from math import sin, cos


def function(update, context):
    try:
        state = context.user_data['state']
    except:
        state = 1
    if state == 1:
        update.message.reply_text('Введите число, у которого нужно посчитать котангенс')
        context.user_data['state'] = 2
        return 0
    elif state == 2:
        try:
            text = update.message.text
            n = int(text)
            update.message.reply_text(cos(n) / sin(n))
            return -1
        except:
            update.message.reply_text('Ошибка, попробуйте снова')
            return 0
