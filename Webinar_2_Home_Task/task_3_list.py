'''Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому
времени года относится месяц (зима, весна, лето, осень). Напишите решения
через list и через dict.'''

seasons_list = ['winter', 'spring', 'summer', 'autumn']
month_number = int(input('Enter month number: '))

if month_number == 1 or month_number == 2 or month_number == 12:
    print(f'Season is {seasons_list[0]}')
elif month_number == 3 or month_number == 4 or month_number == 5:
    print(f'Season is {seasons_list[1]}')
elif month_number == 6 or month_number == 7 or month_number == 8:
    print(f'Season is {seasons_list[2]}')
elif month_number == 9 or month_number == 10 or month_number == 11:
    print(f'Season is {seasons_list[3]}')
else:
    print(f'Mistake - wrong month number')
