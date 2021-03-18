def user_info(name, surname, year, city, email, phone):
    name = input('Введите своё имя: ')
    surname = input('Введите свою фамилию: ')
    year = input('Введите год своего рождения: ')
    city = input('Введите город своего рождения: ')
    email = input('Введите Ваш email: ')
    phone = input('Введите Ваш номер телефона: ')
    return ' '.join([name, surname, year, city, email, phone])

final = user_info('name - {name}', 'Фамилия - {surname}', 'Год рождения - {year}', 'Город - {city}', 'Email - {email}',
                  'Телефон - {phone}')
print(final)
