'''Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
выводить ее на экран.'''

with open('Task_5.txt', 'w+', encoding='utf-8') as f_obj:
    f_obj.write(input('Enter numbers separated by space: '))

with open('Task_5.txt', 'r+', encoding='utf-8') as f_obj:
    print(f'Sum of numbers in file = {sum(map(int, f_obj.read().split()))}')
