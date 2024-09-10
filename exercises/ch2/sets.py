small_primes = set() # an empty set
small_primes.add(2) # adding one element at a time
small_primes.add(3) # adding one element at a time
small_primes.add(5) # adding one element at a time
small_primes.add(1)
print(small_primes)
# Output = {1, 2, 3, 5}
small_primes.remove(1) # remove 1 because it's not prime
print(2 in small_primes) # membeship test
# Output = True
print(1 not in small_primes) # membeship test
# Output = True
small_primes.add(3) # trying to add 3 again
print(small_primes) 
# Output = {2, 3, 5} no change, duplication is not allowed
bigger_primes = set([5, 7, 11, 13]) # Faster creation
print(small_primes | bigger_primes) # Union "|" operator
print(small_primes & bigger_primes) # Intersection "&" operator
print(small_primes - bigger_primes) # Difference "-" operator

# Other way of creating set
other_primes = {2, 3, 5, 5, 3, 7} # creating set using "{}"
print(other_primes)
# Output = {2, 3, 5, 7} - duplicates are not allowed 
