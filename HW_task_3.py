# ---------------------- Задача 3 ------------------------------------------
files_names = ['test1.txt', 'test2.txt', 'test3.txt']

all_data = {}

for file in files_names:
    with open(file, 'r', encoding='utf-8') as fl:
        data = fl.readlines()
        all_data[file] =[len(data), data]

result_str = ''
while all_data:
    min_len_value = min(all_data, key=all_data.get)
    result_str += min_len_value+'\n'
    result_str += str(all_data[min_len_value][0])+'\n'
    for i in all_data[min_len_value][1]:
        result_str += i.strip('\n') + '\n'
        # with open('result.txt', 'a', encoding='utf-8') as fl:
        #     fl.write(i)
    del all_data[min_len_value]

with open('result.txt', 'w', encoding='utf-8') as fl:
    fl.write(result_str)
