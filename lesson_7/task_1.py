# task_3
# sort with bubble in range from -100 to 100


import random


array = [random.randrange(-100, 100) for _ in range(10)]


def task_1_sort(array):
    print(array)
    srtd = True
    while srtd:
        srtd = False
        for i in range(len(array) - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                srtd = True

    print(array)
    return


task_1_sort(array)
