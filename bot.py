import os
import telebot

bot = telebot.TeleBot(os.environ.get('BOT_TOKEN'));

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Привет, отправь мне любое сообщение, и я посчитаю количество символов в нем (команды /start или /hello не считаются)!")

@bot.message_handler(func=lambda message: True, content_types=['text'])
def count_characters(message):
    character_count = len(message.text)
    bot.reply_to(message, f"В вашем сообщении {character_count} символов.")

bot.infinity_polling()