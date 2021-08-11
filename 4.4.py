source_list = [el - 1 if el % 3 == 0 else el + 1 for el in range(10, 20)]

dest_list = []
for i in source_list:
    if source_list.count(i) < 2:
        dest_list.append(i)
print(source_list)
print(dest_list)
