'''Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.'''

number_1, number_2, number_3 = input('Enter three numbers separated by '
                                     'space: ').split()


def two_max_sum(arg_1, arg_2, arg_3):
    '''
    Sum of two maximum arguments
    :param arg_1: first number
    :param arg_2: second number
    :param arg_3: third number
    :return: result
    '''
    my_list = sorted([float(arg_1), float(arg_2), float(arg_3)], reverse=True)
    print(f'Sum of two maximum arguments = {my_list[0] + my_list[1]}')


two_max_sum(number_1, number_2, number_3)
