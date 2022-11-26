'''Спортсмен занимается ежедневными пробежками. В первый день его результат
составил a километров. Каждый день спортсмен увеличивал результат на 10 %
относительно предыдущего. Требуется определить номер дня, на который результат
спортсмена составит не менее b километров. Программа должна принимать значения
параметров a и b и выводить одно натуральное число — номер дня.'''

a = float(input("Enter first day distance, km: "))
b = float(input("Enter target distance, km: "))
WORKOUT_RATIO = 1.1
day = 1
if a >= b:
    print("Goal has already been reached")
else:
    while a < b:
        a = a * WORKOUT_RATIO
        day += 1
    print(f"On the {day} day, the athlete reached the result at least {b} km")