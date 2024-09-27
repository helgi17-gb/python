# Task 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def stream_sum(str, cumulative_sum=0, special="#"):
    terms = str.split(' ')
    stop_flag = False
    for term in terms:
        try:
            cumulative_sum += int(term)
        except ValueError:
            if term == special:
                stop_flag = True
                break
    return (cumulative_sum, stop_flag)


stop = False
sum = 0
while not stop:
    input_string = input("Input sequence of numbers: ")
    (sum, stop) = stream_sum(input_string, sum)
    print(sum)

