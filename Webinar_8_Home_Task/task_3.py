'''Создайте собственный класс-исключение, обрабатывающий ситуацию деления на
нуль. Проверьте его работу на данных, вводимых пользователем. При вводе
пользователем нуля в качестве делителя программа должна корректно обработать
эту ситуацию и не завершиться с ошибкой.'''


# import traceback

class DivisionByZero(Exception):
    '''Derived class'''

    def __init__(self, text):
        self.text = text


def test(a, b):
    '''
    test exception
    :param a: integer number
    :param b: integer number
    :return: result
    '''
    try:
        if b == 0:
            raise DivisionByZero('Cannot divide by zero')
    except DivisionByZero as err:
        print(err)
    else:
        print(f'All right: {a} / {b} = {int(a) / int(b)}')


test(5, 2)
test(5, 0)
