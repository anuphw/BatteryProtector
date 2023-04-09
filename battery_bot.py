#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot

from threading import Thread
from time import sleep
from datetime import datetime

API_TOKEN = 'TOKEN'
MY_CHAT_ID = 'CHAT_ID'
bot = telebot.TeleBot(API_TOKEN)

bat_cap = "/sys/class/power_supply/BAT0/capacity"
bat_status = "/sys/class/power_supply/BAT0/status"
HIGH_LEVEL = 80
LOW_LEVEL = 20
TIME_DELAY = 60*5 # 5 minutes frequency of checking battery status


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    print(message)
    update_power()
    bot.reply_to(message, message.text)

def update_power():
    level =  int(open(bat_cap).readline().strip())
    status = open(bat_status).readline().strip()
    dt = datetime.strftime( datetime.now(), "%Y-%m-%d %H:%M:%S")
    if status == 'Charging' and level > HIGH_LEVEL:
        msg = f"{dt} **Stop Charging**, Battery is {level}% full"
        bot.send_message(chat_id=MY_CHAT_ID, text=msg)
    elif status == 'Discharging' and level < LOW_LEVEL:
        msg = f"{dt} **Connect** charger, battery is only {level}% remaining"
        bot.send_message(chat_id=MY_CHAT_ID, text=msg)
    sleep(TIME_DELAY)
    t = Thread(target=update_power)
    t.start()

mythread = Thread(target=update_power)
mythread.start()
bot.infinity_polling()
