'''Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор
натуральных чисел. У пользователя необходимо запрашивать новый элемент
рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то
новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например,
my_list = [7, 5, 3, 3, 2].'''

rating_list = [7, 5, 3, 3, 2]
print(f'Current rating - {rating_list}')
rating = int(input('Enter rating: '))


def update_rating(r_list, number):
    for i in range(len(r_list)):
        if r_list[i] == number:
            r_list.insert(i + 1, number)
            break
        if r_list[0] < number:
            r_list.insert(0, number)
        elif r_list[-1] > number:
            r_list.append(number)
        elif r_list[i + 1] < number < r_list[i]:
            r_list.insert(i + 1, number)
            break
    return r_list


print(f'Updated rating - {update_rating(rating_list, rating)}')
