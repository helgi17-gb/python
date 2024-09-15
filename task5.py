# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]

while True:
    try:
        rank = int(input('Введите новый элемент рейтинга: '))
        if rank > 0:
            idx = len(my_list) - 1
            while idx >= 0 and my_list[idx] < rank:
                idx -= 1
            my_list.insert(idx+1, rank)
            str_list = []
            for rank_item in my_list:
                str_list.append(str(rank_item))
            print(f"Пользователь ввел число {rank}. Результат: {', '.join(str_list)}")
        else:
            print("Рейтинг должен быть натуральным числом")
    except ValueError:
        print("Ошибочное значение рейтинга")