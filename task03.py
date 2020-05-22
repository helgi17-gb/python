# Task 3. Реализовать базовый класс Worker (работник),
# в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return sum([ v for k, v in self._Worker__income.items()])


worker1 = Position("Ian", "Ivanov", "director", 10, 10)
worker2 = Position("Basil", "Petrov", "master", 100, 100)

print(f"{worker1.get_full_name()}: {worker1.get_total_income()}")
print(f"{worker2.get_full_name()}: {worker2.get_total_income()}")
