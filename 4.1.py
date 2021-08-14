from sys import argv

print(argv)

name, hour, stavka, prem = argv
print("Ваша зарплата ", (int(hour) * int(stavka)) + int(prem), " тугриков")
