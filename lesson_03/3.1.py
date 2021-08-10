def my_div(arg1, arg2):
    return arg1 / arg2


a = int(input("Введите делимое:"))
b = int(input("Введите делитель,не равный нулю:"))

while b == 0:
    b = int(input("Введите делитель,не равный нулю:"))

print(f"Частное равно ", (my_div(a, b)))
