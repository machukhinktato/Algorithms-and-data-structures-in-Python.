import sys, random


def show(mem):
    summary = 0
    for i in mem:
        summary += sys.getsizeof(i)
    return print(f'Объекты занимают {summary} байт в памяти')


# First version.
# Task: Write a program that proves or verifies that for the set of natural numbers
# the equality holds: 1 + 2 + ... + n = n (n + 1) / 2, where n is any natural number.

def func(n):
    if n == 1:
        return n
    lt = n + func(n - 1)
    return lt


def func_v1(n):
    lt = func(n)
    rt = n * (n + 1) // 2

    print(f'В результат: 1+2+..+n={lt}, а n(n+1)/2={rt}, что означает: ')
    if lt == rt:
        print('утверждение верно')
    else:
        print('утверждение не верно')
    mem = (rt, lt, n)
    print(mem)
    show(mem)


# Second version

def func_dict(n):
    func_d = {0: 0, 1: 1}

    def _func_dict(n):
        if n in func_d:
            return func_d[n]
        func_d[n] = n + _func_dict(n - 1)
        rt = n * (n + 1) // 2
        assert func_d[n] == rt
        mem = (rt, func_d, n)
        print(mem)
        show(mem)

        return func_d[n]

    return _func_dict(n)


# Third version

def func_loop(n):
    lt = 0
    for i in range(1, n + 1):
        lt += i
        # mem += i
    rt = n * (n + 1) // 2
    print(f'В результат: 1+2+..+n={lt}, а n(n+1)/2={rt}, что означает: ')
    if lt == rt:
        print('утверждение верно')
    else:
        print('утверждение не верно')
    mem = (lt, rt, n, i)
    print(mem)
    show(mem)

# func_v1(6)  # Объекты занимают 42 байт в памяти
# func_dict(6) # Объекты занимают 224 байт в памяти
# func_loop(6) # Объекты занимают 56 байт в памяти


# По памяти занимаемой, первый вариант, с рекурсией оказался легче, чем с мемоизацией,
# который, за счет её, как мне кажется, стал самым объемным из двух
# Вариант с циклом оказался промежуточным в частности как мне кажется из-за
# большего количества переменных, чем в других случаях
# python 3.8.1 x32
# ('32bit', 'WindowsPE')
