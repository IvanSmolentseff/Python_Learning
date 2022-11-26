'''Пользователь вводит целое положительное число. Найдите самую большую цифру
в числе. Для решения используйте цикл while и арифметические операции.'''

number = int(input("Enter a positive integer: "))
max_digit = 0
while number > 10:
    residue = number % 10
    number //= 10
    if residue > max_digit:
        max_digit = residue
print(f"Maximum digit in number is {max_digit}")