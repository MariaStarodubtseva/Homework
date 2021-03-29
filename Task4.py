class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'Текущая скорость {self.name} составляет {self.speed}'

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость городского автомобиля {self.name} составляет {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} выше допустимой'
        else:
            return f'Скорость {self.name} допустимая'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость рабочего автомобиля {self.name} составляет {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} выше допустимой'
        else:
            return f'Скорость {self.name} допустимая'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

a = TownCar(63, 'Green', 'Daewoo Matiz', False)
b = SportCar(100, 'Yellow', 'Audi R8', False)
c = WorkCar(45, 'Grey', 'Lada Calina', True)
d = PoliceCar(110, 'Blue', 'Ford Tocus', True)
print(a.speed, a.color, a.name, a.is_police)
print(b.speed, b.color, b.name, b.is_police)
print(c.speed, c.color, c.name, c.is_police)
print(d.speed, d.color, d.name, d.is_police)
print(a.go())
print(b.stop())
print(c.turn_left())
print(d.turn_right())
print(a.show_speed())
print(c.show_speed())

