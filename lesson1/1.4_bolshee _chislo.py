a = int(input("Введите целое положительное число:"))
Bol = 0

while a > 0:
    if Bol < a % 10:
        Bol = a % 10
        a = a // 10
    else:
        a = a // 10
print(Bol)
