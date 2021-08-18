from time import sleep
from colorama import Fore, Back, Style


# dict_color = {1: "red", 2: "yellow", 3: "green"}

class TrafficLight:
    # атрибуты класса
    def __init__(self):
        self.__color = "green"

    # методы класса
    def running(self):
        n = 0
        while n < 4:
            print(Fore.RED + "Красный")
            sleep(7)
            print(Fore.YELLOW + "Жёлтый")
            sleep(2)
            print(Fore.GREEN + "Зелёный", "\n")
            sleep(3)
            n += 1


state = TrafficLight()
state.running()
