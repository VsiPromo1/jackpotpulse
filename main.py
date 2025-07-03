import telebot
import random
import time
import threading
import json
import os

TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN, parse_mode='HTML')

# далі йде весь код користувача, сюди краще вставити повну версію при необхідності

print("Бот запущено...")
bot.infinity_polling()
