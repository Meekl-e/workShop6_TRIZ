def load(fileName):
    F = open(fileName, "r", encoding="UTF-8")
    dp = []

    for line in F.readlines():
        line = line.rstrip("\n")
        nums = line.split("\t")
        dp.append(nums)
    return dp
