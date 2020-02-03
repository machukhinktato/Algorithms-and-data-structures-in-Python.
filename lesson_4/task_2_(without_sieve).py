import timeit, cProfile


def anti_sieve(n):
    step = 1
    num = 2

    while step < n:
        num += 1
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            step += 1

    return num


print(timeit.timeit('anti_sieve(100)', number=100, globals=globals()))
# 0.2688532
print(timeit.timeit('anti_sieve(211)', number=100, globals=globals()))
# 0.9396632
print(timeit.timeit('anti_sieve(307)', number=100, globals=globals()))
# 2.1056073
print(timeit.timeit('anti_sieve(400)', number=100, globals=globals()))
# 4.0174994
print(timeit.timeit('anti_sieve(500)', number=100, globals=globals()))
# 6.923534

cProfile.run('anti_sieve(100)')
# 1    0.002    0.002    0.002    0.002 task_2_(without_sieve).py:4(anti_sieve)
cProfile.run('anti_sieve(200)')
# 1    0.008    0.008    0.008    0.008 task_2_(without_sieve).py:4(anti_sieve)
cProfile.run('anti_sieve(300)')
# 1    0.025    0.025    0.025    0.025 task_2_(without_sieve).py:4(anti_sieve)
cProfile.run('anti_sieve(400)')
# 1    0.038    0.038    0.038    0.038 task_2_(without_sieve).py:4(anti_sieve)
cProfile.run('anti_sieve(500)')
# 1    0.066    0.066    0.066    0.066 task_2_(without_sieve).py:4(anti_sieve)

# Во второй задаче, каких-либо сербезных тенденций с загруженностью функционала
# выявлено не было, cProfile показывает стандартные значения. Выделить пожалуй можно лишь одно,
# что отчетливо наблюдается при вызове утилиты timeit.
# С решетом значения почти не изменяются и идут в одном диапозоне, в то время как,
# без решета, заметно линейный рост занчений.
# Проведя небольшие замеры, не вошедшие в подведение итогов, было выявлено,
# что в случае использования решета, основная часть времененного ресурса уходила на формирование массива
# Нахождение же числа по индексу, ресурсов почти не использовало.
