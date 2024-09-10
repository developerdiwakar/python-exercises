'''
For loop syntax: 
for expr in (range, list, tuple, dict, set and etc)
'''
colors = ['Red','Orange','Yellow', 'Blue', 'Green']
# Display a list of color names
# for color in colors:
#     print(color)

# Display a list of color names with position
# for index in range(len(colors)):
#     print(index, colors[index])

# For loop example using enumerate buil-in function
# for position, color in enumerate(colors):
#     print(position, color)

people = ['Kevin', 'Deepak', 'Henrich', 'Tom']
ages = [23,34,44,46]
# Iterating over multiple sequences
# for position in range(len(people)):
#     age = ages[position]
#     person = people[position]
#     print(person, age)

# Multiple sequences using enumerate function
# for position, person in enumerate(people):
#     age = ages[position]
#     print(person, age)

# Multiple sequences using zip function
# for person, age in zip(people, ages):
#     print(person, age)
countries = ['Poland', 'India', 'Germany', 'Mexico']
# for data in zip(people, ages, countries):
#     person, age, country = data
#     print(person, age, country)

# Using range(start, stop, step) function
# for i in range(-10, 10, 2):
#     print(i) 

