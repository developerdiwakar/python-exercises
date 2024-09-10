c = 3.14 + 2.73j
print(c.real)  # real part
# output = 3.14
print(c.imag)  # imaginary part
# output = 2.73
print(c.conjugate())  # conjugate of A + Bj is A - Bj
# output = (3.14-2.73j)
print(c * 2)   # multiplication is allowed
# output = (6.28+5.46j)
print(c ** 2)   # power operation as well
# output = (2.4067000000000007+17.1444j)
d = 1 + 1j   # addition and subtraction as well
print(c - d) 
# output = (2.14+1.73j)