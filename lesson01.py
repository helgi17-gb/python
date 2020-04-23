# Задание 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные,
# выведите на экран.

print('Task 1')
print('='*20)
first = 1
second = 'second'
third = 33.3
print(f'first {first}, second {second}, third {third}')
name = str(input('Input name: '))
surname = str(input('Input surname: '))
age = int(input('Input age: '))
footsize = float(input('Input footsize: '))
print(f'Name: {name}, Surname: {surname}, age: {age}, footsize: {footsize}')

print('='*20)


# Задание 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

# !!! Формат для форматирования взял со стороннего сайта
# (https://dev-gang.ru/article/python-recepty-formatirovaniya-strok/)
# Как применяется такой формат тоже нашел на стороннем сайте
# (https://shultais.education/blog/python-f-strings). Раздел "Погружение в f-строки"
# Думаю эту информацию можно добавить в методичку

print('Task 2')
print('='*20)
time = int(input('Input time in seconds: '))
hours = time // 3600
minutes = (time % 3600) // 60
seconds = (time - hours*3600 - minutes*60)
hours %= 24 # так как не сказано, что делать в случае переполнения
            # (для часов оставлено только два разряда),
            # предполагаю отсечение часов посуточно, а не по 99
print(f'{hours:0>2d}:{minutes:0>2d}:{seconds:0>2d}')
print('='*20)

# Задание 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

print('Task 3')
print('='*20)
n = int(input('Input number n: '))
if (n>0): # нет чисел -1-1 и -1-1-1, 00 и 000, но есть числа 123123 и 123123123
    double_n = int(str(n)*2)
    triple_n = int(str(n)*3)
    sum = n + double_n + triple_n
    print(f'{n} + {double_n} + {triple_n} = {sum}')
else:
    print(f'number n ({n}) can not be a part of number nn and nnn')
print('='*20)

# Задание 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

print('Task 4')
print('=' * 20)
number = int(input('Input positive integer: '))
if (number > 0):
    max_digit = 0  # число целое положительное, значит будет хотя бы одна цифра больше 0
                   # 0 поэтому недопустимый символ для max_digit
    while number > 0:
        remainder = number % 10
        if remainder > max_digit:
            max_digit = remainder
        number = number // 10
    print(f'max digit is {max_digit}')
else:
    print(f'{number} does not appear to be positive integer')
print('=' * 20)

# Задание 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

print('Task 5')
print('=' * 20)
revenue = float(input('Input company revenue: '))
costs = float(input('Input company costs: '))
if revenue >= 0 and costs >=0:
    if revenue < costs:
        print('Company is operating at a loss')
    elif revenue == costs:
        print('Company break even (no profit or loss)')
    else:
        print('Company is profitable')
        cost_effectiveness = (revenue-costs)/revenue    # Проверка на 0 в знаменателе не нужна
                                                        # т. к. мы проверили, что оба показателя >=0,
                                                        # а в этой ветви условия revenue > costs строго.
                                                        # то есть не 0.
        print(f'Company cost-effectiveness is {cost_effectiveness}')
        members = int(input('Input number of employees: '))
        if members <= 0:
            print(f'Company can not consists of {members} number of employees')
        else:
            personal_gain = (revenue-costs)/members
            print(f'Personal gain is {personal_gain}')

else:
    print('revenue and costs should be greater or equal then 0')
print('=' * 20)

# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
#
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

# Полагаю, что все же '.' должны стоять в числах с плавающей точкой в результате вывода

print('Task 6')
print('=' * 20)
factor = 0.1
a = float(input('Input distance at the begining: '))
b = float(input('Input distance threshold: '))
if a>0 and b>=0: # В случае a = 0, цикл не остановится. Зачем это нам?
    day = 1
    print(f'{day}-й день: {a:.3g}')
    while a<b:
        a += a*factor
        day += 1
        print(f'{day}-й день: {a:.3g}')
    print(f'Ответ: на {day}-й день спортсмен достиг результата - не менее {b:.3g} км.')
else:
    print('Initial distance should be greater then 0 and threshold should be greater or equal 0 ')
print('=' * 20)
