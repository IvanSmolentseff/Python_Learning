'''Реализовать генератор с помощью функции с ключевым словом yield, создающим
очередное значение. При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n). Функция
отвечает за получение факториала числа, а в цикле необходимо выводить только
первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n.
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.'''

from itertools import count
from math import factorial


def fact(number):
    '''
    generator of numbers from 1 to the specified
    :param number: specified number
    :return: result
    '''
    for element in count(1):
        if element > number:
            break
        yield element


n = int(input('Enter integer number: '))
for el in fact(n):
    print(f'{el}! = {factorial(el)}')

'''         OR         '''

def fact_gen(number):
    '''
    factorial generator of numbers from 1 to the specified
    :param number: specified number
    :return: result
    '''
    for element in count(1):
        if element > number:
            break
        yield factorial(element)


n = int(input('Enter integer number: '))
for el in fact_gen(n):
    print(el)
