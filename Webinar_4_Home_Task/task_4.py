'''Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию. Элементы
вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]'''

initial_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


def my_func(list_in):
    '''
    Determine the elements of a list that do not have duplicates
    :param list_in: initial list of numbers
    :return: result
    '''
    result_list = [el for el in list_in if list_in.count(el) == 1]
    print(f'Initial list: {list_in}')
    print(f'Result list: {result_list}')


my_func(initial_list)
