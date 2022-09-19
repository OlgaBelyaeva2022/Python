# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.


with open('file19_1.txt', 'r') as data1, open('file19_2.txt', 'r') as data2:
    file19_1 = data1.readline()
    list_of_file19_1 = file19_1.split()
    file19_2 = data2.readline()
    list_of_file19_2 = file19_2.split()
        
print(f'{list_of_file19_1} + {list_of_file19_2}')
sum_list = list_of_file19_1 + list_of_file19_2

with open('file19_3.txt', 'w') as data3:
    data3.write(f'{list_of_file19_1} + {list_of_file19_2}')
