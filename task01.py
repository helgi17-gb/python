# Task 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--rate", type=str, help="rate")
parser.add_argument("--premium", type=str, help="premium")
parser.add_argument("--productivity", type=str, help="productivity")
try:
    args = parser.parse_args()
    rate = float(args.rate)
    premium = float(args.premium)
    productivity = float(args.productivity)

    salary = productivity * rate + premium
    print(f'Salary for rate={rate}, productivity={productivity} and premium={premium} is {salary}')
except ValueError:
    print("Arguments should be float value")
