import telebot
from telebot import types

bot=telebot.TeleBot('8081249668:AAEl36jF_X-Tu4xwx3Qxquzs8FaKAJUlx0w')

@bot.message_handler(commands=['start'])
def start(message):
    mess= f' Привет, {message.from_user.first_name}! Я бот, который может отвечать\
     на вопросы. Задавай свой вопрос, и я постараюсь на него ответить.'
    bot.send_message(message.chat.id,mess)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    vopros = types.KeyboardButton('Хочу задать вопрос')
    markup.add(vopros)
    bot.send_message(message.chat.id, 'С чем нужна помощь?', reply_markup=markup)


@bot.message_handler()
def get_user_text(message):
    if message.text=='Хочу задать вопрос':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        n1 = types.KeyboardButton('Нимбы')
        n2 = types.KeyboardButton('Наушники')
        n3 = types.KeyboardButton('Нейтроны')
        n4 = types.KeyboardButton('Наст')
        n5 = types.KeyboardButton('Носы')
        n6 = types.KeyboardButton('Нимф')
        n7 = types.KeyboardButton('Нитрогениум')
        markup.add(n1,n2,n3,n4,n5,n6,n7)
        bot.send_message(message.chat.id, 'Что тебя интересует?', reply_markup=markup)

    if message.text == 'Нимбы':
        txt = 'условное обозначение сияния вокруг головы изображений Христа, Богоматери, святых и т.д., символизирующее их святость.'
        a1=open('бог.jpg','rb')

        bot.send_message(message.chat.id, txt)
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(a1)])

    elif message.text == 'Наушники':
        txt = ' устройство для персонального прослушивания звуковой информации. В комплекте с микрофоном могут служить головной гарнитурой – средством для ведения переговоров по телефону или иному средству голосовой связи.\
 Кроме того, наушники используются в звукозаписывающих студиях для точного контроля записываемого трека музыкальной композиции.'
        a2=open('наушники.jpg','rb')
        a20=open('наушники2.jpg','rb')

        bot.send_message(message.chat.id, txt)
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(a2),telebot.types.InputMediaPhoto(a20)])

    elif message.text == 'Нейтроны':
        txt = 'тяжёлая элементарная частица, не имеющая электрического заряда.'
        a3=open('нейтроны.jpg','rb')

        bot.send_message(message.chat.id, txt)
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(a3)])

    elif message.text == 'Наст':
        txt = 'это плотная корка снега на поверхности (или в результате последующих снегопадов — в более глубоких слоях) снежного покрова.'
        a4 = open('наст.jpg', 'rb')

        bot.send_message(message.chat.id, txt)
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(a4)])

    elif message.text == 'Носы':
        txt = 'орган для распознавания запахов. Часть лица (у человека) или морды (у остальных животных), участвующая в дыхании, обонянии, добыче корма и общении.'
        a5 = open('носы.jpg', 'rb')
        a59=open('носы2.jpg', 'rb')

        bot.send_message(message.chat.id, txt)
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(a5),telebot.types.InputMediaPhoto(a59)])

    elif message.text == 'Нимф':
        txt = 'это прекрасные, вечно юные женские божества природы в древнегреческой мифологии.'
        a6 = open('нимфы1.jpg', 'rb')

        bot.send_message(message.chat.id, txt)
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(a6)])

    elif message.text == 'Нитрогениум':
        txt = 'Азо́т (N, лат. nitrogenium) — химический элемент 15-й группы, второго периода периодической системы с атомным номером 7.'
        a7 = open('азот.jpg', 'rb')
        a70 = open('азот1.jpg', 'rb')

        bot.send_message(message.chat.id, txt)
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(a7),telebot.types.InputMediaPhoto(a70)])



bot.polling(none_stop=True)