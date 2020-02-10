# task_2
# sorting with merge


import random


array = [round(random.uniform(0, 50), 1) for _ in range(10)]

print(array)


def task_2_mergesort(array):
    if len(array) <= 1:
        return

    middle = len(array) // 2

    left = array[:middle]
    right = array[middle:]

    task_2_mergesort(left)
    task_2_mergesort(right)

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
            k += 1
        else:
            array[k] = right[j]
            j += 1
            k += 1
    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1

    return


task_2_mergesort(array)
print(array)
