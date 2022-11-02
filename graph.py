class Graph(object):
    def __init__(self, nodes, direction):
        self.nodes = nodes
        self.nodes.sort()
        self.nodeCount = len(nodes)
        self.m = []
        self.direction = direction

        # Initialisiere alle Elemente der Matrix mit None
        for i in range(self.nodeCount):
            self.m.append([None for i in range(self.nodeCount)])
        
        # Setze Diagonalelemente auf 0
        for i in range(self.nodeCount):
            self.m[i][i] = 0

    def addConnection(self, n1, n2, weight):
        a = self.nodes.index(n1)
        b = self.nodes.index(n2)

        if self.direction == False:
            self.m[a][b] = weight
            self.m[b][a] = weight
        else:
            self.m[a][b] = weight

    def getWeightMatrix(self):
        return self.m

l = ["A","B","C","D"]

g = Graph(l,False)
g.addConnection("A","B", 3)
g.addConnection("A","C", 4)
g.addConnection("A","D", 1)
g.addConnection("B","D", 2)

# print(g.getWeightMatrix())


g2 = Graph(l, True)
g2.addConnection("A","B", 2)
g2.addConnection("B","D", 1)
g2.addConnection("D","C", 3)
g2.addConnection("A","C", 4)

print(g2.getWeightMatrix())