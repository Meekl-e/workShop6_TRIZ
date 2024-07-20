print('Здраствуйте, что вы хотите сделать?')
change = input(' :')
answer = [change]
#res2 = []
#print('Впишите пожалуйста сколько у вас предметов')
#res1 = int(input(' :'))
#for i in range(res1):
#    res2.append(input(' :'))
while answer[-1] != '.':
     print('А зачем вам', answer[-1], '?')
     answer.append(input(' :'))
answer.pop(0)
print('Вам нужно не', change, ', а', answer)
