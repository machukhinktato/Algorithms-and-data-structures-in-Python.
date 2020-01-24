# https://drive.google.com/file/d/1acHoS8JLKw4G5YrTiqVQMlqpwuP0Z5yV/view?usp=sharing


print('Добро пожаловать в программу клькулятор.')
n = ''
while n != '0':
    n = input('Просим выбрать интересующее Вас действие: '
              '*, /, +, -, для выхода из программы, наберите - 0: ')
    if n == '*' or n == '/' or n == '+' or n == '-':
        x = float(input('Введите первое число: '))
        y = float(input('Введите второе число: '))
        if n == '/':
            if x != 0 and y != 0:
                n = x / y
                print(n)
                n = ''
            else:
                print('Возможность деления на ноль отсутствует!')
        elif n == '*':
            n = x * y
            print(n)
            n = ''
        elif n == '+':
            n = x + y
            print(n)
            n = ''
        else:
            n = x -y
            print(n)
            n = ''
    elif n != '0':
        print('Введенные данные указаны некорректно')
    else:
        print('Желаем хорошего Вам дня')

