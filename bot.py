import telebot
import time

bot_token = '1078127955:AAEpQvG8eDSMb7etCgwdaanNKfesPNkQyBY'

bot = telebot.TeleBot(token=bot_token)
@bot.message_handler(commands = ['start'])
def send_welcome(message):
    bot.reply_to(message, 'welcome! how are you doing well')

bot.polling()
