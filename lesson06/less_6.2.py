class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def massa(self):
        print("Масса асфальта равна ", (float(self._lenght) * float(self._width) * 25 * 5 / 1000), "тонн")


asfalt = Road(10, 5000)
asfalt.massa()
