'''Создать программно файл в текстовом формате, записать в него построчно
данные, вводимые пользователем. Об окончании ввода данных свидетельствует
пустая строка.'''

with open('Task_1.txt', 'w+', encoding='utf-8') as f_obj:
    while True:
        line = input('Enter some text: ')
        if line == '':
            break
        f_obj.write(line + '\n')
    f_obj.close()
