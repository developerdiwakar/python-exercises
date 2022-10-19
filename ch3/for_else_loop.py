'''
For...else loop syntax:
for expr:
    expr
else:
    expr
'''


# class DriverException(Exception):
#     pass

# people = [('Manish', 13),('anish', 20),('Ravish', 23), ('Prabhakar', 12)]

# for person, age in people:
#     if age > 30:
#         driver = (person, age)
#         break
# else:  
#     raise DriverException('Driver Not Found.')


# Check for Prime number upto n numbers without else keyword
""" primes = []
upto = 100
for n in range(2, upto + 1):
    is_prime = True
    for divisor in range(2, n):
        if n % divisor == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(n)
print(primes) """

# Check for Prime number upto n numbers with for...else
primes = []
upto = 100
for n in range(2, upto + 1):
    # is_prime = True
    for divisor in range(2, n):
        if n % divisor == 0:
            # is_prime = False
            break
    else:
        primes.append(n)
print(primes)
