'''Запросите у пользователя значения выручки и издержек фирмы. Определите,с
каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если
фирма отработала с прибылью, вычислите рентабельность выручки (соотношение
прибыли к выручке). Далее запросите численность сотрудников фирмы и определите
прибыль фирмы в расчете на одного сотрудника.'''

proceeds = int(input("Enter your company's proceeds: "))
costs = int(input("Enter your company's costs: "))
if proceeds > costs:
    profit = proceeds - costs
    rentability = profit / proceeds * 100
    print(f"Company has a profit. Rentability is {round(rentability, 2)} % ")
    employee = int(input("Enter number of company employees: "))
    profit_per_employee = profit / employee
    print(f"Profit per employee is {round(profit_per_employee, 2)} ")
else:
    print("Company is operating at a loss")