# импортируем нужные библиотеки и функции
import json
from colorama import Fore, Style
from csv_reader import load
import random
import pymorphy3

# создаём функцию для изменения цвета в консоли
def print_with_color(s, color=Fore.WHITE, brightness=Style.NORMAL):
    print(f"{brightness}{color}{s}{Style.RESET_ALL}")

# открываем файл формата .json где находятся все данные
f = open("t.json", "r", encoding="utf-8")

# загружаем в словарь dictionary файл создаваемый в кодировщике
dictionary = json.load(f)

# здесь располагаются необходимые массивы и счётчики
features = []  # свойства
count = 0  # счётчик

# создаём переменную типа данных 'str' которая будет иметь заглушку
aim = 'water'

# цикл для вывода по каждому изменению
for m in dictionary["aims"]:
    # далее представлен метод работающий по 4-ёх вопроснику
    # изменение делать не надо
    print(f'1. {dictionary["task"]} не надо')
    print('')

    # изменение произойдёт само собой
    print(f'2. {dictionary["task"]} произойдёт само собой')
    print('')

    # выполните изменение с помощью подручных ресурсов
    print(f'3. {dictionary["task"]} выполните с помощью {", ".join(map(str,dictionary["resources"]))}')
    print('')

    # изменение делать не надо, но цели достичь
    print(f'4. {dictionary["task"]} делать не надо, но {m}')
    print('')

    # вывод системы задачи
    print(f'5. Главный объект задачи: {dictionary["system"]}')
    print('')

    # вывод сценария задачи
    print(f'6. Сценарием задачи является: {dictionary["scenario"]}')
    print('')

    # вывод полной задачи
    print(f'7. Задача без сокращений: {dictionary["description"]}')
    print('')

    # цикл в цикле, в ходе которого n раз выводится на какую роль подойдёт исполнитель
    for role in dictionary["roles"]:
        for ispols in dictionary["roles"][role]:
            print(f'8. На роль {role} подойдет {ispols}')
            print('')

    # цикл в ходе которого происходит вывод НЕсвойств объектов
    for feature in dictionary["features"]:
        feature_print = 'не' + dictionary["features"][count]
        feature_prints = dictionary["features"][count]
        # проверка: если слово уже начинается на 'не', то преобразуется в слово без 'не'
        # пример: некрасивый -> ненекрасивый -> красивый
        if feature_print.lower().startswith("нене"):
            final_feature = feature_print.lstrip("нене")
            print(f'9. Свойство объкта {final_feature}')
            print('')
        # проверка: если слово начинается на 'без', то преобразуется в слово исключающее из себя приставку 'без'
        # пример: безводный -> водный
        elif feature_prints.lower().startswith("без"):
            feature_prints = feature_prints[3:]
            print(f'9. Свойство объкта {feature_prints}')
            print('')
        # проверка: если слово начинается на 'бес', то преобразуется в слово исключающее из себя приставку 'бес'
        # пример: беспринципный -> принципный
        elif feature_prints.lower().startswith("бес"):
            feature_prints = feature_prints[3:]
            print(f'9. Свойство объкта {feature_prints}')
            print('')
        else:
            print(f'9. Свойство объкта {feature_print}')
            print('')
        count += 1
    count = 0
    # создаём переменную типа данных 'str' которая будет иметь заглушку
    scenario = 'water'
    # цикл необходимый для вывода сценария, а также работающий до момента, пока пользователь не введёт 'да'
    for p in dictionary["scenariums"]:
        print_with_color(f'10. Сценарий данной задачи: {p}', color=Fore.BLUE)
        print('')
count = 0

# загружаем файл который содержи в себе 40 приёмов Г. Альтшуллера
isp = load("TRIZ.csv")
isp.pop(0)
priem = random.choice(isp)
isp.remove(priem)

# создаём переменную типа данных 'str' которая будет иметь заглушку
a = "water"

# цикл, необходимый для рандомного выбора 1 из предложенных решений и вывода на экран
# пока пользователю не подойдёт решение или пока 40 приемов не закончатся будет работать данный цикл
while a != 'да' and len(isp) > 0:
    priem = random.choice(isp)
    isp.remove(priem)
    print(f'10. Мы можем предложить вам решение таблице Г. Альтшуллера:\n'
          f'{priem}')
    a = input("Подходит ли вам предложенное решение?\n ")
