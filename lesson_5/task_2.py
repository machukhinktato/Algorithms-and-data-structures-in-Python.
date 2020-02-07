from collections import deque

BASE = 16

num4list = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            'A', 'B', 'C', 'D', 'E', 'F')

num4dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
            '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
            'C': 12, 'D': 13, 'E': 14, 'F': 15}


def _sum(first, second):
    first = first.copy()
    second = second.copy()

    if len(second) > len(first):
        first, second = second, first

    second.extendleft('0' * (len(first) - len(second)))

    result = deque()
    unlimiter = 0
    while len(first) != 0:
        first_num = num4dict[first.pop()]
        second_num = num4dict[second.pop()]

        result_num = first_num + second_num + unlimiter

        if result_num >= BASE:
            unlimiter = 1
            result_num -= BASE
        else:
            unlimiter = 0

        result.appendleft(num4list[result_num])

    if unlimiter == 1:
        result.appendleft('1')

    return result


def mult_hex(first, second):
    first = first.copy()
    second = second.copy()

    if len(second) > len(first):
        first, second = second, first

    second.extendleft('0' * (len(first) - len(second)))
    result = deque('0')

    while len(second) != 0:
        second_num = num4dict[second.pop()]

        eggs = deque('0')
        for _ in range(second_num):
            eggs = _sum(eggs, first)

        eggs.extend('0' * (len(first) - len(second) - 1))
        result = _sum(result, eggs)

    return result


a = deque(input('Введите первое число в шестнадцеричном формате: ').upper())
b = deque(input('Введите второе число в шестнадцеричном формате: ').upper())

print(f'{list(a)} + {list(b)} = {list(_sum(a, b))}')
print(f'{a} * {b} = {mult_hex(a, b)}')