from functools import reduce

def my_red(el1, el2):
    return int(el1) + int(el2)

source_list = [el - 1 if el % 3 == 0 else el + 1 for el in range(10, 20)]
myfile = open("text_5.txt", "w", encoding="utf-8")

for el in source_list:
    #print(el)
    myfile.write(str(el))
    myfile.write(" ")
myfile = open("text_5.txt", "r", encoding="utf-8")
content_string = myfile.read()
myfile.close()

content_list=content_string.split()

print(reduce(my_red,content_list))
