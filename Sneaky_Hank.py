import telebot
from config import *
from extensions import *


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    text = 'Привет! Я помогу тебе сконвертировать валюту! \n\
Введи: "Валюту, цену которой хочешь узнать" "Валюту, в которой хочешь узнать цену первой валюты"\
и "Количество первой валюты". Пример: "Доллар Рубль 10"\nИспользуй /values, что-бы увидеть список доступных валют для\
конвертации.'
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['help'])
def help_user(message: telebot.types.Message):
    text = 'Введи: "Валюту, цену которой хочешь узнать" "Валюту, в которой хочешь узнать цену первой валюты"\
и "Количество первой валюты". Пример: "Доллар Рубль 10"\nИспользуй /values, что-бы увидеть список доступных валют для\
конвертации.'
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = "Доступные валюты для конвертации:"
    for key in exch.keys():
        text = '\n'.join((text, key))
    bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        arg = message.text.split()
        if len(arg) != 3:
            raise ConvertionException(
                'Необходимо написать "ТРИ" параметра!\nИспользуй /help чтобы отобразить инструкцию')
        quote, base, amount = arg
        price = round(float(Converter.convert(quote, base, amount)) * float(amount), 2)
    except ConvertionException as e:
        bot.send_message(message.chat.id, f'Ошибка:\n{e}')
    else:
        text = f'"{amount}" "{quote}" в "{base}" = {price}'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
