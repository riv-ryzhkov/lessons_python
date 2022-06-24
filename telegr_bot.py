# riv_echo    @riv_echo_bot
# riv1_bot    @riv1_bot


# pip install pyTelegramBotAPI


import telebot


# Создаем экземпляр бота
# bot = telebot.TeleBot('5378463425:AAEwC5zJvwAAlk4NpfI8e1nb-Dw9Wxzc7JA')
# bot = telebot.TeleBot('5268343767:AAEIakUn_s2kHKMsiKOAlxrDpsfjShsmcA0')
# bot = telebot.TeleBot('5034062450:AAEj1f3Qfq4zv4roJGaTh9LsgYCc4tEmsEc')
bot = telebot.TeleBot('5310154090:AAEBqaw9iNU1_l4Azn7yP7Yp1eqXf6K-uE0')


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