# Task 2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

list = []
list_item = '!'
while list_item != '' :
    list_item = input('Input list item or empty line to done: ')
    if list_item != '':
        list.append(list_item)

for item in list[0::2]: # Можно было бы сделать range, но хотелось использовать свойства выборки из списка
    idx = list.index(item)
    if idx != len(list)-1: # Здесь будет лишний проход при нечетном количестве
        tmp_value = list[idx]
        list[idx] = list[idx+1]
        list[idx+1] = tmp_value

print(list)
