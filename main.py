import os

import telebot
from flask import Flask, request

from bot import bot
from bot.static import TTOKEN

if "webhooks" in list(os.environ.keys()):
    server = Flask(__name__)


    @server.route(f"/{TTOKEN}", methods=['POST'])
    def getMessage():
        bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
        return "!", 200


    @server.route("/")
    def webhook():
        bot.remove_webhook()
        bot.set_webhook(url=os.environ["APP_URL"] + TTOKEN)
        return "!", 200


    server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))

else:
    bot.remove_webhook()
    bot.polling()
