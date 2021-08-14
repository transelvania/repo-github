def my_summa():
    m = 0
    while True:
        string = (input("Введите числа,для выхода введите q: ").split())
        for el in string:
            if el == "q":
                return m
            else:
                try:
                    m += int(el)
                except ValueError:
                    print("Для выхода из программы нажмите q: ")
        print("Сумма равна ", m)
print("Сумма равна ", my_summa())