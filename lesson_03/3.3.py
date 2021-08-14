def my_func(num1, num2, num3):
    my_list = []
    my_list.append(num1)
    my_list.append(num2)
    my_list.append(num3)
    #  print(my_list)
    my_list.sort(reverse=True)
    #  print(my_list)
    summa = my_list[0] + my_list[1]
    print("Сумма равна ", summa)

my_func(10, 20, 15)
