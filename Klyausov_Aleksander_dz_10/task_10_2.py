from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def consumption(self):
        """Расход ткани"""
        pass

    @abstractmethod
    def __str__(self):
        """Название изделия"""
        pass


class Coat(Clothes):
    def __init__(self, name, v):
        super().__init__()
        self.name = name
        self.v = v

    def __str__(self):
        return f'Название изделия {self.name}'

    @property
    def consumption(self):
        return f'Расход ткани {round(self.v / 6.5 + 0.5, 2)}'


class Suit(Clothes):
    def __init__(self, name, h):
        super().__init__()
        self.name = name
        self.h = h

    def __str__(self):
        return f'Название изделия {self.name}'

    @property
    def consumption(self):
        return f'Расход ткани {round(2 * self.h + 0.3, 2)}'


coat = Coat("Duffel coat", 50)
suit = Suit("Burberry", 1.8)

print(coat)
print(coat.consumption)
print(suit)
print(suit.consumption)
