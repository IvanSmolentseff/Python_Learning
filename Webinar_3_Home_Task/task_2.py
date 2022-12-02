'''Реализовать функцию, принимающую несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать
вывод данных о пользователе одной строкой.'''

name = input('Enter your name: ')
surname = input('Enter your surname: ')
birth_year = input('Enter your year of birth: ')
city = input('Enter your city of residence: ')
email = input('Enter your e-mail: ')
phone = input('Enter your phone: ')


def user_data(arg_1, arg_2, arg_3, arg_4, arg_5, arg_6):
    '''
    User data output function
    :param arg_1: name
    :param arg_2: surname
    :param arg_3: year of birth
    :param arg_4: city of residence
    :param arg_5: e-mail
    :param arg_6: phone
    :return: displaying user data in one line
    '''
    print(f'Name - {arg_1}, Surname - {arg_2}, Year of birth - {arg_3}, '
          f'City of residence - {arg_4}, E-mail - {arg_5}, Phone - {arg_6}')


user_data(arg_1=name, arg_2=surname, arg_3=birth_year, arg_4=city,
          arg_5=email, arg_6=phone)
