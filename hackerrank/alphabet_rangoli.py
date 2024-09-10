
# You are given an integer, . Your task is to print an alphabet rangoli of size . (Rangoli is a form of Indian folk art based on creation of patterns.)

# Different sizes of alphabet rangoli are shown below:

#size 3

# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----


def print_rangoli(size):
    start = 96
    ends = start+size
    # your code goes here
    for x in range(ends, start, -1):
        print("-"*(x-start+1),end="")
        for y in range(ends, x-1, -1):
            print(chr(y), end=" ")
        for z in range(ends, x, -1):
            # print("-"*(ends-x),end="")
            print(chr(z), end=" ")
        print()
    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)