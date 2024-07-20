import json
print('Кто главный в нашей системе?')
system = input()
print('Какие качества будут у', system)
features = input().split(", ")
tt = {}
tt
print('Сколько ролей?')
for key in range(int(input())):
    print('Сколько исполнителей')
    for isp in range(int(input())):
        isp = input("введите исполнителя: ")
        sv = input("введите свойства: ").split(", ")
        tt
tt = {"system": system,"features": features,"roles": {  "игрушка": {    "мыши": ["не любят играть"],    "плюшевая мышка": ["безразлично"]  }},"change": "ловить мышей","scenario": "мыши пойманы","res": ["игрушка", "корм"]}
f = open('../общее/test.json', 'w', encoding="UTF-8")
json.dump(tt, f)
f.close()