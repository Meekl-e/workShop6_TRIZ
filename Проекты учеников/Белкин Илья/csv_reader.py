def load(fileName):
    f = open(fileName, "r", encoding="UTF-8")
    dp = []
    for i in f.readlines():
        line = i.rstrip('\n')
        dp.append(line.split('\t'))
    return dp
