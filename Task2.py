time = int(input('Введите время в секундах - '))
hours = (time // 3600)
minutes = (time % 3600) // 60
seconds = (time % 3600) % 60
print(f'чч:мм:сс = {hours}:{minutes}:{seconds}')
