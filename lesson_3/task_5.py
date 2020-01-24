# Find the maximum negative element in the array.
# Display its value and position in the array.
import random

SIZE = 20
MAX_ITEM = 100
MIN_ITEM = -100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Сформированный список: {array}')
idx, i = 0, 0
while i < SIZE:
    if 0 > array[i] and idx == 0:
        idx = i
    elif 0 > array[i] > array[idx]:
        idx = i
    i += 1

print(f'Где максимальный отрицательный элемент равен {array[idx]} '
      f'с индексом {idx}')