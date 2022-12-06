'''Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении
числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие, при
котором повторение элементов списка будет прекращено.'''

from itertools import count, cycle


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
    print(result_list)


my_func_count(3, 10)


def my_func_cycle(list_init, termination_cycle):
    '''
    iterator sequences, repeating elements of some list defined in advance
    :param list_init: initial list
    :param termination_cycle: reiteration number
    :return: result
    '''
    result_list = []
    reiteration_number = 0
    for el in cycle(list_init):
        if reiteration_number > termination_cycle:
            break
        result_list.append(el)
        reiteration_number += 1
    print(result_list)


my_func_cycle([1, 'hh', 3], 7)
