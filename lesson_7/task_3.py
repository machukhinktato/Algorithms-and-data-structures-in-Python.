# task_2
# array with length 2m + 1 find median which separate him by 2 halfs where
# in one array elements lesser than median and other array
# with numbers bigger

import random

M = 5
items = 2 * M + 1
array = [random.randint(0, 100) for _ in range(0, items)]
print(array)


def task_3_sortwithmedian(array):
    for i in range(len(array)):
        lesser = equal = bigger = 0
        for j in range(len(array)):
            if i != j:
                if array[i] < array[j]:
                    lesser += 1
                elif array[i] > array[j]:
                    bigger += 1
                else:
                    equal += 1

        if equal != 0:
            if lesser > bigger:
                lesser, bigger = bigger, lesser

            eggs = bigger - lesser

            if eggs <= equal:
                equal -= eggs
                lesser += equal

        if lesser == bigger or lesser == bigger == equal:
            return array[i]

    return ' try once more ^_^ '


print(sorted(array))
print(f'median is: {task_3_sortwithmedian(array)}')

