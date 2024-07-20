import json

f = {}
f = open('test.json', 'r', encoding="utf-8")
tt = json.load(f)

change = tt["task"]
answer1 = f"{change} делать не надо."
print(answer1, end="\n\n")
answer2 = f"{change} произойдёт само сабой."
print(answer2, end="\n\n")
res2 = tt["roles"]
res1 = len(tt["res"])

for role in res2.keys():
    for res in res2[role]:
        print('На роль', role,'подойдёт', res)
print(change, 'делать не надо, а цель достигнуть')