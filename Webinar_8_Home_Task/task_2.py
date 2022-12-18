'''Реализовать программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс Клетка (Cell).
В его конструкторе инициализировать параметр (quantity),
соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (add()),
вычитание (sub()),
умножение (mul()),
деление (truediv()).
Данные методы должны применяться только к клеткам и выполнять увеличение,
уменьшение, умножение и целочисленное (с округлением до целого) деление клеток,
соответственно.'''


class Cell:
    '''Base class'''

    def __init__(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return f'cell consists of {self.quantity} partitions'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if self.quantity - other.quantity > 0:
            return Cell(self.quantity - other.quantity)
        return 'Subtraction operation is not possible for these cells'

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        if self.quantity >= other.quantity:
            return Cell(self.quantity // other.quantity)
        return 'Division operation is not possible for these cells'

    def make_order(self, cells_row):
        '''
        This method allows you to organize cells in rows.
        :param cells_row: number cellulars in row
        :return:
        '''
        row = []
        for _ in range(self.quantity // cells_row):
            row.append('*' * cells_row)
        if self.quantity % cells_row != 0:
            row.append('*' * (self.quantity % cells_row))
        return '\\n'.join(row)


c_1 = Cell(30)
c_2 = Cell(25)
print(c_1.quantity)
print(c_2.quantity)
print(f'After add operation - {c_1 + c_2}')
print(f'After sub operation - {c_1 - c_2}')
print(f'After mul operation - {c_1 * c_2}')
print(f'After div operation - {c_1 / c_2}')
print(c_1.make_order(5))
print(c_2.make_order(10))
