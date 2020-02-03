# Third version
import cProfile, timeit, random, sys

sys.setrecursionlimit(6000)


def func_loop(n):
    lt = 0
    for i in range(1, n + 1):
        lt += i
    rt = n * (n + 1) // 2
    assert lt == rt


print(timeit.timeit('func_loop(100)', number=100, globals=globals()))
# 0.0006767999999999982
print(timeit.timeit('func_loop(200)', number=100, globals=globals()))
# 0.001232999999999998
print(timeit.timeit('func_loop(400)', number=100, globals=globals()))
# 0.0029216000000000034
print(timeit.timeit('func_loop(800)', number=100, globals=globals()))
# 0.007373499999999998
print(timeit.timeit('func_loop(1600)', number=100, globals=globals()))
# 0.012676199999999999
print(timeit.timeit('func_loop(3200)', number=100, globals=globals()))
# 0.0241691
print(timeit.timeit('func_loop(6400)', number=100, globals=globals()))
# 0.05061450000000001

cProfile.run('func_loop(100)')
# 1    0.000    0.000    0.000    0.000 task_1.v_3-l2-t5-testing.py:7(func_loop)
cProfile.run('func_loop(250)')
# 1    0.000    0.000    0.000    0.000 task_1.v_3-l2-t5-testing.py:7(func_loop)
cProfile.run('func_loop(500)')
# 1    0.000    0.000    0.000    0.000 task_1.v_3-l2-t5-testing.py:7(func_loop)
cProfile.run('func_loop(1000)')
# 1    0.000    0.000    0.000    0.000 task_1.v_3-l2-t5-testing.py:7(func_loop)
cProfile.run('func_loop(2000)')
# 1    0.000    0.000    0.000    0.000 task_1.v_3-l2-t5-testing.py:7(func_loop)
cProfile.run('func_loop(4000)')
# 1    0.000    0.000    0.000    0.000 task_1.v_3-l2-t5-testing.py:7(func_loop)
cProfile.run('func_loop(6000)')
# 1    0.000    0.000    0.000    0.000 task_1.v_3-l2-t5-testing.py:7(func_loop)

# Во всех трех способах решения мы наблюдаем линейную зависимость.
# Произведенные измерительные работы в данном случае показали, что чем
# проще,алгоритм для простых задач, тем он быстрее выполняется.
# Задание выполненное с помощью циклов(task_1.v_3 было самым экономным
# в временом и ресусном плане, функция вызывалась один раз и предоставило,
# тот же ответ, что альтернативные функции, тратившие дополнительные вызовы.
# А рекурсия с мемоизацией оказалось куда более шустрой, чем функция
# просто с рекурсией, однако при больших значениях падала с ошибкой
