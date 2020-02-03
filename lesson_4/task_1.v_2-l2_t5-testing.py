# Second version, recursion + memoization
import cProfile, timeit, random, sys

sys.setrecursionlimit(5000)


def func_dict(n):
    func_d = {0: 0, 1: 1}

    def _func_dict(n):
        if n in func_d:
            return func_d[n]
        func_d[n] = n + _func_dict(n - 1)
        rt = n * (n + 1) // 2
        assert func_d[n] == rt
        return func_d[n]

    return _func_dict(n)


print(timeit.timeit('func_dict(100)', number=100, globals=globals()))
# 0.005232600000000004
print(timeit.timeit('func_dict(200)', number=100, globals=globals()))
# 0.0094604
print(timeit.timeit('func_dict(400)', number=100, globals=globals()))
# 0.021321700000000006
print(timeit.timeit('func_dict(800)', number=100, globals=globals()))
# 0.042419799999999994
print(timeit.timeit('func_dict(1600)', number=100, globals=globals()))
# 0.0896839
print(timeit.timeit('func_dict(3200)', number=100, globals=globals()))
# 0.1861034
print(timeit.timeit('func_dict(6400)', number=100, globals=globals()))
# Process finished with exit code -1073741571 (0xC00000FD)

cProfile.run('func_dict(100)')
# 100/1    0.000    0.000    0.000    0.000 task_1.v_2-l2_t5-testing.py:41(_func_dict)
cProfile.run('func_dict(250)')
# 250/1    0.000    0.000    0.000    0.000 task_1.v_2-l2_t5-testing.py:41(_func_dict)
cProfile.run('func_dict(500)')
# 500/1    0.001    0.000    0.001    0.001 task_1.v_2-l2_t5-testing.py:41(_func_dict)
cProfile.run('func_dict(1000)')
# 1000/1    0.001    0.000    0.001    0.001 task_1.v_2-l2_t5-testing.py:41(_func_dict)
cProfile.run('func_dict(2000)')
# 2000/1    0.002    0.000    0.002    0.002 task_1.v_2-l2_t5-testing.py:41(_func_dict)
cProfile.run('func_dict(4000)')
# 4000/1    0.005    0.000    0.005    0.005 task_1.v_2-l2_t5-testing.py:12(_func_dict)
cProfile.run('func_dict(6000)')  # Process finished with exit code -1073741571 (0xC00000FD)

# Во всех трех способах решения мы наблюдаем линейную зависимость.
# Произведенные измерительные работы в данном случае показали, что чем
# проще,алгоритм для простых задач, тем он быстрее выполняется.
# Задание выполненное с помощью циклов(task_1.v_3 было самым экономным
# в временом и ресусном плане, функция вызывалась один раз и предоставило,
# тот же ответ, что альтернативные функции, тратившие дополнительные вызовы.
# А рекурсия с мемоизацией оказалось куда более шустрой, чем функция
# просто с рекурсией, однако при больших значениях падала с ошибкой
