# in array of random numbers change position
# of max and min elements
import random
SIZE = 10
a, b = 0, 0
MAX_ITEM = 100
MIN_ITEM = 0
mx = 0
mn = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'спиок по результату формирования{array}')

for idx, num in enumerate(array):
    if num > mx:
        mx = num
        if num < mn:
            mn = num
    if num == mx:
        a = idx
        if num == mn:
            b = idx

array[b], array[a] = array[a], array[b]

print(f'Максимальное число= {mx}, Индекс= {a}')
print(f'Минимальное число= {mn}, Индекс= {b}')
print(f'список по результату формирования{array}')