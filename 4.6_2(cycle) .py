from itertools import cycle

my_iter = int(input("Введите количество итераций "))

girls_names = ["Маша", "Даша", "Саша", "Глаша", "Наташа"]
c = 1
for el in cycle(girls_names):
    if c > my_iter:
        break
    print(el)
    c += 1
