def symb_compare():
    for element in input("Введите слова через пробел из латинских строчных букв:\n").split():
        s = 0
        for sym in element:
            if 97 <= ord(sym) <= 122:
                s += 1
        if s == len(element):
            print(element.title(),end= " ")


symb_compare()
