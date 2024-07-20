import json
import colorama

d = {}

print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Каков полный текст задачи?")
b = input()
d["description"] = b

print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Что вы хотите сделать? Какова задача?")
a = input()
d["task"] = a

# print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Какова цель этой задачи?")
# g = input()
# d["goal"] = g

print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Вокруг какого субъекта происходят основные действия задачи?")
k = input()
d["system"] = k

print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Какие свойства имеет субъект?")
p = input()
P = p.split(", ")
d["features"] = P

print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Напишите основной сценарий решения задачи.")
l = input()
d["scenarei"] = l

print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Выберите тип задачи... 1")
y = input()
d["type"] = y

print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Какие ресурсы можно использовать для осуществления изменения?")
r = input()
R = r.split(", ")
d["resourcers"] = R

print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Каковы роли в вашем сценарии?")
print("Напишите в формате роль-исполнитель-свойство исполнителя.")
m = input()
M = m.split(", ")
q = {}
d["roles"] = {"None": {"None": "None"}}
for i in M:
    z = i.split("-")
   # for j in d["roles"].copy():
    if z[0] not in d["roles"].keys():
        d["roles"][z[0]] = {z[1]: z[2]}
        for key in d["roles"].copy().keys():
            if not d["roles"][key].get("None") is None:
                d["roles"][key].pop("None")
            if key == "None":
                d["roles"].pop("None")
    else:
        d["roles"][z[0]][z[1]] = z[2]
# print(d["roles"])

print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Какова цель этой задачи?")
g = input()
d["goal"] = g
# print(d["goal"])

print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Изменился ли субъект задачи?")
k = input()
fgj = []
cbv = []
if k == "Да":
    print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Каков субъект задачи?")
    jk = input()
    fgj.append(d["system"])
    fgj.append(jk)
    d["system"] = fgj
    print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Какие свойства имеет субъект?")
    p = input()
    P = p.split(", ")
    cbv += d["features"]
    cbv.extend(P)
    d["features"] = cbv
# print(d["system"])
# print(d["features"])

print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Изменился ли основной сценарий решения задачи?")
l = input()
xng = []
if l == "Да":
    print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Каков основной сценарий?")
    dfg = input()
    xng.append(d["scenarei"])
    xng.append(dfg)
    d["scenarei"] = xng
# print(d["scenarei"])

print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Изменились ли ресурсы?")
r = input()
xng = []
if r == "Да":
    print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Какие ресурсы появились?")
    dfg = input()
    R = dfg.split(", ")
    xng.extend(d["resourcers"])
    xng.extend(R)
    d["resourcers"] = xng
# print(d["resourcers"])

print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Появились ли новые роли в вашем сценарии?")
sa = input()
ghj = []
if sa == "Да":
    print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Какие роли нужно добавить?")
    print("Напишите в формате роль-исполнитель-свойство исполнителя.")
    m = input()
    M = m.split(", ")
    q = {}
    for i in M:
        z = i.split("-")
        if z[0] not in d["roles"].keys():
            d["roles"][z[0]] = {z[1]: z[2]}
        else:
            d["roles"][z[0]][z[1]] = z[2]
# print(d["roles"])

print('\033[39m')
print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Можете ли вы обобщить цель?")
print('\033[39m')
q = input()
b = 0
c = d["goal"]
d["goal"] = []
d["goal"].append(c)
while q == "Да":
    b += 1
    if b % 2 == 0:
        print('\033[39m')
        print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + f"А зачем выполнять цель '{c}'?")
        print('\033[39m')
        print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Чтобы...")
        print('\033[39m')
        c = input()
        d["goal"].append(c)

        print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Изменился ли субъект задачи?")
        k = input()
        fgj = []
        cbv = []
        if k == "Да":
            print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Каков субъект задачи?")
            jk = input()
            fgj.append(d["system"])
            fgj.append(jk)
            d["system"] = fgj
            print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Какие свойства имеет субъект?")
            p = input()
            P = p.split(", ")
            cbv += d["features"]
            cbv.extend(P)
            d["features"] = cbv
        # print(d["system"])
        # print(d["features"])

        print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Изменился ли основной сценарий решения задачи?")
        l = input()
        xng = []
        if l == "Да":
            print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Каков основной сценарий?")
            dfg = input()
            xng.append(d["scenarei"])
            xng.append(dfg)
            d["scenarei"] = xng
        # print(d["scenarei"])

        print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Изменились ли ресурсы?")
        r = input()
        xng = []
        if r == "Да":
            print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Какие ресурсы появились?")
            dfg = input()
            R = dfg.split(", ")
            xng.extend(d["resourcers"])
            xng.extend(R)
            d["resourcers"] = xng
        # print(d["resourcers"])

        print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Появились ли новые роли в вашем сценарии?")
        sa = input()
        ghj = []
        if sa == "Да":
            print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Какие роли нужно добавить?")
            print("Напишите в формате роль-исполнитель-свойство исполнителя.")
            m = input()
            M = m.split(", ")
            q = {}
            for i in M:
                z = i.split("-")
                if z[0] not in d["roles"].keys():
                    d["roles"][z[0]] = {z[1]: z[2]}
                else:
                    d["roles"][z[0]][z[1]] = z[2]
        # print(d["roles"])

        print('\033[39m')
        print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Можете ли вы обобщить цель?")
        print('\033[39m')
        q = input()
    else:
        print('\033[39m')
        print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + f"С какой целью нужно выполнять цель '{c}'?")
        print('\033[39m')
        print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Чтобы...")
        print('\033[39m')
        c = input()
        d["goal"].append(c)

        print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Изменился ли субъект задачи?")
        k = input()
        fgj = []
        cbv = []
        if k == "Да":
            print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Каков субъект задачи?")
            jk = input()
            fgj.append(d["system"])
            fgj.append(jk)
            d["system"] = fgj
            print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Какие свойства имеет субъект?")
            p = input()
            P = p.split(", ")
            cbv += d["features"]
            cbv.extend(P)
            d["features"] = cbv
        # print(d["system"])
        # print(d["features"])

        print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Изменился ли основной сценарий решения задачи?")
        l = input()
        xng = []
        if l == "Да":
            print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Каков основной сценарий?")
            dfg = input()
            xng.append(d["scenarei"])
            xng.append(dfg)
            d["scenarei"] = xng
        # print(d["scenarei"])

        print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Изменились ли ресурсы?")
        r = input()
        xng = []
        if r == "Да":
            print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Какие ресурсы появились?")
            dfg = input()
            R = dfg.split(", ")
            xng.extend(d["resourcers"])
            xng.extend(R)
            d["resourcers"] = xng
        # print(d["resourcers"])

        print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Появились ли новые роли в вашем сценарии?")
        sa = input()
        ghj = []
        if sa == "Да":
            print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Какие роли нужно добавить?")
            print("Напишите в формате роль-исполнитель-свойство исполнителя.")
            m = input()
            M = m.split(", ")
            q = {}
            for i in M:
                z = i.split("-")
                if z[0] not in d["roles"].keys():
                    d["roles"][z[0]] = {z[1]: z[2]}
                else:
                    d["roles"][z[0]][z[1]] = z[2]
        # print(d["roles"])

        print('\033[39m')
        print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Можете ли вы обобщить цель?")
        print('\033[39m')
        q = input()

f = open("zadacha.json", "w")
json.dump(d, f)
f.close()