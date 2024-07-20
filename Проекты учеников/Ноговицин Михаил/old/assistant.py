

task = input("Введите задачу: ")
change = input(f"А для чего {task}?")
ress = input(f"С помощью чего можно {task}?").split(", ")

print(f"{task} произойдет само собой")
print(f"{task} делать не надо")
for r in ress:
    print(f"{task} выполнить за счет {r}")
print(f"{task} делать не надо, а {change} достичь")


