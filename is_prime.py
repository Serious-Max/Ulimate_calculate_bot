def function(update, context):
    try:
        state = context.user_data['state']
    except:
        state = 1
    if state == 1:
        update.message.reply_text('Enter is_prime(n), where n - num')
        context.user_data['state'] = 2
        return 0
    elif state == 2:
        try:
            text = update.message.text
            n = int(text.split('(')[1][:-1])
            f = False
            for i in range(2, int(n ** .5) + 1):
                if n % i == 0:
                    update.message.reply_text('NO')
                    f = True
                    break
            if not f:
                update.message.reply_text('YES')
            return -1
        except:
            update.message.reply_text('error. try again')
            return 0
