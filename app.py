import os
import telebot

my_secret = os.environ['KEY']
bot = telebot.TeleBot(my_secret)


@bot.message_handler(commands=['start'])
def send_bom_dia(message):
  user_name = message.from_user.first_name
  bom_dia_message = f'Bom dia, {user_name}!'
  bot.reply_to(message, bom_dia_message)


bot.polling()
