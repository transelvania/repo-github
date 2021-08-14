my_list = [7, 5, 3, 3, 2]
new_digit = float(input("Введите натуральное число: "))
i = 0
for n in my_list:
    if new_digit <= n:
        i = i + 1
    else:
        break
my_list.insert(i, new_digit)
print(my_list)
