# Task 3. Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open("task03.txt", "r") as f:
    team = f.readlines()
    low_employee = [mmbr.split()[0] for mmbr in team if float(mmbr.split()[1])<20000]
    print(f"List of employees with salary under 20000: {low_employee}")
    salary = list( map(lambda x: float(x.split()[1]), team) )
    print(f"Average salary is {sum(salary)/len(salary)}")
