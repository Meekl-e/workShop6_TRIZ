# импортируем нужные библиотеки и функции
import json
import re
import pymorphy3

# создаём необходимые словари и списки
dictionary = {}  # словарь
features = []  # список свойств

count = 0  # счётчик

# открываем файл формата .json
f = open("t.json", "w", encoding="utf-8")

dictionary["task"] = input('Введите изменение: ')
# вводим с клавиатуры необходимые данные
dictionary["resources"] = input('С помощью какого ресурс(а/ов) вы будете это выполнять? ').split(', ')
dictionary["description"] = input('Опишите вашу задачу полностью без знаков препинания через пробел каждое слово: ')

# с помощью библиотеки создаём цикл в котором находим существительные испрашивем у пользователя являются ли они системой
a = dictionary["description"]
string = re.sub(r"\W", " ", a).split()
for word in set(string):
    m_analyzer = pymorphy3.MorphAnalyzer()
    former = m_analyzer.parse(word)[0]
    if 'NOUN' == former.tag.POS:
        finder = input(f'{former.normal_form} является главным объектом задачи? ')
        if finder == 'да':
            dictionary["system"] = former.normal_form
            break
else:
    dictionary["system"] = 'не найден'

# вводим с клавиатуры необходимые данные

dictionary["scenariums"] = []
dictionary["aims"] = []
dictionary["features"] = input("Основные свойства главного объекта/сущности в задаче: ").split(', ')
dictionary['scenario'] = input("Введите сценарий задачи: ")
scenario = ''
while scenario != '.':
    dictionary["scenariums"].append(dictionary["scenario"])
    scenario = input("Это последний вариант сценария? ")
    if scenario == 'да':
        break
    else:
        dictionary["scenario"] = input("Введите вариант нового сценария: ")
dictionary["scenariums"].pop(0)
roles = input("Введите роли через запятую: ").split(', ')
dictionary["roles"] = {}

# цикл в ходе которого вводятся исполнители и их свойства
for role in roles:
    ispols = input(f"Введите исполнителей ролей {role} через запятую: ").split(", ")
    for i in ispols:
        svs = input(f'Введите свойства объекта {i} через запятую: ').split(", ")
        dictionary["roles"][role] = {i: svs}

aim = 'water'
while aim != '.':
    aim = input('Ради чего? ')
    dictionary["aims"].append(aim)
dictionary["aims"].pop(-1)

# сохраняем введённые данные в файл .json
json.dump(dictionary, f, indent=4)
