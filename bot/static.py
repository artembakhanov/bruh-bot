import os

from telebot import types

from config import TOKEN

TTOKEN = os.environ.get("t_token", TOKEN)


def START_MESSAGE(user, not_registered):
    return f"Hello, {user.first_name}! bruh" if not_registered else f"bruh... use buttons!"


DNE_MESSAGE = f"Sorry, but you are not in our databases. Please, type /start"
AUDION_MESSAGE = f"Send me your bruh audio!"
RECORDED_MESSAGE = f"Your bruh has been recorded. It will become public after verification."

COMMANDS = ["bruh", "bruh\U0001F50A", "Record my bruh\U0001F3A4"]
CANCEL = "\u274C cancel \u274C"


def COMMANDS_KEYBOARD(chat_type):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, selective=True)
    keyboard.add(*COMMANDS)
    return keyboard if chat_type == "private" else HIDE_KEYBOARD


def CANCEL_KEYBOARD(chat_type):
    keyboard = types.ReplyKeyboardMarkup(selective=True)
    keyboard.add(CANCEL)
    return keyboard if chat_type == "private" else HIDE_KEYBOARD


HIDE_KEYBOARD = types.ReplyKeyboardRemove(selective=True)
BRUH = ["bruh", "bruhh", "bruuh", "bRuh", "BRUH", "brUh", "BruH", "bbrruuhh", "bruh..."]


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
