# https://drive.google.com/file/d/1e-yXHpzB9L9aQxGtCzd9cPvw9vSFxcrm/view?usp=sharing


n = input("Введите трехзначное число: ")
n = int(n)

a = n // 100
b = n % 100 // 10
c = n % 10
print(f'{a}{b}{c}')
print("Сумма цифр числа:", a + b + c)
print("Произведение цифр числа:", a * b * c)