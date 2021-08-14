def user_info():
    name = (input("Введите имя"))
    surname = (input("Введите фамилию"))
    birth_year = int(input("Введите год рождения"))
    city = (input("Введите город проживания"))
    email = (input("Введите email"))
    phone = (input("Введите номер телефона"))
    return [name, surname, birth_year, city, email, phone]


print(user_info())
