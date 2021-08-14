myfile = open("text_1.txt", "w")
while True:
    user_str = input("Введите строку, пустую для завершения записи ")
    if len(user_str) == 0:
        print('Ввод строк завершён')
        break
    else:
        myfile = open("text_1.txt", "a")
        myfile.writelines(user_str)
        myfile.write('\n')
        myfile.close()