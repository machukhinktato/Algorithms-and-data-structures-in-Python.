# Task 1 from 9: in the range of natural numbers from 2 to 99 find
# how much of them have multiplicity with each number from 2 to 9
a = [0] * 8
for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            a[j - 2] += 1
i = 0
while i < len(a):
    print(i + 2, ' - ', a[i])
    i += 1