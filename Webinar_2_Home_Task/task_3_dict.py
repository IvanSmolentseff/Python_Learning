'''Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому
времени года относится месяц (зима, весна, лето, осень). Напишите решения
через list и через dict.'''

month_dict = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May',
              6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October',
              11: 'November', 12: 'December'}
seasons_dict = {'winter': (month_dict.get(1), month_dict.get(2),
                           month_dict.get(12)),
                'spring': (month_dict.get(3), month_dict.get(4),
                           month_dict.get(5)),
                'summer': (month_dict.get(6), month_dict.get(7),
                           month_dict.get(8)),
                'autumn': (month_dict.get(9), month_dict.get(10),
                           month_dict.get(11))}

month_number = int(input('Enter month number: '))


def season_determination(dict_m, dict_s, month):
    if month > 12:
        print('Mistake - wrong month number')
    else:
        for i in dict_m.keys():
            if i == month_number:
                for j in dict_s.keys():
                    if dict_m.get(i) in dict_s[j]:
                        print(f'Month - {dict_m.get(i)}, Season - {j}')


season_determination(month_dict, seasons_dict, month_number)
