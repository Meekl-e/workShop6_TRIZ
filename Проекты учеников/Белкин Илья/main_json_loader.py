import json
import pymorphy3
import re
f = open("main.json", "w", encoding="UTF-8")
tdic = dict()
tdic["description"] = input("Введите полное описание задачи")
string = re.sub(r"\W", " ", tdic["description"]).split()
finder = ''
for word in set(string):
    aboba = pymorphy3.MorphAnalyzer()
    fgs = aboba.parse(word)[0]
    if 'NOUN' == fgs.tag.POS:
        finder = input(f'{fgs.normal_form} является главным объектом? ')
    else:
        tdic["system"] = None
        if finder == 'да':
            tdic["system"] = fgs.normal_form
            break
tdic["task"] = input("Введите проблему, которую Вам нужно преодолеть")

def dic_append(dic, dicts):
    dic["features"] = input("Перечислите свойства главного объекта. Вводите свойства через запятую без пробелов").split(',')
    # rlist = []

    # rin = str()
    dic["roles"] = {}
    while True:
        rin = input("Какие роли есть в Вашей задаче? Чтобы завершить ввод ролей, введите точку")
        if rin == '.':
            break
        inp = int(input("Сколько исполнителей есть на эту роль?"))
        dic["roles"][rin] = {}
        for i in range(inp):
            exin = input("Какой исполнитель этой роли есть в Вашей задаче?")
            fin = input("Какие свойства есть у исполнителя этой роли? Вводите свойства через запятую без пробелов").split(',')
            dic["roles"][rin][exin] = fin
    #inp = input("Введите проблему, которую Вам нужно преодолеть")


    dic["resources"] = input("Введите ресурсы, с помощью которых можно решить задачу").split(',')
    dic["scenario"] = input("Введите сценарий")
    inp = input("Зачем Вам это? Чтобы завершить, введите точку")
    dicts.append(dic)
    if inp == '.':
        return dicts
    d = {"task": inp}
    return  dic_append(d, dicts)



json.dump(dic_append(tdic, []), f, indent=4)
f.close()
