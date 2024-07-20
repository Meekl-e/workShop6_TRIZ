import json # ДЖИСОН
from csv_reader import load
from random import choice
#Импорт всех библиотек
e = True
#Открываем файл
f = open("problemsTRIZ.json", "r", encoding="UTF-8")
#Загружаем
dicti = json.load(f)
#Четырёхопросник
print(dicti)
print(dicti["Task"], "- это делать не надо")
print(dicti["Task"], "- это само собой выполниться")
#Цикл по ресурсам
for i in dicti["Resource"]:
    print(dicti["Task"], "- с помощью ресурсов", {i})
print(dicti["Task"], "это - не делать, достигнуть цель:", dicti["Reason"], "по другому")
resour = dicti["Resource"]
roles = dicti["roles"]
#Цикл роль - исполняющий
for rl in roles :
    for res in roles[rl] :
            print(f"Роль {rl} = исполняющий {res}")
#Метод ТРИZ
print(choice(load("TRIZ.csv")))
t = input("Подошло решение?Если да - напишите точку")
#Спрашиваем пользователя
while e == True:
    if t == ".":
        e = False
        print(f"Надеюсь мы вам помогли с {dicti["Reason"]}. Спасибо огромное")
    else:
        print(choice(load("TRIZ.csv")))
        break
