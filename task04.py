# Task 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def simple_my_func(x, y):
    return x**y

def my_func(x, y):
    res = 1
    for i in range(0, y, -1):
        res /= x
    return res

try:
    value = float(input("Input value: "))
    exponent = int(input("Input exponent: "))
    if exponent >= 0:
        print("Error: exponent should be less then 0")
    else:
        print(f"Function, using ** returns: {simple_my_func(value, exponent)}")
        print(f"Function, not using ** returns: {my_func(value, exponent)}")
except ValueError:
    print("Value should be float, exponent should be integer")