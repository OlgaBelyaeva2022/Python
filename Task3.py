#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

a = int(input('Введите номер четверти для выведения диапозона возможных координат точек - '))

if a == 1:
    print('все положительные')
elif a == 2:
    print('по оси x отрицательные, по оси y положительные')
elif a == 3:
    print('все отрицательные')
elif a == 4:
    print('по оси y отрицательные, по оси x положительные')
else:
    print('error')