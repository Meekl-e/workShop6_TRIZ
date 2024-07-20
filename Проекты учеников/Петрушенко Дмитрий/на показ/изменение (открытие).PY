import json
f = {}
f = open('../общее/test.json', 'r', encoding="utf-8")
tt = json.load(f)

for i in range(len(tt["features"])):
     print(tt["system"], 'не' + tt["features"][i])

for key in(tt["roles"]):
     for isp in(tt["roles"][key]):
          for sv in(tt["roles"][key][isp]):
               print(isp, 'не' + sv)
print(tt["change"], 'не надо')
print(tt["scenario"], 'произойдет само собой')
for i in range(len(tt["res"])):
     print(tt["change"], 'можно с помощью', tt["res"][i])
print(tt["change"], '')
print('Зачем', tt["change"])
pipetka = input()
print('Не надо ',tt['change'], ', надо ',pipetka, sep='')
print('Есть ли другие способы', tt["scenario"])
pipetka = input()
print('Не надо ',tt['scenario'], ', надо ',pipetka, sep='')