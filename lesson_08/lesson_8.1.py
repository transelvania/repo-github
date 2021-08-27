my_dict = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
my_list = (input("Введите дату: ")).split("-")

class Date():
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def getdate(cls, data):
        d, m, y = data
        print(f"Число {d}\nМесяц {m}\nГод {y}\n")
        return cls(int(d), int(m), int(y))

    @staticmethod
    def checkdate(obj):
        try:
            if obj.day > (my_dict[obj.month]):
                print(f'Во {obj.month} месяце не может быть больше {my_dict[obj.month]} дней ')
        except KeyError as ke:
            print(f"Неверно введен номер месяца", ke)
        if obj.year > 2050 or obj.year<1900 :
            print("Введите год в диапазоне 1900-2050")

one = Date.getdate(my_list)
Date.checkdate(one)
