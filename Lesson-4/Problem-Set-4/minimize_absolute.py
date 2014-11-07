#
# Given a list of numbers, L, find a number, x, that
# minimizes the sum of the absolute value of the difference
# between each element in L and x: SUM_{i=0}^{n-1} |L[i] - x|
# 
# Your code should run in Theta(n) time
#

def minimize_absolute(L):
    L2 = L[:]
    L2.sort()
    if len(L2) % 2 == 0:
        return (L2[(len(L2) - 1)/ 2] + L2[(len(L2) - 1)/ 2]) / 2.
    else:
        return L2[(len(L2) - 1)/ 2]
