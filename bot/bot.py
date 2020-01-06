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
    audio = Audio(message.voice.file_id, message.from_user.id)
    session.add(audio)
    return audio.id


@db_write
def random_audio(session):
    return random.choice(session.query(Audio).filter_by(verified=True).all()).id


@db_write
def verify_audio(session, audio_id, verified=True):
    audio = session.query(Audio).filter_by(id=audio_id).first()
    audio.verified = verified
    return audio


@bot.message_handler(commands=['start'])
@create_user
def start_message(not_registered, m):
    bot.send_message(m.chat.id, START_MESSAGE(m.from_user, not_registered), reply_markup=COMMANDS_KEYBOARD(m.chat.type))


@bot.message_handler(func=lambda m: m.text == COMMANDS[0])
def bruh_message(m):
    bot.send_message(m.chat.id, random.choice(BRUH))


@bot.message_handler(commands=['bruht'])
def bruh_message(m):
    bot.send_message(m.chat.id, random.choice(BRUH))


@bot.message_handler(func=lambda m: m.text == COMMANDS[1])
def bruh_audiomessage(m):
    bot.send_voice(m.chat.id, random_audio())


@bot.message_handler(commands=['bruh'])
def bruh_audiomessage(m):
    bot.send_voice(m.chat.id, random_audio())


@bot.message_handler(func=lambda m: m.text == COMMANDS[2])
@create_user
def record_audio_message(not_registered, m):
    change_user_state(m.from_user.id, WAITING_FOR_AUDIO)
    bot.send_message(m.chat.id, AUDION_MESSAGE, reply_markup=HIDE_KEYBOARD)


def send_for_verification(audio_id):
    bot.send_voice(ADMIN_GROUP, audio_id, "Verify, please", reply_markup=VERIFY_KEYBOARD(audio_id))


@bot.message_handler(content_types=['voice'], func=lambda m: get_user_state(m.from_user.id) == WAITING_FOR_AUDIO)
def recorded_audio_message(m):
    audio_id = create_audio(m)
    send_for_verification(audio_id)
    change_user_state(m.from_user.id, DEFAULT_STATE)
    bot.send_message(m.chat.id, RECORDED_MESSAGE, reply_markup=COMMANDS_KEYBOARD(m.chat.type))


@bot.message_handler(func=lambda m: get_user_state(m.from_user.id) == DNE,
                     content_types=ALL_CONTENT_TYPES)
def dne_message(m):
    bot.send_message(m.chat.id, DNE_MESSAGE)


@bot.callback_query_handler(func=lambda call: call.data[0:4] == "ver_")
def verify(call):
    audio_id = call.data[4:]
    audio = verify_audio(audio_id)
    bot.edit_message_caption("Verified!", chat_id=call.message.chat.id, message_id=call.message.message_id,
                             reply_markup=VERIFY_KEYBOARD(audio_id))
    bot.send_voice(audio.user_id, audio.id, caption=f"Your audio *{audio.id[:4]}..{audio_id[-4:]}* has been approved!",
                   parse_mode="markdown")


@bot.callback_query_handler(func=lambda call: call.data[0:4] == "rem_")
def remove(call):
    audio_id = call.data[4:]
    audio = verify_audio(audio_id, False)
    bot.edit_message_caption("Removed.", chat_id=call.message.chat.id, message_id=call.message.message_id,
                             reply_markup=VERIFY_KEYBOARD(audio_id))
    bot.send_voice(audio.user_id, audio.id,
                   caption=f"Unfortunately, your bruh *{audio.id[:4]}..{audio_id[-4:]}* has not been approved. Try again.",
                   parse_mode="markdown")
