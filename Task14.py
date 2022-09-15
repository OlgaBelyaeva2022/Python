# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 


def get_fibonacci(n):
    if n in [1, 2]:                       
        return 1
    else:
        return get_fibonacci(n-1) + get_fibonacci(n-2)

def get_negFibonacci(n):
    num1, num2 = 1, -1
    for i in range(2, n):
        num1, num2 = num2, num1 - num2
    return num2

fibo_list = [0]
k = int(input('Введите число: '))
for e in range(1, k + 1):
    fibo_list.append(get_fibonacci(e))
    fibo_list.insert(0, get_negFibonacci(e))
print(fibo_list)