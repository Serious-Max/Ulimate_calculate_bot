def function(update, context):
    try:
        state = context.user_data['state']
    except:
        state = 1
    if state == 1:
        update.message.reply_text('Введите 2 числа, с которыми нужно произвести операцию, разделяя знаком действия')
        context.user_data['state'] = 2
        return 0
    elif state == 2:
        try:
            text = update.message.text
            if '+' in text:
                sign = '+'
            if '-' in text:
                sign = '-'
            if '*' in text:
                sign = '*'
            if '/' in text:
                sign = '/'
            a = int(text.split(sign)[0])
            b = int(text.split(sign)[1])
            if sign == '+':
                update.message.reply_text(str(a + b))
            if sign == '-':
                update.message.reply_text(str(a - b))
            if sign == '*':
                update.message.reply_text(str(a * b))
            if sign == '/':
                update.message.reply_text(str(a / b))
            return -1
        except:
            update.message.reply_text('Ошибка, попробуйте снова')
            return 0