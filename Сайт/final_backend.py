import os.path

if os.path.exists("word2vec/model.bin"):
    from word2vec.nn_analyze import analyze  # импорт речевого анализатора


def dict_to_list(diction):
    rlist = []
    for j in diction["aims"]:
        rlist.append(f"{diction["task"]} не выполнять, а {j} достичь любым другим путем.")
    for o in diction["features"]:
        feat = "не" + o
        if feat.lower().startswith("нене"):
            feat = feat.lstrip("нене")
        rlist.append(f"Изменить свойство объекта {diction["system"]} на {feat.lower()}.")
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
    if os.path.exists("word2vec/model.bin"):
        rlist = rlist + list(set(analyze(diction)))
    return rlist

# print(dict_to_list(dicti))
