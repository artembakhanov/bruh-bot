import random

import telebot

from bot.static import *
from db.classes import User, Audio
from db.core import create_user, db_read, db_write, get_or_create

bot = telebot.TeleBot(TOKEN)


@db_read
def get_user_state(session, user_id: int):
    user = session.query(User).filter_by(id=user_id).first()
    return user.state if user is not None else DNE


@db_write
def change_user_state(session, user_id: int, new_state: int):
    user = get_or_create(session, User, id=user_id)[0]
    user.state = new_state


@db_write
def create_audio(session, message):
    audio = Audio(message.voice.file_id, message.from_user.id, verified=True)
    session.add(audio)


@db_write
def random_audio(session):
    return random.choice(session.query(Audio).filter_by(verified=True)).id


@bot.message_handler(commands=['start'])
@create_user
def start_message(not_registered, m):
    bot.send_message(m.chat.id, START_MESSAGE(m.from_user, not_registered), reply_markup=COMMANDS_KEYBOARD)


@bot.message_handler(func=lambda m: m.text == commands[0])
def bruh_message(m):
    bot.send_message(m.chat.id, random.choice(BRUH))


@bot.message_handler(func=lambda m: m.text == commands[1])
def bruh_message(m):
    bot.send_voice(m.chat.id, random_audio())


@bot.message_handler(func=lambda m: m.text == commands[2])
def bruh_audiomessage(m):
    change_user_state(m.from_user.id, WAITING_FOR_AUDIO)
    bot.send_message(m.chat.id, AUDION_MESSAGE, reply_markup=HIDE_KEYBOARD)


@bot.message_handler(content_types=['voice'], func=lambda m: get_user_state(m.from_user.id) == WAITING_FOR_AUDIO)
def record_message(m):
    create_audio(m)
    change_user_state(m.from_user.id, DEFAULT_STATE)
    bot.send_voice(m.chat.id, m.voice.file_id)


@bot.message_handler(func=lambda m: get_user_state(m.from_user.id) == DNE,
                     content_types=ALL_CONTENT_TYPES)
def dne_message(m):
    bot.send_message(m.chat.id, DNE_MESSAGE)
