greet_old = 'Hello %s!'
print(greet_old % 'Fabrizio')
# Output: 'Hello Fabrizio!'
# Note: The % operator, is deprecated and shouldn't be used anymore.
greet_positional = 'Hello {} {}!'
print( greet_positional.format('Fabrizio', 'Romano'))
# Output: 'Hello Fabrizio Romano!'

greet_positional_idx = 'This is {0}! {1} loves {0}!'
print( greet_positional_idx.format('Python', 'Fabrizio'))
# Output: 'This is Python! Fabrizio loves Python!'
print( greet_positional_idx.format('Coffee', 'Fab'))
# Output: 'This is Coffee! Fab loves Coffee!'

keyword = 'Hello, my name is {name} {last_name}'
print( keyword.format(name='Fabrizio', last_name='Romano'))
# Output: 'Hello, my name is Fabrizio Romano'

'''
Formatted String Literals
'''
name = 'Fab'
age = 42
print(f"Hello! My name is {name} and I'm {age}")
# Output = Hello! My name is Fab and I'm 42
from math import pi
print(f"No arguing with {pi}, it's irrational...")
# Output = No arguing with 3.141592653589793, it's irrational...

