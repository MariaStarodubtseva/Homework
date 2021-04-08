class MyOwnZeroError(ZeroDivisionError):
    pass


a = 10
b = 0

try:
    if b == 0:
        raise MyOwnZeroError
    a / b
except MyOwnZeroError:
    print('моя ошибка деления на 0')
except ZeroDivisionError:
    print('ошибка деления на 0')

