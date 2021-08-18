class Car:
    """Родительский класс со словарём"""

    def __init__(self, speed, color, name, state):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = state

    def start(self):
        print("Машина поехала")

    def stop(self):
        print(self.name, "остановилась")

    def turn_direction(self, direction):
        self.turn_direction = direction
        print(self.name, "повернула", direction)

    def show_speed(self):
        print(self.speed)
        if (self.speed) > 120:
            print("Скорость превышена")
        else:
            print("Скорость не превышена")


class TownCar(Car):
    def show_speed(self):
        print(self.speed, " км/ч")
        if (self.speed) > 60:
            print("Скорость превышена")
        else:
            print("Скорость не превышена")


class WorkCar(Car):
    def show_speed(self):
        print(self.speed, " км/ч")
        if (self.speed) > 40:
            print("Скорость превышена")
        else:
            print("Скорость не превышена")


class PoliceCar(Car):
    pass


class SportCar(Car):
    pass


# Задания
# 1.Cоздайте экземпляры классов,передайте значения атрибутов
# 2.Выполните доступ к атрибутам,выведите результат.
# 3.Выполните вызов методов и также покажите результат.

# 1. Создайте экземпляры классов,передайте значения атрибутов.

TCar = TownCar(60, "brown", "Duster", False)  # Созданы экземпляр дочернего класса.Значения переданы
WCar = WorkCar(75, "blue", "Polo", False)  # в конструктор родительского класса.

# 2. Получен доступ к атрибутам.

print("Доступ к атрибутам")
print(TCar.name)
print(TCar.speed)
print(WCar.name)
print(WCar.speed)

# 3. Вызов 4 методов родительского класса (унаследованы) двумя экземплярами дочерних классов.

print("********")
TCar.start()
TCar.show_speed()
TCar.turn_direction("направо")
TCar.stop()
print("\n")

WCar.start()
WCar.show_speed()
WCar.turn_direction("налево")
WCar.stop()
print("\n")

# При вызове метода дочернего класса, так как он в нём отсутствует, вызывается метод родительского.
# Предыдущие методы были именно методами экземпляров.

Scar = SportCar(119, "brown", "Duster", False)
Scar.show_speed()
