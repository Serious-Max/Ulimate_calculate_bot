def function(update, context):
    try:
        state = context.user_data['state']
    except:
        state = 1
    if state == 1:
        update.message.reply_text('Enter GCF(a, b), where a and b - numbers')
        context.user_data['state'] = 2
        return 0
    elif state == 2:
        try:
            text = update.message.text
            a = int(text.split('(')[1][:-1].split(',')[0])
            b = int(text.split('(')[1][:-1].split(',')[1])
            k = 1
            for i in range(2, min(a, b)):
                if a % i == 0 and b % i == 0:
                    k = i
            update.message.reply_text(k)
            return -1
        except:
            update.message.reply_text('error. try again')
            return 0