def my_func (a, b):
    return a/b

a = int(input('Введите первое число: '))
if a == 0:
    exit("Ошибка! На ноль делить нельзя")

b = int(input('Введите второе число: '))
if b == 0:
    exit("Ошибка! На ноль делить нельзя")

print(f'Результат деления: ', my_func(a, b))


