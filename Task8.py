#Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

n = int(input('Введите число: ')) 

def get_sequence(n):
    return [round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]

numbers = get_sequence(n)
print(numbers)
print(round(sum(numbers), 2))