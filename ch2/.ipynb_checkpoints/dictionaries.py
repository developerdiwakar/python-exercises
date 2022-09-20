'''
A dictionary maps keys to values. Keys need to be hashable objects, while values can be of any arbitrary type. Dictionaries are mutable objects.
'''

# 5 ways of creating Dictionary
a = dict(A=1, Z=-1)
b = {'A': 1, 'Z': -1}
c = dict(zip(['A', 'Z'], [1, -1]))
d = dict([('A', 1), ('Z', -1)])
e = dict({'Z': -1, 'A': 1})
# print(a == b == c == d == e) # are they all the same?
# Output = True

listdata = list(zip(['h', 'e', 'l', 'l', 'o'], [1, 2, 3, 4, 5]))
# print(listdata)
# Output = [('h', 1), ('e', 2), ('l', 3), ('l', 4), ('o', 5)]
listdata = list(zip('hello', range(1, 6))) # equivalent, more Pythonic
# print(listdata)
# Output = [('h', 1), ('e', 2), ('l', 3), ('l', 4), ('o', 5)]

d = {} # empty dictionary
d['a'] = 1 # let's set a couple of (key, value) pairs
d['b'] = 2
# print(len(d)) # to check how many pairs are?
# Output = 2
# print(d)
# Output = {'a': 1, 'b': 2}
# print(d.keys()) # return all the keys
# Output = dict_keys(['a', 'b'])
# print(d.values()) # return all the values
# Output = dict_values([1, 2])
# print(d.items()) # return all the (key, value) pairs
# Output = dict_items([('a', 1), ('b', 2)])
del d['a'] # to delete element 'a' from the dictionay
# print(d)
# Output = {'b': 2}
d['c'] = 3
# print('c' in d) # membership is checked against the keys
# Output = True
# print(3 in d) # not the values
# Output = False
# print('e' in d)
# Output = False
d.clear() # let's clean everything from this dictionary
# print(d) 
# Output = {}

d = {'e': 1, 'h': 0, 'o': 4, 'l': 3}
d.popitem() # removes a random item
# print(d)
d.pop('o') # remove item with key 'l'
# Output = 3
d.update({'another': 'value'}) # we can update dict this way
d.update(a=13) # or this way (like a function call)
print(d)
# Output = {'e': 1, 'h': 0, 'another': 'value', 'a': 13}
print(d.get('a')) # same as d['a'] but if key is missing no keyError
# Output = 13
print(d.get('k', 177)) # default value used if key is missing
# Output = 177
print(d.get('b')) # key is not there, so None is returned
d.setdefault('k', 12) # 'k' is missing, we get default value. Also, the key/value pair (a, 1) has now been added
print(d)
# Output = {'e': 1, 'h': 0, 'another': 'value', 'a': 13, 'k': 12} 