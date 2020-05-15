# Task 6. Реализовать два небольших скрипта:
# а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.

from itertools import count, cycle

print("Generator using count()")
for el in count(10):
    if el > 15:
        break
    else:
        print(el)
print(f"-")
print("Generator using cycle()")
i = 0
for el in cycle(['winter', 'spring', 'summer', 'autumn']):
    if i > 15:
        break;
    else:
        print(el)
        i += 1

