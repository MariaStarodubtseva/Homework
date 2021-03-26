file = open("task2.txt", "r")
strings = 0
while True:
    text = file.readline().split()
    if len(text) == 0:
        break
    print(text)
    print(f'Количество слов в строке -', len(text))
    strings += 1
file.close()
print(f'Всего строк в файле {strings}')