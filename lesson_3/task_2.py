# In the second array, keep the indices of even elements
# of the first array.
import random


SIZE = 10
MAX_ITEM = 100
MIN_ITEM = -100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
even_array = []
print(array)
[even_array.append(idx) for idx, num in enumerate(array) if num > 0]
print(even_array)