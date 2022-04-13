import requests

def telegram_bot_sendtext(bot_message, token, chatid):
    
    bot_token = token
    bot_chatID = chatid
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
    