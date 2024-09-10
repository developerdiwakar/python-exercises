s = "The trouble is you think you have time."
print(s[0])   # indexing at position 0, which is the first char
# Outpuy = 'T'
print(s[5])   # indexing at position 5, which is the sixth char
# Outpuy = 'r'
print(s[:4])   # slicing, we specify only the stop position
# Outpuy = 'The '
print(s[4:])   # slicing, we specify only the start position
# Outpuy = 'trouble is you think you have time.'
print(s[2:14])   # slicing, both start and stop positions
# Outpuy = 'e trouble is'
print(s[2:14:3])   # slicing, start, stop and step (every 3 chars)
# Outpuy = 'erb '
print(s[:])   # quick way of making a copy
# Outpuy = 'The trouble is you think you have time.'