#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример: - 6782 -> 23; - 0,56 -> 11

# number = input('Введите вещественное число - ')

# sum = 0
# for digit in number:
#     if digit.isdigit():
#         sum += int(digit)
# print(sum)

n = list(input())
n = [int(digit) for digit in n if digit.isdigit()]
print(sum(n))