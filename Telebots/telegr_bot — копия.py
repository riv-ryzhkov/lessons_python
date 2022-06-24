﻿
# pip install pyTelegramBotAPI


import telebot


# Создаем экземпляр бота
bot = telebot.TeleBot('111111111111111111111')


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')


# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
    return message.text


# Запускаем бота
bot.polling(none_stop=True, interval=0)