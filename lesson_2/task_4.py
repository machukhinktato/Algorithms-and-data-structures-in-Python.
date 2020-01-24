# https://drive.google.com/file/d/1acHoS8JLKw4G5YrTiqVQMlqpwuP0Z5yV/view?usp=sharing


n = int(input('Данная программа поможет вам определить число, '
              'с большей суммой цифр. Введите натуральное число, '
              'чтобы сосчитать и 0 чтобы завершить программу: '))
summ = numeral = 0
while n != 0:
    x = n
    y = 0
    while n > 0:
        y += n % 10
        n = n // 10
    if y > summ:
        summ = y
        numeral = x
    n = int(input('Введите следующее натуральное число или 0,'
                  ' чтобы завершить ввод и начать вычесление: '))
print(f'Число {numeral}, имеет максимальную сумму равную: {summ}')