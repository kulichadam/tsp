import math
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

#nearest_neighbor function uses "V" which is list of vertices, "c", and "u", which is the starting point and is chosen by user
def nearest_neighbor(V,c,u):
    #here we save the starting point
    first_point = u
    #create a list called "s" (state), which stores the information whether the vertices were already visited (V) or not (N)
    s = ['N'] * len(c)
    #and a list called k, which is the Hamilton path/cycle. It starts with the starting point
    k = []
    k.append(u)
    #w is the lenght of the path, which is zero while we're in the first vertex
    w = 0
    #the first vertex is marked as "V" - visited
    s[u] = 'V'
    #the cycle creates the path
    while 'N' in s:
        #minimal distance is set to infinite
        minW = math.inf
        ##the cycle calculates all distances from the last vertex to vertices marked as N and stores the vertex with minimal distance in nn
        for v in V:
            if s[v] == 'N':
                dist = math.sqrt((c[u][0]-c[v][0])**2 + (c[u][1]-c[v][1])**2)
                if dist < minW:
                    minW = dist
                    nn = v
        #next vertex is added to the Hamilton path, to the "u" variable and marked as Visited, lenght of the path is elongated by the minimal distance
        k.append(nn)
        u = nn
        s[u] = 'V'
        w = w + minW
    #after all vertices are in the path, we need to calculate distance back to the first vertex and finish the cycle
    distance_to_first = math.sqrt((c[u][0]-c[first_point][0])**2 + (c[u][1]-c[first_point][1])**2)
    k.append(first_point)
    w = w + distance_to_first
    return k, w

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
input_data = "D:\\data_skola\\geoinformatika\\ukol_tsp\\data1.txt"
c = load_data(input_data)
#V stores number of every vertex in a list
V = [*range(0,len(c),1)]
#u is the starting point and it's optional

u=22
k, w = nearest_neighbor(V,c,u)
print(w,k)
plot(k,c)

#this cycle prints w for every starting point u
"""
for v in V:
    u=v
    k, w = nearest_neighbor(V,c,u)
    print (w)
"""
