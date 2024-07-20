import json
import pymorphy3
import colorama
colorama.init()

f = open("zadacha.json", "r", encoding="utf-8")
w = json.load(f)
if w["type"] == "1":
    d = {}
    #print("Что вы хотите сделать? Какова задача?")
    #a = input()
    d["задача"] = w["task"]
    d["основной сценарий"] = w["scenarei"]
    #print("Какие ресурсы можно использовать для осуществления изменения?")
    #print("С помощью...")
    #r = input()
    #R = r.split(", ")
    d["ресурсы"] = w["resourcers"]

    v = {}
    #print("Каковы роли в вашем сценарии?")
    #print("Напишите в формате роль-исполнитель.")
    #m = input()
    #M = m.split(", ")
    for i in w["roles"]:
        #z = i.split("-")
        if w["roles"][i] == {"None": "None"}:
            print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + f"На роль '{i}' нет исполнителя.")
            print('\033[39m')
            print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Хотите ввести исполнителя?")
            print('\033[39m')
            g = input()
            if g == "Да":
                print('\033[39m')
                print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Введите исполнителя...")
                print('\033[39m')
                w["roles"][i] = {input(): "None"}
                v[i] = w["roles"][i]
            else:
                w["roles"][i] = "None"
                v[i] = {w["roles"][i]: "None"}
                break
        else:
            v[i] = w["roles"][i]

        #print(v[i])
    parser = pymorphy3.MorphAnalyzer()

    for i in w["roles"]:
        for j in v[i]:
            if j != "None":
                if v[i][j] == "None":
                    zxc = parser.parse(j)[0]
                    zxc = zxc.inflect({"gent"}).word
                    qwe = parser.parse(i)[0]
                    qwe = zxc.inflect({"gent"}).word
                    print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + f"У {zxc} - {qwe} нет свойства.")
                    print('\033[39m')
                    print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Хотите ввести свойство?")
                    print('\033[39m')
                    qwe = input()
                    if qwe == "Да":
                        print('\033[39m')
                        print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Введите свойство...")
                        print('\033[39m')
                        v[i][j] = input()
                    else:
                        v[i][j] = "None"
    d["сценарий"] = v

    print('\033[39m')
    print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Подходят ли следующие ресурсы на роли?")
    print('\033[39m')
    n = []
    for j in d["сценарий"]:
        # print(d["сценарий"][j])
        #for sd in d["сценарий"][j]:
        for i in d["ресурсы"]:
            print('\033[39m')
            asd = parser.parse(i)[0].normal_form
            print(f"Подходит ли {asd} на роль '{j}'?")
            print('\033[39m')
            x = input()
            if x == "Да":
                # if type(d["сценарий"][j][sd]) == str:
                #     if d["сценарий"][j][sd] == "None":
                #         n.append(d["сценарий"][j][sd])
                #         n.append(i)
                #         d["сценарий"][j][sd] = n
                #         d["сценарий"][j][sd].remove("None")
                #         n = []
                #     else:
                #         n.append(d["сценарий"][j][sd])
                #         n.append(i)
                #         d["сценарий"][j][sd] = n
                #         n = []
                # else:
                d["сценарий"][j][i] = "None"
                # print(d["сценарий"][j])

                for key in d["сценарий"].keys():
                    if not d["сценарий"][key].get("None") is None:
                        d["сценарий"][key].pop("None")
                # print(d["сценарий"])

    if len(w["system"]) == 1:
        d["сценарий"]["система"] = {w["system"]: w["features"]}
    else:
        for i in range(len(w["system"])):
            if i < len(w["features"]):
                d["сценарий"]["система"] = {w["system"][i]: w["features"][i]}
            else:
                d["сценарий"]["система"] = {w["system"][i]: "None"}


    for i in d["сценарий"]:
        for j in d["сценарий"][i]:
            if j != "None":
                if d["сценарий"][i][j] == "None":
                    zxc = parser.parse(j)[0]
                    word_check = zxc.inflect({"gent"})
                    if word_check != None:
                        #zxc = zxc.inflect({"gent"}).word
                        #qwe = parser.parse(i)[0]
                        #qwe = zxc.inflect({"gent"}).word
                        print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + f"У {word_check.word} роли '{i}' нет свойства.")
                        print('\033[39m')
                        print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Хотите ввести свойство?")
                        print('\033[39m')
                        qwe = input()
                        if qwe == "Да":
                            print('\033[39m')
                            print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Введите свойство...")
                            print('\033[39m')
                            d["сценарий"][i][j] = input()
                        else:
                            d["сценарий"][i][j] = "None"
                    else:
                        print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + f"У {zxc.normal_form} роли '{i}' нет свойства.")
                        print('\033[39m')
                        print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Хотите ввести свойство?")
                        print('\033[39m')
                        qwe = input()
                        if qwe == "Да":
                            print('\033[39m')
                            print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Введите свойство...")
                            print('\033[39m')
                            d["сценарий"][i][j] = input()
                        else:
                            d["сценарий"][i][j] = "None"
    # print(d["сценарий"])

    #print("Каков идеальный конечный результат?")
    # print('\033[39m')
    # print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Какова ваша цель?")
    # print('\033[39m')
    #c = input()
    #c = w["task"]
    c = w["goal"]
    d["цепочка целей"] = []
    if type(c) == str:
        d["цепочка целей"].append(c)
    else:
        d["цепочка целей"] = c
    # print('\033[39m')
    # print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Можете ли вы обобщить цель?")
    # print('\033[39m')
    # q = input()
    # b = 0
    # while q == "Да":
    #     b += 1
    #     if b % 2 == 0:
    #         print('\033[39m')
    #         print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + f"А зачем выполнять цель '{c}'?")
    #         print('\033[39m')
    #         print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Чтобы...")
    #         print('\033[39m')
    #         c = input()
    #         d["цепочка целей"].append(c)
    #         print('\033[39m')
    #         print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Можете ли вы обобщить цель?")
    #         print('\033[39m')
    #         q = input()
    #     else:
    #         print('\033[39m')
    #         print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + f"С какой целью нужно выполнять цель '{c}'?")
    #         print('\033[39m')
    #         print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Чтобы...")
    #         print('\033[39m')
    #         c = input()
    #         d["цепочка целей"].append(c)
    #         print('\033[39m')
    #         print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Можете ли вы обобщить цель?")
    #         print('\033[39m')
    #         q = input()

    d["альтернативные сценарии"] = []
    print('\033[39m')
    print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Есть ли альтернативный сценарий? Есть ли другое решение задачи?")
    print('\033[39m')
    zxc = input()
    while zxc == "Да":
        print('\033[39m')
        print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Введите альтернативный сценарий...")
        print('\033[39m')
        qwe = input()
        d["альтернативные сценарии"].append(qwe)
        print('\033[39m')
        print(colorama.Back.BLACK + colorama.Style.BRIGHT + colorama.Fore.GREEN + "Есть ли альтернативный сценарий? Есть ли другое решение задачи?")
        print('\033[39m')
        zxc = input()

    # v = {}
    # print("Каковы роли в вашем сценарии?")
    # print("Напишите в формате роль-исполнитель.")
    # m = input()
    # M = m.split(", ")
    # for i in M:
    #     z = i.split("-")
    #     v[z[0]] = z[1]
    # d["сценарий"] = v
    f = open("input.json", "w")
    # di = []
    # di.append(f"{a} делать не надо.")
    # di.append(f"{a} произойдёт само собой.")
    # for i in R:
    #     di.append(f"{a} осуществить с помощью {i}.")
    # di.append(f"{a} не производить, а {cs} достигнуть.")
    # d["ответы"] = di
    json.dump(d, f)
    f.close()