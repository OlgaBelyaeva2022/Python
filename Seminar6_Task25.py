#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#Пример: - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

from math import factorial

N = int(input('Введите число - '))
# f = []

# multi = 1
# for i in range(0, N):
#     multi *= i + 1
#     f.append(multi)
# print(f)

f = lambda N: N * factorial(N - 1)
list1 = list(f(i) for i in range(1, N+1))

print(list1) 






