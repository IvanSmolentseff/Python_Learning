'''Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать. Если
слово длинное, выводить только первые 10 букв в слове.'''

my_list = input('Enter few words separated by a space: ').split()

for index, word in enumerate(my_list, 1):
    if len(word)<=10:
        print(f'{index}) {word}')
    else:
        print(f'{index}) {word[0:10]}')
