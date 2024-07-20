f = open('PRIEMS.CSV', 'r', encoding="utf-8")
fail = open('TRIZ.csv', 'r', encoding="utf-8")

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

#функция для выпадающего листа, не принимающяя на вход ничего и выводящая список
def down_list():

    sp = []
    for line in range(len(dp)):
        if line != 0:
            sp.append(dp[line][1][4:])
    return sp

def answer(x, y):
    if x == -1 or y == -1:
        return []
    x += 1
    y += 1
    d = dp[x][y]

    print(y, x)

    t = d.split(", ")

    if d != "-" and d != " " and d != "\xa0":
        sp = []
        for r in t:
            sp.append(f"{triz[int(r)][0]} {triz[int(r)][1]} {triz[int(r)][2]}")
            
        return sp
    else:
        sp = []
        sp.append("К сожалению, нет возможных вариантов по таблице применения устранения технических противоречий")
        return sp