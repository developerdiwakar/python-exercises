from collections import namedtuple
'''
namedtuple() => Factory function for creating tuple subclasses with named fields
'''
# normal tuple
# vision = (9.3, 4.7)
# print(vision[0], vision[1]) # elements are accessible via indexes
Vision = namedtuple('Vision', ['left', 'right'])
vision = Vision(9.5, 8.8)
print(vision[0]) # 9.5
print(vision.left, vision.right) # 9.5, 8.8
Vision2 = namedtuple('Vision2', ['left', 'middle', 'right'])
vision2 = Vision2(3.4, 4.4, 6.4)
print(vision2.middle)
'''
The defaultdict data type allows you to avoid checking if a key is in a dictionary by simply inserting it for you on your first access attempt, with a default value whose type you pass on creation.
'''


