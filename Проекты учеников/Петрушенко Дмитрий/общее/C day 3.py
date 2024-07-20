import json
print('сколько ролей в задаче?')

tt = {}
print ('Какая роль в задаче')
исполнитель = input(' :')
роль = input(' :')
print ('Кто в нашей задаче будет', роль)
tt[роль] = исполнитель

f = open('test.json', 'w', encoding="UTF-8")
json.dump(tt, f)
f.close()