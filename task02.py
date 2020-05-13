# Task 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def output_user_data(name, surname, birth_year, city, email, phone):
    print(f"name: {name}, surname: {surname}, birth year: {birth_year}, city: {city}, email: {email}, phone: {phone}")

person = input("Input person name and surname: ").lstrip().split(' ')
birth_year = int(input("Input person year of birh: "))
city = input("Input person city: ")
email = input("Input person email: ")
phone = input("Input person phone number: ")

output_user_data(name=person[0], surname=person[1], phone=phone, email=email,
                 city=city, birth_year=birth_year)