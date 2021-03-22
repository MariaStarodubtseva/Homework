from sys import argv
print(argv)

script_name, hours, rate_per_hour, bonus = argv

print("Выработка в часах ", hours)
print("Ставка в час ", rate_per_hour)
print("Премия ", bonus)

salary = (int(hours) * int(rate_per_hour)) + int(bonus)
print(f'заработная плата сотрудника  {salary}')
