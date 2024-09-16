# Task 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fibo_gen().
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые 15 чисел.
# Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

def factorial():
    i=0
    f=1
    while True:
        if i != 0:
            f = f * i
        i += 1
        yield f

i=0
for el in factorial():
   if i > 15:
       break
   else:
       print(el)
       i += 1