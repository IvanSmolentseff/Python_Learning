'''Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные. При этом английские числительные должны заменяться на
русские. Новый блок строк должен записываться в новый текстовый файл.'''

translation = {'One': 'Адын', 'Two': 'Дыва', 'Three': 'Тры', 'Four': 'Чятыре'}

with open('Task_4(1).txt', 'r', encoding='utf-8') as f_obj:
    translated_list = []
    for line in f_obj:
        line = line.split(' ', 1)
        translated_list.append(translation[line[0]] + ' ' + line[1])

with open('Task_4(2).txt', 'w+', encoding='utf-8') as new_obj:
    new_obj.writelines(translated_list)
