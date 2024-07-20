def load(filename):
    f = open(filename, "r", encoding="UTF-8")
    dp = []
    a = f.readlines()
    for i in a:
        i = i.rstrip("\n")
        nums = i.split("\t")
        dp.append(nums)
    dp.pop(0)
    return dp
