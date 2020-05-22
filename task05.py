# Task 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.

class Stationery:
    # !!! Закоментированные строки - не разобрался, можно ли передать значения
    # в родительский класс, как в этом примере
    # То есть, в базовом классе есть конструктор, который принимает значение,
    # а наследники не имеют в конструкторе принимаемого значения,
    # но записывают константу в базовый класс
    #def __init__(self, title):
    def __init__(self):
            self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def __init__(self):
#        super(Stationery).__init__(self, 'Pen')
        self.title = 'Pen'

    def draw(self):
        print("Отрисовка ручкой")


class Pencil(Stationery):
    def __init__(self):
#        super(Stationery).__init__(self, 'Pencil')
        self.title = 'Pencil'

    def draw(self):
        print("Отрисовка карандашом")


class Handle(Stationery):
    def __init__(self):
#        super(Stationery).__init__(self, 'Handle')
        self.title = 'Handle'

    def draw(self):
        print("Отрисовка маркером")

pen = Pen()
pencil = Pencil()
handle = Handle()

pen.draw()
pencil.draw()
handle.draw()