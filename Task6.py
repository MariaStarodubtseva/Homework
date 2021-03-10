a = int(input("Введите результаты первого дня пробежки в км "))
b = int(input("Введите желаемый результат пробежки в км "))
days = 1
distance = a
while (distance-(b*0.10)) < b:
    a = a + 0.1 * a
    days += 1
    distance = a + 0.1 * a
    print(f'{days}-й день: {a:.2f}')
print(f"Вы достигнете требуемых показателей на %d день" % days)
