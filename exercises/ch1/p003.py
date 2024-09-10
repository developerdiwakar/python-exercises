'''
Write a program to print greatest number in three given numbers
'''

a = eval(input("Enter the first number:"))
b = eval(input("Enter the second number:"))
c = eval(input("Enter the third number:"))

if (a > b) and (a>c):
    print(a, 'is greater' )
elif (b>c) and (b>a):
    print(b, 'is greater')
else:
    print(c, 'is greater')