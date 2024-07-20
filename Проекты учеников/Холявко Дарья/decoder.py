import json
import pymorphy3

morph = pymorphy3.MorphAnalyzer()


f = open("task-new.json", "r", encoding="utf-8")

dictionary = json.load(f)

t = 'Что вы хотите сделать?'

m = []

Зачем = input(f'А зачем вам {dictionary["task"]}?')

while Зачем != '.':
    m.append(Зачем)
    Зачем = input('А зачем вам это?')

answer1 = f"{dictionary['task']} делать не надо."
print(answer1)

answer2 = f'{dictionary["task"]} произойдёт само собой.'
print(answer2)

for res in dictionary['resources']:
    res = morph.parse(res)[0]
    res = res.inflect({"gent"}).word
    print(f'Вы можете {dictionary["task"]} с помощью {res}.')

for i in m:
    print(f'{dictionary["task"]} делать не надо, но цель {i} достичь.')

sposobs = input('Есть ли другие способы сценария?')

for el in dictionary['features']:
    print("не" + el)

for key in dictionary['roles']:
    for isp in dictionary["roles"][key]:
        for sv in dictionary['roles'][key][isp]:

            if sv.startswith("не"):
                sv = sv.lstrip("не")

            print(f"Для {isp} заменить {sv} на не {sv}")
