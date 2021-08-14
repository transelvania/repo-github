import re

file = open("text_6.txt", "r", encoding="utf-8")
result_dict = {}
list = []  # Промежеточный список после парсинга файла
dis_list = []  # Список с перечнем дисциплин
duration_list = []  # Список с длительностью всех типов уроков по каждой дисциплине.
for line in file:
    file = open("text_6.txt", "r", encoding="utf-8")
    content = re.split("\n| |(пр)|(л)|\(", line)
    file.close()
    list.append(content)

for item in list:
    s = int(0)
    for el in item:
        try:
            s = s + int(el)
            # print(s)
        except ValueError:
            pass
        except TypeError:
            pass
    duration_list.append(s)

for i in range(0, len(list)):
    dis_list.append((list[i][0]))

# print(dis_list)
# print(duration_list)

result_dict = dict(zip(dis_list, duration_list))
print("Перечень дисциплин и их продолжительность \n ", result_dict)
