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

            if weight == "None":
                self.m[a][b] = None
                self.m[b][a] = None
            else:
                self.m[a][b] = int(weight)
                self.m[b][a] = int(weight)

        else:
            if weight == "None":
                self.m[a][b] = None
            else:
                self.m[a][b] = int(weight)
                

    def getWeightMatrix(self):
        return self.m


