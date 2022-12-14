'''Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход). Последний атрибут должен
быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
на базе класса Worker. В классе Position реализовать методы получения полного
имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса
Position, передать данные, проверить значения атрибутов, вызвать методы
экземпляров).'''


class Worker:
    '''
    Base class
    '''

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    '''
    Derived class
    '''

    def get_full_name(self):
        '''
        found full name of worker
        :return: result
        '''
        print(f'Worker name is {self.name} {self.surname}')

    def get_total_income(self):
        '''
        found full salary of worker
        :return: result
        '''
        print(f'Worker salary is {sum(self._income.values())}')


employee = Position('Davide', 'Papito', 'manager', 5000, 1700)
employee.get_full_name()
print(employee.position)
employee.get_total_income()
