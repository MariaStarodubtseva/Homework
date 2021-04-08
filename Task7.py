class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print(f'{self.a} + {self.b}i')

    def __add__(self, other):
        print(f'Сумма n1 и n2 = ')
        return f'{self.a + other.a} + {self.b + other.b}i'

    def __mul__(self, other):
        print(f'Произведение n1 и n2 = ')
        return f'{self.a * other.a - (self.b * other.b)} + {self.a * other.b +(other.a * self.b)}i'

    def __str__(self):
        return f'{self.a} + {self.b}i'


n1 = ComplexNumber(1, -2)
n2 = ComplexNumber(3, 4)
print(n1 + n2)
print(n1 * n2)