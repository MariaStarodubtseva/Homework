data_sum = 0

def summing(x):
    global data_sum
    for number in x.split():
        data_sum = data_sum + int(number)
    return f"Сумма чисел: {data_sum}"


while True:
    data = input("Введите строку чисел, разделённых пробелом или # для выхода: ")
    if data.find("#"):
        if data.endswith("#"):
            data = data.replace("#", "")
            print(summing(data))
            break
        else:
            print(summing(data))
    else:
        break