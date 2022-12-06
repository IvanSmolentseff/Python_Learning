'''Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для
формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].'''

initial_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def my_func(list_in):
    '''
    output the elements of the original list,
    whose values are greater than the previous element
    :param list_in: initial list of numbers
    :return: result
    '''
    result_list = [el for el in list_in if el > list_in[list_in.index(el) - 1]]
    print(f'Initial list: {list_in}')
    print(f'Result list: {result_list[1:]}')


my_func(initial_list)
