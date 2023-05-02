import telebot
from telebot import types
import requests
import json
from bs4 import BeautifulSoup as b
import random

bot = telebot.TeleBot('5837141203:AAF129bldHWzILHiDBSThSTWpPNxnx39Z4k')
API = 'ecfb531b4ff8cfc5fd0e2fc28ce1488b'
# URL = 'https://www.anekdot.ru/best/anekdot/0502/'

# def parser(url):
#     r = requests.get(url)
#     soup = b(r.text, 'html.parser')
#     anekdots = soup.find_all('div', class_='text')
#     return [c.text for c in anekdots]

# list_of_joks = parser(URL)
# random.shuffle(list_of_joks)

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Здарова {message.from_user.first_name}'
    bot.send_message(message.chat.id, mess)

@bot.message_handler(commands=['че?'])
def che(message):
    bot.send_message(message.chat.id, "Все першке мээн, ты же меня знаешь бро))")

@bot.message_handler(commands=['бро'])
def bro(message):
    bot.send_message(message.chat.id, "Бро, нига, гангста щеет мэээн))")

@bot.message_handler(commands=['дерьмо'])
def bro(message):
    bot.send_message(message.chat.id, "Эй нига, ты где здесь дерьмо увидел??? Ну разок посрал в гараже, че теперь заебывать меня всю жизнь будешь??)")

@bot.message_handler(commands=['dj'])
def dj(message):
    bot.send_message(message.chat.id, "Бро, дай трэчок свести, ты же меня знаешь я не обосрусь))")

@bot.message_handler(commands=['костя'])
def kos(message):
    bot.send_message(message.chat.id, "Моя судьба тусить, бро, тебе меня не изменить))")

@bot.message_handler(commands=['оля'])
def olya(message):
    bot.send_message(message.chat.id, "Оля джан, я буду стоять рядом с тобой когда ты будешь играть и томно дышать на тебе перегаром))")

@bot.message_handler(commands=['женя'])
def zhenya(message):
    bot.send_message(message.chat.id, "Йо, ты спишь чтоли? Время то детское йопт макарек))")

@bot.message_handler(commands=['бля'])
def zhenya(message):
    bot.send_message(message.chat.id, "Йо мэээн! Че как дела бро!!))")

@bot.message_handler(commands=['спишь?'])
def zhenya(message):
    bot.send_message(message.chat.id, "Йо мэээн, да с вами хуй уснешь, вы как бабки старые все пишите и пишите! Все нахуй в пизду вас, я спать пошел!!))")

@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Бро, нихуя се, крутая фотка!)')

@bot.message_handler(commands=['тречек'])
def audio(message):
    audio = open('blue-oyster-bar.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)

@bot.message_handler(commands=['радио'])
def radio(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Давай делай тык", url="https://meezlove.nwgtm.ru/"))
    bot.send_message(message.chat.id, 'Бро, давай радио включай!)', reply_markup=markup)

# @bot.message_handler(commands=['погода'])
# def pogoda(message):
#     bot.send_message(message.chat.id, 'Йо бро, напиши название города')
#
# @bot.message_handler(content_types=['text'])
# def get_weather(message):
#     city = message.text.strip().lower()
#     res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
#     data = json.loads(res.text)
#     bot.reply_to(message, f'Бро, сейчас погода: {data["main"]["temp"]} С')

# @bot.message_handler(commands=['анекдот'])
# def smile(message):
#     bot.send_message(message.chat.id, 'Йо бро, давай поржем, напиши любую цифру от 1 до 9')
#
# @bot.message_handler(content_types=['text'])
# def jokes(message):
#     if message.text.lower() in '123456789':
#         bot.send_message(message.chat.id, list_of_joks[0])
#         del list_of_joks[0]
#     else:
#         bot.send_message(message.chat.id, 'Йопт, бро, ты цифру нормально введи))')


bot.polling(none_stop=True)
