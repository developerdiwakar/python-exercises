t = ()
print(type(t))
one_ele_tuple = (42, ) # You need the comma!
three_ele_tuple = (1, 3, 5) # braces are optional here, means you can also write as 1, 2, 3
a, b, c = 1, 2, 3 # Tuples are multiple assignment
print(a, b, c)
# Output = 1, 2, 3
print(3 in three_ele_tuple)
# Output = True

# Swap two variables without using 3rd variable
x, y = 0, 1
x, y = y, x # Swapping
print(x, y)
# Output = 1, 0

