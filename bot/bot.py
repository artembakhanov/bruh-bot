import os

import telebot

from bot.static import *
from db.core import create_user

bot = telebot.TeleBot(os.environ["t_token"])


@bot.message_handler(commands=['start'])
@create_user
def start_message(not_registered, m):
    bot.send_message(m.chat.id, START_MESSAGE(m.from_user, not_registered), reply_markup=COMMANDS_KEYBOARD)
