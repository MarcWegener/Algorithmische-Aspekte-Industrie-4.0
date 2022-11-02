from vertex import *


class Graph(object):

    def __init__(self, nodes):
        self.nodes = nodes
        self.nodes.sort(key=lambda x:x.getName())
        

    def getWeightMatrix(self):
        weights = []

        for node in self.nodes:
            l = []
            for k, v in node.getEdges().items():
                if v == None:
                    l.append("N")
                else:
                    l.append(v)
            weights.append(l)

        return weights


v = [Vertex("B", A=5, D=None, B=0, E=None, C=1, F=2),Vertex("A", A=0, D=3, B=5, E=None, C=3, F=7),]
g = Graph(v)

for i in g.getWeightMatrix():
    print(i)
