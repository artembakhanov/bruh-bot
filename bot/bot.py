import os
from time import sleep

import telebot

bot = telebot.AsyncTeleBot(os.environ["t_token"])


@bot.message_handler(commands=['hello'])
def hello_message(m):
    sleep(5)
    print("Hello world")


@bot.message_handler(commands=['hello1'])
def hello_message(m):
    print("Hello world")
