'''
While loop syntax:
while expr:
    expr
'''

# multiple sequences using while loop
people = ['Amit', 'Anish', 'Prabhakar', 'Chhotu']
ages = [23, 32, 23, 34]

position = 0

while position < len(people):
    person = people[position]
    age = ages[position]
    print(person, age)
    position +=1