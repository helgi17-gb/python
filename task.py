# == Лото ==
#
# Правила игры в лото.
#
# Игра ведется с помощью спе циальных карточек, на которых отмечены числа,
# и фишек (бочонков) с цифрами.
#
# Количество бочонков — 90 штук (с цифрами от 1 до 90).
#
# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
# расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
#
# --------------------------
#     9 43 62          74 90
#  2    27    75 78    82
#    41 56 63     76      86
# --------------------------
#
# В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
# случайная карточка.
#
# Каждый ход выбирается один случайный бочонок и выводится на экран.
# Также выводятся карточка игрока и карточка компьютера.
#
# Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
# Если игрок выбрал "зачеркнуть":
#     Если цифра есть на карточке - она зачеркивается и игра продолжается.
#     Если цифры на карточке нет - игрок проигрывает и игра завершается.
# Если игрок выбрал "продолжить":
#     Если цифра есть на карточке - игрок проигрывает и игра завершается.
#     Если цифры на карточке нет - игра продолжается.
#
# Побеждает тот, кто первый закроет все числа на своей карточке.
#
# Пример одного хода:
#
# Новый бочонок: 70 (осталось 76)
# ------ Ваша карточка -----
#  6  7          49    57 58
#    14 26     -    78    85
# 23 33    38    48    71
# --------------------------
# -- Карточка компьютера ---
#  7 87     - 14    11
#       16 49    55 88    77
#    15 20     -       76  -
# --------------------------
# Зачеркнуть цифру? (y/n)
#
# Подсказка: каждый следующий случайный бочонок из мешка удобно получать
# с помощью функции-генератора.
#
# Подсказка: для работы с псевдослучайными числами удобно использовать
# модуль random: http://docs.python.org/3/library/random.html


import random

#   Класс, отвечающий за генерацию номеров от 1 до 90
#   Применяется для заполнения карточек и
#   для непосредственно генерации потока бочонков в игре
#   не дает повторяться цифрам за счет изъятия номеров без возвращения
class Pocket:
    def __init__(self):
        self.pocket = list(range(1, 91))

    def __next__(self):
        if len(self.pocket) == 0: raise StopIteration
        return self.pocket.pop( random.randint(0,len(self.pocket)-1) )

    def __iter__(self):
        return self

#   Класс, отвечающий за карточку
#   Содержит матрицу карточки, имя карточки (или игрока)
#   Обеспечивает заполнение карточки из класса Pocket,
#   вычеркивание числа из карточки
#   Хранит переменную, содержащую количество невычеркнутых номеров
#   Обеспечивает печать карточки в виде, соответствующем требованиям
class Ticket:
    def __init__(self, name):
        self.name = name
        self.matrix = [['', '', '', '', '', '', '', '', ''],
                       ['', '', '', '', '', '', '', '', ''],
                       ['', '', '', '', '', '', '', '', '']]
        self.pocket = Pocket()
        while True:
            try:
                for row in range(3):
                    row_complete = 0
                    while row_complete<5:
                        val = next(self.pocket)
                        index = self.get_index(val)
                        if self.matrix[row][index] == '':
                            self.matrix[row][index] = val
                            row_complete += 1
                break
            except StopIteration:
                pass


        self.keep = 15

    def __str__(self):
        result = '---' + self.name + '-'*(24-len(self.name)) +'\n'
        for row in range(3):
            for col in range(9):
                if self.matrix[row][col] == '':
                    result += '   '
                else:
                    result += f"{str(self.matrix[row][col]):2} "
            result += '\n'

        result += '-'*27
        return result

    def get_index(self, number):
        index = number // 10
        if index > 8: index = 8
        return index

    def x_out(self, number, verbose = True):
       if number not in list(self.matrix[0] + self.matrix[1] + self.matrix[2]):
           if verbose: print("Такого числа нет на Вашей карточке")
       else:
           for row in range(3):
               if number in self.matrix[row]:
                   index = self.get_index(number)
                   self.matrix[row][index] = '-'
                   self.keep -= 1

#   Класс, содержащий логику игры
#   Инициализирует карточки игроков и класс генерации бочонков
#   Содержит функцию итерации для пошагового вызова в цикле for основной программы
#   Содержит функцию проверки выигрыша игроков
class Game:
    def __init__(self):
        self.pocket = Pocket()
        self.player_ticket = Ticket("Ваша карточка")
        self.computer_ticket = Ticket("Карточка компьютера")

    def __iter__(self):
        return self

    def __next__(self):
        p = next(self.pocket)
        print(f"Новый бочонок: {p} (осталось {len(self.pocket.pocket)})")
        print(self.player_ticket)
        print(self.computer_ticket)
        while True:
            self.choice = input("Зачеркнуть цифру? (y/n)")
            if self.choice == 'y':
                self.player_ticket.x_out(p)
                break
            elif self.choice == 'n':
                break
            else:
                print("input 'y' or 'n'")
        self.computer_ticket.x_out(p, verbose=False)
        self.check_win()

    def check_win(self):
        if self.player_ticket.keep == 0:
            if self.computer_ticket.keep == 0:
                print("Обоюдная победа")
                raise StopIteration
            else:
                print("Вы победили")
                raise StopIteration
        else:
            if self.computer_ticket.keep == 0:
                print("Компьютер выиграл")
                raise StopIteration


if __name__ == "__main__":
    game = Game()
    for step in game:
        pass

