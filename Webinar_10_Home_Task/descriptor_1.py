class AttributeValidation:
    ''' Checking the attributes '''

    def __set__(self, instance, value):
        if type(value) != int and type(value) != float:
            raise TypeError(f'The value of "{self.my_attr}" is not a number')
        elif value <= 0:
            raise ValueError(f'Value of "{self.my_attr}" must be greater '
                             f'than zero')
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Road:
    ''' road class '''
    _length = AttributeValidation()
    _width = AttributeValidation()

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


road_1 = Road('5 thousand', 20)
road_2 = Road(5000, -20)
road_1.asphalt_mass(2.5, 0.05)
road_2.asphalt_mass(2.5, 0.05)
