def dict_to_list(diction):
    rlist = []
    rlist.append(f"{diction["task"]} выполнять не надо")
    rlist.append(f"{diction["task"]} произойдёт само собой")
    for j in diction["aims"]:
        rlist.append(f"{diction["task"]} не выполнять, а {j} достичь")
    for o in diction["features"]:
        feat = "не" + o
        if feat.lower().startswith("нене"):
            feat = feat.lstrip("нене")
        rlist.append(f"Изменить свойство объекта {diction["system"]} на {feat.lower()}")
    for f in diction["roles"].keys():
        for s in diction["roles"][f]:
            for g in diction["roles"][f][s]:
                svv = "не" + g
                if svv.lower().startswith("нене"):
                    svv = svv.lstrip("нене")
                rlist.append(f"{diction["task"]} выполнить c помощью {s} ")
                rlist.append(f"Изменить свойство объекта {s} на {svv.lower()}")
    for q in diction["scenario"]:
        rlist.append(f"Попробовать решение по сценарию {q}")
    rlist = rlist
    return rlist


# print(dict_to_list(dicti))
