from abc import ABC, abstractmethod


class Clothes(ABC):
    total = 0

    def __init__(self, param1):
        self.param1 = param1

    @abstractmethod
    def calculation(self):
        pass


class Coat(Clothes):
    p = 0

    @property
    def calculation(self):
        Coat.p = Coat.p + 1
        print(f"Расход ткани на пальто номер {self.p} равно {round(Clothes.total + (self.param1 / 6.5 + 0.5), 3)} кв.м")
        Clothes.total = Clothes.total + round(Clothes.total + (self.param1 / 6.5 + 0.5), 3)
        return round(Clothes.total + (self.param1 * 0.02 + 0.3), 3)

class Suit(Clothes):
    p = 0
    @property
    def calculation(self):
        Suit.p = Suit.p + 1
        print(f"Расход ткани на костюм номер {self.p} равно {round(float(self.param1 * 0.02 + 0.3), 3)} кв.м")
        Clothes.total = Clothes.total + round(Clothes.total + (self.param1 * 0.02 + 0.3), 3)
        return round(Clothes.total + (self.param1 * 0.02 + 0.3), 3)


s1 = Suit(59)
c1 = Coat(59)

s1.calculation
c1.calculation

print(f"Общий расход ткани {Clothes.total} \n **************************************** \n")

