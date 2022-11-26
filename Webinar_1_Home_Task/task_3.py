'''Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например,
пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.'''

n = input("Enter number: ")
a = int(n + n)
b = int(n + n + n)
total = int(n) + a + b
print(total)
