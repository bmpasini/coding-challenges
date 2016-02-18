# Enter your code here. Read input from STDIN. Print output to STDOUT

class Vertex:
    
    def __init__(self, data):
        self.data = data
        self.edges = dict()
        self.visited = False
    
    def add_edge(self, v, weight=0):
        self.edges[v] = weight

class Graph:
    
    def __init__(self):
        self.vertices = dict()
    
    def add_vertex(self, data):
        self.vertices[data] = Vertex(data)
    
    def add_edge(self, f, t, weight=0):
        if f not in self.vertices:
            self.add_vertex(f)
        if t not in self.vertices:
            self.add_vertex(t)
        vertices[f].add_edge(t, weigth)
        vertices[t].add_edge(f, weigth)

def shortest_path(g):
    
        
        
if __name__ == "__main__":
    m, n = ( int(i) for i in input().strip().split(' ') )
    
    g = Graph()
    
    for i in range(m):
        for j in range(n):
            square = i * m + j * n
            g.add_vertex(square)
    
    for i in range(m):
        for j, weight in enumerate(input().strip().split(' ')):
            f = i * m + j * n
            t = i * m + (j+1) * n
            g.add_edge(f, t, int(weight))
     
    for i in range(m-1):
        for j, weight in enumerate(input().strip().split(' ')):
            f = i * m + j * n
            t = (i+1) * m + j * n
            g.add_edge(f, t, int(weight))
            
    
        
        