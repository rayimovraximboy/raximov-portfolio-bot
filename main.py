import telebot
import os
from dotenv import load_dotenv, main

load_dotenv(dotenv_path=".env.txt")

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def start(message):
    portfolio_text = (
        "Assalomu alaykum!  "
        "Mening portfoli botimga xush kelibsiz: "
        "Ism-familiyam: Rayimov Raximboy "
        "Telefon: +998 91 987 04 11 "
        "Gmail: rayimov.raximboy2010@gmail.com "
        "Hozirda **Python** dasturlash tilini o'rganyapman."
        "Men hozirda 23-maktab, 10-sinfda o'qiyman."
    )
    # Xabarni foydalanuvchiga yuborish:
    bot.send_message(message.chat.id, portfolio_text)

@bot.message_handler(commands=['help'])
def help_command(message):
    help_text = (
        "Yordam bo'limi. \n"
        "Bu bot Rayimov Raximboyning shaxsiy portfolio boti hisoblanadi. "
        "Botdan foydalanish uchun quyidagi buyruqlarni yuborishingiz mumkin: "
        "/start - Botni boshlash va men haqimda ma'lumot olish: "
        "/help - Bot qanday ishlashi haqida yordam matnini ko'rish. "
        "Agar savollaringiz bo'lsa, yuqoridagi telefon raqam yoki gmail orqali bog'lanishingiz mumkin."
    )
    bot.reply_to(message, help_text)


bot.infinity_polling()