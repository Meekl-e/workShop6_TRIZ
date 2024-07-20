import json
import random
import csv_reader
import pymorphy3
import colorama
colorama.init()

f = open("input.json", "r")
d = json.load(f)

print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Возможно ваше решение...")
print('\033[39m')

print(f"Изменение: '{d["задача"]}' делать не надо.")

print(f"Изменение: '{d["задача"]}' произойдёт само собой.")

parser = pymorphy3.MorphAnalyzer()

for i in d["ресурсы"]:
    zxc = parser.parse(i)[0]
    zxc = zxc.inflect({"gent"}).word
    print(f"Изменение: '{d["задача"]}' осуществить с помощью {zxc}.")

for i in d["цепочка целей"]:
    print(f"Изменение: '{d["задача"]}' не производить, а цель: '{i}' достигнуть.")

print("")
print(colorama.Fore.GREEN + "Цепочка целей:")
print('\033[39m')
print(d["задача"], end = " -> ")
for i in range(len(d["цепочка целей"])):
    if d["цепочка целей"][i] == d["цепочка целей"][-1]:
        print(d["цепочка целей"][i] + ".")
    else:
        print(d["цепочка целей"][i], end = " -> ")

print("")
print(colorama.Fore.GREEN + "Сценарный анализ:")
print('\033[39m')
for i in d["сценарий"]:
    for yu in d["сценарий"][i]:
        vb = []
        for gh in d["сценарий"][i]:
            asd = parser.parse(gh)[0].normal_form
            vb.append(asd)
        if len(vb) == 1:
            rty = parser.parse(yu)[0]
            word_check = rty.inflect({"ablt"})
            if word_check != None:
                #rty = rty.inflect({"ablt"}).word
                print(f"Роль '{i}' может быть отыграна исполнителем - {word_check.word}.")
            else:
                print(f"Роль '{i}' может быть отыграна исполнителем - {rty.normal_form}.")
        else:
            vb = []
            for gh in d["сценарий"][i]:
                asd = parser.parse(gh)[0].normal_form
                vb.append(asd)
            print(f"Роль '{i}' может быть отыграна следующими исполнителями: {", ".join(vb)}.")
            break


print("")
print(colorama.Fore.GREEN + f"Основной сценарий:")
print('\033[39m')
h = 0
for i in d["основной сценарий"]:
    h += 1
    print(f"{h}. {i}")

if d["альтернативные сценарии"] != []:
    print('\033[39m')
    print(colorama.Fore.GREEN + "Альтернативный сценарий:")
    print('\033[39m')
    h = 0
    for i in d["альтернативные сценарии"]:
        h += 1
        print(f"{h}. {i}")

print('\033[39m')
print(colorama.Fore.GREEN + "Для разрешения противоречий можно использовать антисвойства:")
print('\033[39m')
for i in d["сценарий"]:
    for j in d["сценарий"][i]:
        if d["сценарий"][i][j] != "None":
            if type(d["сценарий"][i][j]) == str:
                if d["сценарий"][i][j][0:2] != "не":
                    asd = parser.parse(j)[0].normal_form
                    print(f"{asd} - не {d["сценарий"][i][j]}")
                else:
                    asd = parser.parse(j)[0].normal_form
                    print(f"{asd} - {d["сценарий"][i][j][3:]}")
            else:
                for dfg in d["сценарий"][i][j]:
                    if dfg[0:2] != "не":
                        asd = parser.parse(j)[0].normal_form
                        print(f"{asd} - не {dfg}")
                    else:
                        asd = parser.parse(j)[0].normal_form
                        print(f"{asd} - {dfg[3:]}")

print("")
print(colorama.Fore.GREEN + "Возможно ваше решение...")
print('\033[39m')
a = csv_reader.load("TRIZ.csv")
c = random.choice(a)
for i in c:
    print(i)

print("")
print(colorama.Fore.GREEN + "Подходит ли вам это решение?")
print('\033[39m')
k = input()
while k == "Нет":
    a.remove(c)
    c = random.choice(a)
    print("")
    for i in c:
        print(i)
    print("")
    print(colorama.Fore.GREEN + "Подходит ли вам это решение?")
    print('\033[39m')
    k = input()

# print(d)