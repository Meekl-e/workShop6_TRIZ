import json
from csv_reader import load
from random import choice
from colorama import init
init()
from colorama import Fore, Back
f = open("main.json", "r", encoding='UTF-8')
dicts = json.load(f)

for dic in dicts:
    lsc = []
    tasks = []
    if 1 == 1:
        listres = []
        tlist = []
        for i in range(len(dic["resources"])):
            listres.append(dic["resources"][i])
        print(Fore.BLACK + Back.RED + "1.", f"{dic["task"]}", "делать не надо")
        print(Fore.BLACK + Back.RED + "2.", f"{dic["task"]}", "произойдёт само собой")
        print(Fore.BLACK + Back.RED + "3.", f"{dic["task"]}", "достигнуть с помощью ресурса/ресурсов", end=' ')
        for i in range(len(listres)-1):
            print(listres[i], end=', ')
        print(listres[-1])
        for i in range(len(tlist)):
            print(Fore.BLACK + Back.RED + "4.", f"{dic["task"]}", "не производить, а", f"{tlist[i]}", "достигнуть")
    #if dic["type"] == "Сценарный анализ":
        for role in dic["roles"].keys():
            for res in dic["roles"][role]:
                print(Fore.BLACK + Back.RED + f"На роль {role} подходит {res}")
    #if dic["type"] == "40 приёмов":
    for i in dic["roles"].keys():
        for j in dic["roles"][i]:
            for k in range(len(dic["roles"][i][j])):
                print(f"Изменить свойство {j} на не {dic["roles"][i][j][k]}")

'''for t in lsc:
    dic["scenario"].append(t)
json.dump(dic, f)'''
choi = load("TRIZZZZ.csv")
choi.remove(choi[0])
rch = choice(choi)
for i in range(2):
    print(Fore.BLACK + Back.RED + rch[i], end=' ')
print(rch[-1])
choi.remove(rch)
inp = input(Fore.BLACK + Back.RED + "Вам подходит это решение? Если подходит, введите Да")
while True:
    if inp != "Да":
        rch = choice(choi)
        print(*rch)
        choi.remove(rch)
        inp = input("Вам подходит это решение? Если подходит, введите Да")
    else:
        print("Отлично! Спасибо за обращение!")
        break
f.close()