import math
import random
import copy
from matplotlib import pyplot

#load_data function saves coordinates to list named "c"
def load_data (input_data):
    c = []
    with open(input_data) as f:
        lines = f.readlines()
        for line in lines:
            line = line[:-2]
            line = line.split(";") 
            line[0] = float(line[0])
            line[1] = float(line[1])
            c.append(line)
    return c

#best insertion function uses only list of vertices V and list of coordinates c
def best_insertion(V,c):
    #first we create a list called "s" (state), which stores the information whether the vertices were already visited (V) or not (N)
    s = ['N'] * len(c)
    #and choose 3 random vertices to make initial triangle
    i1 = random.randint(0,len(c))
    i2 = random.randint(0,len(c))
    i3 = random.randint(0,len(c))
    #they are stored in Hamilton path
    k = [i1,i2,i3]
    #w is lenght of the path and its initial state is calculated by measuring distances in the triangle
    w = (math.sqrt((c[i1][0]-c[i2][0])**2 + (c[i1][1]-c[i2][1])**2))+math.sqrt((c[i2][0]-c[i3][0])**2 + (c[i2][1]-c[i3][1])**2)+math.sqrt((c[i1][0]-c[i3][0])**2 + (c[i1][1]-c[i3][1])**2)
    #we create ancillary list for vertices, that aren't part of the path yet
    V_rest = copy.copy(V)
    #simple cycle marks i1,i2 and i3 as visited and removes them from the list of remaining vertices
    for i in k:
        s[i]='V'
        V_rest.remove(i)
    #the cycle creates the path
    while 'N' in s:
        #a random vertex is chosen from the remaining vertices
        u = random.choice(V_rest)
        #minimal distance is set to infinite
        minW = math.inf
        #this cycle finds minimal distance from every i and i+1 vertices to find an optimal place in the path to put the u vertex
        for i in range(len(k)):
            v1 = k[i]
            #finding neighbouring vertex in the path
            if i+1 < len(k):
                v2 = k[i+1]
            else:
                v2 = k[0]
            #computing distance difference between the previous path and the new one (with u vertex)
            dist = (math.sqrt((c[u][0]-c[v1][0])**2 + (c[u][1]-c[v1][1])**2) + math.sqrt((c[u][0]-c[v2][0])**2 + (c[u][1]-c[v2][1])**2) - math.sqrt((c[v1][0]-c[v2][0])**2 + (c[v1][1]-c[v2][1])**2))
            #saving minimal distance difference and place to put the vertex in the Hamiltons path
            if dist < minW:
                minW=dist
                place = i+1
        #u is marked as visited
        s[u]='V'
        #u is inserted in the path list on the place we saved and is removed from the list of remaining points
        k.insert(place,u)
        V_rest.remove(u)
        #lenght of the path increases
        w=w+minW
    #in the end, the first vertex is copied to the end of the list to make a cycle
    k.append(k[0])
    return k,w

#this function visualise the graph and the path using matplotlib library
def plot(k,c):
    x = []
    y = []
    for u in k:
        x.append(c[u][0])
        y.append(c[u][1])
    pyplot.scatter(x, y)
    pyplot.plot(x, y)
    pyplot.show()

#here the data is loaded
input_data = "D:\\data_skola\\geoinformatika\\ukol_tsp\\data2.txt"
c = load_data(input_data)
#V stores number of every vertex in a list
V = [*range(0,len(c),1)]
#u is the starting point and it's optional

k, w = best_insertion(V,c)
print(w,k)
plot(k,c)