import os

from telebot import types

TOKEN = os.environ["t_token"]


def START_MESSAGE(user, not_registered):
    return f"Hello, {user.first_name}! bruh" if not_registered else f"bruh... use buttons!"


DNE_MESSAGE = f"Sorry, but you are not in our databases. Please, type /start"
AUDION_MESSAGE = f"Send me your bruh audio!"
RECORDED_MESSAGE = f"Your bruh has been recorded. It will be made (become) public after verification."

commands = ["bruh", "bruh\U0001F50A", "Record my bruh\U0001F3A4"]

COMMANDS_KEYBOARD = types.ReplyKeyboardMarkup(row_width=2, selective=True)
COMMANDS_KEYBOARD.add(*commands)

HIDE_KEYBOARD = types.ReplyKeyboardRemove()
BRUH = ["bruh", "bruhh", "bruuh", "bRuh", "BRUH"]


def VERIFY_KEYBOARD(audio):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("Verify", callback_data=f"ver_{audio}"))
    keyboard.add(types.InlineKeyboardButton("Remove", callback_data=f"rem_{audio}"))
    return keyboard


DNE = -1
DEFAULT_STATE = 0
WAITING_FOR_AUDIO = 1

ALL_CONTENT_TYPES = ['audio', 'video', 'document', 'text', 'location', 'contact', 'sticker']

ADMIN_GROUP = -340026947
