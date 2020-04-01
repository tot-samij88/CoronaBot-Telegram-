import telebot
from telebot import types
import COVID19Py


covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot('1153943515:AAE1RQj5b1m0NcC5zLr5e0-sQIuvP6Kkk-E')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Во всём мире')
    btn2 = types.KeyboardButton('Украина')
    btn3 = types.KeyboardButton('Россия')
    btn4 = types.KeyboardButton('Беларусь')
    markup.add(btn1, btn2, btn3, btn4)

    send_message = f"Привет {message.from_user.first_name}!\nХочешь узнать последние данные насчёт коронавируса?\nНапиши " \
        f"название страны, пример: США, Украина, Россия..."
    bot.send_message(message.chat.id, send_message,
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    get_message_bot = message.text.strip().lower()
    if get_message_bot == "сша":
        location = covid19.getLocationByCountryCode("US")
    elif get_message_bot == "украина":
        location = covid19.getLocationByCountryCode("UA")
    elif get_message_bot == "россия":
        location = covid19.getLocationByCountryCode("RU")
    elif get_message_bot == "беларусь":
        location = covid19.getLocationByCountryCode("BY")
    elif get_message_bot == "казакхстан":
        location = covid19.getLocationByCountryCode("KZ")
    elif get_message_bot == "италия":
        location = covid19.getLocationByCountryCode("IT")
    elif get_message_bot == "франция":
        location = covid19.getLocationByCountryCode("FR")
    elif get_message_bot == "германия":
        location = covid19.getLocationByCountryCode("DE")
    elif get_message_bot == "япония":
        location = covid19.getLocationByCountryCode("JP")
    else:
        locations = covid19.getLatest()
        final_message = f"<u>Данные по всему миру:\n</u><b>Заболевших: </b>{locations['confirmed']:,}\n<b>Сметрей: </b>{locations['deaths']:,}"
        bot.send_message(message.chat.id, final_message, parse_mode='html')
        

    if final_message == "":

        final_message = f"<u>Данные по стране:</u>\nКоличество населения: {location[0]['country_population']:,}\nПоследнее обновление: {location[0]['last_updated']}\nПоследние данные:\n<b>Заболевших: </b>{location[0]['latest']['confirmed']:,}\n<b>Сметрей: </b>{location[0]['latest']['deaths']:,}\n<b>Выздоровели: </b>{location[0]['latest']['recovered']:,}"
        bot.send_message(message.chat.id, final_message, parse_mode='html')


bot.polling(none_stop=True)
