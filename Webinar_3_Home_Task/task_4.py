'''
Программа принимает действительное положительное число x и отрицательное число
y. Необходимо выполнить возведение числа x в степень y. Задание необходимо
реализовать в виде функции my_func(x, y). При решении задания необходимо
обойтись без встроенной функции возведения числа в степень.
'''

number_1, number_2 = input('Enter first positive number and second integer'
                           ' negative number separated by space: ').split()


def my_func(x, y):
    '''
    First way
    :param x: real positive number
    :param y: integer negative number
    :return: pow
    '''
    try:
        if int(y) < 0 < float(x):
            print(f'({x})^({y}) = {float(x) ** float(y)}')
        else:
            print('Please enter numbers according to the task')
    except ValueError:
        print('Second number should be integer negative')


my_func(number_1, number_2)


def m_func(x, y):
    '''
    Second way
    :param x: real positive number
    :param y: integer negative number
    :return: pow
    '''
    try:
        if int(y) < 0 < float(x):
            result = 1
            i = 1
            while i <= abs(int(y)):
                result *= float(x)
                i += 1
            print(f'({x})^({y}) = {1 / result}')
        else:
            print('Please enter numbers according to the task')
    except ValueError:
        print('Second number should be integer negative')


m_func(number_1, number_2)
