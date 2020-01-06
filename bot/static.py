import os

from telebot import types

TOKEN = os.environ["t_token"]


def START_MESSAGE(user, not_registered):
    return f"Hello, {user.first_name}! bruh" if not_registered else f"bruh"


DNE_MESSAGE = f"Sorry, but you are not in our databases. Please, type /start"

commands = ["bruh", "bruh\U0001F50A", "Record my bruh\U0001F3A4"]

COMMANDS_KEYBOARD = types.ReplyKeyboardMarkup(row_width=2)
COMMANDS_KEYBOARD.add(*commands)

HIDE_KEYBOARD = types.ReplyKeyboardRemove()
BRUH = ["bruh", "bruhh", "bruuh", "bRuh", "BRUH"]

DNE = -1
DEFAULT_STATE = 0
WAITING_FOR_AUDIO = 1
