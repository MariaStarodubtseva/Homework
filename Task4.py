my_str = input('Введите строку из нескольких слов ')
for el in my_str.split():
    if len(el) <= 10:
        print(el)
    else:
        print(el[0:10:1])






