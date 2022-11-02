# Graphknoten:

class Vertex(object):

    def __init__(self, name, **edges):
        self.name = name
        self.edges = edges

    def getName(self):
        return self.name

    def getEdges(self):
        edges = {key: val for key, val in sorted(self.edges.items(), key = lambda ele: ele[0])}
        return edges





