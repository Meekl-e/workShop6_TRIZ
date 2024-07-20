import json
f = {}
f = open('test.json', 'r', encoding="utf-8")
tt = json.load(f)
print(tt["task"], "делать не надо.")
print(tt["task"], "произойдёт само собой.")
#for i in range(len(tt['res'])):
print(tt["task"], "осуществиться с помошью", tt["res"])
print('делать не надо', tt["task"], 'надо', tt["goal"], end="\n\n")