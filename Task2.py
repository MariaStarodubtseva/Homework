from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self._v = v

    @property
    def amount(self):
        return self._v / 6.5 + 0.5

    def __str__(self):
        return f'Для создания пальто c размером {self._v} необходимо {self.amount} материала'

class Suit(Clothes):
    def __init__(self, h):
        self._h = h

    @property
    def amount(self):
        return 2 * self._h + 0.3

    def __str__(self):
        return f'Для создания костюма c ростом {self._h} необходимо {self.amount} материала'

print(Coat(v=7))
print(Suit(h=7))

