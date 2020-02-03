import timeit, cProfile


def sieve(_range, n):
    sieve = [i for i in range(_range)]
    sieve[1] = 0
    for i in range(2, _range):
        if sieve[i] != 0:
            j = i + i
            while j < _range:
                sieve[j] = 0
                j += i

    res = [i for i in sieve if i != 0]

    return res[n - 1]


# sieve(1000, 88)
#
print(timeit.timeit('sieve(5000, 100)', number=100, globals=globals()))
# # 0.3165379
print(timeit.timeit('sieve(5000, 211)', number=100, globals=globals()))
# # 0.22613159999999993
print(timeit.timeit('sieve(5000, 307)', number=100, globals=globals()))
# # 0.21402279999999996
print(timeit.timeit('sieve(5000, 400)', number=100, globals=globals()))
# # 0.19904520000000003
print(timeit.timeit('sieve(5000, 500)', number=100, globals=globals()))
# # 0.21414160000000015
#
cProfile.run('sieve(5000, 100)')
# # 1    0.003    0.003    0.003    0.003 task_2_(with_sieve).py:4(sieve)
cProfile.run('sieve(5000, 211)')
# # 1    0.002    0.002    0.002    0.002 task_2_(with_sieve).py:4(sieve)
cProfile.run('sieve(5000, 307)')
# # 1    0.002    0.002    0.002    0.002 task_2_(with_sieve).py:4(sieve)
cProfile.run('sieve(5000, 400)')
# # 1    0.002    0.002    0.002    0.002 task_2_(with_sieve).py:4(sieve)
cProfile.run('sieve(5000, 500)')
# # 1    0.002    0.002    0.002    0.002 task_2_(with_sieve).py:4(sieve)
#
#
# Во второй задаче, каких-либо сербезных тенденций с загруженностью функционала
# выявлено не было, cProfile показывает стандартные значения. Выделить пожалуй можно лишь одно,
# что отчетливо наблюдается при вызове утилиты timeit.
# С решетом значения почти не изменяются и идут в одном диапозоне, в то время как,
# без решета, заметно линейный рост занчений.
# Проведя небольшие замеры, не вошедшие в подведение итогов, было выявлено,
# что в случае использования решета, основная часть времененного ресурса уходила на формирование массива
# Нахождение же числа по индексу, ресурсов почти не использовало.
