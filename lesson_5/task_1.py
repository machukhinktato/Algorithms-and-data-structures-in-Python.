# program to detect average income of companies which will be requested by user

from collections import namedtuple

enterprise = namedtuple('enterprise', ['k1', 'k2', 'k3', 'k4'])
companies = {}

n = int(input("Количество предприятий: "))

for i in range(n):
    cname = input(f'Название {i + 1}-ой(-ей) компании: ')
    kvt_1 = int(input("Прибыль за первый квартал: "))
    kvt_2 = int(input("Прибыль за второй квартал: "))
    kvt_3 = int(input("Прибыль за третий квартал: "))
    kvt_4 = int(input("Прибыль за четвертый квартал: "))
    companies[cname] = enterprise(
        k1=kvt_1,
        k2=kvt_2,
        k3=kvt_3,
        k4=kvt_4,
    )

total_income = ()

for cname, income in companies.items():
    print(f'Предприятие: {cname} прибыль за год - {sum(income)}')
    total_income += income

avg_total_income = sum(total_income) / len(companies)
print(f'Средняя прибыль за год для всех предприятий {avg_total_income}')

print('Предприятия, у которых прибыль выше среднего:')

for cname, income in companies.items():
    if sum(income) > avg_total_income:
        print(f'{cname} - {sum(income)}')
print('Предприятия, у которых прибыль ниже среднего:')

for cname, income in companies.items():
    if sum(income) < avg_total_income:
        print(f'{cname} - {sum(income)}')