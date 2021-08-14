def my_func(x, y):
    result = 0
    stepen = abs(y)-1
    while stepen != 0:
        x = x*x
        stepen = stepen - 1

    result = round(1 / x, 10)
    print(result)


my_func(5, -2)
