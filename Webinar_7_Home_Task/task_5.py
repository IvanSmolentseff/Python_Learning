'''Реализовать класс Stationery (канцелярская принадлежность). Определить в
нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение
“Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение. Создать
экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.'''


class Stationary:
    '''Base class'''

    def __init__(self, title):
        self.title = title

    def draw(self):
        '''
        method of draw
        :return: result
        '''
        return 'Start rendering'


class Pen(Stationary):
    '''Derived class'''

    def draw(self):
        return f'Rendering by pen "{self.title}" is not so bad'


class Pencil(Stationary):
    '''Derived class'''

    def draw(self):
        return f'Rendering by pencil "{self.title}" is impossible'


class Handle(Stationary):
    '''Derived class'''

    def draw(self):
        return f'Rendering by handle "{self.title}" is best'


pen = Pen('Parker 5th IM Premium Shiny Chrome F522')
pencil = Pencil('Erich Krause')
handle = Handle('Sketch&Art')
print(pen.draw())
print(pencil.draw())
print(handle.draw())
