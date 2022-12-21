''' Tested scripts'''

from itertools import count


def two_max_sum(arg_1, arg_2, arg_3):
    '''
    Sum of two maximum arguments
    :param arg_1: first number
    :param arg_2: second number
    :param arg_3: third number
    :return: result
    '''
    my_list = sorted([float(arg_1), float(arg_2), float(arg_3)], reverse=True)
    return my_list[0] + my_list[1]


# -----------------------------------------------------------------------------

def int_func(arg):
    '''
    Function that accepts a word/text from small latin letters and returning
    it, but with the first letter capitalized.
    :param arg: word or text
    :return: result
    '''
    return arg.title()


# -----------------------------------------------------------------------------

def my_func(list_in):
    '''
    Determine the elements of a list that do not have duplicates
    :param list_in: initial list of numbers
    :return: result
    '''
    result_list = [el for el in list_in if list_in.count(el) == 1]
    return result_list


# -----------------------------------------------------------------------------

class DivisionByZero(Exception):
    '''Derived class'''

    def __init__(self, text):
        self.text = text


def dbz_test_1(a, b):
    '''
    test exception 1
    :param a: integer number
    :param b: integer number
    :return: result
    '''
    try:
        if b == 0:
            raise DivisionByZero('Cannot divide by zero')
    except DivisionByZero:
        return 'Cannot divide by zero'
    else:
        return a / b


def dbz_test_2(a, b):
    '''
        test exception 2
        :param a: integer number
        :param b: integer number
        :return: result
        '''
    if b == 0:
        raise DivisionByZero('Cannot divide by zero')
    return a / b


# -----------------------------------------------------------------------------

def my_func_count(initial_num, termination_num):
    '''
    an iterator that generates integers starting at the specified
    :param initial_num: starting number
    :param termination_num: termination number
    :return: numbers
    '''
    result_list = []
    for el in count(initial_num):
        if el > termination_num:
            break
        result_list.append(el)
    return result_list


# -----------------------------------------------------------------------------

class Cell:
    '''Base class'''

    def __init__(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return f'cell consists of {self.quantity} partitions'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if self.quantity - other.quantity > 0:
            return Cell(self.quantity - other.quantity)
        return 'Subtraction operation is not possible for these cells'

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        if self.quantity >= other.quantity:
            return Cell(self.quantity // other.quantity)
        return 'Division operation is not possible for these cells'

    def make_order(self, cells_row):
        '''
        This method allows you to organize cells in rows.
        :param cells_row: number cellulars in row
        :return:
        '''
        row = []
        for _ in range(self.quantity // cells_row):
            row.append('*' * cells_row)
        if self.quantity % cells_row != 0:
            row.append('*' * (self.quantity % cells_row))
        return '\\n'.join(row)
