myfile = open("text_2.txt", "r", encoding="utf-8")
file = myfile.read()
myfile.close()

string_list = file.split("\n")
string_count = len(string_list)
print("Количество строк в файле ", string_count)
print("Количество слов в строке ")

for i in range(0, len(string_list)):
    # print(i)
    word_list = string_list[i].split()
    print("В строке ", i + 1, " ", len(word_list))