'''Каждое из слов «class», «function», «method» записать в байтовом типе без
преобразования в последовательность кодов (не используя методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.'''

variable = [b'class', b'function', b'method']


def my_func(my_list):
    '''
    Checking the type, content and length of variables
    :param my_list: List of bytes
    :return: type, content and length of variables
    '''
    for item in my_list:
        print(f'\nVariable type: {type(item)}')
        print(f'Variable content: {item}')
        print(f'Variable length: {len(item)}')


my_func(variable)
