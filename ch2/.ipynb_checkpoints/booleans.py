print(int(True))   # True behaves like 1
# output = 1
print(int(False))   # False behaves like 0
# output = 0
print(bool(1))   # 1 evaluates to True in a boolean context
# output = True
print(bool(-42))   # and so does every non-zero number
# output = True
print(bool(0))   # 0 evaluates to False
# output = False
# quick peak at the operators (and, or, not)
print(not True) 
# output = False
print(not False) 
# output = True
print(True and True) 
# output = True
print(False or True) 
# output = True
print(True + 22)
# output = 23
print(7 + False)
# output = 7
