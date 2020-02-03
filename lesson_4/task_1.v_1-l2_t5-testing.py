import cProfile, timeit, random, sys

sys.setrecursionlimit(7500)


# First version.
# Task: Write a program that proves or verifies that for the set of natural numbers
# the equality holds: 1 + 2 + ... + n = n (n + 1) / 2, where n is any natural number.

def func(n):
    if n == 1:
        return n
    res = n + func(n - 1)
    lt = res
    rt = n * (n + 1) // 2
    assert lt == rt
    return res


print(timeit.timeit('func(100)', number=100, globals=globals()))
# 0.0030736000000000027
print(timeit.timeit('func(200)', number=100, globals=globals()))
# 0.0070351000000000025
print(timeit.timeit('func(400)', number=100, globals=globals()))
# 0.014273399999999992
print(timeit.timeit('func(800)', number=100, globals=globals()))
# 0.0317301
print(timeit.timeit('func(1600)', number=100, globals=globals()))
# 0.0751959
print(timeit.timeit('func(3200)', number=100, globals=globals()))
# 0.1990594
print(timeit.timeit('func(6400)', number=100, globals=globals()))
# 0.43152919999999995

cProfile.run('func(100)')
# 100/1    0.000    0.000    0.000    0.000 task_1.v_1-l2_t5-testing.py:8(func)
cProfile.run('func(250)')
# 250/1    0.000    0.000    0.000    0.000 task_1.v_1-l2_t5-testing.py:6(func)
cProfile.run('func(500)')
# 500/1    0.001    0.000    0.001    0.001 task_1.v_1-l2_t5-testing.py:8(func)
cProfile.run('func(1000)')
# 1000/1    0.001    0.000    0.001    0.001 task_1.v_1-l2_t5-testing.py:8(func)
cProfile.run('func(2000)')
# 2000/1    0.003    0.000    0.003    0.003 task_1.v_1-l2_t5-testing.py:8(func)
cProfile.run('func(4000)')
# 4000/1    0.003    0.000    0.003    0.003 task_1.v_1-l2_t5-testing.py:8(func)
cProfile.run('func(6000)')
# 6000/1    0.005    0.000    0.005    0.005 task_1.v_1-l2_t5-testing.py:8(func)

# Во всех трех способах решения мы наблюдаем линейную зависимость.
# Произведенные измерительные работы в данном случае показали, что чем
# проще,алгоритм для простых задач, тем он быстрее выполняется.
# Задание выполненное с помощью циклов(task_1.v_3 было самым экономным
# в временом и ресусном плане, функция вызывалась один раз и предоставило,
# тот же ответ, что альтернативные функции, тратившие дополнительные вызовы.
# А рекурсия с мемоизацией оказалось куда более шустрой, чем функция
# просто с рекурсией, однако при больших значениях падала с ошибкой
