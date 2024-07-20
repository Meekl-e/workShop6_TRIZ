f = open('PRIEMS.CSV','r', encoding="utf-8")
dp = []

dp2 = []

triz = []

for line in f.readlines():
    line = line.rstrip('\n')
    nums = line.split(';')
    dp.append(nums)

for line in dp:
    print(line[1])

y = int(input('Что вы хотите изменить? (Ответьте числом от 1 до 39)'))+1

N = input()

if N.isdigit() == True:
    print()

for line in dp:
    print(line[1])

x = int(input('Что при этом ухудшится?(В ответе число от 1 до 39)'))+1

if N.isdigit() != True:
    print("Это не число!!!")

d = dp[y][x]

f = open('TRIZ.csv','r', encoding="utf-8")

for line in f.readlines():
    line = line.rstrip('\n')
    nums = line.split('\t')
    triz.append(nums)

t = d.split(", ")


if d != "-" and d!= " " and d!= "\xa0":
    for r in t:
        print(f"Возможно вам подойдёт {triz[int(r)][0]} {triz[int(r)][1]} {triz[int(r)][2]}")
else:
    print("К сожалению, нет возможных вариантов")
