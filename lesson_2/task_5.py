# https://drive.google.com/file/d/1acHoS8JLKw4G5YrTiqVQMlqpwuP0Z5yV/view?usp=sharing


def func(n):
    if n == 1:
        return n
    res = n + func(n - 1)
    return res


n = int(input('Данная программа проверит, что для множества натуральных '
              'чисел, выполняется равенство: 1+2+..+n=n(n+1)/2. '
              'Где n любое натуральное число. '
              'Введите число: '))

lt = func(n)
rt = n * (n + 1) // 2

print(f'В результат: 1+2+..+n={lt}, а n(n+1)/2={rt}, что означает: ')
if lt == rt:
    print('данное утверждение верно')
else:
    print('данное утверждение не верно')