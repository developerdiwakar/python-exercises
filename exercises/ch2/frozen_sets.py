# Note Frozenset are immutable so, we can't add or remove element but we can able to do Union, Intersection and etc. 

small_primes = frozenset([2, 3, 5, 7])
bigger_primes = frozenset([5, 7, 11, 13])

# small_primes.add(1) gives error
# small_primes.remove(2) gives error

print(small_primes & bigger_primes) # Intersect
# Output = frozenset({5, 7})