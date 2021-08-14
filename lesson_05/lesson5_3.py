myfile = open("text_3.txt", "r", encoding="utf-8")
content = myfile.read()
myfile.close()
# print(content)

my_str = content.split()
sum1 = 0
sum2 = 0

print(my_str, "\n")
print("Зарплата сотрудников, указанных ниже, менее 20 000\n")
for i in range(1, len(my_str), 2):
    if float(my_str[i]) < 20000:
        print(my_str[i - 1])
        sum1 = sum1 + float(my_str[i])
    else:
        sum2 = sum2 + float(my_str[i])
print("\n", "Средняя зарплата сотрудника ", (sum1 + sum2) / (len(my_str) / 2))
