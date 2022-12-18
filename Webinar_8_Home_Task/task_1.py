'''Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора
класса (метод init()), который должен принимать данные (список списков) для
формирования матрицы.[[], [], []]
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в
привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения
двух объектов класса Matrix (двух матриц). Результатом сложения должна быть
новая матрица.'''


class Matrix:
    '''Base class'''

    def __init__(self, m_list, rows, columns):
        self.m_list = m_list
        self.rows = rows
        self.columns = columns

    def fill_matrix(self):
        '''
        method of filling matrix from keyboard
        :return: result
        '''
        self.m_list = [list(map(int, input(
            f'Enter {self.columns} numbers separated by split: ').split())) for
                       i in range(self.rows)]
        for item in self.m_list:
            if len(item) != self.columns:
                print('Mistake, matrix not under arguments')
                break
        else:
            print('All right, you can continue')

    def __str__(self):
        return str(
            '\n'.join(['\t'.join([str(j) for j in i]) for i in self.m_list]))

    def __add__(self, other):
        result = [[0] * self.columns for i in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.columns):
                if len(self.m_list) == len(other.m_list) and len(
                        self.m_list[i]) == len(other.m_list[i]):
                    result[i][j] = self.m_list[i][j] + other.m_list[i][j]
                else:
                    return 'For matrices with different sizes, addition is' \
                           ' not possible!'
        return Matrix(result, self.rows, self.columns)


m_1 = Matrix(list, 3, 3)
m_1.fill_matrix()
print(m_1)
m_2 = Matrix(list, 2, 3)
m_2.fill_matrix()
print(m_2)
print(f'\nMatrix sum = \n{m_1 + m_2}')
