from graph import *
from graph_csv import *
from priorityQueue import *


# # g = Graph(l,False)
# # g.addConnection("A","B", 3)
# # g.addConnection("A","C", 4)
# # g.addConnection("A","D", 1)
# # g.addConnection("B","D", 2)

# # # print(g.getWeightMatrix())


# # g2 = Graph(l, True)
# # g2.addConnection("A","B", 2)
# # g2.addConnection("B","D", 1)
# # g2.addConnection("D","C", 3)
# # g2.addConnection("A","C", 4)

# # print(g2.getWeightMatrix())

# # Aufgabe 2
# # g = readCSV("Graph.csv")
# # print(g.getWeightMatrix())
# # writeCSV("graph-output.csv",g)


# Aufgabe 3
def solvePrim(g, currentNodeName):
    pq = PriorityQueue()
    usedNodes = []

    currentNodeIndex = g.nodes.index(currentNodeName)
    edgeWeight = 0

    nextNodeName = currentNodeName

    # Einfügen in PQ erfolgt immer als Tuple (Distanz bzw. Kantengewicht, Knotenname)
    # Einfügen des Startknotens in die PQ. Jeder Startknoten hat zu sich selber die Distanz von 0
    pq.push((0, currentNodeName, nextNodeName))

    # Untergraph von G: MST, also gleiche Knotenmenge und in diesem Fall ungerichtet
    mst = Graph(g.nodes, False)

#count < len(g.nodes) - 1

    # Abbruchbedingung: PQ ist leer
    while(pq.queueLen() != 0):

        # Entfernen des ersten Elements
        y = pq.popQueue()
        if y[2] not in usedNodes:
            usedNodes.append(y[2])
            mst.addConnection(y[1], y[2], y[0])
        print("Used Nodes:", usedNodes)
        currentNodeName = y[2]
        currentNodeIndex = g.nodes.index(y[2])

        # Von dem Startknoten aus wird jeder Knoten der Knotenmenge von G durchlaufen
        for i in range(len(g.nodes)):

            # Wenn Kantengewicht nicht Unendlich (None) oder 0 ist (selber Knoten)
            # wird der Knoten ausgehend von dem aktuell betrachteten Knoten in die PQ eingefügt
            nextNodeName = g.nodes[i]
            edgeWeight = g.m[currentNodeIndex][i]

            if edgeWeight is not None and edgeWeight > 0 and nextNodeName not in usedNodes:
                pq.push((edgeWeight, currentNodeName, nextNodeName))

    return mst


g = readCSV("Graph3.csv")
mst = solvePrim(g, 'F')
print("MST:")
for i in mst.getWeightMatrix():
    print(i)

# nimmt Graphen und Startknoten als String an z.B. 'A'
