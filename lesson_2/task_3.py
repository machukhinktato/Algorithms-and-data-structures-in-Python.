# https://drive.google.com/file/d/1acHoS8JLKw4G5YrTiqVQMlqpwuP0Z5yV/view?usp=sharing


x = 0
n = int(input('Данная программа позволит написать число '
              'выбранное Вами - наооборот. Пожалуйста, введите число: '))
while n > 0:
    x = x * 10 + n % 10
    n = n // 10
print(x)