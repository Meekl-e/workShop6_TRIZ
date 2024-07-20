import telebot.types
from telebot import *
from loader import load

TOKEN = '<YOUR_TOKEN>'
bot = TeleBot(TOKEN)

x = ''#строки
y = ''#столбцы
h = 0
ввод = []#для запаменания ввода пользователя
triz = load("TRIZ.csv", "\t")#таблица для понятие TRIZ приёма
priems = load("PRIEMS.CSV", ";")#таблица для нахождение TRIZ приёма
@bot.message_handler(commands=["start"]) #требуеться для того чтобы функция в следущеё строеке наченалась по написанию команды старт
def start(msg):
    global h
    string = ""
    for i in range(1, 40): #для вывода вариантов
        string += "".join(priems[i][1]) + "\n"
    bot.send_message(msg.chat.id, string)
    bot.send_message(msg.chat.id,"Введите два числа через запятую: ")
@bot.message_handler(content_types="text")#требуеться для того чтобы функция в следущеё строеке наченалась по написанию чего нибудь пользователем
def start2(msg):

    ввод = msg.text.split(", ")
    y = ввод[0]
    x = ввод[1]
    if y.isdigit() == True and x.isdigit() == True:#проверяет являються ли x и y числами
        x = int(x) +1
        y = int(y)
        if y > 0 or y < 40 or x > 0 or x < 40:#проверяет на размер значения тоесть значение x и y должны быть больше 0 и меньше 40(эти числа не взяты из головы это размер таблицы приёмов)
            if priems[y][x] != '-' and priems[y][x] != ' ' and priems[y][x] != '\xa0':
                bot.send_message(msg.chat.id, 'Возможно вам подойдет один из ниже перечисленых способов')
                for i in priems[y][x].split(', '):  # перечисляет все способы которые могут подойти
                    i = triz[int(i)]
                    bot.send_message(msg.chat.id, f"{i[0]} это {i[1]} а точнее: {i[2]}")
            else:
                bot.send_message(msg.chat.id, "Короткое обяснение системы триза по этой ссылке: https://goo.su/EFl6X",link_preview_options=types.LinkPreviewOptions(is_disabled=True))
                bot.send_message(msg.chat.id, "Извините но мы не нашли решение в нашей базе данных!")
        else:
            bot.send_message(msg.chat.id, "Короткое обяснение системы триза по этой ссылке: https://goo.su/EFl6X",link_preview_options=types.LinkPreviewOptions(is_disabled=True))
            bot.send_message(msg.chat.id, "Вы ввели слишком большое либо слишком маленькое значение!")
    else:
        bot.send_message(msg.chat.id, "Короткое обяснение системы триза по этой ссылке: https://goo.su/EFl6X", link_preview_options=types.LinkPreviewOptions(is_disabled=True))  # скрыть содержание
        bot.send_message(msg.chat.id, "Вы ввели недопустимое значение!")



bot.infinity_polling()