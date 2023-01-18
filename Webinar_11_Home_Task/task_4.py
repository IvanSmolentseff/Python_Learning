'''Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить обратное
преобразование (используя методы encode и decode).'''

variable = ['разработка', 'администрирование', 'protocol', 'standard']


def str_byte_str(my_list):
    new_list = []
    for item in my_list:
        x = item.encode('utf-8')
        print(x, type(x))
        new_list.append(x)
    for i in new_list:
        y = i.decode('utf-8')
        print(y, type(y))


str_byte_str(variable)
