"""
1
12
123
1234
12345
123456
1234567
"""

for x in range(1,8):
    for y in range(1,x+1):
        print(y, end="")
    print()