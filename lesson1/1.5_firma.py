viruchka = float(input("Введите выручку фирмы: "))
izderzhki = float(input("Введите издержки фирмы: "))
pribil = viruchka - izderzhki
if pribil < 0:
    print("Ваша компания работает в убыток")
elif pribil == 0:
    print("Ваша компания работает в ноль")
elif pribil > 0:
    print(f"Ваша компания работает c прибылью {pribil}")
    print(f"Рентабельность фирмы {100*pribil/viruchka :.1f}%")
    staff = int(input("Введите количество сотрудников фирмы: "))
    print(f"Прибыль фирмы с рассчётом на одного  сотрудника {pribil/staff: .1f}")

