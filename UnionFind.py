
#Weighted union find with path compression
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
testUnion = UnionFind(10)
testUnion.union(0, 3)
testUnion.union(1,3)
testUnion.union(2,4)
testUnion.union(3, 2)
testUnion.union(6,4)
testUnion.union(7,4)


print(testUnion.rootOf(7))