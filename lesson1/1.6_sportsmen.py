first_day = float(input("Введите количетво км в первый день:"))
resultat = float(input("Введите общее желаемое количетво км :"))

day = 1
curent = first_day
while curent < resultat:
    day = day + 1
    curent = curent + curent * 0.1
    print(f"День {day}. Километров пройдено {curent : .2f}")

print(f"Ответ: на {day} день спортсмен достиг результата — не менее {resultat: .2f} км")
