# https://www.hackerrank.com/challenges/bfsshortreach
import sys

class Vertex(object):
    
    def __init__(self, data):
        self.data = data
        self.adj = dict() # vertex_object => distance
        
    def add_edge(self, w, distance=6):
        self.adj[w] = distance
    
    
class Graph(object):
    
    def __init__(self):
        self.vertices = dict() # data => vertex_object
    
    def add_vertex(self, data):
        self.vertices[data] = Vertex(data)
        
    def add_edge(self, f, t):
        if self.vertices.get(f) is None:
            self.vertices[f] = Vertex(f)
        if self.vertices.get(t) is None:
            self.vertices[t] = Vertex(t)
        self.vertices[f].add_edge(self.vertices[t])
        self.vertices[t].add_edge(self.vertices[f])

    def __iter__(self):
        return iter(v for k, v in sorted(self.vertices.items(), key=lambda x: x[0]))

    
def shortest_paths_from(g, s):
    distances = list()
    for v in g:
        if v.data == s:
            continue
        else:
            distances.append(shortest_path(g, g.vertices[s], v))
    return ' '.join(distances)
                
def shortest_path(g, f, t):
    visits = { v.data : False for v in iter(g) }
    queue = [ (f, 0) ] # insert left, remove right
    visits[f.data] = True
    distance = -1
    while distance == -1 and len(queue) > 0:
        v, dist = queue.pop()
        for w, edge_dist in v.adj.items():
            if not visits[w.data]:
                visits[w.data] = True
                new_dist = dist + edge_dist
                if w == t:
                    distance = new_dist
                queue.insert(0, (w, new_dist))
    return str(distance)
        
t = int(input())
for _ in range(t):
    n, m = [ int(i) for i in input().split(' ') ]
    g = Graph()
    for i in range(1,n+1):
        g.add_vertex(i)
    for i in range(m):
        fr, to = [ int(i) for i in input().split(' ') ]
        g.add_edge(fr, to)
    s = int(input())
    print(shortest_paths_from(g, s))


