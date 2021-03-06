import telebot
from telebot import TeleBot
from config import Config

bot: TeleBot = telebot.TeleBot(Config.TOKEN, parse_mode='HTML')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
