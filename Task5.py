proceeds = float(input('Введите выручку фирмы '))
costs = float(input('Введите издержки фирмы '))
if proceeds > costs:
     print(f"Фирма работает с прибылью. Рентабельность выручки составила {proceeds / costs:.2f}")
     workers = int(input("Введите количество сотрудников фирмы "))
     print(f"прибыль в расчете на одного сотрудника составила {(proceeds - costs) / workers:.2f}")
else:
     print("Фирма работает в убыток")
