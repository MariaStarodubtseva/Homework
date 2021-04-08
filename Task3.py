class NotNumberException(ValueError):
    pass


numbers_list = []

while True:
    user_input = input('Введи число или stop: ')

    if user_input == 'stop':
        break

    try:
        try:
            numbers_list.append(int(user_input))
        except ValueError:
            raise NotNumberException
    except NotNumberException:
        print('наш обработчик сработал')

print(f'Вот твои числа: {numbers_list}')
