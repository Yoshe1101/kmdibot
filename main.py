from curses.panel import bottom_panel
from tkinter import BOTH
from search_cita import get_cita
from telegram_integration import telegram_bot_sendtext
import json


with open('/Users/joseba/Documents/json_data.json') as json_file:
    data = json.load(json_file)

token = data['keys']['telegram_token']
chatid = data['keys']['telegram_chat_id']
id = data['keys']['web_id']
cd = data['keys']['web_cd']
check = False

while check == False:
    check, result = get_cita(id , cd)
    print(result)

bot_message = result
telegram_bot_sendtext(bot_message, token, chatid)
