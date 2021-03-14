my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {my_list}")
new_element = int(input("Введите число: "))
my_list.insert(0, new_element)

sorted_list = []

while my_list:
    minimum = my_list[0]
    for item in my_list:
        if item > minimum:
            minimum = item
    sorted_list.append(minimum)
    my_list.remove(minimum)

print(f"Новый рейтинг - {sorted_list}")
