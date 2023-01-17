'''Каждое из слов «разработка», «сокет», «декоратор» представить в строковом
формате и проверить тип и содержание соответствующих переменных. Затем с
помощью онлайн-конвертера преобразовать строковые представление в формат
Unicode и также проверить тип и содержимое переменных.'''

variable_1 = ['разработка', 'сокет', 'декоратор']
variable_2 = ['\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
              '\u0441\u043e\u043a\u0435\u0442',
              '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']


def my_func(my_list):
    '''
    Checking the type and content of variables
    :param my_list: List of strings
    :return: type and content of variables
    '''
    for item in my_list:
        print(f'\nVariable type: {type(item)}')
        print(f'Variable content: {item}')


my_func(variable_1)
print('-'*30)
my_func(variable_2)
