from audioop import avg, avgpp


print([]) # an empty list
print(list()) # same as []
# Output = []
print([1, 2, 3]) # as with tuples, items are comma separated
# Output = [1, 2, 3]
print([x+5 for x in [2, 3, 4]]) # Python is magic
# Output = [7, 8, 9]
print(list((1, 3, 5, 7))) # list from a tuple
# Output = [1, 3, 5, 7]
print(list('hello')) # list from a string
# Output = ['h', 'e', 'l', 'l', 'o']
'''
Few list methods
'''
a = [1, 2, 1, 3]
a.append(13) # we can append anything at the end
print(a)
# Output = [1, 2, 1, 3, 13]
print(a.count(1)) # how many '1' are there in the list?
# Output = 2
a.extend([5, 7]) # extend the list by another (or sequence)
print(a)
# Output = [1, 2, 1, 3, 13, 5, 7]
print(a.index(13)) # Position of '13' in the list (0-based indexing)
# Output = 4
a.insert(0, 17) # insert '17' at position 0 
print(a)
# Output = [17, 1, 2, 1, 3, 13, 5, 7]
print(a.pop())
# Output = 7
print(a.pop(3))
# Output = 1
a.remove(17) # remove '17' from the list
print(a)
# Output = [1, 2, 3, 13, 5]
a.reverse() # reverse the order of the elements in the list
print(a)
# Output = [5, 13, 3, 2, 1]
a.sort() # sort the list
print(a) 
# Output = [1, 2, 3, 5, 13]
a.clear() # remove all elements from the list
print(a)
# Output = []
a = [1, 3, 5, 7]
print(min(a))
# Output = 1
print(max(a))
# Output = 7
print(sum(a))
# Output = 16
print(len(a))
# Output = 4
b = [6, 7, 8]
print(a+b) # + with list means concatenatio
# Output = [1, 3, 5, 7, 6, 7, 8]
print(a*2) # * has also a special meaning (repeat the list)
# Output = [1, 3, 5, 7, 1, 3, 5, 7]
