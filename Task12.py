# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением
# дробной части элементов.
# Пример:- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5, 10.01]
list1 = []
for i in range(len(list)):
    list1.append(list[i]%1)
    list1=[round(v,2) for v in list1 if v%1 != 0]
print(list1)
print(max(list1)-min(list1))

