'''Для списка реализовать обмен значений соседних элементов, т.е. значениями
обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве
элементов последний сохранить на своем месте. Для заполнения списка элементов
необходимо использовать функцию input().'''

my_list = input('Enter the elements of the'
                ' list separated by a space: ').split()
print(f'Initial list - {my_list}')


def modified_list(list_init):
    i = 0
    if len(list_init) % 2 == 0:
        while i < len(list_init):
            element = list_init[i]
            list_init[i] = list_init[i + 1]
            list_init[i + 1] = element
            i += 2
    else:
        while i < len(list_init) - 1:
            element = list_init[i]
            list_init[i] = list_init[i + 1]
            list_init[i + 1] = element
            i += 2
    return list_init


print(f'Modified list - {modified_list(my_list)}')
