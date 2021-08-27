dlist = []

class Digit(Exception):
    def __init__(self, txt):
        self.txt = txt

while True:
    element = (input("Введите число (stop для прекращения ввода): "))
    if element == "stop":
        print("Ввод значений прекращен пользователем")
        break
    else:
        try:
            if not(element.isdigit()):
                raise Digit("Введена строка,а не число")
        except(Digit) as err:
            print(err)
        else:
                dlist.append(int(element))
print(dlist)
