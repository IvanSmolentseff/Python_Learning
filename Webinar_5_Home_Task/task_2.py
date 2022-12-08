'''Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.'''

with open('Task_1.txt', 'r', encoding='utf-8') as f_obj:
    row = 0
    letters = 0
    for line in f_obj:
        row += line.count('\n')
        letters = len(line) - 1
        print(f'{letters} letters in {line}')
    print(f'Number of rows = {row}')
