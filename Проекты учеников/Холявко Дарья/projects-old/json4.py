import json

f = open('task.json', 'r')
dictionary = json.load(f)
print(dictionary)

answer1 = f"{dictionary['task']} делать не надо."
print(answer1)

answer2 = f'{dictionary["task"]} произойдёт само собой.'
print(answer2)

for res in dictionary['resources']:
    print(f'Вы можете {dictionary["task"]} с помощью {res}.')

print(f'{dictionary["task"]} делать не надо, но цель {dictionary["zachem"]} достичь.')

from csv_reader import load

a = load('TRIZ.csv')

import random

b = random.choice(a)

print('Может быть вам подойдёт решение [0 + 1 + 2]?')
