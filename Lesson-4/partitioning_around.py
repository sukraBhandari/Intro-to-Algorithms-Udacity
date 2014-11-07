#
# Write partition to return a new array with 
# all values less then `v` to the left 
# and all values greater then `v` to the right
#

def partition(L, v):
    smaller = []
    bigger = []
    for each in L:
        if each < v:
            smaller.append(each)
        if each > v:
            bigger.append(each)
    # your code here
    return smaller+[v]+bigger

def rank(L, v):
    pos = 0
    for val in L:
        if val < v:
            pos += 1
    return pos

print partition([5, 78, 4, 44, 26, 18, 5], 44)
