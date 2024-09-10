'''
Ternary Syntax
stmt if expr else stmt

Write a program to input a number and then check whether it is even or odd
'''
num = eval(input("enter a number: "))
output = "Even" if num % 2 == 0 else "Odd"
print(f'{num} is an {output} number')