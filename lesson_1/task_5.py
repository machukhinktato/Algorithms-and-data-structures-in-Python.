# https://drive.google.com/file/d/1e-yXHpzB9L9aQxGtCzd9cPvw9vSFxcrm/view?usp=sharing


print('Добрый день, наша программа поможет вам определить возможность'
      'существования треугольника и определить его тип. '
      'Для этого необходимо ввести расстояние трех отрезков')
a = int(input('Введите первый отрезок: '))
b = int(input('Введите второй отрезок: '))
c = int(input('Введите третий отрезок: '))

if a < b + c and b < a + c and c < a + b:
    print('Такой треугольник может существовать')
    if a != b and a != c and b != c:
        print('Будет разносторонний треугольник')
    elif a == b and a == c:
        print('Будет равносторонний треугольник')
    else:
        print('Будет равнобедренный треугольник')
else:
    print('Треугольников с заданными величинами не бывает')