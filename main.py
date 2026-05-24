import telebot
from telebot import types
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env.txt")

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    text = "Assalom alaykum, meni portfolio botimizga xush kelibsiz."
    keyboard = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("About me")
    btn2 = types.KeyboardButton("Contact")
    btn3 = types.KeyboardButton("Skills")
    btn4 = types.KeyboardButton("Projects")
    keyboard.add(btn1, btn2)
    keyboard.add(btn3, btn4)
    bot.send_message(message.chat.id, text, reply_markup=keyboard)

# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     if message.text == "About me":
#         bot.send_message(message.chat.id, "Men Rayimov Raximboy. \n Men hozirda Python dasturlash tilini o'rganmoqdaman.")
#     elif message.text == "Contact":
#         bot.send_message(message.chat.id, "Bu qism tez orada qo'shiladi")

@bot.message_handler(func=lambda message: message.text == "About me")
def aboutme_handler(message):
    text = "Men Rayimov Raximboy. Hozirda Python dasturlash tilini o'rganmoqdaman."
    bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda message: message.text == "Contact")
def contact_handler(message):
    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Telegram", url="https://t.me/Rakhimoff_JR")
    btn2 = types.InlineKeyboardButton("Linkedin", url="https://www.linkedin.com/in/raximboy-rayimov")
    keyboard.add(btn1, btn2)
    text = "Men bilan bog'lanish uchun pastdagi linklarga bosing"
    
    bot.send_message(message.chat.id, text, reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "Skills")
def skills_handler(message):
    bot.send_message(message.chat.id, "Mening ko'nikmalarim: Python dasturlash tili va Telebot kutubxonasi  va  "
    " Git hamda GitHub tizimlaridan foydalana olaman.")

@bot.message_handler(func=lambda message: message.text == "Projects")
def projects_handler(message):
    bot.send_message(message.chat.id, "1. Portfolio Bot - Men haqimdagi ma'lumotlarni, ko'nikmalarimni va loyihalarimni ulashuvchi interaktiv bot. "
            "2. Lotin-Kirill Translit Bot - Foydalanuvchi yuborgan matnni Lotin alifbosidan Kirillga va Kirill alifbosidan Lotinga bir zumda o'tkazib beruvchi foydali bot.")

bot.infinity_polling()

bot.delete_webhook(drop_pending_updates=True)

