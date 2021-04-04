class Cell:
    count = 0

    def __init__(self, count):
        Cell.count += 1
        self.num = Cell.count
        self.count = count

    def __str__(self):
        return f'Клетка № {self.num} имеет {self.count} ячеек'

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        if self.count - other.count < 0:
            raise ValueError('Разность количества ячеек < 0')
        return Cell(self.count - other.count)

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __floordiv__(self, other):
        return Cell(self.count // other.count)

    def __truediv__(self, other):
        return Cell(self.count // other.count)

    @staticmethod
    def make_order(cell, len):
        for _ in range(cell.count // len):
            print ('*' * len)
        print('*' * (cell.count % len))

cell_1 = Cell(10)
cell_2 = Cell(7) + cell_1
cell_3 = Cell(3) + cell_2

print(cell_3)

Cell.make_order(Cell(100), 33)