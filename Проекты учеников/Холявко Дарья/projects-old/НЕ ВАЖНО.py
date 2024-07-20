import json

t = 'Что вы хотите сделать?'

Что_вы_хотите_сделать = input(t)
Ресурсы = input('Какие у вас есть ресурсы?').split()

m = []

Зачем = input(f'А зачем вам {Что_вы_хотите_сделать}?')

while Зачем != '.':
    m.append(Зачем)
    Зачем = input('А зачем вам это?')

dictionary = {"Что_вы_хотите_сделать":Что_вы_хотите_сделать, 'Ресурсы':Ресурсы, 'Зачем':Зачем}

f = open('Что_вы_хотите_сделать.json', 'w')
json.dump(dictionary, f)
f.close()

f = open('Что_вы_хотите_сделать.json', 'r')
dictionary = json.load(f)

answer1 = f"{dictionary['Что_вы_хотите_сделать']} делать не надо."
print(answer1)

answer2 = f'{dictionary["Что_вы_хотите_сделать"]} произойдёт само собой.'
print(answer2)

for res in dictionary['Ресурсы']:
    print(f'Вы можете {dictionary["Что_вы_хотите_сделать"]} с помощью {res}.')

for i in m:
    print(f'{dictionary["Что_вы_хотите_сделать"]} делать не надо, но цель {i} достичь.')

from csv_reader import load

a = load('TRIZ.csv')

import random

b = random.choice(a)

print(f'Может быть вам подойдёт решение {b[0]} {b[1]} {b[2]}?')
