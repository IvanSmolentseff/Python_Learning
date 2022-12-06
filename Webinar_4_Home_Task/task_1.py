'''Реализовать скрипт, в котором должна быть предусмотрена функция расчета
заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия. Для выполнения расчета для
конкретных значений необходимо запускать скрипт с параметрами.'''

from sys import argv

script_name, hours_worked, hour_rate, bonus = argv

try:
    salary = int(hours_worked) * int(hour_rate) + int(bonus)
    print(f'Worker salary is {salary}')
except ValueError:
    print('You did not enter a number, please try again!')
