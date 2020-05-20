# Task 1. Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open("task01.txt","wt") as f:
    user_input = ' '
    while user_input != '':
        user_input = input("Input string: ")
        f.writelines(f"{user_input}\n")