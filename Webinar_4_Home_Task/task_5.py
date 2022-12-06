'''Реализовать формирование списка, используя функцию range() и возможности
генератора. В список должны войти четные числа от 100 до 1000 (границы).
Необходимо получить результат вычисления произведения всех элементов
списка. Подсказка: использовать функцию reduce().'''

from functools import reduce


def my_func(prev_el, cur_el):
    '''
    Calculate result of producing all elements of the list
    :param prev_el: previous element
    :param cur_el: current element
    :return: result
    '''
    return prev_el * cur_el


my_list = [el for el in range(100, 1001) if el % 2 == 0]

print(f'List of even numbers in range from 100 to 1000: [{my_list[0]},'
      f' {my_list[1]}, .... , {my_list[-2]}, {my_list[-1]}]')
print(f'Result of producing all elements of the list ='
      f' {reduce(my_func, my_list)}')
