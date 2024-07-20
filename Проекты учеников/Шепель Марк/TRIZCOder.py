import json
#Спрашиваем
task = input("Введите задание:")
TRIZ = {}
#Инпуты они же вводы
description = input("Введите описание:")
type = ("Первый тип")
resourcers = input("Ресурсы:").split(", ")
prichina = input("Введите цель:")
rol = input("Введите роли:").split(", ")
#Запись в слонарик
TRIZ["Task"] = task
TRIZ["Description"] = description
TRIZ["Type"] = type
TRIZ["Resource"] = resourcers
TRIZ["roles"] = rol
TRIZ["Reason"] = prichina
#Записываем в JSON
f = open("problemsTRIZ.json", "w", encoding="utf-8")
json.dump(TRIZ, f)
