'''Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки 'b'(без encode decode)
'''

variable = ['attribute', 'класс', 'функция', 'type']


def my_func(my_list):
    for item in my_list:
        if not item.isascii():
            print(f'Word "{item}" cannot be written to byte type '
                  f'with marking "b"')


my_func(variable)
