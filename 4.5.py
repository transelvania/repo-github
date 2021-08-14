from functools import reduce

source_list = [el for el in range(100, 1001) if el % 2 == 0]
print(source_list)


def my_red(el1, el2):
    return el1 * el2


print(reduce(my_red, source_list))
