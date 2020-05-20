# Task 2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open("task02.txt", "r") as f:
    lines = f.readlines()
    print(f"Lines number: {len(lines)}")
    for i, line in enumerate(lines):
        print(f" line {i+1} consists of {len(line.split())} words")
