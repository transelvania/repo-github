list1 = input("Введите список через пробел:").split()

for n in range(1, len(list1), 2):
    list1[n - 1], list1[n] = list1[n], list1[n - 1]
print(list1)