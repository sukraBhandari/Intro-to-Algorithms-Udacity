# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

def find_eulerian_tour(graph):
    tour=[]
    first_element = graph[0][0]    
    find_tour(first_element,graph,tour)
    return tour
def find_tour(u,E,tour): 
    for (a,b) in E:
        if a==u:
            E.remove((a,b))
            find_tour(b,E,tour)
        elif b==u:
            E.remove((a,b))
            find_tour(a,E,tour)
    tour.insert(0,u)
    
print find_eulerian_tour([(1, 2), (2, 3), (3, 1), (3, 4), (4, 3)])   



