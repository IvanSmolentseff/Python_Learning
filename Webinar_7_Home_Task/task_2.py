'''Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина), width (ширина). Значения данных атрибутов должны передаваться
при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего
дорожного полотна. Использовать формулу: длинаширинамасса асфальта для
покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины
полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т'''


class Road:
    '''
    road class
    '''

    def __init__(self, length, width):
        '''
        class attributes
        :param length: in metres
        :param width:  in metres
        '''
        self._length = length
        self._width = width

    def asphalt_mass(self, density, thickness):
        '''
        asphalt mass calculation
        :param density: density in t/m3
        :param thickness: thickness of asphalt in metres
        :return: result
        '''
        mass = self._length * self._width * thickness * density
        print(f'The mass of asphalt required for the construction of road is'
              f' {mass} tonnes')


road = Road(5000, 20)
road.asphalt_mass(2.5, 0.05)
