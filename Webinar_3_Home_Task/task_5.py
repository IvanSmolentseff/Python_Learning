'''
Программа запрашивает у пользователя строку чисел, разделенных пробелом. При
нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить
ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится
специальный символ, выполнение программы завершается. Если специальный символ
введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к
полученной ранее сумме и после этого завершить программу.
'''

import sys

def my_func():
    '''
    The program calculates the sum of the numbers entered by the user until
    the user enters a special character to exit
    :return: sum of the numbers
    '''
    numbers_init = input('Enter numbers separated by space: ').split()
    sum_numbers = sum(float(item) for item in numbers_init)
    print(f'Sum = {sum_numbers}')
    while True:
        numbers_add = input('Enter more numbers or Q/q for exit '
                            'separated by space: ').split()
        for value in numbers_add:
            try:
                sum_numbers += float(value)
            finally:
                if value in ('Q', 'q'):
                    print(f'\nFinal sum = {sum_numbers} \nProgram completed')
                    sys.exit()
        print(f'Sum = {sum_numbers}')


my_func()
