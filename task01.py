# Task 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(a, b):
     return a/b

try:
    divident = float(input("Input divident: "))
    divisor  = float(input("Input divisor: "))
    try:
        print(division(divident,divisor))
    except ZeroDivisionError:
        print(f"Divison by zero detected. Divisor is {divisor}")

except ValueError:
    print("Arguments should be float values")

