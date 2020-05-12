def function(update, context):
    try:
        state = context.user_data['state']
    except:
        state = 1
    if state == 1:
        update.message.reply_text('Enter LCM(a, b), where a and b - numbers')
        context.user_data['state'] = 2
        return 0
    elif state == 2:
        try:
            text = update.message.text
            a = int(text.split('(')[1][:-1].split(',')[0])
            b = int(text.split('(')[1][:-1].split(',')[1])
            for i in range(max(a, b), a * b):
                if i % a == 0 and i % b == 0:
                    update.message.reply_text(i)
                    break
            return -1
        except:
            update.message.reply_text('error. try again')
            return 0