import os

import telebot
from flask import Flask, request

from bot import bot
from bot.static import TOKEN

if "webhooks" in list(os.environ.keys()):
    server = Flask(__name__)


    @server.route(f"/{TOKEN}", methods=['POST'])
    def getMessage():
        bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
        return "!", 200


    @server.route("/")
    def webhook():
        bot.remove_webhook()
        bot.set_webhook(url=os.environ["APP_URL"] + TOKEN)
        return "!", 200


    server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))

else:
    bot.remove_webhook()
    bot.polling()
