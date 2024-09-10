'''
Function syntax:
def function_name:
    stmt
'''
# # scoping levels
# def outer():
#     test = 1 # outer scope 
#     def inner():
#         test = 2 # inner scope
#         print('inner:', test)
#     inner()
#     print('outer:', test)
# test = 0 # global scope
# outer()
# print('global:', test)
# Output: inner 2, outer 1, global 0
'''
nonlocal - The nonlocal statement causes the listed identifiers to
refer to previously bound variables in the nearest enclosing scope 
excluding globals.
'''
# Scoping levels with nonlocal statement

# def outer():
#     test = 1 # outer scope
#     def inner():
#         nonlocal test
#         test = 2 # nearest enclosing scope (which is 'outer') means overrite that value
#         print('inner:', test)
#     inner()
#     print('outer:', test)
# test = 0 # global scope
# outer()
# print('global:', test)
# Output: inner 2, outer 2, global 0

# Scoping levels with global statement
# def outer():
#     test = 1 # outer scope
#     def inner():
#         global test
#         test = 2 # global scope
#         print('inner:', test)
#     inner()
#     print('outer:', test)
# test = 0 # global scope
# outer()
# print('global:', test)
# Output: inner 2, outer 1, global 2

# Positional arguments and default values
def func(a,b=5,c=7):
    print(a,b,c)
func(1,2,3) 
# Output: 1 2 3
func(0)
# Output: 0 5 7

# Keyword arguments and default values
def func(a,b,c):
    print(a,b,c)
func(a=5, c=2, b=4)
# Output = 5 4 2

