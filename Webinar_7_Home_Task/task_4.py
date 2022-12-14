'''Реализуйте базовый класс Car. У данного класса должны быть следующие
атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar,
WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен
показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
атрибутам, выведите результат. Выполните вызов методов и также покажите
результат.'''


class Car:
    '''Base class'''

    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        '''
        the method reports that the car has moved
        :return:
        '''
        return f'{self.name} started to move'

    def stop(self):
        '''
        the method reports that the car has stopped
        :return: result
        '''
        return f'{self.name} stopped'

    def turn(self, direction):
        '''
        the method reports that the car has turned
        :param direction: cardinal or left/right
        :return: result
        '''
        return f'{self.name} turned {direction}'

    def show_speed(self):
        '''
        the method reports the car speed
        :return: result
        '''
        return f'{self.name} is moving at a speed {self.speed} km/h'


class TownCar(Car):
    '''Derived class'''

    def __init__(self, name, color, speed, is_police, is_town_car):
        super().__init__(name, color, speed, is_police)
        self.is_town_car = is_town_car

    def show_speed(self):
        if self.speed > 60:
            return f'{self.name} has exceeded the speed limit, please ' \
                   f'slow down to 60 km/h or less'
        return f'{self.name} is moving at a speed {self.speed} km/h'


class SportCar(Car):
    '''Derived class'''

    def __init__(self, name, color, speed, is_police, is_sport_car):
        super().__init__(name, color, speed, is_police)
        self.is_town_car = is_sport_car


class WorkCar(Car):
    '''Derived class'''

    def __init__(self, name, color, speed, is_police, is_work_car):
        super().__init__(name, color, speed, is_police)
        self.is_town_car = is_work_car

    def show_speed(self):
        '''Derived class'''
        if self.speed > 40:
            return f'{self.name} has exceeded the speed limit, please ' \
                   f'slow down to 40 km/h or less'
        return f'{self.name} is moving at a speed {self.speed} km/h'


class PoliceCar(Car):
    '''Derived class'''

    def patrol(self, offence):
        '''
        the method reports the status of police patrol
        :param offence: bool
        :return: result
        '''
        if offence:
            return 'Noticed a speeding violation, I start the pursuit'
        return 'I am on patrol, there are no offenses'


kia = TownCar('Rio', 'black', 60, False, True)
lamborghini = SportCar('Urus', 'Yellow', 180, False, True)
gaz = WorkCar('GAZelle', 'White', 45, False, True)
ford = PoliceCar('Mondeo', 'White with blue strip', 65, True)
print(f'Kia {kia.name}, is police - {kia.is_police}')
print(f'Ford {ford.name}, is police - {ford.is_police}')
print(f'Lamborghini {lamborghini.go()}  \n{gaz.show_speed()} '
      f'\nPolice: {ford.patrol(True)} ')
print(f'Kia {kia.turn("west")} \n{gaz.stop()}')
