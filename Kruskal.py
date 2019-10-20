from math import sqrt
class UnionFind:
    def __init__(self, components_number):
        self.id = [x for x in range(components_number)]
        self.size = [1 for _ in range(components_number)]
        
    def rootOf(self, component):
        while (component != self.id[component]):
            #make every node in path point to its grandparent (thereby halving path length)
            self.id[component] = self.id[self.id[component]]
            component = self.id[component]
        return component
    
    def areConnected(self, p, q):
        return self.rootOf(p) == self.rootOf(q)
    
    def union(self, p, q):
        rootOfP = self.rootOf(p)
        rootOfQ = self.rootOf(q)
        # self.id[p] = rootOfQ
        if (rootOfP == rootOfQ):
            return
        elif self.size[rootOfP] < self.size[rootOfQ]:
            self.id[rootOfP] = rootOfQ
            self.size[rootOfQ] += self.size[rootOfP]
        else:
            self.id[rootOfQ] = rootOfP
            self.size[rootOfP] += self.size[rootOfQ]

class Vortex:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
    

class Edge:
    def __init__(self, source: Vortex, destination: Vortex):
        self.source = source
        self.destination = destination
        self.weight = sqrt(((source.x - destination.x) ** 2) + (((source.y - destination.y) ** 2)))

    def __str__(self):
        return ("{s} -- {d} == {w:.2f}".format(s=self.source.id, d=self.destination.id, w=self.weight))


class Graph:
    def __init__(self, verticesCount):
        self.verticesCount = verticesCount
        self.edges = []

    def addEdge(self,id, source, destination):
        self.edges.append(Edge(source, destination))

    def MST(self):
        result = []
        unionFind = UnionFind(self.verticesCount + 1)
        edgesCopy = sorted(self.edges, key = lambda edge: edge.weight)
        weight_sum = 0
        for count, edge in enumerate(edgesCopy):
            #Check if connecting edge will not cycle the tree (use union find)
            if not unionFind.areConnected(edge.source.id, edge.destination.id):
                unionFind.union(edge.source.id, edge.destination.id)
                weight_sum += edge.weight
                result.append(edge)
        for edge in result:
            print(edge)
        print("Total weight of minimal span tree: {w:.2f}".format(w=weight_sum))
        return


arrOfNodes = [ 
    [1, 10, 50],
    [2, 30, 56],
    [3, 45, 32],
    [4, 90, 23],
    [5, 44, 33],
]
numberOfNodes = len(arrOfNodes)
vertices = []
for node in arrOfNodes:
    id, x, y = node
    vertices.append(Vortex(id, x, y))

graph = Graph(numberOfNodes)

arrOfEdges = [
    [1, 1, 2],
    [2, 2, 3],
    [3, 3, 4],
    [4, 4, 5],
    [5, 5, 1],
    [6, 1, 3],
    [7, 1, 4],
    [8, 2, 3],
    [9, 2, 4],
    [10, 2, 5],
]
edges = []
for i in arrOfEdges:
    id, source, destination  = i
    graph.addEdge(id, vertices[source - 1], vertices[destination - 1])
graph.MST()




