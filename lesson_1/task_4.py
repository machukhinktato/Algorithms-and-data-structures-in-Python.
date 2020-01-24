# https://drive.google.com/file/d/1e-yXHpzB9L9aQxGtCzd9cPvw9vSFxcrm/view?usp=sharing


print('Добрый день, данная програма поможет Вам выявить среднее число из трёх разных, введенных чисел')
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

if a > b and a < c:
    n = a
elif a > c and a < b:
    n = a
elif b > c and b < a:
    n = b
elif b > a and b < c:
    n = b
else:
    n = c

print(f'срденее число: {n}')