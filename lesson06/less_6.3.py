class Worker:
    """Родительский класс со словарём"""
    def __init__(self,name,surname,position):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {"salary": 70000, "bonus": 13000}

class Position(Worker):
    """Дочерний класс с 2 методами"""

    def get_full_name(self):
        print("Имя и фамилия сотрудника")
        return self.name+" "+self.surname

    def get_total_income(self):
        print("Полная зарплата")
        return sum(self._Worker__income.values())

###########
#1.Проверить работу примера на реальных данных (создать экземпляры класса Position,передать данные.
#2.Проверить значения атрибутов
#3.вызвать методы экземпляров.
###########

# 1.Созданы 2 экземпляра класса Position(объектов)

employee1=Position("Pavel","Kovin","Designer")
employee2=Position("Denis","Kustov","Developer")

#2. Проверка значения атрибутов
print(employee1.name)
print(employee2.name)

#3.Вызов методов экземпляров.

print(employee1.get_full_name())
print(employee1.get_total_income())

print(employee2.get_full_name())
print(employee2.get_total_income())





