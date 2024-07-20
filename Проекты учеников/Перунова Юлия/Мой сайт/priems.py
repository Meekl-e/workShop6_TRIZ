f = open('PRIEMS.CSV', 'r', encoding="utf-8")
fail = open('../TRIZ.csv', 'r', encoding="utf-8")

dp = []
triz = []
for line in f.readlines():  #цикл для заполнения списка dp содержимым файла PRIEMS.CSV
    line = line.rstrip('\n')
    nums = line.split(';')
    dp.append(nums)
for line in fail.readlines():  #цикл для заполнения списка triz содержимым файла TRIZ.csv
    line = line.rstrip('\n')
    nums = line.split('\t')
    triz.append(nums)

#функция для выпадающего листа, не принимающяя на вход ничего и выводящая список того, что хотят улучшить или то, что должно ухудшиться
def down_list():

    sp = []
    for line in range(len(dp)):
        if line != 0:
            sp.append(dp[line][1][4:])
    return sp

#функция, принимающая на вход x и y и выводящая список из подходящих приёмов или говорящая, что подходящего приёма нет
def answer(x, y):

    x += 1
    y += 2
    d = dp[x][y]

    t = d.split(", ")

    if d != "-" and d != " " and d != "\xa0":
        sp = []
        for r in t:
            sp.append(f"{triz[int(r)][0]} {triz[int(r)][1]} {triz[int(r)][2]}")
            
        return list(enumerate(sp))
    else:
        sp = []
        sp.append("К сожалению, нет возможных вариантов")
        return list(enumerate(sp))