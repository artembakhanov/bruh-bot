import random

import telebot

from bot.static import *
from db.classes import User
from db.core import create_user, db_read, db_write, get_or_create

bot = telebot.TeleBot(TOKEN)


@db_read
def get_user_state(session, user_id: int):
    user = session.query(User).filter_by(id=user_id).first()
    return user.state if user is not None else DNE


@db_write
def change_user_state(session, user_id: int, new_state: int):
    user = get_or_create(session, User, id=user_id)
    user.state = new_state


@bot.message_handler(commands=['start'])
@create_user
def start_message(not_registered, m):
    bot.send_message(m.chat.id, START_MESSAGE(m.from_user, not_registered), reply_markup=COMMANDS_KEYBOARD)


@bot.message_handler(func=lambda m: m.text == commands[0])
def bruh_message(m):
    change_user_state(WAITING_FOR_AUDIO)
    bot.send_message(m.chat.id, random.choice(BRUH))


@bot.message_handler(func=lambda m: m.text == commands[1])
def bruh_audiomessage(m):
    bot.send_message(m.chat.id, AUDION_MESSAGE, reply_markup=HIDE_KEYBOARD)


@bot.message_handler(content_types=['audio'], func=lambda m: get_user_state(m.from_user.id) == WAITING_FOR_AUDIO)
def record_message(m):
    print(m)


@bot.message_handler(content_types=['audio'])
def record_message(m):
    pass


@bot.message_handler(func=lambda m: get_user_state(m.from_user.id) == DNE,
                     content_types=ALL_CONTENT_TYPES)
def dne_message(m):
    bot.send_message(m.chat.id, DNE_MESSAGE)
