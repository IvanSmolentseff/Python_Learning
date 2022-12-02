'''Реализовать функцию, принимающую два числа (позиционные аргументы) и
выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
обработку ситуации деления на ноль.'''

number_1 = float(input('Enter first number: '))
number_2 = float(input('Enter second number: '))


def numbers_division(num_1, num_2):
    '''
    Number division function
    :param num_1: divisible number
    :param num_2: divisor
    :return: result of division
    '''
    try:
        print(f'{num_1} / {num_2} = {num_1 / num_2}')
    except ZeroDivisionError:
        print('Сan not be divided by zero')


numbers_division(number_1, number_2)
