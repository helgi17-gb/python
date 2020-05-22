# Task 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, color, name):
        self.color = color
        self.name = name
        self.is_police = False
        self.speed = 0
        self.direction = 'forward'

    def go(self, speed):
        self.speed = speed

    def stop(self):
        self.speed = 0

    def turn(self, direction):
        self.direction = direction
        print(f"car turns {self.direction}")

    def show_speed(self):
        print(f"{self.color} {self.name} speed is now {self.speed}")

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Over speed")

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Over speed")

class SportCar(Car):
    def __new__(cls, color, name):
        if name == 'Ferrari' and color == 'red':
            instance = super(SportCar, cls).__new__(cls)
            return instance
        else:
            raise ValueError(f"{color} {name} is not a sportcar")

#    def __init__(self, color, name):
#        super(Car).__init__(color, "Ferrari")

class PoliceCar(Car):
    def __init__(self, color, name):
        super(Car).__init__(color, name)
        self.is_police = True

cars = []
try:
    sportcar1 = SportCar('green', 'ford')
    cars.append(sportcar1)
except ValueError as e:
    print(e)

try:
    sportcar2 = SportCar('red', 'Ferrari')
    cars.append(sportcar2)
except ValueError:
    print("something wrong")

workcar = WorkCar("green", "ford")
cars.append(workcar)

towncar = TownCar("yellow", "kopeika")
cars.append(towncar)

for car in cars:
    print('-'*20)
    car.go(10)
    car.show_speed()
    car.go(50)
    car.show_speed()
    car.go(100)
    car.show_speed()
    car.turn('left')
    car.turn('right')
    car.stop()
    car.show_speed()
