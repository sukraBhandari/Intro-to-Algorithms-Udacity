#
# Given a list L of n numbers, find the mode 
# (the number that appears the most times).  
# Your algorithm should run in Theta(n).
# If there are ties - just pick one value to return 
#
from operator import itemgetter

def mode(L):
    counts = {}
    for each in L:
        if each not in counts:
            counts[each] = 0
        counts[each] += 1
    x = 0
    y = 0
    for each in counts:
        if counts[each] > x:
            x = counts[each]
            y = each
    return y

####
# Test
#
import time
from random import randint

def test():
    assert 5 == mode([1, 5, 2, 5, 3, 5])
    iterations = (10, 20, 30, 100, 200, 300, 1000, 5000, 10000, 20000, 30000)
    times = []
    for i in iterations:
        L = []
        for j in range(i):
            L.append(randint(1, 10))
        start = time.clock()
        for j in range(500):
            mode(L)
        end = time.clock()
        print start, end
        times.append(float(end - start))
    slopes = []
    for (x1, x2), (y1, y2) in zip(zip(iterations[:-1], iterations[1:]), zip(times[:-1], times[1:])):
        print (x1, x2), (y1, y2)
        slopes.append((y2 - y1) / (x2 - x1))
    # if mode runs in linear time, 
    # these factors should be close (kind of)
    print slopes

test()
                
