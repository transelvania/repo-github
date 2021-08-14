import re
import json

file = open("text_7.txt", "r", encoding="utf-8")
firm_list = []
prib_list = []
prib_all = int(0)  # Переменая для суммирования все прибыли фирм (без отрицательных значений)
plus_counter = int(0)  # Переменная для подсчёта кол-ва фирм с положительной прибылью (без убытков)
firm_dict = {}
result_list=[]

for line in file:
    file = open("text_7.txt", "r", encoding="utf-8")
    content = re.split(" |\n", line)
    file.close()
    firm_list.append(content)

print("Исходный список, считанный из файла:\n", firm_list,"\n")

for i in range(0, len(firm_list)):
    print("Прибыль компании ", firm_list[i][0])
    prib = (int(firm_list[i][2]) - int(firm_list[i][3]))
    prib_list.append(firm_list[i][0])
    prib_list.append(prib)
    if prib > 0:
        prib_all = prib_all + prib
        plus_counter = plus_counter + 1
    print(prib)
    # print(prib_list.append(prib))

average_profit=int(prib_all / plus_counter)
print("\n")
print("Прибыль компаний, представленная в виде списка: \n", prib_list, "\n")
print("Средняя прибыль компании: \n", average_profit,"\n")

firm_dict = {prib_list[i]: prib_list[i + 1] for i in range(0, len(prib_list), 2)}
firm_dict["average_profit"]=average_profit
result_list.append(firm_dict)
print("Словарь помещен в список по условию задания \n",result_list)

with open("json7.json", "w",encoding="utf-8") as res_file:
    json.dump(result_list[0], res_file)
