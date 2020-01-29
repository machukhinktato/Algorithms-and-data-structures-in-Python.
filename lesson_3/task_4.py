# determine which number in the array is most common.
import random

SIZE = 100
MAX_ITEM = 25
MIN_ITEM = 0
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'В списке: {array}, из {SIZE} элементов, от {MIN_ITEM} до {MAX_ITEM}')

num = array[0]
oftn_ud = 1
for i in range(SIZE - 1):
    ud = 1
    for j in range(i + 1, SIZE):
        if array[i] == array[j]:
            ud += 1
            if ud > oftn_ud:
                oftn_ud = ud
                num = array[i]

if oftn_ud > 1:
    print(oftn_ud, 'раз(а) используется число', num)
else:
    print('Каждый элемент, как и человек - уникален по своему')