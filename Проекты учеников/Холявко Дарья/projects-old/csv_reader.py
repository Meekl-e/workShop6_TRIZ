def load(FileName):
    f = open(FileName, 'r', encoding="utf-8")
    dp = []

    for line in f.readlines():
        line = line.rstrip('\n')
        nums = line.split('\t')
        dp.append(nums)

    return dp
