# Eulerian Tour Ver 1
#
# Write a function, `create_tour` that takes as
# input a list of nodes
# and outputs a list of tuples representing
# edges between nodes that have an Eulerian tour.
#
import itertools
def create_tour(nodes):
    # your code here
    #print  [j for j in itertools.product(nodes,2)]
    lists=[]
    length = len(nodes)
    i=0
    while i<(length-1):
        lists.append( (nodes[i],nodes[(i+1)]) )
        i=i+1
    lists.append( (nodes[i],nodes[0]) )
    return lists
