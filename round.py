from math import sin


def function(update, context):
    try:
        state = context.user_data['state']
    except:
        state = 1
    if state == 1:
        update.message.reply_text('Введите число k, которое нужно округлить, целую часть нужно отделить от дробной точкой')
        context.user_data['state'] = 2
        return 0
    elif state == 2:
        try:
            text = update.message.text
            k = int(text)
            fl = k - int(k)
            if fl >= 0.5:
                update.message.reply_text(int(k) + 1)
            else:
                update.message.reply_text(int(k))
            return -1
        except:
            update.message.reply_text('Ошибка, попробуйте снова')
            return 0