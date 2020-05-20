# Task 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

translate = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("task04.txt", "r") as f:
    lines = f.readlines()
    output = [f"{translate[str.split()[0]]} {' '.join(str.split()[1:])}" for str in lines]
    with open("task04.out", "wt") as out:
        out.writelines("\n".join(output))