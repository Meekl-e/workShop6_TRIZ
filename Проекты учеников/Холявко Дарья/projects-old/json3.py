import json

t = 'Что вы хотите сделать?'

task = input(t)
resources = input('Какие у вас есть ресурсы?').split()
zachem = input(f'А зачем вам {task}?')

dictionary = {'task':task, 'resources':resources, 'zachem':zachem}

f = open('task.json', 'w')
json.dump(dictionary, f)
f.close()

scenario = {}

roles = input('Какие у вас есть роли в задаче?').split()
