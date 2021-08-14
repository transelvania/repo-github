from itertools import count

# from itertools import cycle
start = int(input("Введите стартовое число "))
stop = int(input("Введите конечное число "))

for n in count(start):
    if n > stop:
        break
    else:
        print(n)
