from transliterate import to_cyrillic, to_latin
import telebot
TOKEN = '2135580486:AAEwjFnLGPQzccEZXMvRkDtRa8fOzJgVEAY'
bot = telebot.TeleBot(TOKEN, parse_mode = None)
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Assalomu aleykum! \n Matn kiriting:")
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    if msg.isascii():
        ans = to_cyrillic(msg)
    else:ans = to_latin(msg)
    bot.reply_to(message, ans)
bot.polling()

while True:
    text = input()
    if text.isascii():
        print(to_cyrillic(text))
    else: print(to_latin(text))