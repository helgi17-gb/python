# Task 5. Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import random

with open("task05.txt", "w+") as f:
    for i in range(1,101):
       f.write(f"{random.randint(0,100)} ")

    f.seek(0)
    print (f"Sum of file numbers is {sum( map(lambda x: int(x), f.readline().split()) ) }")

