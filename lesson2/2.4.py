str1 = input("Введите элементы через пробел:")
list1 = str1.split()

for i in range(0, (len(list1))):
    if len(list1[i]) < 10:
        print(f"Строка номер {i + 1}", list1[i])
    else:
        print(f"Строка номер {i + 1}", list1[i][:10])
