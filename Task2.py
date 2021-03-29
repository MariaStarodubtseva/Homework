class Road:
    __length = None
    __width = None

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calc(self, thickness, density):
        self.thickness = thickness
        self.density = density
        calc = self.length * self.width * self.thickness * self.density
        calc_in_ton = calc // 1000
        print(f'Нужно {calc_in_ton} т')

road1 = Road(20, 5000)
road1.calc(25, 5)


