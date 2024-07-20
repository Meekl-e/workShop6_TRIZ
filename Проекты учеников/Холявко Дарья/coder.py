import json

dictionary = {}

dictionary['system'] = input('Что или кто главный в вашей задаче?')

dictionary['description'] = input('Пожалуйста, запишите полностью Вашу задачу')

dictionary['task'] = input('Что нужно сделать в Вашей задаче?')

dictionary['features'] = input(f'Назовите свойства {dictionary["system"]}')

dictionary["roles"] = {}

roles = input("Введите роли").split(", ")

for role in roles:
    dictionary["roles"][role] = {}
    isps = input(f"Введите исполнителя на роль {role}").split(", ")
    for isp in isps:
        features = input("Введите свойства данного исполнителя").split(", ")
        dictionary["roles"][role][isp] = features

dictionary['type'] = 1

dictionary['resouces'] = input("Какие у вас есть ресурсы?")

dictionary['scenario'] = input('Какой сценарий в Вашей задаче?')

f = open("task-new.json", "w", encoding="utf-8")

json.dump(dictionary, f, indent=4)

