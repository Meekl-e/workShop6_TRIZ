from общее.ljhl import load
yt = []
tt = load("TRIZ.csv", "\t")
matrix = load("PRIEMS.CSV", ";")
for i in range(1,39):
    print(matrix[i][1])
print('Выберете что вы хотите измененит(от 2, до 39)')
y = int(input(' :')) -1
for i in range(1,39):
    print(matrix[i][1])
if y.isdigit() == True:
    print('Выберете что при этом ухудшаеться(от 2 до 39)')
    x = int(input(' :')) +1
    if x.isdigit() == True and x > 1 and x < 40:
        if matrix[y][x] != '-' and matrix[y][x] != ' ' and matrix[y][x] != '\xa0':
            print('Возможно вам подойдет один из ниже перечисленых способов')
            for i in matrix[y][x].split(', '):
                i = tt[int(i)]
                print(f"{i[0]} это {i[1]} а точнее: {i[2]}")
        else:
            print('Решение не найдено в нашей базе')
else:
    print('Извените, вам требуеться ввести число')