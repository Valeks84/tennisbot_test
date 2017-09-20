import telebot
import datetime


TOKEN = '399554838:AAHi0K7ah2skWcRJb7qaqe3NjqYMVzmnZtw'

date = str(datetime.datetime.now())
bot = telebot.TeleBot(TOKEN)
bot.send_message(-1001148320320, text="Обновление от " + date + '\n', parse_mode = 'HTML')
