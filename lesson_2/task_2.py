# https://drive.google.com/file/d/1acHoS8JLKw4G5YrTiqVQMlqpwuP0Z5yV/view?usp=sharing


positive_number, negative_nubmer = 0, 0
n = int(input('Добро пожаловать в наши программу '
              'Она позволит выявить Вам четные и нечетные числа, '
              'в любом указанном Вами числе. '
              'Пожалуйста введите число: '))
while n > 0:
    if n % 2 == 0:
        positive_number += 1
    else:
        negative_nubmer += 1
    n = n // 10
print(f'четных = {positive_number}, нечетных = {negative_nubmer}')