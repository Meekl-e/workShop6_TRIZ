def load(filename, sep):
    dp = []
    f= open(filename, "r", encoding="utf-8")
    for line in f.readlines():
        line= line.rstrip("\n")
        s = line.split(sep)
        dp.append(s)
    return dp
