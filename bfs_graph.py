class Vertex:
    def  __init__(self, n):
        self.name = n
        self.neighbors = list()
        self.distance = 9999
        self.color = 'black'

    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort() # sort it every time

class Graph:
    vertices = {}
    
    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False
            
    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)
            return True
        else:
            return False
    
    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors) + "  " 
            + str(self.vertices[key].distance))

    def bfs(self, vert):
        queue = list()
        vert.distance = 0
        vert.color = 'red'

        for v in vert.neighbors:
            self.vertices[v].distance = vert.distance + 1
            queue.append(v)
        
        while len(queue) > 0:
            u = queue.pop(0)
            node_u = self.vertices[u]
            node_u.color = 'red'

            for v in node_u.neighbors:
                node_v = self.vertices[v]
                if node_v.color == 'black':
                    queue.append(node_v)
                
                    if node_v.distance > node_u.distance + 1:
                        node_v.distance = node_u.distance +  1



### test code
g = Graph()
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('K')):
    g.add_vertex(Vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
    g.add_edge(edge[:1], edge[1:])
g.bfs(a)
g.print_graph()
        