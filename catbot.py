#!/usr/bin/env python3

import os
import random
import requests
import telebot

token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)
url = "https://catoverflow.com/api/query"

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/cat":
        try:
            text = get_cat()
        except:
            text = "can't get a cat for you, sorry. :("

        bot.send_message(message.from_user.id, text)

    else:
        bot.send_message(message.from_user.id, "i have only one command: /cat")

def get_cat():
    offset = random.randint(1, 369)
    timeout = 3
    params = {'limit': 1, 'offset': offset}
    response = requests.get(url,
                            params=params,
                            timeout=timeout)
    response.raise_for_status()
    return response.content
        
bot.polling(none_stop=True, interval=0)
