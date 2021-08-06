name1 = input("Введите ваше имя:")
age1 = int(input("Введите ваш возраст:"))
name2 = input("Введите ваше имя:")
age2 = int(input("Введите ваш возраст:"))

if age1 > age2:
    print(f"Пользователь {name1} старше")
elif age2 > age1:
    print(f"Пользователь {name2} старше")
else:
    print(f"Пользователи {name1} и {name2} одногодки")
