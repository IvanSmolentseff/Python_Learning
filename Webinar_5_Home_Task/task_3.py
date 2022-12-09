'''Создать текстовый файл (не программно), построчно записать фамилии
сотрудников и величину их окладов (не менее 10 строк). Определить, кто из
сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32'''

with open('Task_3.txt', 'r', encoding='utf-8') as f_obj:
    low_salary_list = [line.split()[0] for line in f_obj if
                       float(line.split()[1]) < 20000]
    print(f'Number of employees with low salary = {len(low_salary_list)}. '
          f'\nNames of these employees: {", ".join(low_salary_list)}.')

with open('Task_3.txt', 'r', encoding='utf-8') as f_obj:
    salary_list = [float(line.split()[1]) for line in f_obj]
    print(f'Average salary = {sum(salary_list) / len(salary_list)}')
