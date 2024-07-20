t = 'Что вы хотите сделать?'

task = input(t)
answer1 = f"{task} делать не надо."
print(answer1)

answer2 = f'{task} произойдёт само собой.'
print(answer2)

resources = input('Какие у вас есть ресурсы?').split()
for res in resources:
    print(f'Вы можете {task} с помощью {res}.')

a_zachem = input(f'А зачем вам {task}?')
print(f'{task} делать не надо, но цель {a_zachem} достичь.')

from csv_reader import load

load()