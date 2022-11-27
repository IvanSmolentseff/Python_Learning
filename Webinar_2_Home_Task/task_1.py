'''Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию
type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
а указать явно, в программе.'''

my_int = 9
my_float = 198.89
my_str = 'abrakadabra'
my_bool = False
my_none = None
my_list = [' ', 5]
my_tuple = ('text', 5)
my_set = {1, 1, 1, 2, 4, 9, 4}  # дубли сделал специально, но pylint ругается
my_dict = {"name": 'Ivan', 'age': 33}

result_list = [my_int, my_float, my_str, my_bool,
               my_none, my_list, my_tuple, my_set, my_dict]
for i in result_list:
    print(f'{i} is {type(i)}')
