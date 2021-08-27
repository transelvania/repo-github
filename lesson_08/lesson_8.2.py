class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt

while True:
    a = input("Введите делимое: ")
    b = input("Введите делитель: ")
    if a == "stop" or b == "stop":
        print("Программа прервана пользователем")
        break
    else:
        try:
            a = int(a)
            b = int(b)
            if b == 0:
                raise MyException(f"Введите делитель, отличный от {b}")
        except (ValueError, MyException) as err:
            print(err)
        else:
            print(a / b)
