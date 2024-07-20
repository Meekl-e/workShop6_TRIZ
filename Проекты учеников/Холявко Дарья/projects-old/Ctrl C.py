import json

from colorama import init
from colorama import Fore, Back, Style
init()

f = open('task-new.json', 'r', encoding="utf-8")
dictionary = json.load(f)
print(dictionary)

answer1 = Back.MAGENTA + Fore.CYAN + f"{dictionary['task']} делать не надо." + Style.RESET_ALL
print(answer1)

answer2 = Back.CYAN + Fore.MAGENTA + f'{dictionary["task"]} произойдёт само собой.' + Style.RESET_ALL
print(answer2)

for res in dictionary['resources']:
    print (Back.BLACK + Fore.WHITE + f'Вы можете {dictionary["task"]} с помощью {res}.' + Style.RESET_ALL)

print(Back.RED + Fore.GREEN + f'{dictionary["task"]} делать не надо, но цель достичь.' + Style.RESET_ALL)


for role in dictionary["roles"].keys():
    print(role)
