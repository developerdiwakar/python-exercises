'''
Syntax: if expr: stmt 
        elif expr: stmt
        else: stmt
Write a program to check greatest number between the three numbers.
'''
a = eval(input('enter the 1st number: '))
b = eval(input('enter the 2nd number: '))
c = eval(input('enter the 3rd number: '))

if a > b and a > c:
    print(f'{a} is greatest number')
elif b > c:
    print(f'{b} is greatest number')
else:
    print(f'{c} is greatest number')