class Kletka:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) + '\n' + "*" * (self.nums % rows)

    def __add__(self, other):
        print("Сумма клеток равна")
        return Kletka(self.nums + other.nums)

    def __str__(self):
        return f'{self.nums}'

    def __sub__(self, other):
        print("Разница клеток равна")
        return Kletka(self.nums - other.nums) if self.nums - other.nums > 0 else print("Вычитанме невозможно")

    def __mul__(self, other):
        print("При умножении клеток мы получим")
        return Kletka(self.nums * other.nums)

    def __floordiv__(self, other):
        print("При делении клеток мы получим")
        return Kletka(self.nums // other.nums)


cell1 = Kletka(14)
cell2 = Kletka(9)

print(cell1*cell2)
print(cell1+cell2)
print(cell1-cell2)

print(cell1.make_order(5))
print (f'\n')
print(cell2.make_order(3))