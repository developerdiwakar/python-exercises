from collections import ChainMap, defaultdict, namedtuple
from enum import Enum
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
# For example
d = {}
d['age'] = d.get('age', 0) + 1 # age not there, we get 0 + 1
print(d)
# Output = {'age': 1}
# We can write the above code like this also:
dd = defaultdict(int) # int is the default type (0 the value)
dd['age'] += 1 # short for dd['age'] = dd['age'] + 1
print(dd)
# Output = defaultdict(<class 'int'>, {'age': 1})

'''
ChainMap is an extremely nice data type which was introduced in Python 3.3. It behaves like a normal dictionary but according to the Python documentation: "is provided for quickly linking a number of mappings so they can be treated as a single unit"
'''
default_connection = { 'host': 'localhost', 'port': 4567}
connection = { 'port': 5678 }
conn = ChainMap(connection, default_connection) # Map creation
print(conn['port']) # port is found in the first dict
print(conn['host']) # host is found in the second dict

print(conn.maps) # We can see the mapping the objects
# Output = [{'port': 5678}, {'host': 'localhost', 'port': 4567}]
conn['host'] = 'test.local.io' # let's add host
print(conn.maps)
# Output = [{'port': 5678, 'host': 'test.local.io'}, {'host': 'localhost', 'port': 4567}]
del conn['port'] # let's remove the port information
print(conn.maps)
# Output = [{'host': 'test.local.io'}, {'host': 'localhost', 'port': 4567}]
print(dict(conn))
# Output = {'host': 'test.local.io', 'port': 4567}
'''
Enums - An enumeration is a set of symbolic names (members) bound to unique, constant values. Within an enumeration, the members can be compared by identity, and the enumeration itself can be iterated over.
'''
# GREEN = 1
# YELLOW = 2
# RED = 4
# TRAFFIC_LIGHTS = (GREEN, YELLOW, RED)
# OR WITH A DICT
# traffic_lights = { 'GREEN': 1, 'YELLOW': 2, 'RED': 4}
class TrafficLight(Enum):
    GREEN = 1
    YELLOW = 2
    RED = 4
print(TrafficLight.GREEN)
# Output = TrafficLight.GREEN
print(repr()) # their repr has more information
print(TrafficLight.GREEN.name, TrafficLight.GREEN.value)
# Output = GREEN, 1
print(TrafficLight(1))
# Output = TrafficLight.GREEN

