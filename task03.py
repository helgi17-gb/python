# Task 3. Реализовать функцию my_func(),
# которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(arg1, arg2, arg3):
    return sum([arg1, arg2, arg3]) - min([arg1, arg2, arg3])

arg1 = float(input("Input first argument: "))
arg2 = float(input("Input second argument: "))
arg3 = float(input("Input third argument: "))

print(my_func(arg1, arg2, arg3))
