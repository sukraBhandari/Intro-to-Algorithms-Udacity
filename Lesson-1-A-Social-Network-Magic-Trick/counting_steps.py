import math
def countdown(x):
    y = 0
    while x > 0:
        x = x - 5
        y = y + 1
    print y
def time(n):
    """ Return the number of steps 
    necessary to calculate"""
    print countdown(n)
    return 3 + 2*math.ceil(n/5.)
print time(50)
