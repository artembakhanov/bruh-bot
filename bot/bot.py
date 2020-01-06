import os
from time import sleep

import telebot

from db.core import create_user

bot = telebot.TeleBot(os.environ["t_token"])


@bot.message_handler(commands=['hello'])
def hello_message(m):
    sleep(5)
    print("Hello world")


@bot.message_handler(commands=['hello1'])
def hello_message(m):
    print("Hello world1")


@bot.message_handler(commands=['start'])
@create_user
def start_message(not_registered, m):
    if not_registered:
        bot.send_message(m.chat.id, "Hello! You are new here... Welcome!")
    else:
        bot.send_message(m.chat.id, "Hello! You are already in!")
