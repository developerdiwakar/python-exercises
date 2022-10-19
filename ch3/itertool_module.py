'''
itertools module examples
'''

# Infinite iterator
from itertools import compress, count, permutations

# Count method example
# for n in count(5, 3):
#     if n > 20:
#         break
#     print(n, end=', ')

# Output = 5, 8, 11, 14, 17, 20, 

# Compress method example
data = range(10)
even_selector = [1, 0] * 10
odd_selector = [0, 1] * 10

even_numbers = list(compress(data, even_selector))
odd_numbers = list(compress(data, odd_selector))

print(list(data))
print(even_selector)
print(odd_selector)
print(even_numbers)
print(odd_numbers)

# Permutations method example
print(list(permutations('ABC')))

